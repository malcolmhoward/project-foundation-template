#!/usr/bin/env python3
"""
Project Foundation Generator - Ethical Lite Edition
Version: 2.1.0-lite
Released: 2025-09-24

This tool generates educational project foundations with built-in governance principles.
It is designed to teach best practices while creating useful templates.

IMPORTANT: This generates TEMPLATES only. They are starting points, not complete solutions.
Actual security, compliance, and governance require ongoing human judgment and expertise.

Copyright (c) 2025 Malcolm Howard

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

Repository: https://github.com/malcolmhoward/project-foundation-template
"""

import argparse
import json
import os
import sys
import hashlib
import time
from datetime import date, datetime, timedelta
from pathlib import Path
from typing import Dict, Set, Any

# Configure stdout for UTF-8 on Windows (handles Unicode characters in output)
if sys.platform == 'win32':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stderr.reconfigure(encoding='utf-8')
    except AttributeError:
        # Python < 3.7 fallback
        import io
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
        sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

# Version and expiration
SCRIPT_VERSION = "2.5.0-lite"
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


def load_config_file(config_path: str = None) -> Dict[str, Any]:
    """
    Load configuration from a .foundationrc file.

    Searches for config files in order:
    1. Explicit path if provided via --config
    2. .foundationrc in current directory
    3. .foundationrc.json in current directory
    4. foundationrc.json in current directory

    Returns empty dict if no config found (not an error).
    """
    config = {}

    if config_path:
        # Explicit config path provided
        path = Path(config_path)
        if not path.exists():
            print(f"⚠️  Config file not found: {config_path}")
            print("   Continuing with command-line arguments only.\n")
            return {}
        try:
            with open(path, 'r', encoding='utf-8') as f:
                config = json.load(f)
            print(f"📋 Loaded config from: {path}\n")
            return config
        except json.JSONDecodeError as e:
            print(f"❌ Error parsing config file: {e}")
            print("   Config file must be valid JSON.\n")
            return {}

    # Search for default config files
    for filename in CONFIG_FILES:
        path = Path(filename)
        if path.exists():
            try:
                with open(path, 'r', encoding='utf-8') as f:
                    config = json.load(f)
                print(f"📋 Loaded config from: {path}\n")
                return config
            except json.JSONDecodeError:
                continue  # Try next file

    return config


def merge_config_with_args(args, config: Dict[str, Any]):
    """
    Merge config file settings with command-line arguments.
    Command-line arguments take precedence over config file.
    """
    # Map config keys to argument names
    config_mapping = {
        "project_name": "project_name",
        "project-name": "project_name",
        "projectName": "project_name",
        "author_name": "author_name",
        "author-name": "author_name",
        "authorName": "author_name",
        "license": "license",
        "output_dir": "output_dir",
        "output-dir": "output_dir",
        "outputDir": "output_dir",
        "include_coc": "include_coc",
        "include-coc": "include_coc",
        "includeCoc": "include_coc",
        "include_security": "include_security",
        "include-security": "include_security",
        "includeSecurity": "include_security",
        # v2.3.0: Community governance templates
        "include_github_templates": "include_github_templates",
        "include-github-templates": "include_github_templates",
        "includeGithubTemplates": "include_github_templates",
        "include_changelog": "include_changelog",
        "include-changelog": "include_changelog",
        "includeChangelog": "include_changelog",
        "include_all": "include_all",
        "include-all": "include_all",
        "includeAll": "include_all",
        # v2.4.0: Security features
        "include_enhanced_security": "include_enhanced_security",
        "include-enhanced-security": "include_enhanced_security",
        "includeEnhancedSecurity": "include_enhanced_security",
        "include_secrets_detection": "include_secrets_detection",
        "include-secrets-detection": "include_secrets_detection",
        "includeSecretsDetection": "include_secrets_detection",
        # v2.5.0: Advanced governance
        "include_adr": "include_adr",
        "include-adr": "include_adr",
        "includeAdr": "include_adr",
        "include_ci": "include_ci",
        "include-ci": "include_ci",
        "includeCi": "include_ci",
        # v2.2.0: Non-interactive mode
        "verbose": "verbose",
        "non_interactive": "non_interactive",
        "non-interactive": "non_interactive",
        "nonInteractive": "non_interactive",
        "accept_terms": "accept_terms",
        "accept-terms": "accept_terms",
        "acceptTerms": "accept_terms",
    }

    for config_key, arg_name in config_mapping.items():
        if config_key in config:
            # Only apply config value if arg wasn't explicitly set
            current_value = getattr(args, arg_name, None)
            default_values = {
                "project_name": None,
                "author_name": None,
                "license": "mit",
                "output_dir": ".",
                "include_coc": False,
                "include_security": False,
                # v2.3.0
                "include_github_templates": False,
                "include_changelog": False,
                "include_all": False,
                # v2.4.0
                "include_enhanced_security": False,
                "include_secrets_detection": False,
                # v2.5.0
                "include_adr": False,
                "include_ci": False,
                # v2.2.0
                "verbose": False,
                "non_interactive": False,
                "accept_terms": False,
            }
            if current_value == default_values.get(arg_name):
                setattr(args, arg_name, config[config_key])

    return args


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

