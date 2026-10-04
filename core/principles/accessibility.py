# core/principles/accessibility.py
# Accessibility principle (v3.0.0)

"""
Accessibility Principle.

Accessibility ensures software is usable by people with disabilities,
expanding reach and often improving usability for everyone.

Introduced in v3.0.0.
"""

PRINCIPLE_ID = "accessibility"

PRINCIPLE = {
    "name": "Accessibility",
    "why": "1 billion people worldwide have disabilities; excluding them limits your reach and may violate laws",
    "what": "WCAG compliance, assistive technology support, and inclusive design practices",
    "risk": "Without accessibility, projects exclude users and face legal liability",
}

EDUCATION = """
📚 LEARNING: Accessible websites reach 15% more users and often rank higher in search engines.

Accessibility (a11y) ensures everyone can use your software regardless of ability.
It's both an ethical imperative and increasingly a legal requirement.

**WCAG Guidelines:**
- Level A: Minimum accessibility (required)
- Level AA: Standard compliance (recommended, often legally required)
- Level AAA: Enhanced accessibility (ideal for inclusive organizations)

**Core Principles (POUR):**
- **Perceivable**: Content available to all senses (alt text, captions)
- **Operable**: Interface works with various inputs (keyboard, voice)
- **Understandable**: Content and operation are clear
- **Robust**: Works with assistive technologies

**Common Implementations:**
- Semantic HTML for screen reader compatibility
- Keyboard navigation for all interactive elements
- Color contrast ratios meeting WCAG standards
- Focus indicators for keyboard users
- Alternative text for images and media
- Captions and transcripts for video content

**Testing:**
- Automated tools (axe, Lighthouse, WAVE)
- Screen reader testing (NVDA, VoiceOver, JAWS)
- Keyboard-only navigation testing
- User testing with people who have disabilities

Accessibility improvements often benefit everyone - captions help in noisy
environments, keyboard navigation helps power users, clear design helps everyone.
"""
