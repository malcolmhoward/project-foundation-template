# foundation/templates/advanced.py
# Advanced template generators: Enhanced security, secrets detection, ADR

"""
Advanced templates for Project Foundation Template.

Contains template generators for:
    - Enhanced SECURITY.md (comprehensive)
    - Pre-commit configuration with secrets detection
    - Architecture Decision Records (ADR)
    - Ethics notice
"""

from datetime import date, datetime
from typing import List
from core.utils import SCRIPT_VERSION, OFFICIAL_REPO, SECRET_DETECTORS


def _secrets_management_section(include_secrets_detection: bool) -> str:
    """Describe secrets protection, claiming detection only when the hook is generated."""
    if not include_secrets_detection:
        return """## Secrets Management

[REPLACE: Describe how this project keeps secrets out of the repository, for example a
pre-commit secrets scanner and a secrets manager for production credentials.]"""

    detected = "\n".join(f"- {description}" for description, _ in SECRET_DETECTORS)
    return f"""## Secrets Management

This project uses a pre-commit hook (`.hooks/detect-secrets.sh`) to catch common secrets
before they are committed.

### What the Hook Detects

The hook matches these patterns in staged files:
{detected}

Pattern matching catches common formats only. It does not find every secret, and it can flag
harmless lines. It checks staged files only, so it does not scan files already committed, and
it skips lines containing the word REPLACE (template placeholders). For stronger protection,
add a dedicated scanner such as
[gitleaks](https://github.com/gitleaks/gitleaks) or
[detect-secrets](https://github.com/Yelp/detect-secrets)."""


def generate_enhanced_security_content(project_name: str, include_secrets_detection: bool = False) -> str:
    """Generate comprehensive SECURITY.md with vulnerability reporting process.

    The Secrets Management section claims automatic detection only when the secrets hook
    is generated too (include_secrets_detection).
    """
    author_email = f"security@{project_name.lower().replace(' ', '-')}.example.com"
    today = date.today().isoformat()

    return f"""# Security Policy

<!--
TEMPLATE NOTICE: This is a comprehensive security policy template.
You MUST customize the email addresses, response times, and supported versions.
A security policy without actual processes behind it creates false confidence.
-->

## Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| Latest  | Yes                |
| Previous| Limited            |
| Older   | No                 |

[REPLACE: Update this table with your actual version support policy]

## Reporting a Vulnerability

We take security vulnerabilities seriously. If you discover a security vulnerability,
please report it responsibly.

### How to Report

**Email**: [REPLACE: {author_email}]

**Do NOT**:
- Open a public GitHub issue for security vulnerabilities
- Disclose the vulnerability publicly before it's fixed
- Exploit the vulnerability beyond proof of concept

### What to Include in Your Report

- **Description**: Clear description of the vulnerability
- **Impact**: What an attacker could achieve
- **Steps to Reproduce**: Detailed steps to reproduce the issue
- **Proof of Concept**: If possible, include a minimal example
- **Suggested Fix**: If you have ideas for fixing it

### What to Expect

| Stage | Timeline |
|-------|----------|
| Initial Response | Within 72 hours |
| Assessment | Within 1 week |
| Status Updates | Every 5 business days |
| Resolution | Depends on severity |

[REPLACE: Adjust these timelines to match your capacity]

## Security Best Practices

### For Users

- Keep your dependencies updated
- Use the latest supported version
- Report suspicious behavior immediately
- Follow the principle of least privilege

### For Contributors

- Never commit secrets (API keys, passwords, tokens)
- Use environment variables for sensitive configuration
- Review dependencies before adding them
- Follow secure coding guidelines

{_secrets_management_section(include_secrets_detection)}

### If You Accidentally Commit a Secret

1. **Rotate immediately**: Change the exposed credential
2. **Don't just delete**: Secrets remain in git history
3. **Consider git-filter-repo**: For complete removal (complex)
4. **Notify security team**: If it's a production credential

## Security Contacts

- **Security Issues**: [REPLACE: {author_email}]
- **General Questions**: [REPLACE: Add general contact]

## Acknowledgments

We appreciate responsible disclosure and may acknowledge security researchers
who help improve our security (with their permission).

---

*Last updated: {today}*
*Generated with [Project Foundation Template]({OFFICIAL_REPO}) - MUST BE CUSTOMIZED*
"""


