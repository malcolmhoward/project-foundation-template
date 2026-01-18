# foundation/education.py
# Educational content and principles

"""
Education module for Project Foundation Template.

Contains:
    - Governance principles (LITE_PRINCIPLES)
    - Educational content (EDUCATION_CONTENT)
    - Ethical use agreement
"""

# Ethical use agreement that must be acknowledged
ETHICAL_USE_AGREEMENT = """
╔══════════════════════════════════════════════════════════════════════════════╗
║                     ETHICAL USE AGREEMENT - PLEASE READ                       ║
╠══════════════════════════════════════════════════════════════════════════════╣
║                                                                                ║
║  By using this tool, you acknowledge and agree that:                          ║
║                                                                                ║
║  1. This generates TEMPLATES ONLY - not complete solutions                    ║
║  2. Templates MUST be customized for your specific needs                      ║
║  3. This does NOT provide legal or compliance advice                          ║
║  4. This does NOT make your project automatically secure                      ║
║  5. This does NOT constitute professional security consultation               ║
║  6. You will implement these practices, not just generate documents           ║
║  7. You will not misrepresent templates as professional compliance            ║
║  8. You accept full responsibility for how you use these templates            ║
║                                                                                ║
║  Misrepresenting these templates as actual compliance or security             ║
║  certification may constitute fraud and could result in:                      ║
║  - Legal penalties                                                            ║
║  - Data breaches                                                              ║
║  - Loss of user trust                                                         ║
║  - Personal liability                                                         ║
║                                                                                ║
║  This tool exists to democratize best practices and education.                ║
║  Please use it responsibly and ethically.                                     ║
║                                                                                ║
╚══════════════════════════════════════════════════════════════════════════════╝
"""

# Core governance principles for lite version
LITE_PRINCIPLES = {
    "readme": {
        "name": "README Documentation",
        "why": "First impression and guide for users and contributors",
        "what": "Clear project overview with purpose, setup, and usage",
        "risk": "Without it, projects are unapproachable and unused"
    },
    "contributing": {
        "name": "Contribution Guidelines",
        "why": "Enables community collaboration and maintains quality",
        "what": "Clear process for contributions and expectations",
        "risk": "Without it, contributions are chaotic or non-existent"
    },
    "license": {
        "name": "License Selection",
        "why": "Defines legal terms for use and contribution",
        "what": "Clear intellectual property terms",
        "risk": "Without it, legal ambiguity prevents adoption"
    },
    "code-of-conduct": {
        "name": "Code of Conduct",
        "why": "Creates safe, inclusive environment for all",
        "what": "Behavioral expectations and enforcement",
        "risk": "Without it, toxic behavior drives away contributors"
    },
    "security": {
        "name": "Security Basics",
        "why": "Vulnerabilities can harm users and reputation",
        "what": "Basic security practices and reporting process",
        "risk": "Without it, projects become attack vectors"
    },
    # v2.4.0: Enhanced security features
    "enhanced-security": {
        "name": "Enhanced Security Policy",
        "why": "Comprehensive security documentation builds trust and enables responsible disclosure",
        "what": "Detailed SECURITY.md with vulnerability reporting, response timelines, and best practices",
        "risk": "Without clear security processes, vulnerabilities go unreported or are disclosed publicly"
    },
    "secrets-detection": {
        "name": "Secrets Detection",
        "why": "Accidentally committed secrets are a leading cause of breaches",
        "what": "Pre-commit hooks that scan for API keys, passwords, and tokens before they enter history",
        "risk": "Once secrets are in git history, they're nearly impossible to fully remove"
    },
    # v2.5.0: Advanced governance
    "adr": {
        "name": "Architecture Decision Records",
        "why": "Teams forget why decisions were made, leading to repeated debates or reversed progress",
        "what": "Lightweight documents capturing context, decision, and consequences of architectural choices",
        "risk": "Without ADRs, institutional knowledge leaves when team members do"
    },
    "ci-workflow": {
        "name": "CI/CD Workflow",
        "why": "Manual testing is error-prone and inconsistent",
        "what": "GitHub Actions workflow for automated testing, linting, and validation",
        "risk": "Without CI, bugs slip through and code quality degrades over time"
    },
    # v2.3.0: Community governance templates
    "issue-templates": {
        "name": "Issue Templates",
        "why": "Structured bug reports and feature requests save time",
        "what": "Templates that guide users to provide needed information",
        "risk": "Without them, issues lack context and take longer to resolve"
    },
    "pr-template": {
        "name": "Pull Request Template",
        "why": "Consistent PR descriptions improve review quality",
        "what": "Checklist ensuring code quality and documentation",
        "risk": "Without it, PRs are inconsistent and harder to review"
    },
    "changelog": {
        "name": "Changelog",
        "why": "Users need to know what changed between versions",
        "what": "Human-readable history of notable changes",
        "risk": "Without it, users can't assess upgrade impact"
    }
}

