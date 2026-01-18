# tests/test_foundation_generator.py
# Unit tests for foundation/generator.py

"""Unit tests for the foundation.generator module."""

import tempfile
import unittest
from argparse import Namespace
from datetime import datetime
from pathlib import Path
from unittest.mock import MagicMock, patch

from core.generator import EthicalFoundationGenerator


def create_mock_args(**kwargs):
    """Create a mock args namespace with default values."""
    defaults = {
        'project_name': 'TestProject',
        'author_name': 'Test Author',
        'license': 'mit',
        'output_dir': '.',
        'non_interactive': True,
        'quiet': True,
        'verbose': False,
        'include_coc': False,
        'include_security': False,
        'include_github_templates': False,
        'include_changelog': False,
        'include_enhanced_security': False,
        'include_secrets_detection': False,
        'include_adr': False,
        'include_ci': False,
        'include_all': False,
    }
    defaults.update(kwargs)
    return Namespace(**defaults)


class TestEthicalFoundationGeneratorInit(unittest.TestCase):
    """Test generator initialization."""

    def test_init_sets_args(self):
        """Generator should store args."""
        args = create_mock_args(project_name='MyProject')
        generator = EthicalFoundationGenerator(args)
        self.assertEqual(generator.args.project_name, 'MyProject')

    def test_init_creates_empty_generated_files(self):
        """Generator should start with empty generated_files list."""
        args = create_mock_args()
        generator = EthicalFoundationGenerator(args)
        self.assertEqual(generator.generated_files, [])

    def test_init_creates_empty_education_shown(self):
        """Generator should start with empty education_shown set."""
        args = create_mock_args()
        generator = EthicalFoundationGenerator(args)
        self.assertEqual(generator.education_shown, set())

    def test_init_sets_start_time(self):
        """Generator should record start time."""
        args = create_mock_args()
        before = datetime.now()
        generator = EthicalFoundationGenerator(args)
        after = datetime.now()
        self.assertGreaterEqual(generator.start_time, before)
        self.assertLessEqual(generator.start_time, after)


class TestIsInteractiveProperty(unittest.TestCase):
    """Test is_interactive property."""

    def test_interactive_when_non_interactive_false(self):
        """Should be interactive when non_interactive is False."""
        args = create_mock_args(non_interactive=False)
        generator = EthicalFoundationGenerator(args)
        self.assertTrue(generator.is_interactive)

    def test_not_interactive_when_non_interactive_true(self):
        """Should not be interactive when non_interactive is True."""
        args = create_mock_args(non_interactive=True)
        generator = EthicalFoundationGenerator(args)
        self.assertFalse(generator.is_interactive)

    def test_interactive_default_when_attr_missing(self):
        """Should be interactive when non_interactive attr is missing."""
        args = Namespace(project_name='Test')
        generator = EthicalFoundationGenerator(args)
        self.assertTrue(generator.is_interactive)


class TestIsQuietProperty(unittest.TestCase):
    """Test is_quiet property."""

    def test_quiet_when_quiet_true(self):
        """Should be quiet when quiet is True."""
        args = create_mock_args(quiet=True)
        generator = EthicalFoundationGenerator(args)
        self.assertTrue(generator.is_quiet)

    def test_not_quiet_when_quiet_false(self):
        """Should not be quiet when quiet is False."""
        args = create_mock_args(quiet=False)
        generator = EthicalFoundationGenerator(args)
        self.assertFalse(generator.is_quiet)

    def test_not_quiet_default_when_attr_missing(self):
        """Should not be quiet when quiet attr is missing."""
        args = Namespace(project_name='Test')
        generator = EthicalFoundationGenerator(args)
        self.assertFalse(generator.is_quiet)


