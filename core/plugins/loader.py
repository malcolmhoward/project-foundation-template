# core/plugins/loader.py
# Plugin loading and merging logic

"""
Plugin loader for Project Foundation Template.

This module handles discovering, loading, and merging plugins with
the built-in principles and guides.
"""

import importlib.util
import os
import sys
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Type, Any

from .base import PrinciplePlugin, GuidePlugin, PluginMetadata
from .validator import validate_plugin, ValidationResult


class PluginLoadError(Exception):
    """Raised when a plugin fails to load.

    Attributes:
        plugin_path: Path to the plugin file.
        reason: Description of why loading failed.
        validation_result: Optional validation result if validation failed.
    """

    def __init__(
        self,
        plugin_path: str,
        reason: str,
        validation_result: Optional[ValidationResult] = None
    ):
        self.plugin_path = plugin_path
        self.reason = reason
        self.validation_result = validation_result
        message = f"Failed to load plugin '{plugin_path}': {reason}"
        if validation_result and not validation_result.valid:
            message += f"\n{validation_result.format_errors()}"
        super().__init__(message)


class PluginConflictError(Exception):
    """Raised when plugins have conflicting IDs.

    Attributes:
        plugin_id: The conflicting ID.
        existing_source: Source of the existing plugin.
        new_source: Source of the new plugin.
    """

    def __init__(self, plugin_id: str, existing_source: str, new_source: str):
        self.plugin_id = plugin_id
        self.existing_source = existing_source
        self.new_source = new_source
        super().__init__(
            f"Plugin ID conflict: '{plugin_id}' exists in both "
            f"'{existing_source}' and '{new_source}'"
        )


class LoadedPlugin:
    """Container for a loaded plugin.

    Attributes:
        plugin_class: The plugin class.
        plugin_type: 'principle' or 'guide'.
        plugin_id: The plugin's unique ID.
        source_path: Path to the plugin file.
        metadata: Optional plugin metadata.
        validation: Validation result.
    """

    def __init__(
        self,
        plugin_class: type,
        plugin_type: str,
        plugin_id: str,
        source_path: str,
        metadata: Optional[PluginMetadata] = None,
        validation: Optional[ValidationResult] = None
    ):
        self.plugin_class = plugin_class
        self.plugin_type = plugin_type
        self.plugin_id = plugin_id
        self.source_path = source_path
        self.metadata = metadata
        self.validation = validation

    def __repr__(self) -> str:
        return f"LoadedPlugin({self.plugin_type}:{self.plugin_id} from {self.source_path})"


