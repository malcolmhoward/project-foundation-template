# Semantic Versioning Strategy

This document explains how Project Foundation Template uses semantic versioning and why we make the choices we do.

## What is Semantic Versioning?

Semantic Versioning (SemVer) uses a three-part version number: `MAJOR.MINOR.PATCH`

```
2.3.1
│ │ └── PATCH: Bug fixes, no new features
│ └──── MINOR: New features, backward compatible
└────── MAJOR: Breaking changes
```

For full specification, see [semver.org](https://semver.org).

## Our Version Philosophy

### Why We Don't Give Dates

You'll notice our [ROADMAP.md](ROADMAP.md) has no dates. This is intentional:

1. **Quality over speed**: Features ship when ready, not when calendars say
2. **Honest expectations**: We can't predict complexity accurately
3. **Education takes time**: Rushing undermines our core mission
4. **No false promises**: Missed dates erode trust

Instead, we communicate:
- What each version will contain
- What criteria must be met
- What's currently in progress

### Version Numbering Decisions

#### Why v2.x Instead of v1.0?

The "lite" edition continues the v2.x line because:
- It's an evolution of v2.0.1, not a fresh start
- Users expect v2.x to be compatible with v2.0.x patterns
- Starting at v1.0 would suggest less maturity than exists

#### Why v3.0.0 for Modular Architecture?

The plugin system is a breaking change:
- API changes for generator usage
- Configuration file format changes
- Different output organization

MAJOR version increment signals "expect changes."

## Our Versioning Rules

### PATCH Increments (2.1.x → 2.1.y)

Increment PATCH for:
- Bug fixes
- Documentation corrections
- Typo fixes
- Security patches that don't change API

**Examples:**
- Fix Unicode handling in generator
- Correct markdown formatting in templates
- Patch vulnerability in dependency

**User impact**: Update freely, no changes needed.

### MINOR Increments (2.x.0 → 2.y.0)

Increment MINOR for:
- New features (backward compatible)
- New optional principles
- Enhanced templates
- New CLI flags

**Examples:**
- Add `--non-interactive` flag
- New issue templates
- Additional license options

**User impact**: Update to get new features. Existing usage unchanged.

### MAJOR Increments (x.0.0 → y.0.0)

Increment MAJOR for:
- Breaking API changes
- Removed features
- Changed defaults that affect output
- Configuration format changes

**Examples:**
- v3.0.0 plugin architecture
- Output directory structure changes
- Required flag becomes optional (changes behavior)

**User impact**: Read migration guide before updating.

## Pre-release Versions

We use pre-release tags for testing:

```
2.3.0-alpha.1   # Early testing, may be unstable
2.3.0-beta.1    # Feature complete, needs testing
2.3.0-rc.1      # Release candidate, final testing
2.3.0           # Stable release
```

### When to Use Pre-releases

- **Alpha**: Internal testing, adventurous early adopters
- **Beta**: Feature complete, seeking feedback
- **RC**: Final validation before release

### Pre-release Stability

| Tag | Stability | Recommended For |
|-----|-----------|-----------------|
| alpha | Experimental | Contributors only |
| beta | Unstable | Testing environments |
| rc | Stable | Staging environments |
| (none) | Production | All users |

## Version Comparison

Versions sort correctly per SemVer:

```
1.0.0 < 2.0.0 < 2.0.1 < 2.1.0 < 2.1.0-alpha.1 < 2.1.0-beta.1 < 2.1.0-rc.1 < 2.1.0 < 3.0.0
```

Note: Pre-releases sort *before* the release they modify.

## Advisory Expiration vs. Version

Our templates have "advisory expiration" dates. This is different from versioning:

| Concept | Purpose | Mechanism |
|---------|---------|-----------|
| Version | Track changes | SemVer numbering |
| Expiration | Prompt updates | Date-based warning |

A template can be the latest version but still expired if it hasn't been updated. Expiration says "this might be stale," not "a newer version exists."

## Backward Compatibility Promises

### Within MINOR versions

All 2.x releases maintain:
- CLI flag compatibility
- Output file locations (unless documented)
- Configuration file format
- Generated file format

### Across MAJOR versions

Breaking changes are:
- Documented in release notes
- Explained in migration guides
- Announced in advance

## Changelog Conventions

Our CHANGELOG follows [Keep a Changelog](https://keepachangelog.com):

```markdown
## [2.3.0] - YYYY-MM-DD

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

The version is defined in `setup_foundation_lite.py`:

```python
VERSION = "2.1.0-lite"
EXPIRATION_DATE = "2026-03-01"
```

Both should be updated together during releases.

## Tagging Releases

Releases are tagged in Git:

```bash
# Create annotated tag
git tag -a v2.3.0 -m "Release v2.3.0: Community governance features"

# Push tag
git push origin v2.3.0
```

Tag format: `v` prefix + version number (e.g., `v2.3.0`)

## Checking Versions

### Current Version

```bash
python setup_foundation_lite.py --version
```

### Version in Generated Files

Generated files include version metadata:

```markdown
<!-- Generated by Project Foundation Template v2.1.0 -->
```

This helps track which version generated which files.

## Priority and Versions

Features are assigned to versions based on priority assessment:

| Priority | Typical Version | Rationale |
|----------|-----------------|-----------|
| High | Next MINOR | Low risk, high impact, ship soon |
| Medium | MINOR+1 or +2 | Moderate complexity, needs preparation |
| Low | Later MINOR or MAJOR | Lower urgency or higher complexity |

## Questions

### "What version should I use?"

Use the latest stable release (no pre-release tags).

### "When will version X release?"

When it's ready. Check GitHub issues for progress.

### "Is my version out of date?"

The generator will warn you if:
- Advisory expiration has passed
- A significantly newer version exists (future feature)

### "Can I skip versions when upgrading?"

Yes, but read all intermediate release notes to understand cumulative changes.

---

## Related Documents

- [ROADMAP.md](ROADMAP.md) - Planned features per version
- [MIGRATION.md](MIGRATION.md) - Upgrading guidance
- [CONTRIBUTING.md](CONTRIBUTING.md) - How versions are developed

---

*Version numbers tell a story. Ours says: education and quality, delivered when ready.*
