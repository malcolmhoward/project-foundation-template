# ADR 0007: Enterprise Feature Parity Strategy

## Status

Accepted

## Date

2026-01-19

## Context

Following the v3.0.0 release with plugin architecture, 23 principles, 15 guides, and 5 presets, a gap analysis was conducted comparing the current implementation against the original ~6,500 line enterprise specification from November 2025.

### Audit Findings

| Category | 6500+ Spec | v3.0.0 | Gap |
|----------|------------|--------|-----|
| Safety/Ethics | 6 safeguards | 6 safeguards | **0% - Complete** |
| Principles | 23 | 23 | Different composition |
| Guides | 20 | 15 | 5 missing |
| Generated Files | 15+ | 10 | 5 missing |
| Language Support | 18 | 0 | 100% |
| i18n Locales | 10 | 0 | 100% |

### Key Finding

**Safety and ethics parity is complete.** All 6 ethical safeguards from the "lite" pivot are fully implemented:
1. Ethical Use Agreement
2. Educational First (WHAT/WHY/RISK)
3. Usage Logging
4. Template Warnings
5. Advisory Expiration
6. Rate Limiting/Friction

The remaining gaps are feature additions, not safety concerns.

## Decision

We will address the enterprise feature gaps through **incremental minor version releases** (v3.1.0 - v3.6.0), maintaining the education-first philosophy and Principle Zero compliance.

### Release Strategy

| Version | Focus | Risk | Complexity |
|---------|-------|------|------------|
| v3.1.0 | Accessibility & Usability | Low | Low |
| v3.2.0 | Developer Documentation | Low | Medium |
| v3.3.0 | Extended Governance | Low | Low |
| v3.4.0 | Advanced Features | Low | Medium |
| v3.5.0 | Programming Languages | Medium | High |
| v3.6.0 | Internationalization | Medium | High |

### Prioritization Rationale

1. **v3.1.0 first** because it addresses the user-reported accessibility concern (glossary, term definitions)
2. **Documentation before principles** because HOW guides complement existing WHAT/WHY principles
3. **Language support late** because it's high-complexity and not core to governance education
4. **i18n last** because it requires significant new infrastructure

## Consequences

### Positive

1. **Incremental delivery**: Users get value with each release
2. **Risk mitigation**: Complex features (languages, i18n) deferred until simpler features proven
3. **Maintains quality**: Each release can be thoroughly tested
4. **Preserves safety**: No changes to ethical safeguards
5. **Clear roadmap**: Contributors know what to work on

### Negative

1. **Extended timeline**: Full parity requires 6 releases
2. **Maintenance burden**: More versions to support
3. **Feature fragmentation**: Users may need to wait for specific features

### Neutral

1. **Version proliferation**: Many minor versions (acceptable per SemVer)
2. **Documentation updates**: Each release needs changelog and migration notes

## Alternatives Considered

### 1. Single v4.0.0 Release

Bundle all gaps into one major release.

**Rejected because**:
- Too much change at once increases risk
- Delays value delivery
- Harder to test comprehensively

### 2. Parallel Feature Branches

Develop all features in parallel, merge when ready.

**Rejected because**:
- Coordination complexity
- Merge conflicts likely
- Harder to maintain quality

### 3. Feature Flags in v3.0.x

Add all features behind flags in patch releases.

**Rejected because**:
- Patch releases should only contain fixes (SemVer)
- Flag complexity increases maintenance burden
- Contradicts education-first philosophy

## Implementation

### GitHub Artifacts

Each version will have:
- **Milestone**: Track progress
- **Issues**: Individual features
- **PR Template**: Link to milestone

### Quality Gates

Each release requires:
- [ ] All features pass Principle Zero review
- [ ] Educational content complete (WHAT/WHY/RISK or HOW)
- [ ] Test coverage maintained
- [ ] Documentation updated
- [ ] No regression in ethical safeguards

## Related Decisions

- [ADR 0001: Education-First Approach](0001-education-first.md) (v2.1.0)
- [ADR 0002: Semantic Versioning Strategy](0002-semantic-versioning-strategy.md) (v2.6.0)
- [ADR 0005: Governance Preset System](0005-preset-system.md) (v2.7.0)
- [ADR 0006: Plugin Architecture](0006-plugin-architecture.md) (v2.11.0)
- [ADR 0008: Programming Language Support](0008-programming-language-support.md) (v3.5.0)
- [ADR 0009: Internationalization Architecture](0009-internationalization-architecture.md) (v3.6.0)

## References

- [ROADMAP.md](../../ROADMAP.md) - Post-v3.0.0 roadmap

---

*This ADR documents the strategic approach to achieving enterprise feature parity while maintaining the safety and educational foundations established in v2.1.0.*