class PluginLoader:
    """Loads plugins from directories.

    This class handles discovering and loading plugin files from
    specified directories, validating them, and merging them with
    built-in principles and guides.

    Attributes:
        plugin_dirs: List of directories to search for plugins.
        loaded_principles: Dict of loaded principle plugins by ID.
        loaded_guides: Dict of loaded guide plugins by ID.
        conflict_mode: How to handle ID conflicts ('error', 'override', 'skip').
    """

    # Default plugin directories
    DEFAULT_DIRS = [
        Path.home() / ".foundation-plugins",
        Path.cwd() / "plugins",
    ]

    def __init__(
        self,
        plugin_dirs: Optional[List[Path]] = None,
        conflict_mode: str = "error"
    ):
        """Initialize the plugin loader.

        Args:
            plugin_dirs: List of directories to search for plugins.
                        If None, uses DEFAULT_DIRS.
            conflict_mode: How to handle ID conflicts:
                          - 'error': Raise PluginConflictError
                          - 'override': User plugins override built-in
                          - 'skip': Skip conflicting user plugins
        """
        self.plugin_dirs = plugin_dirs if plugin_dirs is not None else self.DEFAULT_DIRS
        self.conflict_mode = conflict_mode
        self.loaded_principles: Dict[str, LoadedPlugin] = {}
        self.loaded_guides: Dict[str, LoadedPlugin] = {}
        self._load_errors: List[PluginLoadError] = []

    @property
    def load_errors(self) -> List[PluginLoadError]:
        """Get list of errors that occurred during loading.

        Returns:
            List of PluginLoadError exceptions.
        """
        return self._load_errors.copy()

    def _find_plugin_files(self) -> List[Path]:
        """Find all Python files in plugin directories.

        Returns:
            List of paths to potential plugin files.
        """
        plugin_files = []
        for dir_path in self.plugin_dirs:
            if not dir_path.exists():
                continue
            if not dir_path.is_dir():
                continue
            # Find all .py files (not starting with _)
            for py_file in dir_path.glob("*.py"):
                if not py_file.name.startswith("_"):
                    plugin_files.append(py_file)
            # Also check subdirectories (one level deep)
            for subdir in dir_path.iterdir():
                if subdir.is_dir() and not subdir.name.startswith("_"):
                    for py_file in subdir.glob("*.py"):
                        if not py_file.name.startswith("_"):
                            plugin_files.append(py_file)
        return plugin_files

    def _load_module_from_file(self, file_path: Path) -> Any:
        """Load a Python module from a file path.

        Args:
            file_path: Path to the Python file.

        Returns:
            The loaded module.

        Raises:
            PluginLoadError: If the module cannot be loaded.
        """
        module_name = f"foundation_plugin_{file_path.stem}"
        spec = importlib.util.spec_from_file_location(module_name, file_path)
        if spec is None or spec.loader is None:
            raise PluginLoadError(str(file_path), "Cannot create module spec")

        module = importlib.util.module_from_spec(spec)
        # Temporarily add to sys.modules so relative imports work
        sys.modules[module_name] = module
        try:
            spec.loader.exec_module(module)
        except Exception as e:
            del sys.modules[module_name]
            raise PluginLoadError(str(file_path), f"Error executing module: {e}")

        return module

    def _extract_plugins_from_module(
        self,
        module: Any,
        file_path: Path
    ) -> Tuple[List[LoadedPlugin], List[PluginLoadError]]:
        """Extract plugin classes from a loaded module.

        Args:
            module: The loaded Python module.
            file_path: Path to the module file.

        Returns:
            Tuple of (list of loaded plugins, list of errors).
        """
        plugins = []
        errors = []

        # Get optional metadata from module
        metadata = None
        if hasattr(module, "PLUGIN_METADATA"):
            meta = module.PLUGIN_METADATA
            if isinstance(meta, dict):
                metadata = PluginMetadata(
                    name=meta.get("name", file_path.stem),
                    version=meta.get("version", "1.0.0"),
                    author=meta.get("author", ""),
                    description=meta.get("description", ""),
                    source_path=str(file_path),
                )
            elif isinstance(meta, PluginMetadata):
                metadata = meta
                metadata.source_path = str(file_path)

        # Look for plugin classes in the module
        for name in dir(module):
            if name.startswith("_"):
                continue

            obj = getattr(module, name)

            # Skip non-classes and base classes
            if not isinstance(obj, type):
                continue
            if obj in (PrinciplePlugin, GuidePlugin):
                continue

            # Check if it's a principle plugin
            if hasattr(obj, "PRINCIPLE_ID") and hasattr(obj, "PRINCIPLE"):
                validation = validate_plugin(obj, "principle")
                if validation.valid:
                    plugins.append(LoadedPlugin(
                        plugin_class=obj,
                        plugin_type="principle",
                        plugin_id=obj.PRINCIPLE_ID,
                        source_path=str(file_path),
                        metadata=metadata,
                        validation=validation,
                    ))
                else:
                    errors.append(PluginLoadError(
                        str(file_path),
                        f"Validation failed for principle '{obj.PRINCIPLE_ID}'",
                        validation
                    ))

            # Check if it's a guide plugin
            elif hasattr(obj, "GUIDE_ID") and hasattr(obj, "GUIDE"):
                validation = validate_plugin(obj, "guide")
                if validation.valid:
                    plugins.append(LoadedPlugin(
                        plugin_class=obj,
                        plugin_type="guide",
                        plugin_id=obj.GUIDE_ID,
                        source_path=str(file_path),
                        metadata=metadata,
                        validation=validation,
                    ))
                else:
                    errors.append(PluginLoadError(
                        str(file_path),
                        f"Validation failed for guide '{obj.GUIDE_ID}'",
                        validation
                    ))

        return plugins, errors

    def _handle_conflict(
        self,
        plugin: LoadedPlugin,
        existing: LoadedPlugin
    ) -> Optional[LoadedPlugin]:
        """Handle a plugin ID conflict.

        Args:
            plugin: The new plugin.
            existing: The existing plugin with same ID.

        Returns:
            The plugin to use, or None to skip.

        Raises:
            PluginConflictError: If conflict_mode is 'error'.
        """
        if self.conflict_mode == "error":
            raise PluginConflictError(
                plugin.plugin_id,
                existing.source_path,
                plugin.source_path
            )
        elif self.conflict_mode == "override":
            return plugin  # Use the new one
        else:  # skip
            return None  # Keep existing

    def load_plugins(self) -> Tuple[int, int]:
        """Load all plugins from configured directories.

        Returns:
            Tuple of (principles loaded, guides loaded).

        Note:
            Errors are collected in self._load_errors rather than raised,
            allowing partial loading to succeed.
        """
        self._load_errors = []
        principles_loaded = 0
        guides_loaded = 0

        plugin_files = self._find_plugin_files()

        for file_path in plugin_files:
            try:
                module = self._load_module_from_file(file_path)
                plugins, errors = self._extract_plugins_from_module(module, file_path)
                self._load_errors.extend(errors)

                for plugin in plugins:
                    if plugin.plugin_type == "principle":
                        if plugin.plugin_id in self.loaded_principles:
                            existing = self.loaded_principles[plugin.plugin_id]
                            try:
                                result = self._handle_conflict(plugin, existing)
                                if result is not None:
                                    self.loaded_principles[plugin.plugin_id] = result
                                    principles_loaded += 1
                            except PluginConflictError as e:
                                self._load_errors.append(
                                    PluginLoadError(plugin.source_path, str(e))
                                )
                        else:
                            self.loaded_principles[plugin.plugin_id] = plugin
                            principles_loaded += 1

                    elif plugin.plugin_type == "guide":
                        if plugin.plugin_id in self.loaded_guides:
                            existing = self.loaded_guides[plugin.plugin_id]
                            try:
                                result = self._handle_conflict(plugin, existing)
                                if result is not None:
                                    self.loaded_guides[plugin.plugin_id] = result
                                    guides_loaded += 1
                            except PluginConflictError as e:
                                self._load_errors.append(
                                    PluginLoadError(plugin.source_path, str(e))
                                )
                        else:
                            self.loaded_guides[plugin.plugin_id] = plugin
                            guides_loaded += 1

            except PluginLoadError as e:
                self._load_errors.append(e)

        return principles_loaded, guides_loaded

    def get_principle_plugins(self) -> Dict[str, Type[PrinciplePlugin]]:
        """Get all loaded principle plugin classes.

        Returns:
            Dict mapping principle ID to plugin class.
        """
        return {
            pid: lp.plugin_class
            for pid, lp in self.loaded_principles.items()
        }

    def get_guide_plugins(self) -> Dict[str, Type[GuidePlugin]]:
        """Get all loaded guide plugin classes.

        Returns:
            Dict mapping guide ID to plugin class.
        """
        return {
            gid: lg.plugin_class
            for gid, lg in self.loaded_guides.items()
        }

    def clear(self) -> None:
        """Clear all loaded plugins."""
        self.loaded_principles.clear()
        self.loaded_guides.clear()
        self._load_errors.clear()


