# core/programming_languages/swift.py
# Swift language configuration (v3.5.0)

"""
Swift Language Configuration.

Provides tooling, linting, formatting, testing, and CI/CD configurations
for Swift projects.

Official Resources:
- Website: https://www.swift.org/
- Documentation: https://www.swift.org/documentation/
- Swift Package Index: https://swiftpackageindex.com/

Introduced in v3.5.0.
"""

LANGUAGE_ID = "swift"

LANGUAGE = {
    "name": "Swift",
    "id": "swift",
    "extensions": ["swift"],
    "category": "tier-3",
    "official_website": "https://www.swift.org/",
    "documentation_url": "https://www.swift.org/documentation/",

    # Package managers
    "package_managers": [
        {
            "name": "swift package manager",
            "config_files": ["Package.swift"],
            "lock_file": "Package.resolved",
            "install_cmd": "swift package resolve",
        },
        {
            "name": "cocoapods",
            "config_files": ["Podfile"],
            "lock_file": "Podfile.lock",
            "install_cmd": "pod install",
        },
    ],

    # Linters
    "linters": [
        {
            "name": "swiftlint",
            "description": "Style and conventions (recommended)",
            "config_files": [".swiftlint.yml"],
            "command": "swiftlint",
        },
    ],

    # Formatters
    "formatters": [
        {
            "name": "swift-format",
            "description": "Official formatter",
            "config_files": [".swift-format"],
            "command": "swift-format -r -i .",
        },
        {
            "name": "swiftformat",
            "description": "Community formatter",
            "config_files": [".swiftformat"],
            "command": "swiftformat .",
        },
    ],

    # Test frameworks
    "test_frameworks": [
        {
            "name": "xctest",
            "description": "Built-in testing",
            "config_files": [],
            "command": "swift test",
            "coverage_cmd": "swift test --enable-code-coverage",
        },
        {
            "name": "quick",
            "description": "BDD testing framework",
            "config_files": [],
            "command": "swift test",
        },
    ],

    # Build tools
    "build_tools": [
        {
            "name": "swift build",
            "config_files": ["Package.swift"],
            "description": "Built-in build system",
        },
        {
            "name": "xcodebuild",
            "config_files": ["*.xcodeproj", "*.xcworkspace"],
            "description": "Xcode build tool",
        },
    ],

    # Pre-commit hooks
    "precommit_hooks": [
        {
            "repo": "https://github.com/realm/SwiftLint",
            "hooks": ["swiftlint"],
        },
    ],

    # CI workflow
    "ci_workflow": {
        "setup_steps": [
            "- uses: swift-actions/setup-swift@v2",
            "  with:",
            "    swift-version: '5.10'",
        ],
        "install_steps": [
            "- run: swift package resolve",
        ],
        "lint_steps": [
            "- run: swiftlint",
        ],
        "test_steps": [
            "- run: swift test",
        ],
        "matrix": {
            "swift-version": ["5.9", "5.10"],
        },
    },

    # Documentation
    "documentation_tools": [
        {"name": "DocC", "description": "Apple documentation compiler"},
        {"name": "Jazzy", "description": "Documentation generator"},
    ],

    # Swift-specific features
    "features": {
        "minimum_version": "5.9",
        "recommended_version": "5.10",
        "concurrency": True,
        "macros": True,  # Swift 5.9+
        "observation": True,  # Swift 5.9+
    },
}
