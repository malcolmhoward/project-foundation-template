# core/principles/changelog.py
# Changelog principle (v2.3.0)

"""
Changelog Principle.

A changelog tells users what to expect from each version,
helping them assess upgrade impact and make informed decisions.

Introduced in v2.3.0.
"""

PRINCIPLE_ID = "changelog"

PRINCIPLE = {
    "name": "Changelog",
    "why": "Users need to know what changed between versions",
    "what": "Human-readable history of notable changes",
    "risk": "Without it, users can't assess upgrade impact",
}

EDUCATION = """
📚 LEARNING: 70% of users check changelogs before upgrading.

A changelog is your project's narrative - it tells users what to
expect from each version. Keep a Changelog format (keepachangelog.com)
is the de facto standard.

Without it, users fear breaking changes and delay upgrades.
"""