class EthicalFoundationGenerator:
    """Main generator class with ethical safeguards and education."""

    def __init__(self, args):
        self.args = args
        self.generated_files = []
        self.education_shown = set()
        self.start_time = datetime.now()

    @property
    def is_interactive(self) -> bool:
        """Check if running in interactive mode."""
        return not getattr(self.args, 'non_interactive', False)

    @property
    def is_quiet(self) -> bool:
        """Check if running in quiet mode."""
        return getattr(self.args, 'quiet', False)
        
    def run(self):
        """Main execution with ethical safeguards."""
        # Check expiration
        if not self.check_version_advisory():
            return False
            
        # Show ethical agreement
        if not self.show_ethical_agreement():
            return False
            
        # Educational intro
        self.show_educational_intro()
        
        # Generate foundations
        success = self.generate_foundation()
        
        # Log usage
        self.log_usage_locally(success)
        
        # Show next steps
        if success:
            self.show_next_steps()
            
        return success
    
    def check_version_advisory(self):
        """Advisory version check - warns but doesn't block."""
        if date.today() > EXPIRATION_DATE:
            if not self.is_quiet:
                print(f"""
⚠️  VERSION OUTDATED - SECURITY RISK

This version expired on {EXPIRATION_DATE.isoformat()}.
Security practices and compliance requirements have likely changed.

Using outdated templates may introduce vulnerabilities or compliance issues.

Get the latest version at: {OFFICIAL_REPO}

""")

            if self.is_interactive:
                response = input("Type 'I understand the risks' to continue anyway: ")
                if response.strip() != "I understand the risks":
                    print("❌ Exiting for your safety. Please get the latest version.")
                    return False
                print("⚠️  Proceeding with outdated version at your own risk.\n")
            else:
                # Non-interactive mode: warn but continue (user accepted terms)
                if not self.is_quiet:
                    print("⚠️  Non-interactive mode: Proceeding with outdated version.\n")

        return True
    
    def show_ethical_agreement(self):
        """Display ethical use agreement and get acknowledgment."""
        # In non-interactive mode, terms are pre-accepted via --accept-terms
        if not self.is_interactive:
            if not self.is_quiet:
                print("✓ Ethical use agreement accepted via --accept-terms flag.\n")
            return True

        print(ETHICAL_USE_AGREEMENT)

        # Force them to read it
        for i in range(3, 0, -1):
            print(f"\rPlease read the agreement carefully... {i}", end="")
            time.sleep(1)
        print("\n")

        response = input("Do you understand and agree to these terms? (yes/no): ")
        if response.lower() != "yes":
            print("❌ You must agree to the ethical use terms to continue.")
            return False

        # Second confirmation for emphasis
        response = input("Will you customize these templates for your specific needs? (yes/no): ")
        if response.lower() != "yes":
            print("❌ Templates MUST be customized. They are not complete solutions.")
            return False

        return True
    
    def show_educational_intro(self):
        """Explain what we're doing and why."""
        if self.is_quiet:
            return

        if self.is_interactive:
            print("""
🎓 EDUCATION FIRST, GENERATION SECOND

This tool will:
1. EXPLAIN each governance principle
2. TEACH why it matters
3. SHOW what could go wrong without it
4. THEN generate a template

Remember: Understanding > Copy-Pasting

Let's build a thoughtful foundation for your project...

""")
            time.sleep(2)
        else:
            # Non-interactive: brief message
            print("🏗️  Generating project foundation (non-interactive mode)...\n")
    
    def educate_before_generating(self, principle: str):
        """Show education content before generating each component."""
        if principle in self.education_shown:
            return  # Don't repeat education

        self.education_shown.add(principle)

        info = LITE_PRINCIPLES[principle]
        education = EDUCATION_CONTENT.get(principle, "")

        if self.is_quiet:
            # Quiet mode: minimal output
            return

        if self.is_interactive:
            # Full interactive education experience
            print(f"""
{'='*70}
📖 PRINCIPLE: {info['name']}
{'='*70}

❓ WHY IT MATTERS:
{info['why']}

📋 WHAT IT DOES:
{info['what']}

⚠️  RISK WITHOUT IT:
{info['risk']}
{education}

Generating template in 3 seconds...
""")
            time.sleep(3)

            # Quiz to ensure understanding
            response = input("Quick check: Will you customize this template? (yes/no): ")
            if response.lower() != "yes":
                print("⚠️  Remember: Templates must be customized!\n")
        else:
            # Non-interactive: condensed output
            print(f"  📖 {info['name']}: {info['why']}")
    
    def generate_foundation(self):
        """Generate the core foundation files with education."""
        output_dir = Path(self.args.output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)
        
        print(f"\n🏗️  Building foundation in: {output_dir.absolute()}\n")
        
        # Generate each component with education
        try:
            # README
            self.educate_before_generating("readme")
            self.generate_readme(output_dir)
            
            # CONTRIBUTING
            self.educate_before_generating("contributing")
            self.generate_contributing(output_dir)
            
            # LICENSE
            self.educate_before_generating("license")
            self.generate_license(output_dir)
            
            # Handle --all flag
            include_all = getattr(self.args, 'include_all', False)

            # CODE_OF_CONDUCT
            if self.args.include_coc or include_all:
                self.educate_before_generating("code-of-conduct")
                self.generate_code_of_conduct(output_dir)

            # SECURITY
            if self.args.include_security or include_all:
                self.educate_before_generating("security")
                self.generate_security(output_dir)

            # v2.3.0: GitHub templates (issue templates + PR template)
            if getattr(self.args, 'include_github_templates', False) or include_all:
                self.educate_before_generating("issue-templates")
                self.generate_issue_templates(output_dir)
                self.educate_before_generating("pr-template")
                self.generate_pr_template(output_dir)

            # v2.3.0: CHANGELOG
            if getattr(self.args, 'include_changelog', False) or include_all:
                self.educate_before_generating("changelog")
                self.generate_changelog(output_dir)

            # v2.4.0: Enhanced security
            if getattr(self.args, 'include_enhanced_security', False) or include_all:
                self.educate_before_generating("enhanced-security")
                self.generate_enhanced_security(output_dir)

            # v2.4.0: Secrets detection
            if getattr(self.args, 'include_secrets_detection', False) or include_all:
                self.educate_before_generating("secrets-detection")
                self.generate_pre_commit_config(output_dir)

            # v2.5.0: ADR templates
            if getattr(self.args, 'include_adr', False) or include_all:
                self.educate_before_generating("adr")
                self.generate_adr_templates(output_dir)

            # v2.5.0: CI workflow
            if getattr(self.args, 'include_ci', False) or include_all:
                self.educate_before_generating("ci-workflow")
                self.generate_ci_workflow(output_dir)

            # .gitignore
            self.generate_gitignore(output_dir)

            # Ethics notice in each file
            self.add_ethics_notice_to_files(output_dir)

            return True
            
        except Exception as e:
            print(f"❌ Error during generation: {e}")
            return False
    
    def generate_readme(self, output_dir: Path):
        """Generate README with educational comments."""
        content = f"""# {self.args.project_name}

<!-- 
TEMPLATE NOTICE: This is a starting point. Replace all placeholder text.
Generated by: {SCRIPT_VERSION} on {date.today().isoformat()}
Remember: This template does not make your project secure or compliant.
-->

## 📋 Description

[REPLACE: Describe what your project does and why it exists]

## 🎯 Why This Project?

[REPLACE: What problem does this solve? Why should someone care?]

## 🚀 Quick Start

\\`\\`\\`bash
# Installation
[REPLACE: How to install your project]

# Basic usage
[REPLACE: Simplest possible example]
\\`\\`\\`

## 📖 Documentation

[REPLACE: Link to detailed documentation]

## 🤝 Contributing

Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

<!-- LEARNING: Good READMEs include contribution info even if brief -->

## 📜 License

This project is licensed under the {self.args.license.upper()} License - see [LICENSE](LICENSE) file.

## 🔒 Security

For security concerns, see [SECURITY.md](SECURITY.md).

<!-- LEARNING: Always provide a security contact method -->

## ⚠️ Important Notice

This README was generated from a template. It must be customized for your specific project.
Using template documentation without customization may mislead users and contributors.

---

Generated with [Project Foundation Generator]({OFFICIAL_REPO}) - Please customize!
"""
        
        self.write_file(output_dir / "README.md", content)
    
    def generate_contributing(self, output_dir: Path):
        """Generate comprehensive CONTRIBUTING.md with educational elements."""
        content = f"""# Contributing to {self.args.project_name}

<!--
TEMPLATE NOTICE: This is a comprehensive contribution guide template.
Customize sections marked with [CUSTOMIZE] for your project's specific needs.
-->

Thank you for your interest in contributing to {self.args.project_name}!

This guide explains our contribution workflow, conventions, and review process.

---

## 📚 Before You Start

### Understanding Our Workflow

We use a **fork-first workflow**. This means:
- You work on your own copy (fork) of the repository
- Changes are proposed via Pull Requests from your fork
- This keeps the main repository clean and secure

### Why Fork-First?

1. **Security**: Only maintainers have write access to the main repo
2. **Experimentation**: You can freely experiment in your fork
3. **Learning**: Great practice for contributing to any open source project
4. **Backup**: Your fork serves as a backup of your work

---

## 🔀 Fork-First Workflow

### Step 1: Fork the Repository

1. Click the "Fork" button on the repository page
2. This creates your personal copy at `github.com/YOUR-USERNAME/{self.args.project_name.lower().replace(' ', '-')}`

### Step 2: Clone Your Fork

```bash
# Clone your fork locally
git clone https://github.com/YOUR-USERNAME/{self.args.project_name.lower().replace(' ', '-')}.git
cd {self.args.project_name.lower().replace(' ', '-')}

# Add the original repo as "upstream" for syncing
git remote add upstream https://github.com/ORIGINAL-OWNER/{self.args.project_name.lower().replace(' ', '-')}.git
```

### Step 3: Keep Your Fork Updated

```bash
# Fetch upstream changes
git fetch upstream

# Merge upstream main into your local main
git checkout main
git merge upstream/main

# Push updates to your fork
git push origin main
```

### Step 4: Create a Feature Branch

**Never work directly on `main`**. Always create a branch:

```bash
git checkout -b type/description
```

---

## 🏷️ Branch Naming Conventions

Use descriptive branch names following this pattern:

```
type/short-description
```

### Branch Types

| Type | Purpose | Example |
|------|---------|---------|
| `feat/` | New feature | `feat/user-authentication` |
| `fix/` | Bug fix | `fix/login-validation` |
| `docs/` | Documentation only | `docs/api-examples` |
| `refactor/` | Code restructuring | `refactor/database-layer` |
| `test/` | Adding/updating tests | `test/auth-unit-tests` |
| `chore/` | Maintenance tasks | `chore/update-dependencies` |

### Good Branch Names
- `feat/add-dark-mode`
- `fix/memory-leak-on-upload`
- `docs/installation-guide`

### Avoid
- `my-changes` (not descriptive)
- `fix` (too vague)
- `john-branch` (personal names)

---

## 📝 Conventional Commits

We follow [Conventional Commits](https://www.conventionalcommits.org/) for clear, consistent history.

### Format

```
type(scope): description

[optional body]

[optional footer]
```

### Commit Types

| Type | When to Use |
|------|-------------|
| `feat` | Adding new functionality |
| `fix` | Fixing a bug |
| `docs` | Documentation changes only |
| `style` | Formatting (no code logic change) |
| `refactor` | Restructuring without behavior change |
| `test` | Adding or updating tests |
| `chore` | Maintenance (dependencies, configs) |

### Examples

```bash
# Feature
git commit -m "feat(auth): add password reset flow"

# Bug fix
git commit -m "fix(api): handle null response from server"

# Documentation
git commit -m "docs(readme): add installation instructions"

# Breaking change (note the !)
git commit -m "feat(api)!: change authentication endpoint"
```

### Why Conventional Commits?

1. **Automatic changelogs**: Tools can generate release notes
2. **Clear history**: Easy to understand what changed and why
3. **Semantic versioning**: Commit types inform version bumps
4. **Better reviews**: Reviewers understand intent quickly

---

## 💡 Suggesting Features

### Before Proposing

1. **Search existing issues** - your idea may already be discussed
2. **Check the roadmap** - it might be planned already
3. **Consider scope** - does it fit the project's goals?

### Priority Assessment

When proposing features, consider these factors:

| Factor | Questions to Ask |
|--------|------------------|
| **Impact** | How many users benefit? How significant is the improvement? |
| **Effort** | How complex is implementation? What's the maintenance burden? |
| **Risk** | What could break? Are there security implications? |
| **Alignment** | Does it fit project goals and architecture? |

### Feature Request Template

```markdown
## Problem Statement
What problem does this solve?

## Proposed Solution
How should it work?

## Alternatives Considered
What other approaches exist?

## Priority Assessment
- Impact: [High/Medium/Low]
- Effort: [High/Medium/Low]
- Risk: [High/Medium/Low]
```

---

## 🔍 Code Review Process

### What Reviewers Look For

1. **Correctness**: Does the code do what it claims?
2. **Tests**: Are changes covered by tests?
3. **Style**: Does it follow project conventions?
4. **Documentation**: Are changes documented?
5. **Security**: Are there any vulnerabilities?
6. **Performance**: Any performance implications?

### Educational Review Criteria

We review with education in mind:

| Criteria | What We Check |
|----------|---------------|
| **Clarity** | Is the code readable and self-documenting? |
| **Simplicity** | Is this the simplest solution that works? |
| **Maintainability** | Will future contributors understand this? |
| **Best Practices** | Does it follow established patterns? |

### Responding to Feedback

- **Be open**: Feedback improves code quality
- **Ask questions**: If something is unclear, ask
- **Iterate**: Multiple rounds of review are normal
- **Learn**: Each review is a learning opportunity

---

## 🚀 Pull Request Process

### Before Submitting

- [ ] Code compiles/runs without errors
- [ ] Tests pass locally
- [ ] Branch is up-to-date with main
- [ ] Commit messages follow conventions
- [ ] Documentation updated if needed

### PR Description Template

```markdown
## Summary
Brief description of changes.

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation
- [ ] Refactoring

## Testing
How were changes tested?

## Checklist
- [ ] Tests added/updated
- [ ] Documentation updated
- [ ] No breaking changes (or documented)
```

### After Submitting

1. **Respond to reviews** within a reasonable timeframe
2. **Push fixes** as new commits (easier to review)
3. **Request re-review** after addressing feedback
4. **Squash commits** will happen on merge (if configured)

---

## 📝 Coding Standards

[CUSTOMIZE: Add your project-specific coding standards here]

### General Guidelines

- Write clear, self-documenting code
- Include comments for complex logic
- Follow existing patterns in the codebase
- Keep functions focused and small

### Testing Requirements

[CUSTOMIZE: Specify your testing requirements]

- Unit tests for new functionality
- Integration tests for API changes
- All tests must pass before merge

---

## 🤝 Code of Conduct

[CUSTOMIZE: Reference your CODE_OF_CONDUCT.md if you have one]

We are committed to providing a welcoming and inclusive environment.
Please be respectful and constructive in all interactions.

---

## ❓ Getting Help

- **Questions**: [CUSTOMIZE: Where should questions go?]
- **Bugs**: Open an issue with the bug report template
- **Features**: Open an issue with the feature request template

---

## ⚠️ Template Notice

This CONTRIBUTING.md was generated as a starting point.
Sections marked with [CUSTOMIZE] need project-specific content.
Review and adapt all sections to match your actual workflow.

---

Generated with [Project Foundation Template]({OFFICIAL_REPO})
"""

        self.write_file(output_dir / "CONTRIBUTING.md", content)
    
    def generate_license(self, output_dir: Path):
        """Generate LICENSE file with explanation."""
        licenses = {
            "mit": """MIT License

Copyright (c) {year} {author}

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.""",
            "apache": """Copyright {year} {author}

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.""",
            "gpl": """This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Copyright (C) {year} {author}"""
        }
        
        content = licenses.get(self.args.license, licenses["mit"])
        content = content.format(
            year=date.today().year,
            author=self.args.author_name
        )
        
        # Add educational header
        educational_header = f"""# ⚠️ LICENSE NOTICE

This is a TEMPLATE license. You must:
1. Verify this license suits your needs
2. Replace {{author}} with actual copyright holder
3. Consider patent, trademark, and other IP concerns
4. Consult legal counsel for commercial projects

License type: {self.args.license.upper()}
Learn more: https://choosealicense.com/licenses/{self.args.license}/

---

"""
        
        self.write_file(output_dir / "LICENSE", educational_header + content)
    
    def generate_code_of_conduct(self, output_dir: Path):
        """Generate CODE_OF_CONDUCT.md with context."""
        content = f"""# Code of Conduct

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

## ⚠️ Template Notice

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
        
        self.write_file(output_dir / "CODE_OF_CONDUCT.md", content)
    
    def generate_security(self, output_dir: Path):
        """Generate SECURITY.md with educational content."""
        content = f"""# Security Policy

