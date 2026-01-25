# tests/test_foundation_principles.py
# Tests for the principles module

"""
Tests for core.principles module.

Tests cover:
    - Individual principle module structure
    - Aggregated dictionaries (ALL_PRINCIPLES, ALL_EDUCATION)
    - Category groupings
    - Version mapping
    - Helper functions
"""

import pytest
from core.principles import (
    ALL_PRINCIPLES,
    ALL_EDUCATION,
    CORE_PRINCIPLES,
    GOVERNANCE_PRINCIPLES,
    SECURITY_PRINCIPLES,
    ADVANCED_PRINCIPLES,
    COMMUNITY_PRINCIPLES,
    QUALITY_PRINCIPLES,
    COMPLIANCE_PRINCIPLES,
    INFRASTRUCTURE_PRINCIPLES,
    INCLUSIVITY_PRINCIPLES,
    LIFECYCLE_PRINCIPLES,
    PRINCIPLE_VERSIONS,
    get_principle,
    get_education,
    get_principles_by_category,
    get_principles_for_version,
    list_all_principles,
)


class TestPrincipleDefinitions:
    """Test individual principle definitions."""

    def test_all_principles_is_dict(self):
        """ALL_PRINCIPLES should be a dictionary."""
        assert isinstance(ALL_PRINCIPLES, dict)

    def test_all_education_is_dict(self):
        """ALL_EDUCATION should be a dictionary."""
        assert isinstance(ALL_EDUCATION, dict)

    def test_principle_count(self):
        """Should have 23 principles defined."""
        assert len(ALL_PRINCIPLES) == 23

    def test_education_count(self):
        """Should have 23 education entries (one per principle)."""
        assert len(ALL_EDUCATION) == 23

    def test_principles_and_education_keys_match(self):
        """ALL_PRINCIPLES and ALL_EDUCATION should have the same keys."""
        assert set(ALL_PRINCIPLES.keys()) == set(ALL_EDUCATION.keys())

    def test_all_principles_have_required_fields(self):
        """Each principle must have name, why, what, risk fields."""
        required_fields = ["name", "why", "what", "risk"]
        for pid, principle in ALL_PRINCIPLES.items():
            for field in required_fields:
                assert field in principle, f"Principle '{pid}' missing '{field}'"

    def test_all_principles_fields_are_strings(self):
        """All principle fields should be non-empty strings."""
        for pid, principle in ALL_PRINCIPLES.items():
            for field, value in principle.items():
                assert isinstance(value, str), f"Principle '{pid}' field '{field}' is not a string"
                assert len(value) > 0, f"Principle '{pid}' field '{field}' is empty"

    def test_all_education_are_strings(self):
        """All education entries should be non-empty strings."""
        for pid, education in ALL_EDUCATION.items():
            assert isinstance(education, str), f"Education for '{pid}' is not a string"
            assert len(education) > 0, f"Education for '{pid}' is empty"


class TestPrincipleCategories:
    """Test principle category groupings."""

    def test_core_principles_list(self):
        """CORE_PRINCIPLES should contain expected principles."""
        expected = ["readme", "contributing", "license"]
        assert CORE_PRINCIPLES == expected

    def test_governance_principles_list(self):
        """GOVERNANCE_PRINCIPLES should contain expected principles."""
        expected = ["code-of-conduct", "security"]
        assert GOVERNANCE_PRINCIPLES == expected

    def test_security_principles_list(self):
        """SECURITY_PRINCIPLES should contain expected principles."""
        expected = ["enhanced-security", "secrets-detection"]
        assert SECURITY_PRINCIPLES == expected

    def test_advanced_principles_list(self):
        """ADVANCED_PRINCIPLES should contain expected principles."""
        expected = ["adr", "ci-workflow"]
        assert ADVANCED_PRINCIPLES == expected

    def test_community_principles_list(self):
        """COMMUNITY_PRINCIPLES should contain expected principles."""
        expected = ["issue-templates", "pr-template", "changelog"]
        assert COMMUNITY_PRINCIPLES == expected

    def test_all_categories_cover_all_principles(self):
        """All category lists together should cover all principles."""
        all_categorized = set(
            CORE_PRINCIPLES +
            GOVERNANCE_PRINCIPLES +
            SECURITY_PRINCIPLES +
            ADVANCED_PRINCIPLES +
            COMMUNITY_PRINCIPLES +
            QUALITY_PRINCIPLES +
            COMPLIANCE_PRINCIPLES +
            INFRASTRUCTURE_PRINCIPLES +
            INCLUSIVITY_PRINCIPLES +
            LIFECYCLE_PRINCIPLES
        )
        assert all_categorized == set(ALL_PRINCIPLES.keys())

    def test_no_duplicate_principles_in_categories(self):
        """No principle should appear in multiple categories."""
        all_lists = (
            CORE_PRINCIPLES +
            GOVERNANCE_PRINCIPLES +
            SECURITY_PRINCIPLES +
            ADVANCED_PRINCIPLES +
            COMMUNITY_PRINCIPLES +
            QUALITY_PRINCIPLES +
            COMPLIANCE_PRINCIPLES +
            INFRASTRUCTURE_PRINCIPLES +
            INCLUSIVITY_PRINCIPLES +
            LIFECYCLE_PRINCIPLES
        )
        assert len(all_lists) == len(set(all_lists))


