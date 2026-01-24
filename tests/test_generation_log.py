# tests/test_generation_log.py
# Unit tests for core/generation_log.py

"""Unit tests for the generation log module."""

import json
import tempfile
import unittest
from datetime import datetime
from pathlib import Path

from core.generation_log import (
    create_file_record,
    generate_log_md,
    generate_log_json,
    load_existing_log,
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
        """Should append new entries to existing log."""
        existing = """# Generation Log

| File | Generated | Tool | Version | Customization |
|------|-----------|------|---------|---------------|
| README.md | 2026-01-20 | PFT | v3.6.0 | - |
"""
        files = [
            {"file": "LICENSE", "generated": "2026-01-24", "tool": "PFT",
             "tool_version": "v3.7.0", "customization": "-"},
        ]
        content = generate_log_md("TestProject", files, existing)
        self.assertIn("README.md", content)
        self.assertIn("LICENSE", content)


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
            created = write_generation_log(
                output_dir=output_dir,
                project_name="TestProject",
                generated_files=["README.md", "LICENSE"],
                log_format="md"
            )
            self.assertEqual(len(created), 1)
            self.assertTrue((output_dir / "GENERATION_LOG.md").exists())

    def test_writes_json_format(self):
        """Should write JSON log file."""
        with tempfile.TemporaryDirectory() as tmpdir:
            output_dir = Path(tmpdir)
            created = write_generation_log(
                output_dir=output_dir,
                project_name="TestProject",
                generated_files=["README.md", "LICENSE"],
                log_format="json"
            )
            self.assertEqual(len(created), 1)
            self.assertTrue((output_dir / "GENERATION_LOG.json").exists())

    def test_writes_both_formats(self):
        """Should write both log files when format is 'both'."""
        with tempfile.TemporaryDirectory() as tmpdir:
            output_dir = Path(tmpdir)
            created = write_generation_log(
                output_dir=output_dir,
                project_name="TestProject",
                generated_files=["README.md", "LICENSE"],
                log_format="both"
            )
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
            created = write_generation_log(
                output_dir=output_dir,
                project_name="TestProject",
                generated_files=["LICENSE"],
                log_format="md",
                log_to=str(log_path)
            )

            content = log_path.read_text()
            self.assertIn("README.md", content)
            self.assertIn("LICENSE", content)


if __name__ == "__main__":
    unittest.main()
