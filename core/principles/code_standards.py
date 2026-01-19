# core/principles/code_standards.py
# Code Standards principle (v3.0.0)

"""
Code Standards Principle.

Consistent code standards reduce cognitive load and enable teams to
focus on solving problems rather than deciphering formatting.

Introduced in v3.0.0.
"""

PRINCIPLE_ID = "code-standards"

PRINCIPLE = {
    "name": "Code Standards",
    "why": "Inconsistent code increases cognitive load and review time",
    "what": "Documented style guides, linting rules, and automated formatting",
    "risk": "Without standards, code reviews become style debates instead of logic reviews",
}

EDUCATION = """
📚 LEARNING: Teams with enforced code standards spend 15% less time on code reviews.

Code standards are about more than aesthetics - they're about communication.
When code follows consistent patterns, developers can:

- **Read faster**: Familiar patterns reduce the mental effort to understand code
- **Review effectively**: Focus on logic and design, not formatting
- **Onboard quickly**: New team members learn one style, not many
- **Automate confidently**: Consistent code is easier to analyze and transform

Effective code standards include:
- Naming conventions (variables, functions, classes, files)
- Formatting rules (indentation, line length, whitespace)
- Documentation requirements (comments, docstrings, API docs)
- Language-specific idioms (Pythonic code, idiomatic Go, etc.)

The best standards are automated - use linters, formatters, and pre-commit hooks
to enforce them without human effort. Style debates end when the formatter decides.
"""