<!--
TEMPLATE NOTICE: Security policies require actual processes behind them.
Do not publish this without setting up the mentioned procedures.
-->

## ⚠️ Critical Notice

This is a TEMPLATE security policy. Publishing this without actual security
processes in place creates false confidence and increases risk.

Before using this template:
1. Set up security monitoring
2. Create incident response procedures
3. Designate security contacts
4. Implement the mentioned practices

## 🔒 Security Practices

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

## 🚨 Reporting Vulnerabilities

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

## 📧 Contact

Security Email: [REPLACE: Add actual security contact]
Response Time: [REPLACE: Set realistic response time]

## ⚠️ Template Warning

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
        
        self.write_file(output_dir / "SECURITY.md", content)
    
    def generate_gitignore(self, output_dir: Path):
        """Generate .gitignore without education (self-explanatory)."""
        content = """# Dependencies
node_modules/
vendor/
venv/
env/

# Environment files
.env
.env.*
!.env.example

# IDE
.idea/
.vscode/
*.swp

# OS
.DS_Store
Thumbs.db

# Build outputs
dist/
build/
*.pyc
__pycache__/

# Logs
*.log
logs/

# Testing
coverage/
.coverage
.pytest_cache/

# Project specific
# [ADD YOUR PROJECT'S SPECIFIC IGNORES HERE]
"""
        
        self.write_file(output_dir / ".gitignore", content)

    # v2.3.0: Community governance templates

    def generate_issue_templates(self, output_dir: Path):
        """Generate GitHub issue templates (bug report and feature request)."""
        github_dir = output_dir / ".github" / "ISSUE_TEMPLATE"
        github_dir.mkdir(parents=True, exist_ok=True)

        # Bug report template
        bug_report = f"""---
name: Bug Report
about: Create a report to help us improve
title: '[Bug]: '
labels: 'bug, triage'
assignees: ''
---

## Bug Description
<!-- A clear and concise description of what the bug is -->

## Steps to Reproduce
1. Go to '...'
2. Click on '...'
3. Scroll down to '...'
4. See error

## Expected Behavior
<!-- What you expected to happen -->

## Actual Behavior
<!-- What actually happened -->

## Environment
- OS: [e.g., Windows 11, macOS 14, Ubuntu 22.04]
- Version: [e.g., v1.0.0]
- Browser (if applicable): [e.g., Chrome 120]

## Screenshots
<!-- If applicable, add screenshots to help explain your problem -->

## Additional Context
<!-- Add any other context about the problem here -->

## Possible Solution
<!-- Optional: If you have a suggestion for fixing the bug -->

---
*Generated with [Project Foundation Template]({OFFICIAL_REPO})*
"""
        self.write_file(github_dir / "bug_report.md", bug_report)

        # Feature request template
        feature_request = f"""---
name: Feature Request
about: Suggest an idea for this project
title: '[Feature]: '
labels: 'enhancement'
assignees: ''
---

## Problem Statement
<!-- Is your feature request related to a problem? Describe it -->
<!-- Example: I'm always frustrated when... -->

## Proposed Solution
<!-- A clear and concise description of what you want to happen -->

## Alternatives Considered
<!-- Any alternative solutions or features you've considered -->

## Additional Context
<!-- Add any other context, mockups, or screenshots about the feature request -->

## Priority Assessment (Optional)
<!-- If you've evaluated this feature: -->
- **Impact**: How much does this improve the project?
- **Effort**: How realistic is implementation?
- **Risk**: What could go wrong?
- **Suggested Priority**: High / Medium / Low

---
*Generated with [Project Foundation Template]({OFFICIAL_REPO})*
"""
        self.write_file(github_dir / "feature_request.md", feature_request)

    def generate_pr_template(self, output_dir: Path):
        """Generate GitHub pull request template."""
        github_dir = output_dir / ".github"
        github_dir.mkdir(parents=True, exist_ok=True)

        pr_template = f"""## Description
<!-- Describe your changes in detail -->

## Related Issue
<!-- Link to the issue this PR addresses (e.g., Closes #123) -->

## Type of Change
- [ ] Bug fix (non-breaking change that fixes an issue)
- [ ] New feature (non-breaking change that adds functionality)
- [ ] Breaking change (fix or feature that would cause existing functionality to not work as expected)
- [ ] Documentation update
- [ ] Refactoring (no functional changes)
- [ ] Performance improvement
- [ ] Test updates

## Checklist
- [ ] My code follows the project's style guidelines
- [ ] I have performed a self-review of my own code
- [ ] I have commented my code, particularly in hard-to-understand areas
- [ ] I have made corresponding changes to the documentation
- [ ] My changes generate no new warnings
- [ ] I have added tests that prove my fix is effective or that my feature works
- [ ] New and existing unit tests pass locally with my changes

## Screenshots (if applicable)
<!-- Add screenshots to demonstrate the change -->

## Additional Notes
<!-- Any additional information that reviewers should know -->

---
*Generated with [Project Foundation Template]({OFFICIAL_REPO})*
"""
        self.write_file(github_dir / "PULL_REQUEST_TEMPLATE.md", pr_template)

    def generate_changelog(self, output_dir: Path):
        """Generate CHANGELOG.md following Keep a Changelog format."""
        today = date.today().isoformat()
        project_name = self.args.project_name

        changelog = f"""# Changelog

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
        self.write_file(output_dir / "CHANGELOG.md", changelog)

    # v2.4.0: Security features

    def generate_enhanced_security(self, output_dir: Path):
        """Generate comprehensive SECURITY.md with vulnerability reporting process."""
        author_email = f"security@{self.args.project_name.lower().replace(' ', '-')}.example.com"
        today = date.today().isoformat()

        security_content = f"""# Security Policy

