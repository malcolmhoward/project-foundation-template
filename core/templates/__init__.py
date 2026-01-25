# foundation/templates - Template generation subpackage

"""
Templates subpackage for Project Foundation Template.

Modules:
    core: README, CONTRIBUTING, LICENSE, .gitignore
    governance: CoC, SECURITY, CHANGELOG
    github: Issue templates, PR template, workflows
    advanced: ADR, CI, secrets detection, enhanced security
"""

from core.templates.core import (
    generate_readme_content,
    generate_contributing_content,
    generate_license_content,
    generate_gitignore_content,
    LICENSE_TEMPLATES,
)

from core.templates.governance import (
    generate_code_of_conduct_content,
    generate_security_content,
    generate_changelog_content,
)

from core.templates.github import (
    generate_bug_report_template,
    generate_feature_request_template,
    generate_pr_template_content,
    generate_ci_workflow_content,
    generate_pr_validation_workflow_content,
)

from core.templates.advanced import (
    generate_enhanced_security_content,
    generate_pre_commit_config_content,
    generate_detect_secrets_script,
    generate_adr_readme_content,
    generate_adr_template_content,
    generate_first_adr_content,
    generate_ethics_notice_content,
)

from core.templates.accessibility import (
    generate_glossary_content,
    generate_maintainers_content,
    generate_scaffold_manifest_content,
)

__all__ = [
    # Core
    "generate_readme_content",
    "generate_contributing_content",
    "generate_license_content",
    "generate_gitignore_content",
    "LICENSE_TEMPLATES",
    # Governance
    "generate_code_of_conduct_content",
    "generate_security_content",
    "generate_changelog_content",
    # GitHub
    "generate_bug_report_template",
    "generate_feature_request_template",
    "generate_pr_template_content",
    "generate_ci_workflow_content",
    "generate_pr_validation_workflow_content",
    # Advanced
    "generate_enhanced_security_content",
    "generate_pre_commit_config_content",
    "generate_detect_secrets_script",
    "generate_adr_readme_content",
    "generate_adr_template_content",
    "generate_first_adr_content",
    "generate_ethics_notice_content",
    # Accessibility (v3.1.0)
    "generate_glossary_content",
    "generate_maintainers_content",
    "generate_scaffold_manifest_content",
]
