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

The Conventional Commits specification (conventionalcommits.org)
provides a lightweight convention for commit messages.

Format: <type>(<scope>): <description>

Types:
- feat: New feature (triggers minor version bump)
- fix: Bug fix (triggers patch version bump)
- docs: Documentation only
- style: Formatting, no code change
- refactor: Code restructuring
- test: Adding or fixing tests
- chore: Maintenance tasks
- BREAKING CHANGE: Major version bump

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
