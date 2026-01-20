# core/programming_languages/java.py
# Java language configuration (v3.5.0)

"""
Java Language Configuration.

Provides tooling, linting, formatting, testing, and CI/CD configurations
for Java projects.

Official Resources:
- Website: https://www.java.com/
- Documentation: https://docs.oracle.com/en/java/
- OpenJDK: https://openjdk.org/

Introduced in v3.5.0.
"""

LANGUAGE_ID = "java"

LANGUAGE = {
    "name": "Java",
    "id": "java",
    "extensions": ["java"],
    "category": "tier-2",
    "official_website": "https://www.java.com/",
    "documentation_url": "https://docs.oracle.com/en/java/",

    # Package managers / Build tools
    "package_managers": [
        {
            "name": "maven",
            "config_files": ["pom.xml"],
            "lock_file": None,
            "install_cmd": "mvn install",
        },
        {
            "name": "gradle",
            "config_files": ["build.gradle", "build.gradle.kts"],
            "lock_file": "gradle.lockfile",
            "install_cmd": "gradle build",
        },
    ],

    # Linters
    "linters": [
        {
            "name": "checkstyle",
            "description": "Code style checker",
            "config_files": ["checkstyle.xml"],
            "command": "mvn checkstyle:check",
        },
        {
            "name": "spotbugs",
            "description": "Bug pattern detection",
            "config_files": ["spotbugs-exclude.xml"],
            "command": "mvn spotbugs:check",
        },
        {
            "name": "pmd",
            "description": "Source code analyzer",
            "config_files": ["pmd-ruleset.xml"],
            "command": "mvn pmd:check",
        },
    ],

    # Formatters
    "formatters": [
        {
            "name": "google-java-format",
            "description": "Google style formatter",
            "command": "google-java-format --replace src/**/*.java",
        },
        {
            "name": "spotless",
            "description": "Multi-format code formatter",
            "config_files": ["build.gradle"],
            "command": "gradle spotlessApply",
        },
    ],

    # Test frameworks
    "test_frameworks": [
        {
            "name": "junit5",
            "description": "Standard testing (recommended)",
            "config_files": [],
            "command": "mvn test",
            "coverage_cmd": "mvn jacoco:report",
        },
        {
            "name": "testng",
            "description": "Advanced testing framework",
            "config_files": ["testng.xml"],
            "command": "mvn test",
        },
    ],

    # Build tools
    "build_tools": [
        {
            "name": "maven",
            "config_files": ["pom.xml"],
            "description": "Project management and build",
        },
        {
            "name": "gradle",
            "config_files": ["build.gradle", "build.gradle.kts"],
            "description": "Build automation",
        },
    ],

    # Pre-commit hooks
    "precommit_hooks": [
        {
            "repo": "https://github.com/macisamuele/language-formatters-pre-commit-hooks",
            "hooks": ["pretty-format-java"],
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
            "- run: mvn install -DskipTests",
        ],
        "lint_steps": [
            "- run: mvn checkstyle:check",
        ],
        "test_steps": [
            "- run: mvn test",
        ],
        "matrix": {
            "java-version": ["17", "21"],
        },
    },

    # Documentation
    "documentation_tools": [
        {"name": "Javadoc", "description": "API documentation"},
    ],

    # Java-specific features
    "features": {
        "lts_versions": ["17", "21"],
        "modules": True,  # Java 9+
        "records": True,  # Java 14+
        "pattern_matching": True,  # Java 21+
    },
}
