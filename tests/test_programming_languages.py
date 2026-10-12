# tests/test_programming_languages.py
# Tests for programming language configurations (v3.5.0)

"""
Tests for the programming languages module.

Verifies that all language configurations are properly structured
and contain required fields.
"""

import pytest

from core.programming_languages import (
    ALL_LANGUAGES,
    LANGUAGE_MODULES,
    TIER_1_LANGUAGES,
    TIER_2_LANGUAGES,
    TIER_3_LANGUAGES,
    SPECIALIZED_LANGUAGES,
    get_language,
    get_languages_by_extension,
    get_all_extensions,
    get_tools_for_language,
    get_precommit_hooks,
    get_ci_workflow,
    detect_languages,
    get_recommended_tools,
)


class TestLanguageRegistry:
    """Tests for the language registry and constants."""

    def test_all_languages_count(self):
        """Verify total number of supported languages."""
        assert len(ALL_LANGUAGES) == 18

    def test_tier_1_languages(self):
        """Verify Tier 1 languages."""
        expected = ["python", "javascript", "typescript"]
        assert TIER_1_LANGUAGES == expected

    def test_tier_2_languages(self):
        """Verify Tier 2 languages."""
        expected = ["go", "rust", "java", "csharp"]
        assert TIER_2_LANGUAGES == expected

    def test_tier_3_languages(self):
        """Verify Tier 3 languages."""
        expected = ["c", "cpp", "php", "ruby", "swift", "kotlin", "bash", "scala"]
        assert TIER_3_LANGUAGES == expected

    def test_specialized_languages(self):
        """Verify specialized languages."""
        expected = ["gdscript", "lua", "haxe"]
        assert SPECIALIZED_LANGUAGES == expected

    def test_all_tiers_account_for_all_languages(self):
        """Verify all tiers combined include all languages."""
        all_tiers = (
            TIER_1_LANGUAGES +
            TIER_2_LANGUAGES +
            TIER_3_LANGUAGES +
            SPECIALIZED_LANGUAGES
        )
        assert set(all_tiers) == set(ALL_LANGUAGES.keys())


class TestLanguageConfiguration:
    """Tests for individual language configurations."""

    @pytest.mark.parametrize("lang_id", list(ALL_LANGUAGES.keys()))
    def test_language_has_required_fields(self, lang_id):
        """Verify each language has required configuration fields."""
        config = ALL_LANGUAGES[lang_id]

        # Required fields
        assert "name" in config, f"{lang_id} missing 'name'"
        assert "id" in config, f"{lang_id} missing 'id'"
        assert "extensions" in config, f"{lang_id} missing 'extensions'"
        assert "category" in config, f"{lang_id} missing 'category'"
        assert "official_website" in config, f"{lang_id} missing 'official_website'"
        assert "documentation_url" in config, f"{lang_id} missing 'documentation_url'"

    @pytest.mark.parametrize("lang_id", list(ALL_LANGUAGES.keys()))
    def test_language_id_matches_key(self, lang_id):
        """Verify the language ID in config matches the registry key."""
        config = ALL_LANGUAGES[lang_id]
        assert config["id"] == lang_id

    @pytest.mark.parametrize("lang_id", list(ALL_LANGUAGES.keys()))
    def test_language_has_extensions(self, lang_id):
        """Verify each language has at least one file extension."""
        config = ALL_LANGUAGES[lang_id]
        assert len(config["extensions"]) > 0, f"{lang_id} has no extensions"

    @pytest.mark.parametrize("lang_id", list(ALL_LANGUAGES.keys()))
    def test_language_has_valid_category(self, lang_id):
        """Verify each language has a valid category."""
        config = ALL_LANGUAGES[lang_id]
        valid_categories = ["tier-1", "tier-2", "tier-3", "specialized"]
        assert config["category"] in valid_categories, f"{lang_id} has invalid category"

    @pytest.mark.parametrize("lang_id", list(ALL_LANGUAGES.keys()))
    def test_language_has_official_website(self, lang_id):
        """Verify each language has an official website URL."""
        config = ALL_LANGUAGES[lang_id]
        assert config["official_website"].startswith("https://"), \
            f"{lang_id} official_website should start with https://"

    @pytest.mark.parametrize("lang_id", list(ALL_LANGUAGES.keys()))
    def test_language_has_documentation_url(self, lang_id):
        """Verify each language has a documentation URL."""
        config = ALL_LANGUAGES[lang_id]
        assert config["documentation_url"].startswith("https://"), \
            f"{lang_id} documentation_url should start with https://"


