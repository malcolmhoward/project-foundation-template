# core/principles/secrets_detection.py
# Secrets Detection principle (v2.4.0)

"""
Secrets Detection Principle.

Pre-commit hooks that scan for secrets before they enter git history.
Once committed, secrets are nearly impossible to fully remove.

Introduced in v2.4.0.
"""

PRINCIPLE_ID = "secrets-detection"

PRINCIPLE = {
    "name": "Secrets Detection",
    "why": "Accidentally committed secrets are a leading cause of breaches",
    "what": "Pre-commit hooks that scan for API keys, passwords, and tokens before they enter history",
    "risk": "Once secrets are in git history, they're nearly impossible to fully remove",
}

EDUCATION = """
📚 LEARNING: Exposed credentials are consistently among the top causes of breaches.

According to the Verizon Data Breach Investigations Report, stolen/compromised
credentials are involved in a significant portion of breaches each year.
(Reference: https://www.verizon.com/business/resources/reports/dbir/)

Once a secret is committed to git, it's in the history forever - even if you
delete it from the current version. Pre-commit hooks catch secrets BEFORE
they become permanent security risks.

Common patterns detected: API keys, passwords, tokens, private keys, and
database connection strings.
"""
