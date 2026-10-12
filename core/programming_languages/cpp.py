# core/programming_languages/cpp.py
# C++ language configuration (v3.5.0)

"""
C++ Language Configuration.

Provides tooling, linting, formatting, testing, and CI/CD configurations
for C++ projects.

Official Resources:
- ISO C++ Standard: https://isocpp.org/
- cppreference: https://en.cppreference.com/w/cpp
- GCC: https://gcc.gnu.org/
- Clang: https://clang.llvm.org/

Introduced in v3.5.0.
"""

LANGUAGE_ID = "cpp"

LANGUAGE = {
    "name": "C++",
    "id": "cpp",
    "extensions": ["cpp", "cc", "cxx", "hpp", "hh", "hxx", "h"],
    "category": "tier-3",
    "official_website": "https://isocpp.org/",
    "documentation_url": "https://en.cppreference.com/w/cpp",

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
            "command": "clang-tidy src/*.cpp --",
        },
        {
            "name": "cppcheck",
            "description": "Static code analysis",
            "config_files": [],
            "command": "cppcheck --enable=all --language=c++ src/",
        },
    ],

    # Formatters
    "formatters": [
        {
            "name": "clang-format",
            "description": "Code formatter (recommended)",
            "config_files": [".clang-format"],
            "command": "clang-format -i src/*.cpp src/*.hpp",
        },
    ],

    # Test frameworks
    "test_frameworks": [
        {
            "name": "googletest",
            "description": "Google Test (recommended)",
            "config_files": [],
            "command": "ctest --output-on-failure",
        },
        {
            "name": "catch2",
            "description": "Header-only testing",
            "config_files": [],
            "command": "ctest --output-on-failure",
        },
        {
            "name": "doctest",
            "description": "Fast header-only testing",
            "config_files": [],
            "command": "ctest --output-on-failure",
        },
    ],

    # Build tools
    "build_tools": [
        {
            "name": "cmake",
            "config_files": ["CMakeLists.txt"],
            "description": "Cross-platform build system (recommended)",
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
        {
            "name": "bazel",
            "config_files": ["BUILD", "WORKSPACE"],
            "description": "Scalable build system",
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
            "- run: clang-format --dry-run --Werror src/*.cpp src/*.hpp",
        ],
        "test_steps": [
            "- run: cd build && make && ctest --output-on-failure",
        ],
        "matrix": {
            "compiler": ["gcc", "clang"],
        },
    },

    # Documentation
    "documentation_tools": [
        {"name": "Doxygen", "description": "Documentation generator"},
    ],

    # C++-specific features
    "features": {
        "standards": ["c++14", "c++17", "c++20", "c++23"],
        "compilers": ["gcc", "clang", "msvc"],
        "modules": True,  # C++20
        "concepts": True,  # C++20
        "coroutines": True,  # C++20
    },
}
