# tests/test_foundation_guides.py
# Tests for the guides module

"""
Tests for core.guides module.

Tests cover:
    - Individual guide module structure
    - Aggregated dictionaries (ALL_GUIDES, ALL_GUIDE_CONTENT)
    - Category groupings
    - Complexity levels
    - Helper functions
"""

import pytest
from core.guides import (
    ALL_GUIDES,
    ALL_GUIDE_CONTENT,
    GOVERNANCE_GUIDES,
    DEVELOPMENT_GUIDES,
    SECURITY_GUIDES,
    ONBOARDING_GUIDES,
    OPERATIONS_GUIDES,
    GUIDE_COMPLEXITY,
    GUIDE_VERSIONS,
    get_guide,
    get_guide_content,
    get_guides_by_category,
    get_guides_by_complexity,
    list_all_guides,
)


class TestGuideDefinitions:
    """Test guide definitions."""

    def test_all_guides_is_dict(self):
        """ALL_GUIDES should be a dictionary."""
        assert isinstance(ALL_GUIDES, dict)

    def test_all_guide_content_is_dict(self):
        """ALL_GUIDE_CONTENT should be a dictionary."""
        assert isinstance(ALL_GUIDE_CONTENT, dict)

    def test_guide_count(self):
        """Should have 19 guides defined (15 v3.0.0 + 4 v3.2.0)."""
        assert len(ALL_GUIDES) == 19

    def test_content_count(self):
        """Should have 19 content entries (one per guide)."""
        assert len(ALL_GUIDE_CONTENT) == 19

    def test_guides_and_content_keys_match(self):
        """ALL_GUIDES and ALL_GUIDE_CONTENT should have the same keys."""
        assert set(ALL_GUIDES.keys()) == set(ALL_GUIDE_CONTENT.keys())

    def test_all_guides_have_required_fields(self):
        """Each guide must have title, purpose, audience, complexity fields."""
        required_fields = ["title", "purpose", "audience", "complexity"]
        for gid, guide in ALL_GUIDES.items():
            for field in required_fields:
                assert field in guide, f"Guide '{gid}' missing '{field}'"

    def test_all_guides_fields_are_strings(self):
        """All guide fields should be non-empty strings."""
        for gid, guide in ALL_GUIDES.items():
            for field, value in guide.items():
                assert isinstance(value, str), f"Guide '{gid}' field '{field}' is not a string"
                assert len(value) > 0, f"Guide '{gid}' field '{field}' is empty"

    def test_all_content_are_strings(self):
        """All content entries should be non-empty strings."""
        for gid, content in ALL_GUIDE_CONTENT.items():
            assert isinstance(content, str), f"Content for '{gid}' is not a string"
            assert len(content) > 0, f"Content for '{gid}' is empty"


class TestGuideCategories:
    """Test guide category groupings."""

    def test_governance_guides_list(self):
        """GOVERNANCE_GUIDES should contain expected guides."""
        expected = ["versioning", "release-process", "changelog", "compliance-guide"]
        assert GOVERNANCE_GUIDES == expected

    def test_development_guides_list(self):
        """DEVELOPMENT_GUIDES should contain expected guides."""
        expected = [
            "code-review", "adr", "test-strategies", "coding-standards", "api-standards",
            "developer-handbook", "architecture-overview",  # v3.2.0
        ]
        assert DEVELOPMENT_GUIDES == expected

    def test_security_guides_list(self):
        """SECURITY_GUIDES should contain expected guides."""
        expected = ["security-disclosure"]
        assert SECURITY_GUIDES == expected

    def test_onboarding_guides_list(self):
        """ONBOARDING_GUIDES should contain expected guides."""
        expected = [
            "onboarding", "glossary", "faq", "troubleshooting",
            "contributor-handbook",  # v3.2.0
        ]
        assert ONBOARDING_GUIDES == expected

    def test_operations_guides_list(self):
        """OPERATIONS_GUIDES should contain expected guides."""
        expected = ["dependency-guide", "deployment-guide"]  # v3.2.0: added deployment-guide
        assert OPERATIONS_GUIDES == expected

    def test_all_categories_cover_all_guides(self):
        """All category lists together should cover all guides."""
        all_categorized = set(
            GOVERNANCE_GUIDES +
            DEVELOPMENT_GUIDES +
            SECURITY_GUIDES +
            ONBOARDING_GUIDES +
            OPERATIONS_GUIDES
        )
        assert all_categorized == set(ALL_GUIDES.keys())

    def test_no_duplicate_guides_in_categories(self):
        """No guide should appear in multiple categories."""
        all_lists = (
            GOVERNANCE_GUIDES +
            DEVELOPMENT_GUIDES +
            SECURITY_GUIDES +
            ONBOARDING_GUIDES +
            OPERATIONS_GUIDES
        )
        assert len(all_lists) == len(set(all_lists))


