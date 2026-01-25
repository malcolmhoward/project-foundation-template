# core/principles/internationalization.py
# Internationalization principle (v3.0.0)

"""
Internationalization Principle.

Internationalization (i18n) enables software to be adapted for different
languages and regions without engineering changes.

Introduced in v3.0.0.
"""

PRINCIPLE_ID = "internationalization"

PRINCIPLE = {
    "name": "Internationalization",
    "why": "75% of internet users prefer content in their native language",
    "what": "Architecture and tooling that supports multiple languages, locales, and cultural conventions",
    "risk": "Without i18n, projects are limited to English-speaking markets and exclude global users",
}

EDUCATION = """
📚 LEARNING: Localized software sees 1.5x higher user engagement in non-English markets.

Internationalization (i18n) is the architectural foundation that makes
localization (l10n) possible. Key practices include:

**Text and Content:**
- Extract all user-facing strings to translation files
- Use ICU MessageFormat for pluralization and gender
- Support right-to-left (RTL) languages like Arabic and Hebrew
- Handle text expansion (German text is ~30% longer than English)

**Numbers and Dates:**
- Use locale-aware formatting for numbers, currencies, and percentages
- Support multiple date formats (MM/DD/YYYY vs DD/MM/YYYY)
- Handle timezone conversion correctly

**Cultural Considerations:**
- Color meanings vary by culture (red = luck in China, danger in US)
- Icons and images may need localization (mailbox styles differ globally)
- Names and addresses have different formats worldwide

**Technical Implementation:**
- Use Unicode (UTF-8) everywhere
- Design flexible UIs that adapt to text length and direction
- Implement locale detection and user preference settings
- Set up translation management workflows

Retrofitting i18n into an existing codebase is expensive. Build it in from day one.
"""
