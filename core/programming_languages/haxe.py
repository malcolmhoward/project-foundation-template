# core/programming_languages/haxe.py
# Haxe language configuration (v3.5.0)

"""
Haxe Language Configuration.

Provides tooling, linting, formatting, testing, and CI/CD configurations
for Haxe projects.

Official Resources:
- Website: https://haxe.org/
- Documentation: https://haxe.org/documentation/
- Haxelib: https://lib.haxe.org/

Introduced in v3.5.0.
"""

LANGUAGE_ID = "haxe"

LANGUAGE = {
    "name": "Haxe",
    "id": "haxe",
    "extensions": ["hx", "hxml"],
    "category": "specialized",
    "official_website": "https://haxe.org/",
    "documentation_url": "https://haxe.org/documentation/",

    # Package managers
    "package_managers": [
        {
            "name": "haxelib",
            "config_files": ["haxelib.json"],
            "lock_file": None,
            "install_cmd": "haxelib install all",
        },
        {
            "name": "lix",
            "config_files": ["haxe_libraries/"],
            "lock_file": None,
            "install_cmd": "lix download",
        },
    ],

    # Linters
    "linters": [
        {
            "name": "haxe-checkstyle",
            "description": "Style checker",
            "config_files": ["checkstyle.json"],
            "command": "haxelib run checkstyle -s src",
        },
    ],

    # Formatters
    "formatters": [
        {
            "name": "haxe-formatter",
            "description": "Code formatter",
            "config_files": ["hxformat.json"],
            "command": "haxelib run formatter -s src",
        },
    ],

    # Test frameworks
    "test_frameworks": [
        {
            "name": "utest",
            "description": "Unit testing",
            "config_files": [],
            "command": "haxe test.hxml",
        },
        {
            "name": "munit",
            "description": "Massive Unit testing",
            "config_files": [],
            "command": "haxe test.hxml",
        },
        {
            "name": "buddy",
            "description": "BDD testing framework",
            "config_files": [],
            "command": "haxe test.hxml",
        },
    ],

    # Build tools
    "build_tools": [
        {
            "name": "haxe",
            "config_files": ["*.hxml", "build.hxml"],
            "description": "Haxe compiler",
        },
        {
            "name": "lime",
            "config_files": ["project.xml"],
            "description": "Cross-platform build tool",
        },
    ],

    # Pre-commit hooks
    "precommit_hooks": [],  # No standard pre-commit hooks

    # CI workflow
    "ci_workflow": {
        "setup_steps": [
            "- uses: krdlab/setup-haxe@v1",
            "  with:",
            "    haxe-version: '4.3.4'",
        ],
        "install_steps": [
            "- run: haxelib install all --always",
        ],
        "lint_steps": [
            "- run: haxelib run checkstyle -s src",
        ],
        "test_steps": [
            "- run: haxe test.hxml",
        ],
        "matrix": {
            "haxe-version": ["4.2", "4.3"],
        },
    },

    # Documentation
    "documentation_tools": [
        {"name": "dox", "description": "Haxe documentation generator"},
    ],

    # Haxe-specific features
    "features": {
        "targets": [
            "JavaScript",
            "C++",
            "C#",
            "Java",
            "JVM",
            "Python",
            "Lua",
            "PHP",
            "HashLink",
            "Neko",
        ],
        "macros": True,
        "abstract_types": True,
    },
}