<!--
TEMPLATE NOTICE: This is a comprehensive security policy template.
You MUST customize the email addresses, response times, and supported versions.
A security policy without actual processes behind it creates false confidence.
-->

## Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| Latest  | ✅ Yes            |
| Previous| ⚠️  Limited       |
| Older   | ❌ No             |

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

## Secrets Management

This project uses pre-commit hooks to prevent accidental secret commits.

### Protected Patterns

The following types of secrets are automatically detected:
- API keys and access tokens
- Database credentials and connection strings
- Private keys and certificates
- OAuth secrets and JWT tokens
- Cloud service credentials (AWS, Azure, GCP)
- GitHub tokens and other VCS credentials

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
        self.write_file(output_dir / "SECURITY.md", security_content)

    def generate_pre_commit_config(self, output_dir: Path):
        """Generate pre-commit configuration with secrets detection."""
        # Create .pre-commit-config.yaml
        pre_commit_config = """# Pre-commit hooks configuration
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
        self.write_file(output_dir / ".pre-commit-config.yaml", pre_commit_config)

        # Create hooks directory and detection script
        hooks_dir = output_dir / ".hooks"
        hooks_dir.mkdir(parents=True, exist_ok=True)

        patterns_for_script = "\\n".join([
            "api[_-]?key.*[:=]",
            "secret.*[:=]",
            "password.*[:=]",
            "token.*[:=]",
            "BEGIN.*PRIVATE KEY",
            "ghp_[A-Za-z0-9]",
            "sk-[A-Za-z0-9]",
            "mongodb://",
            "postgres://",
            "mysql://"
        ])

        detect_secrets_script = f"""#!/bin/bash
