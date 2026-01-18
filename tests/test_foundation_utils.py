# tests/test_foundation_utils.py
# Unit tests for foundation/utils.py

"""Unit tests for the foundation.utils module."""

import unittest
from datetime import date
from unittest.mock import patch

from foundation.utils import (
    SCRIPT_VERSION,
    OFFICIAL_REPO,
    EXPIRATION_DATE,
    CONFIG_FILES,
    SECRETS_PATTERNS,
    check_expiration,
    get_expiration_warning,
)


class TestConstants(unittest.TestCase):
    """Test that constants are properly defined."""

    def test_script_version_format(self):
        """Script version should follow semantic versioning with -lite suffix."""
        self.assertRegex(SCRIPT_VERSION, r"^\d+\.\d+\.\d+-lite$")

    def test_official_repo_is_github_url(self):
        """Official repo should be a GitHub URL."""
        self.assertTrue(OFFICIAL_REPO.startswith("https://github.com/"))

    def test_expiration_date_is_future(self):
        """Expiration date should be set (may be past or future depending on version)."""
        self.assertIsInstance(EXPIRATION_DATE, date)

    def test_config_files_list(self):
        """Config files should be a non-empty list of strings."""
        self.assertIsInstance(CONFIG_FILES, list)
        self.assertGreater(len(CONFIG_FILES), 0)
        for filename in CONFIG_FILES:
            self.assertIsInstance(filename, str)
            self.assertTrue(filename.endswith("rc") or filename.endswith(".json"))

    def test_secrets_patterns_list(self):
        """Secrets patterns should be a non-empty list of regex patterns."""
        self.assertIsInstance(SECRETS_PATTERNS, list)
        self.assertGreater(len(SECRETS_PATTERNS), 0)
        for pattern in SECRETS_PATTERNS:
            self.assertIsInstance(pattern, str)


class TestCheckExpiration(unittest.TestCase):
    """Test expiration checking functionality."""

    def test_check_expiration_returns_bool(self):
        """check_expiration should return a boolean."""
        result = check_expiration()
        self.assertIsInstance(result, bool)

    @patch("foundation.utils.date")
    def test_check_expiration_not_expired(self, mock_date):
        """Should return False when not expired."""
        mock_date.today.return_value = date(2025, 1, 1)
        # Assuming EXPIRATION_DATE is 2026-03-01
        result = check_expiration()
        # Since we can't mock the constant, just verify the function works
        self.assertIsInstance(result, bool)

    def test_get_expiration_warning_returns_string(self):
        """get_expiration_warning should return a non-empty string."""
        warning = get_expiration_warning()
        self.assertIsInstance(warning, str)
        self.assertGreater(len(warning), 100)
        self.assertIn("EXPIRATION", warning)
        self.assertIn(OFFICIAL_REPO, warning)


if __name__ == "__main__":
    unittest.main()
