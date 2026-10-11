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
SCRIPT_VERSION = "2.8.0-lite"
EXPIRATION_DATE = date(2026, 3, 1)
OFFICIAL_REPO = "https://github.com/malcolmhoward/project-foundation-template"

# Default config file names (searched in order)
CONFIG_FILES = [".foundationrc", ".foundationrc.json", "foundationrc.json"]

# v2.4.0: Secrets patterns for detection
SECRETS_PATTERNS = [
    r"(api[_-]?key|apikey)['\"]?\s*[:=]\s*['\"]?[A-Za-z0-9+/]{20,}",
    r"(secret|token|password|passwd|pwd)['\"]?\s*[:=]\s*['\"]?[A-Za-z0-9+/]{8,}",
    r"(aws[_-]?access[_-]?key[_-]?id|aws[_-]?secret[_-]?access[_-]?key)",
    r"-----BEGIN (RSA |EC |OPENSSH |DSA |SSH2 |)PRIVATE KEY-----",
    r"(ghp|gho|ghs|ghu)_[A-Za-z0-9_]{36,}",  # GitHub tokens
    r"sk-[A-Za-z0-9]{48}",  # OpenAI keys
    r"(mongodb(\+srv)?|postgres(ql)?|mysql|redis)://[^\\s]+",  # Database URLs
    r"eyJ[A-Za-z0-9+/]*\\.eyJ[A-Za-z0-9+/]*\\.[A-Za-z0-9+/_-]*"  # JWT tokens
]


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