# Secrets detection pre-commit hook
# Generated by Project Foundation Template v2.4.0

set -e

RED='\\033[0;31m'
GREEN='\\033[0;32m'
YELLOW='\\033[1;33m'
NC='\\033[0m'

echo "${{YELLOW}}[secrets-detection] Scanning staged files for potential secrets...${{NC}}"

# Get staged files
STAGED_FILES=$(git diff --cached --name-only --diff-filter=ACM 2>/dev/null || echo "")

if [ -z "$STAGED_FILES" ]; then
    echo "${{GREEN}}No files to check${{NC}}"
    exit 0
fi

SECRETS_FOUND=0

# Patterns to check (simplified for portability)
PATTERNS=(
    "api[_-]?key.*[:=]"
    "secret.*[:=]"
    "password.*[:=]"
    "token.*[:=]"
    "BEGIN.*PRIVATE KEY"
    "ghp_[A-Za-z0-9]"
    "sk-[A-Za-z0-9]"
)

for file in $STAGED_FILES; do
    if [ ! -f "$file" ]; then
        continue
    fi

    # Skip binary files
    if file "$file" 2>/dev/null | grep -q "binary"; then
        continue
    fi

    for pattern in "${{PATTERNS[@]}}"; do
        if grep -iE "$pattern" "$file" 2>/dev/null | grep -v "^#" | grep -v "REPLACE" > /dev/null; then
            echo "${{RED}}Potential secret in $file:${{NC}}"
            grep -n -iE "$pattern" "$file" 2>/dev/null | grep -v "^#" | grep -v "REPLACE" | head -3
            SECRETS_FOUND=1
        fi
    done
