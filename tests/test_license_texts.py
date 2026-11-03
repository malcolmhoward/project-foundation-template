"""
Tests for the full license texts in generated LICENSE files (#128).

WHAT: A generated LICENSE contains the complete license it names, exactly as published,
      and its "Learn more" link points at the right choosealicense.com page.
WHY: Earlier versions wrote only the short source-file notice for Apache 2.0 and the GPL,
     so the generated LICENSE did not contain the license. Keyword checks ("Apache
     License" appears) passed on the notice, so these tests compare whole texts.
HOW: Pin each stored text by its SHA-256 (recorded with its source in
     core/templates/license_texts.py and docs/sources.md), then check that the
     generated file's body is that text.
"""

import hashlib
import os
import subprocess
import sys
from datetime import date
from pathlib import Path

import pytest

from core.templates.core import generate_license_content
from core.templates.license_texts import LICENSE_SOURCES, LICENSE_TEXTS

HEADER_END = "\n---\n\n"


def _body(content):
    return content.split(HEADER_END, 1)[1]


class TestStoredTexts:
    @pytest.mark.parametrize("option", ["mit", "apache", "gpl"])
    def test_text_matches_its_recorded_hash(self, option):
        digest = hashlib.sha256(LICENSE_TEXTS[option].encode("utf-8")).hexdigest()
        assert digest == LICENSE_SOURCES[option][2]

    def test_every_offered_option_has_a_text(self):
        assert set(LICENSE_TEXTS) == set(LICENSE_SOURCES) == {"mit", "apache", "gpl"}


class TestGeneratedLicense:
    @pytest.mark.parametrize("option", ["apache", "gpl"])
    def test_body_is_the_full_published_text(self, option):
        body = _body(generate_license_content(option, "Example Author"))
        assert body == LICENSE_TEXTS[option]
        assert "TERMS AND CONDITIONS" in body
        assert "END OF TERMS AND CONDITIONS" in body

    def test_mit_body_has_copyright_filled_in(self):
        body = _body(generate_license_content("mit", "Example Author"))
        expected = (
            LICENSE_TEXTS["mit"]
            .replace("[year]", str(date.today().year))
            .replace("[fullname]", "Example Author")
        )
        assert body == expected

    @pytest.mark.parametrize("option,slug", [
        ("mit", "mit"), ("apache", "apache-2.0"), ("gpl", "gpl-3.0"),
    ])
    def test_learn_more_link_uses_choosealicense_slug(self, option, slug):
        content = generate_license_content(option, "Example Author")
        assert f"https://choosealicense.com/licenses/{slug}/" in content

    @pytest.mark.parametrize("option", ["apache", "gpl"])
    def test_header_shows_where_the_copyright_notice_goes(self, option):
        header = generate_license_content(option, "Example Author").split(HEADER_END)[0]
        assert f"{date.today().year}" in header and "Example Author" in header

    def test_unknown_option_falls_back_to_mit(self):
        assert _body(generate_license_content("unknown", "A")).startswith("MIT License")

    def test_generate_foundation_writes_the_full_apache_text(self, tmp_path):
        # The command from #128's reproduction steps, with an isolated home directory
        # (as in test_release_integrity.py) so the usage log isn't written to the real one.
        root = Path(__file__).resolve().parent.parent
        home = tmp_path / "home"
        home.mkdir()
        env = dict(os.environ, PYTHONIOENCODING="utf-8", HOME=str(home), USERPROFILE=str(home))
        result = subprocess.run(
            [sys.executable, str(root / "generate_foundation.py"),
             "--project-name", "Demo", "--author-name", "Example Author",
             "--license", "apache", "--output-dir", str(tmp_path / "out"),
             "--non-interactive", "--accept-terms", "--quiet"],
            capture_output=True, text=True, encoding="utf-8", errors="replace",
            env=env, cwd=root,
        )
        assert result.returncode == 0, result.stderr
        written = (tmp_path / "out" / "LICENSE").read_text(encoding="utf-8")
        assert _body(written) == LICENSE_TEXTS["apache"]
