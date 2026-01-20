# core/programming_languages/javascript.py
# JavaScript language configuration (v3.5.0)

"""
JavaScript Language Configuration.

Provides tooling, linting, formatting, testing, and CI/CD configurations
for JavaScript projects.

Official Resources:
- MDN Documentation: https://developer.mozilla.org/en-US/docs/Web/JavaScript
- ECMAScript Specification: https://tc39.es/ecma262/
- Node.js: https://nodejs.org/

Introduced in v3.5.0.
"""

LANGUAGE_ID = "javascript"

LANGUAGE = {
    "name": "JavaScript",
    "id": "javascript",
    "extensions": ["js", "mjs", "cjs", "jsx"],
    "category": "tier-1",
    "official_website": "https://developer.mozilla.org/en-US/docs/Web/JavaScript",
    "documentation_url": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide",
    "specification_url": "https://tc39.es/ecma262/",

    # Package managers
    "package_managers": [
        {
            "name": "npm",
            "config_files": ["package.json"],
            "lock_file": "package-lock.json",
            "install_cmd": "npm install",
        },
        {
            "name": "yarn",
            "config_files": ["package.json"],
            "lock_file": "yarn.lock",
            "install_cmd": "yarn install",
        },
        {
            "name": "pnpm",
            "config_files": ["package.json"],
            "lock_file": "pnpm-lock.yaml",
            "install_cmd": "pnpm install",
        },
        {
            "name": "bun",
            "config_files": ["package.json"],
            "lock_file": "bun.lockb",
            "install_cmd": "bun install",
        },
    ],

    # Linters
    "linters": [
        {
            "name": "eslint",
            "description": "Pluggable linter (recommended)",
            "config_files": ["eslint.config.js", ".eslintrc.js", ".eslintrc.json"],
            "command": "npx eslint .",
        },
        {
            "name": "biome",
            "description": "Fast linter and formatter",
            "config_files": ["biome.json"],
            "command": "npx biome check .",
        },
    ],

    # Formatters
    "formatters": [
        {
            "name": "prettier",
            "description": "Opinionated formatter (recommended)",
            "config_files": [".prettierrc", ".prettierrc.json", "prettier.config.js"],
            "command": "npx prettier --write .",
        },
        {
            "name": "biome",
            "description": "Fast formatter",
            "config_files": ["biome.json"],
            "command": "npx biome format --write .",
        },
    ],

    # Test frameworks
    "test_frameworks": [
        {
            "name": "jest",
            "description": "Full-featured testing (recommended)",
            "config_files": ["jest.config.js", "jest.config.json"],
            "command": "npx jest",
            "coverage_cmd": "npx jest --coverage",
        },
        {
            "name": "vitest",
            "description": "Fast Vite-native testing",
            "config_files": ["vitest.config.js", "vite.config.js"],
            "command": "npx vitest",
            "coverage_cmd": "npx vitest --coverage",
        },
        {
            "name": "mocha",
            "description": "Flexible testing framework",
            "config_files": [".mocharc.js", ".mocharc.json"],
            "command": "npx mocha",
        },
    ],

    # Build tools
    "build_tools": [
        {
            "name": "vite",
            "config_files": ["vite.config.js"],
        },
        {
            "name": "webpack",
            "config_files": ["webpack.config.js"],
        },
        {
            "name": "rollup",
            "config_files": ["rollup.config.js"],
        },
        {
            "name": "esbuild",
            "config_files": [],
        },
    ],

    # Pre-commit hooks
    "precommit_hooks": [
        {
            "repo": "https://github.com/pre-commit/mirrors-eslint",
            "hooks": ["eslint"],
        },
        {
            "repo": "https://github.com/pre-commit/mirrors-prettier",
            "hooks": ["prettier"],
        },
    ],

    # CI workflow
    "ci_workflow": {
        "setup_steps": [
            "- uses: actions/setup-node@v4",
            "  with:",
            "    node-version: '20'",
        ],
        "install_steps": [
            "- run: npm ci",
        ],
        "lint_steps": [
            "- run: npm run lint",
        ],
        "test_steps": [
            "- run: npm test",
        ],
        "matrix": {
            "node-version": ["18", "20", "22"],
        },
    },

    # Documentation
    "documentation_tools": [
        {"name": "JSDoc", "description": "API documentation"},
        {"name": "Storybook", "description": "Component documentation"},
        {"name": "TypeDoc", "description": "TypeScript documentation"},
    ],

    # Runtime environments
    "runtimes": ["Node.js", "Bun", "Deno", "Browser"],
}
