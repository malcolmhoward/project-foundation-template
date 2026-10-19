# Contributing to Project Foundation Template

Thank you for your interest in contributing! This document explains how to contribute effectively while maintaining our educational-first philosophy.

## Before You Start

### Understand Our Philosophy

This project prioritizes **education over automation**. Before contributing, please read:
- [ETHICS.md](ETHICS.md) - Our ethical framework and Principle Zero
- [docs/adr/0001-education-first.md](docs/adr/0001-education-first.md) - Why we chose this approach

### Key Principles

1. **Principle Zero**: "Do no harm, allow no harm" - All contributions must pass this test
2. **WHAT/WHY/HOW**: Documentation explains what something is, why it matters, then how to use it
3. **Education First**: Help users understand, do not just give them files
4. **No Governance Theater**: Substance over appearance

## Fork-First Workflow

All contributions must go through forks. Direct pushes to the main repository are not accepted.

### Setup

```bash
# 1. Fork the repository on GitHub

# 2. Clone your fork
git clone https://github.com/YOUR-USERNAME/project-foundation-template.git
cd project-foundation-template

# 3. Add upstream remote
git remote add upstream https://github.com/malcolmhoward/project-foundation-template.git

# 4. Verify remotes
git remote -v
# origin    https://github.com/YOUR-USERNAME/project-foundation-template.git (fetch)
# origin    https://github.com/YOUR-USERNAME/project-foundation-template.git (push)
# upstream  https://github.com/malcolmhoward/project-foundation-template.git (fetch)
# upstream  https://github.com/malcolmhoward/project-foundation-template.git (push)

# 5. Install development dependencies
pip install -r requirements-dev.txt
```

### Keeping Your Fork Updated

```bash
# Fetch upstream changes
git fetch upstream

# Merge upstream main into your main
git checkout main
git merge upstream/main

# Push to your fork
git push origin main
```

## Branch Naming Conventions

Use descriptive branch names following this pattern:

```
type/issue-number-short-description
```

### Types

| Type | Description | Example |
|------|-------------|---------|
| `feat` | New feature | `feat/42-add-docker-templates` |
| `fix` | Bug fix | `fix/17-config-parsing-error` |
| `docs` | Documentation only | `docs/23-improve-readme` |
| `chore` | Maintenance tasks | `chore/31-update-dependencies` |
| `refactor` | Code restructuring | `refactor/45-simplify-generator` |
| `test` | Adding tests | `test/28-add-unit-tests` |
| `style` | Formatting, no logic change | `style/12-fix-indentation` |

### Examples

```bash
# Good branch names
feat/15-add-issue-templates
fix/23-unicode-handling
docs/8-expand-ethics-section

# Bad branch names
my-changes
fix
update
```

## Conventional Commits

