# core/plugins/__init__.py
# Plugin discovery and loading system

"""
Plugin system for Project Foundation Template.

This module provides a plugin system that allows users to extend the
foundation template with custom principles and guides without modifying
core code.

Quick Start:
    1. Create a plugin file in ~/.foundation-plugins/ or ./plugins/
    2. Define a class inheriting from PrinciplePlugin or GuidePlugin
    3. Use discover_plugins() to load and merge with built-in content

Example:
    # In ~/.foundation-plugins/my_principle.py
    from core.plugins import PrinciplePlugin

    class MyPrinciple(PrinciplePlugin):
        PRINCIPLE_ID = "my-custom-principle"
        PRINCIPLE = {
            "name": "My Custom Principle",
            "why": "Because it's important",
            "what": "What it covers",
            "risk": "Risk without it",
        }
        EDUCATION = "Educational content..."

    # In your code
    from core.plugins import discover_plugins, get_all_principles

    discover_plugins()  # Load plugins from default directories
    all_principles = get_all_principles()  # Includes plugin principles
"""

import os
from pathlib import Path
from typing import Dict, List, Optional, Type

from .base import PrinciplePlugin, GuidePlugin, PluginMetadata
from .validator import (
    ValidationResult,
    ValidationError,
    validate_plugin,
    validate_principle_plugin,
    validate_guide_plugin,
)
from .loader import (
    PluginLoader,
    PluginLoadError,
    PluginConflictError,
    LoadedPlugin,
    merge_principles,
    merge_education,
    merge_guides,
    merge_guide_content,
)


# Global plugin state
_loader: Optional[PluginLoader] = None
_plugins_loaded: bool = False


def get_plugin_dirs() -> List[Path]:
    """Get the list of directories to search for plugins.

    The search order is:
    1. Directory from FOUNDATION_PLUGINS_DIR environment variable (if set)
    2. ~/.foundation-plugins/
    3. ./plugins/ (relative to current working directory)

    Returns:
        List of Path objects for plugin directories.
    """
    dirs = []

    # Check environment variable first
    env_dir = os.environ.get("FOUNDATION_PLUGINS_DIR")
    if env_dir:
        dirs.append(Path(env_dir))

    # Default directories
    dirs.extend([
        Path.home() / ".foundation-plugins",
        Path.cwd() / "plugins",
    ])

    return dirs


def discover_plugins(
    plugin_dirs: Optional[List[Path]] = None,
    conflict_mode: str = "skip",
    reload: bool = False
) -> Dict[str, int]:
    """Discover and load plugins from directories.

    This function searches configured directories for plugin files,
    loads them, validates them, and makes them available for use.

    Args:
        plugin_dirs: List of directories to search. If None, uses
                    default directories (see get_plugin_dirs()).
        conflict_mode: How to handle ID conflicts with built-in items:
                      - 'error': Raise an exception
                      - 'override': User plugins override built-in
                      - 'skip': Skip conflicting plugins (default)
        reload: If True, reload plugins even if already loaded.

    Returns:
        Dict with counts: {'principles': N, 'guides': M, 'errors': E}

    Example:
        >>> result = discover_plugins()
        >>> print(f"Loaded {result['principles']} principles")
        Loaded 2 principles
    """
    global _loader, _plugins_loaded

    if _plugins_loaded and not reload:
        return {
            "principles": len(_loader.loaded_principles) if _loader else 0,
            "guides": len(_loader.loaded_guides) if _loader else 0,
            "errors": len(_loader.load_errors) if _loader else 0,
        }

    dirs = plugin_dirs if plugin_dirs is not None else get_plugin_dirs()
    _loader = PluginLoader(plugin_dirs=dirs, conflict_mode=conflict_mode)

    principles, guides = _loader.load_plugins()
    _plugins_loaded = True

    return {
        "principles": principles,
        "guides": guides,
        "errors": len(_loader.load_errors),
    }


