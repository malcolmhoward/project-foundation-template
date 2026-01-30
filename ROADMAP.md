# Roadmap to v3.0.0

This document outlines the planned evolution of Project Foundation Template from the current lite edition to the full modular architecture.

## Philosophy

Features are reintroduced gradually with:
1. **Educational context** - WHAT/WHY/HOW for each feature
2. **Priority assessment** - Evaluation of impact, effort, and risk
3. **Ethical review** - Principle Zero compliance
4. **Community feedback** - Time for testing and refinement

## Current State: v2.6.0 (Stabilization & Testability)

**Milestone Achievement**: Modular package architecture with comprehensive test suite.

**Available Features:**
- 13 governance principles (core + community + security + advanced)
- Ethical safeguards (agreement, education, logging, warnings, expiration)
- Modular `foundation` package with 9 modules
- 83 unit tests across 5 test files
- Non-interactive mode with config file support
- GitHub templates (issues, PRs, workflows)
- ADR system
- Secrets detection

**Package Structure (v2.6.0):**
```
core/
├── __init__.py             # Package exports
├── utils.py                # Constants and helpers
├── config.py               # Configuration and argument parsing
├── education.py            # 13 principles and educational content
└── templates/
    ├── core.py             # README, CONTRIBUTING, LICENSE, .gitignore
    ├── governance.py       # CoC, SECURITY, CHANGELOG
    ├── github.py           # Issue templates, PR template, workflows
    └── advanced.py         # ADR, secrets detection, enhanced security
```

**Principles Included (13):**
1. README Documentation
2. Contribution Guidelines
3. License Selection
4. Code of Conduct
5. Security Basics
6. Issue Templates (v2.3.0)
7. PR Template (v2.3.0)
8. Changelog (v2.3.0)
9. Enhanced Security (v2.4.0)
10. Secrets Detection (v2.4.0)
11. ADR System (v2.5.0)
12. CI Workflow (v2.5.0)
13. PR Validation (v2.5.0)

**Test Coverage:**
| Test File | Tests | Coverage |
|-----------|-------|----------|
| test_smoke.py | 19 | Integration |
| test_foundation_utils.py | 8 | Utils module |
| test_foundation_config.py | 16 | Config module |
| test_foundation_education.py | 16 | Education module |
| test_foundation_templates.py | 24 | Templates package |
| **Total** | **83** | ~75% estimated |

---

## Version 2.2.x - Core Infrastructure

**Target**: Improved developer experience without adding governance complexity

### Features

| Feature | Description | Priority |
|---------|-------------|----------|
| `--non-interactive` mode | Scripted/CI usage support | High |
| Configuration files | `.foundationrc` support | High |
| JSON export | Machine-readable output | High |
| Improved error messages | Educational error handling | Medium |

### Rationale

These features don't add governance principles but make the tool more usable for advanced users while maintaining educational focus.

### Release Criteria
- [ ] All features pass Principle Zero review
- [ ] Documentation complete with WHAT/WHY/HOW
- [ ] Backward compatible with v2.1.x
- [ ] Community testing period complete

---

## Version 2.3.x - Community Governance

**Target**: Issue/PR templates and community documentation

### Features

| Feature | Description | Priority |
|---------|-------------|----------|
| Issue templates | Bug reports, feature requests | High |
| PR templates | Standardized contribution format | High |
| Enhanced CONTRIBUTING.md | Comprehensive guide | Medium |
| CHANGELOG.md generation | Release tracking | Medium |
| ROADMAP.md template | Project planning | Medium |

### New Principles (6-10)

| # | Principle | Educational Focus |
|---|-----------|-------------------|
| 6 | Issue Management | How to report and track issues effectively |
| 7 | Pull Request Standards | How to contribute quality code |
| 8 | Changelog Maintenance | Why and how to track changes |
| 9 | Community Guidelines | Building healthy contributor communities |
| 10 | Project Planning | Roadmap creation and maintenance |

### Preset Update

| Preset | Principles |
|--------|------------|
| minimal | 1-5 (unchanged) |
| **light** | **1-10 (new)** |

