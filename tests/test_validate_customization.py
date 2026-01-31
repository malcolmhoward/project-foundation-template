# tests/test_validate_customization.py
# Unit tests for validate_customization.py

"""Unit tests for the customization validation script."""

import tempfile
import unittest
from pathlib import Path

# Import from the script (it's in the root, so we need to handle the import)
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from validate_customization import (
    Finding,
    should_scan_file,
    scan_file,
    scan_directory,
    format_findings,
    PLACEHOLDER_PATTERNS,
    SCANNABLE_EXTENSIONS,
    SKIP_DIRECTORIES,
)


class TestShouldScanFile(unittest.TestCase):
    """Test file scanning eligibility."""

    def test_scans_markdown_files(self):
        """Should scan .md files."""
        self.assertTrue(should_scan_file(Path("README.md")))
        self.assertTrue(should_scan_file(Path("docs/CONTRIBUTING.md")))

    def test_scans_yaml_files(self):
        """Should scan .yml and .yaml files."""
        self.assertTrue(should_scan_file(Path("config.yml")))
        self.assertTrue(should_scan_file(Path(".github/workflows/ci.yaml")))

    def test_scans_known_files_without_extension(self):
        """Should scan known files like LICENSE regardless of extension."""
        self.assertTrue(should_scan_file(Path("LICENSE")))
        self.assertTrue(should_scan_file(Path("README")))

    def test_skips_git_directory(self):
        """Should skip files in .git directory."""
        self.assertFalse(should_scan_file(Path(".git/config")))
        self.assertFalse(should_scan_file(Path(".git/hooks/pre-commit")))

    def test_skips_node_modules(self):
        """Should skip files in node_modules."""
        self.assertFalse(should_scan_file(Path("node_modules/package/README.md")))

    def test_skips_pft_output(self):
        """Should skip pft-output directories (raw template output)."""
        self.assertFalse(should_scan_file(Path("pft-output/README.md")))

    def test_skips_unknown_extensions(self):
        """Should skip files with unknown extensions."""
        self.assertFalse(should_scan_file(Path("image.png")))
        self.assertFalse(should_scan_file(Path("data.bin")))


class TestScanFile(unittest.TestCase):
    """Test individual file scanning."""

    def test_finds_replace_marker(self):
        """Should find [REPLACE: ...] markers."""
        with tempfile.TemporaryDirectory() as tmpdir:
            test_file = Path(tmpdir) / "test.md"
            test_file.write_text("# Title\n\n[REPLACE: Add description here]\n")

            findings = scan_file(test_file)
            self.assertEqual(len(findings), 1)
            self.assertIn("REPLACE", findings[0].matched_text)
            self.assertEqual(findings[0].line_number, 3)

    def test_finds_template_notice(self):
        """Should find TEMPLATE NOTICE: markers."""
        with tempfile.TemporaryDirectory() as tmpdir:
            test_file = Path(tmpdir) / "test.md"
            test_file.write_text("<!--\nTEMPLATE NOTICE: This needs customization\n-->\n")

            findings = scan_file(test_file)
            self.assertEqual(len(findings), 1)
            self.assertEqual(findings[0].pattern_type, "Template notice comment")

    def test_finds_multiple_markers(self):
        """Should find multiple markers in same file."""
        with tempfile.TemporaryDirectory() as tmpdir:
            test_file = Path(tmpdir) / "test.md"
            test_file.write_text("[REPLACE: title]\n\n[REPLACE: description]\n\n[TODO: add more]\n")

            findings = scan_file(test_file)
            self.assertEqual(len(findings), 3)

    def test_returns_empty_for_clean_file(self):
        """Should return empty list for properly customized file."""
        with tempfile.TemporaryDirectory() as tmpdir:
            test_file = Path(tmpdir) / "test.md"
            test_file.write_text("# My Project\n\nThis is a real description.\n")

            findings = scan_file(test_file)
            self.assertEqual(len(findings), 0)

    def test_case_insensitive_matching(self):
        """Should match markers case-insensitively."""
        with tempfile.TemporaryDirectory() as tmpdir:
            test_file = Path(tmpdir) / "test.md"
            test_file.write_text("[replace: something]\n[REPLACE: something]\n[Replace: something]\n")

            findings = scan_file(test_file)
            self.assertEqual(len(findings), 3)


