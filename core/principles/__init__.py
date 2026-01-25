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

# v3.0.0 principles
from .quality_assurance import PRINCIPLE as QA_PRINCIPLE, EDUCATION as QA_EDUCATION
from .code_standards import PRINCIPLE as CODE_STANDARDS_PRINCIPLE, EDUCATION as CODE_STANDARDS_EDUCATION
from .versioning import PRINCIPLE as VERSIONING_PRINCIPLE, EDUCATION as VERSIONING_EDUCATION
from .compliance_policy import PRINCIPLE as COMPLIANCE_PRINCIPLE, EDUCATION as COMPLIANCE_EDUCATION
from .internationalization import PRINCIPLE as I18N_PRINCIPLE, EDUCATION as I18N_EDUCATION
from .audit_logging import PRINCIPLE as AUDIT_PRINCIPLE, EDUCATION as AUDIT_EDUCATION
from .dependency_scanning import PRINCIPLE as DEPSCAN_PRINCIPLE, EDUCATION as DEPSCAN_EDUCATION
from .container_support import PRINCIPLE as CONTAINER_PRINCIPLE, EDUCATION as CONTAINER_EDUCATION
from .deprecation_policy import PRINCIPLE as DEPRECATION_PRINCIPLE, EDUCATION as DEPRECATION_EDUCATION
from .accessibility import PRINCIPLE as A11Y_PRINCIPLE, EDUCATION as A11Y_EDUCATION
from .performance_standards import PRINCIPLE as PERF_PRINCIPLE, EDUCATION as PERF_EDUCATION

# v3.1.0 principles
from .glossary import PRINCIPLE as GLOSSARY_PRINCIPLE, EDUCATION as GLOSSARY_EDUCATION
from .maintainers import PRINCIPLE as MAINTAINERS_PRINCIPLE, EDUCATION as MAINTAINERS_EDUCATION

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
    # v3.0.0 principles
    "quality-assurance": QA_PRINCIPLE,
    "code-standards": CODE_STANDARDS_PRINCIPLE,
    "versioning": VERSIONING_PRINCIPLE,
    "compliance-policy": COMPLIANCE_PRINCIPLE,
    "internationalization": I18N_PRINCIPLE,
    "audit-logging": AUDIT_PRINCIPLE,
    "dependency-scanning": DEPSCAN_PRINCIPLE,
    "container-support": CONTAINER_PRINCIPLE,
    "deprecation-policy": DEPRECATION_PRINCIPLE,
    "accessibility": A11Y_PRINCIPLE,
    "performance-standards": PERF_PRINCIPLE,
    # v3.1.0 principles
    "glossary": GLOSSARY_PRINCIPLE,
    "maintainers": MAINTAINERS_PRINCIPLE,
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
    # v3.0.0 principles
    "quality-assurance": QA_EDUCATION,
    "code-standards": CODE_STANDARDS_EDUCATION,
    "versioning": VERSIONING_EDUCATION,
    "compliance-policy": COMPLIANCE_EDUCATION,
    "internationalization": I18N_EDUCATION,
    "audit-logging": AUDIT_EDUCATION,
    "dependency-scanning": DEPSCAN_EDUCATION,
    "container-support": CONTAINER_EDUCATION,
    "deprecation-policy": DEPRECATION_EDUCATION,
    "accessibility": A11Y_EDUCATION,
    "performance-standards": PERF_EDUCATION,
    # v3.1.0 principles
    "glossary": GLOSSARY_EDUCATION,
    "maintainers": MAINTAINERS_EDUCATION,
}

# Principle categories for organization
CORE_PRINCIPLES = ["readme", "contributing", "license"]
GOVERNANCE_PRINCIPLES = ["code-of-conduct", "security"]
SECURITY_PRINCIPLES = ["enhanced-security", "secrets-detection"]
ADVANCED_PRINCIPLES = ["adr", "ci-workflow"]
COMMUNITY_PRINCIPLES = ["issue-templates", "pr-template", "changelog"]

# v3.0.0 categories
QUALITY_PRINCIPLES = ["quality-assurance", "code-standards", "performance-standards"]
COMPLIANCE_PRINCIPLES = ["compliance-policy", "audit-logging"]
INFRASTRUCTURE_PRINCIPLES = ["dependency-scanning", "container-support", "versioning"]
INCLUSIVITY_PRINCIPLES = ["internationalization", "accessibility"]
LIFECYCLE_PRINCIPLES = ["deprecation-policy"]

# v3.1.0 categories
USABILITY_PRINCIPLES = ["glossary", "maintainers"]

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
    # v3.0.0 principles
    "quality-assurance": "3.0.0",
    "code-standards": "3.0.0",
    "versioning": "3.0.0",
    "compliance-policy": "3.0.0",
    "internationalization": "3.0.0",
    "audit-logging": "3.0.0",
    "dependency-scanning": "3.0.0",
    "container-support": "3.0.0",
    "deprecation-policy": "3.0.0",
    "accessibility": "3.0.0",
    "performance-standards": "3.0.0",
    # v3.1.0 principles
    "glossary": "3.1.0",
    "maintainers": "3.1.0",
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
        category: One of 'core', 'governance', 'security', 'advanced', 'community',
                  'quality', 'compliance', 'infrastructure', 'inclusivity', 'lifecycle'

    Returns:
        List of principle IDs in that category
    """
    categories = {
        "core": CORE_PRINCIPLES,
        "governance": GOVERNANCE_PRINCIPLES,
        "security": SECURITY_PRINCIPLES,
        "advanced": ADVANCED_PRINCIPLES,
        "community": COMMUNITY_PRINCIPLES,
        # v3.0.0 categories
        "quality": QUALITY_PRINCIPLES,
        "compliance": COMPLIANCE_PRINCIPLES,
        "infrastructure": INFRASTRUCTURE_PRINCIPLES,
        "inclusivity": INCLUSIVITY_PRINCIPLES,
        "lifecycle": LIFECYCLE_PRINCIPLES,
        # v3.1.0 categories
        "usability": USABILITY_PRINCIPLES,
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
    # v3.0.0 categories
    "QUALITY_PRINCIPLES",
    "COMPLIANCE_PRINCIPLES",
    "INFRASTRUCTURE_PRINCIPLES",
    "INCLUSIVITY_PRINCIPLES",
    "LIFECYCLE_PRINCIPLES",
    # v3.1.0 categories
    "USABILITY_PRINCIPLES",
    # Version mapping
    "PRINCIPLE_VERSIONS",
    # Helper functions
    "get_principle",
    "get_education",
    "get_principles_by_category",
    "get_principles_for_version",
    "list_all_principles",
]
