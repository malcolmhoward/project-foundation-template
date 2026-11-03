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
GitHub Actions is free for public repositories that use standard GitHub-hosted
runners (terms can change), and integrates directly with pull requests.
(Reference: https://docs.github.com/en/actions/automating-builds-and-tests,
https://docs.github.com/en/billing/managing-billing-for-your-products/managing-billing-for-github-actions/about-billing-for-github-actions)

A basic CI workflow runs tests, linting, and builds on every PR, giving
reviewers confidence that the code works.

The generated workflow fails until you replace its "Run checks" step with
your project's commands: a green run that checked nothing would give that
confidence falsely.
"""
