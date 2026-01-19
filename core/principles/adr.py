# core/principles/adr.py
# Architecture Decision Records principle (v2.5.0)

"""
Architecture Decision Records Principle.

ADRs preserve institutional knowledge by capturing the context,
decision, and consequences of architectural choices.

Introduced in v2.5.0.
"""

PRINCIPLE_ID = "adr"

PRINCIPLE = {
    "name": "Architecture Decision Records",
    "why": "Teams forget why decisions were made, leading to repeated debates or reversed progress",
    "what": "Lightweight documents capturing context, decision, and consequences of architectural choices",
    "risk": "Without ADRs, institutional knowledge leaves when team members do",
}

EDUCATION = """
📚 LEARNING: Architecture Decision Records preserve institutional knowledge.

Michael Nygard introduced ADRs in 2011 as a way to capture the 'why' behind
architectural decisions. Without them, teams often reverse good decisions
because they don't understand the original context.
(Reference: https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions)

ADRs are lightweight - just markdown files with context, decision, and
consequences. They're versioned with the code they describe.
"""
