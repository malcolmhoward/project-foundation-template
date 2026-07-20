# File Inventory Analysis

**Generated**: 2026-01-30
**Purpose**: Comprehensive analysis of all PFT files for generation potential

This document extends the [DELTA_ANALYSIS.md](DELTA_ANALYSIS.md) by evaluating ALL project files, not just those compared during the initial dogfooding exercise.

---

## Summary Statistics

| Category | Count |
|----------|-------|
| Root governance files | 19 |
| Core modules | 7 |
| Guides | 25 |
| Principles | 30 |
| Programming languages | 17 |
| Internationalization locales | 10 |
| Presets | 5 |
| ADRs | 11 |
| Tests | 14 |
| **Total tracked files** | ~175 |

---

## File Classification

### Tier 1: Currently Generated

Files that PFT already generates for other projects:

| File Pattern | Principle | Preset Availability |
|--------------|-----------|---------------------|
| README.md | `readme` | All presets |
| CONTRIBUTING.md | `contributing` | All presets |
| LICENSE | `license` | All presets |
| CODE_OF_CONDUCT.md | `code-of-conduct` | light+ |
| SECURITY.md | `security` | light+ |
| CHANGELOG.md | `changelog` | standard+ |
| .gitignore | (automatic) | All presets |
| .github/ISSUE_TEMPLATE/* | `issue-templates` | standard+ |
| .github/PULL_REQUEST_TEMPLATE.md | `pr-template` | standard+ |
| .github/workflows/ci.yml | `ci-workflow` | strict+ |
| .github/workflows/pr-validation.yml | `ci-workflow` | strict+ |
| .pre-commit-config.yaml | `secrets-detection` | strict+ |
| docs/adr/README.md | `adr` | strict+ |
| docs/adr/template.md | `adr` | strict+ |
| docs/adr/0001-*.md | `adr` | strict+ |
| GLOSSARY.md | `glossary` | enterprise |
| ROADMAP.md | `roadmap` | enterprise |
| MAINTAINERS.md | `maintainers` | enterprise |

### Tier 2: Strong Generation Candidates (v3.8.0)

Files that should be added to PFT's generation capabilities:

| File | Proposed Principle | Priority | Rationale |
|------|-------------------|----------|-----------|
| `.github/CODEOWNERS` | `codeowners` | **High** | Simple pattern, widely useful for team projects |
| `MIGRATION.md` | `migration` | **Medium** | Essential for projects with version upgrades |

**CODEOWNERS Analysis**:
```
# Current PFT CODEOWNERS (15 lines)
- Default owner pattern
- Category-specific owners (ethics, docs)
- Simple, template-friendly format
```

**MIGRATION.md Analysis**:
```
# Current PFT MIGRATION.md structure
- Version-specific migration sections
- Before/After code examples
- Breaking change documentation
- New feature highlights
```

### Tier 3: Future Generation Candidates (v3.9.0+)

Files with generation potential for specific use cases:

| File | Potential Principle | Priority | Use Case |
|------|---------------------|----------|----------|
| `ACKNOWLEDGMENTS.md` | `acknowledgments` | Medium | Projects with community contributions |
| `SEMANTIC_VERSIONING.md` | Extend `versioning` | Low | Projects needing versioning philosophy docs |
| `docs/case-studies/README.md` | `case-studies` | Low | Established projects documenting adoption |
| `docs/case-studies/template.md` | `case-studies` | Low | Template for success stories |

### Tier 4: PFT-Unique (Not for Generation)

Files specific to PFT's unique mission:

| File | Why Not Generated |
|------|-------------------|
| `ETHICS.md` | Principle Zero is PFT-specific philosophy |
| `CLAUDE.md` | LLM integration guide specific to this project |
| `docs/ethical-review/*` | Ethical review process tied to Principle Zero |
| `docs/dogfood/*` | Meta-documentation about PFT's self-governance |
| `generate_foundation.py` | PFT's core generator |
| `core/*` | PFT's internal implementation |
| `tests/*` | PFT's test suite |

### Tier 5: Infrastructure (Not Governance)

Files that are project infrastructure, not governance documentation:

| File | Category |
|------|----------|
| `requirements.txt` | Python dependencies (covered by language configs) |
| `requirements-dev.txt` | Python dev dependencies |
| `.idea/*` | IDE configuration (user-specific) |
| `.pytest_cache/*` | Test cache (auto-generated) |
| `scripts/*` | Operational automation |
| `examples/*` | Plugin examples |
| `foundation/*` | Legacy package |

---

## Detailed Analysis by Category

### Root-Level Governance Files

| File | Current Status | Generation Status | Recommendation |
|------|---------------|-------------------|----------------|
| README.md | pre-existing, enhanced | Generated | Keep existing pattern |
| CONTRIBUTING.md | pre-existing, enhanced | Generated | Keep existing pattern |
| LICENSE | pre-existing, aligned | Generated | No change needed |
| CODE_OF_CONDUCT.md | generated, customized | Generated | v3.7.0 adoption |
| SECURITY.md | generated, customized | Generated | v3.7.0 adoption |
| CHANGELOG.md | pre-existing, enhanced | Generated | Keep existing pattern |
| .gitignore | pre-existing, aligned | Generated | No change needed |
| ETHICS.md | unique | Not generated | PFT-specific |
| CLAUDE.md | unique | Not generated | PFT-specific |
| GLOSSARY.md | pre-existing, enhanced | Generated | Template exists |
| ACKNOWLEDGMENTS.md | unique | **Candidate** | v3.9.0 |
| SEMANTIC_VERSIONING.md | unique | **Candidate** | Extend versioning guide |
| ROADMAP.md | pre-existing, enhanced | Generated | Template exists |
| MIGRATION.md | unique | **Candidate** | v3.8.0 |

### GitHub Configuration

| File | Current Status | Generation Status | Recommendation |
|------|---------------|-------------------|----------------|
| .github/CODEOWNERS | unique | **Candidate** | v3.8.0 - High priority |
| .github/ISSUE_TEMPLATE/bug_report.md | pre-existing, enhanced | Generated | Keep existing |
| .github/ISSUE_TEMPLATE/feature_request.md | pre-existing, enhanced | Generated | Keep existing |
| .github/PULL_REQUEST_TEMPLATE.md | pre-existing, enhanced | Generated | Keep existing |
| .github/workflows/ethical-review-check.yml | unique | Not generated | PFT-specific |

### Documentation Structure

| Directory | Current Status | Generation Status | Recommendation |
|-----------|---------------|-------------------|----------------|
| docs/adr/ | pre-existing, enhanced | Generated | Keep existing |
| docs/ethical-review/ | unique | Not generated | PFT-specific |
| docs/case-studies/ | unique | **Candidate** | v3.9.0+ for mature projects |
| docs/dogfood/ | unique | **Candidate** | v3.8.0 via dogfooding principle |

---

## Generation Potential by Preset

### Minimal Preset (Current: 3 principles)
No additional files recommended.

### Light Preset (Current: 6 principles)
No additional files recommended.

### Standard Preset (Current: 9 principles)
No additional files recommended.

### Strict Preset (Current: 12 principles)
| Candidate | Recommendation |
|-----------|----------------|
| MIGRATION.md | Add in v3.8.0 |

### Enterprise Preset (Current: 30 principles)
| Candidate | Recommendation |
|-----------|----------------|
| CODEOWNERS | Add in v3.8.0 |
| MIGRATION.md | Add in v3.8.0 |
| ACKNOWLEDGMENTS.md | Consider for v3.9.0 |

---

## Template Improvement Patterns

Beyond new files, existing templates can be improved based on PFT's enhanced versions:

### README.md Improvements

| Pattern | Source | Template Enhancement |
|---------|--------|---------------------|
| Audience matrix | PFT README lines 15-30 | Add "Who is This For?" section |
| Non-goals section | PFT README lines 45-60 | Add "What This Is Not" clarifications |
| Philosophy section | PFT README lines 65-90 | Add project values placeholder |
| Version history table | PFT README lines 300-320 | Add version highlights template |

### CONTRIBUTING.md Improvements

| Pattern | Source | Template Enhancement |
|---------|--------|---------------------|
| Commit scopes | PFT CONTRIBUTING lines 121-134 | Add [CUSTOMIZE] scopes table |
| Educational review | PFT CONTRIBUTING lines 171-232 | Add project values checklist |
| Attribution policy | PFT CONTRIBUTING lines 547-592 | Add attribution section |

### PR Template Improvements

| Pattern | Source | Template Enhancement |
|---------|--------|---------------------|
| Educational context | PFT PR_TEMPLATE lines 5-15 | Add WHY section |
| Project-specific review | PFT PR_TEMPLATE lines 30-60 | Add values checklist placeholder |

### ADR README Improvements

| Pattern | Source | Template Enhancement |
|---------|--------|---------------------|
| Philosophy paragraph | PFT docs/adr/README lines 82-89 | Add decision reasoning guidance |

---

## Implementation Roadmap

### v3.8.0 (Dogfooding Insights)

**New Principles**:
1. `codeowners` - Generate `.github/CODEOWNERS`
2. `migration` - Generate `MIGRATION.md`
3. `dogfooding` - Generate `docs/dogfood/README.md` (opt-in)

**Template Improvements**:
- README: Audience matrix, non-goals section
- CONTRIBUTING: Commit scopes, educational review
- PR Template: Educational context
- ADR README: Philosophy paragraph

### v3.9.0 (Community Features)

**Candidates**:
1. `acknowledgments` - Generate `ACKNOWLEDGMENTS.md`
2. `case-studies` - Generate case study scaffold
3. Extend `versioning` to generate `SEMANTIC_VERSIONING.md`

### Future Considerations

| Feature | Complexity | Value | Priority |
|---------|------------|-------|----------|
| Ethical review templates | High | Niche | Low |
| Operational scripts | Medium | Niche | Low |
| IDE configurations | Low | Controversial | None |

---

## Files Explicitly NOT for Generation

These files should remain PFT-specific:

| File | Reason |
|------|--------|
| `ETHICS.md` | Principle Zero is PFT's unique philosophy |
| `CLAUDE.md` | LLM integration is context-specific |
| `docs/ethical-review/*` | Tied to Principle Zero implementation |
| `docs/dogfood/DELTA_ANALYSIS.md` | PFT's specific comparison results |
| `docs/dogfood/FILE_INVENTORY_ANALYSIS.md` | This meta-analysis |
| `generate_foundation.py` | PFT's generator implementation |
| `core/*`, `tests/*` | Internal implementation |

---

## Cross-Reference: GENERATION_LOG.md

This analysis informs updates to [GENERATION_LOG.md](../../GENERATION_LOG.md), which now includes:

- All root governance files
- GitHub configuration (including CODEOWNERS)
- Ethical review documentation
- Case study framework
- Operational scripts
- Development infrastructure

---

## Conclusion

The file inventory analysis reveals:

1. **PFT generates most governance files** - 18+ file patterns already covered
2. **Three strong candidates for v3.8.0** - CODEOWNERS, MIGRATION.md, dogfooding principle
3. **Template improvements matter more than new files** - Existing templates can be enhanced
4. **PFT-unique files should stay unique** - Ethics, LLM integration, meta-documentation

The dogfooding exercise demonstrates that PFT's governance exceeds its own templates in many areas, validating both the template quality and the project's maturity.

---

*This analysis supports [ADR-0011: PFT Self-Governance](../adr/0011-pft-self-governance.md)*
