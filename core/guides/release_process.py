# core/guides/release_process.py
# Release Process Guide (v2.9.0)

"""
Release Process Guide.

Provides practical guidance on how to release software
safely and predictably.

Introduced in v2.9.0.
"""

GUIDE_ID = "release-process"

GUIDE = {
    "title": "Release Process Guide",
    "purpose": "Learn how to release software safely and predictably",
    "audience": "Maintainers and release managers",
    "complexity": "intermediate",
}

RELATED_PRINCIPLES = ["changelog", "ci-workflow"]

CONTENT = """
# Release Process Guide

## Overview

A good release process ensures:
- Predictable, repeatable releases
- Clear communication with users
- Minimal risk of introducing bugs
- Easy rollback if needed

## Pre-Release Checklist

### Code Quality
- [ ] All tests pass
- [ ] Code review completed
- [ ] No critical bugs open
- [ ] Security scan clean

### Documentation
- [ ] CHANGELOG updated
- [ ] README reflects changes
- [ ] API docs updated (if applicable)
- [ ] Migration guide (for breaking changes)

### Version
- [ ] Version number follows SemVer
- [ ] Version updated in all relevant files
- [ ] Git tag prepared

## Release Steps

### 1. Prepare the Release Branch

```bash
# Create release branch from main
git checkout main
git pull origin main
git checkout -b release/v1.2.0
```

### 2. Update Version Numbers

Update version in:
- `package.json` / `setup.py` / `Cargo.toml`
- `CHANGELOG.md`
- Any hardcoded version strings

### 3. Update Changelog

Move "Unreleased" items to new version section:

```markdown
## [1.2.0] - 2024-01-15

### Added
- New feature X (#123)

### Fixed
- Bug in feature Y (#124)
```

### 4. Create Release PR

- Title: "Release v1.2.0"
- Description: Summary of changes
- Request review from maintainers

### 5. Merge and Tag

```bash
# After PR approval
git checkout main
git pull origin main
git tag -a v1.2.0 -m "Release v1.2.0"
git push origin v1.2.0
```

### 6. Create GitHub Release

- Go to Releases > Draft new release
- Select the tag
- Copy changelog entry to description
- Attach any artifacts
- Publish release

### 7. Post-Release

- [ ] Verify release artifacts
- [ ] Test installation from release
- [ ] Announce release (if applicable)
- [ ] Update downstream dependencies

## Hotfix Process

For urgent fixes to released versions:

```bash
# Branch from the release tag
git checkout -b hotfix/v1.2.1 v1.2.0

# Make fix, commit, test
git commit -m "fix: critical bug in X"

# Tag and release
git tag -a v1.2.1 -m "Hotfix: critical bug in X"
git push origin v1.2.1

# Merge fix back to main
git checkout main
git merge hotfix/v1.2.1
```

## Rollback Process

If a release has critical issues:

1. **Communicate** - Alert users immediately
2. **Assess** - Determine severity and scope
3. **Decide** - Rollback vs hotfix
4. **Execute** - Either revert or release hotfix
5. **Post-mortem** - Document what went wrong

## Release Frequency

Choose a cadence that fits your project:

| Cadence | Best For |
|---------|----------|
| On-demand | Small projects, libraries |
| Weekly | Active development |
| Monthly | Stable products |
| Quarterly | Enterprise software |

## Automation

Consider automating:
- Version bumping
- Changelog generation
- Tag creation
- Release notes
- Artifact publishing

Tools: semantic-release, release-it, goreleaser

---

*This guide complements your CI/CD workflow and CHANGELOG.md*
"""
