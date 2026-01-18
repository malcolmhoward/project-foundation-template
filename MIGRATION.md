# Migration Guide

This document helps users understand the transition from the enterprise edition to the lite edition and provides guidance on feature reintroduction.

## Understanding the Versions

### Enterprise Edition (v2.0.1)
- **Size**: ~6,500 lines
- **Principles**: 23 governance principles
- **Modules**: 20 documentation modules
- **Presets**: 5 (minimal, light, standard, strict, enterprise)
- **Focus**: Comprehensive automation

### Lite Edition (v2.1.0+)
- **Size**: ~900 lines
- **Principles**: 5 core principles
- **Modules**: Core documentation only
- **Presets**: 1 (minimal/educational)
- **Focus**: Education first

## Why Features Were Removed

The reduction was not due to technical issues but ethical concerns. See [ETHICS.md](ETHICS.md) for full context.

### Identified Risks

| Risk | Description | Mitigation |
|------|-------------|------------|
| Governance Theater | Templates create appearance without substance | Educational requirements |
| AI Exploitation | Mass generation of malicious-looking legitimate repos | Usage logging, delays |
| Environmental Impact | Unnecessary CI/CD carbon footprint | Minimal defaults |
| Social Engineering | Professional facades for scams | Template markers |
| Legal Exploitation | Templates claimed as compliance | Clear disclaimers |

### The Core Problem

Users could generate complete governance suites without understanding:
- What each file does
- Why it matters
- How to customize it properly

This created false confidence and enabled potential misuse.

## Feature Reintroduction Timeline

### 23 Governance Principles

| # | Principle | Current Status | Target Version |
|---|-----------|----------------|----------------|
| 1 | README Documentation | ✅ Available | v2.1.0 |
| 2 | Contribution Guidelines | ✅ Available | v2.1.0 |
| 3 | License Selection | ✅ Available | v2.1.0 |
| 4 | Code of Conduct | ✅ Available | v2.1.0 |
| 5 | Security Basics | ✅ Available | v2.1.0 |
| 6 | Quality Assurance | ⏳ Planned | v2.4.0 |
| 7 | Code Standards | ⏳ Planned | v2.4.0 |
| 8 | Versioning | ⏳ Planned | v2.4.0 |
| 9 | Compliance Policy | ⏳ Planned | v2.4.0 |
| 10 | Security Policy (Advanced) | ⏳ Planned | v2.4.0 |
| 11 | Issue Templates | ⏳ Planned | v2.3.0 |
| 12 | Pull Request Templates | ⏳ Planned | v2.3.0 |
| 13 | Internationalization | ⏳ Planned | v2.5.0 |
| 14 | Audit Logging | ⏳ Planned | v2.5.0 |
| 15 | Dependency Scanning | ⏳ Planned | v2.5.0 |
| 16 | Container Support | ⏳ Planned | v2.5.0 |
| 17 | Documentation System | ⏳ Planned | v2.5.0 |
| 18 | CI/CD Pipelines | ⏳ Planned | v2.5.0 |
| 19 | Branch Protection | ⏳ Planned | v2.5.0 |
| 20 | Release Management | ⏳ Planned | v2.5.0 |
| 21 | Deprecation Policy | ⏳ Planned | v3.0.0 |
| 22 | Accessibility | ⏳ Planned | v3.0.0 |
| 23 | Performance Standards | ⏳ Planned | v3.0.0 |

### 20 Documentation Modules

| # | Module | Target Version |
|---|--------|----------------|
| 1 | Test Strategies | v2.5.0 |
| 2 | Code Review Guide | v2.5.0 |
| 3 | Versioning Guide | v2.5.0 |
| 4 | Release Process | v2.5.0 |
| 5 | Dependency Guide | v2.5.0 |
| 6 | Compliance Guide | v3.0.0 |
| 7 | API Standards | v3.0.0 |
| 8 | Troubleshooting | v3.0.0 |
| 9 | FAQ | v3.0.0 |
| 10 | REFS.md | v3.0.0 |
| 11 | GLOSSARY.md | v2.4.0 |
| 12 | ROADMAP.md | v2.3.0 |
| 13 | SCAFFOLD_MANIFEST.md | v2.4.0 |
| 14 | CONTRIBUTING.md (Enhanced) | v2.3.0 |
| 15 | CHANGELOG.md | v2.3.0 |
| 16 | COMPLIANCE.md | v2.4.0 |
| 17 | Coding Standards | v2.4.0 |
| 18 | Architecture Decisions | v2.5.0 |
| 19 | Security Disclosure | v2.4.0 |
| 20 | Onboarding Guide | v3.0.0 |