def merge_principles(
    builtin: Dict[str, dict],
    plugins: Dict[str, Type[PrinciplePlugin]],
    conflict_mode: str = "error"
) -> Dict[str, dict]:
    """Merge built-in principles with plugin principles.

    Args:
        builtin: Dict of built-in principles (id -> principle dict).
        plugins: Dict of plugin classes (id -> class).
        conflict_mode: How to handle conflicts ('error', 'override', 'skip').

    Returns:
        Merged dict of all principles.

    Raises:
        PluginConflictError: If there's a conflict and mode is 'error'.
    """
    result = builtin.copy()

    for pid, plugin_class in plugins.items():
        if pid in result:
            if conflict_mode == "error":
                raise PluginConflictError(pid, "builtin", plugin_class.__name__)
            elif conflict_mode == "override":
                result[pid] = plugin_class.PRINCIPLE.copy()
            # skip: do nothing
        else:
            result[pid] = plugin_class.PRINCIPLE.copy()

    return result


def merge_education(
    builtin: Dict[str, str],
    plugins: Dict[str, Type[PrinciplePlugin]],
    conflict_mode: str = "error"
) -> Dict[str, str]:
    """Merge built-in education content with plugin education.

    Args:
        builtin: Dict of built-in education (id -> content).
        plugins: Dict of plugin classes (id -> class).
        conflict_mode: How to handle conflicts.

    Returns:
        Merged dict of all education content.
    """
    result = builtin.copy()

    for pid, plugin_class in plugins.items():
        if pid in result:
            if conflict_mode == "error":
                raise PluginConflictError(pid, "builtin", plugin_class.__name__)
            elif conflict_mode == "override":
                result[pid] = plugin_class.EDUCATION
        else:
            result[pid] = plugin_class.EDUCATION

    return result


def merge_guides(
    builtin: Dict[str, dict],
    plugins: Dict[str, Type[GuidePlugin]],
    conflict_mode: str = "error"
) -> Dict[str, dict]:
    """Merge built-in guides with plugin guides.

    Args:
        builtin: Dict of built-in guides (id -> guide dict).
        plugins: Dict of plugin classes (id -> class).
        conflict_mode: How to handle conflicts.

    Returns:
        Merged dict of all guides.
    """
    result = builtin.copy()

    for gid, plugin_class in plugins.items():
        if gid in result:
            if conflict_mode == "error":
                raise PluginConflictError(gid, "builtin", plugin_class.__name__)
            elif conflict_mode == "override":
                result[gid] = plugin_class.GUIDE.copy()
        else:
            result[gid] = plugin_class.GUIDE.copy()

    return result


def merge_guide_content(
    builtin: Dict[str, str],
    plugins: Dict[str, Type[GuidePlugin]],
    conflict_mode: str = "error"
) -> Dict[str, str]:
    """Merge built-in guide content with plugin content.

    Args:
        builtin: Dict of built-in content (id -> content).
        plugins: Dict of plugin classes (id -> class).
        conflict_mode: How to handle conflicts.

    Returns:
        Merged dict of all guide content.
    """
    result = builtin.copy()

    for gid, plugin_class in plugins.items():
        if gid in result:
            if conflict_mode == "error":
                raise PluginConflictError(gid, "builtin", plugin_class.__name__)
            elif conflict_mode == "override":
                result[gid] = plugin_class.CONTENT
        else:
            result[gid] = plugin_class.CONTENT

    return result


__all__ = [
    "PluginLoadError",
    "PluginConflictError",
    "LoadedPlugin",
    "PluginLoader",
    "merge_principles",
    "merge_education",
    "merge_guides",
    "merge_guide_content",
]
