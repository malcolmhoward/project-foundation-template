# core/programming_languages/gdscript.py
# GDScript language configuration (v3.5.0)

"""
GDScript Language Configuration.

Provides tooling, linting, formatting, testing, and CI/CD configurations
for GDScript (Godot Engine) projects.

Official Resources:
- Godot Engine: https://godotengine.org/
- GDScript Documentation: https://docs.godotengine.org/en/stable/tutorials/scripting/gdscript/
- Godot Asset Library: https://godotengine.org/asset-library/asset

Introduced in v3.5.0.
"""

LANGUAGE_ID = "gdscript"

LANGUAGE = {
    "name": "GDScript",
    "id": "gdscript",
    "extensions": ["gd", "tscn", "tres"],
    "category": "specialized",
    "official_website": "https://godotengine.org/",
    "documentation_url": "https://docs.godotengine.org/en/stable/tutorials/scripting/gdscript/",

    # Package managers
    "package_managers": [
        {
            "name": "godot asset library",
            "config_files": ["project.godot"],
            "lock_file": None,
            "install_cmd": None,  # GUI-based
        },
    ],

    # Linters
    "linters": [
        {
            "name": "gdlint",
            "description": "GDScript linter",
            "config_files": [".gdlintrc"],
            "command": "gdlint .",
        },
    ],

    # Formatters
    "formatters": [
        {
            "name": "gdformat",
            "description": "GDScript formatter",
            "config_files": [".gdformatrc"],
            "command": "gdformat -i .",
        },
    ],

    # Test frameworks
    "test_frameworks": [
        {
            "name": "gut",
            "description": "Godot Unit Test",
            "config_files": [".gutconfig.json"],
            "command": "godot --headless -s addons/gut/gut_cmdln.gd",
        },
        {
            "name": "gdunit4",
            "description": "GdUnit4 testing framework",
            "config_files": [],
            "command": "godot --headless -s addons/gdUnit4/runTest.gd",
        },
    ],

    # Build tools
    "build_tools": [
        {
            "name": "godot",
            "config_files": ["project.godot", "export_presets.cfg"],
            "description": "Godot export templates",
        },
    ],

    # Pre-commit hooks
    "precommit_hooks": [
        {
            "repo": "https://github.com/Scony/godot-gdscript-toolkit",
            "hooks": ["gdlint", "gdformat"],
        },
    ],

    # CI workflow
    "ci_workflow": {
        "setup_steps": [
            "- uses: chickensoft-games/setup-godot@v2",
            "  with:",
            "    version: '4.2'",
        ],
        "install_steps": [],
        "lint_steps": [
            "- run: pip install gdtoolkit && gdlint .",
        ],
        "test_steps": [
            "- run: godot --headless -s addons/gut/gut_cmdln.gd",
        ],
        "matrix": {
            "godot-version": ["4.2", "4.3"],
        },
    },

    # Documentation
    "documentation_tools": [
        {"name": "Godot Docs", "description": "In-engine documentation"},
    ],

    # GDScript-specific features
    "features": {
        "godot_version": "4.x",
        "typed_gdscript": True,
        "signals": True,
        "coroutines": True,
    },
}