### Release Criteria
- [ ] Templates tested in real projects
- [ ] Educational content reviewed
- [ ] GitHub integration verified
- [ ] Migration guide updated

---

## Version 2.4.x - Security & Quality

**Target**: Security policies and code quality standards

### Features

| Feature | Description | Priority |
|---------|-------------|----------|
| Advanced security policy | Vulnerability disclosure, scanning | High |
| Secrets detection | Pre-commit hook integration | High |
| Dependency scanning | Outdated/vulnerable dependency alerts | Medium |
| GLOSSARY.md | Terminology definitions | Medium |
| COMPLIANCE.md | Compliance tracking template | Medium |

### New Principles (11-15)

| # | Principle | Educational Focus |
|---|-----------|-------------------|
| 11 | Security Policy (Advanced) | Beyond basics: disclosure, scanning, monitoring |
| 12 | Quality Assurance | Testing strategies and coverage |
| 13 | Code Standards | Linting, formatting, style guides |
| 14 | Versioning Strategy | Semantic versioning in practice |
| 15 | Compliance Tracking | Regulatory and standard compliance |

### Preset Update

| Preset | Principles |
|--------|------------|
| minimal | 1-5 |
| light | 1-10 |
| **standard** | **1-15 (new, becomes default)** |

### Release Criteria
- [ ] Security features don't create false confidence
- [ ] Clear distinction between template and actual security
- [ ] Scanning tools are optional/educational
- [ ] Compliance templates include heavy disclaimers

---

## Version 2.5.x - Advanced Governance

**Target**: CI/CD, architecture decisions, and advanced documentation

### Features

| Feature | Description | Priority |
|---------|-------------|----------|
| GitHub Actions workflows | CI/CD templates | Medium |
| ADR system | Architecture Decision Records | High |
| Branch protection guide | Security recommendations | Medium |
| Release management | Automated release workflows | Medium |
| Full documentation suite | Test strategies, code review, etc. | Medium |

### New Principles (16-20)

| # | Principle | Educational Focus |
|---|-----------|-------------------|
| 16 | CI/CD Pipelines | Continuous integration philosophy |
| 17 | Branch Protection | Git workflow security |
| 18 | Release Management | Version and release automation |
| 19 | Architecture Decisions | ADR creation and maintenance |
| 20 | Documentation System | Comprehensive docs structure |

### New Documentation Modules (1-10)

| # | Module | Focus |
|---|--------|-------|
| 1 | Test Strategies | Testing philosophy and approaches |
| 2 | Code Review Guide | Effective code review |
| 3 | Versioning Guide | SemVer in depth |
| 4 | Release Process | Step-by-step releases |
| 5 | Dependency Guide | Managing dependencies |
| 6 | Internationalization | i18n basics |
| 7 | Audit Logging | Activity tracking |
| 8 | Container Support | Docker fundamentals |
| 9 | API Standards | REST/GraphQL patterns |
| 10 | Security Disclosure | Responsible disclosure |

### Preset Update

| Preset | Principles |
|--------|------------|
| minimal | 1-5 |
| light | 1-10 |
| standard | 1-15 |
| **strict** | **1-20 (new)** |

### Release Criteria
- [ ] CI/CD templates emphasize necessity, not default-on
- [ ] Environmental impact considered
- [ ] ADR system proven useful
- [ ] Documentation modules standalone-useful

---

## Version 3.0.0 - Modular Architecture

**Target**: Full plugin architecture with enterprise feature parity

### Gap Analysis from v2.6.0

The v2.6.0 modularization completed approximately **60% of the v3.0.0 architectural work**:

| Requirement | v2.6.0 Status | Remaining Work |
|-------------|---------------|----------------|
| Modular package | ✅ Complete | Rename `foundation/` → `core/` |
| Config module | ✅ Complete | Minor refactoring |
| Education module | ✅ Complete | Add 10 more principles |
| Template separation | ✅ Complete | Reorganize into `templates/` tree |
| Unit test suite | ✅ Complete (83 tests) | Add integration tests |
| Generator class | 🔄 Partial | Extract from main script |
| Ethics module | ❌ Not started | Extract ethics logic |
| Preset system | ❌ Not started | Create 5 presets |
| Principles directory | ❌ Not started | Split into modules |
| Documentation modules | ❌ Not started | 20 new modules |
| Plugin architecture | ❌ Not started | Dynamic loading |

