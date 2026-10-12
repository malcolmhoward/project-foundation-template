# CLAUDE.md - LLM Integration Guide

## Project Overview

**Project Foundation Template** is an educational template generator for thoughtful software governance. It prioritizes teaching best practices over automation shortcuts.

## Core Philosophy

### Principle Zero: "Do No Harm, Allow No Harm"
Inspired by GAIA from [Horizon Zero Dawn®](https://www.playstation.com/games/horizon-zero-dawn/). Harm prevention is the **primary design constraint**, not an advisory layer. All decisions flow from this principle.

> *Horizon Zero Dawn is a registered trademark of Sony Interactive Entertainment ([Trademark Notice](https://sonyinteractive.com/en/copyright-and-trademark-notice/)). This project is not affiliated with or endorsed by Sony Interactive Entertainment or Guerrilla Games.*

### Educational-First Approach
- **WHAT** before **WHY** before **HOW**
- Templates teach, not automate
- Understanding matters more than speed

### The Ouroboros Architecture
This template can generate governance for any project—including instances that coordinate other projects using this same template. This is **beneficial recursive improvement**, not circular dependency.

## Key Files

| File | Purpose |
|------|---------|
| `generate_foundation.py` | Main entrypoint |
| `core/principles/` | 30 governance principles |
| `core/guides/` | 25 implementation guides |
| `core/presets/` | Governance presets (minimal to enterprise) |
| `core/programming_languages/` | 17 language configurations (v3.5.0) |
| `core/internationalization/` | 10 locale configurations (v3.6.0) |
| `ETHICS.md` | Ethical framework and safeguards |
| `GLOSSARY.md` | PFT terminology definitions |
| `docs/adr/` | Architecture Decision Records |

## Working with This Codebase

### When Modifying the Generator
1. Preserve all ethical safeguards (agreement, education, logging, warnings, expiration)
2. Maintain the WHAT/WHY/HOW educational pattern
3. Test generated output against ethical guidelines
4. Update version and expiration date appropriately

### When Adding Features
Evaluate proposed features using priority assessment:
- **Priority**: High / Medium / Low
- **Impact**: Who benefits and how significantly?
- **Effort**: Rough estimate of implementation complexity
- **Risk**: What could go wrong?
- **Alignment**: Does it support the educational mission?

Features should have clear educational value and align with Principle Zero.

### Identified Risks to Avoid
1. **Governance Theater** - Appearance of compliance without substance
2. **AI Exploitation** - Mass repo pollution, supply chain attacks
3. **Environmental Impact** - Unnecessary CI/CD carbon footprint
4. **Social Engineering** - Professional-looking repos for scams
5. **Legal Exploitation** - Templates misrepresented as actual compliance

## Governance Presets

| Preset | Principles | Best For |
|--------|------------|----------|
| minimal | 3 | Personal projects, prototypes |
| light | 6 | Small open source projects |
| standard | 9 | Active open source projects (Default) |
| strict | 12 | Security-sensitive projects |
| enterprise | 30 | Large organizations, regulated industries |

## Commands

```bash
# Run the generator (v3.0.0)
python generate_foundation.py --project-name "MyProject" --author-name "Author" --output-dir ./output

# With preset selection
python generate_foundation.py --preset standard --project-name "MyProject" --author-name "Author"

# Discovery commands
python generate_foundation.py --list-presets
python generate_foundation.py --list-principles
python generate_foundation.py --list-guides

# Test generated output
ls -la ./output/
```

## Contribution Guidelines

1. **Fork-first workflow** - All changes via fork and PR
2. **Conventional commits** - `type(scope): description`
3. **Educational review** - PRs must explain the WHY
4. **Ethical pause** - Consider implications before merging

## Version Information

- **Current**: v3.6.0
- **Advisory Expiration**: Check `generate_foundation.py` for current date
- **Architecture**: Modular core with plugin support
- **Principles**: 30 governance principles
- **Guides**: 25 implementation guides
- **Languages**: 17 programming language configurations
- **Locales**: 10 internationalization configurations
