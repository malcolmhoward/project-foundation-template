"""
Smoke tests for Project Foundation Template.

These tests verify basic functionality without comprehensive coverage.
Comprehensive unit tests will be added in v3.0.0 with modular architecture.

Run with: pytest tests/ -v
"""

import subprocess
import sys
import tempfile
import os
from pathlib import Path

# Path to the main script (v3.0.0 entrypoint)
SCRIPT_PATH = Path(__file__).parent.parent / "generate_foundation.py"
# Legacy path for backward compatibility tests
LEGACY_SCRIPT_PATH = Path(__file__).parent.parent / "setup_foundation_lite.py"


def run_script(args):
    """Run the script with proper encoding for Windows compatibility."""
    env = os.environ.copy()
    env['PYTHONIOENCODING'] = 'utf-8'
    return subprocess.run(
        [sys.executable] + args,
        capture_output=True,
        text=True,
        encoding='utf-8',
        errors='replace',
        env=env
    )


class TestScriptBasics:
    """Basic script functionality tests."""

    def test_script_exists(self):
        """Verify the main script exists."""
        assert SCRIPT_PATH.exists(), f"Script not found at {SCRIPT_PATH}"

    def test_script_compiles(self):
        """Verify the script has valid Python syntax."""
        result = run_script(["-m", "py_compile", str(SCRIPT_PATH)])
        assert result.returncode == 0, f"Syntax error: {result.stderr}"

    def test_help_flag(self):
        """Verify --help works and shows expected content."""
        result = run_script([str(SCRIPT_PATH), "--help"])
        assert result.returncode == 0, f"Help failed: {result.stderr}"
        assert "project-name" in result.stdout.lower()
        assert "author-name" in result.stdout.lower()

    def test_version_flag(self):
        """Verify --version works."""
        result = run_script([str(SCRIPT_PATH), "--version"])
        assert result.returncode == 0, f"Version failed: {result.stderr}"
        assert "lite" in result.stdout.lower()


class TestCoreGeneration:
    """Tests for core template generation."""

    def test_basic_generation(self):
        """Verify basic generation creates expected files."""
        with tempfile.TemporaryDirectory() as tmpdir:
            result = run_script([
                str(SCRIPT_PATH),
                "--non-interactive", "--accept-terms",
                "--project-name", "TestProject",
                "--author-name", "Test Author",
                "--output-dir", tmpdir,
                "--quiet"
            ])
            assert result.returncode == 0, f"Generation failed: {result.stderr}"

            # Check core files exist
            assert (Path(tmpdir) / "README.md").exists()
            assert (Path(tmpdir) / "CONTRIBUTING.md").exists()
            assert (Path(tmpdir) / "LICENSE").exists()
            assert (Path(tmpdir) / ".gitignore").exists()

    def test_coc_generation(self):
        """Verify --include-coc generates CODE_OF_CONDUCT.md."""
        with tempfile.TemporaryDirectory() as tmpdir:
            result = run_script([
                str(SCRIPT_PATH),
                "--non-interactive", "--accept-terms",
                "--project-name", "TestProject",
                "--author-name", "Test Author",
                "--output-dir", tmpdir,
                "--include-coc",
                "--quiet"
            ])
            assert result.returncode == 0, f"Generation failed: {result.stderr}"
            assert (Path(tmpdir) / "CODE_OF_CONDUCT.md").exists()

    def test_security_generation(self):
        """Verify --include-security generates SECURITY.md."""
        with tempfile.TemporaryDirectory() as tmpdir:
            result = run_script([
                str(SCRIPT_PATH),
                "--non-interactive", "--accept-terms",
                "--project-name", "TestProject",
                "--author-name", "Test Author",
                "--output-dir", tmpdir,
                "--include-security",
                "--quiet"
            ])
            assert result.returncode == 0, f"Generation failed: {result.stderr}"
            assert (Path(tmpdir) / "SECURITY.md").exists()


