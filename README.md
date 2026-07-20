# Project Foundation Template (PFT)

**Educational templates for thoughtful software governance**

> **Governance**: The policies, processes, and documentation that guide project development, maintenance, and contributions. This includes contribution guidelines, security policies, codes of conduct, and architectural decision records. See [GLOSSARY.md](GLOSSARY.md) for more terms.

---

## What is This?

PFT helps you create well-organized projects with the right governance for your needs. Whether you're starting a personal project, launching open source software, or establishing enterprise-grade governance, this tool generates the foundational files you need while teaching you *why* each piece matters.

**Core Philosophy**: Education First — understand WHY before HOW.

### Who is This For?

| You Are... | This Helps You... |
|------------|-------------------|
| **New Developer** | Learn project governance best practices |
| **Open Source Maintainer** | Set up professional project structure quickly |
| **Team Lead** | Establish consistent governance across projects |
| **Organization** | Scale governance standards while maintaining flexibility |
| **AI/LLM User** | Generate well-structured project foundations programmatically |

### Key Concepts

#### Education First

Every template teaches before it generates:
- **WHAT**: What is this file/principle?
- **WHY**: Why does it matter?
- **HOW**: How do you implement it?
- **RISK**: What happens without it?

#### Principle Zero: "Do No Harm, Allow No Harm"

This project is built on an ethical foundation. We don't just generate files — we help you understand governance so you can implement it meaningfully.

Ethical review requirements scale based on a project's relationship to PFT:
- **Tier 1** (Core components): Full ethical review required
- **Tier 2** (Generated instances): Simplified review recommended
- **Tier 3** (Ecosystem coordinators): Inherit principles, lighter process

See [ETHICS.md](ETHICS.md) for the complete ethical framework and review templates.

#### Templates vs. Implementation

Templates are starting points, not finished products. Every generated file requires:
- Review and customization
- Understanding of its purpose
- Ongoing maintenance

### This Is Not

- A compliance shortcut (templates require understanding and customization)
- Instant security certification (security requires ongoing effort)
- A substitute for professional judgment (consult experts for legal/security matters)
- Copy-paste governance theater (files without understanding provide false confidence)

---

## Quick Start

### For New Users (Interactive Learning Mode)

```bash
python setup_foundation.py --project-name "MyProject" --author-name "Your Name"
```

This walks you through each decision, explaining what each file does and why it matters.

### For Experienced Users (Preset Selection)

```bash
# Choose your governance level
python setup_foundation.py --preset minimal --project-name "MyProject" --author-name "Your Name"
python setup_foundation.py --preset standard --project-name "MyProject" --author-name "Your Name"  # Default
python setup_foundation.py --preset enterprise --project-name "MyProject" --author-name "Your Name"
```

### For CI/CD Pipelines

```bash
python setup_foundation.py --non-interactive --accept-terms --preset standard \
  --project-name "MyProject" --author-name "Your Name" --output-dir ./output
```

### Discover Available Options

```bash
python setup_foundation.py --list-presets      # Show all governance presets
python setup_foundation.py --list-principles   # Show all 30 principles
python setup_foundation.py --list-guides       # Show all 25 implementation guides
```

---

## Governance Presets

Choose the level of governance that matches your project's needs:

| Preset | Principles | Best For |
|--------|------------|----------|
| **minimal** | 3 | Personal projects, prototypes, learning exercises |
| **light** | 6 | Small open source projects, basic governance needs |
| **standard** | 9 | Active open source projects, professional teams (Default) |
| **strict** | 12 | Security-sensitive projects, compliance requirements |
| **enterprise** | 30 | Large organizations, regulated industries, maximum governance |

### What Each Preset Includes

```
minimal (3)     → README + CONTRIBUTING + LICENSE
    ↓ adds
light (6)       → Code of Conduct + Security Policy + Changelog
    ↓ adds
standard (9)    → Issue Templates + PR Template + CI Workflow
    ↓ adds
strict (12)     → Enhanced Security + Secrets Detection + ADR
    ↓ adds
enterprise (30) → Quality + Compliance + Infrastructure + Inclusivity + Lifecycle + Workflow + Tooling
```

