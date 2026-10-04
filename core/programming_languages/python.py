# core/programming_languages/python.py
# Python language configuration (v3.5.0)

"""
Python Language Configuration.

Provides tooling, linting, formatting, testing, and CI/CD configurations
for Python projects.

Official Resources:
- Website: https://www.python.org/
- Documentation: https://docs.python.org/3/

Introduced in v3.5.0.
"""

LANGUAGE_ID = "python"

LANGUAGE = {
    "name": "Python",
    "id": "python",
    "extensions": ["py", "pyi", "pyw"],
    "category": "tier-1",
    "official_website": "https://www.python.org/",
    "documentation_url": "https://docs.python.org/3/",

    # Package managers
    "package_managers": [
        {
            "name": "pip",
            "config_files": ["requirements.txt", "requirements-dev.txt"],
            "lock_file": None,
            "install_cmd": "pip install -r requirements.txt",
        },
        {
            "name": "poetry",
            "config_files": ["pyproject.toml"],
            "lock_file": "poetry.lock",
            "install_cmd": "poetry install",
        },
        {
            "name": "pipenv",
            "config_files": ["Pipfile"],
            "lock_file": "Pipfile.lock",
            "install_cmd": "pipenv install",
        },
        {
            "name": "uv",
            "config_files": ["pyproject.toml"],
            "lock_file": "uv.lock",
            "install_cmd": "uv sync",
        },
    ],

    # Linters
    "linters": [
        {
            "name": "ruff",
            "description": "Fast Python linter (recommended)",
            "config_files": ["ruff.toml", "pyproject.toml"],
            "command": "ruff check .",
        },
        {
            "name": "flake8",
            "description": "Style guide enforcement",
            "config_files": [".flake8", "setup.cfg", "tox.ini"],
            "command": "flake8 .",
        },
        {
            "name": "pylint",
            "description": "Comprehensive code analysis",
            "config_files": [".pylintrc", "pyproject.toml"],
            "command": "pylint src/",
        },
        {
            "name": "mypy",
            "description": "Static type checking",
            "config_files": ["mypy.ini", "pyproject.toml"],
            "command": "mypy src/",
        },
        {
            "name": "pyright",
            "description": "Fast type checking (Microsoft)",
            "config_files": ["pyrightconfig.json", "pyproject.toml"],
            "command": "pyright",
        },
    ],

    # Formatters
    "formatters": [
        {
            "name": "ruff",
            "description": "Fast formatter (recommended)",
            "command": "ruff format .",
        },
        {
            "name": "black",
            "description": "Opinionated formatter",
            "config_files": ["pyproject.toml"],
            "command": "black .",
        },
        {
            "name": "isort",
            "description": "Import sorting",
            "config_files": ["pyproject.toml", ".isort.cfg"],
            "command": "isort .",
        },
    ],

    # Test frameworks
    "test_frameworks": [
        {
            "name": "pytest",
            "description": "Feature-rich testing (recommended)",
            "config_files": ["pytest.ini", "pyproject.toml", "conftest.py"],
            "command": "pytest",
            "coverage_cmd": "pytest --cov=src --cov-report=xml",
        },
        {
            "name": "unittest",
            "description": "Standard library testing",
            "config_files": [],
            "command": "python -m unittest discover",
        },
    ],

    # Build tools
    "build_tools": [
        {
            "name": "setuptools",
            "config_files": ["setup.py", "setup.cfg", "pyproject.toml"],
        },
        {
            "name": "hatch",
            "config_files": ["pyproject.toml"],
        },
        {
            "name": "flit",
            "config_files": ["pyproject.toml"],
        },
    ],

    # Pre-commit hooks
    "precommit_hooks": [
        {
            "repo": "https://github.com/astral-sh/ruff-pre-commit",
            "hooks": ["ruff", "ruff-format"],
        },
        {
            "repo": "https://github.com/pre-commit/mirrors-mypy",
            "hooks": ["mypy"],
        },
        {
            "repo": "https://github.com/pycqa/isort",
            "hooks": ["isort"],
        },
    ],

    # CI workflow
    "ci_workflow": {
        "setup_steps": [
            "- uses: actions/setup-python@v5",
            "  with:",
            "    python-version: '3.x'",
        ],
        "install_steps": [
            "- run: pip install -r requirements.txt",
        ],
        "lint_steps": [
            "- run: ruff check .",
            "- run: ruff format --check .",
        ],
        "test_steps": [
            "- run: pytest --cov=src --cov-report=xml",
        ],
        "matrix": {
            "python-version": ["3.9", "3.10", "3.11", "3.12"],
        },
    },

    # Documentation
    "documentation_tools": [
        {"name": "Sphinx", "description": "Documentation generator"},
        {"name": "MkDocs", "description": "Markdown documentation"},
        {"name": "pdoc", "description": "Auto-generate API docs"},
    ],

    # Version requirements
    "minimum_version": "3.9",
    "recommended_version": "3.12",
}
