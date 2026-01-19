# core/principles/versioning.py
# Versioning principle (v3.0.0)

"""
Versioning Principle.

Semantic versioning communicates the impact of changes to users,
enabling them to update dependencies with confidence.

Introduced in v3.0.0.
"""

PRINCIPLE_ID = "versioning"

PRINCIPLE = {
    "name": "Versioning",
    "why": "Users need to understand the impact of updates before adopting them",
    "what": "Semantic versioning (SemVer) with clear version policies",
    "risk": "Without clear versioning, users fear updates and fall behind on security patches",
}

EDUCATION = """
📚 LEARNING: 92% of package ecosystems use Semantic Versioning as their standard.

Semantic Versioning (semver.org) uses MAJOR.MINOR.PATCH format:
- **MAJOR**: Breaking changes that require user action to upgrade
- **MINOR**: New features that are backward compatible
- **PATCH**: Bug fixes that don't change the API

Good versioning practices include:
- Starting at 0.x.x for unstable/development versions
- Reaching 1.0.0 when the API is stable and production-ready
- Documenting breaking changes prominently in release notes
- Maintaining compatibility within major versions
- Providing migration guides for major version bumps

Version numbers are a promise to your users. Breaking that promise (shipping
breaking changes in minor versions) destroys trust and makes users reluctant
to upgrade - which means they miss security fixes and improvements.

Automated tools like commitizen can enforce conventional commits that map
directly to version bumps, removing guesswork from the release process.
"""
