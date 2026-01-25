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

# Existing guides (v2.9.0)
from .versioning import GUIDE as VERSIONING_GUIDE, CONTENT as VERSIONING_CONTENT
from .code_review import GUIDE as CODE_REVIEW_GUIDE, CONTENT as CODE_REVIEW_CONTENT
from .release_process import GUIDE as RELEASE_GUIDE, CONTENT as RELEASE_CONTENT
from .changelog import GUIDE as CHANGELOG_GUIDE, CONTENT as CHANGELOG_CONTENT
from .security_disclosure import GUIDE as SECURITY_DISCLOSURE_GUIDE, CONTENT as SECURITY_DISCLOSURE_CONTENT
from .adr import GUIDE as ADR_GUIDE, CONTENT as ADR_CONTENT

# New guides (v3.0.0)
from .test_strategies import GUIDE as TEST_STRATEGIES_GUIDE, CONTENT as TEST_STRATEGIES_CONTENT
from .dependency_guide import GUIDE as DEPENDENCY_GUIDE, CONTENT as DEPENDENCY_CONTENT
from .compliance_guide import GUIDE as COMPLIANCE_GUIDE, CONTENT as COMPLIANCE_CONTENT
from .api_standards import GUIDE as API_STANDARDS_GUIDE, CONTENT as API_STANDARDS_CONTENT
from .troubleshooting import GUIDE as TROUBLESHOOTING_GUIDE, CONTENT as TROUBLESHOOTING_CONTENT
from .faq import GUIDE as FAQ_GUIDE, CONTENT as FAQ_CONTENT
from .glossary import GUIDE as GLOSSARY_GUIDE, CONTENT as GLOSSARY_CONTENT
from .coding_standards import GUIDE as CODING_STANDARDS_GUIDE, CONTENT as CODING_STANDARDS_CONTENT
from .onboarding import GUIDE as ONBOARDING_GUIDE, CONTENT as ONBOARDING_CONTENT

# v3.2.0 guides
from .developer_handbook import GUIDE as DEVELOPER_HANDBOOK_GUIDE, CONTENT as DEVELOPER_HANDBOOK_CONTENT
from .architecture_overview import GUIDE as ARCHITECTURE_GUIDE, CONTENT as ARCHITECTURE_CONTENT
from .deployment_guide import GUIDE as DEPLOYMENT_GUIDE, CONTENT as DEPLOYMENT_CONTENT
from .contributor_handbook import GUIDE as CONTRIBUTOR_HANDBOOK_GUIDE, CONTENT as CONTRIBUTOR_HANDBOOK_CONTENT

# Aggregated guides dictionary
ALL_GUIDES = {
    # Existing guides (v2.9.0)
    "versioning": VERSIONING_GUIDE,
    "code-review": CODE_REVIEW_GUIDE,
    "release-process": RELEASE_GUIDE,
    "changelog": CHANGELOG_GUIDE,
    "security-disclosure": SECURITY_DISCLOSURE_GUIDE,
    "adr": ADR_GUIDE,
    # New guides (v3.0.0)
    "test-strategies": TEST_STRATEGIES_GUIDE,
    "dependency-guide": DEPENDENCY_GUIDE,
    "compliance-guide": COMPLIANCE_GUIDE,
    "api-standards": API_STANDARDS_GUIDE,
    "troubleshooting": TROUBLESHOOTING_GUIDE,
    "faq": FAQ_GUIDE,
    "glossary": GLOSSARY_GUIDE,
    "coding-standards": CODING_STANDARDS_GUIDE,
    "onboarding": ONBOARDING_GUIDE,
    # v3.2.0 guides
    "developer-handbook": DEVELOPER_HANDBOOK_GUIDE,
    "architecture-overview": ARCHITECTURE_GUIDE,
    "deployment-guide": DEPLOYMENT_GUIDE,
    "contributor-handbook": CONTRIBUTOR_HANDBOOK_GUIDE,
}