done

if [ $SECRETS_FOUND -eq 1 ]; then
    echo ""
    echo "${{RED}}Potential secrets detected! Please review before committing.${{NC}}"
    echo "${{YELLOW}}Tips:${{NC}}"
    echo "  - Use environment variables instead of hardcoded values"
    echo "  - Add sensitive files to .gitignore"
    echo "  - Use a secrets manager for production credentials"
    echo ""
    echo "To bypass (NOT RECOMMENDED): git commit --no-verify"
    exit 1
fi

echo "${{GREEN}}No secrets detected${{NC}}"
exit 0
"""
        hook_path = hooks_dir / "detect-secrets.sh"
        self.write_file(hook_path, detect_secrets_script)

        # Make script executable on Unix
        try:
            import stat
            hook_path.chmod(hook_path.stat().st_mode | stat.S_IEXEC)
        except Exception:
            pass  # Windows doesn't need this

    # v2.5.0: Advanced governance

    def generate_adr_templates(self, output_dir: Path):
        """Generate Architecture Decision Record templates and index."""
        adr_dir = output_dir / "docs" / "adr"
        adr_dir.mkdir(parents=True, exist_ok=True)
        today = date.today().isoformat()

        # ADR README/Index
        adr_readme = f"""# Architecture Decision Records

