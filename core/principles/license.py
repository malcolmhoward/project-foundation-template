# core/principles/license.py
# License Selection principle

"""
License Selection Principle.

A license defines the legal terms for use and contribution. Without one,
"all rights reserved" applies by default, preventing adoption.
"""

PRINCIPLE_ID = "license"

PRINCIPLE = {
    "name": "License Selection",
    "why": "Defines legal terms for use and contribution",
    "what": "Clear intellectual property terms",
    "risk": "Without it, legal ambiguity prevents adoption",
}

EDUCATION = """
📚 LEARNING: No license means "all rights reserved" by default.

Without a license, others legally cannot use, modify, or contribute
to your project. This is the opposite of what most people intend.

Choose MIT for maximum freedom, GPL for copyleft, or Apache for
patent protection. When in doubt, use MIT.
"""
