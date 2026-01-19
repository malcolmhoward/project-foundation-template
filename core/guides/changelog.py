# core/guides/changelog.py
# Changelog Guide (v2.9.0)

"""
Changelog Guide.

Provides practical guidance on maintaining a changelog
following the Keep a Changelog format.

Introduced in v2.9.0.
"""

GUIDE_ID = "changelog"

GUIDE = {
    "title": "Changelog Guide",
    "purpose": "Learn how to maintain a useful changelog",
    "audience": "All developers",
    "complexity": "beginner",
}

RELATED_PRINCIPLES = ["changelog", "versioning"]

CONTENT = """
# Changelog Guide

## What is a Changelog?

A changelog is a file containing a curated, chronologically ordered list
of notable changes for each version of a project.

## Why Keep a Changelog?

- Helps users understand what changed between versions
- Documents the project's evolution
- Assists in upgrade decisions
- Recognizes contributors

## The Keep a Changelog Format

Use [keepachangelog.com](https://keepachangelog.com/) format:

```markdown
# Changelog

All notable changes to this project will be documented in this file.

## [Unreleased]

### Added
- New feature description

## [1.0.0] - 2024-01-15

### Added
- Initial release features

### Changed
- Updated dependencies

### Fixed
- Bug fixes
```

## Change Categories

Use these categories (in this order):

| Category | When to Use |
|----------|-------------|
| **Added** | New features |
| **Changed** | Changes in existing functionality |
| **Deprecated** | Soon-to-be removed features |
| **Removed** | Removed features |
| **Fixed** | Bug fixes |
| **Security** | Vulnerability fixes |

## Writing Good Entries

### Do

- Write for humans, not machines
- Use present tense ("Add" not "Added")
- Link to issues/PRs when relevant
- Group related changes
- Be concise but informative

### Don't

- Include every commit
- Use technical jargon unnecessarily
- Forget breaking changes
- Leave entries vague

## Examples

### Good Entries

```markdown
### Added
- User authentication with OAuth2 support (#123)
- Dark mode theme option in settings

### Changed
- Improved search performance by 40% (#145)
- Updated minimum Node.js version to 18

### Fixed
- Login form no longer accepts empty passwords (#167)
- Resolved memory leak in image processing
```

### Bad Entries

```markdown
### Changed
- Updated stuff
- Fixed things
- Various improvements
```

## Workflow

### During Development

1. Keep an "Unreleased" section at the top
2. Add entries as you make changes
3. Don't wait until release time

### At Release Time

1. Change "Unreleased" to version number and date
2. Create new "Unreleased" section
3. Review and clean up entries
4. Ensure version links work

## Automation Tips

- Use PR templates that remind about changelog updates
- Consider changelog generators for consistency
- But always review auto-generated entries

## Template

```markdown
# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/).

## [Unreleased]

### Added

### Changed

### Deprecated

### Removed

### Fixed

### Security

## [0.1.0] - YYYY-MM-DD

### Added
- Initial release
```

---

*This guide complements your project's CHANGELOG.md template*
"""
