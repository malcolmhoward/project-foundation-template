# ADR 0010: Tiered Ethical Review Framework

## Status

Accepted

## Context

Project Foundation Template (PFT) generates governance files that downstream projects deploy. This creates ethical responsibility: changes to PFT cascade to potentially many projects. However, the ecosystem includes projects with varying relationships to PFT:

1. **PFT itself and core extensions** - Direct impact on all users
2. **Projects using the generator** - Deploy PFT-generated files
3. **Coordination/documentation projects** - Use PFT principles but primarily produce documentation

A one-size-fits-all ethical review process would either:
- Be too heavy for documentation projects (discouraging adoption)
- Be too light for core components (missing potential harms)

We needed a framework that scales ethical rigor to actual risk.

## Decision

Implement a **three-tier ethical review framework** with corresponding templates:

### Tier 1: Core Components (Full Review Required)

**Applies to**: PFT itself, decoupled governance modules, core extensions

**Process**: Full ethical review including:
- Principle Zero assessment (Direct, Enabling, Passive harm)
- Ethical Pause questions (Who harmed? Misuse? Scale? Headlines?)
- Documented mitigations for all identified risks
- Reviewer verification before merge

**Template**: [TEMPLATE.md](../ethical-review/TEMPLATE.md)

### Tier 2: Generated Instances (Review Recommended)

**Applies to**: Projects using PFT generator, projects adopting PFT principles

**Process**: Simplified checklist including:
- Brief Principle Zero checklist (Yes/No with notes)
- Abbreviated Ethical Pause consideration
- Self-certification

**Template**: [TEMPLATE-TIER2.md](../ethical-review/TEMPLATE-TIER2.md)

### Tier 3: Ecosystem Coordinators (Inherit Principles)

**Applies to**: Coordination layers, documentation projects, community resources

**Process**: Minimal ethical awareness:
- Inherit Principle Zero as guiding philosophy
- Common-sense harm prevention
- Escalate to Tier 2 if change has security implications

**Template**: [TEMPLATE-TIER3.md](../ethical-review/TEMPLATE-TIER3.md)

## Alternatives Considered

### Alternative 1: Single Review Process for All

**Rejected because**: The full review process is appropriate for code-generating templates but excessive for documentation. Would discourage ethical review adoption in the ecosystem.

### Alternative 2: No Formal Tiers (Ad-hoc Decisions)

**Rejected because**: Without clear guidance, projects wouldn't know what level of review is appropriate. Inconsistent approaches across ecosystem.

### Alternative 3: Generator Flag (`--ethical-tier`)

**Deferred**: Considered adding a command-line argument to generate tier-appropriate templates:

```bash
python generate_foundation.py --ethical-tier 2 --project-name "MyProject"
```

**Reasoning for deferral**:
1. Most Tier 2/3 projects may not use the PFT generator (they adopt principles manually)
2. Templates are simple enough to copy into PR templates manually
3. Adds code complexity for uncertain demand
4. v3.7.0 scope is already complete

**Future consideration**: If user demand justifies, this could be added in a future version. The tiered structure is designed to support this extension.

## Consequences

### Positive

- **Right-sized review process**: Each project tier gets appropriate ethical rigor
- **Lower adoption barrier**: Tier 3 projects can participate without heavy process
- **Clear guidance**: Projects know exactly what's expected at each level
- **Scalable framework**: Can add generator support later if needed

### Negative

- **Manual template adoption**: Tier 2/3 projects must copy templates manually (for now)
- **Tier judgment required**: Projects must self-assess which tier they belong to
- **Multiple templates to maintain**: Three templates instead of one

### Neutral

- **ETHICS.md complexity increased**: More content, but better organized
- **Documentation overhead**: ADR and templates required upfront investment

## Related

- [ETHICS.md](../../ETHICS.md) - Main ethical framework (updated with tier definitions)
- [ADR 0001: Education First](0001-education-first.md) - Educational philosophy that informed this design
- [Ethical Review Process](../ethical-review/README.md) - Detailed review workflow

## References

- PFT Principle Zero: "Do No Harm, Allow No Harm"
- Risk-based approach to compliance (common in security frameworks)
