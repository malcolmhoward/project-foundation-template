# core/guides/user_stories.py
# User stories guide

"""
User Stories Guide.

Provides guidance on writing effective user stories for requirements gathering.
"""

GUIDE_ID = "user-stories"

GUIDE = {
    "title": "User Stories Guide",
    "purpose": "Writing effective user stories for requirements and planning",
    "audience": "Product managers, developers, and stakeholders",
    "complexity": "beginner",
}

RELATED_PRINCIPLES = ["quality-assurance", "code-standards"]

RELATED_GUIDES = ["test-strategies", "personas"]

CONTENT = """
# User Stories Guide

## Overview

User stories are short, simple descriptions of a feature told from the perspective
of the person who desires the capability. They are a key tool for agile development
and help ensure that work delivers value to users.

## The User Story Format

The standard format is:

```
As a [type of user],
I want [some goal],
So that [some reason/benefit].
```

### Examples

**Good User Story:**
```
As a registered customer,
I want to save items to my wishlist,
So that I can purchase them later without searching again.
```

**Poor User Story:**
```
Implement wishlist functionality.
```

## INVEST Criteria

Good user stories follow the INVEST criteria, introduced by Bill Wake:

| Criterion | Description |
|-----------|-------------|
| **I**ndependent | Can be developed in any order |
| **N**egotiable | Details can be discussed and refined |
| **V**aluable | Delivers value to users or stakeholders |
| **E**stimable | Team can estimate the effort required |
| **S**mall | Can be completed in one sprint |
| **T**estable | Clear criteria for acceptance |

## Writing Acceptance Criteria

Each user story should have clear acceptance criteria:

```
Given [some precondition],
When [some action is taken],
Then [some result is expected].
```

### Example

```
Story: As a user, I want to reset my password

Acceptance Criteria:
- Given I am on the login page
- When I click "Forgot Password" and enter my email
- Then I receive a password reset link within 5 minutes

- Given I have a valid reset link
- When I enter a new password meeting requirements
- Then my password is updated and I can log in
```

## Story Splitting Techniques

Large stories should be split into smaller ones:

1. **By Workflow Steps**: Split along the happy path
2. **By Business Rules**: Each rule becomes a story
3. **By Data Variations**: Different input types
4. **By Interface**: API vs. UI implementation
5. **By Operations**: Create, Read, Update, Delete

## Common Mistakes

- Stories that are too large (epics disguised as stories)
- Technical tasks written as user stories
- Missing the "so that" benefit clause
- No acceptance criteria defined
- Stories that can't be demonstrated

## Tools and Templates

- Issue templates with user story format
- Story mapping tools (Miro, Mural)
- Backlog management (Jira, GitHub Projects)

## Connecting User Stories to Tests

User stories and their acceptance criteria form the foundation for
acceptance testing. See the **Test Strategies Guide** for:

- **Acceptance Test-Driven Development (ATDD)**: Writing tests before code
- **Behavior-Driven Development (BDD)**: Gherkin syntax and frameworks
- **From criteria to code**: Translating Given-When-Then to executable tests

The acceptance criteria you write using Given-When-Then format can be
directly translated into automated tests using BDD frameworks.

## Further Reading

- "User Stories Applied" by Mike Cohn
- "User Story Mapping" by Jeff Patton
- Agile Alliance resources on user stories
"""
