# Project Foundation Template

*Educational templates for thoughtful software governance*

## Core Principle

**Education First** — understand WHY before HOW.

Good governance starts with understanding, not automation. We generate templates that teach best practices while providing starting points for project governance.

## Ethical Foundation

This project is built on **Principle Zero: "Do no harm, allow no harm."**

We recognize that governance templates can be misused:
- To create false impressions of security
- To exploit trust through professional-looking facades
- To claim compliance without implementation

Our safeguards ensure templates are used ethically and responsibly.

## Generator Output

> **Note**: This section describes what the `setup_foundation_lite.py` tool generates for **your projects**. For this repository's own documentation (ETHICS.md, ROADMAP.md, etc.), see the [Documentation](#documentation) section below.

### Core Templates (v2.1.0)
- **README.md** - Project documentation with educational comments
- **CONTRIBUTING.md** - Contribution guidelines
- **LICENSE** - License selection (MIT, Apache, GPL)
- **CODE_OF_CONDUCT.md** - Community standards (optional)
- **SECURITY.md** - Basic security policy (optional)
- **.gitignore** - Standard ignore patterns

### v2.2.0 - Core Infrastructure
- `--non-interactive` mode for CI/CD pipelines
- `.foundationrc` configuration file support
- `--export-json` for machine-readable output
- `--quiet` mode for minimal output
- Educational error messages with guidance

### v2.3.0 - Community Governance
- `--include-github-templates` - Issue and PR templates
- `--include-changelog` - Keep a Changelog format
- `--all` flag for all optional templates

### v2.4.0 - Security Features
- `--include-enhanced-security` - Comprehensive SECURITY.md
- `--include-secrets-detection` - Pre-commit hooks for secret scanning

### v2.5.0 - Advanced Governance
- `--include-adr` - Architecture Decision Records
- `--include-ci` - GitHub Actions CI workflow

## Philosophy

Every template:
- 📚 Explains **WHY** it matters (Education First)
- ⚠️ Shows what happens **without** it (Risk Awareness)
- 📝 **Requires customization** (No Copy-Paste)
- 🎓 **Teaches while generating** (Learning, Not Just Output)

## This Is Not

- ❌ A compliance shortcut — templates require implementation
- ❌ Instant security — security is practice, not documentation
- ❌ A substitute for judgment — you must think critically
- ❌ Copy-paste governance — customization is required

## Ethical Safeguards

To prevent misuse, this tool includes:
- **Ethical Use Agreement** — explicit acknowledgment of responsibilities
- **Educational Content** — mandatory learning before generating
- **Template Warnings** — clear notices that customization is required
- **Version Expiration** — encourages staying current with best practices

## Getting Started

### Interactive Mode (Recommended for Learning)
```bash
python setup_foundation_lite.py --project-name "MyProject" --author-name "Your Name"
```

### Non-Interactive Mode (CI/CD)
```bash
python setup_foundation_lite.py --non-interactive --accept-terms \
  --project-name "MyProject" --author-name "Your Name" --all
```

### Using Config File
```json
// .foundationrc
{
  "project_name": "MyProject",
  "author_name": "Your Name",
  "license": "mit",
  "include_coc": true,
  "include_security": true
}
```
```bash
python setup_foundation_lite.py --non-interactive --accept-terms
```

## Documentation

This repository's own governance documentation:

- [ETHICS.md](ETHICS.md) - Ethical framework and Principle Zero
- [CONTRIBUTING.md](CONTRIBUTING.md) - How to contribute to this project
- [ROADMAP.md](ROADMAP.md) - Version roadmap to v3.0.0
- [CHANGELOG.md](CHANGELOG.md) - Version history
- [CLAUDE.md](CLAUDE.md) - LLM integration guidance
- [docs/adr/](docs/adr/) - Architecture Decision Records

## License

Licensed under the Apache License, Version 2.0. See [LICENSE](LICENSE) for details.

## Acknowledgments

This framework emerged from collaborative work between human and AI, embodying the principle of **Mutual Fallibility** - that both parties have cognitive biases and benefit from structured verification protocols.

---

**Version**: 2.5.0-lite
**Status**: Active development
**Repository**: [GitHub](https://github.com/malcolmhoward/project-foundation-template)
