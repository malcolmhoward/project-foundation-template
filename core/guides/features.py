# core/guides/features.py
# Features guide

"""
Features Guide.

Provides guidance on documenting and managing project features.
"""

GUIDE_ID = "features"

GUIDE = {
    "title": "Features Documentation Guide",
    "purpose": "Documenting and communicating project features effectively",
    "audience": "Product managers, developers, and technical writers",
    "complexity": "beginner",
}

RELATED_PRINCIPLES = ["readme", "quality-assurance"]

CONTENT = """
# Features Documentation Guide

## Overview

Feature documentation helps users understand what your project can do, helps
contributors know what exists, and helps maintainers track capabilities over time.

## Feature Documentation Levels

### 1. Quick Feature List (README)

High-level bullet points for quick scanning:

```markdown
## Features

- **Fast**: Processes 1M records in under 5 seconds
- **Extensible**: Plugin system for custom processors
- **Cross-platform**: Works on Linux, macOS, and Windows
- **Zero dependencies**: Single binary deployment
```

### 2. Feature Matrix

Comparison format for multiple editions or competitors:

```markdown
## Feature Comparison

| Feature | Free | Pro | Enterprise |
|---------|------|-----|------------|
| Basic processing | ✓ | ✓ | ✓ |
| API access | - | ✓ | ✓ |
| Custom plugins | - | ✓ | ✓ |
| SSO integration | - | - | ✓ |
| SLA guarantee | - | - | ✓ |
```

### 3. Detailed Feature Pages

In-depth documentation for each feature:

```markdown
# Plugin System

## Overview
The plugin system allows extending core functionality without modifying source code.

## Capabilities
- Custom data processors
- Output formatters
- Authentication providers

## Getting Started
[Quick start guide]

## API Reference
[Detailed API documentation]

## Examples
[Working code examples]
```

## Writing Feature Descriptions

### The Feature Template

```markdown
## [Feature Name]

**What it does**: One sentence description

**Why it matters**: The problem it solves

**How to use it**: Quick start or link to docs

**Example**:
[Code or screenshot]
```

### Good vs. Poor Descriptions

**Poor:**
```
Supports JSON output.
```

**Good:**
```
**JSON Export**: Export any report to JSON format for integration
with other tools. Supports streaming for large datasets.

Example: `mytool export --format json > report.json`
```

## Feature Status Indicators

Use clear status labels:

| Label | Meaning |
|-------|---------|
| ✓ Stable | Production-ready, API won't change |
| β Beta | Functional but API may change |
| α Alpha | Experimental, may have bugs |
| 🚧 In Progress | Currently being developed |
| 📅 Planned | On the roadmap |
| ⚠️ Deprecated | Still works but will be removed |
| ❌ Removed | No longer available (see migration guide) |

## Feature Discovery

Help users find features:

1. **Categorization**: Group related features
2. **Search**: Enable full-text search in docs
3. **Tags**: Label features by use case
4. **Examples**: Provide working code samples
5. **Tutorials**: Show features in context

## Changelog Integration

Link features to their release:

```markdown
## [1.5.0] - 2024-01-15

### Added
- **Plugin System** (#123): Extensible architecture for custom processors
  - See: [Plugin Documentation](/docs/plugins.md)
```

## Feature Deprecation

Document deprecated features clearly:

```markdown
## Deprecated Features

### Legacy Export (deprecated in v2.0)

**Status**: Will be removed in v3.0
**Migration**: Use the new Export API instead
**Documentation**: [Migration Guide](/docs/migration/export.md)
```

## Removed Features

Document removed features for users upgrading:

```markdown
## Removed Features

### XML Export (removed in v3.0)

**Removed in**: v3.0.0
**Reason**: Low usage, maintenance burden
**Alternative**: Use JSON export with external XML converter
**Migration Guide**: [XML to JSON Migration](/docs/migration/xml-export.md)
```

## Further Reading

- Technical writing best practices
- API documentation standards
- User documentation guidelines
"""
