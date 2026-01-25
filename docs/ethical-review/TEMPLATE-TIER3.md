# Ethical Review Template - Tier 3 (Minimal)

This minimal template is for **Tier 3: Ecosystem Coordinators** - documentation-focused projects, coordination layers, and community resources.

For more comprehensive reviews, see:
- [TEMPLATE-TIER2.md](TEMPLATE-TIER2.md) - Simplified checklist
- [TEMPLATE.md](TEMPLATE.md) - Full review (Tier 1)

---

## When to Use This Template

Use this minimal approach for:
- Coordination/orchestration repositories
- Documentation and guides
- Community resources (build journals, tutorials)
- Getting-started materials

**Escalate to Tier 2** if your change involves:
- Scripts that modify user systems
- Automation that could fail silently
- Security-related documentation
- Content that could be misused for social engineering

---

## Ethical Awareness Statement

Tier 3 projects inherit **Principle Zero** ("Do No Harm, Allow No Harm") from PFT as a guiding philosophy.

Contributors should apply common-sense harm prevention:
- Consider who reads this documentation and how they might use it
- Avoid instructions that could cause harm if followed incorrectly
- Include appropriate warnings for potentially dangerous operations
- Don't provide information that primarily enables malicious use

---

## Embedding in PR Templates

For Tier 3 projects, add this to your PR template:

```markdown
## Ethical Awareness

This project inherits Principle Zero from PFT: "Do No Harm, Allow No Harm"

- [ ] Applied common-sense harm prevention
- [ ] Included appropriate warnings where needed
```

That's it. No detailed review required for documentation and coordination work.

---

## When to Escalate

Consider a more detailed review (Tier 2 or Tier 1) if:

| Situation | Recommended Action |
|-----------|-------------------|
| Change affects user security | Use Tier 2 checklist |
| Script could damage systems if misused | Use Tier 2 checklist |
| Content could enable social engineering | Use Tier 2 checklist |
| Significant automation or tooling | Use Tier 1 full review |

When in doubt, a quick Tier 2 checklist takes only a few minutes and provides peace of mind.

---

*This template inherits from PFT's [ETHICS.md](../../ETHICS.md). See the full framework for context.*
