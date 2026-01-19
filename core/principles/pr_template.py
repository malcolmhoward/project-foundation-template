# core/principles/pr_template.py
# Pull Request Template principle (v2.3.0)

"""
Pull Request Template Principle.

A PR template sets quality expectations and reminds contributors
to run tests, update docs, and describe their changes.

Introduced in v2.3.0.
"""

PRINCIPLE_ID = "pr-template"

PRINCIPLE = {
    "name": "Pull Request Template",
    "why": "Consistent PR descriptions improve review quality",
    "what": "Checklist ensuring code quality and documentation",
    "risk": "Without it, PRs are inconsistent and harder to review",
}

EDUCATION = """
📚 LEARNING: Projects with PR templates have 50% fewer back-and-forth reviews.

A PR checklist reminds contributors to run tests, update docs, and
describe their changes. It sets quality expectations before review.

Without it, reviewers must manually check for common oversights.
"""
