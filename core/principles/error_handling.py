# core/principles/error_handling.py
# Error handling principle

"""
Error Handling Principle.

Defines the governance principle for consistent error handling practices.
"""

PRINCIPLE_ID = "error-handling"

PRINCIPLE = {
    "name": "Error Handling Standards",
    "why": "Consistent error handling improves debugging, user experience, and system reliability",
    "what": "Documented standards for how errors are caught, logged, and communicated",
    "risk": "Without it, silent failures, poor user experience, and difficult debugging",
}

EDUCATION = """
📚 LEARNING: Consistent error handling patterns make debugging easier and improve user experience.

## Error Handling Standards

### What Is Error Handling?

Error handling encompasses how a system detects, responds to, and recovers from
unexpected conditions or failures during execution.

### Why Standards Matter

1. **Debugging Efficiency**: Consistent patterns make issues easier to trace
2. **User Experience**: Clear error messages help users understand and recover
3. **System Reliability**: Proper handling prevents cascading failures
4. **Security**: Avoid exposing sensitive information in error messages

### Error Handling Principles

1. **Fail Fast**: Detect and report errors as early as possible
2. **Fail Safely**: Ensure system remains in a valid state after errors
3. **Be Specific**: Use specific exception types, not generic catches
4. **Log Appropriately**: Include context without sensitive data
5. **Communicate Clearly**: User-facing messages should be actionable

### Common Patterns

- **Try-Catch-Finally**: Standard exception handling
- **Result Types**: Explicit success/failure return values (Rust, Go)
- **Error Boundaries**: Isolating failure domains (React)
- **Circuit Breakers**: Preventing cascade failures in distributed systems
- **Retry with Backoff**: Handling transient failures

### Anti-Patterns to Avoid

- Swallowing exceptions silently
- Catching generic Exception types
- Exposing stack traces to end users
- Logging sensitive information
- Ignoring error return values

### Error Message Guidelines

Good error messages include:
- What happened (the error)
- Why it happened (if known)
- How to fix it (actionable next steps)
- Where to get help (documentation links)

### Further Reading

- "Clean Code" by Robert C. Martin - Chapter on Error Handling
- "The Pragmatic Programmer" by Hunt and Thomas - Error Handling sections
- Language-specific error handling guides in official documentation
"""
