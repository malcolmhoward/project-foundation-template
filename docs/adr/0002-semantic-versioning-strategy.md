# ADR 0002: Semantic Versioning Strategy

## Status

Accepted

## Date

2026-01-18

## Context

Software projects need a consistent way to communicate changes to users. The Project Foundation Template faced several versioning challenges:

### Challenge 1: Version Continuity
The "lite" edition evolved from v2.0.1 enterprise. Should it:
- Reset to v1.0.0 (fresh start)?
- Continue as v2.1.0 (evolution)?

### Challenge 2: Timeline Expectations
Users and stakeholders often ask "when will feature X ship?" This creates pressure to:
- Give dates that may not be met
- Rush features to meet deadlines
- Prioritize speed over quality

### Challenge 3: Breaking Change Communication
The v3.0.0 plugin architecture will fundamentally change how the tool works. Users need clear signals about what to expect.

### Challenge 4: Education vs. Speed
Our education-first philosophy conflicts with "ship fast" culture. How do we version in a way that supports thorough learning?

## Decision

We adopt a **time-agnostic semantic versioning strategy** with the following principles:

### 1. No Date Commitments

The roadmap contains **what** and **why**, never **when**:

```
✅ "v2.4.0 will include enhanced security and secrets detection"
✅ "Features ship when quality criteria are met"

❌ "v2.4.0 releases in Q2 2026"
❌ "This will be done in 2 weeks"
```

**Rationale**: Dates create pressure that undermines education and quality. We ship when ready, not when calendars demand.

### 2. Continuation over Reset

The lite edition continues the v2.x line:

```
v2.0.1 (enterprise) → v2.1.0 (lite) → v2.6.0 (modular) → v3.0.0 (plugins)
```

**Rationale**:
- Users expect v2.x patterns to be compatible
- Starting at v1.0 would suggest less maturity than exists
- It accurately reflects evolution, not reinvention

### 3. Strict SemVer Interpretation

| Change Type | Version Bump | User Action |
|-------------|--------------|-------------|
| Bug fix | PATCH (2.1.x) | Update freely |
| New feature (compatible) | MINOR (2.x.0) | Update to get features |
| Breaking change | MAJOR (x.0.0) | Read migration guide |

### 4. Feature-Based Milestones

Versions are defined by features, not dates:

| Version | Defined By | NOT Defined By |
|---------|------------|----------------|
| v2.3.0 | "Issue/PR templates complete" | "Ships March 2026" |
| v3.0.0 | "Plugin system working" | "End of year release" |

### 5. Quality Gates, Not Date Gates

Release criteria are quality-based:

```markdown
### v2.4.0 Release Criteria
- [ ] All features pass Principle Zero review
- [ ] Documentation complete with WHAT/WHY/HOW
- [ ] Backward compatible with v2.3.x
- [ ] Community testing period complete
```

Not: "Release by April 15th"

## Consequences

### Positive

1. **Quality assurance**: Features ship ready, not rushed
2. **Honest communication**: No missed deadlines, no broken promises
3. **Education time**: Users have time to learn each version
4. **Reduced pressure**: Contributors focus on craft, not calendars
5. **Trust building**: Predictable quality, unpredictable timing is better than the reverse

### Negative

1. **Planning difficulty**: External dependencies can't plan around our releases
2. **Perception issues**: "No dates" may seem unprofessional to some
3. **Impatience**: Users wanting specific features must wait indefinitely
4. **Resource allocation**: Hard to staff without timelines

### Neutral

1. **Community self-selection**: Attracts users who value quality over speed
2. **Different metrics**: Success measured by adoption and satisfaction, not velocity

## Alternatives Considered

### 1. Date-Based Releases
Release quarterly regardless of feature completeness.

**Rejected because**: Creates pressure to ship incomplete features or empty releases.

### 2. Version Reset
Start lite edition at v1.0.0.

**Rejected because**: Misleads users about maturity and breaks expectation continuity.

### 3. CalVer (Calendar Versioning)
Use dates as versions (e.g., 2026.01.18).

**Rejected because**: Implies time-based releases, which conflicts with our quality-first approach.

### 4. Feature Flags Instead of Versions
Ship everything, enable features via flags.

**Rejected because**: Increases complexity and dilutes the education-first approach.

## Implementation

### Version Definition

Versions are defined in `core/utils.py`:

```python
SCRIPT_VERSION = "2.6.0-lite"
EXPIRATION_DATE = date(2026, 3, 1)
```

### Pre-release Tags

```
2.7.0-alpha.1   # Early testing
2.7.0-beta.1    # Feature complete, needs testing
2.7.0-rc.1      # Release candidate
2.7.0           # Stable
```

### Communication Strategy

When asked "when will X ship?":

> "We don't commit to dates because we prioritize quality. You can track progress in our GitHub issues. When the release criteria are met, it ships."

## Related Decisions

- [ADR 0001: Education-First Approach](0001-education-first.md) (v2.1.0)
- [ADR 0003: Advisory Expiration System](0003-advisory-expiration.md) (v2.6.0) - explains date-based expiration vs. version-based updates
- [ADR 0004: Modular Package Architecture](0004-modular-package-architecture.md) (v2.6.0)
- [ADR 0005: Governance Preset System](0005-preset-system.md) (v2.7.0)
- ADR 0006: Plugin Architecture (v2.11.0)

## References

- [SEMANTIC_VERSIONING.md](../../SEMANTIC_VERSIONING.md) - Full versioning guide
- [ROADMAP.md](../../ROADMAP.md) - Feature roadmap (no dates)
- [semver.org](https://semver.org) - SemVer specification

---

*We measure progress in features delivered, not dates met. This ADR codifies our commitment to quality over velocity.*
