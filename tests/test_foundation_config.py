# tests/test_foundation_config.py
# Unit tests for foundation/config.py

"""Unit tests for the foundation.config module."""

import io
import json
import os
import tempfile
import unittest
from unittest.mock import patch
from argparse import Namespace
from pathlib import Path

from core.config import (
    CONFIG_KEY_MAPPING,
    DEFAULT_VALUES,
    load_config_file,
    merge_config_with_args,
    validate_arguments,
)


class TestConfigKeyMapping(unittest.TestCase):
    """Test configuration key mapping."""

    def test_mapping_has_required_keys(self):
        """Mapping should include all core config options."""
        required_keys = ["project_name", "author_name", "license", "output_dir"]
        for key in required_keys:
            self.assertIn(key, CONFIG_KEY_MAPPING)

    def test_mapping_supports_multiple_naming_conventions(self):
        """Mapping should support snake_case, kebab-case, and camelCase."""
        # Check project_name variations
        self.assertEqual(CONFIG_KEY_MAPPING["project_name"], "project_name")
        self.assertEqual(CONFIG_KEY_MAPPING["project-name"], "project_name")
        self.assertEqual(CONFIG_KEY_MAPPING["projectName"], "project_name")


class TestDefaultValues(unittest.TestCase):
    """Test default values."""

    def test_required_fields_are_none(self):
        """Required fields should default to None."""
        self.assertIsNone(DEFAULT_VALUES["project_name"])
        self.assertIsNone(DEFAULT_VALUES["author_name"])

    def test_license_defaults_to_mit(self):
        """License should default to MIT."""
        self.assertEqual(DEFAULT_VALUES["license"], "mit")

    def test_boolean_options_default_to_false(self):
        """Boolean options should default to False."""
        boolean_keys = [
            "include_coc",
            "include_security",
            "include_github_templates",
            "include_changelog",
            "include_all",
            "include_enhanced_security",
            "include_secrets_detection",
            "include_adr",
            "include_ci",
            "verbose",
            "non_interactive",
            "accept_terms",
        ]
        for key in boolean_keys:
            self.assertFalse(DEFAULT_VALUES[key], f"{key} should default to False")


class TestLoadConfigFile(unittest.TestCase):
    """Test configuration file loading."""

    def test_returns_empty_dict_when_no_config(self):
        """Should return empty dict when no config file exists."""
        with tempfile.TemporaryDirectory() as tmpdir:
            original_cwd = os.getcwd()
            try:
                os.chdir(tmpdir)
                config = load_config_file()
                self.assertEqual(config, {})
            finally:
                os.chdir(original_cwd)

    def test_loads_explicit_config_path(self):
        """Should load config from explicit path."""
        with tempfile.TemporaryDirectory() as tmpdir:
            config_path = Path(tmpdir) / "test_config.json"
            config_path.write_text(json.dumps({"project_name": "TestProject"}))
            config = load_config_file(str(config_path))
            self.assertEqual(config.get("project_name"), "TestProject")

    def test_returns_empty_dict_for_missing_explicit_config(self):
        """Should return empty dict when explicit path doesn't exist."""
        config = load_config_file("/nonexistent/path/config.json")
        self.assertEqual(config, {})

    def test_returns_empty_dict_for_invalid_json(self):
        """Should return empty dict for invalid JSON."""
        with tempfile.TemporaryDirectory() as tmpdir:
            config_path = Path(tmpdir) / "invalid_config.json"
            config_path.write_text("not valid json {{{")
            config = load_config_file(str(config_path))
            self.assertEqual(config, {})


