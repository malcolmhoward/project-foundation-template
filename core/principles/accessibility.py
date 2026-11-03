# core/principles/accessibility.py
# Accessibility principle (v2.10.0)

"""
Accessibility Principle.

Accessibility ensures software is usable by people with disabilities,
expanding reach and often improving usability for everyone.

Introduced in v2.10.0.
"""

from core.utils import COMPLIANCE_DISCLAIMER

PRINCIPLE_ID = "accessibility"

PRINCIPLE = {
    "name": "Accessibility",
    "why": "Many people live with disabilities; excluding them limits your reach and may violate laws",
    "what": "WCAG compliance, assistive technology support, and inclusive design practices",
    "risk": "Without accessibility, projects exclude users and may face legal liability",
}

EDUCATION = """
📚 LEARNING: Accessible software reaches more people.

Accessibility (a11y) ensures everyone can use your software regardless of ability.
It's an ethical imperative, and for some software a legal one.

⚖️  """ + COMPLIANCE_DISCLAIMER + """

For example (sources checked October-November 2026):
- US: the Department of Justice's ADA Title II rule makes WCAG 2.1 Level AA the
  technical standard for state and local governments' web content and mobile
  apps, with compliance dates in 2027 and 2028.
  (Reference: https://www.ada.gov/resources/2024-03-08-web-rule/)
- EU: under the European Accessibility Act, Member States' national laws have
  applied since 28 June 2025 to the products and services it lists, with some
  transitional periods; microenterprises providing services are exempt
  (Directive (EU) 2019/882, Arts. 2, 4(5), 31). Whether it applies to your
  project depends on what you offer.
  (Reference: https://eur-lex.europa.eu/eli/dir/2019/882/oj)

**WCAG conformance levels:** A (lowest), AA, and AAA (highest). Level AA means
meeting all Level A and Level AA success criteria, and it is the level the
US rule above uses. W3C does not recommend requiring Level AAA as a general
policy for entire sites. (Reference: https://www.w3.org/TR/WCAG22/#cc1)

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
- Alternative text for images and media (Google also uses alt text to
  understand images: https://developers.google.com/search/docs/appearance/google-images)
- Captions and transcripts for video content

**Testing:**
- Automated tools (axe, Lighthouse, WAVE)
- Screen reader testing (NVDA, VoiceOver, JAWS)
- Keyboard-only navigation testing
- User testing with people who have disabilities

Accessibility improvements often benefit everyone - captions help in noisy
environments, keyboard navigation helps power users, clear design helps everyone.
"""
