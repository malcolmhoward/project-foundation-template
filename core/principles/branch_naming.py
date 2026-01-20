# core/principles/branch_naming.py
# Branch Naming principle (v3.3.0)

"""
Branch Naming Principle.

Consistent branch naming conventions improve collaboration,
automation compatibility, and project organization.

Introduced in v3.3.0.
"""

PRINCIPLE_ID = "branch-naming"

PRINCIPLE = {
    "name": "Branch Naming Convention",
    "why": "Consistent branch names improve automation and collaboration",
    "what": "Standards for naming branches based on their purpose",
    "risk": "Without it, confusion about branch purposes and broken automation workflows",
}

EDUCATION = """
📚 LEARNING: Branch naming conventions enable automation and clarity.

Common branch naming patterns:
- feature/description - New features
- fix/description - Bug fixes
- hotfix/description - Urgent production fixes
- docs/description - Documentation changes
- refactor/description - Code restructuring
- test/description - Test additions or fixes
- chore/description - Maintenance tasks

Benefits of consistent naming:
- CI/CD can trigger different workflows per branch type
- Team members understand branch purpose at a glance
- Pull request templates can be auto-selected
- Branch cleanup automation becomes possible

Include issue numbers when applicable:
- feature/123-add-user-auth
- fix/456-login-validation
"""
