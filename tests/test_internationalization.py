# tests/test_internationalization.py
# Tests for internationalization configurations (v3.6.0)

"""
Tests for the internationalization module.

Verifies that all locale configurations are properly structured
and contain required fields.
"""

import pytest
import json

from core.internationalization import (
    ALL_LOCALES,
    LOCALE_MODULES,
    WESTERN_EUROPEAN_LOCALES,
    EAST_ASIAN_LOCALES,
    RTL_LOCALES,
    INDIC_LOCALES,
    LTR,
    RTL,
    get_locale,
    is_rtl,
    get_text_direction,
    get_locales_by_region,
    get_locale_metadata,
    get_all_locale_metadata,
    get_date_format,
    get_number_format,
    generate_translation_template,
    get_supported_locales_table,
)


class TestLocaleRegistry:
    """Tests for the locale registry and constants."""

    def test_all_locales_count(self):
        """Verify total number of supported locales."""
        assert len(ALL_LOCALES) == 10

    def test_western_european_locales(self):
        """Verify Western European locales."""
        expected = ["en", "es", "fr", "de", "pt"]
        assert WESTERN_EUROPEAN_LOCALES == expected

    def test_east_asian_locales(self):
        """Verify East Asian locales."""
        expected = ["zh", "ja", "ko"]
        assert EAST_ASIAN_LOCALES == expected

    def test_rtl_locales(self):
        """Verify RTL locales."""
        expected = ["ar"]
        assert RTL_LOCALES == expected

    def test_indic_locales(self):
        """Verify Indic locales."""
        expected = ["hi"]
        assert INDIC_LOCALES == expected

    def test_all_regions_account_for_all_locales(self):
        """Verify all regions combined include all locales."""
        all_regions = (
            WESTERN_EUROPEAN_LOCALES +
            EAST_ASIAN_LOCALES +
            RTL_LOCALES +
            INDIC_LOCALES
        )
        assert set(all_regions) == set(ALL_LOCALES.keys())


class TestLocaleConfiguration:
    """Tests for individual locale configurations."""

    @pytest.mark.parametrize("locale_id", list(ALL_LOCALES.keys()))
    def test_locale_has_required_fields(self, locale_id):
        """Verify each locale has required configuration fields."""
        config = ALL_LOCALES[locale_id]

        assert "id" in config, f"{locale_id} missing 'id'"
        assert "name" in config, f"{locale_id} missing 'name'"
        assert "native_name" in config, f"{locale_id} missing 'native_name'"
        assert "direction" in config, f"{locale_id} missing 'direction'"
        assert "script" in config, f"{locale_id} missing 'script'"

    @pytest.mark.parametrize("locale_id", list(ALL_LOCALES.keys()))
    def test_locale_id_matches_key(self, locale_id):
        """Verify the locale ID in config matches the registry key."""
        config = ALL_LOCALES[locale_id]
        assert config["id"] == locale_id

    @pytest.mark.parametrize("locale_id", list(ALL_LOCALES.keys()))
    def test_locale_has_valid_direction(self, locale_id):
        """Verify each locale has a valid text direction."""
        config = ALL_LOCALES[locale_id]
        assert config["direction"] in [LTR, RTL], f"{locale_id} has invalid direction"

    @pytest.mark.parametrize("locale_id", list(ALL_LOCALES.keys()))
    def test_locale_has_formats(self, locale_id):
        """Verify each locale has format configurations."""
        config = ALL_LOCALES[locale_id]
        assert "formats" in config, f"{locale_id} missing 'formats'"
        assert "date" in config["formats"], f"{locale_id} missing date format"
        assert "number" in config["formats"], f"{locale_id} missing number format"

    @pytest.mark.parametrize("locale_id", list(ALL_LOCALES.keys()))
    def test_locale_has_translations(self, locale_id):
        """Verify each locale has translation configurations."""
        config = ALL_LOCALES[locale_id]
        assert "translations" in config, f"{locale_id} missing 'translations'"
        assert "common" in config["translations"], f"{locale_id} missing common translations"
        assert "governance" in config["translations"], f"{locale_id} missing governance translations"


