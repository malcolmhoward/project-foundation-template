"""
Release-integrity tests.

WHAT: Regression tests for problems found in the review of the v2.6.0 -> v3.7.0 PR chain (#86).
WHY: Each of these shipped to a release branch unnoticed because no test covered it; two were
     reintroduced silently by stale commits during cascade rebases.
HOW: Every subprocess runs with a temporary home directory, so tests never write to the real
     ~/.project_foundation_logs.

Run with: pytest tests/test_release_integrity.py -v
"""

import json
import os
import re
import subprocess
import sys
from datetime import date, timedelta
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))


def run(script, *args, home):
    """Run a PFT script with an isolated home directory."""
    env = dict(os.environ, PYTHONIOENCODING="utf-8", HOME=str(home), USERPROFILE=str(home))
    return subprocess.run(
        [sys.executable, str(ROOT / script), *args],
        capture_output=True, text=True, encoding="utf-8", errors="replace", env=env,
    )


@pytest.fixture
def home(tmp_path):
    h = tmp_path / "home"
    h.mkdir()
    return h


def generate(out, home, *extra, script="generate_foundation.py"):
    return run(script, "--project-name", "Demo", "--author-name", "Example Author",
               "--non-interactive", "--accept-terms", "--output-dir", str(out), *extra, home=home)


# ---------------------------------------------------------------- advisory expiration (ADR 0003)

