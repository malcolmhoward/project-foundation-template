# core/guides/coding_standards.py
# Coding Standards Guide (v3.0.0)

"""
Coding Standards Guide.

Provides practical guidance on writing clean, maintainable, and
consistent code following established best practices.

Introduced in v3.0.0.
"""

GUIDE_ID = "coding-standards"

GUIDE = {
    "title": "Coding Standards Guide",
    "purpose": "Learn how to write clean and consistent code",
    "audience": "All developers",
    "complexity": "intermediate",
}

RELATED_PRINCIPLES = ["code-review", "contributing"]

CONTENT = """
# Coding Standards Guide

## Overview

Consistent coding standards improve:
- Code readability
- Team collaboration
- Maintenance efficiency
- Bug prevention

## General Principles

### Write Readable Code

Code is read more often than it is written. Prioritize clarity.

```python
# Bad - unclear intent
def calc(x, y, z):
    return x * y * (1 - z)

# Good - self-documenting
def calculate_discounted_total(unit_price, quantity, discount_rate):
    return unit_price * quantity * (1 - discount_rate)
```

### Keep Functions Small

Functions should do one thing and do it well.

```python
# Bad - does too much
def process_order(order):
    # Validate
    if not order.items:
        raise ValueError("Empty order")
    # Calculate total
    total = sum(item.price * item.quantity for item in order.items)
    # Apply discount
    if order.coupon:
        total *= (1 - order.coupon.discount)
    # Save to database
    db.save(order)
    # Send email
    email.send_confirmation(order)
    return total

# Good - single responsibility
def validate_order(order):
    if not order.items:
        raise ValueError("Empty order")

def calculate_order_total(order):
    subtotal = sum(item.price * item.quantity for item in order.items)
    return apply_discount(subtotal, order.coupon)

def process_order(order):
    validate_order(order)
    total = calculate_order_total(order)
    order_repository.save(order)
    notification_service.send_confirmation(order)
    return total
```

### Avoid Deep Nesting

Flatten nested conditionals using early returns.

```python
# Bad - deep nesting
def process_user(user):
    if user:
        if user.is_active:
            if user.has_permission:
                return do_something(user)
            else:
                raise PermissionError()
        else:
            raise InactiveUserError()
    else:
        raise UserNotFoundError()

# Good - early returns
def process_user(user):
    if not user:
        raise UserNotFoundError()
    if not user.is_active:
        raise InactiveUserError()
    if not user.has_permission:
        raise PermissionError()
    return do_something(user)
```

## Naming Conventions

### Variables

Use descriptive, meaningful names:

```python
# Bad
d = 7  # days
u = get_user()
temp = calculate_result()

# Good
days_until_expiry = 7
current_user = get_user()
monthly_revenue = calculate_result()
```

### Functions/Methods

Use verbs that describe the action:

```python
# Bad
def user_data():
    pass

def string(number):
    pass

# Good
def get_user_data():
    pass

def format_as_string(number):
    pass

# Common prefixes
get_    # Retrieve a value
set_    # Assign a value
is_     # Boolean check
has_    # Boolean check
can_    # Permission check
create_ # Create new entity
update_ # Modify existing entity
delete_ # Remove entity
find_   # Search for entity
```

### Classes

Use nouns in PascalCase:

```python
# Bad
class manage_users:
    pass

class userData:
    pass

# Good
class UserManager:
    pass

class UserData:
    pass
```

### Constants

Use SCREAMING_SNAKE_CASE:

```python
MAX_RETRY_ATTEMPTS = 3
DEFAULT_TIMEOUT_SECONDS = 30
API_BASE_URL = "https://api.example.com"
```

### File Names

Use snake_case for Python, kebab-case for URLs:

```
# Python files
user_service.py
test_user_service.py

# URLs/routes
/api/user-profiles
/api/order-items
```

## Code Organization

### File Structure

Group related code together:

```python
# 1. Imports (standard library, third-party, local)
import os
from datetime import datetime

import requests
from flask import Flask

from .models import User
from .utils import format_date

# 2. Constants
DEFAULT_PAGE_SIZE = 20

# 3. Classes/Functions
class UserService:
    pass

def helper_function():
    pass
```

### Import Organization

```python
# Standard library imports
import os
import sys
from typing import List, Optional

# Third-party imports
import requests
from flask import Flask, request

# Local imports
from .models import User
from .services import UserService
```

### Class Organization

```python
class UserService:
    # Class constants
    DEFAULT_ROLE = "user"

    # Constructor
    def __init__(self, repository):
        self.repository = repository

    # Public methods
    def get_user(self, user_id: str) -> User:
        return self.repository.find(user_id)

    def create_user(self, data: dict) -> User:
        user = self._build_user(data)
        return self.repository.save(user)

    # Private methods
    def _build_user(self, data: dict) -> User:
        return User(**data)
```

## Comments and Documentation

### When to Comment

**Do comment:**
- Why something is done (not what)
- Complex algorithms
- Non-obvious workarounds
- Public APIs

**Don't comment:**
- What the code does (if readable)
- Obvious operations
- Commented-out code (delete it)

```python
# Bad - obvious
# Increment counter by 1
counter += 1

# Bad - what instead of why
# Check if user is admin
if user.role == "admin":

# Good - explains why
# Skip validation for admin users as they have elevated privileges
if user.role == "admin":
    return True
```

### Documentation Strings

```python
def calculate_shipping_cost(
    weight: float,
    destination: str,
    express: bool = False
) -> float:
    # Calculate shipping cost based on package weight and destination.
    #
    # Args:
    #     weight: Package weight in kilograms
    #     destination: Two-letter country code (ISO 3166-1)
    #     express: If True, use express shipping rates
    #
    # Returns:
    #     Calculated shipping cost in USD
    #
    # Raises:
    #     ValueError: If weight is negative or destination is invalid
    #
    # Example:
    #     >>> calculate_shipping_cost(2.5, "US", express=True)
    #     15.99
    pass
```

## Error Handling

### Be Specific with Exceptions

```python
# Bad - generic exception
try:
    user = get_user(user_id)
except Exception:
    return None

# Good - specific exception handling
try:
    user = get_user(user_id)
except UserNotFoundError:
    logger.info(f"User {user_id} not found")
    return None
except DatabaseConnectionError as e:
    logger.error(f"Database error: {e}")
    raise ServiceUnavailableError("Database unavailable")
```

### Fail Fast

```python
def process_payment(amount: float, card: CreditCard) -> Transaction:
    # Validate inputs immediately
    if amount <= 0:
        raise ValueError("Amount must be positive")
    if card.is_expired():
        raise CardExpiredError("Card has expired")

    # Proceed with processing
    return payment_gateway.charge(amount, card)
```

### Don't Swallow Exceptions

```python
# Bad - hides errors
try:
    process_data(data)
except Exception:
    pass  # What happened?

# Good - log and handle appropriately
try:
    process_data(data)
except DataValidationError as e:
    logger.warning(f"Invalid data: {e}")
    return ValidationResult(success=False, errors=e.errors)
except Exception as e:
    logger.exception("Unexpected error processing data")
    raise
```

## Type Hints

### Use Type Annotations

```python
from typing import List, Optional, Dict

def get_users(
    active_only: bool = True,
    limit: Optional[int] = None
) -> List[User]:
    pass

def process_config(config: Dict[str, any]) -> None:
    pass

class UserService:
    def __init__(self, repository: UserRepository) -> None:
        self.repository = repository

    def find_by_email(self, email: str) -> Optional[User]:
        pass
```

## Code Smells to Avoid

### Magic Numbers

```python
# Bad
if retry_count > 3:
    raise MaxRetriesExceeded()

# Good
MAX_RETRY_ATTEMPTS = 3

if retry_count > MAX_RETRY_ATTEMPTS:
    raise MaxRetriesExceeded()
```

### Long Parameter Lists

```python
# Bad
def create_user(name, email, age, address, city, country, phone, role):
    pass

# Good - use an object
@dataclass
class CreateUserRequest:
    name: str
    email: str
    age: int
    address: Address
    phone: str
    role: str

def create_user(request: CreateUserRequest):
    pass
```

### Boolean Parameters

```python
# Bad - unclear at call site
process_order(order, True, False)

# Good - explicit named parameters
process_order(order, send_notification=True, require_payment=False)

# Better - separate functions if behavior differs significantly
process_order(order)
process_order_with_notification(order)
```

### Duplicate Code

```python
# Bad - duplication
def get_admin_users():
    users = db.query(User).filter(role="admin").all()
    return [{"id": u.id, "name": u.name} for u in users]

def get_regular_users():
    users = db.query(User).filter(role="user").all()
    return [{"id": u.id, "name": u.name} for u in users]

# Good - extract common logic
def get_users_by_role(role: str):
    users = db.query(User).filter(role=role).all()
    return [{"id": u.id, "name": u.name} for u in users]

def get_admin_users():
    return get_users_by_role("admin")
```

## Testing Considerations

### Write Testable Code

```python
# Bad - hard to test (creates its own dependencies)
class OrderService:
    def __init__(self):
        self.db = DatabaseConnection()
        self.email = EmailService()

    def process(self, order):
        self.db.save(order)
        self.email.send(order.user.email, "Order confirmed")

# Good - dependency injection
class OrderService:
    def __init__(self, repository: OrderRepository, notifier: Notifier):
        self.repository = repository
        self.notifier = notifier

    def process(self, order):
        self.repository.save(order)
        self.notifier.notify(order.user, "Order confirmed")
```

## Formatting

### Use Automated Formatters

Configure your project with:
- **Python:** Black, isort
- **JavaScript:** Prettier, ESLint
- **Go:** gofmt

```json
// .prettierrc
{
  "semi": true,
  "singleQuote": true,
  "tabWidth": 2
}
```

```toml
# pyproject.toml
[tool.black]
line-length = 88

[tool.isort]
profile = "black"
```

### Consistent Line Length

Keep lines under 88-120 characters for readability.

---

*This guide complements your project's linting configuration and code review process*
"""
