# core/guides/personas.py
# Personas guide

"""
Personas Guide.

Provides guidance on creating and using personas for user-centered design.
"""

GUIDE_ID = "personas"

GUIDE = {
    "title": "Personas Guide",
    "purpose": "Creating and using personas for user-centered development",
    "audience": "Product managers, designers, and developers",
    "complexity": "intermediate",
}

RELATED_PRINCIPLES = ["accessibility", "quality-assurance"]

CONTENT = """
# Personas Guide

## Overview

Personas are fictional characters that represent different user types who might
use your product. They help teams make user-centered decisions by providing
a concrete reference point for discussions about features and design.

## Why Use Personas?

1. **Shared Understanding**: Team aligns on who they're building for
2. **Better Decisions**: "Would Maya use this?" is more concrete than "Would users?"
3. **Empathy Building**: Helps developers understand user perspectives
4. **Scope Control**: Easier to say no to features that don't serve personas
5. **Communication**: Simplifies stakeholder discussions

## Anatomy of a Persona

### Essential Elements

```markdown
## [Name] - [Role/Title]

**Demographics**
- Age: [range]
- Location: [region/type]
- Technical proficiency: [level]

**Goals**
- Primary: [main objective]
- Secondary: [supporting objectives]

**Frustrations**
- [Pain point 1]
- [Pain point 2]

**Quote**
"[A statement that captures their perspective]"
```

### Example Persona

```markdown
## Alex Chen - Senior Developer

**Demographics**
- Age: 32
- Location: Urban tech hub
- Technical proficiency: Expert

**Background**
Alex leads a team of 5 developers at a mid-size startup. They're responsible
for code quality and mentoring junior developers. Time is always scarce.

**Goals**
- Primary: Ship quality code faster
- Secondary: Reduce onboarding time for new team members

**Frustrations**
- Tools that require extensive configuration
- Documentation that assumes too much knowledge
- Inconsistent patterns across the codebase

**Quote**
"I don't have time to read 50 pages of docs. Show me a working example."

**Technology**
- Uses: VS Code, GitHub, Docker
- Prefers: CLI tools over GUIs
- Avoids: Vendor lock-in
```

## Creating Personas

### Research Methods

1. **User Interviews**: Direct conversations with users
2. **Surveys**: Quantitative data collection
3. **Analytics**: Behavior patterns from usage data
4. **Support Tickets**: Common issues and requests
5. **Sales Team Input**: Customer feedback and objections

### Process

1. Gather research data
2. Identify patterns and clusters
3. Draft 3-5 distinct personas
4. Validate with stakeholders
5. Refine based on feedback
6. Document and share

## Using Personas

### In Planning

- "Which persona does this feature serve?"
- "How would [Persona] discover this?"
- "What's the priority for [Persona]?"

### In Design

- "Can [Persona] complete this workflow?"
- "Does this match [Persona]'s mental model?"
- "What would confuse [Persona]?"

### In Development

- "How would [Persona] handle this error?"
- "What defaults make sense for [Persona]?"
- "Is this accessible to [Persona]?"

## Anti-Patterns

- **Elastic Personas**: Changing persona details to justify decisions
- **Too Many Personas**: More than 5 becomes unwieldy
- **Demographic Only**: Missing goals and frustrations
- **Fictional Research**: Making up personas without data
- **Stale Personas**: Never updating as users evolve

## Maintaining Personas

- Review quarterly
- Update after major user research
- Archive personas that no longer represent users
- Add new personas as user base evolves

## Further Reading

- "The Inmates Are Running the Asylum" by Alan Cooper
- Nielsen Norman Group articles on personas
- Lean UX persona techniques
"""
