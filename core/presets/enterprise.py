# core/presets/enterprise.py
# Enterprise preset - Full governance suite

"""
Enterprise preset for Project Foundation Template.

The complete governance suite with all features enabled.
Includes all strict preset features plus any future additions.

This preset is for:
- Large organizations
- Regulated industries
- Projects requiring maximum governance
- Teams with dedicated compliance/security staff

Note: This preset is currently equivalent to strict.
Future versions will add:
- Dependency scanning workflows
- Container support templates
- Compliance documentation
- Internationalization templates
"""

ENTERPRISE_PRESET = {
    "name": "enterprise",
    "description": "Full governance suite - all features enabled",
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
        "Large organizations",
        "Regulated industries",
        "Maximum governance requirements",
        "Dedicated compliance teams",
    ],
    "future_additions": [
        "Dependency scanning",
        "Container templates",
        "Compliance documentation",
        "Internationalization",
    ],
}