### Effort Estimate

| Category | Items | Effort | Risk |
|----------|-------|--------|------|
| Low-hanging fruit | Generator extraction, ethics module, package rename | Low | Low |
| Medium investment | Preset system, principles split | Medium | Low |
| High investment | 20 documentation modules, plugin architecture | High | Medium |

**Recommendation**: The hardest architectural decisions are made. Remaining work is primarily content creation and configuration systems.

### Major Changes

1. **Plugin System**: Governance modules as independent plugins
2. **All Presets**: minimal → enterprise all available
3. **Full Principle Set**: All 23 principles with education
4. **Complete Documentation**: All 20 modules
5. **Configuration System**: Advanced customization
6. **Comprehensive Test Suite**: Full unit and integration testing

### Target Architecture

```
project-foundation-template/
├── generate_foundation.py       # Main entry point
├── core/                        # (renamed from foundation/)
│   ├── generator.py            # Base generator class (extracted)
│   ├── config.py               # Configuration management ✅
│   ├── education.py            # Educational content system ✅
│   └── ethics.py               # Ethical safeguards (new)
├── principles/                  # 23 Governance Principles (new)
│   ├── __init__.py
│   ├── readme.py
│   ├── contributing.py
│   ├── license.py
│   ├── code_of_conduct.py
│   ├── security.py
│   └── ... (18 more)
├── modules/                     # 20 Documentation Modules (new)
│   ├── __init__.py
│   ├── test_strategies.py
│   ├── code_review.py
│   └── ... (18 more)
├── presets/                     # Preset configurations (new)
│   ├── minimal.py
│   ├── light.py
│   ├── standard.py
│   ├── strict.py
│   └── enterprise.py
└── templates/                   # (reorganized from foundation/templates/)
    ├── markdown/
    ├── workflows/
    └── configs/
```

### Testing Architecture

The modular architecture enables comprehensive testing:

```
tests/
├── __init__.py
├── conftest.py              # Shared fixtures
├── test_smoke.py            # Basic integration tests (current)
├── unit/                    # Unit tests per module
│   ├── test_generator.py
│   ├── test_config.py
│   ├── test_education.py
│   └── test_ethics.py
├── principles/              # Tests for each principle
│   ├── test_readme.py
│   ├── test_contributing.py
│   └── ...
├── integration/             # End-to-end tests
│   ├── test_presets.py
│   ├── test_workflows.py
│   └── test_full_generation.py
└── fixtures/                # Test data and templates
```

**Testing Philosophy:**
- Each module is independently testable
- Unit tests verify individual components
- Integration tests verify feature combinations
- Smoke tests (v2.5.0) provide basic coverage during development
- CI runs tests on every PR

### Final Principles (21-23)

| # | Principle | Educational Focus |
|---|-----------|-------------------|
| 21 | Deprecation Policy | Managing breaking changes |
| 22 | Accessibility | A11y in documentation and tools |
| 23 | Performance Standards | Performance budgets and monitoring |

### Final Documentation Modules (11-20)

| # | Module | Focus |
|---|--------|-------|
| 11 | Compliance Guide | Regulatory compliance depth |
| 12 | Troubleshooting | Common issues and solutions |
| 13 | FAQ | Frequently asked questions |
| 14 | References | External resources |
| 15 | Glossary | Complete terminology |
| 16 | Onboarding | New contributor guide |
| 17 | Architecture Guide | System design docs |
| 18 | Performance Guide | Optimization strategies |
| 19 | Accessibility Guide | A11y implementation |
| 20 | Deprecation Guide | Managing sunset features |

### Preset Update (Final)

| Preset | Principles | Use Case |
|--------|------------|----------|
| minimal | 1-5 | Learning, personal projects |
| light | 1-10 | Small teams, simple projects |
| standard | 1-15 | Most projects (default) |
| strict | 1-20 | Regulated industries |
| enterprise | 1-23 | Large organizations |

