# core/guides/tree_preview.py
# Tree preview guide

"""
Tree Preview Guide.

Provides guidance on documenting project structure with tree previews.
"""

GUIDE_ID = "tree-preview"

GUIDE = {
    "title": "Tree Preview Guide",
    "purpose": "Documenting project structure for navigation and understanding",
    "audience": "Maintainers and technical writers",
    "complexity": "beginner",
}

RELATED_PRINCIPLES = ["readme", "code-standards"]

CONTENT = """
# Tree Preview Guide

## Overview

A tree preview is a visual representation of a project's directory structure.
It helps users and contributors quickly understand how a project is organized
and where to find specific types of files.

## Basic Tree Format

```
project-name/
├── src/
│   ├── main.py
│   └── utils/
│       └── helpers.py
├── tests/
│   └── test_main.py
├── docs/
│   └── README.md
├── .gitignore
├── LICENSE
└── README.md
```

### Tree Characters

| Character | Meaning |
|-----------|---------|
| `├──` | Item with siblings below |
| `└──` | Last item in directory |
| `│` | Vertical connector |
| `/` | Directory indicator |

## Generating Tree Previews

### Using the `tree` Command

**Linux/macOS:**
```bash
tree -L 2 --dirsfirst
```

**Windows (PowerShell):**
```powershell
tree /F
```

### Common Options

```bash
# Limit depth
tree -L 3

# Show only directories
tree -d

# Exclude patterns
tree -I 'node_modules|__pycache__|.git'

# Show hidden files
tree -a

# Output to file
tree > structure.txt
```

## Best Practices

### 1. Keep It Relevant

Show structure that helps understanding, not everything:

**Too Much:**
```
project/
├── node_modules/          # 500+ subdirectories
│   ├── lodash/
│   ├── express/
│   └── ... (500 more)
```

**Just Right:**
```
project/
├── src/                   # Application source
├── tests/                 # Test files
├── docs/                  # Documentation
├── node_modules/          # Dependencies (not shown)
└── package.json
```

### 2. Add Annotations

```
project/
├── src/
│   ├── api/              # REST API endpoints
│   ├── models/           # Database models
│   ├── services/         # Business logic
│   └── utils/            # Helper functions
├── tests/
│   ├── unit/             # Unit tests
│   └── integration/      # Integration tests
└── config/               # Configuration files
```

### 3. Show Key Files

Include important files, not just directories:

```
project/
├── src/
│   └── index.ts          # Application entry point
├── .env.example          # Environment template
├── docker-compose.yml    # Container orchestration
├── Makefile              # Build automation
└── README.md             # Project documentation
```

## Context-Specific Trees

### For Onboarding

Focus on where new contributors should look:

```markdown
## Project Structure

New contributors should focus on:

project/
├── CONTRIBUTING.md       # ← Start here
├── docs/
│   └── development.md    # ← Setup instructions
├── src/
│   └── core/             # ← Main logic lives here
└── tests/                # ← Add tests here
```

### For Architecture Docs

Show component relationships:

```
src/
├── presentation/         # UI Layer
│   ├── components/
│   └── pages/
├── application/          # Use Cases
│   └── services/
├── domain/               # Business Logic
│   ├── entities/
│   └── repositories/
└── infrastructure/       # External Interfaces
    ├── database/
    └── api/
```

### For Security Review

Highlight sensitive areas:

```
project/
├── config/
│   ├── secrets/          # ⚠️ Sensitive - not in git
│   └── public/           # Safe to commit
├── src/
│   └── auth/             # ⚠️ Security-critical
└── .env.example          # Template only, no secrets
```

## Maintenance

- Update tree when structure changes significantly
- Use automation to detect drift (CI check)
- Consider generating from actual structure

## Tools

- `tree` command (Unix/Windows)
- VS Code extensions for file tree generation
- Documentation generators (Sphinx, MkDocs)
- ASCII art generators for custom formatting

## Further Reading

- "Clean Architecture" by Robert C. Martin - Directory structure patterns
- Project structure conventions for your language/framework
- Monorepo structure guides
"""
