# CLAUDE.md - LLM Integration Guide

## Project Overview

**Project Foundation Template** is an educational template generator for thoughtful software governance. It prioritizes teaching best practices over automation shortcuts.

## Core Philosophy

### Principle Zero: "Do No Harm, Allow No Harm"
Inspired by GAIA from Horizon Zero Dawn. Harm prevention is the **primary design constraint**, not an advisory layer. All decisions flow from this principle.

### Educational-First Approach
- **WHAT** before **WHY** before **HOW**
- Templates teach, not automate
- Understanding matters more than speed

### The Ouroboros Architecture
This template can generate governance for any project—including instances that coordinate other projects using this same template. This is **beneficial recursive improvement**, not circular dependency.

## Key Files

| File | Purpose |
|------|---------|
| `generate_foundation.py` | Main entrypoint (v3.0.0) |
| `setup_foundation_lite.py` | Legacy entrypoint (deprecated) |
| `core/` | Modular core package |
| `ETHICS.md` | Ethical framework and safeguards |
| `ROADMAP.md` | Version roadmap |
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

## Governance Presets (Roadmap)

| Preset | Principles | Version |
|--------|------------|---------|
| minimal | ~5 core | v2.2.0 (current) |
| light | ~10 | v2.3.0 |
| standard | ~15 | v2.4.0 |
| strict | ~20 | v2.5.0 |
| enterprise | All 23 | v3.0.0 |

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

- **Current**: v3.0.0
- **Advisory Expiration**: Check `generate_foundation.py` for current date
- **Architecture**: Modular core with plugin support
