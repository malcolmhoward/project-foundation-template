# Migration Guide

This document helps you migrate between versions of Project Foundation Template.

---

## Migrating to v3.0.0 (Breaking Changes)

Version 3.0.0 introduces a **breaking change**: a new entrypoint script.

### Breaking Change: New Entrypoint

**Before (v2.x):**
```bash
python setup_foundation_lite.py --project-name "My Project" --author-name "Name"
```

**After (v3.0.0):**
```bash
python generate_foundation.py --project-name "My Project" --author-name "Name"
```

The old `setup_foundation_lite.py` remains for reference but is **deprecated**.

### New Features in v3.0.0

#### Preset Selection

```bash
# Minimal (5 principles)
python generate_foundation.py --preset minimal --project-name "My Project" --author-name "Name"

# Standard (15 principles) - Default
python generate_foundation.py --preset standard --project-name "My Project" --author-name "Name"

# Enterprise (23 principles)
python generate_foundation.py --preset enterprise --project-name "My Project" --author-name "Name"
```

#### Discovery Commands

```bash
python generate_foundation.py --list-presets      # Show available presets
python generate_foundation.py --list-principles   # Show available principles
python generate_foundation.py --list-guides       # Show available guides
```

#### Plugin Support (v2.11.0+)

```bash
python generate_foundation.py --plugins-dir ./my-plugins --project-name "My Project" --author-name "Name"
```

### v3.0.0 Migration Checklist

- [ ] Update scripts: `setup_foundation_lite.py` → `generate_foundation.py`
- [ ] Review preset options (may simplify your command line)
- [ ] Update CI/CD pipelines referencing old entrypoint
- [ ] Test with existing configuration files

### Backward Compatibility

All v2.x command-line arguments remain supported:
`--project-name`, `--author-name`, `--output-dir`, `--license`, `--all`, `--coc`, `--security`, `--enhanced-security`, `--secrets-detection`, `--changelog`, `--issue-templates`, `--pr-template`, `--adr`, `--ci-workflow`, `--non-interactive`, `--accept-terms`, `--config`, `--export-json`

### Config File Updates

Configuration files now support preset selection:

```json
{
  "project_name": "My Project",
  "author_name": "Author",
  "preset": "standard",
  "plugins_dir": "./plugins"
}
```

---

## Historical Context

This section documents the original transition from enterprise to lite edition.

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

### 23 Governance Principles (All Available in v2.10.0+)

| Category | Principles | Version |
|----------|------------|---------|
| Core | readme, contributing, license | v2.1.0 |
| Governance | code-of-conduct, security | v2.1.0 |
| Security | enhanced-security, secrets-detection | v2.4.0 |
| Community | issue-templates, pr-template, changelog | v2.3.0 |
| Advanced | adr, ci-workflow | v2.5.0 |
| Quality | quality-assurance, code-standards, performance-standards | v2.10.0 |
| Compliance | compliance-policy, audit-logging | v2.10.0 |
| Infrastructure | versioning, dependency-scanning, container-support | v2.10.0 |
| Inclusivity | internationalization, accessibility | v2.10.0 |
| Lifecycle | deprecation-policy | v2.10.0 |

### 15 Implementation Guides (All Available in v2.10.0+)

| Category | Guides | Version |
|----------|--------|---------|
| Governance | versioning, release-process, changelog, compliance-guide | v2.9.0-v2.10.0 |
| Development | code-review, adr, test-strategies, coding-standards, api-standards | v2.9.0-v2.10.0 |
| Security | security-disclosure | v2.9.0 |
| Onboarding | onboarding, glossary, faq, troubleshooting | v2.10.0 |
| Operations | dependency-guide | v2.10.0 |

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

## Waiting for Feature Reintroduction

If you need features not yet available in the lite edition, we recommend waiting for their official reintroduction. Each version adds features with full educational context, ensuring:

- You get tested, documented features
- Educational content explains proper use
- Community feedback has refined the implementation
- Ethical safeguards are maintained

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
