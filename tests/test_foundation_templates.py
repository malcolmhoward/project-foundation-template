# tests/test_foundation_templates.py
# Unit tests for foundation/templates module

"""Unit tests for the foundation.templates module."""

import unittest
from datetime import date

from core.templates import (
    # Core
    generate_readme_content,
    generate_contributing_content,
    generate_license_content,
    generate_gitignore_content,
    LICENSE_TEMPLATES,
    # Governance
    generate_code_of_conduct_content,
    generate_security_content,
    generate_changelog_content,
    # GitHub
    generate_bug_report_template,
    generate_feature_request_template,
    generate_pr_template_content,
    generate_ci_workflow_content,
    generate_pr_validation_workflow_content,
    # Advanced
    generate_enhanced_security_content,
    generate_pre_commit_config_content,
    generate_detect_secrets_script,
    generate_adr_readme_content,
    generate_adr_template_content,
    generate_first_adr_content,
    generate_ethics_notice_content,
)


class TestCoreTemplates(unittest.TestCase):
    """Test core template generators."""

    def test_readme_content(self):
        """README should include project name and license."""
        content = generate_readme_content("TestProject", "mit")
        self.assertIn("TestProject", content)
        self.assertIn("MIT", content)
        self.assertIn("TEMPLATE NOTICE", content)

    def test_contributing_content(self):
        """CONTRIBUTING should include project name and workflows."""
        content = generate_contributing_content("TestProject")
        self.assertIn("TestProject", content)
        self.assertIn("Fork-First", content)
        self.assertIn("Conventional Commits", content)

    def test_license_mit(self):
        """MIT license should include copyright."""
        content = generate_license_content("mit", "Test Author")
        self.assertIn("MIT License", content)
        self.assertIn("Test Author", content)
        self.assertIn(str(date.today().year), content)

    def test_license_apache(self):
        """Apache license should include copyright."""
        content = generate_license_content("apache", "Test Author")
        self.assertIn("Apache License", content)
        self.assertIn("Test Author", content)

    def test_license_gpl(self):
        """GPL license should include copyright."""
        content = generate_license_content("gpl", "Test Author")
        self.assertIn("GNU General Public License", content)
        self.assertIn("Test Author", content)

    def test_gitignore_content(self):
        """Gitignore should include common patterns."""
        content = generate_gitignore_content()
        self.assertIn("node_modules", content)
        self.assertIn(".env", content)
        self.assertIn("__pycache__", content)


class TestGovernanceTemplates(unittest.TestCase):
    """Test governance template generators."""

    def test_code_of_conduct(self):
        """Code of conduct should include key sections."""
        content = generate_code_of_conduct_content()
        self.assertIn("Our Pledge", content)
        self.assertIn("Our Standards", content)
        self.assertIn("Enforcement", content)
        self.assertIn("TEMPLATE", content)

    def test_security_content(self):
        """Security policy should include key sections."""
        content = generate_security_content()
        self.assertIn("Security Policy", content)
        self.assertIn("Reporting Vulnerabilities", content)
        self.assertIn("TEMPLATE", content)

    def test_changelog_content(self):
        """Changelog should follow Keep a Changelog format."""
        content = generate_changelog_content("TestProject")
        self.assertIn("TestProject", content)
        self.assertIn("Unreleased", content)
        self.assertIn("Keep a Changelog", content)
        self.assertIn("Semantic Versioning", content)


class TestGitHubTemplates(unittest.TestCase):
    """Test GitHub template generators."""

    def test_bug_report_template(self):
        """Bug report should include key sections."""
        content = generate_bug_report_template()
        self.assertIn("Bug Report", content)
        self.assertIn("Steps to Reproduce", content)
        self.assertIn("Expected Behavior", content)
        self.assertIn("Environment", content)

    def test_feature_request_template(self):
        """Feature request should include key sections."""
        content = generate_feature_request_template()
        self.assertIn("Feature Request", content)
        self.assertIn("Problem Statement", content)
        self.assertIn("Proposed Solution", content)

    def test_pr_template(self):
        """PR template should include checklist."""
        content = generate_pr_template_content()
        self.assertIn("Description", content)
        self.assertIn("Type of Change", content)
        self.assertIn("Checklist", content)

    def test_ci_workflow(self):
        """CI workflow should be valid YAML structure."""
        content = generate_ci_workflow_content()
        self.assertIn("name: CI", content)
        self.assertIn("on:", content)
        self.assertIn("jobs:", content)
        self.assertIn("runs-on:", content)

    def test_pr_validation_workflow(self):
        """PR validation should validate conventional commits."""
        content = generate_pr_validation_workflow_content()
        self.assertIn("PR Validation", content)
        self.assertIn("semantic-pull-request", content)


class TestAdvancedTemplates(unittest.TestCase):
    """Test advanced template generators."""

    def test_enhanced_security(self):
        """Enhanced security should be comprehensive."""
        content = generate_enhanced_security_content("TestProject")
        self.assertIn("Supported Versions", content)
        self.assertIn("Reporting a Vulnerability", content)
        self.assertIn("Security Best Practices", content)
        self.assertIn("Secrets Management", content)

    def test_pre_commit_config(self):
        """Pre-commit config should include hooks."""
        content = generate_pre_commit_config_content()
        self.assertIn("repos:", content)
        self.assertIn("secrets-detection", content)
        self.assertIn("pre-commit-hooks", content)

    def test_detect_secrets_script(self):
        """Secrets detection script should be bash script."""
        content = generate_detect_secrets_script()
        self.assertIn("#!/bin/bash", content)
        self.assertIn("PATTERNS", content)
        self.assertIn("SECRETS_FOUND", content)

    def test_adr_readme(self):
        """ADR readme should explain ADRs."""
        content = generate_adr_readme_content("TestProject")
        self.assertIn("Architecture Decision Records", content)
        self.assertIn("TestProject", content)
        self.assertIn("What is an ADR", content)

    def test_adr_template(self):
        """ADR template should have standard sections."""
        content = generate_adr_template_content()
        self.assertIn("Context", content)
        self.assertIn("Decision", content)
        self.assertIn("Consequences", content)
        self.assertIn("Status", content)

    def test_first_adr(self):
        """First ADR should document ADR adoption."""
        content = generate_first_adr_content()
        self.assertIn("Record Architecture Decisions", content)
        self.assertIn("Accepted", content)
        self.assertIn("Michael Nygard", content)

    def test_ethics_notice(self):
        """Ethics notice should list generated files."""
        files = ["README.md", "LICENSE", "CONTRIBUTING.md"]
        content = generate_ethics_notice_content(files)
        self.assertIn("ETHICAL USE NOTICE", content)
        for f in files:
            self.assertIn(f, content)


class TestLicenseTemplates(unittest.TestCase):
    """Test license template dictionary."""

    def test_has_mit(self):
        """Should have MIT license template."""
        self.assertIn("mit", LICENSE_TEMPLATES)
        self.assertIn("MIT License", LICENSE_TEMPLATES["mit"])

    def test_has_apache(self):
        """Should have Apache license template."""
        self.assertIn("apache", LICENSE_TEMPLATES)
        self.assertIn("Apache License", LICENSE_TEMPLATES["apache"])

    def test_has_gpl(self):
        """Should have GPL license template."""
        self.assertIn("gpl", LICENSE_TEMPLATES)
        self.assertIn("GNU General Public License", LICENSE_TEMPLATES["gpl"])


if __name__ == "__main__":
    unittest.main()
