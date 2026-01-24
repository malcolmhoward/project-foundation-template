# tests/test_generation_log.py
# Unit tests for core/generation_log.py

"""Unit tests for the generation log module."""

import json
import tempfile
import unittest
from datetime import datetime
from pathlib import Path
from unittest.mock import patch

from core.generation_log import (
    create_file_record,
    detect_existing_logs,
    generate_log_md,
    generate_log_json,
    load_existing_log,
    prompt_overwrite_action,
    write_generation_log,
)


class TestCreateFileRecord(unittest.TestCase):
    """Test file record creation."""

    def test_creates_basic_record(self):
        """Should create a valid file record."""
        record = create_file_record("README.md")
        self.assertEqual(record["file"], "README.md")
        self.assertEqual(record["tool"], "PFT")
        self.assertIn("tool_version", record)
        self.assertIn("generated", record)

    def test_accepts_custom_tool(self):
        """Should accept custom tool name."""
        record = create_file_record("README.md", tool="CustomTool")
        self.assertEqual(record["tool"], "CustomTool")

    def test_accepts_customization_note(self):
        """Should accept customization description."""
        record = create_file_record("README.md", customization="Added badges")
        self.assertEqual(record["customization"], "Added badges")

    def test_date_format(self):
        """Generated date should be in YYYY-MM-DD format."""
        record = create_file_record("README.md")
        # Should parse without error
        datetime.strptime(record["generated"], "%Y-%m-%d")


class TestDetectExistingLogs(unittest.TestCase):
    """Test detection of existing log files."""

    def test_returns_empty_when_no_logs(self):
        """Should return empty dict when no logs exist."""
        with tempfile.TemporaryDirectory() as tmpdir:
            result = detect_existing_logs(Path(tmpdir), "md")
            self.assertEqual(result, {})

    def test_detects_md_log(self):
        """Should detect existing markdown log."""
        with tempfile.TemporaryDirectory() as tmpdir:
            output_dir = Path(tmpdir)
            (output_dir / "GENERATION_LOG.md").write_text("# Log")
            result = detect_existing_logs(output_dir, "md")
            self.assertIn("md", result)
            self.assertEqual(result["md"], output_dir / "GENERATION_LOG.md")

    def test_detects_json_log(self):
        """Should detect existing JSON log."""
        with tempfile.TemporaryDirectory() as tmpdir:
            output_dir = Path(tmpdir)
            (output_dir / "GENERATION_LOG.json").write_text("{}")
            result = detect_existing_logs(output_dir, "json")
            self.assertIn("json", result)

    def test_detects_both_logs(self):
        """Should detect both log formats when both exist."""
        with tempfile.TemporaryDirectory() as tmpdir:
            output_dir = Path(tmpdir)
            (output_dir / "GENERATION_LOG.md").write_text("# Log")
            (output_dir / "GENERATION_LOG.json").write_text("{}")
            result = detect_existing_logs(output_dir, "both")
            self.assertIn("md", result)
            self.assertIn("json", result)


class TestPromptOverwriteAction(unittest.TestCase):
    """Test overwrite action prompting."""

    def test_returns_create_when_no_existing(self):
        """Should return 'create' when no existing logs."""
        result = prompt_overwrite_action({}, interactive=True)
        self.assertEqual(result, "create")

    def test_returns_append_in_non_interactive_mode(self):
        """Should default to 'append' in non-interactive mode."""
        with tempfile.TemporaryDirectory() as tmpdir:
            existing = {"md": Path(tmpdir) / "GENERATION_LOG.md"}
            result = prompt_overwrite_action(existing, interactive=False)
            self.assertEqual(result, "append")


