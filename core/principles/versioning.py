# core/principles/versioning.py
# Versioning principle (v2.10.0)

"""
Versioning Principle.

Semantic versioning communicates the impact of changes to users,
enabling them to update dependencies with confidence.

Introduced in v2.10.0.
"""

PRINCIPLE_ID = "versioning"

PRINCIPLE = {
    "name": "Versioning",
    "why": "Users need to understand the impact of updates before adopting them",
    "what": "Semantic versioning (SemVer) with clear version policies",
    "risk": "Without clear versioning, users fear updates and fall behind on security patches",
}

EDUCATION = """
📚 LEARNING: Semantic Versioning signals the impact of a release in its version number.

Semantic Versioning uses MAJOR.MINOR.PATCH format:
(Reference: https://semver.org/spec/v2.0.0.html)
- **MAJOR**: Breaking changes that require user action to upgrade
- **MINOR**: New features that are backward compatible
- **PATCH**: Bug fixes that don't change the API

Good versioning practices include:
- Starting at 0.y.z for initial development, when the public API should not be
  considered stable (SemVer item 4)
- Reaching 1.0.0 once the software is used in production or users depend on a
  stable API (the SemVer FAQ says it "should probably already be 1.0.0" then)
- Documenting breaking changes prominently in release notes
- Maintaining compatibility within major versions
- Providing migration guides for major version bumps

Version numbers are a promise to your users. Breaking that promise (shipping
breaking changes in minor versions) can erode trust and make users reluctant
to upgrade, so they miss security fixes and improvements.

Automated tools like commitizen can enforce conventional commits that map
directly to version bumps, removing guesswork from the release process.
"""
