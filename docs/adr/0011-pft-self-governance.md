# ADR 0011: PFT Self-Governance

**Date**: 2026-01-30
**Status**: Accepted
**Deciders**: Malcolm Howard
**Context**: PFT v3.7.0 dogfooding exercise

## Context

Project Foundation Template generates governance files for other projects. The question arose: should PFT apply its own governance templates to itself?

This "dogfooding" exercise serves multiple purposes:
1. **Validation** - Verify template quality by real-world application
2. **Credibility** - Demonstrate commitment to our own principles
3. **Discovery** - Identify template improvements through self-application
4. **Documentation** - Create provenance records for PFT's governance files

## Decision

**PFT adopts its own strict preset as the governance standard for itself.**

This means:
- PFT's existing governance files are evaluated against strict preset output
- Where existing exceeds template quality, we keep existing and document insights
- Where template has features existing lacks, we adopt with customization
- All files are documented in GENERATION_LOG.md with provenance status

## Principles Adopted (Strict Preset)

The strict preset includes 12 governance principles:

| Principle | Implementation Status | Notes |
|-----------|----------------------|-------|
| readme | Enhanced | 7x more comprehensive than template |
| contributing | Enhanced | Includes ethical review, attribution policy |
| license | Aligned | MIT license |
| code-of-conduct | Adopted | Generated and customized |
| security | Adopted | Generated and customized |
| enhanced-security | Enhanced | Existing exceeds template |
| secrets-detection | Considered | Pre-commit config available |
| changelog | Enhanced | Real version history |
| issue-templates | Enhanced | Principle Zero integration |
| pr-template | Enhanced | Ethical verification sections |
| ci-workflow | Not Applicable | Python project, different needs |
| adr | Enhanced | 11 ADRs with educational philosophy |

### Implementation Status Legend

| Status | Meaning |
|--------|---------|
| Aligned | Existing matches template intent |
| Enhanced | Existing exceeds template quality |
| Adopted | Generated and customized for PFT |
| Considered | Evaluated but not yet adopted |
| Not Applicable | Template pattern doesn't fit PFT's context |

## PFT-Specific Governance Additions

Beyond the strict preset, PFT maintains unique governance files:

| File | Purpose |
|------|---------|
| ETHICS.md | Core ethical framework (Principle Zero, safeguards, risk assessment) |
| CLAUDE.md | LLM integration guide (safety, context preservation) |
| GLOSSARY.md | Terminology definitions for clarity |
| ACKNOWLEDGMENTS.md | Feature inspiration credits |
| SEMANTIC_VERSIONING.md | Versioning philosophy |
| ethical-review-check.yml | Automated ethical review validation |

These files represent governance practices that **cannot be generated** - they emerge from project-specific ethical commitments and operational experience.

## Consequences

### Positive

1. **Credibility reinforced** - PFT practices what it preaches
2. **Template improvements identified** - 8 enhancement opportunities documented
3. **Provenance established** - All files now have documented origin
4. **Self-reference enabled** - PFT can point to itself as implementation example
5. **Governance maturity visible** - Gap between template and existing shows evolution

### Negative

1. **Maintenance burden** - Must update GENERATION_LOG.md when files change
2. **Recursive complexity** - Self-reference requires careful documentation
3. **Expectation setting** - Users may expect their projects to match PFT quality immediately

### Neutral

1. **Template vs. Practice distinction** - Clarifies that templates are starting points, not destinations
2. **Tiering validation** - Confirms strict preset is appropriate for PFT's security focus

## Alternatives Considered

### Alternative 1: No Self-Governance

Don't apply PFT templates to itself.

**Rejected because**: Undermines credibility. "Do as I say, not as I do" is poor leadership.

### Alternative 2: Full Template Replacement

Replace all existing files with generated output.

**Rejected because**: Existing files often exceed template quality. Replacement would be a regression.

### Alternative 3: Enterprise Preset

Apply enterprise (30 principles) instead of strict (12 principles).

**Rejected because**: Enterprise preset is for large organizations. Strict is appropriate for security-focused projects like PFT.

## Template Improvements Identified

This exercise identified these template improvement opportunities:

### High Priority

1. **README: "Who is This For?" pattern** - Audience matrix helps users self-identify
2. **README: "What This Is Not" section** - Prevents common misconceptions
3. **CONTRIBUTING: Commit scope table** - Improves history navigability

### Medium Priority

4. **CONTRIBUTING: Educational review criteria** - Beyond technical review
5. **PR Template: Educational context section** - WHY emphasis
6. **ADR README: Philosophy paragraph** - Decision reasoning guidance

### Lower Priority (Preset-Specific)

7. **Feature Request: Ethical assessment option** - For strict preset
8. **PR Template: Ethical verification option** - For projects with ethical frameworks

See [docs/dogfood/DELTA_ANALYSIS.md](../dogfood/DELTA_ANALYSIS.md) for detailed analysis.

## Implementation

1. Created `pft-dogfood-output/` with strict preset generation
2. Compared all generated files against existing
3. Documented findings in `docs/dogfood/DELTA_ANALYSIS.md`
4. Created `GENERATION_LOG.md` with file provenance
5. Created this ADR to formalize governance adoption
6. Adopted CODE_OF_CONDUCT.md and SECURITY.md with customization
7. Adopted docs/adr/template.md for future ADR creation

## References

- [GENERATION_LOG.md](../../GENERATION_LOG.md) - File provenance documentation
- [docs/dogfood/DELTA_ANALYSIS.md](../dogfood/DELTA_ANALYSIS.md) - Comparison insights
- [core/presets/strict.py](../../core/presets/strict.py) - Strict preset definition
- [ETHICS.md](../../ETHICS.md) - PFT's ethical framework

---

*This ADR formalizes PFT's commitment to practicing what it preaches.*
