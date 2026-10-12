# core/programming_languages/php.py
# PHP language configuration (v3.5.0)

"""
PHP Language Configuration.

Provides tooling, linting, formatting, testing, and CI/CD configurations
for PHP projects.

Official Resources:
- Website: https://www.php.net/
- Documentation: https://www.php.net/docs.php
- Packagist: https://packagist.org/

Introduced in v3.5.0.
"""

LANGUAGE_ID = "php"

LANGUAGE = {
    "name": "PHP",
    "id": "php",
    "extensions": ["php", "phtml"],
    "category": "tier-3",
    "official_website": "https://www.php.net/",
    "documentation_url": "https://www.php.net/docs.php",

    # Package managers
    "package_managers": [
        {
            "name": "composer",
            "config_files": ["composer.json"],
            "lock_file": "composer.lock",
            "install_cmd": "composer install",
        },
    ],

    # Linters
    "linters": [
        {
            "name": "phpstan",
            "description": "Static analysis (recommended)",
            "config_files": ["phpstan.neon", "phpstan.neon.dist"],
            "command": "vendor/bin/phpstan analyse",
        },
        {
            "name": "psalm",
            "description": "Static analysis",
            "config_files": ["psalm.xml"],
            "command": "vendor/bin/psalm",
        },
        {
            "name": "phpcs",
            "description": "Code style checker",
            "config_files": ["phpcs.xml", ".phpcs.xml"],
            "command": "vendor/bin/phpcs",
        },
    ],

    # Formatters
    "formatters": [
        {
            "name": "php-cs-fixer",
            "description": "Code style fixer (recommended)",
            "config_files": [".php-cs-fixer.php", ".php-cs-fixer.dist.php"],
            "command": "vendor/bin/php-cs-fixer fix",
        },
        {
            "name": "phpcbf",
            "description": "Code beautifier",
            "config_files": ["phpcs.xml"],
            "command": "vendor/bin/phpcbf",
        },
    ],

    # Test frameworks
    "test_frameworks": [
        {
            "name": "phpunit",
            "description": "Unit testing (recommended)",
            "config_files": ["phpunit.xml", "phpunit.xml.dist"],
            "command": "vendor/bin/phpunit",
            "coverage_cmd": "vendor/bin/phpunit --coverage-clover coverage.xml",
        },
        {
            "name": "pest",
            "description": "Modern testing framework",
            "config_files": ["phpunit.xml"],
            "command": "vendor/bin/pest",
        },
    ],

    # Build tools
    "build_tools": [
        {
            "name": "composer",
            "config_files": ["composer.json"],
            "description": "Dependency and autoload management",
        },
    ],

    # Pre-commit hooks
    "precommit_hooks": [
        {
            "repo": "https://github.com/digitalpulp/pre-commit-php",
            "hooks": ["php-lint", "php-cs-fixer"],
        },
    ],

    # CI workflow
    "ci_workflow": {
        "setup_steps": [
            "- uses: shivammathur/setup-php@v2",
            "  with:",
            "    php-version: '8.3'",
        ],
        "install_steps": [
            "- run: composer install --prefer-dist --no-progress",
        ],
        "lint_steps": [
            "- run: vendor/bin/phpstan analyse",
            "- run: vendor/bin/php-cs-fixer fix --dry-run --diff",
        ],
        "test_steps": [
            "- run: vendor/bin/phpunit",
        ],
        "matrix": {
            "php-version": ["8.1", "8.2", "8.3"],
        },
    },

    # Documentation
    "documentation_tools": [
        {"name": "phpDocumentor", "description": "API documentation"},
    ],

    # PHP-specific features
    "features": {
        "minimum_version": "8.1",
        "recommended_version": "8.3",
        "attributes": True,
        "enums": True,
        "fibers": True,
    },
}
