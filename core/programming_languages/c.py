# core/programming_languages/c.py
# C language configuration (v3.5.0)

"""
C Language Configuration.

Provides tooling, linting, formatting, testing, and CI/CD configurations
for C projects.

Official Resources:
- ISO C Standard: https://www.iso.org/standard/74528.html
- cppreference: https://en.cppreference.com/w/c
- GCC: https://gcc.gnu.org/
- Clang: https://clang.llvm.org/

Introduced in v3.5.0.
"""

LANGUAGE_ID = "c"

LANGUAGE = {
    "name": "C",
    "id": "c",
    "extensions": ["c", "h"],
    "category": "tier-3",
    "official_website": "https://en.cppreference.com/w/c",
    "documentation_url": "https://en.cppreference.com/w/c",

    # Package managers
    "package_managers": [
        {
            "name": "vcpkg",
            "config_files": ["vcpkg.json"],
            "lock_file": None,
            "install_cmd": "vcpkg install",
        },
        {
            "name": "conan",
            "config_files": ["conanfile.txt", "conanfile.py"],
            "lock_file": "conan.lock",
            "install_cmd": "conan install .",
        },
    ],

    # Linters
    "linters": [
        {
            "name": "clang-tidy",
            "description": "Static analysis (recommended)",
            "config_files": [".clang-tidy"],
            "command": "clang-tidy src/*.c --",
        },
        {
            "name": "cppcheck",
            "description": "Static code analysis",
            "config_files": [],
            "command": "cppcheck --enable=all src/",
        },
    ],

    # Formatters
    "formatters": [
        {
            "name": "clang-format",
            "description": "Code formatter (recommended)",
            "config_files": [".clang-format"],
            "command": "clang-format -i src/*.c src/*.h",
        },
    ],

    # Test frameworks
    "test_frameworks": [
        {
            "name": "unity",
            "description": "Unit testing for C",
            "config_files": [],
            "command": "make test",
        },
        {
            "name": "cmocka",
            "description": "Unit testing with mocking",
            "config_files": [],
            "command": "make test",
        },
        {
            "name": "check",
            "description": "Unit testing framework",
            "config_files": [],
            "command": "make check",
        },
    ],

    # Build tools
    "build_tools": [
        {
            "name": "cmake",
            "config_files": ["CMakeLists.txt"],
            "description": "Cross-platform build system",
        },
        {
            "name": "make",
            "config_files": ["Makefile"],
            "description": "Traditional build tool",
        },
        {
            "name": "meson",
            "config_files": ["meson.build"],
            "description": "Modern build system",
        },
    ],

    # Pre-commit hooks
    "precommit_hooks": [
        {
            "repo": "https://github.com/pocc/pre-commit-hooks",
            "hooks": ["clang-format", "clang-tidy", "cppcheck"],
        },
    ],

    # CI workflow
    "ci_workflow": {
        "setup_steps": [
            "- run: sudo apt-get update && sudo apt-get install -y build-essential cmake",
        ],
        "install_steps": [
            "- run: mkdir -p build && cd build && cmake ..",
        ],
        "lint_steps": [
            "- run: clang-format --dry-run --Werror src/*.c src/*.h",
        ],
        "test_steps": [
            "- run: cd build && make && make test",
        ],
        "matrix": {
            "compiler": ["gcc", "clang"],
        },
    },

    # Documentation
    "documentation_tools": [
        {"name": "Doxygen", "description": "Documentation generator"},
    ],

    # C-specific features
    "features": {
        "standards": ["c99", "c11", "c17", "c23"],
        "compilers": ["gcc", "clang", "msvc"],
    },
}
