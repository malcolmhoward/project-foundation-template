# ADR 0006: Plugin Architecture

## Status

Accepted

## Date

2026-01-18

## Context

As the Project Foundation Template matured through v2.x versions, a recurring challenge emerged: how do users extend the template with custom principles and guides without forking or modifying core code?

### The Problem

1. **Customization Needs**: Organizations have domain-specific governance requirements
2. **Core Stability**: Modifications to core code risk breaking updates
3. **Sharing Barriers**: Custom extensions couldn't be easily shared between projects
4. **Version Coupling**: Custom code tightly coupled to specific template versions

### User Scenarios

| Scenario | Need |
|----------|------|
| Financial services | Compliance-specific principles |
| Healthcare | HIPAA-related governance |
| Game development | Platform certification guides |
| Internal tools | Company-specific standards |

### Requirements

1. **Extensibility**: Add principles and guides without modifying core
2. **Discoverability**: Automatic loading from standard locations
3. **Validation**: Ensure plugins meet quality standards
4. **Conflict Resolution**: Handle ID collisions gracefully
5. **Education Alignment**: Plugins must follow WHAT/WHY/HOW pattern

## Decision

We implement a **plugin system** with the following architecture:

### Package Structure

```
core/
└── plugins/
    ├── __init__.py      # Discovery and loading API
    ├── base.py          # Base classes (PrinciplePlugin, GuidePlugin)
    ├── loader.py        # Plugin loading and merging logic
    └── validator.py     # Plugin validation rules
```

### Plugin Discovery

Plugins are discovered from:
1. `FOUNDATION_PLUGINS_DIR` environment variable (if set)
2. `~/.foundation-plugins/` (user-level)
3. `./plugins/` (project-level)

### Base Classes

```python
class PrinciplePlugin:
    """Base class for principle plugins."""
    PRINCIPLE_ID: str       # Unique identifier
    PRINCIPLE: dict         # Principle definition (name, why, what, risk)
    EDUCATION: str          # Educational content

class GuidePlugin:
    """Base class for guide plugins."""
    GUIDE_ID: str           # Unique identifier
    GUIDE_INFO: dict        # Guide metadata
    GUIDE_CONTENT: str      # Full guide content
```

### Usage

```python
# Create a custom principle plugin
# In ~/.foundation-plugins/my_principle.py
from core.plugins import PrinciplePlugin

class CompliancePrinciple(PrinciplePlugin):
    PRINCIPLE_ID = "regulatory-compliance"
    PRINCIPLE = {
        "name": "Regulatory Compliance",
        "why": "Legal requirements mandate specific governance",
        "what": "Ensures compliance with industry regulations",
        "risk": "Legal liability, fines, operational restrictions",
    }
    EDUCATION = """
    ## Regulatory Compliance

    Understanding your industry's regulatory requirements...
    """

# Load and use plugins
from core.plugins import discover_plugins, get_all_principles

discover_plugins()
all_principles = get_all_principles()  # Includes plugin principles
```

### Validation

All plugins are validated for:
- Required attributes present
- Correct types (PRINCIPLE_ID is string, PRINCIPLE is dict)
- WHAT/WHY/HOW educational pattern compliance
- No conflicts with built-in IDs (unless conflict_mode allows)

### Conflict Resolution

```python
discover_plugins(
    conflict_mode="skip"      # Ignore plugins with conflicting IDs (default)
    # conflict_mode="replace" # Plugin overrides built-in
    # conflict_mode="error"   # Raise PluginConflictError
)
```

## Consequences

### Positive

1. **Extensibility**: Users can add custom governance without forking
2. **Maintainability**: Core code stays clean, plugins are isolated
3. **Shareability**: Plugin files can be shared between projects
4. **Version Independence**: Plugins can work across template versions
5. **Quality Assurance**: Validation ensures plugins meet standards
6. **Education Preservation**: Plugins must follow educational pattern

### Negative

1. **Complexity**: Additional abstraction layer to understand
2. **Discovery Magic**: Auto-loading may surprise users
3. **Debugging Difficulty**: Issues may come from plugins vs core
4. **API Stability**: Plugin API must remain stable across versions

### Neutral

1. **Optional Feature**: Users not needing customization can ignore plugins
2. **Documentation Burden**: Plugin development guide needed

## Alternatives Considered

### 1. Configuration-Based Extension

Allow principles via JSON/YAML configuration files.

**Rejected because**: Limited expressiveness, no code execution for complex logic, harder to validate educational content.

### 2. Monkey Patching

Let users modify core dictionaries directly.

**Rejected because**: Fragile, no validation, difficult to track what was modified, breaks on updates.

### 3. Fork-and-Modify

Expect users to fork the repo for customization.

**Rejected because**: Maintenance burden, difficult to receive updates, discourages contribution back.

### 4. Class Inheritance (Chosen)

Python class-based plugins with validation.

**Selected because**: Familiar pattern, strong typing, validation possible, education pattern enforceable, clean separation.

## Implementation

### File Structure for Plugins

```
~/.foundation-plugins/
├── compliance_principle.py    # Single principle
├── security_guides/
│   ├── __init__.py
│   ├── penetration_testing.py # Guide plugin
│   └── incident_response.py   # Guide plugin
└── company_standards.py       # Multiple plugins in one file
```

### Validation Rules

```python
# All plugins must have:
# 1. Class inheriting from PrinciplePlugin or GuidePlugin
# 2. Required ID attribute (PRINCIPLE_ID or GUIDE_ID)
# 3. Required content attributes (PRINCIPLE/EDUCATION or GUIDE_INFO/GUIDE_CONTENT)
# 4. Content following WHAT/WHY/HOW pattern
```

### Integration with Generator

```python
class EthicalFoundationGenerator:
    def __init__(self, args):
        # Load plugins before generating
        from core.plugins import discover_plugins
        discover_plugins()

    def generate_foundation(self):
        # get_all_principles() now includes plugins
        from core.plugins import get_all_principles
        principles = get_all_principles()
```

## Migration

### From v2.10.0 to v2.11.0

No migration required. Plugins are opt-in:
- Projects without plugins work identically
- To use plugins, create files in plugin directories

### Future: Custom Presets via Plugins

v3.0.0 may allow defining custom presets as plugins:
```python
class HealthcarePreset(PresetPlugin):
    PRESET_ID = "healthcare"
    PRINCIPLES = ["regulatory-compliance", "hipaa", "audit-logging", ...]
```

## Related Decisions

- [ADR 0001: Education-First Approach](0001-education-first.md) (v2.1.0) - plugins must follow educational pattern
- [ADR 0002: Semantic Versioning Strategy](0002-semantic-versioning-strategy.md) (v2.6.0)
- [ADR 0003: Advisory Expiration System](0003-advisory-expiration.md) (v2.6.0)
- [ADR 0004: Modular Package Architecture](0004-modular-package-architecture.md) (v2.6.0) - foundation for plugin system
- [ADR 0005: Governance Preset System](0005-preset-system.md) (v2.7.0) - plugins extend presets

## References

- `core/plugins/` - Implementation
- `core/plugins/base.py` - Base classes
- `tests/test_foundation_plugins.py` - Test suite
- [ROADMAP.md](../../ROADMAP.md) - Plugin system in version roadmap

---

*The plugin system extends the education-first philosophy: custom content must still teach WHAT, WHY, and HOW.*
