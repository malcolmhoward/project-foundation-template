# foundation/templates/governance.py
# Governance template generators: CODE_OF_CONDUCT, SECURITY, CHANGELOG

"""
Governance templates for Project Foundation Template.

Contains template generators for:
    - CODE_OF_CONDUCT.md
    - SECURITY.md (basic)
    - CHANGELOG.md
"""

from datetime import date
from foundation.utils import OFFICIAL_REPO


def generate_code_of_conduct_content() -> str:
    """Generate CODE_OF_CONDUCT.md content."""
    return f"""# Code of Conduct

<!--
TEMPLATE NOTICE: This is the Contributor Covenant v2.0.
Customize enforcement, contact methods, and scope for your project.
A CoC without enforcement is worse than no CoC at all.
-->

## Our Pledge

We pledge to make participation in our community a harassment-free experience for everyone.

## Our Standards

Examples of positive behavior:
* Using welcoming and inclusive language
* Being respectful of differing viewpoints
* Gracefully accepting constructive criticism
* Focusing on what is best for the community
* Showing empathy towards other members

Examples of unacceptable behavior:
* Harassment of any kind
* Discriminatory language or actions
* Publishing others' private information
* Other conduct which could reasonably be considered inappropriate

## Enforcement

[REPLACE: Who enforces this? How do people report violations?]
[CRITICAL: Without enforcement, this document is meaningless]

Contact: [REPLACE: Add actual contact method]

## Template Notice

This Code of Conduct is a TEMPLATE. You must:
1. Set up actual enforcement mechanisms
2. Designate responsible parties
3. Provide real contact methods
4. Train moderators on enforcement
5. Be prepared to actually enforce it

A Code of Conduct without enforcement enables harm by providing false safety.

---

Adapted from Contributor Covenant v2.0
Generated with [Project Foundation Generator]({OFFICIAL_REPO})
"""


def generate_security_content() -> str:
    """Generate basic SECURITY.md content with educational notices."""
    return f"""# Security Policy

<!--
TEMPLATE NOTICE: Security policies require actual processes behind them.
Do not publish this without setting up the mentioned procedures.
-->

## Critical Notice

This is a TEMPLATE security policy. Publishing this without actual security
processes in place creates false confidence and increases risk.

Before using this template:
1. Set up security monitoring
2. Create incident response procedures
3. Designate security contacts
4. Implement the mentioned practices

## Security Practices

[REPLACE: What security measures are actually in place?]

### What We Do (Examples - REPLACE with actual practices):
- Dependency scanning
- Code review
- Security testing
- Incident response

### What We Don't Do (Be honest about limitations):
- 24/7 monitoring
- Penetration testing
- Formal audits

## Reporting Vulnerabilities

[REPLACE: How should security issues be reported?]
[REPLACE: What is your response timeline?]
[REPLACE: Who handles security issues?]

### Do:
- Report security issues privately
- Include reproduction steps
- Allow time for patches

### Don't:
- Publicly disclose unpatched vulnerabilities
- Exploit vulnerabilities beyond POC

## Contact

Security Email: [REPLACE: Add actual security contact]
Response Time: [REPLACE: Set realistic response time]

## Template Warning

Using this template without implementing actual security practices may:
- Create legal liability
- Mislead users about security
- Increase attack surface
- Violate compliance requirements

Security is not documentation - it's action.

---

Generated with [Project Foundation Generator]({OFFICIAL_REPO})
MUST BE CUSTOMIZED before use!
"""


def generate_changelog_content(project_name: str) -> str:
    """Generate CHANGELOG.md following Keep a Changelog format."""
    today = date.today().isoformat()

    return f"""# Changelog

All notable changes to {project_name} will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Initial project setup

### Changed
- (No changes yet)

### Deprecated
- (No deprecations yet)

### Removed
- (No removals yet)

### Fixed
- (No fixes yet)

### Security
- (No security updates yet)

## [0.1.0] - {today}

### Added
- Initial project foundation
- README with project overview
- CONTRIBUTING guidelines
- LICENSE file

---

<!--
How to update this changelog:

1. Add new entries under "Unreleased"
2. When releasing:
   - Change "Unreleased" to version number and date
   - Create new "Unreleased" section above it
3. Use categories: Added, Changed, Deprecated, Removed, Fixed, Security
4. Write for humans, not machines
5. Link to relevant issues/PRs

Example entry:
### Added
- New feature description ([#123](link-to-issue))
-->

*Generated with [Project Foundation Template]({OFFICIAL_REPO})*
"""