### Release Criteria
- [ ] Plugin system battle-tested
- [ ] Full backward compatibility
- [x] Migration from v2.x documented (MIGRATION.md exists)
- [ ] Performance acceptable
- [x] All ethical safeguards maintained
- [x] Education-first philosophy preserved
- [x] Comprehensive test suite with >80% coverage (83 tests in v2.6.0)
- [x] All tests passing in CI

---

## Post-v3.0.0 Roadmap: Enterprise Feature Parity

Based on gap analysis comparing v3.0.0 against the original ~6,500 line enterprise specification, the following minor versions will address remaining feature gaps while maintaining safety/ethics parity (which is already complete).

### Version 3.1.0 - Accessibility & Usability

**Target**: Address immediate usability gaps identified in audit

| Feature | Description | Priority |
|---------|-------------|----------|
| GLOSSARY.md generation | Generate glossary from existing guide content | High |
| MAINTAINERS.md generation | Project maintainer documentation | Medium |
| SCAFFOLD_MANIFEST.md | Document what was generated | Medium |
| `glossary` principle | Promote guide to full principle with WHAT/WHY/RISK | High |

**Rationale**: These are quick wins that improve accessibility for users of all experience levels.

---

### Version 3.2.0 - Developer Documentation

**Target**: Add missing documentation modules from enterprise spec

| Guide | Description | Priority |
|-------|-------------|----------|
| `developer-handbook` | Complete developer reference | High |
| `architecture-overview` | System architecture documentation | High |
| `deployment-guide` | Deployment instructions | High |
| `contributor-handbook` | Extended contributor guide | Medium |

**Rationale**: These guides provide essential HOW documentation that complements the WHAT/WHY principles.

---

### Version 3.3.0 - Extended Governance Principles

**Target**: Add missing governance principles from enterprise spec

| Principle | Description | Priority |
|-----------|-------------|----------|
| `maintainers` | Project maintainer documentation | Medium |
| `roadmap` | Project planning principle (generate ROADMAP.md) | Medium |
| `branch-naming` | Branch naming conventions | Low |
| `conventional-commits` | Commit message format standards | Low |

**Rationale**: These principles complete the governance suite for stricter compliance needs.

---

### Version 3.4.0 - Advanced Features

**Target**: Additional principles and guides from enterprise spec

| Feature | Type | Description | Priority |
|---------|------|-------------|----------|
| `pre-commit-hooks` | Principle | Enhanced pre-commit automation | Medium |
| `error-handling` | Principle | Standardized error patterns | Low |
| `user-stories` | Guide | User story templates | Low |
| `personas` | Guide | User persona definitions | Low |
| `features` | Guide | Feature documentation templates | Low |
| `contribution-opportunities` | Guide | Ways to contribute | Low |
| `refs` | Guide | External references (REFS.md) | Low |
| `tree-preview` | Guide | Project structure visualization | Low |

**Rationale**: Lower-priority features that complete the enterprise feature set.

---

### Version 3.5.0 - Programming Language Support

**Target**: Add language-specific configurations (18 languages from spec)

| Language Category | Languages | Features |
|-------------------|-----------|----------|
| Top 10 General | Python, JavaScript, TypeScript, Java, C++, C, C#, Go, Rust, PHP | Linter, Formatter, Test Framework |
| Additional | Ruby, Swift, Kotlin, Bash | Same as above |
| Game Development | GDScript, Lua, Haxe | Same as above |

**Per-Language Configuration**:
```python
{
    "extensions": [...],
    "linter": "...",
    "formatter": "...",
    "test_framework": "...",
    "max_line_length": N,
    "indent": N or "tab"
}
```

**Rationale**: Enables language-specific code standards and quality tooling.

---

### Version 3.6.0 - Internationalization

**Target**: Full i18n locale generation

| Feature | Description | Priority |
|---------|-------------|----------|
| Locale structure | Generate `locales/` directory with 10 languages | Medium |
| RTL support | Right-to-left language support (Arabic) | Low |
| Translation templates | JSON/YAML templates for each locale | Medium |

**Supported Locales** (from spec):
- English (en), Spanish (es), French (fr), German (de), Chinese (zh)
- Japanese (ja), Korean (ko), Portuguese (pt), Arabic (ar, RTL), Hindi (hi)

