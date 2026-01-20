# core/programming_languages/bash.py
# Bash language configuration (v3.5.0)

"""
Bash Language Configuration.

Provides tooling, linting, formatting, testing, and CI/CD configurations
for Bash/shell script projects.

Official Resources:
- Bash Reference Manual: https://www.gnu.org/software/bash/manual/
- POSIX Shell Specification: https://pubs.opengroup.org/onlinepubs/9699919799/utilities/V3_chap02.html

Introduced in v3.5.0.
"""

LANGUAGE_ID = "bash"

LANGUAGE = {
    "name": "Bash",
    "id": "bash",
    "extensions": ["sh", "bash", "zsh"],
    "category": "tier-3",
    "official_website": "https://www.gnu.org/software/bash/",
    "documentation_url": "https://www.gnu.org/software/bash/manual/",

    # Package managers (not applicable, but script managers exist)
    "package_managers": [],

    # Linters
    "linters": [
        {
            "name": "shellcheck",
            "description": "Static analysis (recommended)",
            "config_files": [".shellcheckrc"],
            "command": "shellcheck **/*.sh",
        },
    ],

    # Formatters
    "formatters": [
        {
            "name": "shfmt",
            "description": "Shell formatter (recommended)",
            "config_files": [".editorconfig"],
            "command": "shfmt -w .",
        },
    ],

    # Test frameworks
    "test_frameworks": [
        {
            "name": "bats",
            "description": "Bash Automated Testing System",
            "config_files": [],
            "command": "bats test/",
        },
        {
            "name": "shunit2",
            "description": "xUnit-based testing",
            "config_files": [],
            "command": "./test/run_tests.sh",
        },
    ],

    # Build tools (not typical for shell scripts)
    "build_tools": [
        {
            "name": "make",
            "config_files": ["Makefile"],
            "description": "Task automation",
        },
    ],

    # Pre-commit hooks
    "precommit_hooks": [
        {
            "repo": "https://github.com/koalaman/shellcheck-precommit",
            "hooks": ["shellcheck"],
        },
        {
            "repo": "https://github.com/scop/pre-commit-shfmt",
            "hooks": ["shfmt"],
        },
    ],

    # CI workflow
    "ci_workflow": {
        "setup_steps": [
            "- run: sudo apt-get update && sudo apt-get install -y shellcheck",
        ],
        "install_steps": [],
        "lint_steps": [
            "- run: shellcheck **/*.sh",
            "- run: shfmt -d .",
        ],
        "test_steps": [
            "- run: bats test/",
        ],
        "matrix": {},
    },

    # Documentation
    "documentation_tools": [
        {"name": "shdoc", "description": "Shell documentation generator"},
    ],

    # Bash-specific features
    "features": {
        "posix_compatible": True,
        "shells": ["bash", "zsh", "sh", "dash"],
        "shebang": "#!/usr/bin/env bash",
    },
}
