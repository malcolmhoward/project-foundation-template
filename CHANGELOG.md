# Changelog

All notable changes to Project Foundation Template will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- (Upcoming features will be listed here)

## [3.7.0] - Unreleased

Versions 2.4.0 through 3.6.0 were developed as a chain of pull requests and ship together
in 3.7.0. Changes are grouped by the version that introduced them.

### Added
- **2.4.0**: Comprehensive SECURITY.md generation (`--include-enhanced-security`) and a
  pre-commit secrets-detection setup (`--include-secrets-detection`); principles
  `enhanced-security` and `secrets-detection`.
- **2.5.0**: Architecture Decision Record templates (`--include-adr`) and a GitHub Actions CI
  workflow (`--include-ci`); principles `adr` and `ci-workflow`; first smoke tests.
- **2.6.0**: The generator is now a Python package (`core/`) instead of a single file.
- **2.7.0**: Governance presets: `minimal` (3 principles), `light` (6), `standard` (9, default),
  `strict` (12) and `enterprise` (all 30).
- **2.8.0 / 2.9.0**: One module per principle (`core/principles/`) and implementation guides
  (`core/guides/`, 6 at first).
- **2.11.0**: Plugin API (`core/plugins/`) for custom principles and guides.
- **3.0.0**: New entry point `generate_foundation.py` with `--preset`, `--list-presets`,
  `--list-principles` and `--list-guides`; 11 principles (quality, compliance, infrastructure,
  inclusivity, lifecycle) and 9 guides.
- **3.1.0**: Accessibility and usability features; principles `glossary` and `maintainers`;
  scaffold manifest.
- **3.2.0**: 4 developer documentation guides.
- **3.3.0**: Principles `roadmap`, `branch-naming` and `conventional-commits`.
- **3.4.0**: Principles `pre-commit-hooks` and `error-handling`, and 6 guides (30 principles and
  25 guides in total).
- **3.5.0**: 18 programming-language configurations (`core/programming_languages/`). Available
  through the Python API; not yet selectable from the command line.
- **3.6.0**: 10 locale configurations (`core/internationalization/`). Available through the
  Python API; not yet selectable from the command line.
- **3.7.0**: Generation log (`--include-generation-log`, `--log-format md|json|both`,
  `--log-to`), `validate_customization.py`, ACKNOWLEDGMENTS.md and a tiered ethical review
  process.

### Changed
- `setup_foundation_lite.py` is now a compatibility shim: it runs `generate_foundation.py` with
  the same arguments and needs the full repository (see MIGRATION.md).
- Generated templates no longer contain emoji in headings, and README code blocks are no longer
  written with escaped backticks.
- The generation log records files by path relative to the output directory
  (for example `.github/workflows/ci.yml`).
- The advisory expiration date is now 2027-04-01.

### Deprecated
- `setup_foundation_lite.py`; call `generate_foundation.py` instead.

### Fixed
- The README Quick Start pointed to a script that does not exist.
- A generated GENERATION_LOG failed `validate_customization.py --strict`.
- `--log-to` with `--log-format both` could overwrite the other format's existing log; an
  unreadable JSON log is now backed up instead of replaced.
- The enterprise preset enabled 23 of 30 principles; `--list-principles` and `--list-guides`
  showed only part of each catalogue.
- Smoke tests no longer write to the real `~/.project_foundation_logs`.

### Removed
- The stale `foundation/` package, left behind by the rename to `core/`.

### Security
- Plugins are no longer discovered in `./plugins/` of the current directory by default, so
  running the generator inside an untrusted checkout cannot execute its code. A plugin can no
  longer replace a built-in principle or guide unless the loader is explicitly set to override.
  `--plugins-dir` is accepted but plugin loading is not yet wired into the generator.

## [2.3.0-lite] - 2026-01-18

### Added
- **Issue Templates Generation**: Generate bug_report.md and feature_request.md
- **PR Template Generation**: Generate PULL_REQUEST_TEMPLATE.md
- **CHANGELOG Generation**: Generate CHANGELOG.md following Keep a Changelog format
- `--include-github-templates` flag for GitHub issue/PR templates
- `--include-changelog` flag for CHANGELOG.md generation
- `--all` flag to include all optional templates at once
- New educational content for issue-templates, pr-template, and changelog principles

### Changed
- Updated version to 2.3.0-lite

### Referenced
- Enterprise script (2720 lines) used as reference for template implementations

## [2.2.0-lite] - 2026-01-18

### Added
- **Non-Interactive Mode**: `--non-interactive` flag for CI/script usage
- **Config File Support**: `.foundationrc` JSON config file support
- **JSON Export**: `--export-json` flag for machine-readable output
- **Educational Error Messages**: Helpful prompts when arguments are missing
- `--accept-terms` flag for pre-accepting ethical agreement in non-interactive mode
- `--quiet` flag for minimal output
- `--config` flag for specifying custom config file path
- Windows UTF-8 encoding fix for Unicode output

### Changed
- `--project-name` and `--author-name` are no longer required if provided in config file
- Updated argument parsing with proper `dest` parameters
- Improved non-interactive mode skips all prompts and sleeps

### Fixed
- Literal `\n` being printed instead of newlines
- Unicode encoding errors on Windows terminals

## [2.1.0-lite] - 2025-09-24

### Added
- Initial lite edition release
- Core governance principles (readme, contributing, license, code-of-conduct, security)
- Educational content for each principle
- Ethical use agreement with acknowledgment flow
- Version expiration advisory
- Local usage logging
- README, CONTRIBUTING, LICENSE generation
- Optional CODE_OF_CONDUCT and SECURITY generation
- .gitignore generation
- FOUNDATION_NOTICE.md ethics notice

### Philosophy
- Education First: WHAT/WHY before HOW
- Templates as starting points, not complete solutions
- Ethical safeguards against misuse

---

*This changelog documents the evolution of Project Foundation Template.*
*Generated and maintained following the Keep a Changelog standard.*
