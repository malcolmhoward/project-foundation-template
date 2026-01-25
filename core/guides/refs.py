# core/guides/refs.py
# References guide (REFS.md)

"""
References Guide.

Provides guidance on creating and maintaining a project references file.
"""

GUIDE_ID = "refs"

GUIDE = {
    "title": "References Guide (REFS.md)",
    "purpose": "Documenting external resources and references for a project",
    "audience": "Maintainers and contributors",
    "complexity": "beginner",
}

RELATED_PRINCIPLES = ["readme", "glossary"]

CONTENT = """
# References Guide (REFS.md)

## Overview

A REFS.md file serves as a curated collection of external resources, documentation,
and references that are relevant to understanding and working with a project.
It's the project's bibliography.

## Why Maintain References?

1. **Onboarding**: New contributors find learning resources
2. **Context**: Explains design decisions with sources
3. **Attribution**: Credits influential work
4. **Maintenance**: Keeps track of upstream dependencies
5. **Education**: Provides learning paths

## REFS.md Structure

### Basic Template

```markdown
# References

## Specifications

Standards and specifications this project implements or follows.

- [Semantic Versioning 2.0.0](https://semver.org/)
- [Conventional Commits 1.0.0](https://conventionalcommits.org/)
- [Keep a Changelog](https://keepachangelog.com/)

## Documentation

Official documentation for dependencies and tools.

- [Python Documentation](https://docs.python.org/3/)
- [pytest Documentation](https://docs.pytest.org/)

## Tutorials & Guides

Learning resources for contributors.

- [Real Python Tutorials](https://realpython.com/)
- [The Hitchhiker's Guide to Python](https://docs.python-guide.org/)

## Research & Papers

Academic or industry research relevant to the project.

- [Paper Title](https://example.com/paper) - Brief description

## Influential Projects

Projects that inspired design decisions.

- [Project Name](https://github.com/org/project) - What we learned

## Books

Recommended reading for deeper understanding.

- "Book Title" by Author - Relevant chapters
```

### Categorized by Topic

```markdown
# References

## Architecture

- [Clean Architecture](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html)
- [Hexagonal Architecture](https://alistair.cockburn.us/hexagonal-architecture/)

## Testing

- [Test Pyramid](https://martinfowler.com/articles/practical-test-pyramid.html)
- [TDD by Example](https://www.amazon.com/Test-Driven-Development-Kent-Beck/dp/0321146530)

## Security

- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [CWE Top 25](https://cwe.mitre.org/top25/)
```

## Best Practices

### Link Stability Guidelines

Not all references need URLs. Consider link stability when deciding what to link:

**Safe to link (stable sources):**
- Official specifications (semver.org, conventionalcommits.org)
- Standards bodies (W3C, IETF RFCs, ISO)
- Wikipedia (established articles)
- Major organization documentation (OWASP, GitHub Docs)

**Reference by name only (no links):**
- Books (title + author is permanent; URLs are not)
- Individual blog posts (prone to disappear)
- Project-specific documentation (URLs change with versions)
- Conference talks (hosting platforms change)

**Example:**
```markdown
## Recommended Reading

- "Clean Code" by Robert C. Martin - Chapter 7 on Error Handling
- "The Pragmatic Programmer" by Hunt and Thomas

## Specifications

- [Semantic Versioning 2.0.0](https://semver.org/)
- [Conventional Commits](https://conventionalcommits.org/)
```

### Link Hygiene

- Use permanent links when available (DOI, archive.org)
- Check links periodically for rot
- Include access dates for frequently updated resources
- Mirror critical resources if permitted

### Annotations

Add context to each reference:

```markdown
- [Semantic Versioning](https://semver.org/) - Version numbering scheme used
  for all releases. See VERSIONING.md for our interpretation.
```

### Versioning References

For specs and standards, include versions:

```markdown
- [OpenAPI Specification v3.1.0](https://spec.openapis.org/oas/v3.1.0)
  - We currently implement v3.0.3
  - v3.1.0 migration planned for Q2 2024
```

## Integration with Other Docs

### From README.md

```markdown
## Further Reading

See [REFS.md](./REFS.md) for specifications, research, and learning resources.
```

### From ADRs

```markdown
## References

See [REFS.md](../REFS.md#architecture) for background on architectural patterns.
```

### From Code Comments

```python
# Implementation based on algorithm described in REFS.md#algorithms
def process_data():
    ...
```

## Maintenance

- Review quarterly for dead links
- Add new references as the project evolves
- Remove outdated or superseded references
- Keep organized as the list grows

## Related Resources

- Citation management best practices
- Link rot prevention strategies
- Academic reference formatting
"""
