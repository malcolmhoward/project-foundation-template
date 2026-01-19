# core/guides/code_review.py
# Code Review Guide (v2.9.0)

"""
Code Review Guide.

Provides practical guidance on conducting effective code reviews
that improve code quality and team collaboration.

Introduced in v2.9.0.
"""

GUIDE_ID = "code-review"

GUIDE = {
    "title": "Code Review Guide",
    "purpose": "Learn how to give and receive effective code reviews",
    "audience": "All developers",
    "complexity": "intermediate",
}

RELATED_PRINCIPLES = ["contributing", "pr-template"]

CONTENT = """
# Code Review Guide

## Why Code Reviews Matter

Code reviews:
- Catch bugs before they reach production
- Share knowledge across the team
- Maintain consistent code quality
- Provide learning opportunities

## For Reviewers

### Before You Start
1. Understand the context (read the PR description)
2. Check if tests pass
3. Review in a quiet environment

### What to Look For

**Correctness**
- Does the code do what it's supposed to?
- Are edge cases handled?
- Are error conditions handled?

**Design**
- Is the code in the right place?
- Does it follow existing patterns?
- Is it appropriately abstracted?

**Readability**
- Can you understand it without the author explaining?
- Are names clear and meaningful?
- Is complex logic commented?

**Security**
- Are inputs validated?
- Is sensitive data protected?
- Are there injection vulnerabilities?

**Testing**
- Are there adequate tests?
- Do tests cover edge cases?
- Are tests readable and maintainable?

### How to Give Feedback

**Be Kind**
- Comment on the code, not the person
- Use "we" instead of "you"
- Acknowledge good work

**Be Clear**
- Explain why, not just what
- Provide examples when helpful
- Distinguish must-fix from nice-to-have

**Be Constructive**
- Suggest alternatives
- Ask questions instead of demanding
- Link to relevant documentation

### Example Comments

Instead of:
> "This is wrong."

Write:
> "This might cause issues when X is empty. Consider adding a check for that case."

Instead of:
> "Why did you do it this way?"

Write:
> "I'm curious about the approach here. Would Y approach work? It might handle Z better."

## For Authors

### Before Requesting Review
1. Self-review your changes
2. Ensure tests pass
3. Write a clear PR description
4. Keep PRs small and focused

### Receiving Feedback
- Assume good intent
- Ask for clarification if needed
- Explain your reasoning respectfully
- Thank reviewers for their time

### PR Description Template

```
## What
Brief description of changes

## Why
Context and motivation

## How
Implementation approach

## Testing
How to verify the changes

## Screenshots (if applicable)
```

## Review Checklist

- [ ] Code compiles/lints without errors
- [ ] Tests pass
- [ ] New code has appropriate tests
- [ ] Documentation is updated
- [ ] No security concerns
- [ ] No performance concerns
- [ ] Follows project conventions

## Common Anti-Patterns

1. **Rubber stamping** - Approving without actually reviewing
2. **Nitpicking** - Focusing only on style over substance
3. **Scope creep** - Requesting unrelated changes
4. **Delayed reviews** - Letting PRs sit for days
5. **Large PRs** - Submitting too many changes at once

---

*This guide complements your project's CONTRIBUTING.md and PR template*
"""