**Rationale**: Enables global reach and accessibility for international projects.

---

### Version 3.7.0 - Generation Log Tracking

**Target**: File provenance documentation and self-governance validation

| Feature | Description | Priority |
|---------|-------------|----------|
| `--include-generation-log` | Track generated files with provenance | High |
| `--log-format` | Support md, json, or both formats | Medium |
| `--log-to` | Custom log file path | Low |
| Dogfooding documentation | Self-governance validation procedure | Medium |

**New Files**:
- `GENERATION_LOG.md` - Markdown provenance tracking
- `GENERATION_LOG.json` - Machine-readable provenance
- `docs/dogfood/README.md` - Dogfooding procedure (PFT-internal)
- `docs/dogfood/DELTA_ANALYSIS.md` - Comparison insights (PFT-internal)

**Rationale**: Enables transparency about auto-generated files and supports template quality validation through self-application.

---

### Version 3.8.0 - Template Improvements (Dogfooding Insights)

**Target**: Template enhancements identified through v3.7.0 dogfooding exercise

| Feature | Type | Description | Priority |
|---------|------|-------------|----------|
| `codeowners` principle | New principle | Generate CODEOWNERS file | High |
| `migration` principle | New principle | Generate MIGRATION.md template | Medium |
| Audience matrix | README pattern | "Who is This For?" section template | High |
| Non-goals section | README pattern | "What This Is Not" clarifications | High |
| Governance section | README pattern | Governance status and adoption roadmap | Medium |
| Commit scopes | CONTRIBUTING pattern | [CUSTOMIZE] scopes table | Medium |
| Educational review | CONTRIBUTING pattern | Project values placeholder | Medium |
| Educational context | PR template pattern | WHY section emphasis | Medium |
| ADR philosophy | ADR README pattern | Decision reasoning guidance | Low |
| `dogfooding` principle | New principle | Opt-in self-validation procedure | Medium |

**New Principles**:

| Principle | Generates | Preset Inclusion |
|-----------|-----------|------------------|
| `codeowners` | `.github/CODEOWNERS` | enterprise (default), opt-in for others |
| `migration` | `MIGRATION.md` | strict, enterprise (default), opt-in for others |
| `dogfooding` | `docs/dogfood/README.md` | opt-in only (for generator/framework projects) |

**Template Pattern Improvements**:
- README: "Who is This For?" audience matrix
- README: "What This Is Not" non-goals section
- README: "Governance" section with adoption status and roadmap
- CONTRIBUTING: [CUSTOMIZE] commit scopes table
- CONTRIBUTING: Project values/ethics placeholder
- PR Template: Educational context (WHY) section
- ADR README: Philosophy paragraph on decision reasoning
- ADR Template: Structured "Change History" table (implemented in v3.7.0)

**Rationale**: Improvements emerged from running PFT against itself. See [ADR-0011](docs/adr/0011-pft-self-governance.md) and [DELTA_ANALYSIS.md](docs/dogfood/DELTA_ANALYSIS.md).

---

### Version 3.9.0 - Multi-Platform & Container Support

**Target**: Documentation patterns for multi-platform projects and containerized applications

**Inspiration**: Patterns observed in a Tier 3 ecosystem project (non-anonymous attribution available upon request)

| Feature | Type | Description | Priority |
|---------|------|-------------|----------|
| `feature-matrix` | New guide | Platform/browser/version compatibility matrix template | High |
| `docker-compose` | New principle | Generate docker-compose.yml with service templates | High |
| `component-readme` | README variant | Component-specific README for monorepo projects | Medium |
| `acknowledgments` | New principle | Generate ACKNOWLEDGMENTS.md for attribution tracking | Medium |

**New Principles**:

| Principle | Generates | Preset Inclusion |
|-----------|-----------|------------------|
| `docker-compose` | `docker-compose.yml`, `DOCKER_README.md` | strict+, opt-in for others |
| `acknowledgments` | `ACKNOWLEDGMENTS.md` | enterprise (default), opt-in for others |

**New Guides**:

