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

# Version and expiration
SCRIPT_VERSION = "2.1.0-lite"
EXPIRATION_DATE = date(2026, 3, 1)
OFFICIAL_REPO = "https://github.com/malcolmhoward/project-foundation-template"

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
    """
}

class EthicalFoundationGenerator:
    """Main generator class with ethical safeguards and education."""
    
    def __init__(self, args):
        self.args = args
        self.generated_files = []
        self.education_shown = set()
        self.start_time = datetime.now()
        
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
            print(f"""
⚠️  VERSION OUTDATED - SECURITY RISK
            
This version expired on {EXPIRATION_DATE.isoformat()}.
Security practices and compliance requirements have likely changed.

Using outdated templates may introduce vulnerabilities or compliance issues.

Get the latest version at: {OFFICIAL_REPO}

""")
            response = input("Type 'I understand the risks' to continue anyway: ")
            if response.strip() != "I understand the risks":
                print("❌ Exiting for your safety. Please get the latest version.")
                return False
                
            print("⚠️  Proceeding with outdated version at your own risk.\\n")
            
        return True
    
    def show_ethical_agreement(self):
        """Display ethical use agreement and get acknowledgment."""
        print(ETHICAL_USE_AGREEMENT)
        
        # Force them to read it
        for i in range(3, 0, -1):
            print(f"\\rPlease read the agreement carefully... {i}", end="")
            time.sleep(1)
        print("\\n")
        
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
    
    def educate_before_generating(self, principle: str):
        """Show education content before generating each component."""
        if principle in self.education_shown:
            return  # Don't repeat education
            
        self.education_shown.add(principle)
        
        info = LITE_PRINCIPLES[principle]
        education = EDUCATION_CONTENT.get(principle, "")
        
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
            print("⚠️  Remember: Templates must be customized!\\n")
    
    def generate_foundation(self):
        """Generate the core foundation files with education."""
        output_dir = Path(self.args.output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)
        
        print(f"\\n🏗️  Building foundation in: {output_dir.absolute()}\\n")
        
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
            
            # CODE_OF_CONDUCT
            if self.args.include_coc:
                self.educate_before_generating("code-of-conduct")
                self.generate_code_of_conduct(output_dir)
            
            # SECURITY
            if self.args.include_security:
                self.educate_before_generating("security")
                self.generate_security(output_dir)
            
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
        """Generate CONTRIBUTING.md with educational elements."""
        content = f"""# Contributing Guidelines

<!--
TEMPLATE NOTICE: Customize these guidelines for your project's needs.
Generic contribution guidelines frustrate contributors and maintainers alike.
-->

Thank you for your interest in contributing to {self.args.project_name}!

## 📚 Before Contributing

**IMPORTANT**: These are template guidelines. The maintainers must:
1. Customize these for their workflow
2. Define specific standards
3. Set up the mentioned processes

## 🎯 How to Contribute

### Reporting Issues

[REPLACE: How should issues be reported? What information is needed?]

### Suggesting Features

[REPLACE: How do you want feature requests handled?]

### Submitting Changes

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Test your changes [REPLACE: How should they test?]
5. Commit your changes (`git commit -m 'Add amazing feature'`)
6. Push to your branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

## 📝 Coding Standards

[REPLACE: What are your code style requirements?]
[REPLACE: Do you use linters? Which ones?]
[REPLACE: What about test coverage requirements?]

## ⚠️ Template Notice

This is a TEMPLATE. It provides structure but not substance.
The maintainers must define actual standards and processes.
Contributors should not assume these generic guidelines apply.

---

Generated with [Project Foundation Generator]({OFFICIAL_REPO})
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
            f.write(json.dumps(log_entry) + "\\n")
        
        if self.args.verbose:
            print(f"\\n📝 Usage logged to: {log_file}")
    
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

Example:
  %(prog)s --project-name MyProject --author "Jane Doe"
        """
    )
    
    parser.add_argument(
        "--project-name",
        required=True,
        help="Name of your project"
    )
    
    parser.add_argument(
        "--author-name",
        required=True,
        help="Your name or organization"
    )
    
    parser.add_argument(
        "--license",
        choices=["mit", "apache", "gpl"],
        default="mit",
        help="License type (default: mit)"
    )
    
    parser.add_argument(
        "--output-dir",
        default=".",
        help="Output directory (default: current directory)"
    )
    
    parser.add_argument(
        "--include-coc",
        action="store_true",
        help="Include Code of Conduct template"
    )
    
    parser.add_argument(
        "--include-security",
        action="store_true",
        help="Include Security Policy template"
    )
    
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Show detailed output"
    )
    
    parser.add_argument(
        "--version",
        action="version",
        version=f"%(prog)s {SCRIPT_VERSION}"
    )
    
    return parser.parse_args()

def main():
    """Main entry point with ethical safeguards."""
    args = parse_arguments()
    
    print(f"""
╔══════════════════════════════════════════════════════════════╗
║     Project Foundation Generator - Ethical Lite Edition      ║
║                      Version {SCRIPT_VERSION:^8}                      ║
╚══════════════════════════════════════════════════════════════╝
""")
    
    generator = EthicalFoundationGenerator(args)
    
    if generator.run():
        return 0
    else:
        return 1

if __name__ == "__main__":
    sys.exit(main())
