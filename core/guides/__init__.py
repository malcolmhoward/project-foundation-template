# core/guides/__init__.py
# Implementation guides as individual modules

"""
Guides module for Project Foundation Template.

Each guide is defined in its own module with:
    - GUIDE_ID: Unique identifier
    - GUIDE: Dict with title, purpose, audience, complexity
    - CONTENT: The actual guide content
    - RELATED_PRINCIPLES: List of related principle IDs

This modular structure provides:
    - Implementation guidance (HOW) complementing principles (WHAT/WHY)
    - Selective loading based on user needs
    - Easy addition of new guides
    - Clear separation from template generation
"""

from .versioning import GUIDE as VERSIONING_GUIDE, CONTENT as VERSIONING_CONTENT
from .code_review import GUIDE as CODE_REVIEW_GUIDE, CONTENT as CODE_REVIEW_CONTENT
from .release_process import GUIDE as RELEASE_GUIDE, CONTENT as RELEASE_CONTENT
from .changelog import GUIDE as CHANGELOG_GUIDE, CONTENT as CHANGELOG_CONTENT
from .security_disclosure import GUIDE as SECURITY_DISCLOSURE_GUIDE, CONTENT as SECURITY_DISCLOSURE_CONTENT
from .adr import GUIDE as ADR_GUIDE, CONTENT as ADR_CONTENT

# Aggregated guides dictionary
ALL_GUIDES = {
    "versioning": VERSIONING_GUIDE,
    "code-review": CODE_REVIEW_GUIDE,
    "release-process": RELEASE_GUIDE,
    "changelog": CHANGELOG_GUIDE,
    "security-disclosure": SECURITY_DISCLOSURE_GUIDE,
    "adr": ADR_GUIDE,
}

# Aggregated content dictionary
ALL_GUIDE_CONTENT = {
    "versioning": VERSIONING_CONTENT,
    "code-review": CODE_REVIEW_CONTENT,
    "release-process": RELEASE_CONTENT,
    "changelog": CHANGELOG_CONTENT,
    "security-disclosure": SECURITY_DISCLOSURE_CONTENT,
    "adr": ADR_CONTENT,
}

# Guide categories
GOVERNANCE_GUIDES = ["versioning", "release-process", "changelog"]
DEVELOPMENT_GUIDES = ["code-review", "adr"]
SECURITY_GUIDES = ["security-disclosure"]

# Complexity levels
GUIDE_COMPLEXITY = {
    "versioning": "beginner",
    "code-review": "intermediate",
    "release-process": "intermediate",
    "changelog": "beginner",
    "security-disclosure": "advanced",
    "adr": "intermediate",
}

# Version mapping (when each guide was introduced)
GUIDE_VERSIONS = {
    "versioning": "2.9.0",
    "code-review": "2.9.0",
    "release-process": "2.9.0",
    "changelog": "2.9.0",
    "security-disclosure": "2.9.0",
    "adr": "2.9.0",
}


def get_guide(name: str) -> dict:
    """Get a guide by name.

    Args:
        name: Guide identifier (e.g., 'versioning', 'code-review')

    Returns:
        Guide dict with title, purpose, audience, complexity, or empty dict if not found
    """
    return ALL_GUIDES.get(name, {})


def get_guide_content(name: str) -> str:
    """Get content for a guide.

    Args:
        name: Guide identifier

    Returns:
        Guide content string, or empty string if not found
    """
    return ALL_GUIDE_CONTENT.get(name, "")


def get_guides_by_category(category: str) -> list:
    """Get guide IDs by category.

    Args:
        category: One of 'governance', 'development', 'security'

    Returns:
        List of guide IDs in that category
    """
    categories = {
        "governance": GOVERNANCE_GUIDES,
        "development": DEVELOPMENT_GUIDES,
        "security": SECURITY_GUIDES,
    }
    return categories.get(category.lower(), [])


def get_guides_by_complexity(complexity: str) -> list:
    """Get guide IDs by complexity level.

    Args:
        complexity: One of 'beginner', 'intermediate', 'advanced'

    Returns:
        List of guide IDs at that complexity level
    """
    return [
        gid for gid, level in GUIDE_COMPLEXITY.items()
        if level == complexity.lower()
    ]


def list_all_guides() -> list:
    """List all available guide IDs.

    Returns:
        List of all guide identifiers
    """
    return list(ALL_GUIDES.keys())


__all__ = [
    # Aggregated dictionaries
    "ALL_GUIDES",
    "ALL_GUIDE_CONTENT",
    # Categories
    "GOVERNANCE_GUIDES",
    "DEVELOPMENT_GUIDES",
    "SECURITY_GUIDES",
    # Mappings
    "GUIDE_COMPLEXITY",
    "GUIDE_VERSIONS",
    # Helper functions
    "get_guide",
    "get_guide_content",
    "get_guides_by_category",
    "get_guides_by_complexity",
    "list_all_guides",
]