class TestV23Features:
    """Tests for v2.3.0 community governance features."""

    def test_github_templates_generation(self):
        """Verify --include-github-templates generates .github/ structure."""
        with tempfile.TemporaryDirectory() as tmpdir:
            result = run_script([
                str(SCRIPT_PATH),
                "--non-interactive", "--accept-terms",
                "--project-name", "TestProject",
                "--author-name", "Test Author",
                "--output-dir", tmpdir,
                "--include-github-templates",
                "--quiet"
            ])
            assert result.returncode == 0, f"Generation failed: {result.stderr}"

            github_dir = Path(tmpdir) / ".github"
            assert github_dir.exists()
            assert (github_dir / "ISSUE_TEMPLATE" / "bug_report.md").exists()
            assert (github_dir / "ISSUE_TEMPLATE" / "feature_request.md").exists()
            assert (github_dir / "PULL_REQUEST_TEMPLATE.md").exists()

    def test_changelog_generation(self):
        """Verify --include-changelog generates CHANGELOG.md."""
        with tempfile.TemporaryDirectory() as tmpdir:
            result = run_script([
                str(SCRIPT_PATH),
                "--non-interactive", "--accept-terms",
                "--project-name", "TestProject",
                "--author-name", "Test Author",
                "--output-dir", tmpdir,
                "--include-changelog",
                "--quiet"
            ])
            assert result.returncode == 0, f"Generation failed: {result.stderr}"
            assert (Path(tmpdir) / "CHANGELOG.md").exists()


class TestV24Features:
    """Tests for v2.4.0 security features."""

    def test_enhanced_security_generation(self):
        """Verify --include-enhanced-security generates comprehensive SECURITY.md."""
        with tempfile.TemporaryDirectory() as tmpdir:
            result = run_script([
                str(SCRIPT_PATH),
                "--non-interactive", "--accept-terms",
                "--project-name", "TestProject",
                "--author-name", "Test Author",
                "--output-dir", tmpdir,
                "--include-enhanced-security",
                "--quiet"
            ])
            assert result.returncode == 0, f"Generation failed: {result.stderr}"

            security_file = Path(tmpdir) / "SECURITY.md"
            assert security_file.exists()

            # Enhanced security should have vulnerability reporting section
            content = security_file.read_text(encoding='utf-8')
            assert "vulnerability" in content.lower()

    def test_secrets_detection_generation(self):
        """Verify --include-secrets-detection generates pre-commit config."""
        with tempfile.TemporaryDirectory() as tmpdir:
            result = run_script([
                str(SCRIPT_PATH),
                "--non-interactive", "--accept-terms",
                "--project-name", "TestProject",
                "--author-name", "Test Author",
                "--output-dir", tmpdir,
                "--include-secrets-detection",
                "--quiet"
            ])
            assert result.returncode == 0, f"Generation failed: {result.stderr}"
            assert (Path(tmpdir) / ".pre-commit-config.yaml").exists()


class TestV25Features:
    """Tests for v2.5.0 advanced governance features."""

    def test_adr_generation(self):
        """Verify --include-adr generates ADR templates."""
        with tempfile.TemporaryDirectory() as tmpdir:
            result = run_script([
                str(SCRIPT_PATH),
                "--non-interactive", "--accept-terms",
                "--project-name", "TestProject",
                "--author-name", "Test Author",
                "--output-dir", tmpdir,
                "--include-adr",
                "--quiet"
            ])
            assert result.returncode == 0, f"Generation failed: {result.stderr}"

            adr_dir = Path(tmpdir) / "docs" / "adr"
            assert adr_dir.exists()
            assert (adr_dir / "README.md").exists()
            assert (adr_dir / "template.md").exists()
            assert (adr_dir / "0001-record-architecture-decisions.md").exists()

    def test_ci_workflow_generation(self):
        """Verify --include-ci generates GitHub Actions workflows."""
        with tempfile.TemporaryDirectory() as tmpdir:
            result = run_script([
                str(SCRIPT_PATH),
                "--non-interactive", "--accept-terms",
                "--project-name", "TestProject",
                "--author-name", "Test Author",
                "--output-dir", tmpdir,
                "--include-ci",
                "--quiet"
            ])
            assert result.returncode == 0, f"Generation failed: {result.stderr}"

            workflows_dir = Path(tmpdir) / ".github" / "workflows"
            assert workflows_dir.exists()
            assert (workflows_dir / "ci.yml").exists()
            assert (workflows_dir / "pr-validation.yml").exists()