# Aggregated content dictionary
ALL_GUIDE_CONTENT = {
    # Existing guides (v2.9.0)
    "versioning": VERSIONING_CONTENT,
    "code-review": CODE_REVIEW_CONTENT,
    "release-process": RELEASE_CONTENT,
    "changelog": CHANGELOG_CONTENT,
    "security-disclosure": SECURITY_DISCLOSURE_CONTENT,
    "adr": ADR_CONTENT,
    # New guides (v3.0.0)
    "test-strategies": TEST_STRATEGIES_CONTENT,
    "dependency-guide": DEPENDENCY_CONTENT,
    "compliance-guide": COMPLIANCE_CONTENT,
    "api-standards": API_STANDARDS_CONTENT,
    "troubleshooting": TROUBLESHOOTING_CONTENT,
    "faq": FAQ_CONTENT,
    "glossary": GLOSSARY_CONTENT,
    "coding-standards": CODING_STANDARDS_CONTENT,
    "onboarding": ONBOARDING_CONTENT,
    # v3.2.0 guides
    "developer-handbook": DEVELOPER_HANDBOOK_CONTENT,
    "architecture-overview": ARCHITECTURE_CONTENT,
    "deployment-guide": DEPLOYMENT_CONTENT,
    "contributor-handbook": CONTRIBUTOR_HANDBOOK_CONTENT,
}

# Guide categories
GOVERNANCE_GUIDES = ["versioning", "release-process", "changelog", "compliance-guide"]
DEVELOPMENT_GUIDES = [
    "code-review", "adr", "test-strategies", "coding-standards", "api-standards",
    "developer-handbook", "architecture-overview",  # v3.2.0
]
SECURITY_GUIDES = ["security-disclosure"]
ONBOARDING_GUIDES = [
    "onboarding", "glossary", "faq", "troubleshooting",
    "contributor-handbook",  # v3.2.0
]
OPERATIONS_GUIDES = ["dependency-guide", "deployment-guide"]  # v3.2.0: added deployment-guide

# Complexity levels
GUIDE_COMPLEXITY = {
    # Existing guides (v2.9.0)
    "versioning": "beginner",
    "code-review": "intermediate",
    "release-process": "intermediate",
    "changelog": "beginner",
    "security-disclosure": "advanced",
    "adr": "intermediate",
    # New guides (v3.0.0)
    "test-strategies": "intermediate",
    "dependency-guide": "intermediate",
    "compliance-guide": "advanced",
    "api-standards": "advanced",
    "troubleshooting": "intermediate",
    "faq": "beginner",
    "glossary": "beginner",
    "coding-standards": "intermediate",
    "onboarding": "beginner",
    # v3.2.0 guides
    "developer-handbook": "intermediate",
    "architecture-overview": "intermediate",
    "deployment-guide": "intermediate",
    "contributor-handbook": "beginner",
}

# Version mapping (when each guide was introduced)
GUIDE_VERSIONS = {
    # Existing guides (v2.9.0)
    "versioning": "2.9.0",
    "code-review": "2.9.0",
    "release-process": "2.9.0",
    "changelog": "2.9.0",
    "security-disclosure": "2.9.0",
    "adr": "2.9.0",
    # New guides (v3.0.0)
    "test-strategies": "3.0.0",
    "dependency-guide": "3.0.0",
    "compliance-guide": "3.0.0",
    "api-standards": "3.0.0",
    "troubleshooting": "3.0.0",
    "faq": "3.0.0",
    "glossary": "3.0.0",
    "coding-standards": "3.0.0",
    "onboarding": "3.0.0",
    # v3.2.0 guides
    "developer-handbook": "3.2.0",
    "architecture-overview": "3.2.0",
    "deployment-guide": "3.2.0",
    "contributor-handbook": "3.2.0",
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
        category: One of 'governance', 'development', 'security', 'onboarding', 'operations'

    Returns:
        List of guide IDs in that category
    """
    categories = {
        "governance": GOVERNANCE_GUIDES,
        "development": DEVELOPMENT_GUIDES,
        "security": SECURITY_GUIDES,
        "onboarding": ONBOARDING_GUIDES,
        "operations": OPERATIONS_GUIDES,
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
    "ONBOARDING_GUIDES",
    "OPERATIONS_GUIDES",
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
