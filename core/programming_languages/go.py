# core/programming_languages/go.py
# Go language configuration (v3.5.0)

"""
Go Language Configuration.

Provides tooling, linting, formatting, testing, and CI/CD configurations
for Go projects.

Official Resources:
- Website: https://go.dev/
- Documentation: https://go.dev/doc/
- Package Index: https://pkg.go.dev/

Introduced in v3.5.0.
"""

LANGUAGE_ID = "go"

LANGUAGE = {
    "name": "Go",
    "id": "go",
    "extensions": ["go"],
    "category": "tier-2",
    "official_website": "https://go.dev/",
    "documentation_url": "https://go.dev/doc/",

    # Package managers
    "package_managers": [
        {
            "name": "go modules",
            "config_files": ["go.mod"],
            "lock_file": "go.sum",
            "install_cmd": "go mod download",
        },
    ],

    # Linters
    "linters": [
        {
            "name": "golangci-lint",
            "description": "Aggregated linter (recommended)",
            "config_files": [".golangci.yml", ".golangci.yaml"],
            "command": "golangci-lint run",
        },
        {
            "name": "go vet",
            "description": "Built-in static analysis",
            "config_files": [],
            "command": "go vet ./...",
        },
        {
            "name": "staticcheck",
            "description": "Advanced static analysis",
            "config_files": ["staticcheck.conf"],
            "command": "staticcheck ./...",
        },
    ],

    # Formatters
    "formatters": [
        {
            "name": "gofmt",
            "description": "Standard formatter (built-in)",
            "command": "gofmt -w .",
        },
        {
            "name": "goimports",
            "description": "Format and manage imports",
            "command": "goimports -w .",
        },
        {
            "name": "gofumpt",
            "description": "Stricter gofmt",
            "command": "gofumpt -w .",
        },
    ],

    # Test frameworks
    "test_frameworks": [
        {
            "name": "go test",
            "description": "Built-in testing (recommended)",
            "config_files": [],
            "command": "go test ./...",
            "coverage_cmd": "go test -coverprofile=coverage.out ./...",
        },
        {
            "name": "testify",
            "description": "Assertions and mocking",
            "config_files": [],
            "command": "go test ./...",
        },
    ],

    # Build tools
    "build_tools": [
        {
            "name": "go build",
            "config_files": ["go.mod"],
            "description": "Built-in compiler",
        },
        {
            "name": "goreleaser",
            "config_files": [".goreleaser.yml", ".goreleaser.yaml"],
            "description": "Release automation",
        },
        {
            "name": "mage",
            "config_files": ["magefile.go"],
            "description": "Make-like build tool",
        },
    ],

    # Pre-commit hooks
    "precommit_hooks": [
        {
            "repo": "https://github.com/golangci/golangci-lint",
            "hooks": ["golangci-lint"],
        },
        {
            "repo": "https://github.com/dnephin/pre-commit-golang",
            "hooks": ["go-fmt", "go-vet", "go-imports"],
        },
    ],

    # CI workflow
    "ci_workflow": {
        "setup_steps": [
            "- uses: actions/setup-go@v5",
            "  with:",
            "    go-version: '1.22'",
        ],
        "install_steps": [
            "- run: go mod download",
        ],
        "lint_steps": [
            "- run: golangci-lint run",
        ],
        "test_steps": [
            "- run: go test -v -coverprofile=coverage.out ./...",
        ],
        "matrix": {
            "go-version": ["1.21", "1.22"],
        },
    },

    # Documentation
    "documentation_tools": [
        {"name": "godoc", "description": "Built-in documentation"},
        {"name": "pkgsite", "description": "Package documentation"},
    ],

    # Go-specific features
    "features": {
        "modules": True,
        "generics": True,  # Go 1.18+
        "workspaces": True,  # Go 1.18+
    },
}
