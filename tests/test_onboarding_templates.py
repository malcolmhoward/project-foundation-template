"""
Tests for the onboarding templates: GLOSSARY.md, MAINTAINERS.md and SCAFFOLD_MANIFEST.md (#110).

WHAT: The three templates and the --include-glossary, --include-maintainers and
      --include-manifest options that write them.
WHY: They were added in v3.1.0 with no tests.
HOW: Unit tests call the template functions through `core.templates`; end-to-end tests
     run generate_foundation.py with an isolated home directory.
"""

import os
import re
import subprocess
import sys
from pathlib import Path

import pytest

from core.templates import (
    generate_glossary_content,
    generate_maintainers_content,
    generate_scaffold_manifest_content,
)

ROOT = Path(__file__).resolve().parent.parent


def generate(out, home, *flags):
    env = dict(os.environ, PYTHONIOENCODING="utf-8", HOME=str(home), USERPROFILE=str(home))
    return subprocess.run(
        [sys.executable, str(ROOT / "generate_foundation.py"), "--project-name", "Demo",
         "--author-name", "Example Author", "--non-interactive", "--accept-terms", "--quiet",
         "--output-dir", str(out), *flags],
        capture_output=True, text=True, encoding="utf-8", errors="replace", env=env,
    )


@pytest.fixture
def home(tmp_path):
    h = tmp_path / "home"
    h.mkdir()
    return h


class TestGlossaryTemplate:
    def test_has_alphabetical_sections_of_terms(self):
        content = generate_glossary_content()
        assert content.startswith("# Glossary")
        letters = re.findall(r"^## ([A-Z])$", content, re.M)
        assert len(letters) >= 10
        assert letters == sorted(letters)
        assert len(re.findall(r"^### ", content, re.M)) >= 30


class TestMaintainersTemplate:
    def test_names_the_project_and_author(self):
        content = generate_maintainers_content("Demo", "Example Author")
        assert "**Demo**" in content
        assert "| Example Author |" in content

    def test_does_not_guess_a_github_username(self):
        """A handle guessed from the name could belong to someone else."""
        content = generate_maintainers_content("Demo", "Example Author")
        assert "@exampleauthor" not in content.lower()
        assert "[REPLACE: @GitHub username]" in content
        assert "TEMPLATE NOTICE" in content


class TestScaffoldManifestTemplate:
    def test_records_files_principles_and_configuration(self):
        content = generate_scaffold_manifest_content(
            project_name="Demo", version="9.9.9", preset="standard",
            generated_files=["README.md", "LICENSE"], principles_used=["readme", "license"],
            guides_used=[], config={"project_name": "Demo", "license": "mit"},
        )
        assert "| **Project Name** | Demo |" in content
        assert "| **Generator Version** | 9.9.9 |" in content
        assert "- `LICENSE`" in content and "- `README.md`" in content
        assert "- license" in content and "- readme" in content
        assert "| `license` | `mit` |" in content


class TestOnboardingOptions:
    @pytest.mark.parametrize("flag, filename", [
        ("--include-glossary", "GLOSSARY.md"),
        ("--include-maintainers", "MAINTAINERS.md"),
        ("--include-manifest", "SCAFFOLD_MANIFEST.md"),
    ])
    def test_each_option_writes_its_file_only_when_given(self, tmp_path, home, flag, filename):
        with_flag = tmp_path / "with"
        r = generate(with_flag, home, flag)
        assert r.returncode == 0, r.stdout + r.stderr
        assert (with_flag / filename).is_file()

        without = tmp_path / "without"
        assert generate(without, home).returncode == 0
        assert not (without / filename).exists()

    def test_manifest_lists_every_file_the_run_wrote(self, tmp_path, home):
        out = tmp_path / "out"
        assert generate(out, home, "--all").returncode == 0
        manifest = (out / "SCAFFOLD_MANIFEST.md").read_text(encoding="utf-8")
        written = {p.relative_to(out).as_posix() for p in out.rglob("*") if p.is_file()}
        # The manifest is written before the ethics notice, so it cannot list that notice
        for path in sorted(written - {"SCAFFOLD_MANIFEST.md", "FOUNDATION_NOTICE.md"}):
            assert f"- `{path}`" in manifest, path

    def test_maintainers_file_is_flagged_until_customized(self, tmp_path, home):
        out = tmp_path / "out"
        assert generate(out, home, "--include-maintainers").returncode == 0
        env = dict(os.environ, PYTHONIOENCODING="utf-8")
        r = subprocess.run([sys.executable, str(ROOT / "validate_customization.py"), "--verbose", str(out)],
                           capture_output=True, text=True, encoding="utf-8", errors="replace", env=env)
        assert "MAINTAINERS.md" in r.stdout
