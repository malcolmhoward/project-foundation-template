# core/presets/enterprise.py
# Enterprise preset - Full governance suite (v3.0.0)

"""
Enterprise preset for Project Foundation Template.

The complete governance suite with all 23 principles enabled.
This is the maximum governance configuration for organizations
requiring comprehensive project governance.

This preset is for:
- Large organizations
- Regulated industries
- Projects requiring maximum governance
- Teams with dedicated compliance/security staff
"""

ENTERPRISE_PRESET = {
    "name": "enterprise",
    "description": "Full governance suite - all 23 principles enabled",
    "principles": [
        # Core (v2.1.0)
        "readme",
        "contributing",
        "license",
        # Governance (v2.1.0)
        "code-of-conduct",
        "security",
        # Security (v2.4.0)
        "enhanced-security",
        "secrets-detection",
        # Community (v2.3.0)
        "issue-templates",
        "pr-template",
        "changelog",
        # Advanced (v2.5.0)
        "adr",
        "ci-workflow",
        # Quality (v3.0.0)
        "quality-assurance",
        "code-standards",
        "performance-standards",
        # Compliance (v3.0.0)
        "compliance-policy",
        "audit-logging",
        # Infrastructure (v3.0.0)
        "versioning",
        "dependency-scanning",
        "container-support",
        # Inclusivity (v3.0.0)
        "internationalization",
        "accessibility",
        # Lifecycle (v3.0.0)
        "deprecation-policy",
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
        "Large organizations",
        "Regulated industries (HIPAA, SOC2, GDPR)",
        "Maximum governance requirements",
        "Dedicated compliance teams",
        "Accessibility-focused products",
        "International/multilingual projects",
    ],
}
