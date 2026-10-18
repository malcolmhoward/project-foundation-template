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

The implementation guides, and the principles that do not have their own generated files, are
reference content in 3.7.0: they are available through `--list-principles`, `--list-guides` and
the Python API, but the generator does not write them into projects, and a preset's principle
list does not change which files are generated (the strict and enterprise presets generate the
same files). Connecting them to generated output is planned for 3.8.0
([#116](https://github.com/malcolmhoward/project-foundation-template/issues/116)).

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
- **2.10.0**: 11 principles (quality, compliance, infrastructure, inclusivity, lifecycle) and
  9 guides.
- **2.11.0**: Plugin API (`core/plugins/`) for custom principles and guides.
- **3.0.0**: New entry point `generate_foundation.py` with `--preset`, `--list-presets`,
  `--list-principles` and `--list-guides`.
- **3.1.0**: Onboarding files (GLOSSARY.md, MAINTAINERS.md); principles `glossary` and `maintainers`;
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
  process. A Tests workflow runs the test suite on Linux and macOS for pull requests.

### Changed
- `setup_foundation_lite.py` is now a compatibility shim: it runs `generate_foundation.py` with
  the same arguments and needs the full repository (see MIGRATION.md).
- Generated templates no longer contain emoji in headings, and README code blocks are no longer
  written with escaped backticks.
- The generation log records files by path relative to the output directory
  (for example `.github/workflows/ci.yml`).
- The advisory expiration date is now 2027-04-01.
- Non-interactive runs no longer overwrite existing files: they stop with an error unless
  `--force-overwrite` is given. Interactive runs still ask first. Only files the run would
  write are checked, so a repository's own files that the run does not generate (for example
  its CHANGELOG.md, when the changelog is not requested) do not stop it. An existing generation
  log is still appended to, not replaced, unless `--force-overwrite` is given; the replaced log
  is then kept as a backup.
- The generated CI workflow (`ci.yml`) is language-neutral and fails, with a message saying why,
  until its "Run checks" step is replaced with the project's own commands. It no longer runs
  Node.js commands by default or uses `continue-on-error`, which kept runs green when lint,
  tests or the build failed. It runs on pushes and pull requests to `main` only (`develop` was
  dropped). Presets that include it (standard, strict, enterprise) are affected. When it is
  generated, the generator says so in its last line of output, `--quiet` included.
- `SECRETS_PATTERNS` (in `core/utils.py` and the `core` package) now holds the patterns of the
  new `SECRET_DETECTORS` table, which the generated secrets hook uses; its contents changed.
- `core/templates/accessibility.py` is now `core/templates/onboarding.py`: it holds the
  glossary, maintainers and scaffold-manifest templates, which support onboarding, while
  "accessibility" in PFT means access for people with disabilities. Import its functions from
  `core.templates`, which is unchanged.
- The principles and guides first added in 2.10.0 are recorded as 2.10.0 instead of 3.0.0, in
  `PRINCIPLE_VERSIONS`, `GUIDE_VERSIONS` and the modules' headers.
- The generated secrets hook reports the file, the line numbers and the kind of secret it
  found, not the matching line, so the secret does not end up in terminal history or CI logs.
  It ignores the text of `[REPLACE: ...]` placeholders instead of skipping every line that
  contains "REPLACE". It starts with `#!/usr/bin/env bash`, so it also runs where bash is not at
  `/bin/bash`, including under pre-commit on Windows.
- PFT's own PR template and Ethical Review Check: the reviewer's checklist is four items (the
  three overlapping documentation items are merged, and "no unmitigated critical risks" is part
  of the risk item); "No new ethical concerns discovered during implementation" is replaced by a
  required "New concerns found during implementation" line. The check now confirms only that the
  sections are present, since the PR's author can edit the description, and its label step,
  which never ran with the workflow's read-only token, is removed.
- `scripts/bulk-operations/update-github-issues.sh` is a dry run unless `--apply` is given,
  needs `--repo`, and will not apply while any `[REPLACE: ...]` placeholder is unfilled. Run
  as-is, it used to edit issues 1-10 of this repository and record "Principle Zero: ✅ Passes"
  on them.

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
- `--quiet` no longer hides the warning that the version is outdated; it prints a one-line
  version of it.
- The generated SECURITY.md claimed detections the secrets hook did not have (cloud
  credentials, JWTs, connection strings), and described the hook even when it was not
  generated. It now lists exactly what the hook detects, and only when the hook is generated;
  the hook and the list share one set of patterns (`SECRET_DETECTORS` in `core/utils.py`).
- The generated secrets hook flagged its own file and SECURITY.md, so freshly generated files
  could not be committed. It also printed colour codes literally, skipped staged files whose
  names contain spaces, skipped renamed files, and scanned the working copy instead of the
  staged version. With nothing staged it now says so instead of reporting no secrets.
- `--all` wrote SECURITY.md twice, the basic policy and then the enhanced one.
- Replacing a generation log (with `--force-overwrite`, the interactive "overwrite" choice, or
  because a JSON log could not be read) discarded the old log, or wrote over an earlier backup.
  The old log is now kept as `GENERATION_LOG.md.bak` (or `.json.bak`), then `.bak.1`, `.bak.2`.
- The scaffold manifest suggested `--preset None` for runs without a preset, which the command
  rejects; it now suggests the options the run used. Its guides section says why it is empty
  (guides are not generated into projects yet) instead of "None specified".
- Translation templates written as YAML now load back unchanged: strings are quoted and
  escaped, and keys such as `yes` and `no` are no longer read as booleans. `generated_by` names
  the current version instead of v3.6.0.
- The education text cited statistics without sources (for example "Codes of Conduct increase
  diversity by 40%"); they are replaced with statements that need no figures.
- The glossary guide, written for generated projects, included PFT's own terms; they are
  removed, and the general terms "Governance" and "Governance Theater" moved into the list.
- Six guides listed related principles that do not exist (`code-review`, `release-process`).
- Documentation corrected to match the code: the README restores the list of ways governance
  templates can be misused and notes which sections describe generated output; CONTRIBUTING's
  steps for adding principles and guides match the module structure; ADR 0004, ADR 0005,
  ROADMAP.md and MIGRATION.md give the measured counts; MIGRATION.md says the v2.6.0 refactor
  changed the content of six generated files; the enterprise edition is labelled v2.1.0, not
  v2.0.1, and its specification is dated September 2025; ADR 0006 names the `override` conflict
  mode; ADRs 0008 and 0009 are marked accepted; `--all`'s help lists every file it adds;
  Conventional Commits' breaking-change marker is described correctly.
- The generated MAINTAINERS.md listed a GitHub username guessed from the author's name, which
  could belong to someone else; it is now a placeholder, and the file has a template notice.

### Removed
- The stale `foundation/` package, left behind by the rename to `core/`.

### Security
- Plugins are no longer discovered in `./plugins/` of the current directory by default, so
  running the generator inside an untrusted checkout cannot execute its code. A plugin can no
  longer replace a built-in principle or guide unless the loader is explicitly set to override.
  `--plugins-dir` is accepted but plugin loading is not yet wired into the generator.
- `accept_terms` and `force_overwrite` in a config file (`.foundationrc` or `--config`) are
  ignored with a warning; they must be given on the command line, so a config file in a cloned
  or shared repository cannot accept the ethical use agreement or overwrite files on someone's
  behalf.

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
