# core/principles/secrets_detection.py
# Secrets Detection principle (v2.4.0)

"""
Secrets Detection Principle.

Pre-commit hooks that scan for secrets before they enter git history.
Once committed, secrets are hard to remove from history.

Introduced in v2.4.0.
"""

PRINCIPLE_ID = "secrets-detection"

PRINCIPLE = {
    "name": "Secrets Detection",
    "why": "Accidentally committed secrets can lead to breaches",
    "what": "Pre-commit hooks that scan for API keys, passwords, and tokens before they enter history",
    "risk": "Once secrets are in git history, they are hard to remove and must be revoked or rotated",
}

EDUCATION = """
📚 LEARNING: Stolen credentials are one of the ways attackers get in.

In the 2026 Verizon Data Breach Investigations Report, credential abuse was
the initial access vector in 13% of the breaches in its dataset where that
vector was known, second to the exploitation of vulnerabilities (31%).
(Reference: https://www.verizon.com/business/resources/reports/dbir/)

Once a secret is committed to git, it stays in the history even if you
delete it from the current version. Removing it means rewriting history, so
GitHub advises revoking or rotating the secret first.
(Reference: https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository)
Pre-commit hooks catch secrets BEFORE they are committed.

Common patterns detected: API keys, passwords, tokens, private keys, and
database connection strings.
"""
