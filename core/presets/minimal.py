# core/presets/minimal.py
# Minimal preset - Core essentials only

"""
Minimal preset for Project Foundation Template.

The absolute essentials for any open source project:
- README for project overview
- LICENSE for legal clarity
- CONTRIBUTING for collaboration basics
- .gitignore for clean repositories

This preset is for:
- Personal projects
- Quick prototypes
- Learning exercises
- Projects with minimal external collaboration
"""

MINIMAL_PRESET = {
    "name": "minimal",
    "description": "Core essentials only - README, LICENSE, CONTRIBUTING, .gitignore",
    "principles": [
        "readme",
        "contributing",
        "license",
    ],
    "features": {
        # Core files (always generated)
        "readme": True,
        "contributing": True,
        "license": True,
        "gitignore": True,
        # Governance files
        "code_of_conduct": False,
        "security": False,
        "changelog": False,
        # GitHub templates
        "issue_templates": False,
        "pr_template": False,
        # Advanced features
        "enhanced_security": False,
        "secrets_detection": False,
        "adr": False,
        "ci_workflow": False,
    },
    "recommended_for": [
        "Personal projects",
        "Prototypes",
        "Learning exercises",
        "Internal tools",
    ],
}