### Governance Presets

| Preset | Principles Included | Target Version |
|--------|---------------------|----------------|
| minimal | 5 core | ✅ v2.1.0 (current) |
| light | ~10 | v2.3.0 |
| standard | ~15 (default) | v2.4.0 |
| strict | ~20 | v2.5.0 |
| enterprise | All 23 | v3.0.0 |

## How to Upgrade Safely

### From Enterprise (v2.0.1) to Lite (v2.1.x)

If you have existing projects generated with the enterprise edition:

1. **Don't panic**: Your existing files still work
2. **Don't regenerate blindly**: You'll lose customizations
3. **Review what you have**: Understand each generated file
4. **Adopt incrementally**: Add lite-edition principles to your understanding

```bash
# DON'T do this:
python setup_foundation_lite.py --force-overwrite existing-project/

# DO this:
# 1. Generate to a new directory
python setup_foundation_lite.py --project-name "Test" --output-dir ./compare/

# 2. Compare with your existing files
diff -r existing-project/ ./compare/

# 3. Manually adopt improvements you understand
```

### From Lite (v2.1.x) to Future Versions

As features are reintroduced:

1. **Read the release notes**: Understand what's new and why
2. **Review the educational content**: Each feature comes with WHAT/WHY/HOW
3. **Test in isolation**: Generate to a test directory first
4. **Adopt deliberately**: Add features because you need them, not because they exist

### Version Upgrade Checklist

- [ ] Read CHANGELOG for the new version
- [ ] Understand new features (WHAT/WHY/HOW)
- [ ] Generate to test directory
- [ ] Compare with existing project
- [ ] Identify relevant additions
- [ ] Manually integrate understood features
- [ ] Update your documentation to reflect changes

## Maintaining Enterprise Features Manually

If you need enterprise features before their reintroduction:

### Option 1: Reference the Enterprise Branch
The enterprise edition exists in git history. You can reference it for ideas:

```bash
# View enterprise edition (if available in history)
git log --all --oneline | grep enterprise
```

### Option 2: Build Your Own
Use the lite edition's educational approach to build features yourself:

1. Understand WHAT the feature does
2. Understand WHY you need it
3. Implement HOW it works for your context

This approach creates better governance than copy-pasting.

### Option 3: Wait for Reintroduction
Each version adds features with full educational context. Waiting ensures:
- You get tested, documented features
- Educational content explains proper use
- Community feedback has refined the implementation

## Feature Prioritization

Features are reintroduced based on priority assessment:

| Dimension | Description |
|-----------|-------------|
| Impact | How significantly does this improve governance? |
| Effort | How much work is required to implement? |
| Risk | What could go wrong? |
| Strategic Fit | Alignment with educational mission |

Features are categorized as High, Medium, or Low priority based on these factors.

## Getting Help

### Questions About Migration
- Open an issue with the `migration` label
- Include your current version and target version
- Describe what you're trying to accomplish

### Feature Requests
- Use the feature request template
- Include educational value justification
- Consider impact, effort, and risk in your proposal

### Reporting Issues
- Use the bug report template
- Specify version numbers clearly
- Include reproduction steps

## Related Documents

- [ROADMAP.md](ROADMAP.md) - Detailed version roadmap
- [ETHICS.md](ETHICS.md) - Why this approach was chosen
- [docs/adr/0001-education-first.md](docs/adr/0001-education-first.md) - Decision record
- [CONTRIBUTING.md](CONTRIBUTING.md) - How to contribute

---

*Migration is not just about moving files—it's about moving understanding. Take the time to learn what you're adopting.*
