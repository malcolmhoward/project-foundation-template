# core/principles/conventional_commits.py
# Conventional Commits principle (v3.3.0)

"""
Conventional Commits Principle.

A standardized commit message format that enables automated
changelog generation and semantic versioning.

Introduced in v3.3.0.
"""

PRINCIPLE_ID = "conventional-commits"

PRINCIPLE = {
    "name": "Conventional Commits",
    "why": "Standardized commit messages enable automation and clarity",
    "what": "A specification for structured commit messages with type, scope, and description",
    "risk": "Without it, commit history is hard to parse and changelog generation is manual",
}

EDUCATION = """
📚 LEARNING: Conventional Commits enable automated workflows.

The Conventional Commits specification provides a lightweight convention for
commit messages.
(Reference: https://www.conventionalcommits.org/en/v1.0.0/)

Format: <type>(<scope>): <description>

Types:
- feat: New feature (correlates with a MINOR version bump in SemVer)
- fix: Bug fix (correlates with a PATCH version bump)
- docs: Documentation only
- style: Formatting, no code change
- refactor: Code restructuring
- test: Adding or fixing tests
- chore: Maintenance tasks

Breaking changes are not a type: mark them with `!` before the colon
(feat!: ...) or a `BREAKING CHANGE:` footer. Either correlates with a MAJOR
version bump. The specification defines only feat and fix; the other types
above are a common convention it allows.

Benefits:
- Automated changelog generation
- Semantic version determination
- Clear commit history
- Easier code review
- Triggering specific CI/CD workflows

Example:
feat(auth): add password reset functionality

Implements password reset via email verification.
Users receive a time-limited token.

Closes #234
"""
