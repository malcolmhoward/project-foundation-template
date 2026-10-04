# Ethical Review Template - Tier 2 (Simplified)

This simplified template is for **Tier 2: Generated Instances** - projects that use PFT to generate their governance files or adopt PFT principles.

For full ethical review requirements, see [TEMPLATE.md](TEMPLATE.md) (Tier 1).

---

## When to Use This Template

Use this simplified review for:
- Projects generated using PFT
- Projects adopting PFT governance principles
- Changes to governance files in your project

**Note**: If your change has significant harm potential (security features, automation, code generation), consider using the full Tier 1 template instead.

---

## Quick Ethical Review

**Feature/Change**: [Brief description]
**Date**: YYYY-MM-DD
**Reviewer**: [Name]

### Principle Zero Checklist

Answer each question. If any answer is "Yes" without mitigation, reconsider the change.

| Question | Yes/No | Notes |
|----------|--------|-------|
| Could this directly harm users, systems, or organizations? | | |
| Could this enable others to cause harm more easily? | | |
| Could inaction on this cause harm? | | |

### Ethical Pause (Brief)

| Question | Response |
|----------|----------|
| Who might be affected by this? | |
| Could this be misused? How? | |
| Any concerns at scale? | |

### Conclusion

- [ ] Passes Principle Zero (no unmitigated harms)
- [ ] Considered potential misuse
- [ ] Comfortable with this change

**Decision**: [ ] Approved / [ ] Needs revision / [ ] Escalate to full review

---

## Embedding in PR Templates

For Tier 2 projects, add this to your PR template:

```markdown
## Ethical Consideration

- [ ] No direct harm to users, systems, or organizations
- [ ] Does not enable misuse more easily than alternatives
- [ ] Considered who might be affected by this change

**Brief notes** (optional):
<!-- Any ethical considerations worth noting -->
```

---

*This template inherits from PFT's [ETHICS.md](../../ETHICS.md). See the full framework for context.*
