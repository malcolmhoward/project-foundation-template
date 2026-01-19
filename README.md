# Project Foundation Template

*Educational templates for thoughtful software governance*

## Philosophy

This project believes that good governance starts with understanding, not automation. We generate templates that teach best practices while providing starting points for project governance.

**Core Principle**: Education First - understand WHY before HOW.

## Features

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

### v2.6.0 - Stabilization & Testability
- Modular `core/` package structure
- Extracted config, education, and template modules
- 83 unit tests for better maintainability

### v2.7.0 - Governance Presets
- `--preset` flag with 5 governance levels (minimal, light, standard, strict, enterprise)
- Progressive governance adoption
- Preset-specific principle selection

## What Makes This Different

Every template:
- 📚 Explains WHY it matters before generating
- ⚠️ Shows risks of not having it
- 📝 Requires customization (not copy-paste ready)
- 🎓 Teaches governance principles

## This Is Not

- ❌ A compliance shortcut
- ❌ Instant security certification
- ❌ A substitute for professional judgment
- ❌ Copy-paste governance theater

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

- [ETHICS.md](ETHICS.md) - Ethical framework and Principle Zero
- [CONTRIBUTING.md](CONTRIBUTING.md) - How to contribute
- [ROADMAP.md](ROADMAP.md) - Version roadmap to v3.0.0
- [CHANGELOG.md](CHANGELOG.md) - Version history
- [docs/adr/](docs/adr/) - Architecture Decision Records

## License

Licensed under the Apache License, Version 2.0. See [LICENSE](LICENSE) for details.

## Acknowledgments

This framework emerged from collaborative work between human and AI, embodying the principle of **Mutual Fallibility** - that both parties have cognitive biases and benefit from structured verification protocols.

---

**Version**: 2.7.0
**Status**: Active development
**Repository**: [GitHub](https://github.com/malcolmhoward/project-foundation-template)