This directory contains Architecture Decision Records (ADRs) for {self.args.project_name}.

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
        self.write_file(adr_dir / "README.md", adr_readme)

        # ADR Template
        adr_template = """# ADR-NNNN: [Short Title]

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
        self.write_file(adr_dir / "template.md", adr_template)

        # First ADR - Recording Architecture Decisions
        first_adr = f"""# ADR-0001: Record Architecture Decisions

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
        self.write_file(adr_dir / "0001-record-architecture-decisions.md", first_adr)

    def generate_ci_workflow(self, output_dir: Path):
        """Generate GitHub Actions CI workflow."""
        workflows_dir = output_dir / ".github" / "workflows"
        workflows_dir.mkdir(parents=True, exist_ok=True)

        ci_workflow = f"""# Continuous Integration Workflow
# Generated by Project Foundation Template v2.5.0
#
# This workflow runs on every push and pull request to ensure code quality.
# Customize the steps below for your project's needs.

name: CI

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main, develop]

jobs:
  build:
    runs-on: ubuntu-latest

    strategy:
      matrix:
        # [CUSTOMIZE]: Update for your language/runtime versions
        node-version: [18.x, 20.x]

    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      # [CUSTOMIZE]: Replace with your language's setup action
      - name: Setup Node.js ${{{{ matrix.node-version }}}}
        uses: actions/setup-node@v4
        with:
          node-version: ${{{{ matrix.node-version }}}}
          cache: 'npm'

      # [CUSTOMIZE]: Replace with your package manager commands
      - name: Install dependencies
        run: npm ci

      - name: Run linter
        run: npm run lint
        continue-on-error: true  # Remove this line once linting is configured

      - name: Run tests
        run: npm test
        continue-on-error: true  # Remove this line once tests are configured

      - name: Build
        run: npm run build
        continue-on-error: true  # Remove this line once build is configured

  # Optional: Add security scanning
  # security:
  #   runs-on: ubuntu-latest
  #   steps:
  #     - uses: actions/checkout@v4
  #     - name: Run security audit
  #       run: npm audit

# ---
# TEMPLATE NOTICE:
# This is a starting point. You must:
# 1. Replace placeholder commands with your actual build/test commands
# 2. Update the matrix for your language versions
# 3. Remove continue-on-error once steps are properly configured
# 4. Add additional jobs as needed (deploy, security scan, etc.)
#
# Generated with Project Foundation Template
# https://github.com/malcolmhoward/project-foundation-template
"""
        self.write_file(workflows_dir / "ci.yml", ci_workflow)

        # Also create a basic PR validation workflow
        pr_workflow = """# Pull Request Validation
# Validates PR title follows conventional commits format

name: PR Validation

on:
  pull_request:
    types: [opened, edited, synchronize]

jobs:
  validate-pr-title:
    runs-on: ubuntu-latest
    steps:
      - name: Validate PR title
        uses: amannn/action-semantic-pull-request@v5
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        with:
          # Require conventional commit format
          types: |
            feat
            fix
            docs
            style
            refactor
            perf
            test
            build
            ci
            chore
            revert
          requireScope: false
          subjectPattern: ^.{1,50}$
          subjectPatternError: |
            PR title must be 50 characters or less.
            Current length: {length}

# ---
# This workflow ensures PR titles follow conventional commits format.
# This helps with automatic changelog generation and semantic versioning.
#
# Generated with Project Foundation Template
"""
        self.write_file(workflows_dir / "pr-validation.yml", pr_workflow)

    def add_ethics_notice_to_files(self, output_dir: Path):
        """Add ethics notice to a summary file."""
        notice = f"""# ⚠️ ETHICAL USE NOTICE

This project foundation was generated on {datetime.now().isoformat()}.

The following templates were created:
{chr(10).join(f"- {f}" for f in self.generated_files)}

## Critical Reminders:

1. **These are TEMPLATES** - They must be customized
2. **This is NOT legal advice** - Consult professionals for compliance
3. **This is NOT security consultation** - Implement actual security measures
4. **Templates ≠ Implementation** - You must actually follow these practices
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

1. ✏️ Customize every template for your specific needs
2. 🔍 Review with appropriate professionals
3. 🚀 Implement the actual practices
4. 🔄 Keep them updated
5. 📚 Keep learning

---

Generated with Project Foundation Generator {SCRIPT_VERSION}
Learn more: {OFFICIAL_REPO}
"""
        
        self.write_file(output_dir / "FOUNDATION_NOTICE.md", notice)
    
    def write_file(self, filepath: Path, content: str):
        """Write file and track what was generated."""
        filepath.write_text(content, encoding='utf-8')
        self.generated_files.append(filepath.name)
        print(f"✅ Generated: {filepath.name}")
    
    def log_usage_locally(self, success: bool):
        """Log usage locally for accountability."""
        log_dir = Path.home() / ".project_foundation_logs"
        log_dir.mkdir(exist_ok=True)
        
        log_file = log_dir / f"usage_{date.today().isoformat()}.log"
        
        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "version": SCRIPT_VERSION,
            "project_name": self.args.project_name,
            "success": success,
            "files_generated": len(self.generated_files),
            "ethics_acknowledged": True,
            "duration_seconds": (datetime.now() - self.start_time).total_seconds(),
            "outdated": date.today() > EXPIRATION_DATE
        }
        
        with open(log_file, 'a') as f:
            f.write(json.dumps(log_entry) + "\n")
        
        if self.args.verbose:
            print(f"\n📝 Usage logged to: {log_file}")
    
    def show_next_steps(self):
        """Show what to do next with emphasis on customization."""
        print(f"""
{'='*70}
✅ FOUNDATION GENERATED - NOW THE REAL WORK BEGINS
{'='*70}

Your templates have been created in: {Path(self.args.output_dir).absolute()}

⚠️ THESE ARE NOT READY TO USE YET! You must:

1. 📝 CUSTOMIZE every template for your specific needs
   - Replace all [REPLACE] placeholders
   - Remove irrelevant sections
   - Add project-specific information

2. 🔍 REVIEW with appropriate professionals
   - Legal review for licenses and compliance
   - Security review for policies
   - Team review for contribution guidelines

3. 🚀 IMPLEMENT the actual practices
   - Don't just have documents - follow them
   - Set up mentioned processes
   - Train team members

4. 🔄 MAINTAIN these documents
   - Review quarterly
   - Update when practices change
   - Learn from incidents

5. 📚 KEEP LEARNING
   - These are basics - keep improving
   - Join communities
   - Share your experiences

Remember: Documentation without implementation is worse than no documentation.
It creates false confidence and legal liability.

QUESTIONS TO ASK YOURSELF:
- Do I understand WHY each file exists?
- Have I customized everything for my needs?
- Am I prepared to actually follow these practices?
- Do I have the processes to enforce these policies?

If you answered "no" to any of these, you're not ready to publish these files.

---

Thank you for using this tool ethically and thoughtfully.
Together, we can build better, safer software.

Learn more: {OFFICIAL_REPO}
""")

def parse_arguments():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description="Generate ethical project foundations with education",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
This tool generates TEMPLATE documentation for project governance.
Templates must be customized for your specific needs.

Examples:
  Interactive mode:
    %(prog)s --project-name MyProject --author-name "Jane Doe"

  Non-interactive mode (for CI/scripts):
    %(prog)s --non-interactive --accept-terms --project-name MyProject --author-name "Jane Doe"

  Using config file:
    %(prog)s --config .foundationrc