class TestWriteFile(unittest.TestCase):
    """Test write_file method."""

    def test_write_file_creates_file(self):
        """write_file should create file with content."""
        with tempfile.TemporaryDirectory() as tmpdir:
            args = create_mock_args(output_dir=tmpdir)
            generator = EthicalFoundationGenerator(args)

            filepath = Path(tmpdir) / "test.txt"
            generator.write_file(filepath, "test content")

            self.assertTrue(filepath.exists())
            self.assertEqual(filepath.read_text(encoding='utf-8'), "test content")

    def test_write_file_tracks_filename(self):
        """write_file should track generated filename."""
        with tempfile.TemporaryDirectory() as tmpdir:
            args = create_mock_args(output_dir=tmpdir)
            generator = EthicalFoundationGenerator(args)

            filepath = Path(tmpdir) / "test.txt"
            generator.write_file(filepath, "test content")

            self.assertIn("test.txt", generator.generated_files)

    def test_write_file_handles_unicode(self):
        """write_file should handle unicode content."""
        with tempfile.TemporaryDirectory() as tmpdir:
            args = create_mock_args(output_dir=tmpdir)
            generator = EthicalFoundationGenerator(args)

            filepath = Path(tmpdir) / "unicode.txt"
            content = "Unicode: \u2713 \u274c \u26a0\ufe0f"
            generator.write_file(filepath, content)

            self.assertEqual(filepath.read_text(encoding='utf-8'), content)


class TestEducateBeforeGenerating(unittest.TestCase):
    """Test educate_before_generating method."""

    def test_marks_principle_as_shown(self):
        """Should mark principle as shown."""
        args = create_mock_args(quiet=True)
        generator = EthicalFoundationGenerator(args)

        generator.educate_before_generating("readme")

        self.assertIn("readme", generator.education_shown)

    def test_does_not_repeat_education(self):
        """Should not repeat education for same principle."""
        # Use non-interactive mode to avoid input() calls
        args = create_mock_args(quiet=False, non_interactive=True)
        generator = EthicalFoundationGenerator(args)

        # First call marks it as shown
        generator.educate_before_generating("readme")

        # Second call should be a no-op (principle already shown)
        initial_shown = generator.education_shown.copy()
        generator.educate_before_generating("readme")
        self.assertEqual(generator.education_shown, initial_shown)

    def test_quiet_mode_no_output(self):
        """Should produce no output in quiet mode."""
        args = create_mock_args(quiet=True)
        generator = EthicalFoundationGenerator(args)

        # Should not raise any exceptions in quiet mode
        generator.educate_before_generating("readme")
        self.assertIn("readme", generator.education_shown)


class TestShowEducationalIntro(unittest.TestCase):
    """Test show_educational_intro method."""

    def test_quiet_mode_returns_early(self):
        """Should return early in quiet mode."""
        args = create_mock_args(quiet=True)
        generator = EthicalFoundationGenerator(args)

        # Should not raise any exceptions
        generator.show_educational_intro()

    @patch('builtins.print')
    def test_non_interactive_shows_brief_message(self, mock_print):
        """Should show brief message in non-interactive mode."""
        args = create_mock_args(quiet=False, non_interactive=True)
        generator = EthicalFoundationGenerator(args)

        generator.show_educational_intro()

        # Check that print was called with non-interactive message
        calls = [str(call) for call in mock_print.call_args_list]
        self.assertTrue(any('non-interactive' in call.lower() for call in calls))


