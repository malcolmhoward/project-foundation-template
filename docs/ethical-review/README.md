# Ethical Review Process

This document explains how ethical reviews are conducted for Project Foundation Template, ensuring all changes align with our [Ethical Framework](../../ETHICS.md) and Principle Zero.

---

## Overview

Ethical review is **mandatory** for all feature proposals and pull requests. This is not bureaucracy—it's how we ensure every change passes the "Do No Harm, Allow No Harm" test before affecting users.

### Why Ethical Review Matters

Project Foundation Template generates governance files that people rely on for their projects. A flaw in our templates could:
- Create security vulnerabilities across many projects
- Enable bad actors to create professional-looking malicious repositories
- Mislead users about compliance status
- Contribute to "governance theater" (appearance without substance)

Ethical review prevents these outcomes by requiring documented consideration of potential harms **before** implementation.

---

## The Review Process

### Stage 1: Feature Proposal (Issue)

When proposing a new feature, the contributor must complete:

#### Principle Zero Assessment

Every feature must explicitly address three types of potential harm:

| Harm Type | Question | Documentation Required |
|-----------|----------|------------------------|
| **Direct Harm** | Could this directly cause harm? | Considerations, risks, mitigations |
| **Enabling Harm** | Could this enable others to cause harm? | Considerations, risks, mitigations |
| **Passive Harm** | Could inaction cause harm? | Considerations, risks, mitigations |

**Example - Direct Harm Analysis:**
```markdown
**Considerations**: Could generating security policies mislead users about actual security?
**Identified Risks**: Users might believe generated policies provide real protection
**Mitigations**: Clear "TEMPLATE - CUSTOMIZE" warnings, educational content explaining policies need implementation
```

#### Ethical Pause Questions

Four mandatory questions from ETHICS.md:

1. **Who could be harmed by this?**
   - List all stakeholders who could be negatively affected
   - If none, explain your reasoning

2. **How could this be misused?**
   - Consider bad actors and unintended usage
   - Document potential abuse scenarios

3. **What would happen if this scaled 1000x?**
   - Consider mass generation, automation
   - Think about cumulative ecosystem effects

4. **Would we be comfortable if this appeared in a news headline?**
   - "PFT adds feature that enables X"
   - Consider public perception

### Stage 2: Implementation (Pull Request)

When submitting a PR, the contributor must:

1. **Self-assess** that ethical considerations were addressed
2. **Summarize** key findings from the linked issue's ethical review
3. **Document** any new ethical considerations discovered during implementation

A **reviewer must verify**:
- Ethical review documentation exists and is complete
- All Principle Zero questions have documented considerations
- All Ethical Pause questions have documented answers
- Identified risks have mitigations OR documented acceptable risk justification

---

## Acceptable Risk

Principle Zero does not mean "zero risk." Some residual risk is acceptable when:

1. **Risk is low** and monitoring is in place
2. **Mitigation is not practical** given technical or resource constraints
3. **Benefits greatly outweigh risks** after careful analysis

### When Accepting Risk

Document:
- Why the risk is acceptable
- What benefits justify accepting the risk
- What monitoring or future mitigations might address it

### Example: Professional-Looking Repository Risk

**Risk**: PFT could help bad actors create professional-looking malicious repositories.

**Why Acceptable**:
- The benefit of simplifying governance education is substantial
- Mitigations exist (ethical agreement, usage logging, template warnings)
- The same risk exists with any documentation tool
- Educational approach reduces "governance theater" which is itself a harm

---

## Review Roles

### Contributor Responsibilities

- Complete all ethical review sections honestly
- Document considerations even when "None identified"
- Raise concerns discovered during implementation
- Update ethical review if scope changes

### Reviewer Responsibilities

- Verify documentation completeness
- Challenge insufficient analysis
- Approve only when satisfied with ethical review quality
- Document reviewer verification with name and date

### Maintainer Responsibilities

- Ensure GitHub Action validation is passing
- Block merges without proper ethical review
- Escalate concerns to project leadership
- Update this process as lessons are learned

---

## Documentation Standards

### What "Documented Considerations" Means

**Insufficient:**
```markdown
**Considerations**: None
**Identified Risks**: None
**Mitigations**: N/A
```

**Sufficient:**
```markdown
**Considerations**: Evaluated whether this feature could be used to generate misleading compliance documentation. Considered impact on users who might not customize templates.
**Identified Risks**: None identified after consideration - feature generates educational content only
**Mitigations**: N/A - no risks identified
```

### Common Mistakes

1. **Skipping sections** - All sections must be completed
2. **Generic responses** - Considerations must be specific to the feature
3. **Missing "why"** - Explain reasoning, not just conclusions
4. **No reviewer verification** - Reviewer must sign off explicitly

---

## Automation

A GitHub Action validates ethical review presence:

- **Validates**: PR description contains required sections
- **Checks**: Contributor checkboxes are present
- **Verifies**: Reviewer verification section exists
- **Fails**: If ethical review sections are missing

The action does **not** validate quality—that requires human review.

---

## Related Documents

- [ETHICS.md](../../ETHICS.md) - Full ethical framework
- [TEMPLATE.md](./TEMPLATE.md) - Reusable ethical review template
- [historical-audits.md](./historical-audits.md) - Retroactive reviews for past versions

---

## Process Evolution

This process will evolve based on:
- Lessons learned from actual reviews
- Community feedback
- Changes to the ethical framework

Suggestions for improvement are welcome via issues or PRs to this document.

---

*Last updated: January 2026*
