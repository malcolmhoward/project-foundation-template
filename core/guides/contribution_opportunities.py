# core/guides/contribution_opportunities.py
# Contribution opportunities guide

"""
Contribution Opportunities Guide.

Provides guidance on creating and managing contribution opportunities for open source.
"""

GUIDE_ID = "contribution-opportunities"

GUIDE = {
    "title": "Contribution Opportunities Guide",
    "purpose": "Creating welcoming contribution paths for open source projects",
    "audience": "Maintainers and community managers",
    "complexity": "intermediate",
}

RELATED_PRINCIPLES = ["contributing", "code-of-conduct", "maintainers"]

CONTENT = """
# Contribution Opportunities Guide

## Overview

Creating clear contribution opportunities helps grow your contributor community.
Good first issues, documentation needs, and feature requests all serve different
contributor skill levels and interests.

## Types of Contributions

### Code Contributions

| Type | Skill Level | Examples |
|------|-------------|----------|
| Bug fixes | Beginner-Intermediate | Typos, edge cases, error handling |
| Features | Intermediate-Advanced | New functionality, integrations |
| Refactoring | Advanced | Architecture improvements |
| Performance | Advanced | Optimization, profiling |

### Non-Code Contributions

| Type | Skill Level | Examples |
|------|-------------|----------|
| Documentation | Beginner | Typos, clarifications, examples |
| Translation | Beginner | i18n content |
| Design | Intermediate | UI/UX improvements, icons |
| Testing | Beginner-Intermediate | Bug reports, test cases |
| Triage | Intermediate | Issue management, reproduction |
| Community | All levels | Answering questions, mentoring |

## Issue Labels for Contributors

### Standard Labels

```
good first issue     - Great for newcomers
help wanted          - Community help welcome
documentation        - Docs improvements needed
bug                  - Something isn't working
enhancement          - New feature or request
question             - Further information requested
```

### Skill-Based Labels

```
difficulty: easy     - Minimal codebase knowledge needed
difficulty: medium   - Some familiarity required
difficulty: hard     - Deep understanding needed
area: frontend       - UI/browser code
area: backend        - Server/API code
area: docs           - Documentation
```

## Creating Good First Issues

### Checklist

- [ ] Clear problem statement
- [ ] Expected behavior defined
- [ ] Relevant files/functions identified
- [ ] Links to related documentation
- [ ] Mentor available (optional)
- [ ] Estimated time/effort

### Template

```markdown
## Summary
[One sentence description]

## Current Behavior
[What happens now]

## Expected Behavior
[What should happen]

## Getting Started

1. Look at `src/module/file.py`
2. The function `process_data()` needs updating
3. See the related test in `tests/test_module.py`

## Resources
- [Contributing Guide](/CONTRIBUTING.md)
- [Development Setup](/docs/development.md)

## Mentorship
@maintainer is available to help with this issue.

Labels: good first issue, help wanted, difficulty: easy
```

## Contributor Pathways

### The Contributor Ladder

```
First-time Contributor
        ↓
    Contributor (multiple PRs merged)
        ↓
    Regular Contributor (sustained activity)
        ↓
    Maintainer (commit access)
        ↓
    Core Maintainer (governance role)
```

### Recognition

- Acknowledge contributions in release notes
- Add to CONTRIBUTORS.md or AUTHORS
- Highlight contributors in community channels
- Provide references for job applications

## Maintaining Contribution Health

### Metrics to Track

- Time to first response on issues/PRs
- Time to merge for first-time contributors
- Number of unique contributors per month
- Good first issue availability
- Contributor retention rate

### Warning Signs

- No good first issues available
- Issues sitting without response > 7 days
- Contributors not returning after first PR
- Same few people doing all reviews

## Outreach Strategies

1. **Hacktoberfest**: Prepare issues for October
2. **GSoC/Outreachy**: Define mentor projects
3. **Conference Sprints**: Prepare for code sprints
4. **University Partnerships**: Capstone projects
5. **Company Programs**: Corporate contributor programs

## Further Reading

- GitHub's documentation on building communities
- Open Source Guides (opensource.guide)
- First Timers Only initiative
"""
