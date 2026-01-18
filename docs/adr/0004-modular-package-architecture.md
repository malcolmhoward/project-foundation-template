# ADR 0004: Modular Package Architecture (v2.6.0)

## Status

Accepted

## Date

2026-01-18

## Context

After completing versions 2.1.0 through 2.5.0, the `setup_foundation_lite.py` script had grown to 2,177 lines as a single monolithic file. This made the codebase:

- **Difficult to test**: Unit testing required running the entire script
- **Hard to maintain**: Changes risked unintended side effects
- **Challenging to extend**: Adding features meant modifying one large file
- **Incompatible with v3.0.0 goals**: The roadmap calls for a plugin architecture

### Original Structure (v2.5.0)

```
project-foundation-template/
├── setup_foundation_lite.py    # 2,177 lines - everything in one file
└── tests/
    └── test_smoke.py           # 19 integration tests only
```

### Problems

1. **Test coverage limited**: Only smoke tests possible without module boundaries
2. **No separation of concerns**: Config, education, templates, and generation mixed
3. **v3.0.0 blocked**: Could not implement plugin architecture without modularization
4. **Code duplication**: Template content interleaved with generation logic

## Decision

We will modularize the codebase into a `foundation` package with clear module boundaries:

### v2.6.0 Package Structure

```
project-foundation-template/
├── setup_foundation_lite.py    # 128 lines - thin entry point
├── core/
│   ├── __init__.py             # Package exports
│   ├── utils.py                # Constants and helpers
│   ├── config.py               # Configuration and argument parsing
│   ├── education.py            # Principles and educational content
│   ├── ethics.py               # Ethical safeguards (standalone functions)
│   ├── generator.py            # EthicalFoundationGenerator class
│   └── templates/
│       ├── __init__.py         # Template subpackage exports
│       ├── core.py             # README, CONTRIBUTING, LICENSE, .gitignore
│       ├── governance.py       # CoC, SECURITY, CHANGELOG
│       ├── github.py           # Issue templates, PR template, workflows
│       └── advanced.py         # ADR, secrets detection, enhanced security
└── tests/
    ├── test_smoke.py           # 19 integration tests
    ├── test_foundation_utils.py      # 8 unit tests
    ├── test_foundation_config.py     # 16 unit tests
    ├── test_foundation_education.py  # 16 unit tests
    └── test_foundation_templates.py  # 24 unit tests
```

### Module Responsibilities

| Module | Responsibility | Lines |
|--------|---------------|-------|
| `utils.py` | Constants, version, expiration, Windows UTF-8 handling | ~70 |
| `config.py` | Argument parsing, config file loading, validation | ~200 |
| `education.py` | LITE_PRINCIPLES, EDUCATION_CONTENT, ETHICAL_USE_AGREEMENT | ~450 |
| `templates/core.py` | Core template generators | ~510 |
| `templates/governance.py` | Governance template generators | ~200 |
| `templates/github.py` | GitHub template generators | ~250 |
| `templates/advanced.py` | Advanced template generators | ~450 |
| `setup_foundation_lite.py` | Generator class and CLI entry point | ~595 |

### Metrics

| Metric | Before (v2.5.0) | After (v2.6.0) | Change |
|--------|-----------------|----------------|--------|
| Main script | 2,177 lines | 594 lines | -73% |
| Total modules | 1 | 9 | +800% |
| Test files | 1 | 5 | +400% |
| Unit tests | 19 | 83 | +337% |
| Test coverage* | ~30% (smoke only) | ~75% (estimated) | +150% |

*Coverage estimate based on module boundary testing

## Consequences

### Positive

1. **Unit testing enabled**: Each module can be tested in isolation
2. **Clear boundaries**: Separation of concerns makes code easier to understand
3. **v3.0.0 foundation**: Module structure aligns with target plugin architecture
4. **Maintainability**: Changes in one module don't affect others
5. **Parallel development**: Multiple contributors can work on different modules
6. **Import flexibility**: Users can import specific functionality

### Negative

1. **Import complexity**: Multiple files to navigate
2. **Module coordination**: Changes may need updates across modules
3. **Learning curve**: New contributors must understand package structure

### Neutral

1. **Backward compatibility**: Main script remains the entry point
2. **Test organization**: Tests mirror module structure

## Gap Analysis: v2.6.0 → v3.0.0

### Already Complete (v2.6.0+)

| v3.0.0 Requirement | Status | Notes |
|--------------------|--------|-------|
| Modular package | ✅ Complete | `core/` package (renamed from `foundation/`) |
| Config module | ✅ Complete | `core/config.py` |
| Education module | ✅ Complete | `core/education.py` |
| Template separation | ✅ Complete | `core/templates/` subpackage |
| Unit test suite | ✅ Complete | 148 tests across 7 files |
| 13+ principles | ✅ Complete | LITE_PRINCIPLES has 13 principles |
| Generator class | ✅ Complete | `core/generator.py` - EthicalFoundationGenerator |
| Ethics module | ✅ Complete | `core/ethics.py` - standalone ethics functions |
| Package rename | ✅ Complete | `foundation/` → `core/` |

### Remaining Work for v3.0.0

| v3.0.0 Requirement | Effort | Risk | Notes |
|--------------------|--------|------|-------|
| Preset system | Medium | Low | Create `presets/` with 5 preset configs |
| Principles directory | Medium | Medium | Split LITE_PRINCIPLES into separate modules |
| Documentation modules | High | Low | 20 new modules with content |
| Plugin architecture | High | Medium | Dynamic loading, hooks, extensions |

### Risk/Reward Assessment

**Low-Hanging Fruit (High Reward, Low Risk):**
- Generator extraction: Completes separation of concerns
- Ethics module: Natural boundary already exists
- Preset system: Configuration-only, no logic changes

**Medium Investment:**
- Principles directory: Content exists, needs reorganization

**High Investment:**
- Plugin architecture: Core v3.0.0 differentiator
- Documentation modules: 20 modules of new content

### Recommendation

The v2.6.0 modularization completed **~60% of the v3.0.0 architectural work**:

- Package structure: ✅ Done
- Module boundaries: ✅ Done
- Test infrastructure: ✅ Done
- Template separation: ✅ Done

Remaining work is primarily:
- Content creation (documentation modules)
- Configuration systems (presets, plugins)
- Organizational refinement (package rename, principles split)

**Risk Level: Low-Medium** — The hard architectural decisions are made. Remaining work is incremental.

## Implementation Notes

### Backward Compatibility

The main script (`setup_foundation_lite.py`) remains the entry point:
```bash
python setup_foundation_lite.py --project-name "MyProject" --author-name "Author"
```

### Import Patterns

```python
# Full import
from core import SCRIPT_VERSION, parse_arguments, LITE_PRINCIPLES

# Template imports
from core.templates import generate_readme_content, generate_license_content

# Direct module access
from core.config import load_config_file
from core.education import get_principle
```

## Related Decisions

- ADR 0001: Education-First Approach
- ADR 0002: Semantic Versioning Strategy
- ADR 0003: Advisory Expiration
- ADR 0005: Preset System (planned, v2.7.0)
- ADR 0006: Plugin Architecture (planned, v3.0.0)

## References

- [ROADMAP.md](../../ROADMAP.md) - Version roadmap
- PR #32: v2.6.0 Modularization (staging branch)
- Issue #27-31: v2.6.0 milestone issues

---

*This ADR documents the pivotal v2.6.0 release that transformed the codebase from monolithic to modular, establishing the foundation for the v3.0.0 plugin architecture.*
