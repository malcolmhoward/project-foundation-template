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


# ---------------------------------------------------------------- command-line-only safeguards (#93, #113)

class TestCommandLineOnlySafeguards:
    def test_config_file_cannot_accept_the_agreement(self, tmp_path, home):
        """A .foundationrc that sets accept_terms must not skip the ethical agreement (#93)."""
        out = tmp_path / "out"
        config = tmp_path / "foundationrc.json"
        config.write_text(json.dumps({"project_name": "Demo", "author_name": "Example Author",
                                      "non_interactive": True, "accept_terms": True}), encoding="utf-8")
        r = run("generate_foundation.py", "--config", str(config), "--output-dir", str(out), "--quiet", home=home)
        assert r.returncode == 1
        assert "--accept-terms" in r.stdout + r.stderr
        assert not out.exists() or not any(out.iterdir()), "files were generated without accepting the agreement"

    def test_non_interactive_run_does_not_overwrite_without_force(self, tmp_path, home):
        """Existing files survive a non-interactive rerun unless --force-overwrite is given (#113)."""
        out = tmp_path / "out"
        assert generate(out, home, "--quiet").returncode == 0
        readme = out / "README.md"
        readme.write_text(readme.read_text(encoding="utf-8") + "\nLOCAL-EDIT\n", encoding="utf-8")

        r = generate(out, home, "--quiet")
        assert r.returncode == 1
        assert "--force-overwrite" in r.stdout
        assert "LOCAL-EDIT" in readme.read_text(encoding="utf-8")

        r = generate(out, home, "--quiet", "--force-overwrite")
        assert r.returncode == 0, r.stderr
        assert "LOCAL-EDIT" not in readme.read_text(encoding="utf-8")

    def test_existing_generation_log_alone_does_not_block(self, tmp_path, home):
        """Logs are appended to, so an existing log must not stop a non-interactive run."""
        out = tmp_path / "out"
        out.mkdir()
        (out / "GENERATION_LOG.md").write_text("# Generation Log" + chr(10), encoding="utf-8")
        r = generate(out, home, "--quiet", "--include-generation-log")
        assert r.returncode == 0, r.stdout + r.stderr

    def test_overwrite_check_covers_every_generated_file(self, tmp_path, home):
        """Every file a full run writes, except the appended logs, is checked before overwriting."""
        from core.generator import EXISTING_FILE_CHECKS, EXISTING_DIR_CHECKS
        out = tmp_path / "out"
        assert generate(out, home, "--quiet", "--preset", "enterprise", "--all").returncode == 0
        for path in sorted(p.relative_to(out).as_posix() for p in out.rglob("*") if p.is_file()):
            if path.startswith("GENERATION_LOG"):
                continue
            covered = path in EXISTING_FILE_CHECKS or any(path.startswith(d + "/") for d in EXISTING_DIR_CHECKS)
            assert covered, f"{path} is written but not checked before overwriting"


# ---------------------------------------------------------------- generated security and CI files (#94, #95, #96)

def _find_bash():
    """Git's bash, or any bash that is not the WSL launcher (which cannot see Windows temp paths)."""
    import shutil
    bash = shutil.which("bash")
    if bash and sys.platform == "win32" and ("system32" in bash.lower() or "windowsapps" in bash.lower()):
        return None
    return bash


BASH = _find_bash()
needs_bash = pytest.mark.skipif(BASH is None or not __import__("shutil").which("git"),
                                reason="needs bash and git")

# One sample per detector, built at run time so this file holds no secret-shaped strings
# (hosting providers' push protection scans for them).
SECRET_SAMPLES = {
    "Private keys (PEM)": "-----BEGIN " + "RSA PRIVATE KEY-----",
    "AWS access key IDs": "AKIA" + "ABCDEFGHIJKLMNOP",
    "AWS secret access keys assigned in code or config": 'aws_secret_access_key = "' + "A1b2" * 10 + '"',
    "Azure storage account keys in connection strings":
        "DefaultEndpointsProtocol=https;AccountName=demo;AccountKey=" + "A" * 86 + "==",
    "Google API keys": "AIza" + "B" * 35,
    "Google Cloud service account key files": '{"type": "service_account", "project_id": "demo"}',
    "GitHub tokens": "gh" + "p_" + "C" * 36,
    "OpenAI-style API keys (sk-...)": "s" + "k-" + "D" * 24,
    "JSON Web Tokens (JWTs)": "eyJ" + "hbGciOiJIUzI1NiJ9" + ".eyJ" + "zdWIiOiIxIn0" + ".c2lnbmF0dXJl",
    "Database connection strings that include a password":
        "postgres://" + "app:" + "hunter2pass" + "@db.example.com/app",
    "Quoted API keys, secrets, tokens and passwords assigned in code or config":
        'password = "' + "correct-horse" + '"',
}


