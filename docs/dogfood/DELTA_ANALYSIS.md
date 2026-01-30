# Delta Analysis: PFT Dogfooding

**Generated**: 2026-01-30
**Preset Used**: strict
**PFT Version**: 3.7.0

This document captures insights from running Project Foundation Template against itself. Every comparison informs template improvements, even when keeping existing files.

---

## Executive Summary

Running PFT with `--preset strict` against itself reveals a **template-for-template** scenario where:
- Generated output provides solid **baseline governance scaffolding**
- Existing PFT files demonstrate **mature, ethically-grounded governance**
- The gap between them shows what projects grow into over time

Key findings:
1. **Ethical integration** is the primary differentiator between generated and existing templates
2. **Educational philosophy** (WHAT/WHY/HOW) permeates existing docs but is minimal in generated output
3. **Template improvements** identified: audience matrix, "What This Is Not" sections, commit scopes

---

## File Comparison Summary

| Generated File | Existing? | Action | Key Insight |
|---------------|-----------|--------|-------------|
| README.md | Yes | Keep existing | Existing is 7x more comprehensive with audience matrix, philosophy, 30 principles |
| CONTRIBUTING.md | Yes | Keep existing | Existing has ethical review criteria, 12 commit scopes, attribution policy |
| LICENSE | Yes | Keep existing | MIT license, identical intent |
| .gitignore | Yes | Keep existing | Existing is project-specific |
| CODE_OF_CONDUCT.md | No | **Add** | Contributor Covenant v2.0 with customization needed |
| SECURITY.md | No | **Add** | Comprehensive security policy with disclosure process |
| CHANGELOG.md | Yes | Keep existing | Existing has real version history |
| .github/ISSUE_TEMPLATE/* | Yes | Keep existing | Existing has Principle Zero integration |
| .github/PULL_REQUEST_TEMPLATE.md | Yes | Keep existing | Existing has ethical review sections |
| .github/workflows/*.yml | Partial | Keep existing | Existing has ethical-review-check.yml |
| .pre-commit-config.yaml | No | **Consider** | Secrets detection scaffolding |
| docs/adr/README.md | Yes | Keep existing | Existing has 10 ADRs with philosophy |
| docs/adr/template.md | No | **Add** | Structured ADR template with options comparison |

---

## Detailed Analysis by File Category

### 1. README.md

**Generated**: Minimal template starter (54 lines) with placeholders
**Existing**: Comprehensive project guide (357 lines) with progressive disclosure

#### Where Existing Exceeds Template

| Feature | Existing Has | Generated Lacks |
|---------|--------------|-----------------|
| Audience Matrix | "Who is This For?" with 5 personas | Generic audience assumption |
| Educational Framework | WHAT/WHY/HOW/RISK model | Template notice only |
| Philosophy | Principle Zero explanation | No ethical context |
| Non-Goals | "What This Is Not" (4 items) | Brief footer notice |
| Quick Start Paths | 4 scenarios (interactive, preset, CI/CD, discovery) | Single placeholder |
| Governance Visualization | Preset hierarchy diagram | No preset info |
| Principles Reference | All 30 principles by category | None |
| Project Structure | Detailed file tree | None |
| Version History | v1-v3.7 with highlights | None |

#### Template Improvement Opportunities

1. **Add "What This Is Not" section pattern** - Prevents misuse by clarifying non-goals
2. **Add audience matrix option** - Helps users self-identify quickly
3. **Expand Quick Start with multiple paths** - Reduces friction for different user types
4. **Include documentation index template** - Guides maintainers on what docs to create

---

### 2. CONTRIBUTING.md

**Generated**: 313 lines, basic workflow + code standards
**Existing**: 605 lines, comprehensive with ethical review integration

#### Where Existing Exceeds Template

| Feature | Existing Has | Generated Lacks |
|---------|--------------|-----------------|
| Philosophy Anchor | Links to ETHICS.md, ADR-0001 | No philosophical grounding |
| Commit Scopes | 6 project-specific scopes | Generic type only |
| Educational Review | Ethical alignment + value checklists | Technical review only |
| Contribution Types | Detailed guidance for 4 types | Mentioned in PR checklist only |
| Adding Principles | 7-step comprehensive process | No extension guidance |
| Adding Guides | Similar comprehensive process | No extension guidance |
| Attribution Policy | Anonymous default, opt-in named | None |

#### Template Improvement Opportunities

1. **Add placeholder for project values/ethics link** - Philosophy anchoring
2. **Add [CUSTOMIZE] scopes table** - Make commit history navigable
3. **Extend review section with project-specific evaluation** - Beyond technical
4. **Add section for "contributing extensions"** - Self-directed contribution

---

### 3. GitHub Issue Templates

#### Bug Report

**Generated**: Generic, 40 lines, practical
**Existing**: PFT-specific, 33 lines, educational disclaimer

Key differences:
- Generated uses `[Bug]:`, existing uses `[BUG]` (title format inconsistency)
- Generated adds 'triage' label for workflow management
- Existing asks for Python Version, Template Version (domain-specific)
- Existing includes educational reminder about customizing files

#### Feature Request

**Generated**: 31 lines, problem-solution focus
**Existing**: 111 lines, full ethical review framework

Critical difference: Existing includes:
- Principle Zero Assessment (Direct/Enabling/Passive Harm)
- Ethical Pause with 4 critical questions
- Educational value requirements
- Risk assessment with mitigation documentation

**Template Improvement**: Consider "strict" or "ethical" preset option that includes Principle Zero assessments in templates.

#### Pull Request Template

**Generated**: 33 lines, standard engineering format
**Existing**: 101 lines, ethical review as first-class concern

Existing includes:
- Educational Context section (WHY, not just WHAT)
- Contributor Self-Assessment (4 ethical checkboxes)
- Reviewer Verification (3 ethical checkboxes)
- Links to ethical review process documentation

---

### 4. ADR System

**Generated**: Basic ADR README + template + 0001
**Existing**: 10 established ADRs with educational philosophy

| Aspect | Generated | Existing |
|--------|-----------|----------|
| ADR Count | 1 (0001) | 10 (0001-0010) |
| Philosophy Section | Absent | Education-first approach |
| Template Format | YAML frontmatter style | Markdown sections |
| Unique Sections | "Options Considered" + "History" | None (simpler) |

**Template Improvement**: Add minimal philosophy paragraph to generated ADR README.

---

### 5. CI/CD Workflows

**Generated**: ci.yml (basic matrix), pr-validation.yml (conventional commits)
**Existing**: ethical-review-check.yml (188 lines, sophisticated)

The existing ethical-review-check.yml:
- Validates PR has ethical review sections
- Checks contributor and reviewer checkboxes
- Adds conditional labels based on completion
- References ETHICS.md and ethical review docs

**Decision**: Ethical review workflows should NOT be generated—they're project-specific. This is correct tiering.

---

## Files to Add to PFT

### CODE_OF_CONDUCT.md

Based on Contributor Covenant v2.0. Customization needed:
- Define enforcement team and contact method
- Add PFT-specific behavioral expectations
- Establish escalation path
- Add Principle Zero acknowledgment

### SECURITY.md

Comprehensive security policy. Customization needed:
- Replace placeholder email
- Update version support table for PFT
- Add governance template-specific security considerations
- Document dependency review approach

### docs/adr/template.md

Structured ADR template. Consider extending:
- Add "Principle Alignment" field
- Add "Educational Value" section
- Add governance-specific examples

---

## Template Improvement Issues

The following patterns from existing PFT files could improve generated templates:

### High Priority

1. **README: "Who is This For?" pattern**
   - Audience matrix with personas
   - Helps users self-identify
   - Reduces support burden

2. **README: "What This Is Not" section**
   - Prevents common misconceptions
   - Sets realistic expectations
   - Reduces misuse potential

3. **CONTRIBUTING: Commit scope table**
   - [CUSTOMIZE] placeholder
   - Improves history navigability
   - Domain-specific organization

### Medium Priority

4. **CONTRIBUTING: Educational review criteria**
   - Placeholder for project values
   - Beyond technical review
   - Teaches thoughtful contribution

5. **PR Template: Educational context section**
   - WHY emphasis
   - Not just WHAT changed
   - Supports knowledge transfer

6. **ADR README: Philosophy paragraph**
   - Minimal guidance on decision reasoning
   - Focus on WHY, not just WHAT
   - Supports long-term maintenance

### Lower Priority (Preset-Specific)

7. **Feature Request: Ethical assessment option**
   - For "strict" or "ethical" preset
   - Principle Zero integration
   - Harm category analysis

8. **PR Template: Ethical verification option**
   - For projects with ethical frameworks
   - Two-phase verification pattern
   - Link to ethics documentation

---

## Structural Insights

### Tiering is Correct

Generated templates provide **baseline governance** appropriate for new projects. The gap between generated and existing reflects what projects should grow into, not what they need on day one.

### Educational Philosophy Matters

The primary differentiator is WHAT/WHY/HOW framing:
- Generated: Procedural (how to report bugs, submit PRs)
- Existing: Educational (why processes exist, what values they embody)

### Ethical Integration is Project-Specific

Principle Zero and ethical review are deeply integrated into existing templates but inappropriate for generated output. Projects must earn this complexity through experience.

---

## Recommendations

### For This Dogfooding Exercise

1. **Add** CODE_OF_CONDUCT.md (customize enforcement)
2. **Add** SECURITY.md (customize contact info)
3. **Add** docs/adr/template.md (extend with PFT-specific fields)
4. **Keep** all existing files (they exceed template quality)
5. **Document** findings in GENERATION_LOG.md

### For Template Improvements (Future Work)

1. Create GitHub issues for high-priority patterns
2. Consider preset variants with ethical review options
3. Add [CUSTOMIZE] prompts for project-specific values
4. Extend learning comments throughout templates

---

## Conclusion

Dogfooding PFT validates both the template quality and the project's governance maturity. The generated output is appropriate for new projects; the existing files demonstrate what thoughtful governance looks like at scale.

The key insight: **Templates teach basics; practice teaches depth.** PFT's existing files reflect countless decisions about ethical governance that cannot be achieved through generation alone.

---

*This analysis supports ADR-0011: PFT Self-Governance*
