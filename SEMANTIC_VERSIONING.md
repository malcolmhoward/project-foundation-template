# Semantic Versioning Policy

This document explains how Project Foundation Template uses semantic versioning and why we make the choices we do.

## What is Semantic Versioning?

Semantic Versioning (SemVer) uses a three-part version number: `MAJOR.MINOR.PATCH`

```
2.9.0
| | |__ PATCH: Bug fixes, no new features
| |____ MINOR: New features, backward compatible
|______ MAJOR: Breaking changes
```

For the full specification, see [semver.org](https://semver.org).

## Our Version Philosophy

### Why We Do Not Provide Dates

You will notice our [ROADMAP.md](ROADMAP.md) has no release dates. This is intentional:

1. **Quality over speed**: Features ship when ready, not when calendars say
2. **Honest expectations**: We cannot predict complexity accurately
3. **Education takes time**: Rushing undermines our core mission
4. **No false promises**: Missed dates erode trust

Instead, we communicate:
- What each version will contain
- What criteria must be met before release
- What is currently in progress

### Version Numbering Decisions

#### Why v2.x Instead of v1.0?

The "lite" edition continues the v2.x line because:
- It is an evolution of v2.0.1, not a fresh start
- Users expect v2.x to be compatible with v2.0.x patterns
- Starting at v1.0 would suggest less maturity than exists
- The ethical pivot was a scope change, not a rewrite

#### Why v3.0.0 for Modular Architecture?

The plugin system will be a breaking change:
- API changes for programmatic generator usage
- Configuration file format changes
- Different output organization
- Import paths will change

MAJOR version increment signals "expect changes, read migration guide."

## What Constitutes a Breaking Change

### Breaking Changes (Require MAJOR Bump)

These changes require incrementing the MAJOR version:

| Change Type | Example |
|-------------|---------|
| Removed CLI flags | `--old-flag` no longer exists |
| Changed default output | Files now go to `./output/` instead of `./` |
| Renamed generated files | `SECURITY.md` renamed to `security-policy.md` |
| Changed config file format | JSON schema incompatibility |
| Changed programmatic API | Function signatures changed |
| Removed features | A principle is removed entirely |

### Non-Breaking Changes (MINOR or PATCH)

These changes do not require a MAJOR bump:

| Change Type | Version | Example |
|-------------|---------|---------|
| New CLI flag | MINOR | Added `--include-adr` |
| New template type | MINOR | Added PR template generation |
| Bug fix | PATCH | Fixed Unicode handling |
| Documentation fix | PATCH | Corrected typo in CONTRIBUTING.md |
| New optional feature | MINOR | Added secrets detection |
| Performance improvement | PATCH | Faster template generation |

## Our Versioning Rules

### PATCH Increments (2.9.x to 2.9.y)

Increment PATCH for:
- Bug fixes
- Documentation corrections
- Typo fixes
- Security patches that do not change API
- Performance improvements

**Examples:**
- Fix Unicode handling in generator
- Correct markdown formatting in templates
- Patch vulnerability in dependency
- Improve error message clarity

**User impact**: Update freely, no changes needed.

### MINOR Increments (2.x.0 to 2.y.0)

Increment MINOR for:
- New features (backward compatible)
- New optional principles
- Enhanced templates
- New CLI flags

**Examples:**
- Add `--include-adr` flag
- New issue templates
- Additional license options
- New documentation guide

**User impact**: Update to get new features. Existing usage unchanged.

### MAJOR Increments (x.0.0 to y.0.0)

Increment MAJOR for:
- Breaking API changes
- Removed features
- Changed defaults that affect output
- Configuration format changes

**Examples:**
- v3.0.0 plugin architecture
- Output directory structure changes
- Required flag becomes optional (changes behavior)
- Configuration file schema changes

**User impact**: Read migration guide before updating.

## Pre-release Versions

We use pre-release tags for testing:

```
2.9.0-alpha.1   # Early testing, may be unstable
2.9.0-beta.1    # Feature complete, needs testing
2.9.0-rc.1      # Release candidate, final testing
2.9.0           # Stable release
```

### When to Use Pre-releases

| Tag | Stability | Recommended For |
|-----|-----------|-----------------|
| alpha | Experimental | Contributors only |
| beta | Unstable | Testing environments |
| rc | Stable | Staging environments |
| (none) | Production | All users |

### Pre-release Sorting

Versions sort correctly per SemVer:

```
2.8.0 < 2.9.0-alpha.1 < 2.9.0-beta.1 < 2.9.0-rc.1 < 2.9.0 < 3.0.0
```

Note: Pre-releases sort *before* the release they modify.

## Advisory Expiration vs. Version

Our templates have "advisory expiration" dates. This is different from versioning:

| Concept | Purpose | Mechanism |
|---------|---------|-----------|
| Version | Track changes | SemVer numbering |
| Expiration | Prompt updates | Date-based warning |

A template can be the latest version but still expired if it has not been updated in a long time. Expiration says "this might be stale," not "a newer version exists."

## Release Process

### 1. Feature Completion

All planned features for the version are complete and tested.

### 2. Educational Review

- All new features have WHAT/WHY/HOW documentation
- Educational content is accurate and helpful
- Examples are tested and working

### 3. Ethical Review

- Features pass Principle Zero test
- Misuse potential has been considered
- Appropriate safeguards are in place

### 4. Community Testing

- Pre-release available for testing
- Feedback incorporated
- Issues resolved

### 5. Documentation Update

- CHANGELOG updated
- MIGRATION guide updated (if needed)
- README updated
- ROADMAP updated

### 6. Release

```bash
# Create annotated tag
git tag -a v2.9.0 -m "Release v2.9.0: Documentation and stability"

# Push tag
git push origin v2.9.0
```

### 7. Post-Release

- Announce release
- Monitor for issues
- Begin next version planning

## Version Support Policy

### Active Support

| Version | Support Level | Duration |
|---------|---------------|----------|
| Current | Full | Until next MINOR release |
| Previous MINOR | Security only | 6 months after next MINOR |
| Previous MAJOR | None | Migration guide available |

### What "Security Only" Means

- Critical security fixes backported
- No new features
- No bug fixes (except security)
- Documentation updates only for security

### End of Life

When a version reaches end of life:
- No further updates
- Users encouraged to migrate
- Documentation remains available
- Advisory expiration may trigger warnings

## Backward Compatibility Promises

### Within MINOR Versions

All 2.x releases maintain:
- CLI flag compatibility
- Output file locations (unless documented)
- Configuration file format
- Generated file format

### Across MAJOR Versions

Breaking changes are:
- Documented in release notes
- Explained in migration guides
- Announced in advance via pre-releases

## Changelog Conventions

Our CHANGELOG follows [Keep a Changelog](https://keepachangelog.com):

```markdown
## [2.9.0] - 2026-01-18

### Added
- New features

### Changed
- Changes in existing functionality

### Deprecated
- Soon-to-be removed features

### Removed
- Removed features

### Fixed
- Bug fixes

### Security
- Security fixes
```

## Version in Code

The version is defined in `generate_foundation.py` and `core/utils.py`:

```python
SCRIPT_VERSION = "3.0.0"
EXPIRATION_DATE = date(2026, 6, 1)
```

Both should be updated together during releases.

## Checking Versions

### Current Version

```bash
python generate_foundation.py --version
```

### Version in Generated Files

Generated files include version metadata:

```markdown
<!-- Generated by Project Foundation Template v2.9.0 -->
```

This helps track which version generated which files.

## Questions

### "What version should I use?"

Use the latest stable release (no pre-release tags).

### "When will version X release?"

When it is ready. Check GitHub issues and ROADMAP for progress.

### "Is my version out of date?"

The generator will warn you if:
- Advisory expiration has passed
- You are using an alpha/beta version

### "Can I skip versions when upgrading?"

Yes, but read all intermediate release notes to understand cumulative changes. Check MIGRATION.md for any breaking changes.

### "Why does the version say 'lite'?"

The `-lite` suffix indicates this is the education-first edition that emerged from the ethical pivot. It will be dropped in v3.0.0 when the full modular architecture is complete.

---

## Related Documents

- [ROADMAP.md](ROADMAP.md) - Planned features per version
- [MIGRATION.md](MIGRATION.md) - Upgrading guidance
- [CHANGELOG.md](CHANGELOG.md) - Version history
- [CONTRIBUTING.md](CONTRIBUTING.md) - How versions are developed

---

*Version numbers tell a story. Ours says: education and quality, delivered when ready.*