---

## The 30 Governance Principles

Every principle includes **WHAT** (definition), **WHY** (importance), and **RISK** (what happens without it).

### Core (Always Included)
| Principle | Purpose |
|-----------|---------|
| `readme` | Project overview and getting started |
| `contributing` | How to contribute to the project |
| `license` | Legal terms for using the code |

### Governance
| Principle | Purpose |
|-----------|---------|
| `code-of-conduct` | Community behavior standards |
| `security` | Vulnerability reporting process |

### Security
| Principle | Purpose |
|-----------|---------|
| `enhanced-security` | Comprehensive security policies |
| `secrets-detection` | Prevent credential leaks via pre-commit hooks |

### Community
| Principle | Purpose |
|-----------|---------|
| `issue-templates` | Structured bug reports and feature requests |
| `pr-template` | Consistent pull request descriptions |
| `changelog` | Track changes across versions |

### Advanced
| Principle | Purpose |
|-----------|---------|
| `adr` | Document architectural decisions |
| `ci-workflow` | Automated testing with GitHub Actions |

### Quality
| Principle | Purpose |
|-----------|---------|
| `quality-assurance` | Testing and quality standards |
| `code-standards` | Coding style and conventions |
| `performance-standards` | Performance requirements and monitoring |

### Compliance
| Principle | Purpose |
|-----------|---------|
| `compliance-policy` | Regulatory compliance framework |
| `audit-logging` | Audit trail requirements |

### Infrastructure
| Principle | Purpose |
|-----------|---------|
| `versioning` | Semantic versioning practices |
| `dependency-scanning` | Dependency vulnerability monitoring |
| `container-support` | Docker and containerization standards |

### Inclusivity
| Principle | Purpose |
|-----------|---------|
| `internationalization` | Multi-language support (i18n) |
| `accessibility` | Accessibility standards (a11y) |

### Lifecycle
| Principle | Purpose |
|-----------|---------|
| `deprecation-policy` | How features are deprecated and removed |

### Documentation (v3.1.0+)
| Principle | Purpose |
|-----------|---------|
| `glossary` | Project terminology definitions |
| `maintainers` | Maintainer roles and responsibilities |

### Workflow (v3.3.0+)
| Principle | Purpose |
|-----------|---------|
| `roadmap` | Project direction and planning |
| `branch-naming` | Consistent branch naming conventions |
| `conventional-commits` | Structured commit messages |

### Tooling (v3.4.0+)
| Principle | Purpose |
|-----------|---------|
| `pre-commit-hooks` | Automated code quality checks |
| `error-handling` | Consistent error handling patterns |

---

## Project Structure

