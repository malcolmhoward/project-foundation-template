# core/guides/adr.py
# Architecture Decision Records Guide (v2.9.0)

"""
Architecture Decision Records (ADR) Guide.

Provides practical guidance on documenting architectural decisions
to preserve context and rationale for future reference.

Introduced in v2.9.0.
"""

GUIDE_ID = "adr"

GUIDE = {
    "title": "Architecture Decision Records Guide",
    "purpose": "Learn how to document architectural decisions effectively",
    "audience": "Developers and architects",
    "complexity": "intermediate",
}

RELATED_PRINCIPLES = ["adr"]

CONTENT = """
# Architecture Decision Records Guide

## What is an ADR?

An Architecture Decision Record (ADR) captures an important architectural
decision along with its context and consequences.

## Why Write ADRs?

- **Preserve context** - Why was this decision made?
- **Onboard new team members** - Understand the system's evolution
- **Revisit decisions** - When circumstances change
- **Learn from history** - Both successes and failures

## When to Write an ADR

Write an ADR when:
- Choosing between technologies or frameworks
- Designing system boundaries or interfaces
- Making trade-offs that affect multiple components
- Establishing patterns or conventions
- Any decision you'll want to remember in 6 months

## ADR Structure

### Title
Short, descriptive title with ADR number.
Example: "ADR-0005: Use PostgreSQL for User Data"

### Status
- **Proposed** - Under discussion
- **Accepted** - Approved and implementing
- **Rejected** - Not approved (keep for context!)
- **Deprecated** - No longer relevant
- **Superseded** - Replaced by another ADR

### Context
What's driving this decision?
- Problem statement
- Constraints (technical, business, time)
- Current state
- Forces at play

### Decision
What are we going to do?
- Be specific and actionable
- This is the core of the ADR

### Consequences
What happens because of this decision?
- Positive outcomes
- Negative trade-offs
- Neutral changes

### Options Considered
What alternatives did you evaluate?
- Document each option's pros/cons
- Shows you did due diligence

## Writing Tips

### Be Concise
- One decision per ADR
- 1-2 pages maximum
- Focus on the decision, not the research

### Be Honest
- Document trade-offs openly
- Include rejected options
- Note uncertainties

### Be Timely
- Write while context is fresh
- Don't wait for "perfect" understanding
- Update if things change

## Example ADR

```markdown
# ADR-0003: Use JWT for API Authentication

**Date**: 2024-01-15
**Status**: Accepted

## Context

Our API needs authentication. Requirements:
- Stateless (for horizontal scaling)
- Support for mobile and web clients
- Reasonable security for our use case

## Decision

We will use JWT (JSON Web Tokens) for API authentication.

- Tokens signed with RS256
- 15-minute access token expiry
- 7-day refresh token expiry
- Tokens stored in httpOnly cookies for web

## Consequences

### Positive
- Stateless authentication enables easy scaling
- Standard format with good library support
- Works across platforms

### Negative
- Cannot revoke individual tokens without state
- Token size larger than session IDs
- Complexity in token refresh logic

### Neutral
- Team needs to learn JWT best practices
- Monitoring needs to track token metrics

## Options Considered

### Option 1: Session-based Auth
- Pros: Simple, easy revocation
- Cons: Requires session store, scaling complexity

### Option 2: JWT (Chosen)
- Pros: Stateless, standard
- Cons: Revocation complexity

### Option 3: OAuth2 with External Provider
- Pros: Offloads auth entirely
- Cons: Vendor dependency, overkill for our needs

## References
- [JWT Best Practices](https://datatracker.ietf.org/doc/html/rfc8725)
```

## ADR Lifecycle

1. **Propose** - Write initial draft
2. **Discuss** - Review with team
3. **Decide** - Accept or reject
4. **Implement** - Build according to decision
5. **Revisit** - Update status if circumstances change

## Organizing ADRs

### Naming Convention
```
docs/adr/
  0001-record-architecture-decisions.md
  0002-use-react-for-frontend.md
  0003-use-jwt-for-authentication.md
```

### Index
Maintain an index (README.md) with:
- ADR number and title
- Status
- Date
- Brief summary

## Tools

- **adr-tools** - CLI for managing ADRs
- **Log4brains** - ADR management with UI
- **GitHub** - Use issues/PRs for discussion

## Anti-Patterns

1. **Skipping rejected decisions** - They provide valuable context
2. **Too much detail** - ADR != design document
3. **Not updating status** - Keep them current
4. **Writing retroactively** - Context gets lost
5. **No discussion** - ADRs should involve the team

---

*This guide complements your project's ADR templates*
"""