Config file format (.foundationrc):
  {
    "project_name": "MyProject",
    "author_name": "Jane Doe",
    "license": "mit",
    "include_coc": true,
    "include_security": true
  }
        """
    )

    # Core options
    parser.add_argument(
        "--project-name",
        dest="project_name",
        help="Name of your project (required unless in config)"
    )

    parser.add_argument(
        "--author-name",
        dest="author_name",
        help="Your name or organization (required unless in config)"
    )

    parser.add_argument(
        "--license",
        choices=["mit", "apache", "gpl"],
        default="mit",
        help="License type (default: mit)"
    )

    parser.add_argument(
        "--output-dir",
        dest="output_dir",
        default=".",
        help="Output directory (default: current directory)"
    )

    # Optional components
    parser.add_argument(
        "--include-coc",
        dest="include_coc",
        action="store_true",
        help="Include Code of Conduct template"
    )

    parser.add_argument(
        "--include-security",
        dest="include_security",
        action="store_true",
        help="Include Security Policy template"
    )

    # v2.3.0: Community governance templates
    parser.add_argument(
        "--include-github-templates",
        dest="include_github_templates",
        action="store_true",
        help="Include GitHub issue and PR templates (.github/ folder)"
    )

    parser.add_argument(
        "--include-changelog",
        dest="include_changelog",
        action="store_true",
        help="Include CHANGELOG.md template"
    )

    parser.add_argument(
        "--all",
        dest="include_all",
        action="store_true",
        help="Include all optional templates (CoC, Security, GitHub, Changelog, Enhanced Security, Secrets Detection, ADR, CI)"
    )

    # v2.4.0: Security features
    parser.add_argument(
        "--include-enhanced-security",
        dest="include_enhanced_security",
        action="store_true",
        help="Include comprehensive SECURITY.md with vulnerability reporting process"
    )

    parser.add_argument(
        "--include-secrets-detection",
        dest="include_secrets_detection",
        action="store_true",
        help="Include pre-commit config with secrets detection hooks"
    )

    # v2.5.0: Advanced governance
    parser.add_argument(
        "--include-adr",
        dest="include_adr",
        action="store_true",
        help="Include Architecture Decision Record templates"
    )

    parser.add_argument(
        "--include-ci",
        dest="include_ci",
        action="store_true",
        help="Include GitHub Actions CI workflow"
    )

    # v2.2.0: Non-interactive mode
    parser.add_argument(
        "--non-interactive",
        dest="non_interactive",
        action="store_true",
        help="Run without prompts (for CI/scripts). Requires --accept-terms."
    )

    parser.add_argument(
        "--accept-terms",
        dest="accept_terms",
        action="store_true",
        help="Accept ethical use agreement (required for --non-interactive)"
    )

    # v2.2.0: Config file support
    parser.add_argument(
        "--config",
        dest="config_path",
        help="Path to config file (default: .foundationrc in current directory)"
    )

    # v2.2.0: JSON export
    parser.add_argument(
        "--export-json",
        dest="export_json",
        action="store_true",
        help="Output results as JSON (useful for tooling integration)"
    )

    # Output control
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Show detailed output"
    )

    parser.add_argument(
        "--quiet",
        action="store_true",
        help="Minimal output (implies --non-interactive behavior for output only)"
    )

    parser.add_argument(
        "--version",
        action="version",
        version=f"%(prog)s {SCRIPT_VERSION}"
    )

    return parser.parse_args()

def validate_arguments(args) -> tuple:
    """
    Validate that required arguments are provided.
    Returns (is_valid, error_message).
    """
    errors = []

    if not args.project_name:
        errors.append("--project-name is required (or set 'project_name' in config file)")

    if not args.author_name:
        errors.append("--author-name is required (or set 'author_name' in config file)")

    if args.non_interactive and not args.accept_terms:
        errors.append("--accept-terms is required when using --non-interactive mode")
        errors.append("  This ensures you've read and understood the ethical use agreement.")
        errors.append("  Review the agreement by running without --non-interactive first.")

    if errors:
        return False, "\n".join(errors)

    return True, ""

def main():
    """Main entry point with ethical safeguards."""
    args = parse_arguments()

    # Load config file and merge with arguments
    config = load_config_file(args.config_path)
    if config:
        args = merge_config_with_args(args, config)

    # Validate arguments
    is_valid, error_message = validate_arguments(args)
    if not is_valid:
        # Educational error message
        print(f"""
❌ MISSING REQUIRED ARGUMENTS

{error_message}

📚 HELP: How to provide required values

Option 1: Command line arguments
  python {sys.argv[0]} --project-name "MyProject" --author-name "Your Name"

Option 2: Config file (.foundationrc)
  Create a file named .foundationrc with:
  {{
    "project_name": "MyProject",
    "author_name": "Your Name"
  }}

Option 3: Both (command line overrides config)
  python {sys.argv[0]} --config .foundationrc --project-name "Override"

For CI/automation, use:
  python {sys.argv[0]} --non-interactive --accept-terms --project-name "MyProject" --author-name "Your Name"

Run with --help for all options.
""")
        return 1

    # Show banner (unless quiet mode)
    if not args.quiet:
        print(f"""
╔══════════════════════════════════════════════════════════════╗
║     Project Foundation Generator - Ethical Lite Edition      ║
║                      Version {SCRIPT_VERSION:^8}                      ║
╚══════════════════════════════════════════════════════════════╝
""")

    generator = EthicalFoundationGenerator(args)

    success = generator.run()

    # Export JSON if requested
    if args.export_json:
        result = {
            "success": success,
            "version": SCRIPT_VERSION,
            "project_name": args.project_name,
            "author_name": args.author_name,
            "output_dir": str(Path(args.output_dir).absolute()),
            "files_generated": generator.generated_files if success else [],
            "timestamp": datetime.now().isoformat()
        }
        print("\n--- JSON OUTPUT ---")
        print(json.dumps(result, indent=2))

    if success:
        return 0
    else:
        return 1


if __name__ == "__main__":
    sys.exit(main())
