# ADR 0008: Programming Language Support Architecture

## Status

Proposed (Target: v3.5.0)

## Date

2026-01-19

## Context

The original ~6,500 line enterprise specification included support for 18 programming languages with language-specific configurations for linters, formatters, and test frameworks. The current v3.0.0 implementation does not include this feature.

### Original Specification

```python
SUPPORTED_PROGRAMMING_LANGUAGES = {
    "python": {
        "extensions": [".py"],
        "linter": "flake8",
        "formatter": "black",
        "test_framework": "pytest",
        "max_line_length": 100,
        "indent": 4,
    },
    # ... 17 more languages
}
```

### Languages in Specification

| Category | Languages |
|----------|-----------|
| Top 10 General | Python, JavaScript, TypeScript, Java, C++, C, C#, Go, Rust, PHP |
| Additional | Ruby, Swift, Kotlin, Bash |
| Game Development | GDScript, Lua, Haxe |

### Use Cases

1. **Code Standards Principle**: Generate language-specific linter configs
2. **Quality Assurance Principle**: Generate language-specific test configs
3. **Pre-commit Hooks**: Language-aware hook configurations
4. **CI Workflows**: Language-specific build and test steps

## Decision

We will implement programming language support as a **modular configuration system** within the existing plugin architecture.

### Architecture

```
core/
├── languages/
│   ├── __init__.py          # Language registry and helpers
│   ├── base.py              # Base language configuration class
│   ├── python.py            # Python configuration
│   ├── javascript.py        # JavaScript configuration
│   ├── typescript.py        # TypeScript configuration
│   └── ... (15 more)
```

### Language Configuration Schema

```python
@dataclass
class LanguageConfig:
    """Configuration for a programming language."""
    id: str                    # e.g., "python"
    name: str                  # e.g., "Python"
    extensions: List[str]      # e.g., [".py"]
    linter: str                # e.g., "flake8"
    linter_config: str         # e.g., ".flake8" or "pyproject.toml"
    formatter: str             # e.g., "black"
    formatter_config: str      # e.g., "pyproject.toml"
    test_framework: str        # e.g., "pytest"
    test_config: str           # e.g., "pytest.ini"
    max_line_length: int       # e.g., 100
    indent: Union[int, str]    # e.g., 4 or "tab"
    description: str           # e.g., "Python 3.8+"
```

### Integration Points

1. **`--language` CLI argument**: Specify primary project language
2. **`code-standards` principle**: Generates language-specific configs
3. **`quality-assurance` principle**: Generates test framework configs
4. **`pre-commit-hooks` principle**: Language-aware hooks
5. **Presets**: Can specify default language

### Generated Files (Example: Python)

```
.flake8                     # Linter config
pyproject.toml              # Formatter + test config section
.pre-commit-config.yaml     # Language-specific hooks
.github/workflows/ci.yml    # Python-specific CI steps
```

## Consequences

### Positive

1. **Language-specific guidance**: Users get appropriate tooling for their language
2. **Reduced setup time**: Configs are pre-generated with best practices
3. **Consistency**: Standard configurations across projects
4. **Extensible**: Plugin system allows custom language definitions

### Negative

1. **Maintenance burden**: 18 languages to keep updated
2. **Tool version drift**: Linter/formatter versions may change
3. **Opinionated defaults**: May not match all team preferences
4. **Complexity**: Significant new code surface area

### Neutral

1. **Optional feature**: Projects without `--language` work as before
2. **Override support**: Generated configs can be customized

## Alternatives Considered

### 1. Single Generic Configuration

Provide generic linter/formatter guidance without language-specific configs.

**Rejected because**: Misses the value proposition of language-specific best practices.

### 2. External Tool Integration

Integrate with existing tools like `cookiecutter` or `copier` for language templates.

**Rejected because**: Adds external dependencies, reduces educational value.

### 3. Link to External Resources

Just link to language-specific setup guides.

**Rejected because**: Doesn't provide actionable generated files.

## Implementation Plan

### Phase 1: Core Infrastructure
- [ ] Create `core/languages/` module structure
- [ ] Define `LanguageConfig` dataclass
- [ ] Implement language registry

### Phase 2: Priority Languages (8)
- [ ] Python, JavaScript, TypeScript, Go
- [ ] Java, C#, Rust, Bash

### Phase 3: Additional Languages (7)
- [ ] C, C++, PHP, Ruby, Swift, Kotlin

### Phase 4: Game Development (3)
- [ ] GDScript, Lua, Haxe

### Phase 5: Integration
- [ ] CLI argument support
- [ ] Principle integration
- [ ] Preset language defaults

## Related Decisions

- [ADR 0006: Plugin Architecture](0006-plugin-architecture.md) (v2.11.0)
- [ADR 0007: Enterprise Feature Parity](0007-enterprise-feature-parity.md) (v3.0.0)

## References

- [ROADMAP.md](../../ROADMAP.md) - v3.5.0 planning

---

*This ADR proposes the architecture for programming language support, planned for v3.5.0.*
