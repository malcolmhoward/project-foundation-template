# core/guides/test_strategies.py
# Test Strategies Guide (v3.0.0)

"""
Test Strategies Guide.

Provides practical guidance on implementing effective testing strategies
including unit tests, integration tests, and end-to-end tests.

Introduced in v3.0.0.
"""

GUIDE_ID = "test-strategies"

GUIDE = {
    "title": "Test Strategies Guide",
    "purpose": "Learn how to implement effective testing strategies",
    "audience": "All developers",
    "complexity": "intermediate",
}

RELATED_PRINCIPLES = ["code-review", "ci-workflow"]

CONTENT = """
# Test Strategies Guide

## Overview

A comprehensive testing strategy ensures software quality by catching bugs early,
enabling confident refactoring, and documenting expected behavior.

## The Testing Pyramid

```
        /\\
       /  \\
      / E2E \\        Few, slow, expensive
     /--------\\
    /Integration\\    Some, moderate speed
   /--------------\\
  /   Unit Tests   \\ Many, fast, cheap
 /------------------\\
```

### Unit Tests
- Test individual functions/methods in isolation
- Fast execution (milliseconds)
- High coverage target (80%+)

### Integration Tests
- Test component interactions
- Moderate execution time
- Test database, API, and service integrations

### End-to-End (E2E) Tests
- Test complete user workflows
- Slowest execution
- Test critical paths only

## Unit Testing Best Practices

### Structure: Arrange-Act-Assert

```python
def test_calculate_total_with_discount():
    # Arrange
    cart = ShoppingCart()
    cart.add_item(Item("Widget", 100))
    discount = Discount(percentage=10)

    # Act
    total = cart.calculate_total(discount)

    # Assert
    assert total == 90
```

### Naming Conventions

Use descriptive names that explain:
- What is being tested
- Under what conditions
- Expected outcome

```python
# Good
def test_user_login_with_invalid_password_returns_error():
    ...

def test_calculate_shipping_for_international_orders_adds_customs_fee():
    ...

# Bad
def test_login():
    ...

def test_shipping():
    ...
```

### Test Independence

- Each test should be independent
- No shared mutable state between tests
- Use setup/teardown for common initialization

### What to Test

**Do Test:**
- Edge cases (empty inputs, boundaries)
- Error conditions
- Core business logic
- Complex algorithms

**Don't Test:**
- Third-party libraries
- Trivial getters/setters
- Framework code

## Integration Testing

### Database Integration

```python
@pytest.fixture
def test_db():
    # Setup: Create test database
    db = create_test_database()
    yield db
    # Teardown: Clean up
    db.drop_all()

def test_user_repository_saves_user(test_db):
    repo = UserRepository(test_db)
    user = User(name="Alice", email="alice@example.com")

    saved_user = repo.save(user)

    assert saved_user.id is not None
    assert repo.find_by_id(saved_user.id) == saved_user
```

### API Integration

```python
def test_external_payment_api_processes_valid_card():
    # Use test/sandbox environment
    client = PaymentClient(api_key=TEST_API_KEY)

    result = client.charge(
        amount=1000,
        card_token="tok_test_valid"
    )

    assert result.success is True
    assert result.transaction_id is not None
```

### Best Practices

- Use test databases, not production
- Mock external services when appropriate
- Test both success and failure scenarios
- Clean up test data after each test

## End-to-End Testing

### When to Use E2E Tests

- Critical user journeys (checkout, signup)
- Smoke tests for deployment verification
- Cross-system workflows

### E2E Test Example

```python
def test_user_can_complete_purchase():
    # Navigate to product page
    browser.go_to("/products/widget")

    # Add to cart
    browser.click("#add-to-cart")
    assert browser.find("#cart-count").text == "1"

    # Checkout
    browser.click("#checkout")
    browser.fill("#email", "test@example.com")
    browser.fill("#card", "4242424242424242")
    browser.click("#submit-order")

    # Verify success
    assert "Order Confirmed" in browser.page_title
```

### E2E Best Practices

- Keep E2E tests minimal (test pyramid)
- Use stable selectors (data-testid, not CSS classes)
- Handle async operations properly
- Run in isolated environments

## Test Doubles

### Types of Test Doubles

| Type | Purpose | Example |
|------|---------|---------|
| **Stub** | Returns canned answers | `stub.get_user() -> User("test")` |
| **Mock** | Verifies interactions | `mock.send_email.assert_called_once()` |
| **Fake** | Working implementation | In-memory database |
| **Spy** | Records calls for verification | Wraps real object |

### When to Use Mocks

**Use mocks for:**
- External services (email, payment)
- Time-dependent code
- Random number generation
- Slow operations

**Avoid mocks for:**
- Simple value objects
- Testing internal implementation
- Everything (over-mocking)

## Test Coverage

### Coverage Metrics

- **Line coverage**: Lines executed during tests
- **Branch coverage**: Decision points tested
- **Path coverage**: Execution paths tested

### Setting Coverage Targets

```yaml
# Example coverage configuration
coverage:
  minimum: 80%
  exclude:
    - "tests/*"
    - "migrations/*"
  fail_under: true
```

### Coverage Anti-Patterns

- Chasing 100% coverage blindly
- Writing tests just to increase coverage
- Ignoring mutation testing

## Testing Strategies by Type

### Testing Pure Functions

```python
# Pure functions are easiest to test
def add(a, b):
    return a + b

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
```

### Testing Side Effects

```python
def test_save_user_sends_welcome_email(mock_email_service):
    user_service = UserService(email_service=mock_email_service)

    user_service.create_user("alice@example.com")

    mock_email_service.send.assert_called_once_with(
        to="alice@example.com",
        template="welcome"
    )
```

### Testing Async Code

```python
@pytest.mark.asyncio
async def test_fetch_user_data():
    client = AsyncAPIClient()

    user = await client.get_user(123)

    assert user.id == 123
    assert user.name is not None
```

## Continuous Integration

### Test Automation in CI

```yaml
# Example CI workflow
test:
  steps:
    - run: pip install -r requirements.txt
    - run: pytest --cov=src --cov-report=xml
    - run: coverage report --fail-under=80
```

### Test Categories in CI

- **Fast tests**: Run on every commit
- **Integration tests**: Run on PR
- **E2E tests**: Run before deploy

## Common Testing Mistakes

1. **Testing implementation, not behavior**
   - Focus on what, not how

2. **Flaky tests**
   - Eliminate randomness and race conditions

3. **Slow test suites**
   - Optimize or parallelize

4. **No test isolation**
   - Tests should not affect each other

5. **Over-mocking**
   - Test real behavior when possible

## Test Maintenance

### Keeping Tests Maintainable

- Use descriptive names
- Follow DRY within reason
- Create test utilities/helpers
- Review tests during code review

### When to Delete Tests

- Duplicated coverage
- Testing deleted features
- Consistently flaky with no fix

## Quick Reference

| Test Type | Speed | Isolation | When to Use |
|-----------|-------|-----------|-------------|
| Unit | Fast | Complete | Business logic, algorithms |
| Integration | Medium | Partial | Component interactions |
| E2E | Slow | None | Critical user paths |

---

*This guide complements your project's testing configuration and CI workflow*
"""
