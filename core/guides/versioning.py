# core/guides/versioning.py
# Semantic Versioning Guide (v2.9.0)

"""
Semantic Versioning Guide.

Provides practical guidance on how to version your project
following Semantic Versioning (SemVer) conventions.

Introduced in v2.9.0.
"""

GUIDE_ID = "versioning"

GUIDE = {
    "title": "Semantic Versioning Guide",
    "purpose": "Learn how to version your software meaningfully",
    "audience": "All developers",
    "complexity": "beginner",
}

RELATED_PRINCIPLES = ["changelog", "release-process"]

CONTENT = """
# Semantic Versioning Guide

## Overview

Semantic Versioning (SemVer) uses a three-part version number: MAJOR.MINOR.PATCH

## The Rules

### MAJOR version (X.0.0)
Increment when you make **incompatible API changes**.

**Examples:**
- Removing a public function
- Changing function signatures
- Breaking backward compatibility
- Major architectural changes

### MINOR version (0.X.0)
Increment when you add **functionality in a backward-compatible manner**.

**Examples:**
- Adding new features
- Adding new functions/methods
- Deprecating features (but not removing)
- Non-breaking improvements

### PATCH version (0.0.X)
Increment when you make **backward-compatible bug fixes**.

**Examples:**
- Bug fixes
- Security patches
- Documentation updates
- Performance improvements (non-breaking)

## Pre-release Versions

Use suffixes for pre-release versions:
- `1.0.0-alpha.1` - Early testing
- `1.0.0-beta.1` - Feature complete, testing
- `1.0.0-rc.1` - Release candidate

## Starting a Project

Start at `0.1.0` for initial development:
- `0.x.x` signals API instability
- Anything may change at any time
- Move to `1.0.0` when API is stable

## Common Mistakes

1. **Incrementing MAJOR for every change**
   - Only increment MAJOR for breaking changes

2. **Not incrementing MAJOR for breaking changes**
   - Breaking changes MUST increment MAJOR

3. **Using version numbers for marketing**
   - SemVer is for API compatibility, not marketing

4. **Forgetting pre-release conventions**
   - Use `-alpha`, `-beta`, `-rc` appropriately

## Quick Reference

| Change Type | Version Part | Example |
|-------------|--------------|---------|
| Breaking change | MAJOR | 1.0.0 -> 2.0.0 |
| New feature | MINOR | 1.0.0 -> 1.1.0 |
| Bug fix | PATCH | 1.0.0 -> 1.0.1 |

## Resources

- [semver.org](https://semver.org/) - Official specification
- [Keep a Changelog](https://keepachangelog.com/) - Changelog format

---

*This guide complements your project's CHANGELOG.md*
"""