| Guide | Purpose | Use Case |
|-------|---------|----------|
| `feature-matrix` | Document feature support across platforms | Multi-platform, cross-browser, API versioning |
| `component-readme` | README template for monorepo components | Monorepo projects with multiple packages |
| `governance-roadmap` | Phased governance adoption planning | Projects adopting governance incrementally |

**Rationale**: Multi-platform and containerized projects need structured ways to document compatibility and orchestration. Patterns inspired by real-world Tier 3 ecosystem adoption.

---

### Version 3.10.0 - Ecosystem & Coordination Patterns

**Target**: Documentation patterns for multi-repo ecosystems and complex project coordination

**Inspiration**: Patterns observed in a Tier 3 ecosystem project (non-anonymous attribution available upon request)

| Feature | Type | Description | Priority |
|---------|------|-------------|----------|
| `cost-analysis` | New guide | Hardware/infrastructure cost comparison template | Medium |
| `hardware-tiers` | New guide | Hardware progression paths and tier recommendations | Medium |
| `monorepo-scripts` | New principle | Cross-repo automation script templates | Medium |
| `documentation-architecture` | New guide | Three-tier docs pattern (portal/coordination/component) | Low |
| `communication-patterns` | New guide | Distributed system communication documentation (MQTT, etc.) | Low |

**New Principles**:

| Principle | Generates | Preset Inclusion |
|-----------|-----------|------------------|
| `monorepo-scripts` | `scripts/for-each-repo.sh`, `scripts/README.md` | enterprise, opt-in for others |

**New Guides**:

| Guide | Purpose | Use Case |
|-------|---------|----------|
| `cost-analysis` | Document build costs, cloud costs, vendor comparisons | Hardware projects, cloud infrastructure |
| `hardware-tiers` | Document hardware progression paths | IoT, embedded, robotics projects |
| `documentation-architecture` | Document three-tier architecture | Large projects with portal + coordination layers |
| `communication-patterns` | Document inter-service communication | Distributed systems, microservices, IoT |

**Rationale**: Complex ecosystems with multiple repositories, hardware platforms, or distributed components need structured coordination documentation. These patterns emerged from observing real-world adoption in sophisticated multi-repo projects.

---

### Version 3.11.0 - Coordination & Research Patterns

**Target**: Documentation patterns for multi-repo coordination, research documentation, and decision frameworks

**Inspiration**: Patterns observed in a Tier 3 ecosystem project (non-anonymous attribution available upon request)

| Feature | Type | Description | Priority |
|---------|------|-------------|----------|
| `meta-issue-tracking` | New guide | Two-tier issue system for multi-repo coordination | High |
| `research-documentation` | New guide | Evaluation criteria, comparison tables, recommendation patterns | Medium |
| `decision-framework` | ADR enhancement | Options comparison, stakeholder section, deferred decisions | High |
| `plan-locally-workflow` | CONTRIBUTING pattern | Draft → implement → refine → publish workflow | Medium |

**New Guides**:

| Guide | Purpose | Use Case |
|-------|---------|----------|
| `meta-issue-tracking` | Document two-tier issue tracking (meta-issues vs tracking references) | Multi-repo ecosystems, coordination layers |
| `research-documentation` | Template for evaluating options with criteria tables and recommendations | Technology selection, library evaluation, architectural decisions |

**ADR Template Enhancements**:

| Enhancement | Description |
|-------------|-------------|
| Options comparison table | Structured pros/cons for each alternative |
| Stakeholder considerations | Section for documenting stakeholder-specific concerns |
| Deferred decisions | Pattern for decisions awaiting stakeholder input |
| Preliminary recommendation | Section for early recommendations pending validation |

**CONTRIBUTING Pattern Enhancements**:

| Enhancement | Description |
|-------------|-------------|
| "Plan Locally First" workflow | Draft issues → local implementation → refine scope → public issue |
| Two-tier issue ownership | Meta-issues (coordination owns) vs tracking references (component owns) |

**Rationale**: Multi-repo coordination requires clear ownership boundaries for issues, structured research documentation for technology decisions, and workflows that allow implementation details to inform issue scope before public commitment.

---

