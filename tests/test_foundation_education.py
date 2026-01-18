# tests/test_foundation_education.py
# Unit tests for foundation/education.py

"""Unit tests for the foundation.education module."""

import unittest

from foundation.education import (
    LITE_PRINCIPLES,
    EDUCATION_CONTENT,
    ETHICAL_USE_AGREEMENT,
    get_principle,
    get_education_content,
    format_principle_display,
)


class TestLitePrinciples(unittest.TestCase):
    """Test governance principles definitions."""

    def test_has_core_principles(self):
        """Should have all core governance principles."""
        core_principles = [
            "readme",
            "contributing",
            "license",
            "code-of-conduct",
            "security",
        ]
        for principle in core_principles:
            self.assertIn(principle, LITE_PRINCIPLES)

    def test_has_v24_principles(self):
        """Should have v2.4.0 security principles."""
        v24_principles = ["enhanced-security", "secrets-detection"]
        for principle in v24_principles:
            self.assertIn(principle, LITE_PRINCIPLES)

    def test_has_v25_principles(self):
        """Should have v2.5.0 advanced governance principles."""
        v25_principles = ["adr", "ci-workflow"]
        for principle in v25_principles:
            self.assertIn(principle, LITE_PRINCIPLES)

    def test_has_v23_principles(self):
        """Should have v2.3.0 community governance principles."""
        v23_principles = ["issue-templates", "pr-template", "changelog"]
        for principle in v23_principles:
            self.assertIn(principle, LITE_PRINCIPLES)

    def test_principle_structure(self):
        """Each principle should have name, why, what, and risk."""
        required_keys = ["name", "why", "what", "risk"]
        for name, principle in LITE_PRINCIPLES.items():
            for key in required_keys:
                self.assertIn(
                    key, principle, f"Principle '{name}' missing '{key}'"
                )
                self.assertIsInstance(
                    principle[key], str, f"Principle '{name}' key '{key}' should be string"
                )
                self.assertGreater(
                    len(principle[key]), 0, f"Principle '{name}' key '{key}' should not be empty"
                )


class TestEducationContent(unittest.TestCase):
    """Test educational content definitions."""

    def test_has_content_for_all_principles(self):
        """Should have educational content for all principles."""
        for principle in LITE_PRINCIPLES:
            self.assertIn(
                principle,
                EDUCATION_CONTENT,
                f"Missing education content for '{principle}'",
            )

    def test_content_is_substantial(self):
        """Educational content should be substantial (>50 chars)."""
        for name, content in EDUCATION_CONTENT.items():
            self.assertIsInstance(content, str)
            self.assertGreater(
                len(content), 50, f"Education content for '{name}' is too short"
            )

    def test_content_includes_learning_marker(self):
        """Educational content should include LEARNING marker."""
        for name, content in EDUCATION_CONTENT.items():
            self.assertIn(
                "LEARNING",
                content,
                f"Education content for '{name}' should include 'LEARNING' marker",
            )


class TestEthicalUseAgreement(unittest.TestCase):
    """Test ethical use agreement."""

    def test_is_substantial(self):
        """Agreement should be substantial."""
        self.assertIsInstance(ETHICAL_USE_AGREEMENT, str)
        self.assertGreater(len(ETHICAL_USE_AGREEMENT), 500)

    def test_includes_key_warnings(self):
        """Agreement should include key warnings."""
        key_phrases = [
            "TEMPLATES ONLY",
            "customized",
            "legal",
            "responsibility",
        ]
        for phrase in key_phrases:
            self.assertIn(
                phrase.lower(),
                ETHICAL_USE_AGREEMENT.lower(),
                f"Agreement should include '{phrase}'",
            )


class TestGetPrinciple(unittest.TestCase):
    """Test get_principle helper function."""

    def test_returns_principle_by_name(self):
        """Should return principle dict by name."""
        principle = get_principle("readme")
        self.assertIsInstance(principle, dict)
        self.assertIn("name", principle)
        self.assertEqual(principle["name"], "README Documentation")

    def test_returns_empty_dict_for_unknown(self):
        """Should return empty dict for unknown principle."""
        principle = get_principle("nonexistent")
        self.assertEqual(principle, {})


class TestGetEducationContent(unittest.TestCase):
    """Test get_education_content helper function."""

    def test_returns_content_by_name(self):
        """Should return content by name."""
        content = get_education_content("readme")
        self.assertIsInstance(content, str)
        self.assertIn("LEARNING", content)

    def test_returns_empty_string_for_unknown(self):
        """Should return empty string for unknown principle."""
        content = get_education_content("nonexistent")
        self.assertEqual(content, "")


class TestFormatPrincipleDisplay(unittest.TestCase):
    """Test format_principle_display helper function."""

    def test_formats_principle_for_display(self):
        """Should format principle in a display box."""
        display = format_principle_display("readme")
        self.assertIsInstance(display, str)
        self.assertIn("README Documentation", display)
        self.assertIn("WHY:", display)
        self.assertIn("WHAT:", display)
        self.assertIn("RISK:", display)

    def test_returns_empty_string_for_unknown(self):
        """Should return empty string for unknown principle."""
        display = format_principle_display("nonexistent")
        self.assertEqual(display, "")


if __name__ == "__main__":
    unittest.main()