def _git(repo, *args):
    return subprocess.run(["git", "-C", str(repo), *args], capture_output=True, text=True, check=True)


def _run_hook(repo):
    return subprocess.run([BASH, ".hooks/detect-secrets.sh"], cwd=repo, capture_output=True,
                          text=True, encoding="utf-8", errors="replace")


@pytest.fixture
def generated_repo(tmp_path, home):
    """A fully generated project in a new git repository, with everything staged."""
    repo = tmp_path / "repo"
    assert generate(repo, home, "--quiet", "--preset", "enterprise", "--all",
                    "--include-generation-log").returncode == 0
    _git(repo, "init", "-q")
    _git(repo, "add", "-A")
    return repo


@pytest.fixture
def hook_repo(tmp_path):
    """A new git repository holding only the generated hook, staged."""
    from core.templates.advanced import generate_detect_secrets_script
    repo = tmp_path / "hook-repo"
    (repo / ".hooks").mkdir(parents=True)
    (repo / ".hooks" / "detect-secrets.sh").write_text(generate_detect_secrets_script(),
                                                       encoding="utf-8", newline="\n")
    _git(repo, "init", "-q")
    _git(repo, "add", "-A")
    return repo


class TestGeneratedSecretsHook:
    def test_every_detector_has_a_sample(self):
        from core.utils import SECRET_DETECTORS
        assert set(SECRET_SAMPLES) == {description for description, _ in SECRET_DETECTORS}

    def test_documented_patterns_match_their_samples(self):
        """Python check of the same patterns the hook uses with grep -iE."""
        from core.utils import SECRET_DETECTORS
        for description, pattern in SECRET_DETECTORS:
            assert re.search(pattern, SECRET_SAMPLES[description], re.IGNORECASE), description

    @needs_bash
    def test_hook_passes_on_freshly_generated_files(self, generated_repo):
        """The hook must not block committing the files PFT just generated, itself included (#94)."""
        r = _run_hook(generated_repo)
        assert r.returncode == 0, r.stdout + r.stderr

    @needs_bash
    @pytest.mark.parametrize("description", sorted(SECRET_SAMPLES))
    def test_hook_detects_each_documented_secret_type(self, hook_repo, description):
        """Every type SECURITY.md lists is caught, in a staged file whose name has a space (#94)."""
        sample = hook_repo / "app config.txt"
        sample.write_text(f"setting\n{SECRET_SAMPLES[description]}\n", encoding="utf-8")
        _git(hook_repo, "add", "app config.txt")
        r = _run_hook(hook_repo)
        assert r.returncode == 1, f"{description} not detected:\n{r.stdout}{r.stderr}"
        assert "app config.txt" in r.stdout

    @needs_bash
    def test_hook_scans_the_staged_version(self, hook_repo):
        """A secret removed from the working copy but still staged is still caught."""
        sample = hook_repo / "settings.txt"
        sample.write_text(SECRET_SAMPLES["GitHub tokens"] + "\n", encoding="utf-8")
        _git(hook_repo, "add", "settings.txt")
        sample.write_text("cleaned\n", encoding="utf-8")
        assert _run_hook(hook_repo).returncode == 1

    @needs_bash
    def test_hook_scans_renamed_files(self, hook_repo):
        """A secret added while renaming a file must not slip through as a rename."""
        original = hook_repo / "notes.txt"
        original.write_text("".join(f"line {i}\n" for i in range(40)), encoding="utf-8")
        _git(hook_repo, "add", "notes.txt")
        _git(hook_repo, "-c", "user.name=Example", "-c", "user.email=user@example.com",
             "commit", "-q", "--no-verify", "-m", "initial")
        _git(hook_repo, "mv", "notes.txt", "renamed.txt")
        with open(hook_repo / "renamed.txt", "a", encoding="utf-8") as f:
            f.write(SECRET_SAMPLES["AWS access key IDs"] + "\n")
        _git(hook_repo, "add", "renamed.txt")
        assert "R" in _git(hook_repo, "diff", "--cached", "--name-status").stdout
        assert _run_hook(hook_repo).returncode == 1

    @needs_bash
    def test_hook_ignores_common_harmless_lines(self, hook_repo):
        """Lines that look like secrets only by accident should not block a commit."""
        (hook_repo / "harmless.txt").write_text("\n".join([
            "See the risk-assessment-framework-overview and disk-usage-monitoring-service docs.",
            '"node_modules/@scope/task-runner-configuration-helper": {',
            "class AsiaPacificRegionalSettings:",
            'password = "${DB_PASSWORD}"',
            'token: "<your token>"',
        ]) + "\n", encoding="utf-8")
        _git(hook_repo, "add", "harmless.txt")
        r = _run_hook(hook_repo)
        assert r.returncode == 0, r.stdout

    @needs_bash
    def test_hook_says_when_nothing_is_staged(self, tmp_path):
        """With nothing staged (e.g. pre-commit run --all-files), it must not claim a clean scan."""
        from core.templates.advanced import generate_detect_secrets_script
        repo = tmp_path / "empty"
        (repo / ".hooks").mkdir(parents=True)
        (repo / ".hooks" / "detect-secrets.sh").write_text(generate_detect_secrets_script(),
                                                           encoding="utf-8", newline="\n")
        _git(repo, "init", "-q")
        r = _run_hook(repo)
        assert r.returncode == 0
        assert "No staged files to scan" in r.stdout and "No secrets detected" not in r.stdout

    @needs_bash
    def test_hook_prints_no_raw_colour_codes(self, hook_repo):
        """Colour codes were printed literally as \\033[...; output that is not a terminal has none."""
        r = _run_hook(hook_repo)
        assert "\\033" not in r.stdout and "\x1b" not in r.stdout