class TestScanDirectory(unittest.TestCase):
    """Test directory scanning."""

    def test_scans_directory_recursively(self):
        """Should scan files in subdirectories."""
        with tempfile.TemporaryDirectory() as tmpdir:
            # Create nested structure
            subdir = Path(tmpdir) / "docs"
            subdir.mkdir()

            # File in root
            (Path(tmpdir) / "README.md").write_text("[REPLACE: root]")
            # File in subdirectory
            (subdir / "GUIDE.md").write_text("[REPLACE: nested]")

            findings = scan_directory(Path(tmpdir))
            self.assertEqual(len(findings), 2)

    def test_skips_excluded_directories(self):
        """Should skip .git and other excluded directories."""
        with tempfile.TemporaryDirectory() as tmpdir:
            # Create .git directory (should be skipped)
            git_dir = Path(tmpdir) / ".git"
            git_dir.mkdir()
            (git_dir / "config").write_text("[REPLACE: should not find]")

            # File in root (should be found)
            (Path(tmpdir) / "README.md").write_text("[REPLACE: should find]")

            findings = scan_directory(Path(tmpdir))
            self.assertEqual(len(findings), 1)
            self.assertIn("README.md", findings[0].file_path)


class TestFormatFindings(unittest.TestCase):
    """Test findings formatting."""

    def test_formats_empty_findings(self):
        """Should report success for empty findings."""
        result = format_findings([])
        self.assertIn("properly customized", result)

    def test_formats_findings_with_count(self):
        """Should include count of findings."""
        findings = [
            Finding("README.md", 1, "Template placeholder", "[REPLACE: x]", "line"),
            Finding("README.md", 2, "Template placeholder", "[REPLACE: y]", "line"),
        ]
        result = format_findings(findings)
        self.assertIn("2 uncustomized", result)

    def test_groups_by_file(self):
        """Should group findings by file."""
        findings = [
            Finding("README.md", 1, "Template placeholder", "[REPLACE: x]", "line"),
            Finding("CONTRIBUTING.md", 1, "Template placeholder", "[REPLACE: y]", "line"),
        ]
        result = format_findings(findings)
        self.assertIn("README.md", result)
        self.assertIn("CONTRIBUTING.md", result)

    def test_includes_action_required_message(self):
        """Should include action required message."""
        findings = [
            Finding("README.md", 1, "Template placeholder", "[REPLACE: x]", "line"),
        ]
        result = format_findings(findings)
        self.assertIn("ACTION REQUIRED", result)


class TestFinding(unittest.TestCase):
    """Test Finding namedtuple."""

    def test_finding_attributes(self):
        """Should have all required attributes."""
        f = Finding(
            file_path="README.md",
            line_number=10,
            pattern_type="Template placeholder",
            matched_text="[REPLACE: foo]",
            line_content="Some [REPLACE: foo] content"
        )
        self.assertEqual(f.file_path, "README.md")
        self.assertEqual(f.line_number, 10)
        self.assertEqual(f.pattern_type, "Template placeholder")
        self.assertEqual(f.matched_text, "[REPLACE: foo]")


class TestPlaceholderPatterns(unittest.TestCase):
    """Test that placeholder patterns are correctly defined."""

    def test_patterns_exist(self):
        """Should have defined placeholder patterns."""
        self.assertGreater(len(PLACEHOLDER_PATTERNS), 0)

    def test_replace_pattern_included(self):
        """Should include [REPLACE:] pattern."""
        patterns = [p[0] for p in PLACEHOLDER_PATTERNS]
        self.assertTrue(any('REPLACE' in p for p in patterns))


class TestConstants(unittest.TestCase):
    """Test module constants."""

    def test_scannable_extensions_include_markdown(self):
        """Should include .md extension."""
        self.assertIn('.md', SCANNABLE_EXTENSIONS)

    def test_skip_directories_include_git(self):
        """Should skip .git directory."""
        self.assertIn('.git', SKIP_DIRECTORIES)

    def test_skip_directories_include_pft_output(self):
        """Should skip pft-output directory."""
        self.assertIn('pft-output', SKIP_DIRECTORIES)


if __name__ == '__main__':
    unittest.main()
