"""
Tests for sourced claims in principle, guide and template text (#124).

WHAT: Phrases that usually signal an unsupported claim ("research shows", "leading cause",
      "increases exponentially") do not appear in core/ unless a source is recorded here,
      and specific corrected claims stay corrected.
WHY: PFT teaches governance, so an unsourced claim teaches readers to repeat it. An audit
     found such claims, some of them wrong; this keeps them from coming back. See
     CONTRIBUTING.md, Sources and Claims.
HOW: Scan the Python modules under core/ for the phrases (whitespace is normalised, so a
     phrase split across lines is still found), and check a few corrected passages
     directly. To use one of the phrases with a source, add the file and phrase to
     ALLOWED with the source.
"""

import re
from pathlib import Path

import pytest

from core.guides import get_guide_content
from core.principles.secrets_detection import EDUCATION as SECRETS_EDUCATION

ROOT = Path(__file__).resolve().parent.parent

# Phrases that need a source. "case studies" is a different meaning, so it is excluded.
UNSOURCED_PATTERNS = [
    r"research (?:shows|has shown|indicates|suggests)",
    r"(?<!case )studies (?:show|have shown|indicate|suggest|found)",
    r"proven to",
    r"leading cause",
    r"increases? exponentially",
    r"industry best practices?",
    r"don't be a statistic",
]

# (path relative to the repository, lower-case phrase as matched): the source that supports it.
ALLOWED = {}


def find_unsourced(text, pattern):
    """Return the matches of pattern in text, ignoring line breaks."""
    flat = re.sub(r"\s+", " ", text)
    return [m.group(0).lower() for m in re.finditer(pattern, flat, re.IGNORECASE)]


def _core_modules():
    return sorted(
        p for p in (ROOT / "core").rglob("*.py") if "__pycache__" not in p.parts
    )


class TestUnsourcedPhrases:
    @pytest.mark.parametrize("pattern", UNSOURCED_PATTERNS)
    def test_phrase_absent_or_sourced(self, pattern):
        hits = []
        for path in _core_modules():
            rel = path.relative_to(ROOT).as_posix()
            for phrase in find_unsourced(path.read_text(encoding="utf-8"), pattern):
                if (rel, phrase) not in ALLOWED:
                    hits.append(f"{rel}: {phrase!r}")
        assert not hits, (
            "Unsourced claim phrasing found. Cite a source and add it to ALLOWED, "
            "or reword (CONTRIBUTING.md, Sources and Claims):\n" + "\n".join(hits)
        )

    def test_allowed_entries_name_a_source(self):
        for key, source in ALLOWED.items():
            assert isinstance(source, str) and source.strip(), f"No source for {key}"

    def test_phrase_split_across_lines_is_found(self):
        assert find_unsourced("Research\n    shows that it works.", UNSOURCED_PATTERNS[0])

    def test_case_studies_is_not_flagged(self):
        pattern = UNSOURCED_PATTERNS[1]
        assert not find_unsourced("Two case studies show the approach", pattern)
        assert find_unsourced("Studies show the approach works", pattern)


class TestCorrectedClaims:
    def test_dbir_figure_names_its_edition_and_scope(self):
        # The 2026 DBIR puts credential abuse second (13%) to vulnerability exploitation.
        assert "2026 Verizon Data Breach Investigations Report" in SECRETS_EDUCATION
        assert "13% of the breaches in its dataset where that" in SECRETS_EDUCATION
        assert "top causes" not in SECRETS_EDUCATION

    def test_422_uses_rfc_9110_name(self):
        content = get_guide_content("api-standards")
        assert "422 | Unprocessable Content" in content
        assert "Unprocessable Entity" not in content
        assert "RFC 9110" in content

    def test_cve_steps_do_not_say_update_nvd(self):
        content = get_guide_content("security-disclosure")
        assert "Update** NVD" not in content
        assert "CNA" in content