```
project-foundation-template/
│
├── setup_foundation.py          # Main entry point (v3.0.0)
├── setup_foundation_lite.py     # Legacy entry point (deprecated)
│
├── core/                        # Core modules
│   ├── __init__.py             # Package exports
│   ├── config.py               # Configuration management
│   ├── education.py            # Educational content
│   ├── ethics.py               # Ethical safeguards
│   ├── generator.py            # File generation engine
│   ├── utils.py                # Utility functions
│   │
│   ├── principles/             # 30 Governance Principles
│   │   ├── __init__.py         # Principle aggregation
│   │   ├── readme.py           # README principle
│   │   ├── contributing.py     # Contributing principle
│   │   ├── license.py          # License principle
│   │   └── ...                 # (27 more principles)
│   │
│   ├── guides/                 # 25 Implementation Guides
│   │   ├── __init__.py         # Guide aggregation
│   │   ├── versioning.py       # Versioning guide
│   │   ├── code_review.py      # Code review guide
│   │   └── ...                 # (23 more guides)
│   │
│   ├── presets/                # Governance Presets
│   │   ├── __init__.py         # Preset aggregation
│   │   ├── minimal.py          # 3 principles
│   │   ├── light.py            # 6 principles
│   │   ├── standard.py         # 9 principles (default)
│   │   ├── strict.py           # 12 principles
│   │   └── enterprise.py       # 30 principles
│   │
│   └── plugins/                # Plugin System
│       ├── __init__.py         # Plugin API
│       ├── base.py             # Base classes
│       ├── loader.py           # Plugin discovery
│       └── validator.py        # Plugin validation
│
├── templates/                   # Generated file templates
│   ├── markdown/               # Documentation templates
│   ├── workflows/              # GitHub Actions templates
│   └── configs/                # Configuration templates
│
├── tests/                       # Test suite
│   ├── test_foundation_*.py    # Core module tests
│   └── ...
│
├── docs/                        # Documentation
│   ├── adr/                    # Architecture Decision Records
│   │   └── 0001-education-first.md
│   └── guides/                 # Implementation guides
│
├── CLAUDE.md                    # LLM integration guidance
├── ETHICS.md                    # Ethical framework
├── ROADMAP.md                   # Version roadmap
├── MIGRATION.md                 # Migration guide
├── CONTRIBUTING.md              # How to contribute
├── CHANGELOG.md                 # Version history
├── SECURITY.md                  # Security policy
├── CODE_OF_CONDUCT.md          # Community standards
└── LICENSE                      # Apache 2.0
```

---

## Documentation

| Document | Purpose |
|----------|---------|
| [CLAUDE.md](CLAUDE.md) | LLM/AI integration guidance |
| [ETHICS.md](ETHICS.md) | Ethical framework and Principle Zero |
| [GLOSSARY.md](GLOSSARY.md) | PFT terminology definitions |
| [ROADMAP.md](ROADMAP.md) | Version roadmap and future plans |
| [MIGRATION.md](MIGRATION.md) | Upgrading between versions |
| [CONTRIBUTING.md](CONTRIBUTING.md) | How to contribute |
| [CHANGELOG.md](CHANGELOG.md) | Version history |
| [SEMANTIC_VERSIONING.md](SEMANTIC_VERSIONING.md) | Versioning policy |
| [docs/adr/](docs/adr/) | Architecture Decision Records |

---

## Extending with Plugins

Create custom principles and guides for your organization:

```bash
# Use plugins from a custom directory
python setup_foundation.py --plugins-dir ./my-plugins --project-name "MyProject" --author-name "Your Name"
```

See [core/plugins/examples/](core/plugins/examples/) for plugin examples.

---

## Version History

| Version | Highlights |
|---------|------------|
| v3.7.0 | Generation log, attribution policy, tiered ethical review |
| v3.6.0 | Internationalization support (10 locales) |
| v3.5.0 | Programming language support infrastructure (17 languages) |
| v3.4.0 | Advanced features - 30 principles, 25 guides |
| v3.3.0 | Extended governance principles (28 total) |
| v3.2.0 | Developer documentation guides |
| v3.1.0 | Accessibility & usability features (25 principles) |
| v3.0.0 | New entrypoint, 23 principles, 15 guides, plugin system |
| v2.x | Modular architecture, presets, educational content |
| v1.x | Initial implementation |

See [CHANGELOG.md](CHANGELOG.md) for complete history.

---

## Contributing

We welcome contributions! See [CONTRIBUTING.md](CONTRIBUTING.md) for:
- Fork-first workflow
- Branch naming conventions
- Conventional commits
- Educational review criteria

---

## License

Licensed under the Apache License, Version 2.0. See [LICENSE](LICENSE) for details.

---

## Acknowledgments

This framework emerged from collaborative work between human and AI, embodying the principle of **Mutual Fallibility** — both parties have cognitive biases and benefit from structured verification protocols.

---

**Version**: 3.7.0
**Status**: Active Development
**Repository**: [GitHub](https://github.com/malcolmhoward/project-foundation-template)