class TestAdvisoryExpiration:
    def test_window_covers_latest_release(self):
        """The advisory date must be set relative to a release, about 6 months after it.

        Tied to the newest dated CHANGELOG release rather than to today, so the test does not
        start failing on its own; it fails when a release is dated without moving the date.
        """
        from core.utils import EXPIRATION_DATE
        changelog = (ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
        dates = re.findall(r"^## \[[^\]]+\] - (\d{4}-\d{2}-\d{2})", changelog, re.M)
        latest = max(date.fromisoformat(d) for d in dates)
        assert EXPIRATION_DATE >= latest + timedelta(days=150), (
            f"EXPIRATION_DATE {EXPIRATION_DATE} is less than ~5 months after release {latest}"
        )


# ---------------------------------------------------------------- legacy entry point

class TestLegacyShim:
    def test_is_thin_and_defines_nothing_of_its_own(self):
        src = (ROOT / "setup_foundation_lite.py").read_text(encoding="utf-8")
        assert len(src.splitlines()) < 100, "the shim has grown back into a second generator"
        assert "import generate_foundation" in src
        assert "EXPIRATION_DATE" not in src and "SCRIPT_VERSION" not in src

    def test_reports_the_same_version(self, home):
        legacy = run("setup_foundation_lite.py", "--version", home=home)
        current = run("generate_foundation.py", "--version", home=home)
        assert legacy.returncode == 0, legacy.stderr
        assert legacy.stdout.split()[-1] == current.stdout.split()[-1]

    def test_generates_the_same_files(self, tmp_path, home):
        a, b = tmp_path / "legacy", tmp_path / "current"
        assert generate(a, home, "--preset", "light", script="setup_foundation_lite.py").returncode == 0
        assert generate(b, home, "--preset", "light").returncode == 0
        files = lambda d: sorted(p.relative_to(d).as_posix() for p in d.rglob("*") if p.is_file())
        assert files(a) == files(b)


# ---------------------------------------------------------------- documentation

class TestDocumentedCommands:
    @pytest.mark.parametrize("doc", ["README.md", "MIGRATION.md", "CLAUDE.md", "CONTRIBUTING.md"])
    def test_scripts_named_in_docs_exist(self, doc):
        text = (ROOT / doc).read_text(encoding="utf-8")
        for name in sorted(set(re.findall(r"python3? ([A-Za-z_]\w*\.py)", text))):
            assert (ROOT / name).exists(), f"{doc} runs {name}, which does not exist"


# ---------------------------------------------------------------- generation log

class TestGenerationLog:
    def test_generated_log_passes_strict_validation(self, tmp_path, home):
        from validate_customization import scan_file
        out = tmp_path / "out"
        r = generate(out, home, "--preset", "minimal", "--include-generation-log", "--log-format", "both")
        assert r.returncode == 0, r.stderr
        for name in ("GENERATION_LOG.md", "GENERATION_LOG.json"):
            assert scan_file(out / name) == [], f"{name} trips validate_customization"

    def test_nested_files_recorded_with_their_paths(self, tmp_path, home):
        out = tmp_path / "out"
        r = generate(out, home, "--include-ci", "--include-generation-log", "--log-format", "json")
        assert r.returncode == 0, r.stderr
        recorded = {f["file"] for f in json.loads((out / "GENERATION_LOG.json").read_text(encoding="utf-8"))["files"]}
        assert ".github/workflows/ci.yml" in recorded
        assert "ci.yml" not in recorded

    def test_log_to_md_with_both_formats_appends_existing_json(self, tmp_path, home):
        out = tmp_path / "out"
        out.mkdir()
        (out / "GENERATION_LOG.json").write_text(json.dumps({"version": "1.0", "files": [{"file": "KEEP.md"}]}),
                                                 encoding="utf-8")
        r = generate(out, home, "--preset", "minimal", "--include-generation-log", "--log-format", "both",
                     "--log-to", str(out / "GENERATION_LOG.md"))
        assert r.returncode == 0, r.stderr
        recorded = [f["file"] for f in json.loads((out / "GENERATION_LOG.json").read_text(encoding="utf-8"))["files"]]
        assert "KEEP.md" in recorded and "README.md" in recorded

    def test_json_log_without_files_key_is_extended(self):
        from core.generation_log import generate_log_json
        merged = json.loads(generate_log_json("Demo", [{"file": "README.md"}], '{"version": "1.0"}'))
        assert merged["files"] == [{"file": "README.md"}]

    def test_unreadable_json_log_is_backed_up_not_discarded(self, tmp_path):
        from core.generation_log import write_generation_log
        log = tmp_path / "GENERATION_LOG.json"
        log.write_text("{ not json", encoding="utf-8")
        created, ok = write_generation_log(tmp_path, "Demo", ["README.md"], log_format="json",
                                           log_to=str(log), interactive=False)
        assert ok
        assert (tmp_path / "GENERATION_LOG.json.bak").read_text(encoding="utf-8") == "{ not json"
        assert json.loads(log.read_text(encoding="utf-8"))["files"][0]["file"] == "README.md"


# ---------------------------------------------------------------- presets and catalogue listings

class TestPresetsAndListings:
    def test_enterprise_enables_every_principle(self):
        from core.presets import get_preset
        from core.principles import ALL_PRINCIPLES
        principles = get_preset("enterprise")["principles"]
        assert set(principles) == set(ALL_PRINCIPLES)
        assert len(principles) == len(set(principles))

    @pytest.mark.parametrize("flag,catalogue", [("--list-principles", "ALL_PRINCIPLES"),
                                                ("--list-guides", "ALL_GUIDES")])
    def test_list_commands_show_the_whole_catalogue(self, home, flag, catalogue):
        import core.guides
        import core.principles
        expected = getattr(core.principles, catalogue, None) or getattr(core.guides, catalogue)
        out = run("generate_foundation.py", flag, home=home).stdout
        listed = re.findall(r"^    - ([a-z0-9-]+)", out, re.M)
        assert sorted(listed) == sorted(expected)


# ---------------------------------------------------------------- plugin safety

PLUGIN_TEMPLATE = '''
from core.plugins import PrinciplePlugin


class Example(PrinciplePlugin):
    PRINCIPLE_ID = "{pid}"
    PRINCIPLE = {{
        "name": "Example {pid}",
        "why": "Demonstrates plugin loading in a test",
        "what": "A principle supplied by a test plugin",
        "risk": "None; this exists only for tests",
    }}
    EDUCATION = """
## Example

This education text exists only to exercise plugin loading in tests. It is long enough to
satisfy the validator and says nothing else of interest.
"""
'''


@pytest.fixture
def plugins_state():
    import core.plugins as plugins
    yield plugins
    plugins.discover_plugins(plugin_dirs=[], reload=True)  # leave no plugins loaded for other tests


class TestPluginSafety:
    def test_current_directory_is_not_searched_by_default(self, plugins_state):
        assert Path.cwd() / "plugins" not in plugins_state.get_plugin_dirs()

    def test_plugin_cannot_replace_a_builtin_by_default(self, tmp_path, plugins_state):
        from core.principles import ALL_PRINCIPLES
        (tmp_path / "shadow.py").write_text(PLUGIN_TEMPLATE.format(pid="security"), encoding="utf-8")
        plugins_state.discover_plugins(plugin_dirs=[tmp_path], reload=True)
        assert plugins_state.get_all_principles()["security"] == ALL_PRINCIPLES["security"]

    def test_same_named_plugin_files_do_not_collide(self, tmp_path, plugins_state):
        for sub, pid in (("a", "plugin-one"), ("b", "plugin-two")):
            d = tmp_path / sub
            d.mkdir()
            (d / "team.py").write_text(PLUGIN_TEMPLATE.format(pid=pid), encoding="utf-8")
        before = {k for k in sys.modules if k.startswith("foundation_plugin_team")}
        plugins_state.discover_plugins(plugin_dirs=[tmp_path / "a", tmp_path / "b"], reload=True)
        ids = set(plugins_state.get_all_principles(include_builtin=False))
        assert {"plugin-one", "plugin-two"} <= ids
        # Each file must get its own module entry; a shared name means the second replaced the first.
        added = {k for k in sys.modules if k.startswith("foundation_plugin_team")} - before
        assert len(added) == 2, f"plugin modules collided: {sorted(added)}"