class TestGuideComplexity:
    """Test complexity level mapping."""

    def test_guide_complexity_is_dict(self):
        """GUIDE_COMPLEXITY should be a dictionary."""
        assert isinstance(GUIDE_COMPLEXITY, dict)

    def test_all_guides_have_complexity(self):
        """Every guide should have a complexity entry."""
        assert set(GUIDE_COMPLEXITY.keys()) == set(ALL_GUIDES.keys())

    def test_complexity_values_are_valid(self):
        """All complexity values should be valid levels."""
        valid_levels = {"beginner", "intermediate", "advanced"}
        for gid, level in GUIDE_COMPLEXITY.items():
            assert level in valid_levels, f"Guide '{gid}' has invalid complexity '{level}'"

    def test_beginner_guides(self):
        """Should have beginner complexity guides."""
        beginner = [g for g, c in GUIDE_COMPLEXITY.items() if c == "beginner"]
        assert "versioning" in beginner
        assert "changelog" in beginner

    def test_intermediate_guides(self):
        """Should have intermediate complexity guides."""
        intermediate = [g for g, c in GUIDE_COMPLEXITY.items() if c == "intermediate"]
        assert "code-review" in intermediate
        assert "adr" in intermediate

    def test_advanced_guides(self):
        """Should have advanced complexity guides."""
        advanced = [g for g, c in GUIDE_COMPLEXITY.items() if c == "advanced"]
        assert "security-disclosure" in advanced


class TestGuideVersions:
    """Test version mapping."""

    def test_guide_versions_is_dict(self):
        """GUIDE_VERSIONS should be a dictionary."""
        assert isinstance(GUIDE_VERSIONS, dict)

    def test_all_guides_have_versions(self):
        """Every guide should have a version entry."""
        assert set(GUIDE_VERSIONS.keys()) == set(ALL_GUIDES.keys())

    def test_versions_are_valid_semver(self):
        """All versions should be valid semantic version strings."""
        import re
        semver_pattern = r"^\d+\.\d+\.\d+$"
        for gid, version in GUIDE_VERSIONS.items():
            assert re.match(semver_pattern, version), f"Version '{version}' for '{gid}' is not valid semver"


class TestGetGuide:
    """Test get_guide() function."""

    def test_get_existing_guide(self):
        """Should return guide dict for existing guide."""
        result = get_guide("versioning")
        assert isinstance(result, dict)
        assert result["title"] == "Semantic Versioning Guide"

    def test_get_nonexistent_guide(self):
        """Should return empty dict for nonexistent guide."""
        result = get_guide("nonexistent")
        assert result == {}

    def test_get_guide_case_sensitive(self):
        """Guide lookup should be case sensitive."""
        result = get_guide("VERSIONING")
        assert result == {}


class TestGetGuideContent:
    """Test get_guide_content() function."""

    def test_get_existing_content(self):
        """Should return content string for existing guide."""
        result = get_guide_content("versioning")
        assert isinstance(result, str)
        assert "Semantic Versioning" in result

    def test_get_nonexistent_content(self):
        """Should return empty string for nonexistent guide."""
        result = get_guide_content("nonexistent")
        assert result == ""


class TestGetGuidesByCategory:
    """Test get_guides_by_category() function."""

    def test_get_governance_category(self):
        """Should return governance guides list."""
        result = get_guides_by_category("governance")
        assert result == GOVERNANCE_GUIDES

    def test_get_development_category(self):
        """Should return development guides list."""
        result = get_guides_by_category("development")
        assert result == DEVELOPMENT_GUIDES

    def test_get_security_category(self):
        """Should return security guides list."""
        result = get_guides_by_category("security")
        assert result == SECURITY_GUIDES

    def test_get_nonexistent_category(self):
        """Should return empty list for nonexistent category."""
        result = get_guides_by_category("nonexistent")
        assert result == []

    def test_category_case_insensitive(self):
        """Category lookup should be case insensitive."""
        result = get_guides_by_category("GOVERNANCE")
        assert result == GOVERNANCE_GUIDES


class TestGetGuidesByComplexity:
    """Test get_guides_by_complexity() function."""

    def test_get_beginner_guides(self):
        """Should return beginner guides list."""
        result = get_guides_by_complexity("beginner")
        assert "versioning" in result
        assert "changelog" in result

    def test_get_intermediate_guides(self):
        """Should return intermediate guides list."""
        result = get_guides_by_complexity("intermediate")
        assert "code-review" in result
        assert "adr" in result

    def test_get_advanced_guides(self):
        """Should return advanced guides list."""
        result = get_guides_by_complexity("advanced")
        assert "security-disclosure" in result

    def test_get_nonexistent_complexity(self):
        """Should return empty list for nonexistent complexity."""
        result = get_guides_by_complexity("expert")
        assert result == []

    def test_complexity_case_insensitive(self):
        """Complexity lookup should be case insensitive."""
        result = get_guides_by_complexity("BEGINNER")
        assert "versioning" in result


class TestListAllGuides:
    """Test list_all_guides() function."""

    def test_returns_list(self):
        """Should return a list."""
        result = list_all_guides()
        assert isinstance(result, list)

    def test_returns_all_guide_ids(self):
        """Should return all guide IDs."""
        result = list_all_guides()
        assert set(result) == set(ALL_GUIDES.keys())

    def test_returns_19_guides(self):
        """Should return 19 guides (15 v3.0.0 + 4 v3.2.0)."""
        result = list_all_guides()
        assert len(result) == 19


