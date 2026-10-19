"""
Tests for the compliance disclaimer (#100) and translation status marking (#112).

WHAT: The "not legal advice, not compliance" statement appears wherever PFT presents
      compliance content, and every locale says how far its translations can be trusted.
WHY: Both are mitigations named in PFT's ethical reviews that did not exist: compliance
     templates could be taken for compliance, and unreviewed translations could mislead
     the people they are meant to help.
HOW: Check the guide, the principle, the preset listing and the locale API directly.
"""

import json
import os
import subprocess
import sys
from pathlib import Path

import pytest

from core.utils import COMPLIANCE_DISCLAIMER
from core.internationalization import (
    ALL_LOCALES,
    TRANSLATION_STATUSES,
    generate_translation_template,
    get_locale_metadata,
    get_supported_locales_table,
    get_translation_status,
    TRANSLATION_ORIGINS,
)

ROOT = Path(__file__).resolve().parent.parent


class TestComplianceDisclaimer:
    def test_disclaimer_says_what_it_must(self):
        assert "Not legal advice" in COMPLIANCE_DISCLAIMER
        assert "does not make a project compliant" in COMPLIANCE_DISCLAIMER

    def test_compliance_guide_opens_with_it(self):
        from core.guides import get_guide_content
        content = get_guide_content("compliance-guide")
        assert COMPLIANCE_DISCLAIMER in content
        assert content.index(COMPLIANCE_DISCLAIMER) < content.index("## Common Compliance Frameworks")

    def test_compliance_principle_education_includes_it(self):
        from core.principles import get_education
        assert COMPLIANCE_DISCLAIMER in get_education("compliance-policy")

    def test_enterprise_preset_listing_shows_it(self, tmp_path):
        env = dict(os.environ, PYTHONIOENCODING="utf-8", HOME=str(tmp_path), USERPROFILE=str(tmp_path))
        r = subprocess.run([sys.executable, str(ROOT / "generate_foundation.py"), "--list-presets"],
                           capture_output=True, text=True, encoding="utf-8", errors="replace", env=env)
        assert r.returncode == 0, r.stderr
        enterprise = r.stdout.split("ENTERPRISE", 1)[1]
        assert "Regulated industries" in enterprise
        assert "Not legal advice" in enterprise


class TestTranslationStatus:
    @pytest.mark.parametrize("locale_id", sorted(ALL_LOCALES))
    def test_every_locale_has_a_known_status(self, locale_id):
        assert get_translation_status(locale_id)["status"] in TRANSLATION_STATUSES

    def test_english_is_the_source_and_nothing_is_claimed_reviewed(self):
        """No locale may claim a review that is not recorded."""
        assert get_translation_status("en")["status"] == "source"
        for locale_id in ALL_LOCALES:
            status = get_translation_status(locale_id)
            if status["status"] == "reviewed":
                assert status["reviewed_by"] and status["reviewed_on"]

    @pytest.mark.parametrize("status", ["reviewed", "ai-reviewed"])
    def test_a_review_needs_a_reviewer_and_a_date(self, monkeypatch, status):
        locale = dict(ALL_LOCALES["es"], translation_status=status)
        monkeypatch.setitem(ALL_LOCALES, "es", locale)
        with pytest.raises(ValueError, match="reviewed_by"):
            get_translation_status("es")
        locale.update(reviewed_by="@example", reviewed_on="2026-10-18")
        assert get_translation_status("es")["reviewed_by"] == "@example"

    def test_every_locale_records_its_origin(self):
        """English is the source; the other nine were drafted with an AI model (#85)."""
        assert get_translation_status("en")["origin"] == "source"
        for locale_id in ALL_LOCALES:
            if locale_id != "en":
                record = get_translation_status(locale_id)
                assert record["origin"] == "ai-generated"
                assert "Claude Opus 4.5" in record["origin_description"]

    def test_unknown_origin_is_rejected(self, monkeypatch):
        monkeypatch.setitem(ALL_LOCALES, "es", dict(ALL_LOCALES["es"], translation_origin="unknown"))
        with pytest.raises(ValueError, match="unknown translation origin"):
            get_translation_status("es")

    def test_unknown_status_is_rejected(self, monkeypatch):
        monkeypatch.setitem(ALL_LOCALES, "es", dict(ALL_LOCALES["es"], translation_status="machine"))
        with pytest.raises(ValueError, match="unknown translation status"):
            get_translation_status("es")

    def test_status_travels_with_generated_templates(self):
        metadata = json.loads(generate_translation_template("es"))["_metadata"]
        assert metadata["translation_status"]["status"] == "unreviewed"
        assert metadata["translation_status"]["origin"] == "ai-generated"
        assert "fluent speaker" in metadata["translation_status"]["description"]
        assert "CONTRIBUTING.md" in metadata["translation_status"]["description"]

    def test_status_is_in_metadata_and_the_locales_table(self):
        assert get_locale_metadata("ja")["translation_status"] == "unreviewed"
        assert get_locale_metadata("ja")["translation_origin"] == "ai-generated"
        table = get_supported_locales_table()
        assert "| Translations | Origin |" in table
        assert "| unreviewed | ai-generated |" in table

    def test_contributing_explains_how_to_correct_and_review(self):
        contributing = (ROOT / "CONTRIBUTING.md").read_text(encoding="utf-8")
        section = contributing.split("## Improving Translations", 1)[1].split("\n## ", 1)[0]
        for value in list(TRANSLATION_STATUSES) + list(TRANSLATION_ORIGINS):
            assert f"`{value}`" in section
        assert "reviewed_by" in section and "reviewed_on" in section


def test_status_travels_without_metadata_too():
    """Leaving the metadata out must not drop the warning."""
    parsed = json.loads(generate_translation_template("es", include_metadata=False))
    assert "_metadata" not in parsed
    assert parsed["_translation_status"]["status"] == "unreviewed"
    yaml_text = generate_translation_template("es", format="yaml", include_metadata=False)
    assert "_translation_status" in yaml_text and '"unreviewed"' in yaml_text


def test_contributing_limits_what_an_ai_review_can_claim():
    contributing = (ROOT / "CONTRIBUTING.md").read_text(encoding="utf-8")
    assert "can make a locale `ai-reviewed`, not `reviewed`" in contributing
    assert "use a different model from the one that drafted the translations" in contributing


def test_ethics_scopes_required_review_to_pft_itself():
    """#107: section 6 matches the ecosystem tiers, and names the real usage-logging code."""
    ethics = (ROOT / "ETHICS.md").read_text(encoding="utf-8")
    assert "All features and pull requests require documented ethical review" not in ethics
    assert "Every feature and pull request to PFT itself (Tier 1" in ethics
    assert "`log_usage_locally` in [core/generator.py]" in ethics
