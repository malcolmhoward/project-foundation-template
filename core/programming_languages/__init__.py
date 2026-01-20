# core/programming_languages/__init__.py
# Programming language support infrastructure (v3.5.0)

"""
Programming Language Support Infrastructure.

Provides language-specific configurations for tooling, linting, formatting,
testing, and CI/CD workflows. Each language module defines common patterns
and recommended tools for that language ecosystem.

Note: This module is named 'programming_languages' to distinguish it from
spoken/written language support in the internationalization module.

Introduced in v3.5.0.
"""

from typing import Dict, List, Any

# Import all language configurations
from . import python
from . import javascript
from . import typescript
from . import go
from . import rust
from . import java
from . import csharp
from . import c
from . import cpp
from . import php
from . import ruby
from . import swift
from . import kotlin
from . import bash
from . import gdscript
from . import lua
from . import haxe
from . import scala

# Language module registry
LANGUAGE_MODULES = {
    "python": python,
    "javascript": javascript,
    "typescript": typescript,
    "go": go,
    "rust": rust,
    "java": java,
    "csharp": csharp,
    "c": c,
    "cpp": cpp,
    "php": php,
    "ruby": ruby,
    "swift": swift,
    "kotlin": kotlin,
    "bash": bash,
    "gdscript": gdscript,
    "lua": lua,
    "haxe": haxe,
    "scala": scala,
}

# All language configurations
ALL_LANGUAGES: Dict[str, Dict[str, Any]] = {
    lang_id: module.LANGUAGE
    for lang_id, module in LANGUAGE_MODULES.items()
}

# Language categories for organization
TIER_1_LANGUAGES = ["python", "javascript", "typescript"]
TIER_2_LANGUAGES = ["go", "rust", "java", "csharp"]
TIER_3_LANGUAGES = ["c", "cpp", "php", "ruby", "swift", "kotlin", "bash", "scala"]
SPECIALIZED_LANGUAGES = ["gdscript", "lua", "haxe"]


def get_language(language_id: str) -> Dict[str, Any]:
    """Get language configuration by ID."""
    if language_id not in ALL_LANGUAGES:
        raise ValueError(f"Unknown language: {language_id}")
    return ALL_LANGUAGES[language_id]


def get_languages_by_extension(extension: str) -> List[str]:
    """Find languages that use a given file extension."""
    extension = extension.lstrip(".")
    matches = []
    for lang_id, config in ALL_LANGUAGES.items():
        if extension in config.get("extensions", []):
            matches.append(lang_id)
    return matches


def get_all_extensions() -> Dict[str, str]:
    """Get a mapping of all extensions to their primary language."""
    extensions = {}
    for lang_id, config in ALL_LANGUAGES.items():
        for ext in config.get("extensions", []):
            if ext not in extensions:  # First language wins
                extensions[ext] = lang_id
    return extensions


def get_tools_for_language(language_id: str) -> Dict[str, Any]:
    """Get all tools configuration for a language."""
    config = get_language(language_id)
    return {
        "linters": config.get("linters", []),
        "formatters": config.get("formatters", []),
        "test_frameworks": config.get("test_frameworks", []),
        "package_managers": config.get("package_managers", []),
        "build_tools": config.get("build_tools", []),
    }


def get_precommit_hooks(language_id: str) -> List[Dict[str, Any]]:
    """Get pre-commit hook configurations for a language."""
    config = get_language(language_id)
    return config.get("precommit_hooks", [])


def get_ci_workflow(language_id: str) -> Dict[str, Any]:
    """Get CI workflow configuration for a language."""
    config = get_language(language_id)
    return config.get("ci_workflow", {})


# Utility functions for multi-language projects
def detect_languages(file_paths: List[str]) -> Dict[str, int]:
    """Detect languages used in a project based on file paths."""
    extension_map = get_all_extensions()
    language_counts: Dict[str, int] = {}

    for path in file_paths:
        ext = path.rsplit(".", 1)[-1] if "." in path else ""
        if ext in extension_map:
            lang = extension_map[ext]
            language_counts[lang] = language_counts.get(lang, 0) + 1

    return language_counts


def get_recommended_tools(languages: List[str]) -> Dict[str, List[str]]:
    """Get recommended tools for a set of languages."""
    all_linters: set[str] = set()
    all_formatters: set[str] = set()
    all_test_frameworks: set[str] = set()

    for lang_id in languages:
        if lang_id in ALL_LANGUAGES:
            tools = get_tools_for_language(lang_id)
            for linter in tools["linters"]:
                all_linters.add(linter["name"])
            for formatter in tools["formatters"]:
                all_formatters.add(formatter["name"])
            for framework in tools["test_frameworks"]:
                all_test_frameworks.add(framework["name"])

    return {
        "linters": list(all_linters),
        "formatters": list(all_formatters),
        "test_frameworks": list(all_test_frameworks),
    }
