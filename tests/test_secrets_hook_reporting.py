"""
Tests for what the generated secrets hook reports and skips (#118, items 1 and 2).

WHAT: The hook names the kind of secret and its line numbers without printing the value,
      and ignores only the text of [REPLACE: ...] placeholders.
WHY: Printing the matched line put the secret in terminal history and CI logs, and
     skipping every line containing "REPLACE" let a real secret on such a line through.
HOW: The generated hook runs in a new git repository with one staged file.
"""

import os
import shutil
import subprocess
import sys

import pytest

from core.templates.advanced import generate_detect_secrets_script


def _find_bash():
    """Git's bash, or any bash that is not the WSL launcher (which cannot see Windows temp paths)."""
    if os.environ.get("PFT_TEST_BASH"):  # e.g. /bin/bash on macOS, to test bash 3.2
        return os.environ["PFT_TEST_BASH"]
    bash = shutil.which("bash")
    if bash and sys.platform == "win32" and ("system32" in bash.lower() or "windowsapps" in bash.lower()):
        return None
    return bash


BASH = _find_bash()
pytestmark = pytest.mark.skipif(BASH is None or not shutil.which("git"), reason="needs bash and git")

# Built at run time so this file holds no secret-shaped strings
GITHUB_TOKEN = "gh" + "p_" + "C" * 36
AWS_KEY_ID = "AKIA" + "ABCDEFGHIJKLMNOP"


def _git(repo, *args):
    subprocess.run(["git", "-C", str(repo), *args], capture_output=True, text=True, check=True)


def _scan(tmp_path, content):
    repo = tmp_path / "repo"
    (repo / ".hooks").mkdir(parents=True)
    (repo / ".hooks" / "detect-secrets.sh").write_text(generate_detect_secrets_script(),
                                                       encoding="utf-8", newline="\n")
    (repo / "settings.txt").write_text(content, encoding="utf-8", newline="\n")
    _git(repo, "init", "-q")
    _git(repo, "add", "-A")
    return subprocess.run([BASH, ".hooks/detect-secrets.sh"], cwd=repo, capture_output=True,
                          text=True, encoding="utf-8", errors="replace")


def test_reports_kind_and_line_without_the_value(tmp_path):
    r = _scan(tmp_path, f"first line\n{GITHUB_TOKEN}\n")
    assert r.returncode == 1
    assert "settings.txt" in r.stdout
    assert "GitHub tokens (line 2)" in r.stdout
    assert GITHUB_TOKEN not in r.stdout and GITHUB_TOKEN not in r.stderr


def test_secret_on_a_line_mentioning_replace_is_caught(tmp_path):
    """Only placeholder text is ignored, not the whole line."""
    r = _scan(tmp_path, f"{AWS_KEY_ID} # REPLACE later\n")
    assert r.returncode == 1
    assert "AWS access key IDs (line 1)" in r.stdout


def test_text_inside_a_placeholder_is_ignored(tmp_path):
    r = _scan(tmp_path, f"key: [REPLACE: for example {AWS_KEY_ID}]\n")
    assert r.returncode == 0, r.stdout


PRE_COMMIT = shutil.which("pre-commit")


@pytest.mark.skipif(PRE_COMMIT is None, reason="needs pre-commit")
@pytest.mark.parametrize("staged, expected", [("no secrets here", 0), (GITHUB_TOKEN, 1)])
def test_hook_runs_under_pre_commit(tmp_path, staged, expected):
    """The hook works as the generated config declares it (language: script, pass_filenames: false)."""
    from core.templates.advanced import generate_pre_commit_config_content

    repo = tmp_path / "repo"
    (repo / ".hooks").mkdir(parents=True)
    hook = repo / ".hooks" / "detect-secrets.sh"
    hook.write_text(generate_detect_secrets_script(), encoding="utf-8", newline="\n")
    hook.chmod(0o755)
    # Only the local hook, so no network access is needed to install the other repositories
    local_only = generate_pre_commit_config_content().split("\n  # Basic file checks")[0] + "\n"
    (repo / ".pre-commit-config.yaml").write_text(local_only, encoding="utf-8", newline="\n")
    (repo / "settings.txt").write_text(staged + "\n", encoding="utf-8", newline="\n")
    _git(repo, "init", "-q")
    _git(repo, "add", "-A")
    _git(repo, "update-index", "--chmod=+x", ".hooks/detect-secrets.sh")

    r = subprocess.run([PRE_COMMIT, "run", "secrets-detection"], cwd=repo, capture_output=True,
                       text=True, encoding="utf-8", errors="replace",
                       env=dict(os.environ, PRE_COMMIT_HOME=str(tmp_path / "pre-commit-home")))
    assert r.returncode == expected, r.stdout + r.stderr
    assert GITHUB_TOKEN not in r.stdout


def test_file_that_is_not_utf8_is_still_scanned(tmp_path):
    """BSD sed stops on invalid UTF-8 in a UTF-8 locale; the hook must not then report it clean."""
    repo = tmp_path / "repo"
    (repo / ".hooks").mkdir(parents=True)
    (repo / ".hooks" / "detect-secrets.sh").write_text(generate_detect_secrets_script(),
                                                       encoding="utf-8", newline="\n")
    (repo / "latin1.txt").write_bytes(b"caf\xe9\n" + AWS_KEY_ID.encode() + b"\n")
    _git(repo, "init", "-q")
    _git(repo, "add", "-A")
    r = subprocess.run([BASH, ".hooks/detect-secrets.sh"], cwd=repo, capture_output=True,
                       text=True, encoding="utf-8", errors="replace",
                       env=dict(os.environ, LC_ALL="en_US.UTF-8", LANG="en_US.UTF-8"))
    assert r.returncode == 1
    assert "AWS access key IDs (line 2)" in r.stdout
