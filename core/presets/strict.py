# core/presets/strict.py
# Strict preset - Comprehensive governance

"""
Strict preset for Project Foundation Template.

Comprehensive governance for security-conscious projects:
- All standard preset features
- Enhanced security policy
- Secrets detection with pre-commit hooks
- Architecture Decision Records

This preset is for:
- Projects handling sensitive data
- Security-focused development
- Teams requiring audit trails
- Projects with compliance requirements
"""

STRICT_PRESET = {
    "name": "strict",
    "description": "Comprehensive governance - adds security features and ADR to standard",
    "principles": [
        "readme",
        "contributing",
        "license",
        "code-of-conduct",
        "security",
        "enhanced-security",
        "secrets-detection",
        "changelog",
        "issue-templates",
        "pr-template",
        "ci-workflow",
        "adr",
    ],
    "features": {
        # Core files
        "readme": True,
        "contributing": True,
        "license": True,
        "gitignore": True,
        # Governance files
        "code_of_conduct": True,
        "security": True,
        "changelog": True,
        # GitHub templates
        "issue_templates": True,
        "pr_template": True,
        # Advanced features
        "enhanced_security": True,
        "secrets_detection": True,
        "adr": True,
        "ci_workflow": True,
    },
    "recommended_for": [
        "Security-sensitive projects",
        "Projects with compliance requirements",
        "Teams requiring audit trails",
        "Enterprise development",
    ],
}