class TestPrincipleVersions:
    """Test version mapping."""

    def test_principle_versions_is_dict(self):
        """PRINCIPLE_VERSIONS should be a dictionary."""
        assert isinstance(PRINCIPLE_VERSIONS, dict)

    def test_all_principles_have_versions(self):
        """Every principle should have a version entry."""
        assert set(PRINCIPLE_VERSIONS.keys()) == set(ALL_PRINCIPLES.keys())

    def test_versions_are_valid_semver(self):
        """All versions should be valid semantic version strings."""
        import re
        semver_pattern = r"^\d+\.\d+\.\d+$"
        for pid, version in PRINCIPLE_VERSIONS.items():
            assert re.match(semver_pattern, version), f"Version '{version}' for '{pid}' is not valid semver"

    def test_core_principles_introduced_early(self):
        """Core principles should be introduced in v2.1.0."""
        for pid in CORE_PRINCIPLES:
            assert PRINCIPLE_VERSIONS[pid] == "2.1.0"

    def test_security_principles_introduced_v240(self):
        """Security principles should be introduced in v2.4.0."""
        for pid in SECURITY_PRINCIPLES:
            assert PRINCIPLE_VERSIONS[pid] == "2.4.0"

    def test_advanced_principles_introduced_v250(self):
        """Advanced principles should be introduced in v2.5.0."""
        for pid in ADVANCED_PRINCIPLES:
            assert PRINCIPLE_VERSIONS[pid] == "2.5.0"


class TestGetPrinciple:
    """Test get_principle() function."""

    def test_get_existing_principle(self):
        """Should return principle dict for existing principle."""
        result = get_principle("readme")
        assert isinstance(result, dict)
        assert result["name"] == "README Documentation"

    def test_get_nonexistent_principle(self):
        """Should return empty dict for nonexistent principle."""
        result = get_principle("nonexistent")
        assert result == {}

    def test_get_principle_case_sensitive(self):
        """Principle lookup should be case sensitive."""
        result = get_principle("README")
        assert result == {}


class TestGetEducation:
    """Test get_education() function."""

    def test_get_existing_education(self):
        """Should return education string for existing principle."""
        result = get_education("readme")
        assert isinstance(result, str)
        assert "README" in result

    def test_get_nonexistent_education(self):
        """Should return empty string for nonexistent principle."""
        result = get_education("nonexistent")
        assert result == ""


class TestGetPrinciplesByCategory:
    """Test get_principles_by_category() function."""

    def test_get_core_category(self):
        """Should return core principles list."""
        result = get_principles_by_category("core")
        assert result == CORE_PRINCIPLES

    def test_get_governance_category(self):
        """Should return governance principles list."""
        result = get_principles_by_category("governance")
        assert result == GOVERNANCE_PRINCIPLES

    def test_get_security_category(self):
        """Should return security principles list."""
        result = get_principles_by_category("security")
        assert result == SECURITY_PRINCIPLES

    def test_get_advanced_category(self):
        """Should return advanced principles list."""
        result = get_principles_by_category("advanced")
        assert result == ADVANCED_PRINCIPLES

    def test_get_community_category(self):
        """Should return community principles list."""
        result = get_principles_by_category("community")
        assert result == COMMUNITY_PRINCIPLES

    def test_get_nonexistent_category(self):
        """Should return empty list for nonexistent category."""
        result = get_principles_by_category("nonexistent")
        assert result == []

    def test_category_case_insensitive(self):
        """Category lookup should be case insensitive."""
        result = get_principles_by_category("CORE")
        assert result == CORE_PRINCIPLES


