# examples/plugins/custom_principle.py
# Example custom principle plugin

"""
Example Custom Principle Plugin.

This file demonstrates how to create a custom principle that extends
the Project Foundation Template. Users can copy this file to their
plugin directory and modify it to create their own principles.

Plugin directories (searched in order):
    1. $FOUNDATION_PLUGINS_DIR (environment variable)
    2. ~/.foundation-plugins/
    3. ./plugins/ (relative to project root)

Usage:
    1. Copy this file to ~/.foundation-plugins/my_principle.py
    2. Modify the class to define your own principle
    3. Run the generator - your principle will be automatically loaded

Example:
    $ cp examples/plugins/custom_principle.py ~/.foundation-plugins/
    $ python generate_foundation.py --list-principles
    # Your custom principle should appear in the list
"""

# Import the base class for type hints and IDE support
# Note: This import is optional - the plugin system will work without it
try:
    from core.plugins import PrinciplePlugin, GuidePlugin
except ImportError:
    # Define stub classes if core is not available
    # This allows the file to be edited standalone
    class PrinciplePlugin:
        pass

    class GuidePlugin:
        pass


# =============================================================================
# PLUGIN METADATA (Optional)
# =============================================================================
# This metadata is used for display purposes and plugin management.
# It's optional but recommended for documenting your plugin.

PLUGIN_METADATA = {
    "name": "Team Standards Plugin",
    "version": "1.0.0",
    "author": "Your Name <your.email@example.com>",
    "description": "Custom principles for team-specific standards and workflows",
}


# =============================================================================
# PRINCIPLE PLUGIN EXAMPLE
# =============================================================================

class TeamStandardsPrinciple(PrinciplePlugin):
    """Example: Team coding standards principle.

    This principle defines team-specific coding standards that go beyond
    the generic code standards provided by the foundation template.

    Required class attributes:
        PRINCIPLE_ID: Unique identifier (lowercase, hyphens allowed)
        PRINCIPLE: Dict with name, why, what, risk keys
        EDUCATION: Educational content string

    Tips for creating good principles:
        - Keep PRINCIPLE_ID short but descriptive
        - Make 'why' compelling - explain the business value
        - Make 'what' actionable - list specific items
        - Make 'risk' concrete - describe real consequences
    """

    # Unique identifier for this principle
    # Must be lowercase, can contain hyphens, no spaces
    # This ID is used in presets and configuration
    PRINCIPLE_ID = "team-standards"

    # The principle definition
    # All four fields are required
    PRINCIPLE = {
        "name": "Team Coding Standards",
        "why": "Ensures consistency across team members and reduces code review friction",
        "what": "Team-specific naming conventions, patterns, and code organization rules",
        "risk": "Inconsistent code style leads to harder reviews and maintenance burden",
    }

    # Educational content for this principle
    # This is displayed when users request education mode
    # Can include markdown formatting
    EDUCATION = """
## Team Coding Standards

Consistent coding standards help your team:

1. **Reduce cognitive load** - Familiar patterns are easier to read
2. **Speed up code reviews** - Less time debating style
3. **Onboard faster** - New members learn the "team way"
4. **Maintain code** - Anyone can work on any part

### What to Include

Your team standards should cover:
- Naming conventions (variables, functions, classes)
- File organization and project structure
- Comment and documentation requirements
- Error handling patterns
- Testing requirements

### Implementation Tips

- Start with industry standards (PEP 8, Google Style, etc.)
- Add team-specific modifications
- Document the "why" behind each rule
- Use automated tools (linters, formatters) to enforce
- Review and update standards quarterly
"""


# =============================================================================
# GUIDE PLUGIN EXAMPLE
# =============================================================================

class OnboardingGuide(GuidePlugin):
    """Example: Developer onboarding guide.

    This guide provides a comprehensive onboarding process for new
    team members joining the project.

    Required class attributes:
        GUIDE_ID: Unique identifier (lowercase, hyphens allowed)
        GUIDE: Dict with title, purpose, audience, complexity keys
        CONTENT: Full guide content (markdown)

    Optional class attributes:
        RELATED_PRINCIPLES: List of related principle IDs
    """

    # Unique identifier for this guide
    GUIDE_ID = "onboarding"

    # Guide metadata
    GUIDE = {
        "title": "Developer Onboarding Guide",
        "purpose": "Help new team members get productive quickly",
        "audience": "New developers joining the team",
        "complexity": "beginner",  # beginner, intermediate, or advanced
    }

    # Related principles (optional)
    # These are principle IDs that complement this guide
    RELATED_PRINCIPLES = ["team-standards", "contributing", "code-standards"]

    # Full guide content in markdown format
    CONTENT = """
# Developer Onboarding Guide

Welcome to the team! This guide will help you get set up and productive.

## Day 1: Environment Setup

### Prerequisites

- [ ] Git installed and configured
- [ ] Python 3.8+ installed
- [ ] IDE of choice (we recommend VS Code or PyCharm)
- [ ] Access to team repositories

### Setup Steps

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd <project-name>
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # or `venv\\Scripts\\activate` on Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   pip install -r requirements-dev.txt
   ```

4. **Run tests to verify setup**
   ```bash
   pytest
   ```

## Day 2-3: Understanding the Codebase

### Key Files to Read

1. `README.md` - Project overview and quick start
2. `CONTRIBUTING.md` - How to contribute
3. `docs/architecture.md` - System architecture
4. `CHANGELOG.md` - Recent changes

### Code Structure

```
project/
├── core/           # Core business logic
├── api/            # API endpoints
├── tests/          # Test files
├── docs/           # Documentation
└── scripts/        # Utility scripts
```

## Week 1: First Contribution

### Recommended First Tasks

- Fix a documentation typo
- Add a missing test
- Implement a small feature from the backlog

### Code Review Process

1. Create a feature branch
2. Make your changes
3. Run tests locally
4. Open a pull request
5. Address review feedback
6. Merge after approval

## Resources

- Team Slack: #dev-team
- Wiki: https://wiki.example.com
- Office hours: Tuesdays 2-3pm

---

*Welcome aboard! Don't hesitate to ask questions.*
"""


# =============================================================================
# MULTIPLE PLUGINS IN ONE FILE
# =============================================================================
# You can define multiple principles and guides in a single file.
# Each class with the correct attributes will be loaded automatically.

class DocumentationStandardsPrinciple(PrinciplePlugin):
    """Another example principle in the same file."""

    PRINCIPLE_ID = "documentation-standards"

    PRINCIPLE = {
        "name": "Documentation Standards",
        "why": "Good documentation reduces support burden and improves adoption",
        "what": "Standards for code comments, API docs, and user guides",
        "risk": "Poor documentation leads to misuse and increased support requests",
    }

    EDUCATION = """
## Documentation Standards

Documentation is a first-class deliverable, not an afterthought.

### Types of Documentation

1. **Code Comments** - Explain "why", not "what"
2. **API Documentation** - Auto-generated from docstrings
3. **Architecture Docs** - High-level system design
4. **User Guides** - How to use the software
5. **Runbooks** - Operational procedures

### Best Practices

- Write docs as you code
- Keep docs close to code (in repo)
- Review docs in PRs
- Test documentation accuracy
"""
