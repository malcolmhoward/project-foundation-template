# core/guides/developer_handbook.py
# Developer Handbook Guide (v3.2.0)

"""
Developer Handbook Guide.

A comprehensive reference for developers working on the project,
covering standards, practices, and conventions.

Introduced in v3.2.0.
"""

GUIDE_ID = "developer-handbook"

GUIDE = {
    "title": "Developer Handbook",
    "purpose": "Comprehensive reference for project development standards and practices",
    "audience": "All developers",
    "complexity": "intermediate",
}

RELATED_PRINCIPLES = ["code-standards", "contributing", "quality-assurance"]

CONTENT = """
# Developer Handbook

## Purpose

This handbook serves as the authoritative reference for development practices,
standards, and conventions used in this project. All team members should be
familiar with its contents.

## Code Standards

### Formatting

**General Rules:**
- Use consistent indentation (spaces or tabs as per project config)
- Maximum line length: 100 characters (80 for comments)
- Use meaningful whitespace to separate logical blocks
- End files with a single newline

**File Organization:**
```
1. License/copyright header (if required)
2. Module docstring
3. Imports (standard library, third-party, local)
4. Constants
5. Type definitions
6. Classes
7. Functions
8. Main block (if applicable)
```

### Naming Conventions

| Element | Style | Example |
|---------|-------|---------|
| Variables | snake_case | `user_count` |
| Functions | snake_case | `calculate_total()` |
| Classes | PascalCase | `UserManager` |
| Constants | UPPER_SNAKE | `MAX_RETRIES` |
| Private | _leading_underscore | `_internal_state` |
| Files | snake_case | `user_service.py` |

### Documentation

**Functions and Methods:**
```python
def process_data(input_data: dict, options: dict = None) -> Result:
    \"\"\"Process input data according to specified options.

    Args:
        input_data: Dictionary containing raw data to process.
        options: Optional configuration. Defaults to None.
            - validate: Whether to validate input (default: True)
            - transform: Transformation function to apply

    Returns:
        Result object containing processed data and metadata.

    Raises:
        ValidationError: If input_data fails validation.
        ProcessingError: If processing cannot complete.

    Example:
        >>> result = process_data({'key': 'value'})
        >>> print(result.status)
        'success'
    \"\"\"
```

**Classes:**
```python
class DataProcessor:
    \"\"\"Processes data according to configured rules.

    This class handles data transformation, validation, and storage.
    It supports both synchronous and asynchronous operation modes.

    Attributes:
        config: Configuration dictionary for processing rules.
        stats: Processing statistics and metrics.

    Example:
        >>> processor = DataProcessor(config={'mode': 'strict'})
        >>> processor.process(data)
    \"\"\"
```

## Development Workflow

### Branch Strategy

```
main ────●─────●─────●─────●─────
          \\   /   \\     /
develop    ●─●     ●───●
            \\       \\
feature/x    ●───●   ●───●
```

**Branch Types:**
- `main` - Production-ready code
- `develop` - Integration branch (if used)
- `feature/*` - New features
- `fix/*` - Bug fixes
- `hotfix/*` - Urgent production fixes
- `release/*` - Release preparation

### Commit Practices

**Conventional Commits:**
```
<type>(<scope>): <subject>

[optional body]

[optional footer]
```

**Types:**
- `feat` - New feature
- `fix` - Bug fix
- `docs` - Documentation
- `style` - Formatting, no code change
- `refactor` - Code restructuring
- `test` - Adding tests
- `chore` - Maintenance

**Good Commit Messages:**
```
feat(auth): add password strength validation

- Add zxcvbn library for password scoring
- Require minimum score of 3 for registration
- Display strength indicator in UI

Closes #234
```

### Code Review

**Before Requesting Review:**
- [ ] All tests pass locally
- [ ] Code is self-reviewed
- [ ] Documentation updated
- [ ] Changelog entry added (if applicable)
- [ ] PR description is complete

**Review Focus Areas:**
1. **Correctness** - Does it work as intended?
2. **Design** - Is the approach sound?
3. **Readability** - Is it clear and maintainable?
4. **Testing** - Are tests adequate?
5. **Security** - Any vulnerabilities introduced?

## Testing Standards

### Test Organization

```
tests/
├── unit/           # Isolated component tests
├── integration/    # Multi-component tests
├── e2e/            # End-to-end tests
├── fixtures/       # Test data
└── conftest.py     # Shared fixtures
```

### Test Naming

```python
# Pattern: test_<what>_<condition>_<expected>
def test_login_with_valid_credentials_succeeds():
    pass

def test_login_with_invalid_password_returns_401():
    pass

def test_user_creation_without_email_raises_validation_error():
    pass
```

### Test Coverage

**Minimum Requirements:**
- Unit tests: 80% coverage
- Critical paths: 100% coverage
- New code: Must include tests

**What to Test:**
- Happy paths
- Error conditions
- Edge cases
- Boundary values

## Error Handling

### Principles

1. **Fail fast** - Detect and report errors early
2. **Be specific** - Use appropriate error types
3. **Provide context** - Include helpful error messages
4. **Don't swallow errors** - Log or propagate appropriately

### Error Hierarchy

```python
class ApplicationError(Exception):
    \"\"\"Base error for application-specific exceptions.\"\"\"
    pass

class ValidationError(ApplicationError):
    \"\"\"Input validation failed.\"\"\"
    pass

class NotFoundError(ApplicationError):
    \"\"\"Requested resource not found.\"\"\"
    pass

class AuthorizationError(ApplicationError):
    \"\"\"User lacks required permissions.\"\"\"
    pass
```

### Error Messages

**Good:**
```python
raise ValidationError(
    f"Email '{email}' is invalid: {reason}. "
    f"Expected format: user@domain.com"
)
```

**Bad:**
```python
raise Exception("Invalid input")
```

## Logging Standards

### Log Levels

| Level | Use Case |
|-------|----------|
| DEBUG | Detailed diagnostic information |
| INFO | Routine operational messages |
| WARNING | Unexpected but handled situations |
| ERROR | Failures that need attention |
| CRITICAL | System-wide failures |

### Log Format

```python
import logging

logger = logging.getLogger(__name__)

# Include relevant context
logger.info(
    "User action completed",
    extra={
        "user_id": user.id,
        "action": "purchase",
        "item_id": item.id,
        "duration_ms": elapsed
    }
)
```

### What to Log

**Do Log:**
- Authentication attempts
- Authorization decisions
- Data modifications
- External service calls
- Error conditions

**Don't Log:**
- Passwords or tokens
- Personal data (unless required)
- High-frequency debug info in production

## Security Practices

### Input Validation

- Validate all external input
- Use allowlists over denylists
- Sanitize before use
- Validate on both client and server

### Authentication

- Use established libraries
- Implement proper session management
- Enforce strong passwords
- Support multi-factor authentication

### Data Protection

- Encrypt sensitive data at rest
- Use TLS for data in transit
- Minimize data collection
- Implement proper access controls

## Performance Guidelines

### Code Efficiency

- Profile before optimizing
- Choose appropriate data structures
- Avoid premature optimization
- Cache expensive operations

### Database

- Use indexes appropriately
- Avoid N+1 queries
- Use connection pooling
- Optimize query patterns

### API Design

- Implement pagination
- Support filtering
- Use appropriate caching headers
- Consider rate limiting

## Dependencies

### Adding Dependencies

Before adding a new dependency:
1. Check if functionality exists in standard library
2. Evaluate maintenance status
3. Check license compatibility
4. Review security history
5. Consider bundle size impact

### Version Pinning

```
# Pin exact versions for reproducibility
requests==2.28.1

# Or use compatible release
requests~=2.28.1
```

## Environment Configuration

### Environment Variables

```bash
# Required
DATABASE_URL=postgresql://user:pass@host:5432/db
API_KEY=your-api-key

# Optional with defaults
LOG_LEVEL=INFO
DEBUG=false
```

### Configuration Files

```yaml
# config/default.yml
app:
  name: MyApp
  version: 1.0.0

database:
  pool_size: 10
  timeout: 30
```

## Troubleshooting

### Common Issues

**Build Failures:**
1. Clear cache: `npm cache clean --force`
2. Remove node_modules and reinstall
3. Check Node.js version compatibility

**Test Failures:**
1. Check test isolation
2. Verify test data setup
3. Review recent changes

**Performance Issues:**
1. Check database queries
2. Review external service calls
3. Profile application code

### Getting Help

1. Check this handbook and project documentation
2. Search existing issues
3. Ask in team chat
4. Escalate to tech lead if blocked

---

*This handbook is a living document. Suggest improvements via PR.*
"""