def generate_pre_commit_config_content() -> str:
    """Generate pre-commit configuration with secrets detection."""
    return """# Pre-commit hooks configuration
# See https://pre-commit.com for more information
# Run: pip install pre-commit && pre-commit install

repos:
  # Secrets detection
  - repo: local
    hooks:
      - id: secrets-detection
        name: Detect secrets
        entry: .hooks/detect-secrets.sh
        language: script
        types: [text]
        pass_filenames: false

  # Basic file checks
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.5.0
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
      - id: check-yaml
      - id: check-json
      - id: check-added-large-files
        args: ['--maxkb=1000']
      - id: check-merge-conflict
      - id: detect-private-key

# To install: pre-commit install
# To run manually: pre-commit run --all-files
"""


_DETECT_SECRETS_HEAD = r"""#!/bin/bash
# Secrets detection pre-commit hook
# Generated by Project Foundation Template v__VERSION__
#
# Scans the staged version of each staged file for common secret formats.
# Pattern matching catches common formats only; see the Secrets Management
# section of SECURITY.md.

set -u

# Colours only when writing to a terminal
if [ -t 1 ]; then
    RED=$'\033[0;31m'; GREEN=$'\033[0;32m'; YELLOW=$'\033[1;33m'; NC=$'\033[0m'
else
    RED=''; GREEN=''; YELLOW=''; NC=''
fi

PATTERNS=$(mktemp)
STAGED=$(mktemp)
LIST=$(mktemp)
trap 'rm -f "$PATTERNS" "$STAGED" "$LIST"' EXIT

# One extended regular expression per line, matched case-insensitively.
# To add a pattern, add a line; to stop checking one, delete its line.
cat > "$PATTERNS" <<'END_PATTERNS'
"""

_DETECT_SECRETS_TAIL = r"""END_PATTERNS

# This file lists the patterns, so it is not scanned itself.
SELF=".hooks/detect-secrets.sh"

printf '%s\n' "${YELLOW}[secrets-detection] Scanning staged files for potential secrets...${NC}"

# Added, copied, modified, renamed and type-changed files; -z keeps file names with
# spaces or other special characters intact
if ! git diff --cached --name-only -z --diff-filter=ACMRT > "$LIST"; then
    printf '%s\n' "${RED}Could not list staged files; is this a git repository?${NC}"
    exit 1
fi

# This hook reads only staged files, so `pre-commit run --all-files` with nothing
# staged checks nothing; say so rather than reporting that no secrets were found.
if [ ! -s "$LIST" ]; then
    printf '%s\n' "${YELLOW}No staged files to scan.${NC}"
    exit 0
fi

SECRETS_FOUND=0

while IFS= read -r -d '' file; do
    if [ "$file" = "$SELF" ]; then
        continue
    fi

    # Scan what will be committed, not the working copy
    git show ":$file" > "$STAGED" 2>/dev/null || continue

    # -I skips binary files; lines containing REPLACE are template placeholders
    matches=$(grep -n -I -i -E -f "$PATTERNS" "$STAGED" | grep -v "REPLACE" | head -5)
    if [ -n "$matches" ]; then
        printf '%s\n' "${RED}Potential secret in ${file}:${NC}" "$matches"
        SECRETS_FOUND=1
    fi
done < "$LIST"

if [ "$SECRETS_FOUND" -eq 1 ]; then
    printf '%s\n' "" \
        "${RED}Potential secrets detected! Please review before committing.${NC}" \
        "${YELLOW}Tips:${NC}" \
        "  - Use environment variables instead of hardcoded values" \
        "  - Add sensitive files to .gitignore" \
        "  - Use a secrets manager for production credentials" \
        "" \
        "To bypass (NOT RECOMMENDED): git commit --no-verify"
    exit 1
fi

printf '%s\n' "${GREEN}No secrets detected${NC}"
exit 0
"""


def generate_detect_secrets_script() -> str:
    """Generate the secrets detection bash script.

    The patterns come from SECRET_DETECTORS, the same list the generated SECURITY.md
    describes. The script needs bash 3.2 or later (the default on macOS).
    """
    patterns = "\n".join(pattern for _, pattern in SECRET_DETECTORS)
    head = _DETECT_SECRETS_HEAD.replace("__VERSION__", SCRIPT_VERSION)
    return head + patterns + "\n" + _DETECT_SECRETS_TAIL