class TestLanguageTools:
    """Tests for language tool configurations."""

    @pytest.mark.parametrize("lang_id", [
        "python", "javascript", "typescript", "go", "rust", "java", "csharp"
    ])
    def test_major_languages_have_linters(self, lang_id):
        """Verify major languages have linter configurations."""
        config = ALL_LANGUAGES[lang_id]
        assert "linters" in config, f"{lang_id} missing linters"
        assert len(config["linters"]) > 0, f"{lang_id} has no linters"

    @pytest.mark.parametrize("lang_id", [
        "python", "javascript", "typescript", "go", "rust", "java", "csharp"
    ])
    def test_major_languages_have_formatters(self, lang_id):
        """Verify major languages have formatter configurations."""
        config = ALL_LANGUAGES[lang_id]
        assert "formatters" in config, f"{lang_id} missing formatters"
        assert len(config["formatters"]) > 0, f"{lang_id} has no formatters"

    @pytest.mark.parametrize("lang_id", [
        "python", "javascript", "typescript", "go", "rust", "java", "csharp"
    ])
    def test_major_languages_have_test_frameworks(self, lang_id):
        """Verify major languages have test framework configurations."""
        config = ALL_LANGUAGES[lang_id]
        assert "test_frameworks" in config, f"{lang_id} missing test_frameworks"
        assert len(config["test_frameworks"]) > 0, f"{lang_id} has no test frameworks"

    @pytest.mark.parametrize("lang_id", [
        "python", "javascript", "typescript", "go", "rust", "java", "csharp"
    ])
    def test_major_languages_have_ci_workflow(self, lang_id):
        """Verify major languages have CI workflow configurations."""
        config = ALL_LANGUAGES[lang_id]
        assert "ci_workflow" in config, f"{lang_id} missing ci_workflow"
        workflow = config["ci_workflow"]
        assert "setup_steps" in workflow, f"{lang_id} ci_workflow missing setup_steps"
        assert "test_steps" in workflow, f"{lang_id} ci_workflow missing test_steps"


class TestUtilityFunctions:
    """Tests for utility functions."""

    def test_get_language_valid(self):
        """Test getting a valid language configuration."""
        config = get_language("python")
        assert config["name"] == "Python"

    def test_get_language_invalid(self):
        """Test getting an invalid language raises error."""
        with pytest.raises(ValueError, match="Unknown language"):
            get_language("nonexistent")

    def test_get_languages_by_extension_py(self):
        """Test finding languages by .py extension."""
        langs = get_languages_by_extension("py")
        assert "python" in langs

    def test_get_languages_by_extension_with_dot(self):
        """Test finding languages with leading dot."""
        langs = get_languages_by_extension(".py")
        assert "python" in langs

    def test_get_languages_by_extension_js(self):
        """Test finding languages by .js extension."""
        langs = get_languages_by_extension("js")
        assert "javascript" in langs

    def test_get_all_extensions(self):
        """Test getting all extensions mapping."""
        extensions = get_all_extensions()
        assert "py" in extensions
        assert "js" in extensions
        assert "ts" in extensions
        assert "go" in extensions
        assert "rs" in extensions

    def test_get_tools_for_language(self):
        """Test getting tools for a language."""
        tools = get_tools_for_language("python")
        assert "linters" in tools
        assert "formatters" in tools
        assert "test_frameworks" in tools
        assert "package_managers" in tools
        assert "build_tools" in tools

    def test_get_precommit_hooks(self):
        """Test getting pre-commit hooks."""
        hooks = get_precommit_hooks("python")
        assert isinstance(hooks, list)

    def test_get_ci_workflow(self):
        """Test getting CI workflow configuration."""
        workflow = get_ci_workflow("python")
        assert isinstance(workflow, dict)
        assert "setup_steps" in workflow

    def test_detect_languages(self):
        """Test detecting languages from file paths."""
        files = [
            "src/main.py",
            "src/utils.py",
            "test/test_main.py",
            "frontend/app.js",
            "frontend/types.ts",
        ]
        counts = detect_languages(files)
        assert counts.get("python", 0) == 3
        assert counts.get("javascript", 0) == 1
        assert counts.get("typescript", 0) == 1

    def test_get_recommended_tools(self):
        """Test getting recommended tools for multiple languages."""
        tools = get_recommended_tools(["python", "javascript"])
        assert "linters" in tools
        assert "formatters" in tools
        assert "test_frameworks" in tools


class TestLanguageModules:
    """Tests for individual language module attributes."""

    @pytest.mark.parametrize("lang_id", list(LANGUAGE_MODULES.keys()))
    def test_module_has_language_id(self, lang_id):
        """Verify each module exports LANGUAGE_ID."""
        module = LANGUAGE_MODULES[lang_id]
        assert hasattr(module, "LANGUAGE_ID")
        assert module.LANGUAGE_ID == lang_id

    @pytest.mark.parametrize("lang_id", list(LANGUAGE_MODULES.keys()))
    def test_module_has_language_dict(self, lang_id):
        """Verify each module exports LANGUAGE dict."""
        module = LANGUAGE_MODULES[lang_id]
        assert hasattr(module, "LANGUAGE")
        assert isinstance(module.LANGUAGE, dict)
