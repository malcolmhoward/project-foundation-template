# tests/test_foundation_presets.py
# Unit tests for core/presets module

"""Unit tests for the core.presets module."""

import unittest

from core.presets import (
    PRESETS,
    DEFAULT_PRESET,
    MINIMAL_PRESET,
    LIGHT_PRESET,
    STANDARD_PRESET,
    STRICT_PRESET,
    ENTERPRISE_PRESET,
    get_preset,
    list_presets,
    get_preset_description,
)


class TestPresetsDefinition(unittest.TestCase):
    """Test preset definitions."""

    def test_has_all_five_presets(self):
        """Should have all five governance presets."""
        expected = ["minimal", "light", "standard", "strict", "enterprise"]
        for name in expected:
            self.assertIn(name, PRESETS)

    def test_default_preset_is_standard(self):
        """Default preset should be standard."""
        self.assertEqual(DEFAULT_PRESET, "standard")

    def test_presets_count(self):
        """Should have exactly 5 presets."""
        self.assertEqual(len(PRESETS), 5)


class TestPresetStructure(unittest.TestCase):
    """Test that each preset has required structure."""

    def test_all_presets_have_name(self):
        """Each preset should have a name field."""
        for name, preset in PRESETS.items():
            self.assertIn("name", preset, f"Preset '{name}' missing 'name'")
            self.assertEqual(preset["name"], name)

    def test_all_presets_have_description(self):
        """Each preset should have a description."""
        for name, preset in PRESETS.items():
            self.assertIn("description", preset, f"Preset '{name}' missing 'description'")
            self.assertIsInstance(preset["description"], str)
            self.assertGreater(len(preset["description"]), 10)

    def test_all_presets_have_principles(self):
        """Each preset should have a principles list."""
        for name, preset in PRESETS.items():
            self.assertIn("principles", preset, f"Preset '{name}' missing 'principles'")
            self.assertIsInstance(preset["principles"], list)
            self.assertGreater(len(preset["principles"]), 0)

    def test_all_presets_have_features(self):
        """Each preset should have a features dict."""
        for name, preset in PRESETS.items():
            self.assertIn("features", preset, f"Preset '{name}' missing 'features'")
            self.assertIsInstance(preset["features"], dict)

    def test_all_presets_have_recommended_for(self):
        """Each preset should have recommended_for list."""
        for name, preset in PRESETS.items():
            self.assertIn("recommended_for", preset, f"Preset '{name}' missing 'recommended_for'")
            self.assertIsInstance(preset["recommended_for"], list)


class TestPresetHierarchy(unittest.TestCase):
    """Test that presets build on each other properly."""

    def test_minimal_has_core_principles(self):
        """Minimal should have readme, contributing, license."""
        principles = MINIMAL_PRESET["principles"]
        self.assertIn("readme", principles)
        self.assertIn("contributing", principles)
        self.assertIn("license", principles)

    def test_light_extends_minimal(self):
        """Light should include all minimal principles."""
        minimal_principles = set(MINIMAL_PRESET["principles"])
        light_principles = set(LIGHT_PRESET["principles"])
        self.assertTrue(minimal_principles.issubset(light_principles))

    def test_standard_extends_light(self):
        """Standard should include all light principles."""
        light_principles = set(LIGHT_PRESET["principles"])
        standard_principles = set(STANDARD_PRESET["principles"])
        self.assertTrue(light_principles.issubset(standard_principles))

    def test_strict_extends_standard(self):
        """Strict should include all standard principles."""
        standard_principles = set(STANDARD_PRESET["principles"])
        strict_principles = set(STRICT_PRESET["principles"])
        self.assertTrue(standard_principles.issubset(strict_principles))

    def test_enterprise_extends_strict(self):
        """Enterprise should include all strict principles."""
        strict_principles = set(STRICT_PRESET["principles"])
        enterprise_principles = set(ENTERPRISE_PRESET["principles"])
        self.assertTrue(strict_principles.issubset(enterprise_principles))

    def test_principle_counts_increase(self):
        """Each higher preset should have more or equal principles."""
        counts = [
            len(MINIMAL_PRESET["principles"]),
            len(LIGHT_PRESET["principles"]),
            len(STANDARD_PRESET["principles"]),
            len(STRICT_PRESET["principles"]),
            len(ENTERPRISE_PRESET["principles"]),
        ]
        for i in range(len(counts) - 1):
            self.assertLessEqual(counts[i], counts[i + 1])


class TestFeatureFlags(unittest.TestCase):
    """Test feature flags in presets."""

    def test_minimal_has_core_features_only(self):
        """Minimal should only enable core features."""
        features = MINIMAL_PRESET["features"]
        self.assertTrue(features["readme"])
        self.assertTrue(features["contributing"])
        self.assertTrue(features["license"])
        self.assertTrue(features["gitignore"])
        self.assertFalse(features["code_of_conduct"])
        self.assertFalse(features["security"])

    def test_standard_has_ci_workflow(self):
        """Standard should include CI workflow."""
        features = STANDARD_PRESET["features"]
        self.assertTrue(features["ci_workflow"])

    def test_strict_has_security_features(self):
        """Strict should include security features."""
        features = STRICT_PRESET["features"]
        self.assertTrue(features["enhanced_security"])
        self.assertTrue(features["secrets_detection"])
        self.assertTrue(features["adr"])

    def test_enterprise_has_all_features(self):
        """Enterprise should have all features enabled."""
        features = ENTERPRISE_PRESET["features"]
        for key, value in features.items():
            self.assertTrue(value, f"Enterprise feature '{key}' should be True")


class TestGetPreset(unittest.TestCase):
    """Test get_preset helper function."""

    def test_returns_preset_by_name(self):
        """Should return preset dict by name."""
        preset = get_preset("minimal")
        self.assertEqual(preset["name"], "minimal")

    def test_case_insensitive(self):
        """Should be case insensitive."""
        preset1 = get_preset("STANDARD")
        preset2 = get_preset("Standard")
        preset3 = get_preset("standard")
        self.assertEqual(preset1, preset2)
        self.assertEqual(preset2, preset3)

    def test_returns_empty_dict_for_unknown(self):
        """Should return empty dict for unknown preset."""
        preset = get_preset("nonexistent")
        self.assertEqual(preset, {})


class TestListPresets(unittest.TestCase):
    """Test list_presets helper function."""

    def test_returns_list(self):
        """Should return a list."""
        presets = list_presets()
        self.assertIsInstance(presets, list)

    def test_contains_all_presets(self):
        """Should contain all preset names."""
        presets = list_presets()
        expected = ["minimal", "light", "standard", "strict", "enterprise"]
        for name in expected:
            self.assertIn(name, presets)


class TestGetPresetDescription(unittest.TestCase):
    """Test get_preset_description helper function."""

    def test_returns_description(self):
        """Should return preset description."""
        desc = get_preset_description("minimal")
        self.assertIn("Core essentials", desc)

    def test_returns_empty_string_for_unknown(self):
        """Should return empty string for unknown preset."""
        desc = get_preset_description("nonexistent")
        self.assertEqual(desc, "")


class TestImportFromPackage(unittest.TestCase):
    """Test that presets can be imported from core package."""

    def test_import_from_core(self):
        """Should be importable from core package."""
        from core import PRESETS as CorePresets
        self.assertEqual(CorePresets, PRESETS)

    def test_get_preset_from_core(self):
        """get_preset should be importable from core."""
        from core import get_preset as core_get_preset
        self.assertEqual(core_get_preset, get_preset)


if __name__ == "__main__":
    unittest.main()