class TestGenerateFoundation(unittest.TestCase):
    """Test generate_foundation method."""

    def test_creates_output_directory(self):
        """Should create output directory if it doesn't exist."""
        with tempfile.TemporaryDirectory() as tmpdir:
            output_dir = Path(tmpdir) / "new_dir"
            args = create_mock_args(output_dir=str(output_dir))
            generator = EthicalFoundationGenerator(args)

            generator.generate_foundation()

            self.assertTrue(output_dir.exists())

    def test_generates_core_files(self):
        """Should generate core files (README, CONTRIBUTING, LICENSE)."""
        with tempfile.TemporaryDirectory() as tmpdir:
            args = create_mock_args(output_dir=tmpdir)
            generator = EthicalFoundationGenerator(args)

            result = generator.generate_foundation()

            self.assertTrue(result)
            self.assertTrue((Path(tmpdir) / "README.md").exists())
            self.assertTrue((Path(tmpdir) / "CONTRIBUTING.md").exists())
            self.assertTrue((Path(tmpdir) / "LICENSE").exists())

    def test_generates_gitignore(self):
        """Should generate .gitignore."""
        with tempfile.TemporaryDirectory() as tmpdir:
            args = create_mock_args(output_dir=tmpdir)
            generator = EthicalFoundationGenerator(args)

            generator.generate_foundation()

            self.assertTrue((Path(tmpdir) / ".gitignore").exists())

    def test_generates_foundation_notice(self):
        """Should generate FOUNDATION_NOTICE.md."""
        with tempfile.TemporaryDirectory() as tmpdir:
            args = create_mock_args(output_dir=tmpdir)
            generator = EthicalFoundationGenerator(args)

            generator.generate_foundation()

            self.assertTrue((Path(tmpdir) / "FOUNDATION_NOTICE.md").exists())

    def test_generates_coc_when_requested(self):
        """Should generate CODE_OF_CONDUCT.md when include_coc is True."""
        with tempfile.TemporaryDirectory() as tmpdir:
            args = create_mock_args(output_dir=tmpdir, include_coc=True)
            generator = EthicalFoundationGenerator(args)

            generator.generate_foundation()

            self.assertTrue((Path(tmpdir) / "CODE_OF_CONDUCT.md").exists())

    def test_generates_security_when_requested(self):
        """Should generate SECURITY.md when include_security is True."""
        with tempfile.TemporaryDirectory() as tmpdir:
            args = create_mock_args(output_dir=tmpdir, include_security=True)
            generator = EthicalFoundationGenerator(args)

            generator.generate_foundation()

            self.assertTrue((Path(tmpdir) / "SECURITY.md").exists())

    def test_include_all_generates_everything(self):
        """Should generate all optional files when include_all is True."""
        with tempfile.TemporaryDirectory() as tmpdir:
            args = create_mock_args(output_dir=tmpdir, include_all=True)
            generator = EthicalFoundationGenerator(args)

            generator.generate_foundation()

            # Check optional files
            self.assertTrue((Path(tmpdir) / "CODE_OF_CONDUCT.md").exists())
            self.assertTrue((Path(tmpdir) / "SECURITY.md").exists())
            self.assertTrue((Path(tmpdir) / "CHANGELOG.md").exists())
            self.assertTrue((Path(tmpdir) / ".pre-commit-config.yaml").exists())
            self.assertTrue((Path(tmpdir) / "docs" / "adr" / "README.md").exists())

    def test_returns_false_on_error(self):
        """Should return False when an error occurs."""
        args = create_mock_args(output_dir="/nonexistent/readonly/path")
        generator = EthicalFoundationGenerator(args)

        # This should fail because the path doesn't exist
        with patch.object(generator, 'generate_readme', side_effect=Exception("Test error")):
            result = generator.generate_foundation()
            self.assertFalse(result)