class TestGenerateLogMd(unittest.TestCase):
    """Test markdown log generation."""

    def test_generates_valid_markdown(self):
        """Should generate valid markdown content."""
        files = [
            {"file": "README.md", "generated": "2026-01-24", "tool": "PFT",
             "tool_version": "v3.7.0", "customization": "-"},
        ]
        content = generate_log_md("TestProject", files)
        self.assertIn("# Generation Log", content)
        self.assertIn("TestProject", content)
        self.assertIn("README.md", content)
        self.assertIn("| File |", content)

    def test_includes_ethics_reference(self):
        """Should include reference to ETHICS.md."""
        files = [
            {"file": "README.md", "generated": "2026-01-24", "tool": "PFT",
             "tool_version": "v3.7.0", "customization": "-"},
        ]
        content = generate_log_md("TestProject", files)
        self.assertIn("ETHICS.md", content)
        self.assertIn("Usage Logging", content)

    def test_includes_all_files(self):
        """Should include all files in the table."""
        files = [
            {"file": "README.md", "generated": "2026-01-24", "tool": "PFT",
             "tool_version": "v3.7.0", "customization": "-"},
            {"file": "LICENSE", "generated": "2026-01-24", "tool": "PFT",
             "tool_version": "v3.7.0", "customization": "-"},
        ]
        content = generate_log_md("TestProject", files)
        self.assertIn("README.md", content)
        self.assertIn("LICENSE", content)

    def test_appends_to_existing_content(self):
        """Should append new entries to existing log within table."""
        existing = """# Generation Log

**Project**: TestProject
**Last Updated**: 2026-01-20 10:00:00

## Generated Files

| File | Generated | Tool | Version | Customization |
|------|-----------|------|---------|---------------|
| README.md | 2026-01-20 | PFT | v3.6.0 | - |

## Understanding This Log

Some footer content.
"""
        files = [
            {"file": "LICENSE", "generated": "2026-01-24", "tool": "PFT",
             "tool_version": "v3.7.0", "customization": "-"},
        ]
        content = generate_log_md("TestProject", files, existing)
        self.assertIn("README.md", content)
        self.assertIn("LICENSE", content)
        # New entry should be in the table, before "Understanding This Log"
        readme_pos = content.find("README.md")
        license_pos = content.find("LICENSE")
        understanding_pos = content.find("Understanding This Log")
        self.assertLess(readme_pos, license_pos)
        self.assertLess(license_pos, understanding_pos)

    def test_updates_timestamp_on_append(self):
        """Should update Last Updated timestamp when appending."""
        existing = """# Generation Log

**Project**: TestProject
**Last Updated**: 2026-01-20 10:00:00

| File | Generated | Tool | Version | Customization |
|------|-----------|------|---------|---------------|
| README.md | 2026-01-20 | PFT | v3.6.0 | - |
"""
        files = [
            {"file": "LICENSE", "generated": "2026-01-24", "tool": "PFT",
             "tool_version": "v3.7.0", "customization": "-"},
        ]
        content = generate_log_md("TestProject", files, existing)
        # Old timestamp should be replaced
        self.assertNotIn("2026-01-20 10:00:00", content)
        self.assertIn("**Last Updated**:", content)


