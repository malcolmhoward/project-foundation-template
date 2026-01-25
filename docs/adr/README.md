# Architecture Decision Records

This directory contains Architecture Decision Records (ADRs) for the Project Foundation Template.

## What is an ADR?

An ADR captures an important architectural decision along with its context and consequences. They serve as:
- Historical record of why decisions were made
- Onboarding documentation for new contributors
- Reference when revisiting past decisions

## ADR Format

Each ADR follows this structure:

1. **Status**: Proposed, Accepted, Deprecated, Superseded
2. **Date**: When the decision was made
3. **Context**: What situation prompted this decision
4. **Decision**: What we decided to do
5. **Consequences**: What happens as a result (positive, negative, neutral)
6. **Alternatives Considered**: Other options evaluated

## Index

| ADR | Title | Status | Date |
|-----|-------|--------|------|
| [0001](0001-education-first.md) | Education-First Approach | Accepted | 2025-10-29 |
| [0002](0002-semantic-versioning-strategy.md) | Semantic Versioning Strategy | Accepted | 2026-01-18 |
| [0003](0003-advisory-expiration.md) | Advisory Expiration System | Accepted | 2026-01-18 |
| [0004](0004-modular-package-architecture.md) | Modular Package Architecture (v2.6.0) | Accepted | 2026-01-18 |
| [0005](0005-preset-system.md) | Governance Preset System (v2.7.0) | Accepted | 2026-01-18 |
| [0006](0006-plugin-architecture.md) | Plugin Architecture (v2.11.0) | Accepted | 2026-01-18 |
| [0007](0007-enterprise-feature-parity.md) | Enterprise Feature Parity Strategy (v3.0.0+) | Accepted | 2026-01-19 |
| [0008](0008-programming-language-support.md) | Programming Language Support (v3.5.0) | Proposed | 2026-01-19 |
| [0009](0009-internationalization-architecture.md) | Internationalization Architecture (v3.6.0) | Proposed | 2026-01-19 |
| [0010](0010-tiered-ethical-review-framework.md) | Tiered Ethical Review Framework (v3.7.0) | Accepted | 2026-01-25 |

## Creating New ADRs

1. Copy the template below
2. Number sequentially (0002, 0003, etc.)
3. Fill in all sections
4. Update this index
5. Submit via PR with educational context

## Template

```markdown
# ADR NNNN: Title

## Status
Proposed | Accepted | Deprecated | Superseded by [ADR XXXX](link)

## Date
YYYY-MM-DD

## Context
What is the issue that we're seeing that is motivating this decision?

## Decision
What is the change that we're proposing and/or doing?

## Consequences
What becomes easier or more difficult to do because of this change?

### Positive
-

### Negative
-

### Neutral
-

## Alternatives Considered
What other options were evaluated?

## References
Links to related documents, issues, or external resources.
```

## Philosophy

ADRs in this project follow our education-first approach:
- **WHAT**: Clearly state the decision
- **WHY**: Explain the context and reasoning
- **HOW**: Describe implementation and consequences

We believe understanding past decisions is as important as making new ones.
