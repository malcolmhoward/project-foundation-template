# core/utils.py
# Utility constants and helper functions

"""
Utility module for Project Foundation Template.

Contains:
    - Version and configuration constants
    - Helper functions used across modules
"""

import sys
from datetime import date
from pathlib import Path

# Version and expiration
SCRIPT_VERSION = "3.7.0"
# Advisory expiration: about 6 months after release (ADR 0003). Update with every release.
EXPIRATION_DATE = date(2027, 4, 1)
OFFICIAL_REPO = "https://github.com/malcolmhoward/project-foundation-template"

# Default config file names (searched in order)
CONFIG_FILES = [".foundationrc", ".foundationrc.json", "foundationrc.json"]

# Secrets the generated pre-commit hook detects, as (what it catches, pattern) pairs.
# The generated SECURITY.md lists the descriptions, so its claims cannot drift from the
# hook. Each pattern must work both as a Python regex and in `grep -iE`: no \s, \d or \b,
# no backslash escapes inside brackets, and no newlines. Matching is case-insensitive, so
# patterns that rely on a fixed prefix (AKIA, sk-) also require a boundary before it.
# The quoted-assignment rule skips values that start with $ or <, such as ${DB_PASSWORD}.
SECRET_DETECTORS = [
    ("Private keys (PEM)", r"-----BEGIN ([A-Z0-9]+ )*PRIVATE KEY-----"),
    ("AWS access key IDs", r"(^|[^A-Za-z0-9])(AKIA|ASIA)[0-9A-Z]{16}([^A-Za-z0-9]|$)"),
    ("AWS secret access keys assigned in code or config",
     r'''aws_?secret_?access_?key["']?[ ]*[:=][ ]*["']?[A-Za-z0-9/+]{40}'''),
    ("Azure storage account keys in connection strings", r"AccountKey=[A-Za-z0-9+/]{40,}"),
    ("Google API keys", r"AIza[0-9A-Za-z_-]{35}"),
    ("Google Cloud service account key files", r'"type":[ ]*"service_account"'),
    ("GitHub tokens", r"(ghp|gho|ghs|ghu|ghr)_[A-Za-z0-9]{36}|github_pat_[A-Za-z0-9_]{22,}"),
    ("OpenAI-style API keys (sk-...)", r"(^|[^A-Za-z0-9_-])sk-[A-Za-z0-9_-]{20,}"),
    ("JSON Web Tokens (JWTs)", r"eyJ[A-Za-z0-9_-]+\.eyJ[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+"),
    ("Database connection strings that include a password",
     r"(mongodb(\+srv)?|postgres(ql)?|mysql|redis|amqp)://[^:/@ ]+:[^@ ]+@"),
    ("Quoted API keys, secrets, tokens and passwords assigned in code or config",
     r'''(api_?key|secret|token|passw(or)?d)["']?[ ]*[:=][ ]*["'][^"' $<][^"' ]{7,}["']'''),
]

# The patterns alone, kept for the public API.
SECRETS_PATTERNS = [pattern for _, pattern in SECRET_DETECTORS]


def configure_windows_utf8():
    """Configure stdout/stderr for UTF-8 on Windows."""
    if sys.platform == 'win32':
        try:
            sys.stdout.reconfigure(encoding='utf-8')
            sys.stderr.reconfigure(encoding='utf-8')
        except AttributeError:
            # Python < 3.7 fallback
            import io
            sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
            sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')


def check_expiration() -> bool:
    """
    Check if the script has expired.

    Returns:
        True if expired, False otherwise
    """
    return date.today() > EXPIRATION_DATE


def get_expiration_warning() -> str:
    """Get the expiration warning message."""
    return f"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                          ⚠️  VERSION EXPIRATION NOTICE                        ║
╠══════════════════════════════════════════════════════════════════════════════╣
║  This version of Project Foundation Template has reached its advisory        ║
║  expiration date ({EXPIRATION_DATE}).                                              ║
║                                                                              ║
║  WHY VERSIONS EXPIRE:                                                        ║
║  - Best practices evolve continuously                                        ║
║  - Security standards change                                                 ║
║  - Old templates may teach outdated patterns                                 ║
║                                                                              ║
║  WHAT TO DO:                                                                 ║
║  1. Check for updates: {OFFICIAL_REPO}     ║
║  2. Review what has changed in governance best practices                     ║
║  3. Consider regenerating your foundation files                              ║
║                                                                              ║
║  You can continue using this version, but please update soon.                ║
╚══════════════════════════════════════════════════════════════════════════════╝
"""
