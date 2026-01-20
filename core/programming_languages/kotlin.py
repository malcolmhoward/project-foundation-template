# core/programming_languages/kotlin.py
# Kotlin language configuration (v3.5.0)

"""
Kotlin Language Configuration.

Provides tooling, linting, formatting, testing, and CI/CD configurations
for Kotlin projects.

Official Resources:
- Website: https://kotlinlang.org/
- Documentation: https://kotlinlang.org/docs/
- Kotlin Playground: https://play.kotlinlang.org/

Introduced in v3.5.0.
"""

LANGUAGE_ID = "kotlin"

LANGUAGE = {
    "name": "Kotlin",
    "id": "kotlin",
    "extensions": ["kt", "kts"],
    "category": "tier-3",
    "official_website": "https://kotlinlang.org/",
    "documentation_url": "https://kotlinlang.org/docs/",

    # Package managers (uses JVM ecosystem)
    "package_managers": [
        {
            "name": "gradle",
            "config_files": ["build.gradle.kts", "build.gradle"],
            "lock_file": "gradle.lockfile",
            "install_cmd": "gradle build",
        },
        {
            "name": "maven",
            "config_files": ["pom.xml"],
            "lock_file": None,
            "install_cmd": "mvn install",
        },
    ],

    # Linters
    "linters": [
        {
            "name": "detekt",
            "description": "Static code analysis (recommended)",
            "config_files": ["detekt.yml"],
            "command": "gradle detekt",
        },
        {
            "name": "ktlint",
            "description": "Style checker and formatter",
            "config_files": [".editorconfig"],
            "command": "ktlint",
        },
    ],

    # Formatters
    "formatters": [
        {
            "name": "ktlint",
            "description": "Kotlin linter and formatter (recommended)",
            "config_files": [".editorconfig"],
            "command": "ktlint -F",
        },
        {
            "name": "ktfmt",
            "description": "Kotlin formatter (Google)",
            "config_files": [],
            "command": "ktfmt --kotlinlang-style .",
        },
    ],

    # Test frameworks
    "test_frameworks": [
        {
            "name": "junit5",
            "description": "Standard testing (recommended)",
            "config_files": [],
            "command": "gradle test",
            "coverage_cmd": "gradle test jacocoTestReport",
        },
        {
            "name": "kotest",
            "description": "Kotlin-native testing",
            "config_files": [],
            "command": "gradle test",
        },
    ],

    # Build tools
    "build_tools": [
        {
            "name": "gradle",
            "config_files": ["build.gradle.kts", "build.gradle"],
            "description": "Build automation (recommended)",
        },
        {
            "name": "maven",
            "config_files": ["pom.xml"],
            "description": "Project management",
        },
    ],

    # Pre-commit hooks
    "precommit_hooks": [
        {
            "repo": "https://github.com/macisamuele/language-formatters-pre-commit-hooks",
            "hooks": ["pretty-format-kotlin"],
        },
    ],

    # CI workflow
    "ci_workflow": {
        "setup_steps": [
            "- uses: actions/setup-java@v4",
            "  with:",
            "    java-version: '21'",
            "    distribution: 'temurin'",
        ],
        "install_steps": [
            "- run: gradle build -x test",
        ],
        "lint_steps": [
            "- run: gradle detekt",
            "- run: ktlint",
        ],
        "test_steps": [
            "- run: gradle test",
        ],
        "matrix": {
            "java-version": ["17", "21"],
        },
    },

    # Documentation
    "documentation_tools": [
        {"name": "Dokka", "description": "Documentation engine for Kotlin"},
    ],

    # Kotlin-specific features
    "features": {
        "multiplatform": True,
        "coroutines": True,
        "compose": True,
        "targets": ["JVM", "JS", "Native", "WASM"],
    },
}