class TestIndividualGuideModules:
    """Test that individual guide modules are properly structured."""

    @pytest.mark.parametrize("guide_id", [
        "versioning",
        "code-review",
        "release-process",
        "changelog",
        "security-disclosure",
        "adr",
        "test-strategies",
        "dependency-guide",
        "compliance-guide",
        "api-standards",
        "troubleshooting",
        "faq",
        "glossary",
        "coding-standards",
        "onboarding",
        # v3.2.0 guides
        "developer-handbook",
        "architecture-overview",
        "deployment-guide",
        "contributor-handbook",
    ])
    def test_guide_in_all_guides(self, guide_id):
        """Each guide ID should be in ALL_GUIDES."""
        assert guide_id in ALL_GUIDES

    @pytest.mark.parametrize("guide_id", [
        "versioning",
        "code-review",
        "release-process",
        "changelog",
        "security-disclosure",
        "adr",
        "test-strategies",
        "dependency-guide",
        "compliance-guide",
        "api-standards",
        "troubleshooting",
        "faq",
        "glossary",
        "coding-standards",
        "onboarding",
        # v3.2.0 guides
        "developer-handbook",
        "architecture-overview",
        "deployment-guide",
        "contributor-handbook",
    ])
    def test_guide_in_all_content(self, guide_id):
        """Each guide ID should be in ALL_GUIDE_CONTENT."""
        assert guide_id in ALL_GUIDE_CONTENT

    @pytest.mark.parametrize("guide_id", [
        "versioning",
        "code-review",
        "release-process",
        "changelog",
        "security-disclosure",
        "adr",
        "test-strategies",
        "dependency-guide",
        "compliance-guide",
        "api-standards",
        "troubleshooting",
        "faq",
        "glossary",
        "coding-standards",
        "onboarding",
        # v3.2.0 guides
        "developer-handbook",
        "architecture-overview",
        "deployment-guide",
        "contributor-handbook",
    ])
    def test_guide_in_complexity(self, guide_id):
        """Each guide ID should be in GUIDE_COMPLEXITY."""
        assert guide_id in GUIDE_COMPLEXITY

    @pytest.mark.parametrize("guide_id", [
        "versioning",
        "code-review",
        "release-process",
        "changelog",
        "security-disclosure",
        "adr",
        "test-strategies",
        "dependency-guide",
        "compliance-guide",
        "api-standards",
        "troubleshooting",
        "faq",
        "glossary",
        "coding-standards",
        "onboarding",
        # v3.2.0 guides
        "developer-handbook",
        "architecture-overview",
        "deployment-guide",
        "contributor-handbook",
    ])
    def test_guide_in_versions(self, guide_id):
        """Each guide ID should be in GUIDE_VERSIONS."""
        assert guide_id in GUIDE_VERSIONS


class TestGuideContentQuality:
    """Test that guide content meets quality standards."""

    @pytest.mark.parametrize("guide_id", [
        "versioning",
        "code-review",
        "release-process",
        "changelog",
        "security-disclosure",
        "adr",
        "test-strategies",
        "dependency-guide",
        "compliance-guide",
        "api-standards",
        "troubleshooting",
        "faq",
        "glossary",
        "coding-standards",
        "onboarding",
        # v3.2.0 guides
        "developer-handbook",
        "architecture-overview",
        "deployment-guide",
        "contributor-handbook",
    ])
    def test_content_has_overview(self, guide_id):
        """Each guide content should have an overview section."""
        content = get_guide_content(guide_id)
        assert "##" in content  # Has headings

    @pytest.mark.parametrize("guide_id", [
        "versioning",
        "code-review",
        "release-process",
        "changelog",
        "security-disclosure",
        "adr",
        "test-strategies",
        "dependency-guide",
        "compliance-guide",
        "api-standards",
        "troubleshooting",
        "faq",
        "glossary",
        "coding-standards",
        "onboarding",
        # v3.2.0 guides
        "developer-handbook",
        "architecture-overview",
        "deployment-guide",
        "contributor-handbook",
    ])
    def test_content_minimum_length(self, guide_id):
        """Each guide content should have substantial content."""
        content = get_guide_content(guide_id)
        assert len(content) > 500  # At least 500 characters


class TestCorePackageExports:
    """Test that guides are properly exported from core package."""

    def test_core_exports_all_guides(self):
        """core package should export ALL_GUIDES."""
        from core import ALL_GUIDES as core_guides
        assert core_guides == ALL_GUIDES

    def test_core_exports_get_guide(self):
        """core package should export get_guide."""
        from core import get_guide as core_get_guide
        assert core_get_guide("versioning") == get_guide("versioning")

    def test_core_exports_list_all_guides(self):
        """core package should export list_all_guides."""
        from core import list_all_guides as core_list_guides
        assert core_list_guides() == list_all_guides()
