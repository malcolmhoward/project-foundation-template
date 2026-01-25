# core/principles/enhanced_security.py
# Enhanced Security Policy principle (v2.4.0)

"""
Enhanced Security Policy Principle.

A comprehensive security policy enables responsible vulnerability
disclosure and builds trust with users and security researchers.

Introduced in v2.4.0.
"""

PRINCIPLE_ID = "enhanced-security"

PRINCIPLE = {
    "name": "Enhanced Security Policy",
    "why": "Comprehensive security documentation builds trust and enables responsible disclosure",
    "what": "Detailed SECURITY.md with vulnerability reporting, response timelines, and best practices",
    "risk": "Without clear security processes, vulnerabilities go unreported or are disclosed publicly",
}

EDUCATION = """
📚 LEARNING: A clear security policy enables responsible vulnerability disclosure.

Security researchers need to know how to report issues safely. Without a
SECURITY.md, they may disclose publicly, report to the wrong channel, or
not report at all. GitHub recommends security policies for all public repos.
(Reference: https://docs.github.com/en/code-security/getting-started/adding-a-security-policy-to-your-repository)

Key elements: Supported versions, reporting process, response timeline, and
security best practices specific to your project.
"""
