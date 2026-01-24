# foundation/generator.py
# Main generator class for Project Foundation Template

"""
EthicalFoundationGenerator - Main generator class with ethical safeguards and education.

This module contains the core generator logic extracted from setup_foundation_lite.py
for better modularity and testability.
"""

import json
import time
from datetime import date, datetime
from pathlib import Path

from core.utils import (
    SCRIPT_VERSION,
    OFFICIAL_REPO,
    EXPIRATION_DATE,
)

from core.education import (
    LITE_PRINCIPLES,
    EDUCATION_CONTENT,
)

from core.ethics import (
    check_version_advisory,
    show_ethical_agreement,
)

from core.generation_log import write_generation_log

from core.templates import (
    # Core templates
    generate_readme_content,
    generate_contributing_content,
    generate_license_content,
    generate_gitignore_content,
    # Governance templates
    generate_code_of_conduct_content,
    generate_security_content,
    generate_changelog_content,
    # GitHub templates
    generate_bug_report_template,
    generate_feature_request_template,
    generate_pr_template_content,
    generate_ci_workflow_content,
    generate_pr_validation_workflow_content,
    # Advanced templates
    generate_enhanced_security_content,
    generate_pre_commit_config_content,
    generate_detect_secrets_script,
    generate_adr_readme_content,
    generate_adr_template_content,
    generate_first_adr_content,
    generate_ethics_notice_content,
    # Accessibility templates (v3.1.0)
    generate_glossary_content,
    generate_maintainers_content,
    generate_scaffold_manifest_content,
)


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

        # v3.7.0: Generate generation log if requested
        if success:
            self.generate_generation_log()

        # Show next steps
        if success:
            self.show_next_steps()

        return success

    def check_version_advisory(self):
        """Advisory version check - warns but doesn't block.

        This is a thin wrapper around the standalone check_version_advisory
        function from core.ethics for backward compatibility.
        """
        return check_version_advisory(
            expiration_date=EXPIRATION_DATE,
            is_interactive=self.is_interactive,
            is_quiet=self.is_quiet
        )

    def show_ethical_agreement(self):
        """Display ethical use agreement and get acknowledgment.

        This is a thin wrapper around the standalone show_ethical_agreement
        function from core.ethics for backward compatibility.
        """
        return show_ethical_agreement(
            is_interactive=self.is_interactive,
            is_quiet=self.is_quiet
        )

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

            # v3.1.0: Accessibility features
            if getattr(self.args, 'include_glossary', False) or include_all:
                self.educate_before_generating("glossary")
                self.generate_glossary(output_dir)

            if getattr(self.args, 'include_maintainers', False) or include_all:
                self.educate_before_generating("maintainers")
                self.generate_maintainers(output_dir)

            # .gitignore
            self.generate_gitignore(output_dir)

            # Scaffold manifest (always generated to document what was created)
            if getattr(self.args, 'include_manifest', False) or include_all:
                self.generate_scaffold_manifest(output_dir)

            # Ethics notice in each file
            self.add_ethics_notice_to_files(output_dir)

            return True

        except Exception as e:
            print(f"❌ Error during generation: {e}")
            return False

    def generate_readme(self, output_dir: Path):
        """Generate README with educational comments."""
        content = generate_readme_content(self.args.project_name, self.args.license)
        self.write_file(output_dir / "README.md", content)

    def generate_contributing(self, output_dir: Path):
        """Generate comprehensive CONTRIBUTING.md with educational elements."""
        content = generate_contributing_content(self.args.project_name)
        self.write_file(output_dir / "CONTRIBUTING.md", content)

    def generate_license(self, output_dir: Path):
        """Generate LICENSE file with explanation."""
        content = generate_license_content(self.args.license, self.args.author_name)
        self.write_file(output_dir / "LICENSE", content)

    def generate_code_of_conduct(self, output_dir: Path):
        """Generate CODE_OF_CONDUCT.md with context."""
        content = generate_code_of_conduct_content()
        self.write_file(output_dir / "CODE_OF_CONDUCT.md", content)

    def generate_security(self, output_dir: Path):
        """Generate SECURITY.md with educational content."""
        content = generate_security_content()
        self.write_file(output_dir / "SECURITY.md", content)

    def generate_gitignore(self, output_dir: Path):
        """Generate .gitignore without education (self-explanatory)."""
        content = generate_gitignore_content()
        self.write_file(output_dir / ".gitignore", content)

    # v2.3.0: Community governance templates

    def generate_issue_templates(self, output_dir: Path):
        """Generate GitHub issue templates (bug report and feature request)."""
        github_dir = output_dir / ".github" / "ISSUE_TEMPLATE"
        github_dir.mkdir(parents=True, exist_ok=True)

        self.write_file(github_dir / "bug_report.md", generate_bug_report_template())
        self.write_file(github_dir / "feature_request.md", generate_feature_request_template())

    def generate_pr_template(self, output_dir: Path):
        """Generate GitHub pull request template."""
        github_dir = output_dir / ".github"
        github_dir.mkdir(parents=True, exist_ok=True)

        self.write_file(github_dir / "PULL_REQUEST_TEMPLATE.md", generate_pr_template_content())

    def generate_changelog(self, output_dir: Path):
        """Generate CHANGELOG.md following Keep a Changelog format."""
        content = generate_changelog_content(self.args.project_name)
        self.write_file(output_dir / "CHANGELOG.md", content)

    # v2.4.0: Security features

    def generate_enhanced_security(self, output_dir: Path):
        """Generate comprehensive SECURITY.md with vulnerability reporting process."""
        content = generate_enhanced_security_content(self.args.project_name)
        self.write_file(output_dir / "SECURITY.md", content)

    def generate_pre_commit_config(self, output_dir: Path):
        """Generate pre-commit configuration with secrets detection."""
        # Create .pre-commit-config.yaml
        self.write_file(output_dir / ".pre-commit-config.yaml", generate_pre_commit_config_content())

        # Create hooks directory and detection script
        hooks_dir = output_dir / ".hooks"
        hooks_dir.mkdir(parents=True, exist_ok=True)

        hook_path = hooks_dir / "detect-secrets.sh"
        self.write_file(hook_path, generate_detect_secrets_script())

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

        self.write_file(adr_dir / "README.md", generate_adr_readme_content(self.args.project_name))
        self.write_file(adr_dir / "template.md", generate_adr_template_content())
        self.write_file(adr_dir / "0001-record-architecture-decisions.md", generate_first_adr_content())

    def generate_ci_workflow(self, output_dir: Path):
        """Generate GitHub Actions CI workflow."""
        workflows_dir = output_dir / ".github" / "workflows"
        workflows_dir.mkdir(parents=True, exist_ok=True)

        self.write_file(workflows_dir / "ci.yml", generate_ci_workflow_content())
        self.write_file(workflows_dir / "pr-validation.yml", generate_pr_validation_workflow_content())

    # v3.1.0: Accessibility features

    def generate_glossary(self, output_dir: Path):
        """Generate GLOSSARY.md with project terminology definitions."""
        content = generate_glossary_content()
        self.write_file(output_dir / "GLOSSARY.md", content)

    def generate_maintainers(self, output_dir: Path):
        """Generate MAINTAINERS.md with maintainer information."""
        content = generate_maintainers_content(
            self.args.project_name,
            self.args.author_name
        )
        self.write_file(output_dir / "MAINTAINERS.md", content)

    def generate_scaffold_manifest(self, output_dir: Path):
        """Generate SCAFFOLD_MANIFEST.md documenting what was scaffolded."""
        # Collect configuration info
        config = {
            "project_name": self.args.project_name,
            "author_name": self.args.author_name,
            "license": getattr(self.args, 'license', 'mit'),
            "preset": getattr(self.args, 'preset', 'minimal'),
        }

        # Get principles and guides used (simplified for now)
        principles_used = list(self.education_shown)
        guides_used = []  # Will be populated when guide system is connected

        content = generate_scaffold_manifest_content(
            project_name=self.args.project_name,
            version=SCRIPT_VERSION,
            preset=getattr(self.args, 'preset', 'minimal'),
            generated_files=self.generated_files,
            principles_used=principles_used,
            guides_used=guides_used,
            config=config
        )
        self.write_file(output_dir / "SCAFFOLD_MANIFEST.md", content)

    def add_ethics_notice_to_files(self, output_dir: Path):
        """Add ethics notice to a summary file."""
        content = generate_ethics_notice_content(self.generated_files)
        self.write_file(output_dir / "FOUNDATION_NOTICE.md", content)

    # v3.7.0: Generation log

    def generate_generation_log(self):
        """Generate GENERATION_LOG if requested via --include-generation-log."""
        include_log = getattr(self.args, 'include_generation_log', False)

        if not include_log:
            return

        output_dir = Path(self.args.output_dir)
        log_format = getattr(self.args, 'log_format', 'md')
        log_to = getattr(self.args, 'log_to', None)

        # Filter out the generation log itself from the list
        files_to_log = [f for f in self.generated_files
                        if not f.startswith('GENERATION_LOG')]

        created_logs = write_generation_log(
            output_dir=output_dir,
            project_name=self.args.project_name,
            generated_files=files_to_log,
            log_format=log_format,
            log_to=log_to
        )

        for log_file in created_logs:
            print(f"📋 Generated: {Path(log_file).name}")

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