class TestGenerateLogJson(unittest.TestCase):
    """Test JSON log generation."""

    def test_generates_valid_json(self):
        """Should generate valid JSON content."""
        files = [
            {"file": "README.md", "generated": "2026-01-24", "tool": "PFT",
             "tool_version": "v3.7.0", "customization": "-"},
        ]
        content = generate_log_json("TestProject", files)
        data = json.loads(content)  # Should parse without error
        self.assertEqual(data["project"], "TestProject")
        self.assertEqual(data["version"], "1.0")
        self.assertEqual(len(data["files"]), 1)

    def test_includes_ethics_reference(self):
        """Should include reference to ETHICS.md."""
        files = [
            {"file": "README.md", "generated": "2026-01-24", "tool": "PFT",
             "tool_version": "v3.7.0", "customization": "-"},
        ]
        content = generate_log_json("TestProject", files)
        data = json.loads(content)
        self.assertIn("ethics_reference", data)

    def test_includes_all_files(self):
        """Should include all files in the JSON."""
        files = [
            {"file": "README.md", "generated": "2026-01-24", "tool": "PFT",
             "tool_version": "v3.7.0", "customization": "-"},
            {"file": "LICENSE", "generated": "2026-01-24", "tool": "PFT",
             "tool_version": "v3.7.0", "customization": "-"},
        ]
        content = generate_log_json("TestProject", files)
        data = json.loads(content)
        self.assertEqual(len(data["files"]), 2)

    def test_merges_with_existing_json(self):
        """Should merge new entries with existing JSON log."""
        existing = json.dumps({
            "version": "1.0",
            "project": "TestProject",
            "files": [
                {"file": "README.md", "generated": "2026-01-20", "tool": "PFT",
                 "tool_version": "v3.6.0", "customization": "-"},
            ]
        })
        files = [
            {"file": "LICENSE", "generated": "2026-01-24", "tool": "PFT",
             "tool_version": "v3.7.0", "customization": "-"},
        ]
        content = generate_log_json("TestProject", files, existing)
        data = json.loads(content)
        self.assertEqual(len(data["files"]), 2)


class TestLoadExistingLog(unittest.TestCase):
    """Test loading existing log files."""

    def test_returns_none_for_missing_file(self):
        """Should return None when file doesn't exist."""
        result = load_existing_log(Path("/nonexistent/file.md"))
        self.assertIsNone(result)

    def test_loads_existing_file(self):
        """Should load content from existing file."""
        with tempfile.TemporaryDirectory() as tmpdir:
            log_path = Path(tmpdir) / "GENERATION_LOG.md"
            log_path.write_text("# Test Content")
            result = load_existing_log(log_path)
            self.assertEqual(result, "# Test Content")


