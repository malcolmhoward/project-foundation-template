# core/programming_languages/typescript.py
# TypeScript language configuration (v3.5.0)

"""
TypeScript Language Configuration.

Provides tooling, linting, formatting, testing, and CI/CD configurations
for TypeScript projects.

Official Resources:
- Website: https://www.typescriptlang.org/
- Documentation: https://www.typescriptlang.org/docs/
- Playground: https://www.typescriptlang.org/play

Introduced in v3.5.0.
"""

LANGUAGE_ID = "typescript"

LANGUAGE = {
    "name": "TypeScript",
    "id": "typescript",
    "extensions": ["ts", "tsx", "mts", "cts"],
    "category": "tier-1",
    "official_website": "https://www.typescriptlang.org/",
    "documentation_url": "https://www.typescriptlang.org/docs/",

    # Package managers (same as JavaScript)
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

    # TypeScript-specific config
    "type_config": {
        "config_file": "tsconfig.json",
        "command": "npx tsc --noEmit",
    },

    # Linters
    "linters": [
        {
            "name": "eslint",
            "description": "Pluggable linter with TypeScript support",
            "config_files": ["eslint.config.js", ".eslintrc.js"],
            "command": "npx eslint . --ext .ts,.tsx",
        },
        {
            "name": "biome",
            "description": "Fast linter and formatter",
            "config_files": ["biome.json"],
            "command": "npx biome check .",
        },
        {
            "name": "typescript",
            "description": "Type checking (built-in)",
            "config_files": ["tsconfig.json"],
            "command": "npx tsc --noEmit",
        },
    ],

    # Formatters
    "formatters": [
        {
            "name": "prettier",
            "description": "Opinionated formatter (recommended)",
            "config_files": [".prettierrc", ".prettierrc.json"],
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
            "description": "Full-featured testing with ts-jest",
            "config_files": ["jest.config.ts", "jest.config.js"],
            "command": "npx jest",
            "coverage_cmd": "npx jest --coverage",
        },
        {
            "name": "vitest",
            "description": "Fast Vite-native testing (recommended)",
            "config_files": ["vitest.config.ts", "vite.config.ts"],
            "command": "npx vitest",
            "coverage_cmd": "npx vitest --coverage",
        },
    ],

    # Build tools
    "build_tools": [
        {
            "name": "tsc",
            "config_files": ["tsconfig.json"],
            "description": "TypeScript compiler",
        },
        {
            "name": "vite",
            "config_files": ["vite.config.ts"],
        },
        {
            "name": "esbuild",
            "config_files": [],
        },
        {
            "name": "swc",
            "config_files": [".swcrc"],
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
            "- run: npx tsc --noEmit",
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
        {"name": "TypeDoc", "description": "API documentation"},
        {"name": "Storybook", "description": "Component documentation"},
    ],

    # Runtime environments
    "runtimes": ["Node.js", "Bun", "Deno", "Browser"],
}