### Gap Analysis Summary

| Category | 6500+ Spec | Current | Gap | Status |
|----------|------------|---------|-----|--------|
| Safety/Ethics | 6 safeguards | 6 safeguards | 0% | ✅ Complete |
| Principles | 23 | 30 | Exceeded | ✅ Complete |
| Guides | 20 | 25 | Exceeded | ✅ Complete |
| Generated Files | 15+ | 15+ | 0% | ✅ Complete |
| Language Support | 18 | 17 | 6% | ✅ v3.5.0 |
| i18n Locales | 10 | 10 | 0% | ✅ v3.6.0 |
| Generation Log | N/A | New feature | N/A | 🔄 v3.7.0 |
| Dogfooding | N/A | New principle | N/A | 📋 v3.8.0 |
| Multi-Platform Docs | N/A | New guides | N/A | 📋 v3.9.0 |
| Ecosystem Coordination | N/A | New guides | N/A | 📋 v3.10.0 |
| Coordination & Research | N/A | New guides + patterns | N/A | 📋 v3.11.0 |

---

## Version History

| Version | Status | Key Achievement |
|---------|--------|-----------------|
| 2.1.x | ✅ Released | Lite edition, ethical safeguards |
| 2.2.x | ✅ Released | Non-interactive mode, config files |
| 2.3.x | ✅ Released | Issue/PR templates, CHANGELOG |
| 2.4.x | ✅ Released | Enhanced security, secrets detection |
| 2.5.x | ✅ Released | ADR system, CI workflows, smoke tests |
| 2.6.0 | ✅ Released | Modular package, 83 unit tests |
| 3.0.0 | ✅ Released | Plugin architecture, 30 principles, 25 guides, 5 presets |
| 3.1.0 | ✅ Released | Accessibility (GLOSSARY generation) |
| 3.2.0 | ✅ Released | Developer documentation guides |
| 3.3.0 | ✅ Released | Extended governance principles |
| 3.4.0 | ✅ Released | Advanced features |
| 3.5.0 | ✅ Released | Programming language support (17 languages) |
| 3.6.0 | ✅ Released | Internationalization (10 locales) |
| 3.7.0 | 🔄 In Progress | Generation log tracking, dogfooding documentation |
| 3.8.0 | 📋 Planned | Template improvements (dogfooding insights) |
| 3.9.0 | 📋 Planned | Multi-platform docs, container support |
| 3.10.0 | 📋 Planned | Ecosystem coordination patterns |
| 3.11.0 | 📋 Planned | Coordination & research patterns |

## Priority Summary

| Version | Risk Level | Complexity | Status |
|---------|------------|------------|--------|
| 2.2.x | Low | Low | ✅ Done |
| 2.3.x | Low | Medium | ✅ Done |
| 2.4.x | Medium | Medium | ✅ Done |
| 2.5.x | Medium | High | ✅ Done |
| 2.6.0 | Low | Medium | ✅ Done |
| 3.0.0 | Medium-High | Medium* | 🔄 60% Complete |

*Complexity reduced from High to Medium due to v2.6.0 modularization laying the foundation.

---

## Timeline

**Note**: We intentionally do not provide dates. See [SEMANTIC_VERSIONING.md](SEMANTIC_VERSIONING.md) for why.

Versions release when:
1. All features complete
2. Educational content reviewed
3. Community testing done
4. Ethical review passed

Quality over speed. Always.

---

## How to Influence the Roadmap

1. **Open issues**: Discuss specific features
2. **Assess priorities**: Help evaluate impact, effort, and risk
3. **Contribute**: PRs that align with roadmap get priority review
4. **Test prereleases**: Early feedback shapes final releases

---

## Related Documents

- [MIGRATION.md](MIGRATION.md) - Upgrading between versions
- [SEMANTIC_VERSIONING.md](SEMANTIC_VERSIONING.md) - Version numbering strategy
- [ETHICS.md](ETHICS.md) - Ethical framework guiding decisions
- [docs/adr/](docs/adr/) - Architecture decisions

---

*This roadmap is a living document. It will evolve based on community feedback, emerging best practices, and our commitment to education-first development.*