class TestGeneratedSecurityPolicy:
    def test_claims_match_the_hook_when_it_is_generated(self, tmp_path, home):
        from core.utils import SECRET_DETECTORS
        out = tmp_path / "out"
        assert generate(out, home, "--quiet", "--include-enhanced-security",
                        "--include-secrets-detection").returncode == 0
        policy = (out / "SECURITY.md").read_text(encoding="utf-8")
        for description, _ in SECRET_DETECTORS:
            assert f"- {description}" in policy
        assert "Cloud service credentials (AWS, Azure, GCP)" not in policy

    def test_no_detection_claims_without_the_hook(self, tmp_path, home):
        """Enhanced security alone must not say a hook protects the project (#94)."""
        out = tmp_path / "out"
        assert generate(out, home, "--quiet", "--include-enhanced-security").returncode == 0
        assert not (out / ".hooks").exists()
        policy = (out / "SECURITY.md").read_text(encoding="utf-8")
        assert "Secrets Management" in policy
        assert "pre-commit hook" not in policy and "What the Hook Detects" not in policy

    def test_all_writes_security_policy_once(self, tmp_path, home):
        """--all wrote the basic and then the enhanced SECURITY.md to the same path (#95)."""
        out = tmp_path / "out"
        r = generate(out, home, "--all", "--export-json")
        assert r.returncode == 0, r.stderr
        files = json.loads(r.stdout.split("--- JSON OUTPUT ---", 1)[1])["files_generated"]
        assert files.count("SECURITY.md") == 1
        assert len(files) == len(set(files)), "a file was written twice"
        assert "Reporting a Vulnerability" in (out / "SECURITY.md").read_text(encoding="utf-8")


class TestGeneratedCiWorkflow:
    @staticmethod
    def _code_lines():
        from core.templates.github import generate_ci_workflow_content
        return [l for l in generate_ci_workflow_content().splitlines() if not l.lstrip().startswith("#")]

    def test_no_check_can_pass_when_it_fails(self):
        """continue-on-error kept the run green when lint, test or build failed (#96)."""
        assert not [l for l in self._code_lines() if "continue-on-error" in l]

    def test_unconfigured_workflow_fails_and_says_why(self):
        """Until the placeholder step is replaced, the run fails instead of passing with no checks."""
        code = "\n".join(self._code_lines())
        step = code.split("- name: Run checks", 1)[1]
        assert "::error::" in step and "exit 1" in step
        assert "examples are in the comments above the step" in step
        assert "npm" not in code, "a language-specific command runs by default"

    def test_generation_warns_that_ci_fails_until_configured(self, tmp_path, home):
        """The first sign must not be a failing check after the first push, even with --quiet."""
        r = generate(tmp_path / "with-ci", home, "--quiet", "--include-ci")
        assert r.returncode == 0, r.stderr
        assert "ci.yml fails until you replace its 'Run checks' step" in r.stdout

        r = generate(tmp_path / "without-ci", home, "--quiet")
        assert r.returncode == 0, r.stderr
        assert "Run checks" not in r.stdout

    def test_workflow_is_valid_yaml(self):
        yaml = pytest.importorskip("yaml")
        from core.templates.github import generate_ci_workflow_content
        steps = yaml.safe_load(generate_ci_workflow_content())["jobs"]["build"]["steps"]
        assert [s.get("name") for s in steps] == ["Checkout code", "Run checks"]
