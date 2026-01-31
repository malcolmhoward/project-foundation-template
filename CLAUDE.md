# CLAUDE.md - LLM Integration Guide

## Project Overview

**Project Foundation Template** is an educational template generator for thoughtful software governance. It prioritizes teaching best practices over automation shortcuts.

---

## Critical: Agentic Safety Guidelines

### Command Execution Security Review

**Before executing ANY command**, review for these risks:

1. **Secret Exposure via Terminal Output**
   - Commands that dump environment variables (`env`, `printenv`, `set`)
   - Commands that read secret files (`cat ~/.ssh/*`, `cat .env`)
   - API calls that include tokens in verbose output
   - Git commands that might expose credentials in remotes

2. **Secret Exposure to the Model**
   - File reads that might contain credentials
   - Database queries that return sensitive data
   - Log files that contain tokens or passwords

3. **Destructive Operations**
   - `rm -rf`, `git reset --hard`, `git push --force`
   - Database truncation or deletion
   - Overwriting files without backup

**Mitigation**: When in doubt, ask the user before executing. Prefer read-only operations for exploration.

### Context Preservation via Orchestrator + Sub-agent Pattern

**Problem**: Long sessions cause "context rot" — accumulated blind spots and lost awareness of earlier details.

**Solution**: Use the root session as an orchestrator; delegate focused tasks to sub-agents:

```
Root Session (Orchestrator):
├── Define high-level goal
├── Launch Sub-agent 1: "Specific focused task"
├── Launch Sub-agent 2: "Another focused task"
├── Launch Sub-agent 3: "Verification task"
└── Synthesize results and report to user
```

**When to use sub-agents**:
- Complex multi-step operations (rebases, bulk updates)
- Tasks requiring fresh context (no accumulated assumptions)
- Verification after changes (independent check)
- Parallel exploration of different approaches

**Benefits**:
| Problem | Solution |
|---------|----------|
| Context rot during long sessions | Fresh context per sub-agent |
| Accumulated blind spots | Each agent focuses on one task |
| Lost awareness of details | Explicit documentation before changes |
| Silent regressions | Dedicated verification step |

See `scripts/bulk-operations/safe-pr-chain-rebase.md` for a detailed example pattern.

---

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
| `core/generation_log.py` | Generation log tracking (v3.7.0) |
| `ETHICS.md` | Ethical framework and safeguards |
| `ACKNOWLEDGMENTS.md` | Feature inspiration credits (v3.7.0) |
| `GLOSSARY.md` | PFT terminology definitions |
| `docs/adr/` | Architecture Decision Records |

## Working with This Codebase

### Parallelization Guidance

When working on multi-file tasks, **always consider parallelization**:
- **Identify independent operations** - File reads, writes, and tool calls that don't depend on each other
- **Batch parallel operations** - Make multiple tool calls in a single message when operations are independent
- **Sequential when necessary** - Only serialize operations that have true dependencies

**Examples of parallelizable work:**
- Reading multiple files simultaneously
- Creating multiple new files at once
- Running independent tests or validations
- Updating unrelated sections of different files

**Examples requiring sequential execution:**
- Reading a file before editing it
- Creating a directory before writing files into it
- Validating output after a build step

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

### Script Reusability Evaluation

When creating scripts during implementation work, evaluate whether they could be:
- Added to PFT as optional generation features (if governance-related)
- Added to your project's coordination utilities (if ecosystem-related)
- Documented as reusable patterns in ADRs
- Generalized for broader applicability

Before committing one-off scripts, ask: "Could this help other projects?"

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
# Run the generator (v3.7.0)
python generate_foundation.py --project-name "MyProject" --author-name "Author" --output-dir ./output

# With preset selection
python generate_foundation.py --preset standard --project-name "MyProject" --author-name "Author"

# With generation log tracking (v3.7.0)
python generate_foundation.py --project-name "MyProject" --author-name "Author" --include-generation-log
python generate_foundation.py --project-name "MyProject" --author-name "Author" --include-generation-log --log-format both
python generate_foundation.py --project-name "MyProject" --author-name "Author" --include-generation-log --log-to ./GENERATION_LOG.md

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

- **Current**: v3.7.0
- **Advisory Expiration**: Check `generate_foundation.py` for current date
- **Architecture**: Modular core with plugin support
- **Principles**: 30 governance principles
- **Guides**: 25 implementation guides
- **Languages**: 17 programming language configurations
- **Locales**: 10 internationalization configurations
- **Generation Log**: Tracks file provenance (md/json/both formats)