class TestMergeConfigWithArgs(unittest.TestCase):
    """Test merging config with command-line arguments."""

    def test_config_applies_to_default_values(self):
        """Config values should apply when args have default values."""
        args = Namespace(
            project_name=None,
            author_name=None,
            license="mit",
        )
        config = {"project_name": "FromConfig", "author_name": "Config Author"}
        result = merge_config_with_args(args, config)
        self.assertEqual(result.project_name, "FromConfig")
        self.assertEqual(result.author_name, "Config Author")

    def test_cli_args_override_config(self):
        """CLI arguments should override config values."""
        args = Namespace(
            project_name="FromCLI",
            author_name=None,
            license="mit",
        )
        config = {"project_name": "FromConfig", "author_name": "Config Author"}
        result = merge_config_with_args(args, config)
        self.assertEqual(result.project_name, "FromCLI")
        self.assertEqual(result.author_name, "Config Author")


class TestCommandLineOnlySettings(unittest.TestCase):
    """Accepting the agreement and overwriting files can't be set in a config file (#93, #113)."""

    def _args(self):
        return Namespace(project_name=None, author_name=None, license="mit",
                         non_interactive=False, accept_terms=False, force_overwrite=False)

    def test_accept_terms_in_config_is_ignored(self):
        for key in ("accept_terms", "accept-terms", "acceptTerms"):
            with self.subTest(key=key), patch("sys.stderr", new_callable=io.StringIO) as err:
                result = merge_config_with_args(self._args(), {key: True, "non_interactive": True})
                self.assertFalse(result.accept_terms)
                self.assertTrue(result.non_interactive)
                self.assertIn("--accept-terms", err.getvalue())

    def test_force_overwrite_in_config_is_ignored(self):
        for key in ("force_overwrite", "force-overwrite", "forceOverwrite"):
            with self.subTest(key=key), patch("sys.stderr", new_callable=io.StringIO) as err:
                result = merge_config_with_args(self._args(), {key: True})
                self.assertFalse(result.force_overwrite)
                self.assertIn("--force-overwrite", err.getvalue())

    def test_config_alone_cannot_pass_validation_in_non_interactive_mode(self):
        args = merge_config_with_args(
            Namespace(project_name=None, author_name=None, license="mit",
                      non_interactive=False, accept_terms=False, force_overwrite=False),
            {"project_name": "P", "author_name": "A", "non_interactive": True, "accept_terms": True})
        is_valid, message = validate_arguments(args)
        self.assertFalse(is_valid)
        self.assertIn("--accept-terms", message)


class TestValidateArguments(unittest.TestCase):
    """Test argument validation."""

    def test_valid_args_pass(self):
        """Valid arguments should pass validation."""
        args = Namespace(
            project_name="TestProject",
            author_name="Test Author",
            non_interactive=False,
            accept_terms=False,
        )
        is_valid, error = validate_arguments(args)
        self.assertTrue(is_valid)
        self.assertEqual(error, "")

    def test_missing_project_name_fails(self):
        """Missing project name should fail validation."""
        args = Namespace(
            project_name=None,
            author_name="Test Author",
            non_interactive=False,
            accept_terms=False,
        )
        is_valid, error = validate_arguments(args)
        self.assertFalse(is_valid)
        self.assertIn("project-name", error)

    def test_missing_author_name_fails(self):
        """Missing author name should fail validation."""
        args = Namespace(
            project_name="TestProject",
            author_name=None,
            non_interactive=False,
            accept_terms=False,
        )
        is_valid, error = validate_arguments(args)
        self.assertFalse(is_valid)
        self.assertIn("author-name", error)

    def test_non_interactive_requires_accept_terms(self):
        """Non-interactive mode requires accept-terms."""
        args = Namespace(
            project_name="TestProject",
            author_name="Test Author",
            non_interactive=True,
            accept_terms=False,
        )
        is_valid, error = validate_arguments(args)
        self.assertFalse(is_valid)
        self.assertIn("accept-terms", error)

    def test_non_interactive_with_accept_terms_passes(self):
        """Non-interactive mode with accept-terms should pass."""
        args = Namespace(
            project_name="TestProject",
            author_name="Test Author",
            non_interactive=True,
            accept_terms=True,
        )
        is_valid, error = validate_arguments(args)
        self.assertTrue(is_valid)


if __name__ == "__main__":
    unittest.main()
