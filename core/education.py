# core/education.py
# Educational content and principles

"""
Education module for Project Foundation Template.

Contains:
    - Governance principles (LITE_PRINCIPLES) - imported from principles/
    - Educational content (EDUCATION_CONTENT) - imported from principles/
    - Ethical use agreement
    - Display formatting helpers

Note: As of v2.8.0, principles are defined in core/principles/ modules.
This module re-exports them for backward compatibility.
"""

from core.principles import (
    ALL_PRINCIPLES as LITE_PRINCIPLES,
    ALL_EDUCATION as EDUCATION_CONTENT,
    get_principle,
    get_education as get_education_content,
)

# Ethical use agreement that must be acknowledged
ETHICAL_USE_AGREEMENT = """
╔══════════════════════════════════════════════════════════════════════════════╗
║                     ETHICAL USE AGREEMENT - PLEASE READ                       ║
╠══════════════════════════════════════════════════════════════════════════════╣
║                                                                                ║
║  By using this tool, you acknowledge and agree that:                          ║
║                                                                                ║
║  1. This generates TEMPLATES ONLY - not complete solutions                    ║
║  2. Templates MUST be customized for your specific needs                      ║
║  3. This does NOT provide legal or compliance advice                          ║
║  4. This does NOT make your project automatically secure                      ║
║  5. This does NOT constitute professional security consultation               ║
║  6. You will implement these practices, not just generate documents           ║
║  7. You will not misrepresent templates as professional compliance            ║
║  8. You accept full responsibility for how you use these templates            ║
║                                                                                ║
║  Misrepresenting these templates as actual compliance or security             ║
║  certification may constitute fraud and could result in:                      ║
║  - Legal penalties                                                            ║
║  - Data breaches                                                              ║
║  - Loss of user trust                                                         ║
║  - Personal liability                                                         ║
║                                                                                ║
║  This tool exists to democratize best practices and education.                ║
║  Please use it responsibly and ethically.                                     ║
║                                                                                ║
╚══════════════════════════════════════════════════════════════════════════════╝
"""


def format_principle_display(name: str) -> str:
    """Format a principle for display.

    Args:
        name: Principle identifier

    Returns:
        Formatted string for terminal display, or empty string if not found
    """
    principle = get_principle(name)
    if not principle:
        return ""

    return f"""
╔══════════════════════════════════════════════════════════════════════════════╗
║  📖 {principle['name']:<70} ║
╠══════════════════════════════════════════════════════════════════════════════╣
║  WHY: {principle['why']:<68} ║
║  WHAT: {principle['what']:<67} ║
║  RISK: {principle['risk']:<67} ║
╚══════════════════════════════════════════════════════════════════════════════╝
"""