def generate_adr_readme_content(project_name: str) -> str:
    """Generate ADR README/Index."""
    today = date.today().isoformat()

    return f"""# Architecture Decision Records

This directory contains Architecture Decision Records (ADRs) for {project_name}.

## What is an ADR?

An Architecture Decision Record captures an important architectural decision made along with its context and consequences. ADRs help teams:

- Understand why past decisions were made
- Onboard new team members effectively
- Revisit decisions when circumstances change
- Document trade-offs and alternatives considered

## Process

1. Copy `template.md` to create a new ADR
2. Name it `NNNN-short-title.md` (e.g., `0002-use-postgresql.md`)
3. Fill in the template with context, decision, and consequences
4. Submit via pull request
5. Discuss and refine with the team
6. Merge when consensus is reached

## Index

| ADR | Title | Status | Date |
|-----|-------|--------|------|
| [0001](0001-record-architecture-decisions.md) | Record Architecture Decisions | Accepted | {today} |

## Status Types

- **Proposed** - Under discussion
- **Accepted** - Approved and implemented
- **Rejected** - Not approved (keep for context)
- **Deprecated** - No longer relevant
- **Superseded** - Replaced by another ADR

## References

- [Documenting Architecture Decisions](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions) - Michael Nygard
- [ADR GitHub Organization](https://adr.github.io/)

---

*Generated with [Project Foundation Template]({OFFICIAL_REPO})*
"""


def generate_adr_template_content() -> str:
    """Generate ADR template."""
    return """# ADR-NNNN: [Short Title]

**Date**: YYYY-MM-DD

**Status**: [Proposed | Accepted | Rejected | Deprecated | Superseded by ADR-XXXX]

## Context

What is the issue motivating this decision? Describe the forces at play:
- Technical constraints
- Business requirements
- Team capabilities
- Time pressures

## Decision

What is the change we're proposing or have agreed to implement?

Be specific and actionable. This is the core of the ADR.

## Consequences

### Positive
- [What becomes easier?]
- [What improves?]

### Negative
- [What becomes harder?]
- [What trade-offs are we accepting?]

### Neutral
- [What changes but isn't clearly better or worse?]

## Options Considered

### Option 1: [Name]
- **Pros**: ...
- **Cons**: ...

### Option 2: [Name]
- **Pros**: ...
- **Cons**: ...

## References

- [Link to relevant documentation]
- [Link to related ADRs]

## History

- YYYY-MM-DD: Initial draft
"""


def generate_first_adr_content() -> str:
    """Generate the first ADR about recording architecture decisions."""
    today = date.today().isoformat()

    return f"""# ADR-0001: Record Architecture Decisions

**Date**: {today}

**Status**: Accepted

## Context

We need to record architectural decisions made on this project so that:

- Future team members understand why decisions were made
- We can revisit decisions when circumstances change
- Knowledge isn't lost when people leave the team
- We learn from past decisions (both good and bad)

## Decision

We will use Architecture Decision Records (ADRs), as described by Michael Nygard, stored in `docs/adr/`.

Each ADR will:
1. Be numbered sequentially (0001, 0002, etc.)
2. Be written in Markdown
3. Follow our standard template
4. Be reviewed via pull request
5. Include a History section for updates

## Consequences

### Positive
- Architectural decisions are documented and discoverable
- New team members can understand historical context
- Decision-making process becomes transparent

### Negative
- Requires discipline to maintain
- Adds overhead to decision-making process

### Neutral
- Team needs to learn the ADR process
- Templates need periodic updates

## References

- [Documenting Architecture Decisions](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions) - Michael Nygard
- [ADR Tools](https://github.com/npryce/adr-tools)

## History

- {today}: Initial ADR created and accepted

---

*Generated with [Project Foundation Template]({OFFICIAL_REPO})*
"""


def generate_ethics_notice_content(generated_files: List[str]) -> str:
    """Generate ethics notice file content."""
    files_list = "\n".join(f"- {f}" for f in generated_files)

    return f"""# ETHICAL USE NOTICE

This project foundation was generated on {datetime.now().isoformat()}.

The following templates were created:
{files_list}

## Critical Reminders:

1. **These are TEMPLATES** - They must be customized
2. **This is NOT legal advice** - Consult professionals for compliance
3. **This is NOT security consultation** - Implement actual security measures
4. **Templates != Implementation** - You must actually follow these practices
5. **Your responsibility** - You are liable for how you use these templates

## Why These Notices Matter

Every year, companies face penalties for:
- Claiming false compliance (fraud)
- Inadequate security practices (negligence)
- Toxic project cultures (liability)
- Misleading documentation (misrepresentation)

Don't be a statistic. Use these templates as education and starting points,
not as final solutions.

## Next Steps

1. Customize every template for your specific needs
2. Review with appropriate professionals
3. Implement the actual practices
4. Keep them updated
5. Keep learning

---

Generated with Project Foundation Generator {SCRIPT_VERSION}
Learn more: {OFFICIAL_REPO}
"""
