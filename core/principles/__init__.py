# core/principles/__init__.py
# Governance principles as individual modules

"""
Principles module for Project Foundation Template.

Each principle is defined in its own module with:
    - PRINCIPLE: Dict with name, why, what, risk
    - EDUCATION: Educational content string
    - PRINCIPLE_ID: Unique identifier

This modular structure allows:
    - Individual principle documentation
    - Selective loading for presets
    - Easy addition of new principles
    - Clear separation of concerns
"""

from .readme import PRINCIPLE as README_PRINCIPLE, EDUCATION as README_EDUCATION
from .contributing import PRINCIPLE as CONTRIBUTING_PRINCIPLE, EDUCATION as CONTRIBUTING_EDUCATION
from .license import PRINCIPLE as LICENSE_PRINCIPLE, EDUCATION as LICENSE_EDUCATION
from .code_of_conduct import PRINCIPLE as COC_PRINCIPLE, EDUCATION as COC_EDUCATION
from .security import PRINCIPLE as SECURITY_PRINCIPLE, EDUCATION as SECURITY_EDUCATION
from .enhanced_security import PRINCIPLE as ENHANCED_SECURITY_PRINCIPLE, EDUCATION as ENHANCED_SECURITY_EDUCATION
from .secrets_detection import PRINCIPLE as SECRETS_PRINCIPLE, EDUCATION as SECRETS_EDUCATION
from .adr import PRINCIPLE as ADR_PRINCIPLE, EDUCATION as ADR_EDUCATION
from .ci_workflow import PRINCIPLE as CI_PRINCIPLE, EDUCATION as CI_EDUCATION
from .issue_templates import PRINCIPLE as ISSUE_PRINCIPLE, EDUCATION as ISSUE_EDUCATION
from .pr_template import PRINCIPLE as PR_PRINCIPLE, EDUCATION as PR_EDUCATION
from .changelog import PRINCIPLE as CHANGELOG_PRINCIPLE, EDUCATION as CHANGELOG_EDUCATION

# Aggregated principles dictionary (backward compatible with LITE_PRINCIPLES)
ALL_PRINCIPLES = {
    "readme": README_PRINCIPLE,
    "contributing": CONTRIBUTING_PRINCIPLE,
    "license": LICENSE_PRINCIPLE,
    "code-of-conduct": COC_PRINCIPLE,
    "security": SECURITY_PRINCIPLE,
    "enhanced-security": ENHANCED_SECURITY_PRINCIPLE,
    "secrets-detection": SECRETS_PRINCIPLE,
    "adr": ADR_PRINCIPLE,
    "ci-workflow": CI_PRINCIPLE,
    "issue-templates": ISSUE_PRINCIPLE,
    "pr-template": PR_PRINCIPLE,
    "changelog": CHANGELOG_PRINCIPLE,
}

# Aggregated education content dictionary (backward compatible with EDUCATION_CONTENT)
ALL_EDUCATION = {
    "readme": README_EDUCATION,
    "contributing": CONTRIBUTING_EDUCATION,
    "license": LICENSE_EDUCATION,
    "code-of-conduct": COC_EDUCATION,
    "security": SECURITY_EDUCATION,
    "enhanced-security": ENHANCED_SECURITY_EDUCATION,
    "secrets-detection": SECRETS_EDUCATION,
    "adr": ADR_EDUCATION,
    "ci-workflow": CI_EDUCATION,
    "issue-templates": ISSUE_EDUCATION,
    "pr-template": PR_EDUCATION,
    "changelog": CHANGELOG_EDUCATION,
}

# Principle categories for organization
CORE_PRINCIPLES = ["readme", "contributing", "license"]
GOVERNANCE_PRINCIPLES = ["code-of-conduct", "security"]
SECURITY_PRINCIPLES = ["enhanced-security", "secrets-detection"]
ADVANCED_PRINCIPLES = ["adr", "ci-workflow"]
COMMUNITY_PRINCIPLES = ["issue-templates", "pr-template", "changelog"]

# Version mapping (when each principle was introduced)
PRINCIPLE_VERSIONS = {
    "readme": "2.1.0",
    "contributing": "2.1.0",
    "license": "2.1.0",
    "code-of-conduct": "2.1.0",
    "security": "2.1.0",
    "enhanced-security": "2.4.0",
    "secrets-detection": "2.4.0",
    "adr": "2.5.0",
    "ci-workflow": "2.5.0",
    "issue-templates": "2.3.0",
    "pr-template": "2.3.0",
    "changelog": "2.3.0",
}


def get_principle(name: str) -> dict:
    """Get a principle by name.

    Args:
        name: Principle identifier (e.g., 'readme', 'security')

    Returns:
        Principle dict with name, why, what, risk, or empty dict if not found
    """
    return ALL_PRINCIPLES.get(name, {})


def get_education(name: str) -> str:
    """Get educational content for a principle.

    Args:
        name: Principle identifier

    Returns:
        Educational content string, or empty string if not found
    """
    return ALL_EDUCATION.get(name, "")


def get_principles_by_category(category: str) -> list:
    """Get principle IDs by category.

    Args:
        category: One of 'core', 'governance', 'security', 'advanced', 'community'

    Returns:
        List of principle IDs in that category
    """
    categories = {
        "core": CORE_PRINCIPLES,
        "governance": GOVERNANCE_PRINCIPLES,
        "security": SECURITY_PRINCIPLES,
        "advanced": ADVANCED_PRINCIPLES,
        "community": COMMUNITY_PRINCIPLES,
    }
    return categories.get(category.lower(), [])


def get_principles_for_version(version: str) -> list:
    """Get principle IDs available in a specific version.

    Args:
        version: Version string (e.g., '2.3.0')

    Returns:
        List of principle IDs available in that version or earlier
    """
    def parse_version(v: str) -> tuple:
        """Parse version string to comparable tuple."""
        clean = v.replace("-lite", "").split("-")[0]
        parts = clean.split(".")
        return tuple(int(p) for p in parts[:3])

    target = parse_version(version)
    return [
        pid for pid, v in PRINCIPLE_VERSIONS.items()
        if parse_version(v) <= target
    ]


def list_all_principles() -> list:
    """List all available principle IDs.

    Returns:
        List of all principle identifiers
    """
    return list(ALL_PRINCIPLES.keys())


__all__ = [
    # Aggregated dictionaries
    "ALL_PRINCIPLES",
    "ALL_EDUCATION",
    # Categories
    "CORE_PRINCIPLES",
    "GOVERNANCE_PRINCIPLES",
    "SECURITY_PRINCIPLES",
    "ADVANCED_PRINCIPLES",
    "COMMUNITY_PRINCIPLES",
    # Version mapping
    "PRINCIPLE_VERSIONS",
    # Helper functions
    "get_principle",
    "get_education",
    "get_principles_by_category",
    "get_principles_for_version",
    "list_all_principles",
]