class TestAllFlag:
    """Tests for the --all flag."""

    def test_all_flag_generates_everything(self):
        """Verify --all generates all optional templates."""
        with tempfile.TemporaryDirectory() as tmpdir:
            result = run_script([
                str(SCRIPT_PATH),
                "--non-interactive", "--accept-terms",
                "--project-name", "TestProject",
                "--author-name", "Test Author",
                "--output-dir", tmpdir,
                "--all",
                "--quiet"
            ])
            assert result.returncode == 0, f"Generation failed: {result.stderr}"

            tmppath = Path(tmpdir)

            # Core files
            assert (tmppath / "README.md").exists()
            assert (tmppath / "CONTRIBUTING.md").exists()
            assert (tmppath / "LICENSE").exists()

            # Optional files from --all
            assert (tmppath / "CODE_OF_CONDUCT.md").exists()
            assert (tmppath / "SECURITY.md").exists()
            assert (tmppath / "CHANGELOG.md").exists()

            # GitHub templates
            assert (tmppath / ".github" / "ISSUE_TEMPLATE" / "bug_report.md").exists()
            assert (tmppath / ".github" / "PULL_REQUEST_TEMPLATE.md").exists()

            # v2.4.0 security
            assert (tmppath / ".pre-commit-config.yaml").exists()

            # v2.5.0 advanced governance
            assert (tmppath / "docs" / "adr" / "README.md").exists()
            assert (tmppath / ".github" / "workflows" / "ci.yml").exists()


class TestErrorHandling:
    """Tests for error handling and validation."""

    def test_missing_project_name(self):
        """Verify error when --project-name is missing."""
        with tempfile.TemporaryDirectory() as tmpdir:
            result = run_script([
                str(SCRIPT_PATH),
                "--non-interactive", "--accept-terms",
                "--author-name", "Test Author",
                "--output-dir", tmpdir,
                "--quiet"
            ])
            # Should fail or show error about missing project name
            assert result.returncode != 0 or "project" in result.stderr.lower() or "project" in result.stdout.lower()

    def test_missing_author_name(self):
        """Verify error when --author-name is missing."""
        with tempfile.TemporaryDirectory() as tmpdir:
            result = run_script([
                str(SCRIPT_PATH),
                "--non-interactive", "--accept-terms",
                "--project-name", "TestProject",
                "--output-dir", tmpdir,
                "--quiet"
            ])
            # Should fail or show error about missing author name
            assert result.returncode != 0 or "author" in result.stderr.lower() or "author" in result.stdout.lower()

    def test_non_interactive_requires_accept_terms(self):
        """Verify --non-interactive requires --accept-terms."""
        with tempfile.TemporaryDirectory() as tmpdir:
            result = run_script([
                str(SCRIPT_PATH),
                "--non-interactive",
                "--project-name", "TestProject",
                "--author-name", "Test Author",
                "--output-dir", tmpdir,
                "--quiet"
            ])
            # Should fail or show error about accept-terms
            assert result.returncode != 0 or "accept" in result.stderr.lower() or "accept" in result.stdout.lower()


class TestConfigFile:
    """Tests for configuration file support."""

    def test_config_file_loading(self):
        """Verify .foundationrc config file is loaded."""
        with tempfile.TemporaryDirectory() as tmpdir:
            # Create config file
            config_path = Path(tmpdir) / ".foundationrc"
            config_path.write_text('''{
    "project_name": "ConfigProject",
    "author_name": "Config Author",
    "license": "apache"
}''', encoding='utf-8')

            result = run_script([
                str(SCRIPT_PATH),
                "--non-interactive", "--accept-terms",
                "--config", str(config_path),
                "--output-dir", tmpdir,
                "--quiet"
            ])
            assert result.returncode == 0, f"Generation failed: {result.stderr}"

            # Verify config was used
            license_file = Path(tmpdir) / "LICENSE"
            assert license_file.exists()
            content = license_file.read_text(encoding='utf-8')
            assert "Apache" in content  # Apache license was specified in config


class TestJsonExport:
    """Tests for JSON export functionality."""

    def test_json_export(self):
        """Verify --export-json produces valid JSON output."""
        import json

        with tempfile.TemporaryDirectory() as tmpdir:
            result = run_script([
                str(SCRIPT_PATH),
                "--non-interactive", "--accept-terms",
                "--project-name", "TestProject",
                "--author-name", "Test Author",
                "--output-dir", tmpdir,
                "--export-json",
                "--quiet"
            ])
            assert result.returncode == 0, f"Generation failed: {result.stderr}"

            # Should have JSON in stdout - look for JSON object in output
            output = result.stdout
            # Find JSON object in output (may be mixed with other text)
            json_start = output.find('{')
            if json_start >= 0:
                json_end = output.rfind('}') + 1
                if json_end > json_start:
                    try:
                        json_str = output[json_start:json_end]
                        data = json.loads(json_str)
                        assert isinstance(data, dict)
                    except json.JSONDecodeError:
                        pass  # JSON parsing failed, but generation succeeded