# Educational content for each principle
EDUCATION_CONTENT = {
    "readme": """
    📚 LEARNING: The README is your project's front door.

    Studies show that projects with clear READMEs get 5x more contributions.
    A good README answers: What? Why? How? Who? When?

    Without a README, even excellent code goes unused because people
    don't understand what it does or how to use it.
    """,

    "contributing": """
    📚 LEARNING: Contribution guidelines are your quality gateway.

    Clear contribution guidelines reduce review time by 50% and increase
    contribution quality. They set expectations and prevent frustration.

    Without them, you'll spend more time rejecting or fixing contributions
    than it would take to write the guidelines.
    """,

    "license": """
    📚 LEARNING: No license means "all rights reserved" by default.

    Without a license, others legally cannot use, modify, or contribute
    to your project. This is the opposite of what most people intend.

    Choose MIT for maximum freedom, GPL for copyleft, or Apache for
    patent protection. When in doubt, use MIT.
    """,

    "code-of-conduct": """
    📚 LEARNING: Codes of Conduct increase diversity by 40%.

    Research shows that projects with CoCs have more diverse contributors
    and fewer toxic interactions. They're not about policing, but about
    setting positive expectations.

    Without one, you implicitly tolerate behavior that drives people away.
    """,

    "security": """
    📚 LEARNING: 83% of projects have at least one vulnerability.

    Security isn't optional - it's a responsibility to your users.
    Basic practices like dependency scanning and security policies
    can prevent most common vulnerabilities.

    Without security practices, you're one CVE away from headlines.
    """,

    # v2.4.0: Enhanced security features
    "enhanced-security": """
    📚 LEARNING: A clear security policy enables responsible vulnerability disclosure.

    Security researchers need to know how to report issues safely. Without a
    SECURITY.md, they may disclose publicly, report to the wrong channel, or
    not report at all. GitHub recommends security policies for all public repos.
    (Reference: https://docs.github.com/en/code-security/getting-started/adding-a-security-policy-to-your-repository)

    Key elements: Supported versions, reporting process, response timeline, and
    security best practices specific to your project.
    """,

    "secrets-detection": """
    📚 LEARNING: Exposed credentials are consistently among the top causes of breaches.

    According to the Verizon Data Breach Investigations Report, stolen/compromised
    credentials are involved in a significant portion of breaches each year.
    (Reference: https://www.verizon.com/business/resources/reports/dbir/)

    Once a secret is committed to git, it's in the history forever - even if you
    delete it from the current version. Pre-commit hooks catch secrets BEFORE
    they become permanent security risks.

    Common patterns detected: API keys, passwords, tokens, private keys, and
    database connection strings.
    """,

    # v2.5.0: Advanced governance
    "adr": """
    📚 LEARNING: Architecture Decision Records preserve institutional knowledge.

    Michael Nygard introduced ADRs in 2011 as a way to capture the 'why' behind
    architectural decisions. Without them, teams often reverse good decisions
    because they don't understand the original context.
    (Reference: https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions)

    ADRs are lightweight - just markdown files with context, decision, and
    consequences. They're versioned with the code they describe.
    """,

    "ci-workflow": """
    📚 LEARNING: CI/CD catches issues before they reach production.

    Continuous Integration ensures that every change is automatically tested.
    GitHub Actions provides free CI for public repositories and integrates
    directly with pull requests.
    (Reference: https://docs.github.com/en/actions/automating-builds-and-tests)

    A basic CI workflow runs tests, linting, and builds on every PR, giving
    reviewers confidence that the code works.
    """,

    # v2.3.0: Community governance templates
    "issue-templates": """
    📚 LEARNING: Structured issue templates reduce resolution time by 30%.

    When users report bugs without environment info, or request features
    without context, maintainers waste time asking follow-up questions.

    Good templates guide users to provide what you need upfront.
    """,

    "pr-template": """
    📚 LEARNING: Projects with PR templates have 50% fewer back-and-forth reviews.

    A PR checklist reminds contributors to run tests, update docs, and
    describe their changes. It sets quality expectations before review.

    Without it, reviewers must manually check for common oversights.
    """,

    "changelog": """
    📚 LEARNING: 70% of users check changelogs before upgrading.

    A changelog is your project's narrative - it tells users what to
    expect from each version. Keep a Changelog format (keepachangelog.com)
    is the de facto standard.

    Without it, users fear breaking changes and delay upgrades.
    """
}


def get_principle(name: str) -> dict:
    """Get a principle by name."""
    return LITE_PRINCIPLES.get(name, {})


def get_education_content(name: str) -> str:
    """Get educational content for a principle."""
    return EDUCATION_CONTENT.get(name, "")


def format_principle_display(name: str) -> str:
    """Format a principle for display."""
    principle = get_principle(name)
    if not principle:
        return ""

    return f"""
╔══════════════════════════════════════════════════════════════════════════════╗
║  📖 {principle['name']:<70} ║
╠══════════════════════════════════════════════════════════════════════════════╣
║  WHY: {principle['why']:<68} ║
║  WHAT: {principle['what']:<67} ║
║  RISK: {principle['risk']:<67} ║
╚══════════════════════════════════════════════════════════════════════════════╝
"""