All commits must follow the [Conventional Commits](https://www.conventionalcommits.org/) specification.

### Format

```
type(scope): description

[optional body]

[optional footer(s)]
```

### Types

| Type | Description |
|------|-------------|
| `feat` | New feature for users |
| `fix` | Bug fix for users |
| `docs` | Documentation changes |
| `style` | Formatting, missing semicolons, etc. |
| `refactor` | Code change that neither fixes a bug nor adds a feature |
| `test` | Adding missing tests |
| `chore` | Maintenance tasks |

### Scopes

| Scope | Description |
|-------|-------------|
| `generator` | Changes to generate_foundation.py |
| `core` | Changes to core/ package |
| `principles` | Changes to governance principles |
| `guides` | Changes to documentation guides |
| `presets` | Changes to governance presets |
| `templates` | Changes to generated templates |
| `docs` | Documentation files |
| `ethics` | Ethical framework changes |
| `ci` | CI/CD configuration |
| `deps` | Dependency updates |

### Examples

```bash
# Good commits
feat(generator): add support for custom license headers
fix(templates): correct markdown formatting in README template
docs(ethics): clarify Principle Zero application
chore(deps): update Python minimum version to 3.9

# With body
feat(principles): add deprecation policy principle

Adds principle #21 for managing breaking changes and sunset features.
Includes educational content explaining WHAT/WHY/HOW of deprecation.

Closes #42

# Bad commits
fixed stuff
update
WIP
```

### Breaking Changes

For breaking changes, add `!` after the type/scope:

```bash
feat(generator)!: change default output directory structure

BREAKING CHANGE: Output files are now organized by category
instead of flat structure. Update any scripts that depend on
specific file paths.
```

## Educational Review Criteria

Pull requests are reviewed not just for code quality, but for educational value.

### Every PR Must Answer

1. **WHAT**: What does this change do?
2. **WHY**: Why is this change needed? What problem does it solve?
3. **HOW**: How does the implementation work?

### Review Checklist

Reviewers evaluate PRs against these criteria:

#### Ethical Alignment
- [ ] Passes Principle Zero ("Do no harm, allow no harm")
- [ ] Does not enable governance theater
- [ ] Considers potential for misuse
- [ ] Maintains educational focus

#### Educational Value
- [ ] Documentation explains WHAT/WHY/HOW
- [ ] Comments explain reasoning, not just mechanics
- [ ] Examples help users understand
- [ ] Complexity is justified by value

#### Code Quality
- [ ] Follows existing patterns
- [ ] No unnecessary complexity
- [ ] Appropriate error handling
- [ ] Clear variable/function names

#### Testing
- [ ] Generator still runs correctly
- [ ] Generated files are valid
- [ ] Edge cases considered
- [ ] Tests pass (`pytest`)

### Independent Review

**WHAT**: Every change is reviewed by someone other than its author before it merges. If an AI assistant helped write the change, "someone other than the author" means a person, or a different AI model working from a fresh context. The same assistant re-reading its own work, in the same conversation or a new one, does not count.

**WHY**: An author, human or AI, shares the assumptions that produced the change, so it tends to miss the same things twice. A reviewer who starts fresh with a different model, ideally from a different model family, sees different gaps. This is the [Mutual Fallibility](ETHICS.md#mutual-fallibility) design implication applied to review: redundant safeguards that assume both parties will make mistakes. A second opinion costs far less than a missed defect, so ask for it routinely, not only for large changes.

**HOW**:
- Match the review to the change:
  - code: a correctness review
  - code that handles credentials, personal data or untrusted input: also an adversarial security and privacy pass
  - documentation: a fact-check of claims, links, numbers and examples
- Give the reviewer the change and the context it needs, not the author's conclusions about it.
- If the change was reviewed before you opened the PR (for example by a different AI model), say so in the PR description, for example "Independent review: a different AI model; findings addressed in the second commit". Otherwise the maintainer's review is the independent review.
- AI review supplements maintainer review; it does not replace it. A maintainer still approves and merges.
- The habit is useful beyond pull requests too: ask a different reviewer to challenge a plan, a design or an analysis before you act on it.

### What We Look For

**Good PR description:**
```markdown
## Summary
Adds Docker template generation for projects that need containerization.

## Why This Matters
Many projects need Docker support but do not know where to start.
This provides an educational foundation that explains:
- What Docker does and why it is useful
- Basic Dockerfile structure
- When to use vs. not use containers

## Changes
- Added `docker` principle to generator
- Created Dockerfile template with educational comments
- Added docker-compose example for multi-service setups
- Updated CLAUDE.md with Docker guidance

## Educational Approach
Templates include extensive comments explaining each directive.
Users learn Docker concepts while getting a working starting point.
```

**Not-so-good PR description:**
```markdown
Added docker stuff
```

## Pull Request Process

### 1. Create Your Branch

```bash
git checkout main
git pull upstream main
git checkout -b feat/42-your-feature
```

### 2. Make Your Changes

- Write code following our patterns
- Add educational documentation
- Test thoroughly

### 3. Run Tests

```bash
# Run all tests
pytest

# Run with verbose output
pytest -v

# Run specific test file
pytest tests/test_foundation_generator.py
```

### 4. Commit Your Changes

```bash
git add .
git commit -m "feat(scope): clear description"
```

### 5. Push to Your Fork

```bash
git push origin feat/42-your-feature
```

### 6. Create Pull Request

- Go to your fork on GitHub
- Click "Compare & pull request"
- Fill out the PR template completely
- Link related issues
- If the change was independently reviewed before you opened the PR, say who or what reviewed it (see [Independent Review](#independent-review))

### 7. Address Review Feedback

- Respond to all comments
- Make requested changes
- Push additional commits (do not force-push during review)

### 8. After Approval

- Maintainer will merge
- Delete your branch

## Types of Contributions

### Documentation

- Fix typos and clarify language
- Add examples
- Improve educational content
- Expand WHAT/WHY/HOW explanations

### Bug Fixes

- Fix generator errors
- Correct template formatting
- Handle edge cases

### New Features

- Propose via issue first
- Include educational justification
- Assess priority based on impact, effort, and risk

### Tests

- Add test cases
- Improve coverage
- Test edge cases

## Adding New Principles

Want to add a new governance principle? Follow this process:

### 1. Propose the Principle

Open an issue with:
- **WHAT**: What is this principle?
- **WHY**: Why does it matter? What problem does it solve?
- **HOW**: How would users implement it?
- **Risks**: How could it be misused?

### 2. Create the Principle Module

Each principle is one module in `core/principles/`. Create `core/principles/new_principle.py`:

```python
# core/principles/new_principle.py
# New Principle (vX.Y.Z)

"""
New Principle.

One or two sentences on what this principle is and why it matters.

Introduced in vX.Y.Z.
"""

PRINCIPLE_ID = "new-principle"

PRINCIPLE = {
    "name": "New Principle Name",
    "why": "Why this principle matters and what problem it solves",
    "what": "What a project following it has or does",
    "risk": "What goes wrong without it",
}

EDUCATION = """
📚 LEARNING: One sentence a user should remember.

A short explanation of WHY and HOW. Cite a source for any statistic,
or leave the statistic out.
"""
```

### 3. Register the Principle

In `core/principles/__init__.py`:

- import `PRINCIPLE` and `EDUCATION` from the new module;
- add them to `ALL_PRINCIPLES` and `ALL_EDUCATION` under the principle's ID;
- add the ID to the category list it belongs to (for example `QUALITY_PRINCIPLES`); a new
  category also needs a branch in `get_principles_by_category()`;
- add the ID and the version that introduces it to `PRINCIPLE_VERSIONS`.

### 4. Add to Presets

Add the ID to the `principles` list of each preset in `core/presets/` that should include it.

A principle module provides education and appears in `--list-principles`; it does not generate a file on its own. To generate one, add a template in `core/templates/`, a step in `core/generator.py` and an `--include-*` option. Connecting principles and guides to generated output more generally is planned for v3.8.0 ([#116](https://github.com/malcolmhoward/project-foundation-template/issues/116)).

### 5. Add Tests

Add tests to `tests/test_foundation_principles.py`, for example that the principle is registered, belongs to a category, and has WHAT, WHY and RISK text. Existing tests check the total number of principles and each preset's list, so update those counts too.

### 6. Update Documentation

- Add the principle to the README's principles tables and counts
- Add an entry to CHANGELOG.md
- Update CLAUDE.md if the principle count changes

## Adding New Guides

Want to add a new documentation guide? Follow this process:

### 1. Propose the Guide

Open an issue with:
- **WHAT**: What is this guide about?
- **WHY**: Why would users need this guide?
- **HOW**: What will the guide teach?

### 2. Create the Guide Module

Each guide is one module in `core/guides/`. Create `core/guides/new_guide.py`:

```python
# core/guides/new_guide.py
# New Guide (vX.Y.Z)

"""
New Guide.

One or two sentences on what this guide teaches.

Introduced in vX.Y.Z.
"""

GUIDE_ID = "new-guide"

GUIDE = {
    "title": "New Guide Title",
    "purpose": "What a reader can do after reading it",
    "audience": "Who it is for",
    "complexity": "beginner",  # beginner, intermediate or advanced
}

RELATED_PRINCIPLES = ["contributing"]  # principle IDs from core/principles/

CONTENT = """
# New Guide Title

The guide itself, in Markdown, following WHAT / WHY / HOW.
"""
```

### 3. Register the Guide

In `core/guides/__init__.py`:

- import `GUIDE` and `CONTENT` from the new module;
- add them to `ALL_GUIDES` and `ALL_GUIDE_CONTENT` under the guide's ID;
- add the ID to its category list (for example `ONBOARDING_GUIDES`);
- add it to `GUIDE_COMPLEXITY` and, with the version that introduces it, to `GUIDE_VERSIONS`.

Guides appear in `--list-guides` and the Python API; they are not yet written into generated projects ([#116](https://github.com/malcolmhoward/project-foundation-template/issues/116)).

### 4. Add Tests

Add tests to `tests/test_foundation_guides.py`. A test there checks that every `RELATED_PRINCIPLES` entry is a real principle ID.

## Improving Translations

PFT includes translations for 10 locales in `core/internationalization/`. A wrong translation can mislead the people it is meant to help, so each locale records how far its translations can be trusted in its `translation_status`:

| Status | Meaning |
|--------|---------|
| `source` | The original text that translations are made from (English) |
| `unreviewed` | Not yet reviewed by a fluent speaker; may contain errors |
| `ai-reviewed` | Checked by an AI model, not a fluent speaker; may still contain errors |
| `reviewed` | Reviewed by a fluent speaker |

`ai-reviewed` and `reviewed` record who checked the locale and when, in `reviewed_by` and `reviewed_on`. Each locale also records where its translations came from in `translation_origin`: `source` (the original text), `ai-generated` (drafted with an AI model) or `human` (translated by a person). The nine non-English locales are `ai-generated`: they were drafted with an AI model when they were added in #85, whose commit is co-authored by Claude Opus 4.5.

The status and origin are shown wherever the translations are used: in `get_locale_metadata()`, in the supported-locales table and in every generated translation template (in its `_metadata`, or in `_translation_status` when the metadata is left out).

No locale has been reviewed yet: apart from English, every locale is `unreviewed`. Reviewing one is a good way to contribute if you are fluent in one of these languages.

### Reporting a Translation Problem

Open an issue titled "Translation: <language>" with the locale code, the key (for example `governance.code_of_conduct`), the current text, your suggested text, and why. You do not need to write code.

### Correcting a Translation

1. Edit the locale's file in `core/internationalization/` (for example `spanish.py`).
2. Keep every key: only the translated values change.
3. Open a PR that explains each change; a correction does not change the locale's status.

### Reviewing a Locale

A locale becomes `reviewed` only when a fluent speaker has checked **all** of its translations. A review by an AI model or a machine-translation tool can make a locale `ai-reviewed`, not `reviewed`: it can catch mistakes, but it cannot vouch for the result. For an AI review, use a different model from the one that drafted the translations (see the origin above), and name the model and version in `reviewed_by`, so readers can judge how independent the check was.

1. Check every value in the locale's `translations`, and correct any you need to.
2. Set `"translation_status": "reviewed"` (or `"ai-reviewed"`) and add `"reviewed_by"` (your GitHub username, or the AI model and version) and `"reviewed_on": "YYYY-MM-DD"`.
3. Open a PR saying how you reviewed it (for example, how you know the language and how you checked each string). A maintainer who does not speak the language checks that the review is described, not the translations themselves.

If a reviewed locale later gets new keys, set it back to `unreviewed` until they are reviewed too. If you translate a locale yourself rather than correcting it, also set `"translation_origin": "human"`.

## Priority Assessment

Significant changes should include priority evaluation:

| Dimension | Your Assessment |
|-----------|-----------------|
| **Impact** | How much does this improve the template? |
| **Effort** | How realistic is implementation? What resources are needed? |
| **Risk** | What could go wrong? |
| **Strategic Fit** | Does it align with the educational mission? |
| **Priority** | High / Medium / Low |

## Code of Conduct

We do not have a separate Code of Conduct file because our [ETHICS.md](ETHICS.md) covers behavioral expectations. In summary:

- Be respectful and constructive
- Focus on education over ego
- Assume good faith
- Help others learn

## Getting Help

- **Questions**: Open a discussion or issue
- **Bugs**: Use the bug report template
- **Features**: Use the feature request template
- **Security**: See [SECURITY.md](SECURITY.md) (if generated) or email directly

## Recognition

Contributors are recognized in:
- Release notes
- README acknowledgments
- Git history

We value all contributions, from typo fixes to major features.

## Attribution Policy

When features are inspired by community feedback, project usage, or external suggestions, we follow this attribution approach:

### Default: Anonymous Attribution

By default, inspiration is acknowledged anonymously:

```markdown
Inspired by community feedback
```

This protects privacy and does not create implied obligations between projects.

### Opt-In Named Attribution

If you would like to be named for inspiring a feature:

1. Request named attribution when suggesting the feature, or
2. Request retroactive attribution via issue or PR

Named attribution appears in:
- Relevant commit messages
- ACKNOWLEDGMENTS.md (if the project maintains one)
- Release notes for the version introducing the feature

Example:
```markdown
Inspired by feedback from @username on Project XYZ
```

### Guidelines

- **No implied partnership**: Attribution does not create official relationships between projects
- **Retroactive attribution**: Can be added after initial release
- **Maintainer discretion**: Final attribution wording at maintainer discretion
- **Opt-out**: Previously named attributions can be anonymized upon request

### Why This Matters

This policy ensures:
- Contributors receive credit when desired
- Privacy is protected by default
- Projects remain independent
- The collaborative spirit of open source is maintained

---

## Related Documents

- [ETHICS.md](ETHICS.md) - Ethical framework
- [ROADMAP.md](ROADMAP.md) - Feature roadmap
- [SEMANTIC_VERSIONING.md](SEMANTIC_VERSIONING.md) - Versioning policy
- [CLAUDE.md](CLAUDE.md) - LLM integration guide

---

*Contributing is about more than code. It is about helping others learn. Thank you for being part of that mission.*
