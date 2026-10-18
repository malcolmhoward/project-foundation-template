"""
Tests for scripts/bulk-operations/update-github-issues.sh (#106).

WHAT: The script is run against a fake `gh` that records calls instead of editing issues.
WHY: Run as-is, the old script edited issues 1-10 of this repository and stamped
     "Principle Zero: ✅ Passes" on them with no dry run.
HOW: Each test copies the script, optionally fills its placeholders, and checks which
     `gh issue edit` calls were made.
"""

import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
SCRIPT = ROOT / "scripts" / "bulk-operations" / "update-github-issues.sh"


def _find_bash():
    """Git's bash, or any bash that is not the WSL launcher (which cannot see Windows temp paths)."""
    if os.environ.get("PFT_TEST_BASH"):  # e.g. /bin/bash on macOS, to test bash 3.2
        return os.environ["PFT_TEST_BASH"]
    bash = shutil.which("bash")
    if bash and sys.platform == "win32" and ("system32" in bash.lower() or "windowsapps" in bash.lower()):
        return None
    return bash


BASH = _find_bash()
pytestmark = pytest.mark.skipif(BASH is None, reason="needs bash")

FAKE_GH = """#!/bin/bash
echo "$*" >> "$GH_LOG"
if [ "$1 $2" = "issue view" ]; then
    echo "Original body of issue $3"
fi
if [ "$1 $2 $3" = "issue edit ${FAIL_EDIT:-}" ]; then
    exit 1
fi
"""


@pytest.fixture
def env(tmp_path):
    bin_dir = tmp_path / "bin"
    bin_dir.mkdir()
    gh = bin_dir / "gh"
    gh.write_text(FAKE_GH, encoding="utf-8", newline="\n")
    gh.chmod(0o755)
    log = tmp_path / "gh.log"
    log.touch()
    environment = dict(os.environ, GH_LOG=str(log), TMPDIR=str(tmp_path))
    environment["PATH"] = str(bin_dir) + os.pathsep + environment["PATH"]
    return environment, log


def _script(tmp_path, filled, issues=1):
    text = SCRIPT.read_text(encoding="utf-8")
    block = re.search(r'update_issue 1 .*?\n\n', text, re.S).group(0)
    text = text.replace(block, "".join(block.replace("update_issue 1 ", f"update_issue {n} ", 1)
                                       for n in range(1, issues + 1)))
    if filled:
        text = re.sub(r"\[REPLACE: [^\]]*\]", "Reviewed: example result", text)
    copy = tmp_path / "update-github-issues.sh"
    copy.write_text(text, encoding="utf-8", newline="\n")
    return copy


def _run(script, env, *args):
    return subprocess.run([BASH, str(script), *args], capture_output=True, text=True,
                          encoding="utf-8", errors="replace", env=env[0])


def _edits(env):
    return [line for line in env[1].read_text(encoding="utf-8").splitlines() if line.startswith("issue edit")]


def test_repository_must_be_named(tmp_path, env):
    r = _run(_script(tmp_path, filled=True), env)
    assert r.returncode == 2
    assert "--repo" in r.stderr
    assert env[1].read_text(encoding="utf-8") == ""


def test_dry_run_edits_nothing(tmp_path, env):
    r = _run(_script(tmp_path, filled=True), env, "--repo", "example/repo")
    assert r.returncode == 0, r.stdout + r.stderr
    assert _edits(env) == []
    assert "Dry run" in r.stdout


def test_placeholders_block_apply(tmp_path, env):
    """The shipped script cannot edit anything until a reviewer fills in the outcome."""
    r = _run(_script(tmp_path, filled=False), env, "--repo", "example/repo", "--apply")
    assert r.returncode == 1
    assert _edits(env) == []
    assert "[REPLACE:" in r.stdout


def test_apply_edits_the_named_repository(tmp_path, env):
    r = _run(_script(tmp_path, filled=True), env, "--repo", "example/repo", "--apply")
    assert r.returncode == 0, r.stdout + r.stderr
    edits = _edits(env)
    assert len(edits) == 1
    assert edits[0].startswith("issue edit 1 --repo example/repo --body-file ")


def test_no_hard_coded_repository_or_verdict():
    text = SCRIPT.read_text(encoding="utf-8")
    assert "malcolmhoward" not in text
    assert "Passes (risks identified" not in text


def test_a_failed_edit_says_where_it_stopped(tmp_path, env):
    """Edits run one at a time, so a failure part-way must name what was and was not updated."""
    environment = dict(env[0], FAIL_EDIT="2")
    r = subprocess.run([BASH, str(_script(tmp_path, filled=True, issues=3)), "--repo", "example/repo", "--apply"],
                       capture_output=True, text=True, encoding="utf-8", errors="replace", env=environment)
    assert r.returncode == 1
    assert [e.split()[2] for e in _edits(env)] == ["1", "2"]
    assert "Already updated: #1" in r.stderr
    assert "everything from #2 on" in r.stderr


@pytest.mark.parametrize("args", [["--repo"], ["--repo", "--apply"], ["--repo", "no-slash"]])
def test_repository_argument_is_validated(tmp_path, env, args):
    r = _run(_script(tmp_path, filled=True), env, *args)
    assert r.returncode == 2
    assert env[1].read_text(encoding="utf-8") == ""
