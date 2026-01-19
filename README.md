# Project Foundation Template

**Educational templates for thoughtful software governance**

---

## What is This?

Project Foundation Template helps you create well-organized projects with the right governance for your needs. Whether you're starting a personal project, launching open source software, or establishing enterprise-grade governance, this tool generates the foundational files you need while teaching you *why* each piece matters.

---

## Ethical Foundation

This project is built on a fundamental principle:

> **Principle Zero: "Do No Harm, Allow No Harm"**

We believe governance templates carry responsibility. Unlike tools that prioritize speed over understanding, Project Foundation Template:

- **Teaches before it generates** — Every template explains WHAT it is, WHY it matters, and the RISK of not having it
- **Requires acknowledgment** — Users must understand that templates are starting points, not finished products
- **Prevents misuse** — We intentionally limit features that could enable governance theater or mass automation
- **Expires gracefully** — Advisory dates prompt users to check for updates rather than running outdated governance

This framework emerged from collaborative work between human and AI, embodying the principle of **Mutual Fallibility** — recognizing that both parties have cognitive biases and benefit from structured verification.

See [ETHICS.md](ETHICS.md) for our complete ethical framework.

---

## Who is This For?

| You Are... | This Helps You... |
|------------|-------------------|
| **New Developer** | Learn project governance best practices |
| **Open Source Maintainer** | Set up professional project structure quickly |
| **Team Lead** | Establish consistent governance across projects |
| **Organization** | Scale governance standards while maintaining flexibility |
| **AI/LLM User** | Generate well-structured project foundations programmatically |

---

## Quick Start

### Scenario 1: New Project (Interactive Learning)

Create a new project directory and generate governance files directly into it:

```bash
# Create and enter your project directory
mkdir my-new-project && cd my-new-project

# Run PFT from its location, outputting to current directory
python /path/to/project-foundation-template/setup_foundation.py \
  --project-name "MyProject" \
  --author-name "Your Name" \
  --output-dir .
```

This walks you through each decision, explaining what each file does and why it matters.

### Scenario 2: Existing Project

Add governance to an existing project by targeting its directory:

```bash
# From anywhere, target your existing project
python /path/to/project-foundation-template/setup_foundation.py \
  --project-name "ExistingProject" \
  --author-name "Your Name" \
  --output-dir /path/to/existing-project \
  --preset standard
```

Files are generated into the target directory. Existing files are not overwritten without confirmation.

### Scenario 3: Git Submodule Integration

Embed PFT within your project for version-controlled governance updates:

```bash
# Add PFT as a submodule in your project
cd your-project
git submodule add https://github.com/malcolmhoward/project-foundation-template.git tools/pft

# Generate governance files to your project root
python tools/pft/setup_foundation.py \
  --project-name "YourProject" \
  --author-name "Your Name" \
  --output-dir . \
  --preset standard

# Commit the submodule and generated files
git add .gitmodules tools/pft
git commit -m "Add Project Foundation Template as submodule"
```

Benefits of submodule approach:
- Lock to a specific PFT version
- Update governance templates by updating the submodule
- Keep PFT separate from your project code

### Scenario 4: CI/CD Pipeline Integration

Non-interactive mode for automated environments:

```bash
python setup_foundation.py \
  --non-interactive \
  --accept-terms \
  --preset standard \
  --project-name "MyProject" \
  --author-name "CI Bot" \
  --output-dir ./output
```

### Scenario 5: Monorepo / Multi-Project

Generate governance for multiple projects from a central location:

```bash
# Generate for each project in a monorepo
for project in frontend backend shared; do
  python /path/to/pft/setup_foundation.py \
    --non-interactive \
    --accept-terms \
    --preset light \
    --project-name "$project" \
    --author-name "Team" \
    --output-dir "./packages/$project"
done
```

### Scenario 6: Organization-Wide Standards

Use plugins to enforce organization-specific governance:

```bash
# Create custom plugins in your org's shared location
python setup_foundation.py \
  --plugins-dir /shared/org-governance-plugins \
  --preset enterprise \
  --project-name "CorpProject" \
  --author-name "Enterprise Team" \
  --output-dir ./new-project
```

### Discover Available Options

```bash
python setup_foundation.py --list-presets      # Show all governance presets
python setup_foundation.py --list-principles   # Show all 23 principles
python setup_foundation.py --list-guides       # Show all 15 implementation guides
python setup_foundation.py --help              # Full command reference
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
| **enterprise** | 23 | Large organizations, regulated industries, maximum governance |

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
enterprise (23) → Quality + Compliance + Infrastructure + Inclusivity + Lifecycle
```

---

## The 23 Governance Principles

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
│   ├── principles/             # 23 Governance Principles
│   ├── guides/                 # 15 Implementation Guides
│   ├── presets/                # Governance Presets
│   └── plugins/                # Plugin System
│
├── docs/                        # Documentation
│   ├── adr/                    # Architecture Decision Records
│   └── case-studies/           # Real-world adoption stories
│
├── ETHICS.md                    # Ethical framework (start here)
├── CLAUDE.md                    # LLM integration guidance
├── ROADMAP.md                   # Version roadmap
├── MIGRATION.md                 # Migration guide
├── CONTRIBUTING.md              # How to contribute
├── CHANGELOG.md                 # Version history
└── LICENSE                      # Apache 2.0
```

---

## Documentation

| Document | Purpose |
|----------|---------|
| [ETHICS.md](ETHICS.md) | Ethical framework and Principle Zero |
| [CLAUDE.md](CLAUDE.md) | LLM/AI integration guidance |
| [ROADMAP.md](ROADMAP.md) | Version roadmap and future plans |
| [MIGRATION.md](MIGRATION.md) | Upgrading between versions |
| [CONTRIBUTING.md](CONTRIBUTING.md) | How to contribute |
| [CHANGELOG.md](CHANGELOG.md) | Version history |
| [SEMANTIC_VERSIONING.md](SEMANTIC_VERSIONING.md) | Versioning policy |
| [docs/adr/](docs/adr/) | Architecture Decision Records |
| [docs/case-studies/](docs/case-studies/) | Real-world adoption stories |

---

## Extending with Plugins

Create custom principles and guides for your organization:

```bash
# Use plugins from a custom directory
python setup_foundation.py --plugins-dir ./my-plugins --project-name "MyProject" --author-name "Your Name"
```

See [core/plugins/examples/](core/plugins/examples/) for plugin examples.

---

## This Is Not

- A compliance shortcut (templates require understanding and customization)
- Instant security certification (security requires ongoing effort)
- A substitute for professional judgment (consult experts for legal/security matters)
- Copy-paste governance theater (files without understanding provide false confidence)

---

## Version History

| Version | Highlights |
|---------|------------|
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

**Version**: 3.0.0
**Status**: Active Development
**Repository**: [GitHub](https://github.com/malcolmhoward/project-foundation-template)
