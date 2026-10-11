# core/templates/accessibility.py
# Accessibility Templates (v3.1.0)

"""
Accessibility-focused templates for Project Foundation Template.

Includes:
    - GLOSSARY.md: Project terminology definitions
    - MAINTAINERS.md: Maintainer information and roles
    - SCAFFOLD_MANIFEST.md: Generated files documentation

Introduced in v3.1.0.
"""

from typing import List, Dict
from datetime import datetime


def generate_glossary_content() -> str:
    """Generate GLOSSARY.md with comprehensive terminology definitions."""
    return """# Glossary of Terms

This glossary defines common terms, abbreviations, and concepts used throughout this project and in software development generally.

---

## A

### ADR (Architecture Decision Record)
A document that captures an important architectural decision along with its context and consequences. ADRs help preserve the "why" behind technical choices.

### API (Application Programming Interface)
A set of protocols and tools for building software applications. APIs define how different software components should interact with each other.

### Artifact
Any output produced during the software development process, such as compiled binaries, Docker images, documentation, or test reports.

---

## B

### Backward Compatible
A change that doesn't break existing functionality. Old code continues to work with new versions of a library or API.

### Branch
A parallel version of the codebase in Git. Branches allow developers to work on features independently before merging changes.

### Breaking Change
A change that causes existing code to stop working. Breaking changes require a major version bump in semantic versioning.

---

## C

### CD (Continuous Delivery/Deployment)
- **Continuous Delivery:** Automated preparation of code for release
- **Continuous Deployment:** Automated release to production

### CI (Continuous Integration)
The practice of frequently merging code changes into a shared repository, with automated testing to catch issues early.

### CLI (Command Line Interface)
A text-based interface for interacting with software using typed commands rather than a graphical interface.

### Commit
A snapshot of changes in Git. Each commit has a unique identifier (SHA) and records what changed, when, and by whom.

### Container
A lightweight, standalone package containing everything needed to run software, including code, runtime, and dependencies.

---

## D

### Dependency
External code or library that your project requires to function. Dependencies can be direct (explicitly imported) or transitive (dependencies of dependencies).

### Deploy
The process of releasing software to an environment where it can be accessed by users or other systems.

### Deprecation
The process of marking features as outdated and scheduled for removal. Deprecated features continue to work but should not be used in new code.

---

## F

### Fork
A personal copy of someone else's repository. Forks allow you to freely experiment with changes without affecting the original project.

---

## G

### Git
A distributed version control system for tracking changes in source code during software development.

### Governance
The policies, processes, and documentation that guide how a project is developed, maintained, and contributed to.

---

## I

### i18n (Internationalization)
Designing software to support multiple languages and regions. The "18" represents the 18 letters between "i" and "n" in "internationalization."

### Issue
A tracked item in a project management system representing a bug, feature request, task, or discussion topic.

---

## L

### Linter
A tool that analyzes source code for potential errors, bugs, stylistic issues, and suspicious constructs.

---

## M

### Main/Master Branch
The primary branch of a repository, typically containing production-ready code.

### Merge
Combining changes from one branch into another.

### Milestone
A collection of issues and pull requests grouped together to track progress toward a goal.

---

## P

### PR (Pull Request)
A request to merge code changes from one branch into another. PRs enable code review and discussion before changes are integrated.

### Preset
A predefined collection of governance principles bundled for common use cases.

### Principle
A governance concept that defines WHAT must be done, WHY it matters, and the RISK of omission.

---

## R

### Repository (Repo)
A storage location for a project, including all files, history, and branches.

### Review
The process of examining code changes before they are merged, checking for correctness, style, and potential issues.

---

## S

### Semantic Versioning (SemVer)
A versioning scheme using MAJOR.MINOR.PATCH format where:
- MAJOR: Breaking changes
- MINOR: New features (backward compatible)
- PATCH: Bug fixes (backward compatible)

### SHA (Secure Hash Algorithm)
A unique identifier for Git commits, typically shown as a 40-character hexadecimal string.

---

## T

### Tag
A reference to a specific commit, typically used to mark release versions.

### Template
A pre-configured starting point or boilerplate that can be customized for specific needs.

---

## V

### Version Control
A system for tracking and managing changes to files over time, enabling collaboration and history preservation.

---

## W

### Workflow
An automated process triggered by events (like pushing code), typically running tests, builds, or deployments.

---

*This glossary is generated by [Project Foundation Template](https://github.com/malcolmhoward/project-foundation-template).*
*For comprehensive software development terminology, see external resources like the [GitHub Glossary](https://docs.github.com/en/get-started/quickstart/github-glossary).*
"""


