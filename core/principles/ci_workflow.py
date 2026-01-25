# core/principles/ci_workflow.py
# CI/CD Workflow principle (v2.5.0)

"""
CI/CD Workflow Principle.

Continuous Integration ensures that every change is automatically tested,
catching issues before they reach production.

Introduced in v2.5.0.
"""

PRINCIPLE_ID = "ci-workflow"

PRINCIPLE = {
    "name": "CI/CD Workflow",
    "why": "Manual testing is error-prone and inconsistent",
    "what": "GitHub Actions workflow for automated testing, linting, and validation",
    "risk": "Without CI, bugs slip through and code quality degrades over time",
}

EDUCATION = """
📚 LEARNING: CI/CD catches issues before they reach production.

Continuous Integration ensures that every change is automatically tested.
GitHub Actions provides free CI for public repositories and integrates
directly with pull requests.
(Reference: https://docs.github.com/en/actions/automating-builds-and-tests)

A basic CI workflow runs tests, linting, and builds on every PR, giving
reviewers confidence that the code works.
"""
