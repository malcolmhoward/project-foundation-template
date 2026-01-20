# core/programming_languages/rust.py
# Rust language configuration (v3.5.0)

"""
Rust Language Configuration.

Provides tooling, linting, formatting, testing, and CI/CD configurations
for Rust projects.

Official Resources:
- Website: https://www.rust-lang.org/
- Documentation: https://doc.rust-lang.org/
- Package Registry: https://crates.io/

Introduced in v3.5.0.
"""

LANGUAGE_ID = "rust"

LANGUAGE = {
    "name": "Rust",
    "id": "rust",
    "extensions": ["rs"],
    "category": "tier-2",
    "official_website": "https://www.rust-lang.org/",
    "documentation_url": "https://doc.rust-lang.org/",

    # Package managers
    "package_managers": [
        {
            "name": "cargo",
            "config_files": ["Cargo.toml"],
            "lock_file": "Cargo.lock",
            "install_cmd": "cargo build",
        },
    ],

    # Linters
    "linters": [
        {
            "name": "clippy",
            "description": "Official linter (recommended)",
            "config_files": ["clippy.toml", ".clippy.toml"],
            "command": "cargo clippy -- -D warnings",
        },
        {
            "name": "rust-analyzer",
            "description": "IDE support with diagnostics",
            "config_files": ["rust-analyzer.toml"],
            "command": None,  # IDE-only
        },
    ],

    # Formatters
    "formatters": [
        {
            "name": "rustfmt",
            "description": "Official formatter (recommended)",
            "config_files": ["rustfmt.toml", ".rustfmt.toml"],
            "command": "cargo fmt",
        },
    ],

    # Test frameworks
    "test_frameworks": [
        {
            "name": "cargo test",
            "description": "Built-in testing (recommended)",
            "config_files": [],
            "command": "cargo test",
            "coverage_cmd": "cargo tarpaulin --out Xml",
        },
        {
            "name": "nextest",
            "description": "Fast test runner",
            "config_files": [".config/nextest.toml"],
            "command": "cargo nextest run",
        },
    ],

    # Build tools
    "build_tools": [
        {
            "name": "cargo",
            "config_files": ["Cargo.toml"],
            "description": "Built-in build system",
        },
        {
            "name": "cargo-make",
            "config_files": ["Makefile.toml"],
            "description": "Task runner",
        },
    ],

    # Pre-commit hooks
    "precommit_hooks": [
        {
            "repo": "https://github.com/doublify/pre-commit-rust",
            "hooks": ["fmt", "cargo-check", "clippy"],
        },
    ],

    # CI workflow
    "ci_workflow": {
        "setup_steps": [
            "- uses: dtolnay/rust-toolchain@stable",
            "  with:",
            "    components: clippy, rustfmt",
        ],
        "install_steps": [
            "- run: cargo fetch",
        ],
        "lint_steps": [
            "- run: cargo fmt --all -- --check",
            "- run: cargo clippy -- -D warnings",
        ],
        "test_steps": [
            "- run: cargo test",
        ],
        "matrix": {
            "rust-version": ["stable", "beta"],
        },
    },

    # Documentation
    "documentation_tools": [
        {"name": "rustdoc", "description": "Built-in documentation"},
        {"name": "mdbook", "description": "Book-style documentation"},
    ],

    # Rust-specific features
    "features": {
        "editions": ["2018", "2021", "2024"],
        "cargo_features": True,
        "workspaces": True,
    },
}
