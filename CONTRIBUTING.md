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
3. **Education First**: Help users understand, don't just give them files
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
| `generator` | Changes to setup_foundation_lite.py |
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
feat(generator): add JSON export option

Adds --export-json flag that outputs generated file paths
and metadata in JSON format for tooling integration.

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
- [ ] Doesn't enable governance theater
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

### What We Look For

**Good PR description:**
```markdown
## Summary
Adds Docker template generation for projects that need containerization.

## Why This Matters
Many projects need Docker support but don't know where to start.
This provides an educational foundation that explains:
- What Docker does and why it's useful
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

### 3. Commit Your Changes

```bash
git add .
git commit -m "feat(scope): clear description"
```

### 4. Push to Your Fork

```bash
git push origin feat/42-your-feature
```

### 5. Create Pull Request

- Go to your fork on GitHub
- Click "Compare & pull request"
- Fill out the PR template completely
- Link related issues

### 6. Address Review Feedback

- Respond to all comments
- Make requested changes
- Push additional commits (don't force-push during review)

### 7. After Approval

- Maintainer will merge
- Delete your branch

## Types of Contributions

### Documentation
- Fix typos and clarify language
- Add examples
- Improve educational content
- Translate (future)

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

We don't have a separate Code of Conduct file because our [ETHICS.md](ETHICS.md) covers behavioral expectations. In summary:

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
- Git history (obviously)

We value all contributions, from typo fixes to major features.

---

*Contributing is about more than code—it's about helping others learn. Thank you for being part of that mission.*