def get_loaded_plugins() -> Dict[str, List[LoadedPlugin]]:
    """Get all loaded plugins.

    Returns:
        Dict with 'principles' and 'guides' keys, each containing
        a list of LoadedPlugin objects.
    """
    if _loader is None:
        return {"principles": [], "guides": []}

    return {
        "principles": list(_loader.loaded_principles.values()),
        "guides": list(_loader.loaded_guides.values()),
    }


def get_plugin_errors() -> List[PluginLoadError]:
    """Get any errors that occurred during plugin loading.

    Returns:
        List of PluginLoadError exceptions.
    """
    if _loader is None:
        return []
    return _loader.load_errors


def get_all_principles(include_builtin: bool = True) -> Dict[str, dict]:
    """Get all principles including plugins.

    Args:
        include_builtin: If True, include built-in principles.
                        If False, return only plugin principles.

    Returns:
        Dict mapping principle ID to principle dict.
    """
    # Import here to avoid circular imports
    from ..principles import ALL_PRINCIPLES

    plugin_principles = {}
    if _loader:
        for pid, loaded in _loader.loaded_principles.items():
            plugin_principles[pid] = loaded.plugin_class.PRINCIPLE.copy()

    if include_builtin:
        # Merge with plugins taking precedence (if they exist)
        result = ALL_PRINCIPLES.copy()
        result.update(plugin_principles)
        return result
    else:
        return plugin_principles


def get_all_education(include_builtin: bool = True) -> Dict[str, str]:
    """Get all education content including plugins.

    Args:
        include_builtin: If True, include built-in education.

    Returns:
        Dict mapping principle ID to education string.
    """
    from ..principles import ALL_EDUCATION

    plugin_education = {}
    if _loader:
        for pid, loaded in _loader.loaded_principles.items():
            plugin_education[pid] = loaded.plugin_class.EDUCATION

    if include_builtin:
        result = ALL_EDUCATION.copy()
        result.update(plugin_education)
        return result
    else:
        return plugin_education


def get_all_guides(include_builtin: bool = True) -> Dict[str, dict]:
    """Get all guides including plugins.

    Args:
        include_builtin: If True, include built-in guides.

    Returns:
        Dict mapping guide ID to guide dict.
    """
    from ..guides import ALL_GUIDES

    plugin_guides = {}
    if _loader:
        for gid, loaded in _loader.loaded_guides.items():
            plugin_guides[gid] = loaded.plugin_class.GUIDE.copy()

    if include_builtin:
        result = ALL_GUIDES.copy()
        result.update(plugin_guides)
        return result
    else:
        return plugin_guides


def get_all_guide_content(include_builtin: bool = True) -> Dict[str, str]:
    """Get all guide content including plugins.

    Args:
        include_builtin: If True, include built-in content.

    Returns:
        Dict mapping guide ID to content string.
    """
    from ..guides import ALL_GUIDE_CONTENT

    plugin_content = {}
    if _loader:
        for gid, loaded in _loader.loaded_guides.items():
            plugin_content[gid] = loaded.plugin_class.CONTENT

    if include_builtin:
        result = ALL_GUIDE_CONTENT.copy()
        result.update(plugin_content)
        return result
    else:
        return plugin_content


def list_plugin_principles() -> List[str]:
    """List IDs of all loaded principle plugins.

    Returns:
        List of principle IDs from plugins.
    """
    if _loader is None:
        return []
    return list(_loader.loaded_principles.keys())


def list_plugin_guides() -> List[str]:
    """List IDs of all loaded guide plugins.

    Returns:
        List of guide IDs from plugins.
    """
    if _loader is None:
        return []
    return list(_loader.loaded_guides.keys())


def is_plugin_principle(principle_id: str) -> bool:
    """Check if a principle ID is from a plugin.

    Args:
        principle_id: The principle ID to check.

    Returns:
        True if the principle is from a plugin.
    """
    if _loader is None:
        return False
    return principle_id in _loader.loaded_principles