class TestGenerateSpecificFiles(unittest.TestCase):
    """Test individual file generation methods."""

    def test_generate_readme(self):
        """Should generate README.md with project name."""
        with tempfile.TemporaryDirectory() as tmpdir:
            args = create_mock_args(output_dir=tmpdir, project_name='MyProject')
            generator = EthicalFoundationGenerator(args)

            generator.generate_readme(Path(tmpdir))

            readme = Path(tmpdir) / "README.md"
            self.assertTrue(readme.exists())
            content = readme.read_text(encoding='utf-8')
            self.assertIn("MyProject", content)

    def test_generate_contributing(self):
        """Should generate CONTRIBUTING.md."""
        with tempfile.TemporaryDirectory() as tmpdir:
            args = create_mock_args(output_dir=tmpdir)
            generator = EthicalFoundationGenerator(args)

            generator.generate_contributing(Path(tmpdir))

            self.assertTrue((Path(tmpdir) / "CONTRIBUTING.md").exists())

    def test_generate_license(self):
        """Should generate LICENSE with author name."""
        with tempfile.TemporaryDirectory() as tmpdir:
            args = create_mock_args(output_dir=tmpdir, author_name='John Doe')
            generator = EthicalFoundationGenerator(args)

            generator.generate_license(Path(tmpdir))

            license_file = Path(tmpdir) / "LICENSE"
            self.assertTrue(license_file.exists())
            content = license_file.read_text(encoding='utf-8')
            self.assertIn("John Doe", content)

    def test_generate_issue_templates(self):
        """Should generate GitHub issue templates."""
        with tempfile.TemporaryDirectory() as tmpdir:
            args = create_mock_args(output_dir=tmpdir)
            generator = EthicalFoundationGenerator(args)

            generator.generate_issue_templates(Path(tmpdir))

            github_dir = Path(tmpdir) / ".github" / "ISSUE_TEMPLATE"
            self.assertTrue((github_dir / "bug_report.md").exists())
            self.assertTrue((github_dir / "feature_request.md").exists())

    def test_generate_pr_template(self):
        """Should generate GitHub PR template."""
        with tempfile.TemporaryDirectory() as tmpdir:
            args = create_mock_args(output_dir=tmpdir)
            generator = EthicalFoundationGenerator(args)

            generator.generate_pr_template(Path(tmpdir))

            self.assertTrue((Path(tmpdir) / ".github" / "PULL_REQUEST_TEMPLATE.md").exists())

    def test_generate_changelog(self):
        """Should generate CHANGELOG.md."""
        with tempfile.TemporaryDirectory() as tmpdir:
            args = create_mock_args(output_dir=tmpdir)
            generator = EthicalFoundationGenerator(args)

            generator.generate_changelog(Path(tmpdir))

            self.assertTrue((Path(tmpdir) / "CHANGELOG.md").exists())

    def test_generate_adr_templates(self):
        """Should generate ADR templates."""
        with tempfile.TemporaryDirectory() as tmpdir:
            args = create_mock_args(output_dir=tmpdir)
            generator = EthicalFoundationGenerator(args)

            generator.generate_adr_templates(Path(tmpdir))

            adr_dir = Path(tmpdir) / "docs" / "adr"
            self.assertTrue((adr_dir / "README.md").exists())
            self.assertTrue((adr_dir / "template.md").exists())
            self.assertTrue((adr_dir / "0001-record-architecture-decisions.md").exists())

    def test_generate_ci_workflow(self):
        """Should generate GitHub Actions workflows."""
        with tempfile.TemporaryDirectory() as tmpdir:
            args = create_mock_args(output_dir=tmpdir)
            generator = EthicalFoundationGenerator(args)

            generator.generate_ci_workflow(Path(tmpdir))

            workflows_dir = Path(tmpdir) / ".github" / "workflows"
            self.assertTrue((workflows_dir / "ci.yml").exists())
            self.assertTrue((workflows_dir / "pr-validation.yml").exists())


class TestCheckVersionAdvisory(unittest.TestCase):
    """Test check_version_advisory method."""

    @patch('core.generator.check_version_advisory')
    def test_calls_standalone_function(self, mock_check):
        """Should call standalone check_version_advisory function."""
        mock_check.return_value = True
        args = create_mock_args()
        generator = EthicalFoundationGenerator(args)

        result = generator.check_version_advisory()

        self.assertTrue(result)
        mock_check.assert_called_once()


class TestShowEthicalAgreement(unittest.TestCase):
    """Test show_ethical_agreement method."""

    @patch('core.generator.show_ethical_agreement')
    def test_calls_standalone_function(self, mock_show):
        """Should call standalone show_ethical_agreement function."""
        mock_show.return_value = True
        args = create_mock_args()
        generator = EthicalFoundationGenerator(args)

        result = generator.show_ethical_agreement()

        self.assertTrue(result)
        mock_show.assert_called_once()


class TestLogUsageLocally(unittest.TestCase):
    """Test log_usage_locally method."""

    def test_creates_log_directory(self):
        """Should create log directory if it doesn't exist."""
        with tempfile.TemporaryDirectory() as tmpdir:
            args = create_mock_args(output_dir=tmpdir)
            generator = EthicalFoundationGenerator(args)

            with patch('pathlib.Path.home', return_value=Path(tmpdir)):
                generator.log_usage_locally(True)

                log_dir = Path(tmpdir) / ".project_foundation_logs"
                self.assertTrue(log_dir.exists())


class TestImportFromPackage(unittest.TestCase):
    """Test that generator can be imported from core package."""

    def test_import_from_foundation(self):
        """Should be importable from core package."""
        from core import EthicalFoundationGenerator as FromPackage
        self.assertEqual(FromPackage, EthicalFoundationGenerator)

    def test_in_all(self):
        """Should be in core.__all__."""
        import core
        self.assertIn("EthicalFoundationGenerator", core.__all__)


if __name__ == "__main__":
    unittest.main()
