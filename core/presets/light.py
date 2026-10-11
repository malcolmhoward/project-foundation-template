# core/presets/light.py
# Light preset - Basic governance

"""
Light preset for Project Foundation Template.

Adds basic governance to the minimal preset:
- Code of Conduct for community standards
- Security policy for vulnerability reporting
- Changelog for version history

This preset is for:
- Small open source projects
- Projects expecting some external contributions
- Teams wanting basic governance without overhead
"""

LIGHT_PRESET = {
    "name": "light",
    "description": "Basic governance - adds CoC, Security, Changelog to minimal",
    "principles": [
        "readme",
        "contributing",
        "license",
        "code-of-conduct",
        "security",
        "changelog",
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
        "issue_templates": False,
        "pr_template": False,
        # Advanced features
        "enhanced_security": False,
        "secrets_detection": False,
        "adr": False,
        "ci_workflow": False,
    },
    "recommended_for": [
        "Small open source projects",
        "Projects with occasional contributors",
        "Teams wanting basic governance",
    ],
}