class TestRTLSupport:
    """Tests for RTL (Right-to-Left) language support."""

    def test_arabic_is_rtl(self):
        """Verify Arabic is correctly identified as RTL."""
        assert is_rtl("ar") is True
        assert get_text_direction("ar") == RTL

    def test_ltr_languages(self):
        """Verify LTR languages are correctly identified."""
        ltr_locales = ["en", "es", "fr", "de", "pt", "zh", "ja", "ko", "hi"]
        for locale_id in ltr_locales:
            assert is_rtl(locale_id) is False
            assert get_text_direction(locale_id) == LTR

    def test_arabic_has_rtl_config(self):
        """Verify Arabic has RTL-specific configuration."""
        config = ALL_LOCALES["ar"]
        assert config["direction"] == RTL
        assert "rtl" in config
        assert config["rtl"]["enabled"] is True


class TestUtilityFunctions:
    """Tests for utility functions."""

    def test_get_locale_valid(self):
        """Test getting a valid locale configuration."""
        config = get_locale("en")
        assert config["name"] == "English"

    def test_get_locale_invalid(self):
        """Test getting an invalid locale raises error."""
        with pytest.raises(ValueError, match="Unknown locale"):
            get_locale("nonexistent")

    def test_get_locales_by_region(self):
        """Test getting locales by region."""
        western = get_locales_by_region("western_european")
        assert "en" in western
        assert "fr" in western

        east_asian = get_locales_by_region("east_asian")
        assert "zh" in east_asian
        assert "ja" in east_asian

    def test_get_locale_metadata(self):
        """Test getting locale metadata."""
        metadata = get_locale_metadata("en")
        assert metadata["id"] == "en"
        assert metadata["name"] == "English"
        assert metadata["native_name"] == "English"
        assert metadata["direction"] == LTR

    def test_get_all_locale_metadata(self):
        """Test getting all locale metadata."""
        all_metadata = get_all_locale_metadata()
        assert len(all_metadata) == 10
        assert all("id" in m for m in all_metadata)

    def test_get_date_format(self):
        """Test getting date format."""
        us_format = get_date_format("en")
        assert "MM" in us_format or "DD" in us_format

        de_format = get_date_format("de")
        assert "." in de_format  # German uses dots

    def test_get_number_format(self):
        """Test getting number format."""
        en_format = get_number_format("en")
        assert en_format["decimal"] == "."
        assert en_format["thousands"] == ","

        de_format = get_number_format("de")
        assert de_format["decimal"] == ","
        assert de_format["thousands"] == "."


class TestTranslationTemplates:
    """Tests for translation template generation."""

    def test_generate_json_template(self):
        """Test generating JSON translation template."""
        template = generate_translation_template("en", format="json")
        parsed = json.loads(template)

        assert "_metadata" in parsed
        assert parsed["_metadata"]["locale"] == "en"
        assert "common" in parsed
        assert "governance" in parsed
        assert "errors" in parsed

    def test_generate_yaml_template(self):
        """Test generating YAML translation template."""
        template = generate_translation_template("en", format="yaml")

        assert "_metadata:" in template
        assert "common:" in template
        assert "governance:" in template

    def test_generate_template_without_metadata(self):
        """Test generating template without metadata."""
        template = generate_translation_template("en", include_metadata=False)
        parsed = json.loads(template)

        assert "_metadata" not in parsed
        assert "common" in parsed

    def test_template_has_translations(self):
        """Test that template includes actual translations for locales with them."""
        template = generate_translation_template("es", format="json")
        parsed = json.loads(template)

        assert parsed["common"]["yes"] == "Sí"
        assert parsed["common"]["no"] == "No"


class TestSupportedLocalesTable:
    """Tests for the supported locales markdown table."""

    def test_table_generation(self):
        """Test generating the supported locales table."""
        table = get_supported_locales_table()

        assert "| Code |" in table
        assert "| en |" in table
        assert "| ar |" in table
        assert "RTL" in table  # Arabic should show RTL
        assert "LTR" in table  # Most should show LTR


class TestLocaleModules:
    """Tests for individual locale module attributes."""

    @pytest.mark.parametrize("locale_id", list(LOCALE_MODULES.keys()))
    def test_module_has_locale_id(self, locale_id):
        """Verify each module exports LOCALE_ID."""
        module = LOCALE_MODULES[locale_id]
        assert hasattr(module, "LOCALE_ID")
        assert module.LOCALE_ID == locale_id

    @pytest.mark.parametrize("locale_id", list(LOCALE_MODULES.keys()))
    def test_module_has_locale_dict(self, locale_id):
        """Verify each module exports LOCALE dict."""
        module = LOCALE_MODULES[locale_id]
        assert hasattr(module, "LOCALE")
        assert isinstance(module.LOCALE, dict)
