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

RELATED_PRINCIPLES = ["code-review", "ci-workflow", "quality-assurance"]

RELATED_GUIDES = ["user-stories"]

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

## Acceptance Test-Driven Development (ATDD)

ATDD connects user stories to executable tests, ensuring that development
is driven by user requirements. See the **User Stories Guide** for writing
effective user stories and acceptance criteria.

### The ATDD Cycle

```
User Story → Acceptance Criteria → Executable Tests → Implementation → Refactor
     ↑                                                                    |
     └────────────────────────────────────────────────────────────────────┘
```

### From User Story to Test

**User Story:**
```
As a registered customer,
I want to reset my password,
So that I can regain access to my account.
```

**Acceptance Criteria (Given-When-Then):**
```
Given I am on the login page
When I click "Forgot Password" and enter my email
Then I receive a password reset link within 5 minutes
```

**Executable Test:**
```python
def test_password_reset_sends_email():
    # Given: User on login page
    user = create_user(email="alice@example.com")

    # When: Request password reset
    response = client.post("/forgot-password", {"email": user.email})

    # Then: Email sent within time limit
    assert response.status_code == 200
    assert email_service.was_called_with(to=user.email)
    assert email_contains_reset_link(user.email)
```

### Behavior-Driven Development (BDD)

BDD extends ATDD with a shared language between developers, testers, and
business stakeholders. Tests are written in natural language format.

**Gherkin Syntax Example:**
```gherkin
Feature: Password Reset
  As a registered customer
  I want to reset my password
  So that I can regain access to my account

  Scenario: Successful password reset request
    Given I am a registered user with email "alice@example.com"
    And I am on the login page
    When I click "Forgot Password"
    And I enter my email address
    And I click "Send Reset Link"
    Then I should see "Check your email for a reset link"
    And a password reset email should be sent to "alice@example.com"

  Scenario: Password reset with unregistered email
    Given I am on the login page
    When I click "Forgot Password"
    And I enter "unknown@example.com"
    And I click "Send Reset Link"
    Then I should see "If this email exists, a reset link will be sent"
    And no email should be sent
```

### BDD Frameworks by Language

| Language | Framework | Notes |
|----------|-----------|-------|
| Python | Behave, pytest-bdd | Gherkin support |
| JavaScript | Cucumber.js, Jest-Cucumber | Node.js ecosystem |
| Ruby | Cucumber | Original BDD framework |
| Java | Cucumber-JVM | JUnit integration |
| .NET | SpecFlow | Visual Studio integration |
| Go | Godog | Gherkin for Go |

### ATDD Best Practices

1. **Write acceptance tests before implementation**
   - Tests define "done" for the feature
   - Prevents scope creep

2. **Collaborate on acceptance criteria**
   - Include product owner, developers, and testers
   - "Three Amigos" sessions

3. **Keep scenarios focused**
   - One behavior per scenario
   - Avoid testing multiple things at once

4. **Use domain language**
   - Write in terms users understand
   - Avoid technical implementation details

5. **Maintain living documentation**
   - Scenarios document system behavior
   - Keep them updated as features evolve

### When to Use ATDD/BDD

**Good fit:**
- User-facing features with clear acceptance criteria
- Complex business rules
- Cross-functional teams needing shared understanding
- Regulated environments requiring traceability

**Less suitable:**
- Low-level technical components
- Rapid prototyping phases

## Performance Testing

Performance testing validates that your application meets speed, scalability,
and stability requirements under expected and peak conditions.

### Types of Performance Tests

| Type | Purpose | Key Question |
|------|---------|--------------|
| **Load Testing** | Test under expected load | Can we handle normal traffic? |
| **Stress Testing** | Test beyond capacity | Where does it break? |
| **Spike Testing** | Test sudden load increases | Can we handle traffic bursts? |
| **Endurance Testing** | Test over extended periods | Are there memory leaks? |
| **Scalability Testing** | Test scaling behavior | Does adding resources help? |

### Load Testing Example

```python
# Using locust framework
from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    wait_time = between(1, 3)  # Wait 1-3 seconds between tasks

    @task(3)  # Weight: 3x more likely than other tasks
    def view_homepage(self):
        self.client.get("/")

    @task(2)
    def view_product(self):
        self.client.get("/products/123")

    @task(1)
    def checkout(self):
        self.client.post("/checkout", json={"product_id": 123})
```

### Performance Testing Tools

| Tool | Language | Use Case |
|------|----------|----------|
| Locust | Python | Scriptable load testing |
| k6 | JavaScript | Developer-centric load testing |
| JMeter | Java | Enterprise load testing |
| Gatling | Scala | High-performance testing |
| Artillery | JavaScript | Modern load testing |
| wrk | C | HTTP benchmarking |

### Key Performance Metrics

- **Response Time**: How long requests take (p50, p95, p99)
- **Throughput**: Requests per second (RPS)
- **Error Rate**: Percentage of failed requests
- **Concurrent Users**: Simultaneous active users
- **Resource Utilization**: CPU, memory, network usage

### Performance Test Example with Metrics

```yaml
# k6 test configuration
scenarios:
  average_load:
    executor: ramping-vus
    startVUs: 0
    stages:
      - duration: 2m
        target: 100    # Ramp up to 100 users
      - duration: 5m
        target: 100    # Stay at 100 users
      - duration: 2m
        target: 0      # Ramp down

thresholds:
  http_req_duration: ['p(95)<500']  # 95% of requests under 500ms
  http_req_failed: ['rate<0.01']    # Less than 1% errors
```

### Performance Testing Best Practices

1. **Test in production-like environments**
   - Match hardware, data volume, and configuration
   - Use realistic test data

2. **Establish baselines**
   - Measure current performance before changes
   - Track trends over time

3. **Test early and often**
   - Include in CI/CD pipeline
   - Catch regressions quickly

4. **Monitor during tests**
   - Watch server metrics (CPU, memory, I/O)
   - Identify bottlenecks

5. **Use realistic scenarios**
   - Model actual user behavior
   - Include think time between actions

### When to Performance Test

- Before major releases
- After significant code changes
- When infrastructure changes
- During capacity planning
- After performance incidents

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
