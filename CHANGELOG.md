# Changelog

All notable changes to Project Foundation Template will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- (Upcoming features will be listed here)

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
