# core/principles/maintainers.py
# Maintainers principle (v3.1.0)

"""
Maintainers Principle.

A maintainers document identifies who maintains the project,
their roles, and how others can become maintainers.

Introduced in v3.1.0.
"""

PRINCIPLE_ID = "maintainers"

PRINCIPLE = {
    "name": "Maintainers",
    "why": "Contributors need to know who has authority and responsibility",
    "what": "Documentation of project maintainers, their roles, and succession paths",
    "risk": "Without it, unclear ownership leads to stalled decisions and contributor frustration",
}

EDUCATION = """
📚 LEARNING: Clear maintainership tells contributors who decides and who to ask.

A MAINTAINERS file establishes:
- Who can merge pull requests
- Who triages issues
- Who makes release decisions
- How to become a maintainer

Documenting it makes ownership and decision-making visible, and helps
potential contributors know who to contact.
"""