class TestWriteGenerationLog(unittest.TestCase):
    """Test writing generation log files."""

    def test_writes_md_format(self):
        """Should write markdown log file."""
        with tempfile.TemporaryDirectory() as tmpdir:
            output_dir = Path(tmpdir)
            created, success = write_generation_log(
                output_dir=output_dir,
                project_name="TestProject",
                generated_files=["README.md", "LICENSE"],
                log_format="md"
            )
            self.assertTrue(success)
            self.assertEqual(len(created), 1)
            self.assertTrue((output_dir / "GENERATION_LOG.md").exists())

    def test_writes_json_format(self):
        """Should write JSON log file."""
        with tempfile.TemporaryDirectory() as tmpdir:
            output_dir = Path(tmpdir)
            created, success = write_generation_log(
                output_dir=output_dir,
                project_name="TestProject",
                generated_files=["README.md", "LICENSE"],
                log_format="json"
            )
            self.assertTrue(success)
            self.assertEqual(len(created), 1)
            self.assertTrue((output_dir / "GENERATION_LOG.json").exists())

    def test_writes_both_formats(self):
        """Should write both log files when format is 'both'."""
        with tempfile.TemporaryDirectory() as tmpdir:
            output_dir = Path(tmpdir)
            created, success = write_generation_log(
                output_dir=output_dir,
                project_name="TestProject",
                generated_files=["README.md", "LICENSE"],
                log_format="both"
            )
            self.assertTrue(success)
            self.assertEqual(len(created), 2)
            self.assertTrue((output_dir / "GENERATION_LOG.md").exists())
            self.assertTrue((output_dir / "GENERATION_LOG.json").exists())

    def test_log_to_append_functionality(self):
        """Should append to existing log when log_to is specified."""
        with tempfile.TemporaryDirectory() as tmpdir:
            output_dir = Path(tmpdir)
            log_path = output_dir / "GENERATION_LOG.md"

            # Write initial log
            log_path.write_text("""# Generation Log

| File | Generated | Tool | Version | Customization |
|------|-----------|------|---------|---------------|
| README.md | 2026-01-20 | PFT | v3.6.0 | - |
""")

            # Append to existing log
            created, success = write_generation_log(
                output_dir=output_dir,
                project_name="TestProject",
                generated_files=["LICENSE"],
                log_format="md",
                log_to=str(log_path)
            )

            self.assertTrue(success)
            content = log_path.read_text()
            self.assertIn("README.md", content)
            self.assertIn("LICENSE", content)

    def test_non_interactive_appends_by_default(self):
        """Should append by default in non-interactive mode when log exists."""
        with tempfile.TemporaryDirectory() as tmpdir:
            output_dir = Path(tmpdir)
            log_path = output_dir / "GENERATION_LOG.md"

            # Write initial log
            log_path.write_text("""# Generation Log

| File | Generated | Tool | Version | Customization |
|------|-----------|------|---------|---------------|
| README.md | 2026-01-20 | PFT | v3.6.0 | - |
""")

            # Run without log_to, should detect and append
            created, success = write_generation_log(
                output_dir=output_dir,
                project_name="TestProject",
                generated_files=["LICENSE"],
                log_format="md",
                interactive=False  # Non-interactive defaults to append
            )

            self.assertTrue(success)
            content = log_path.read_text()
            self.assertIn("README.md", content)
            self.assertIn("LICENSE", content)

    def test_force_overwrite_replaces_log(self):
        """Should replace log when force_overwrite is True."""
        with tempfile.TemporaryDirectory() as tmpdir:
            output_dir = Path(tmpdir)
            log_path = output_dir / "GENERATION_LOG.md"

            # Write initial log
            log_path.write_text("""# Generation Log

| File | Generated | Tool | Version | Customization |
|------|-----------|------|---------|---------------|
| README.md | 2026-01-20 | PFT | v3.6.0 | - |
""")

            # Run with force_overwrite
            created, success = write_generation_log(
                output_dir=output_dir,
                project_name="TestProject",
                generated_files=["LICENSE"],
                log_format="md",
                interactive=False,
                force_overwrite=True
            )

            self.assertTrue(success)
            content = log_path.read_text()
            # Original README entry should NOT be present (overwritten)
            # Only LICENSE should be in the fresh log
            self.assertIn("LICENSE", content)
            # Count occurrences - should only have the new file
            self.assertEqual(content.count("| LICENSE |"), 1)


class TestOverwriteProtectionIntegration(unittest.TestCase):
    """Integration tests for overwrite protection behavior."""

    def test_creates_new_log_in_empty_directory(self):
        """Should create new log without prompting in empty directory."""
        with tempfile.TemporaryDirectory() as tmpdir:
            output_dir = Path(tmpdir)
            created, success = write_generation_log(
                output_dir=output_dir,
                project_name="TestProject",
                generated_files=["README.md"],
                log_format="md",
                interactive=True
            )
            self.assertTrue(success)
            self.assertTrue((output_dir / "GENERATION_LOG.md").exists())

    def test_preserves_customization_notes_on_append(self):
        """Should preserve user's customization notes when appending."""
        with tempfile.TemporaryDirectory() as tmpdir:
            output_dir = Path(tmpdir)
            log_path = output_dir / "GENERATION_LOG.md"

            # Write initial log with customization
            log_path.write_text("""# Generation Log

**Project**: TestProject
**Last Updated**: 2026-01-20 10:00:00

| File | Generated | Tool | Version | Customization |
|------|-----------|------|---------|---------------|
| README.md | 2026-01-20 | PFT | v3.6.0 | Added project badges |

## Understanding This Log

Footer content.
""")

            # Append new entries
            created, success = write_generation_log(
                output_dir=output_dir,
                project_name="TestProject",
                generated_files=["LICENSE"],
                log_format="md",
                interactive=False
            )

            content = log_path.read_text()
            # User's customization note should be preserved
            self.assertIn("Added project badges", content)
            self.assertIn("LICENSE", content)


if __name__ == "__main__":
    unittest.main()