def is_plugin_guide(guide_id: str) -> bool:
    """Check if a guide ID is from a plugin.

    Args:
        guide_id: The guide ID to check.

    Returns:
        True if the guide is from a plugin.
    """
    if _loader is None:
        return False
    return guide_id in _loader.loaded_guides


def get_plugin_metadata(plugin_id: str) -> Optional[PluginMetadata]:
    """Get metadata for a loaded plugin.

    Args:
        plugin_id: The principle or guide ID.

    Returns:
        PluginMetadata if available, None otherwise.
    """
    if _loader is None:
        return None

    if plugin_id in _loader.loaded_principles:
        return _loader.loaded_principles[plugin_id].metadata
    if plugin_id in _loader.loaded_guides:
        return _loader.loaded_guides[plugin_id].metadata
    return None


def reset_plugins() -> None:
    """Reset the plugin system state.

    This clears all loaded plugins and allows discover_plugins()
    to reload from scratch.
    """
    global _loader, _plugins_loaded
    if _loader:
        _loader.clear()
    _loader = None
    _plugins_loaded = False


def create_plugin_directory(
    path: Optional[Path] = None,
    create_example: bool = True
) -> Path:
    """Create a plugin directory with optional example file.

    Args:
        path: Directory to create. If None, uses ~/.foundation-plugins/
        create_example: If True, create an example plugin file.

    Returns:
        Path to the created directory.
    """
    if path is None:
        path = Path.home() / ".foundation-plugins"

    path.mkdir(parents=True, exist_ok=True)

    if create_example:
        example_path = path / "example_principle.py"
        if not example_path.exists():
            example_content = '''# Example custom principle plugin
# Place this file in ~/.foundation-plugins/ or ./plugins/

from core.plugins import PrinciplePlugin

# Optional: Plugin metadata (for display purposes)
PLUGIN_METADATA = {
    "name": "Example Plugin",
    "version": "1.0.0",
    "author": "Your Name",
    "description": "An example custom principle",
}


class ExamplePrinciple(PrinciplePlugin):
    """Example custom principle.

    This demonstrates how to create a custom principle plugin.
    Rename and modify this to create your own principles.
    """

    PRINCIPLE_ID = "example-custom-principle"

    PRINCIPLE = {
        "name": "Example Custom Principle",
        "why": "Demonstrates the plugin system",
        "what": "A template for creating custom principles",
        "risk": "Without customization, projects miss domain-specific guidance",
    }

    EDUCATION = """
    This is an example custom principle to demonstrate the plugin system.

    To create your own principle:
    1. Copy this file
    2. Update PRINCIPLE_ID (must be unique, lowercase with hyphens)
    3. Update PRINCIPLE dict with your principle's details
    4. Update EDUCATION with helpful content

    Your principle will be automatically loaded when you run the generator!
    """
'''
            example_path.write_text(example_content)

    return path


__all__ = [
    # Base classes
    "PrinciplePlugin",
    "GuidePlugin",
    "PluginMetadata",
    # Validation
    "ValidationResult",
    "ValidationError",
    "validate_plugin",
    "validate_principle_plugin",
    "validate_guide_plugin",
    # Loading
    "PluginLoader",
    "PluginLoadError",
    "PluginConflictError",
    "LoadedPlugin",
    # Main API
    "get_plugin_dirs",
    "discover_plugins",
    "get_loaded_plugins",
    "get_plugin_errors",
    "get_all_principles",
    "get_all_education",
    "get_all_guides",
    "get_all_guide_content",
    "list_plugin_principles",
    "list_plugin_guides",
    "is_plugin_principle",
    "is_plugin_guide",
    "get_plugin_metadata",
    "reset_plugins",
    "create_plugin_directory",
    # Merge utilities
    "merge_principles",
    "merge_education",
    "merge_guides",
    "merge_guide_content",
]
