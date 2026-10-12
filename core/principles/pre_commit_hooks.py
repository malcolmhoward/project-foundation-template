# core/principles/pre_commit_hooks.py
# Pre-commit hooks principle

"""
Pre-commit Hooks Principle.

Defines the governance principle for automated pre-commit validation.
"""

PRINCIPLE_ID = "pre-commit-hooks"

PRINCIPLE = {
    "name": "Pre-commit Hooks",
    "why": "Catching issues before they enter version control prevents technical debt accumulation",
    "what": "Automated checks that run before each commit to validate code quality",
    "risk": "Without it, broken code, style violations, and secrets enter the repository",
}

EDUCATION = """
📚 LEARNING: Pre-commit hooks provide immediate feedback, catching issues before they enter version control.

## Pre-commit Hooks

### What Are Pre-commit Hooks?

Pre-commit hooks are scripts that run automatically before each commit is finalized.
They act as a first line of defense against common issues entering your codebase.

### Why They Matter

1. **Immediate Feedback**: Developers learn about issues instantly, not in CI/CD
2. **Consistent Quality**: Every commit meets minimum quality standards
3. **Reduced CI Load**: Fewer failing builds from trivial issues
4. **Security Protection**: Secrets and credentials caught before being committed

### Common Pre-commit Checks

- **Linting**: Code style and syntax validation
- **Formatting**: Automatic code formatting (Prettier, Black, gofmt)
- **Type Checking**: Static type analysis (TypeScript, mypy)
- **Secrets Detection**: Scanning for API keys and credentials
- **Test Running**: Quick unit tests for changed files
- **Commit Message Validation**: Enforcing conventional commits

### Implementation Approaches

1. **Git Native Hooks**: Scripts in `.git/hooks/`
2. **pre-commit Framework**: Python-based hook management (pre-commit.com)
3. **Husky**: JavaScript/Node.js hook management
4. **lefthook**: Fast, language-agnostic hook runner

### Best Practices

- Keep hooks fast (under 10 seconds)
- Allow bypass for emergencies (`--no-verify`)
- Document required hooks in CONTRIBUTING.md
- Use shared configuration for team consistency

### Related Resources

- pre-commit.com - Framework documentation
- Git Hooks documentation
- Husky documentation for JavaScript projects
"""
