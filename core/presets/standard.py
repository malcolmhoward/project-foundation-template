# core/presets/standard.py
# Standard preset - Recommended default

"""
Standard preset for Project Foundation Template.

The recommended default for most projects:
- All light preset features
- GitHub issue and PR templates
- CI workflow for automated testing

This preset is for:
- Active open source projects
- Projects expecting regular contributions
- Teams wanting professional project structure
"""

STANDARD_PRESET = {
    "name": "standard",
    "description": "Recommended default - adds GitHub templates and CI to light",
    "principles": [
        "readme",
        "contributing",
        "license",
        "code-of-conduct",
        "security",
        "changelog",
        "issue-templates",
        "pr-template",
        "ci-workflow",
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
        "enhanced_security": False,
        "secrets_detection": False,
        "adr": False,
        "ci_workflow": True,
    },
    "recommended_for": [
        "Active open source projects",
        "Projects with regular contributions",
        "Professional project structure",
    ],
}
