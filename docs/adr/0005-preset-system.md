# ADR 0005: Governance Preset System

## Status

Accepted

## Date

2026-01-18

## Context

As the Project Foundation Template evolved from a minimal "lite" edition toward the full v3.0.0 vision, we faced a challenge: how do users select the appropriate level of governance for their projects?

### The Problem

Different projects have different governance needs:

| Project Type | Governance Needs |
|-------------|------------------|
| Personal hobby project | Minimal (README, LICENSE) |
| Small open source library | Light (+ CONTRIBUTING, CoC) |
| Active community project | Standard (+ issue templates, CI) |
| Enterprise software | Strict (+ security policies, ADRs) |
| Regulated industry | Enterprise (full governance suite) |

### Previous Approach

The original enterprise edition had a `--preset` flag, but:
- Presets were hardcoded in the main script
- Adding new presets required modifying core logic
- No clear documentation of what each preset included
- Users couldn't easily customize preset contents

### Requirements

1. **Clear progression**: Users should understand the path from minimal → enterprise
2. **Discoverability**: Easy to see what each preset includes
3. **Extensibility**: Add new presets without touching core code
4. **Education**: Each preset should explain WHY it includes certain features

## Decision

We implement a **modular preset system** with the following architecture:

### Package Structure

```
core/
└── presets/
    ├── __init__.py      # Registry and helper functions
    ├── minimal.py       # 5 principles
    ├── light.py         # 8 principles
    ├── standard.py      # 10 principles (default)
    ├── strict.py        # 12 principles
    └── enterprise.py    # All principles
```

### Preset Definition

Each preset is a dictionary with:

```python
STANDARD_PRESET = {
    "name": "standard",
    "description": "Recommended default - adds GitHub templates and CI",
    "principles": [
        "readme",
        "contributing",
        "license",
        "code-of-conduct",
        "security",
        "changelog",
        "issue-templates",
        "pr-template",
        "ci-workflow",
    ],
    "features": {
        "readme": True,
        "contributing": True,
        # ... feature flags
    },
    "recommended_for": [
        "Active open source projects",
        "Projects with regular contributions",
    ],
}
```

### Preset Progression

| Preset | Principles | Target Audience |
|--------|------------|-----------------|
| minimal | 5 | Personal projects, learning |
| light | 8 | Small libraries, utilities |
| standard | 10 | Active open source (default) |
| strict | 12 | Enterprise, security-focused |
| enterprise | 13+ | Regulated industries, large orgs |

### API

```python
from core.presets import get_preset, list_presets, DEFAULT_PRESET

# Get preset configuration
config = get_preset("standard")

# List available presets
presets = list_presets()  # ["minimal", "light", "standard", "strict", "enterprise"]
```

## Consequences

### Positive

1. **Clear mental model**: Users understand the governance spectrum
2. **Self-documenting**: Each preset file explains its purpose
3. **Extensible**: Add custom presets without modifying core code
4. **Testable**: Each preset can be independently tested
5. **Educational**: Preset files teach WHY features are grouped together

### Negative

1. **More files**: Package has multiple small files instead of one configuration
2. **Learning curve**: Users must understand the preset system
3. **Maintenance**: Changes to features may require updates to multiple presets

### Neutral

1. **Opinionated defaults**: "standard" as default may not suit everyone
2. **Fixed progression**: The 5-tier system is somewhat arbitrary

## Alternatives Considered

### 1. Interactive Questionnaire
Ask users questions to determine appropriate governance level.

**Rejected because**: Adds friction, hard to automate, users may not know their needs.

### 2. Single Configuration File
One YAML/JSON file with all presets.

**Rejected because**: Less self-documenting, harder to extend, no educational comments.

### 3. Feature-Based Selection
Let users pick individual features, auto-suggest preset.

**Rejected because**: Too granular for most users, loses the "curated experience" benefit.

### 4. No Presets (All Manual)
Users explicitly enable each feature they want.

**Rejected because**: Requires too much knowledge upfront, loses educational structure.

## Implementation

### Usage in CLI

```bash
# Use default preset (standard)
python setup_foundation_lite.py --project-name "MyProject" --author-name "Me"

# Explicitly select preset
python setup_foundation_lite.py --preset minimal --project-name "MyProject" --author-name "Me"

# List available presets
python setup_foundation_lite.py --list-presets
```

### Integration with Generator

```python
class EthicalFoundationGenerator:
    def __init__(self, args):
        preset_name = getattr(args, 'preset', DEFAULT_PRESET)
        self.preset = get_preset(preset_name)
        # Use preset to determine which features to generate
```

## Related Decisions

- [ADR 0001: Education-First Approach](0001-education-first.md) (v2.1.0)
- [ADR 0002: Semantic Versioning Strategy](0002-semantic-versioning-strategy.md) (v2.6.0)
- [ADR 0003: Advisory Expiration System](0003-advisory-expiration.md) (v2.6.0)
- [ADR 0004: Modular Package Architecture](0004-modular-package-architecture.md) (v2.6.0)
- ADR 0006: Plugin Architecture (v2.11.0)

## References

- [ROADMAP.md](../../ROADMAP.md) - Preset system in version roadmap
- `core/presets/` - Implementation
- `tests/test_foundation_presets.py` - Test suite

---

*The preset system embodies our education-first philosophy: rather than overwhelming users with choices, we offer curated paths that teach appropriate governance levels.*
