## Summary
<!-- Brief description of changes -->

## Type of Change
- [ ] Bug fix (non-breaking change that fixes an issue)
- [ ] New feature (non-breaking change that adds functionality)
- [ ] Breaking change (fix or feature that would cause existing functionality to change)
- [ ] Documentation update

## Related Issues
<!-- Link any related issues: Fixes #123, Relates to #456 -->

## Educational Context
<!-- Explain WHY these changes matter, not just WHAT they do -->

---

## Ethical Review

*Principle Zero and the Ethical Pause are defined in [ETHICS.md](https://github.com/malcolmhoward/project-foundation-template/blob/main/ETHICS.md).*

### Contributor Self-Assessment
*Required: Check each box that is fully true and provide documentation below*

- [ ] Principle Zero test completed with documented considerations (in linked issue or below)
- [ ] Ethical Pause taken with documented analysis (in linked issue or below)
- [ ] Identified risks have mitigations OR documented acceptable risk justification

**New concerns found during implementation**: <!-- "None", or list each one with its tracking issue -->

**Summary of Ethical Considerations**:
<!-- Briefly summarize key ethical considerations from the linked issue -->

**Link to Ethical Review**: <!-- Link to issue with completed Principle Zero and Ethical Pause sections, OR complete sections below for PRs without issues -->

<details>
<summary>Ethical Review Details (expand if not in linked issue)</summary>

#### Principle Zero Assessment

**Direct Harm Considerations**:
<!-- What potential direct harms were considered? -->

**Enabling Harm Considerations**:
<!-- What misuse potential was considered? -->

**Passive Harm Considerations**:
<!-- What passive harm risks were considered? Include what the change leaves out: if content was removed or not added (for example, a claim that couldn't be verified), say what readers lose, and whether that is mitigated or accepted, and why. -->

#### Ethical Pause Answers

1. **Who could be harmed?**
<!-- Answer -->

2. **How could this be misused?**
<!-- Answer -->

3. **What if this scaled 1000x?**
<!-- Answer -->

4. **News headline test?**
<!-- Answer -->

</details>

---

### Reviewer Verification
*Required: A maintainer completes this section before merge. These boxes record the reviewer's judgement; the ethical-review check confirms only that the sections are present, because the PR's author can edit this description. Merging into `main` requires an approving review; when an administrator merges without one, these boxes are the record of the review.*

> Notes under each item are pre-review evidence prepared by the PR's author (or the AI assistant that helped), not a sign-off; the maintainer ticks each box. A box that is only partly true stays unticked, with a note naming what is missing; a tick records that the statement is fully true at merge time.

- [ ] The Principle Zero and Ethical Pause sections are complete
  - Evidence: <!-- where each section is answered -->
- [ ] Every identified risk has a mitigation or a documented justification, and no critical risk is accepted without a mitigation
  - Evidence: <!-- Start with the totals: how many risks are mitigated, how many are accepted, and whether any is critical. Then give each risk named above its own line, in whichever of the two forms below fits it, including risks from what the change leaves out. Delete the example lines you don't use, or write "No risks identified." -->
    - **Risk: <!-- what could go wrong, in one sentence -->** **Mitigated:** <!-- what prevents or limits it, with a link to the code, test, or doc -->
    - **Risk: <!-- what could go wrong, in one sentence -->** **Accepted. Justification:** <!-- why it is acceptable without a mitigation -->
- [ ] Educational value preserved
  - Evidence: <!-- what the change still teaches, and where -->
- [ ] Independently reviewed by someone other than the author: a person, or a different AI model from a fresh context (see CONTRIBUTING.md, Independent Review)
  - Evidence: <!-- who or what reviewed it (for an AI model: model and version, fresh context, effort if known); what it checked; what it found and where that was fixed; its limits (for example, same provider as the author) -->

**Reviewer**: @<!-- GitHub username -->
**Review Date**: <!-- YYYY-MM-DD -->
**Notes**:
<!-- Any additional ethical considerations, concerns, or observations -->

---

## Code Quality Checklist
- [ ] Code follows existing patterns
- [ ] Comments explain the WHY, not the WHAT
- [ ] No unnecessary complexity added

## Testing Checklist
- [ ] Generator runs without errors
- [ ] Generated files are valid
- [ ] Ethical safeguards function correctly

## Documentation Checklist
- [ ] README updated (if needed)
- [ ] CLAUDE.md updated (if needed)
- [ ] Version updated (if applicable)

---
*This project prioritizes education over automation. PRs should help users understand better, not just do more.*
*See [Ethical Review Process](docs/ethical-review/README.md) for guidance on completing the ethical review.*