class TestGetPrinciplesForVersion:
    """Test get_principles_for_version() function."""

    def test_version_210_has_core_principles(self):
        """v2.1.0 should include core principles."""
        result = get_principles_for_version("2.1.0")
        for pid in CORE_PRINCIPLES:
            assert pid in result

    def test_version_230_has_community_principles(self):
        """v2.3.0 should include community principles."""
        result = get_principles_for_version("2.3.0")
        for pid in COMMUNITY_PRINCIPLES:
            assert pid in result

    def test_version_240_has_security_principles(self):
        """v2.4.0 should include security principles."""
        result = get_principles_for_version("2.4.0")
        for pid in SECURITY_PRINCIPLES:
            assert pid in result

    def test_version_250_has_advanced_principles(self):
        """v2.5.0 should include advanced principles."""
        result = get_principles_for_version("2.5.0")
        for pid in ADVANCED_PRINCIPLES:
            assert pid in result

    def test_version_300_has_all_principles(self):
        """v3.0.0 should include all principles."""
        result = get_principles_for_version("3.0.0")
        assert set(result) == set(ALL_PRINCIPLES.keys())

    def test_lite_suffix_handled(self):
        """Version with -lite suffix should work."""
        result = get_principles_for_version("3.0.0-lite")
        assert set(result) == set(ALL_PRINCIPLES.keys())

    def test_early_version_excludes_later_principles(self):
        """Early version should not include later principles."""
        result = get_principles_for_version("2.2.0")
        assert "enhanced-security" not in result  # Added in 2.4.0
        assert "adr" not in result  # Added in 2.5.0


class TestListAllPrinciples:
    """Test list_all_principles() function."""

    def test_returns_list(self):
        """Should return a list."""
        result = list_all_principles()
        assert isinstance(result, list)

    def test_returns_all_principle_ids(self):
        """Should return all principle IDs."""
        result = list_all_principles()
        assert set(result) == set(ALL_PRINCIPLES.keys())

    def test_returns_23_principles(self):
        """Should return 23 principles."""
        result = list_all_principles()
        assert len(result) == 23


class TestIndividualPrincipleModules:
    """Test that individual principle modules are properly structured."""

    @pytest.mark.parametrize("principle_id", [
        "readme",
        "contributing",
        "license",
        "code-of-conduct",
        "security",
        "enhanced-security",
        "secrets-detection",
        "adr",
        "ci-workflow",
        "issue-templates",
        "pr-template",
        "changelog",
    ])
    def test_principle_in_all_principles(self, principle_id):
        """Each principle ID should be in ALL_PRINCIPLES."""
        assert principle_id in ALL_PRINCIPLES

    @pytest.mark.parametrize("principle_id", [
        "readme",
        "contributing",
        "license",
        "code-of-conduct",
        "security",
        "enhanced-security",
        "secrets-detection",
        "adr",
        "ci-workflow",
        "issue-templates",
        "pr-template",
        "changelog",
    ])
    def test_principle_in_all_education(self, principle_id):
        """Each principle ID should be in ALL_EDUCATION."""
        assert principle_id in ALL_EDUCATION

    @pytest.mark.parametrize("principle_id", [
        "readme",
        "contributing",
        "license",
        "code-of-conduct",
        "security",
        "enhanced-security",
        "secrets-detection",
        "adr",
        "ci-workflow",
        "issue-templates",
        "pr-template",
        "changelog",
    ])
    def test_principle_in_versions(self, principle_id):
        """Each principle ID should be in PRINCIPLE_VERSIONS."""
        assert principle_id in PRINCIPLE_VERSIONS


class TestBackwardCompatibility:
    """Test backward compatibility with education.py re-exports."""

    def test_education_module_exports_lite_principles(self):
        """education.py should export LITE_PRINCIPLES (alias for ALL_PRINCIPLES)."""
        from core.education import LITE_PRINCIPLES
        assert LITE_PRINCIPLES == ALL_PRINCIPLES

    def test_education_module_exports_education_content(self):
        """education.py should export EDUCATION_CONTENT (alias for ALL_EDUCATION)."""
        from core.education import EDUCATION_CONTENT
        assert EDUCATION_CONTENT == ALL_EDUCATION

    def test_education_module_exports_get_principle(self):
        """education.py should export get_principle."""
        from core.education import get_principle as edu_get_principle
        assert edu_get_principle("readme") == get_principle("readme")

    def test_education_module_exports_get_education_content(self):
        """education.py should export get_education_content."""
        from core.education import get_education_content
        assert get_education_content("readme") == get_education("readme")
