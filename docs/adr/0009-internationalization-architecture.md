# ADR 0009: Internationalization Architecture

## Status

Proposed (Target: v3.6.0)

## Date

2026-01-19

## Context

The original ~6,500 line enterprise specification included support for 10 locales with i18n infrastructure. The current v3.0.0 has an `internationalization` principle but does not generate locale files or i18n infrastructure.

### Original Specification

```python
SUPPORTED_LOCALES = {
    "en": {"name": "English", "direction": "ltr"},
    "es": {"name": "Spanish", "direction": "ltr"},
    "fr": {"name": "French", "direction": "ltr"},
    "de": {"name": "German", "direction": "ltr"},
    "zh": {"name": "Chinese", "direction": "ltr"},
    "ja": {"name": "Japanese", "direction": "ltr"},
    "ko": {"name": "Korean", "direction": "ltr"},
    "pt": {"name": "Portuguese", "direction": "ltr"},
    "ar": {"name": "Arabic", "direction": "rtl"},
    "hi": {"name": "Hindi", "direction": "ltr"}
}
```

### Current State

The `internationalization` principle exists in v3.0.0 and explains:
- WHAT: Multi-language support structure
- WHY: Global reach and accessibility
- RISK: Limited market reach without i18n

However, it does not generate actual locale infrastructure.

### Use Cases

1. **Global Products**: Projects targeting international markets
2. **Open Source**: Community translations of documentation
3. **Enterprise**: Multi-region deployment requirements
4. **Accessibility**: Language as an accessibility dimension

## Decision

We will implement internationalization support as a **locale structure generator** that creates the foundation for i18n without imposing a specific translation framework.

### Architecture

```
core/
├── locales/
│   ├── __init__.py          # Locale registry and helpers
│   ├── base.py              # Base locale configuration
│   └── supported.py         # 10 supported locale definitions
```

### Generated Structure

When `internationalization` principle is active:

```
{project}/
├── locales/
│   ├── README.md            # i18n setup guide
│   ├── en/
│   │   └── messages.json    # English translations (template)
│   ├── es/
│   │   └── messages.json    # Spanish translations (placeholder)
│   ├── fr/
│   │   └── messages.json    # French translations (placeholder)
│   └── ... (7 more locales)
├── docs/
│   └── i18n-guide.md        # Translation contribution guide
```

### Locale Configuration Schema

```python
@dataclass
class LocaleConfig:
    """Configuration for a locale."""
    code: str                  # e.g., "en", "es", "ar"
    name: str                  # e.g., "English", "Spanish", "Arabic"
    native_name: str           # e.g., "English", "Español", "العربية"
    direction: str             # "ltr" or "rtl"
    plural_forms: int          # Number of plural forms
    date_format: str           # e.g., "MM/DD/YYYY", "DD/MM/YYYY"
```

### Framework Agnostic

The generated structure is **framework agnostic**:
- JSON format for broad compatibility
- Works with: i18next, react-intl, python-i18n, gettext, etc.
- Includes conversion scripts for common frameworks

### CLI Integration

```bash
# Generate with i18n support
python generate_foundation.py --preset enterprise --project-name "MyApp"

# Specify locales
python generate_foundation.py --locales en,es,fr,de --project-name "MyApp"

# Generate all supported locales
python generate_foundation.py --all-locales --project-name "MyApp"
```

## Consequences

### Positive

1. **Ready for translation**: Projects can accept translations immediately
2. **Framework flexibility**: Not locked to specific i18n library
3. **RTL support**: Arabic support demonstrates RTL handling
4. **Educational**: Teaches i18n best practices
5. **Community contributions**: Easy for translators to contribute

### Negative

1. **Placeholder content**: Generated files are templates, not real translations
2. **Maintenance**: 10 locales to keep template-consistent
3. **Complexity**: RTL support adds complexity
4. **False confidence**: Users might think they have "real" i18n

### Neutral

1. **Optional feature**: Only generated with `internationalization` principle
2. **Customizable**: Users can add/remove locales

## Alternatives Considered

### 1. Just Documentation

Only generate i18n guide without locale files.

**Rejected because**: Doesn't provide actionable infrastructure.

### 2. Single Framework Support

Generate for a specific framework (e.g., i18next only).

**Rejected because**: Limits flexibility, adds dependency assumption.

### 3. Full Translation Service Integration

Integrate with translation services (Crowdin, Transifex).

**Rejected because**: Adds external dependencies, scope creep.

### 4. Machine Translation

Auto-generate translations using AI.

**Rejected because**: Quality concerns, adds API dependency, cost.

## Implementation Plan

### Phase 1: Core Infrastructure
- [ ] Create `core/locales/` module structure
- [ ] Define `LocaleConfig` dataclass
- [ ] Implement locale registry

### Phase 2: LTR Locales (7)
- [ ] English, Spanish, French, German
- [ ] Chinese, Japanese, Korean

### Phase 3: RTL Support (1)
- [ ] Arabic with RTL infrastructure

### Phase 4: Additional Locales (2)
- [ ] Portuguese, Hindi

### Phase 5: Integration
- [ ] CLI argument support
- [ ] Principle integration
- [ ] Translation guide generation

## Ethical Considerations

### Accessibility

i18n is an accessibility feature. Non-English speakers deserve equal access to software and documentation.

### Cultural Sensitivity

- Locale templates should avoid cultural assumptions
- Date/time formats respect regional conventions
- No machine translation that might be offensive

### Resource Equity

- Generated structures don't favor any locale over another
- All locales get equal template quality

## Related Decisions

- [ADR 0006: Plugin Architecture](0006-plugin-architecture.md) (v2.11.0)
- [ADR 0007: Enterprise Feature Parity](0007-enterprise-feature-parity.md) (v3.0.0)
- [ADR 0008: Programming Language Support](0008-programming-language-support.md) (v3.5.0)

## References

- [ROADMAP.md](../../ROADMAP.md) - v3.6.0 planning
- [W3C Internationalization](https://www.w3.org/International/) - i18n best practices

---

*This ADR proposes the architecture for internationalization support, planned for v3.6.0.*