def generate_maintainers_content(project_name: str, author_name: str) -> str:
    """Generate MAINTAINERS.md with project maintainer information."""
    return f"""# Maintainers

This document lists the maintainers of **{project_name}** and describes how to become one.

---

## Current Maintainers

### Lead Maintainer

| Name | GitHub | Role | Since |
|------|--------|------|-------|
| {author_name} | @{author_name.lower().replace(' ', '')} | Lead Maintainer | {datetime.now().strftime('%Y-%m')} |

### Component Maintainers

*Component maintainers have commit access to specific areas of the codebase.*

| Name | GitHub | Component | Since |
|------|--------|-----------|-------|
| *None yet* | | | |

### Emeritus Maintainers

*Former maintainers who have stepped back from active maintenance.*

| Name | GitHub | Tenure |
|------|--------|--------|
| *None yet* | | |

---

## Maintainer Responsibilities

Maintainers are expected to:

1. **Review Pull Requests** - Provide constructive feedback within a reasonable timeframe
2. **Triage Issues** - Label, prioritize, and respond to new issues
3. **Maintain Code Quality** - Ensure changes meet project standards
4. **Guide Contributors** - Help new contributors understand the codebase
5. **Make Releases** - Prepare and publish new versions
6. **Uphold the Code of Conduct** - Enforce community standards

---

## Becoming a Maintainer

### Path to Maintainership

1. **Consistent Contributions** - Make quality contributions over time
2. **Community Engagement** - Help others, review PRs, triage issues
3. **Domain Expertise** - Demonstrate understanding of specific areas
4. **Nomination** - Be nominated by an existing maintainer
5. **Consensus** - Receive approval from current maintainers

### Component Maintainer

To become a component maintainer:
- Make multiple significant contributions to that component
- Show understanding of the component's architecture
- Be nominated by the lead maintainer or another component maintainer

### Lead Maintainer

Lead maintainer succession:
- The lead maintainer may nominate a successor
- All maintainers vote on the nomination
- A majority is required for approval

---

## Decision Making

### Technical Decisions
- Minor decisions: Any maintainer can approve
- Major decisions: Require discussion and consensus
- Breaking changes: Require ADR and lead maintainer approval

### Project Direction
- Discussed in maintainer meetings or async communication
- Major direction changes require consensus
- The lead maintainer has final say in case of deadlock

---

## Communication

### Maintainer Channels
- **GitHub Issues/PRs**: Primary communication
- **Discussions**: For broader topics
- **Email**: For sensitive matters

### Response Time Expectations
- Issues: Initial response within 1 week
- PRs: Initial review within 2 weeks
- Security issues: Within 48 hours

---

## Recognition

We value our maintainers' contributions. Recognition includes:
- Listed in this document
- Credited in release notes
- Acknowledged in project communications

---

*Want to help maintain this project? Start by contributing regularly and engaging with the community.*
"""


def generate_scaffold_manifest_content(
    project_name: str,
    version: str,
    preset: str,
    generated_files: List[str],
    principles_used: List[str],
    guides_used: List[str],
    config: Dict
) -> str:
    """Generate SCAFFOLD_MANIFEST.md documenting what was scaffolded."""
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    files_list = "\n".join([f"- `{f}`" for f in sorted(generated_files)])
    principles_list = "\n".join([f"- {p}" for p in sorted(principles_used)]) if principles_used else "- *None specified*"
    guides_list = "\n".join([f"- {g}" for g in sorted(guides_used)]) if guides_used else "- *None specified*"

    config_items = "\n".join([f"| `{k}` | `{v}` |" for k, v in sorted(config.items())])

    return f"""# Scaffold Manifest

This document records what was generated by Project Foundation Template and the configuration used.

---

## Generation Summary

| Property | Value |
|----------|-------|
| **Project Name** | {project_name} |
| **Generated At** | {timestamp} |
| **Generator Version** | {version} |
| **Preset Used** | {preset} |

---

## Generated Files

The following files were created or updated:

{files_list}

---

## Principles Applied

The following governance principles were applied:

{principles_list}

---

## Guides Included

The following implementation guides were used:

{guides_list}

---

## Configuration Used

| Setting | Value |
|---------|-------|
{config_items}

---

## Validation

To verify your setup matches this manifest:

```bash
# Check all files exist
for file in {' '.join([f'"{f}"' for f in generated_files[:5]])}; do
  [ -f "$file" ] && echo "✓ $file" || echo "✗ $file missing"
done
```

---

## Updating Your Foundation

To update governance files in the future:

1. **Check for updates**
   ```bash
   # Compare with latest template version
   python generate_foundation.py --version
   ```

2. **Review changes**
   ```bash
   # Generate to temporary directory first
   python generate_foundation.py --preset {preset} --output-dir ./temp-foundation
   diff -r . ./temp-foundation
   ```

3. **Apply selectively**
   - Don't blindly overwrite customized files
   - Review each change before applying
   - Update this manifest after changes

---

## Notes

- This manifest is auto-generated and should not be manually edited
- If you add custom governance files, consider documenting them below
- Re-running the generator will update this manifest

### Custom Additions

*List any manually added governance files here:*

- *None yet*

---

*Generated by [Project Foundation Template](https://github.com/malcolmhoward/project-foundation-template) v{version}*
"""
