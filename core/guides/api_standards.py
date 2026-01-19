# core/guides/api_standards.py
# API Standards Guide (v3.0.0)

"""
API Standards Guide.

Provides practical guidance on designing, implementing, and documenting
RESTful APIs following industry best practices.

Introduced in v3.0.0.
"""

GUIDE_ID = "api-standards"

GUIDE = {
    "title": "API Standards Guide",
    "purpose": "Learn how to design and implement consistent APIs",
    "audience": "Backend developers and API designers",
    "complexity": "advanced",
}

RELATED_PRINCIPLES = ["code-review", "versioning"]

CONTENT = """
# API Standards Guide

## Overview

Consistent API design improves:
- Developer experience
- Maintainability
- Integration ease
- Documentation clarity

## URL Design

### Resource Naming

**Use nouns, not verbs:**
```
# Good
GET /users
GET /users/123
GET /users/123/orders

# Bad
GET /getUsers
GET /getUserById/123
POST /createUser
```

**Use plural nouns:**
```
# Good
/users
/products
/orders

# Bad
/user
/product
/order
```

**Use lowercase with hyphens:**
```
# Good
/user-profiles
/order-items

# Bad
/userProfiles
/user_profiles
/UserProfiles
```

### URL Structure

```
https://api.example.com/v1/resources/{id}/sub-resources
└── scheme ──────────┘ └─ version ───┘ └─ path ─────┘

# Examples
GET  /v1/users                    # List users
GET  /v1/users/123                # Get user
POST /v1/users                    # Create user
PUT  /v1/users/123                # Update user
DELETE /v1/users/123              # Delete user
GET  /v1/users/123/orders         # List user's orders
```

## HTTP Methods

### Method Semantics

| Method | Purpose | Idempotent | Safe |
|--------|---------|------------|------|
| GET | Retrieve resource | Yes | Yes |
| POST | Create resource | No | No |
| PUT | Replace resource | Yes | No |
| PATCH | Partial update | No | No |
| DELETE | Remove resource | Yes | No |

### Method Examples

```http
# Create a new user
POST /v1/users
Content-Type: application/json

{
  "name": "Alice",
  "email": "alice@example.com"
}

# Update entire user
PUT /v1/users/123
Content-Type: application/json

{
  "name": "Alice Smith",
  "email": "alice.smith@example.com"
}

# Partial update
PATCH /v1/users/123
Content-Type: application/json

{
  "name": "Alice Smith"
}
```

## HTTP Status Codes

### Success Codes

| Code | Meaning | When to Use |
|------|---------|-------------|
| 200 | OK | Successful GET, PUT, PATCH |
| 201 | Created | Successful POST creating resource |
| 204 | No Content | Successful DELETE |

### Client Error Codes

| Code | Meaning | When to Use |
|------|---------|-------------|
| 400 | Bad Request | Invalid request syntax/body |
| 401 | Unauthorized | Authentication required |
| 403 | Forbidden | Authenticated but not authorized |
| 404 | Not Found | Resource doesn't exist |
| 409 | Conflict | Resource state conflict |
| 422 | Unprocessable Entity | Validation errors |
| 429 | Too Many Requests | Rate limit exceeded |

### Server Error Codes

| Code | Meaning | When to Use |
|------|---------|-------------|
| 500 | Internal Server Error | Unexpected server error |
| 502 | Bad Gateway | Upstream service error |
| 503 | Service Unavailable | Service temporarily down |

## Request/Response Format

### JSON Conventions

```json
{
  "id": "123",
  "created_at": "2024-01-15T10:30:00Z",
  "user_name": "alice",
  "is_active": true,
  "order_count": 5,
  "metadata": {
    "source": "web",
    "campaign_id": "abc123"
  }
}
```

**Conventions:**
- Use snake_case for property names
- Use ISO 8601 for dates: `2024-01-15T10:30:00Z`
- Use strings for IDs (even if numeric)
- Include `null` for missing optional fields

### Collection Responses

```json
{
  "data": [
    {"id": "1", "name": "Alice"},
    {"id": "2", "name": "Bob"}
  ],
  "meta": {
    "total_count": 100,
    "page": 1,
    "per_page": 20,
    "total_pages": 5
  },
  "links": {
    "self": "/v1/users?page=1",
    "next": "/v1/users?page=2",
    "prev": null,
    "first": "/v1/users?page=1",
    "last": "/v1/users?page=5"
  }
}
```

### Single Resource Response

```json
{
  "data": {
    "id": "123",
    "type": "user",
    "attributes": {
      "name": "Alice",
      "email": "alice@example.com",
      "created_at": "2024-01-15T10:30:00Z"
    },
    "relationships": {
      "organization": {
        "data": {"type": "organization", "id": "456"}
      }
    }
  }
}
```

## Error Handling

### Error Response Format

```json
{
  "error": {
    "code": "validation_error",
    "message": "The request body contains invalid data",
    "details": [
      {
        "field": "email",
        "code": "invalid_format",
        "message": "Email must be a valid email address"
      },
      {
        "field": "age",
        "code": "out_of_range",
        "message": "Age must be between 0 and 150"
      }
    ],
    "request_id": "req_abc123",
    "documentation_url": "https://docs.example.com/errors/validation_error"
  }
}
```

### Error Codes

Define consistent error codes:

```python
class ErrorCodes:
    # Authentication
    AUTHENTICATION_REQUIRED = "authentication_required"
    INVALID_TOKEN = "invalid_token"
    TOKEN_EXPIRED = "token_expired"

    # Authorization
    PERMISSION_DENIED = "permission_denied"
    INSUFFICIENT_SCOPE = "insufficient_scope"

    # Validation
    VALIDATION_ERROR = "validation_error"
    INVALID_FORMAT = "invalid_format"
    REQUIRED_FIELD = "required_field"

    # Resources
    RESOURCE_NOT_FOUND = "resource_not_found"
    RESOURCE_ALREADY_EXISTS = "resource_already_exists"

    # Rate Limiting
    RATE_LIMIT_EXCEEDED = "rate_limit_exceeded"
```

## Pagination

### Offset-Based Pagination

```http
GET /v1/users?page=2&per_page=20

Response:
{
  "data": [...],
  "meta": {
    "page": 2,
    "per_page": 20,
    "total_count": 100,
    "total_pages": 5
  }
}
```

### Cursor-Based Pagination

Better for large datasets or real-time data:

```http
GET /v1/users?cursor=eyJpZCI6MTIzfQ&limit=20

Response:
{
  "data": [...],
  "meta": {
    "next_cursor": "eyJpZCI6MTQzfQ",
    "has_more": true
  }
}
```

## Filtering and Sorting

### Filtering

```http
# Simple filters
GET /v1/users?status=active
GET /v1/users?role=admin&status=active

# Comparison operators
GET /v1/orders?created_at[gte]=2024-01-01
GET /v1/products?price[lt]=100

# Multiple values
GET /v1/users?status[in]=active,pending
```

### Sorting

```http
# Single field
GET /v1/users?sort=created_at

# Descending order
GET /v1/users?sort=-created_at

# Multiple fields
GET /v1/users?sort=-created_at,name
```

### Field Selection

```http
# Return only specific fields
GET /v1/users?fields=id,name,email

# Nested fields
GET /v1/users?fields=id,name,organization.name
```

## API Versioning

### URL Path Versioning (Recommended)

```
GET /v1/users
GET /v2/users
```

**Pros:** Clear, easy to implement
**Cons:** URL changes between versions

### Header Versioning

```http
GET /users
Accept: application/vnd.example.v1+json
```

### Query Parameter Versioning

```http
GET /users?version=1
```

### Version Lifecycle

```
v1 (current) -> v2 (next)
   │              │
   │              └── New features, breaking changes
   │
   └── Maintained for 12 months after v2 release
```

## Authentication

### API Key Authentication

```http
GET /v1/users
Authorization: Api-Key sk_live_abc123
```

### Bearer Token (JWT)

```http
GET /v1/users
Authorization: Bearer eyJhbGciOiJIUzI1NiIs...
```

### OAuth 2.0

```http
# Authorization request
GET /oauth/authorize?
  client_id=CLIENT_ID&
  redirect_uri=https://app.example.com/callback&
  response_type=code&
  scope=read:users write:users

# Token exchange
POST /oauth/token
Content-Type: application/x-www-form-urlencoded

grant_type=authorization_code&
code=AUTH_CODE&
client_id=CLIENT_ID&
client_secret=CLIENT_SECRET
```

## Rate Limiting

### Response Headers

```http
HTTP/1.1 200 OK
X-RateLimit-Limit: 1000
X-RateLimit-Remaining: 999
X-RateLimit-Reset: 1640000000
```

### Rate Limit Exceeded Response

```http
HTTP/1.1 429 Too Many Requests
Retry-After: 60
Content-Type: application/json

{
  "error": {
    "code": "rate_limit_exceeded",
    "message": "Rate limit exceeded. Try again in 60 seconds.",
    "retry_after": 60
  }
}
```

## Documentation

### OpenAPI Specification

```yaml
openapi: 3.0.0
info:
  title: Example API
  version: 1.0.0

paths:
  /users:
    get:
      summary: List users
      parameters:
        - name: page
          in: query
          schema:
            type: integer
            default: 1
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/UserList'

components:
  schemas:
    User:
      type: object
      properties:
        id:
          type: string
        name:
          type: string
        email:
          type: string
          format: email
```

### Documentation Requirements

- Clear descriptions for all endpoints
- Request/response examples
- Error code documentation
- Authentication instructions
- Rate limiting information
- Changelog

## Best Practices Summary

### Do

- Use HTTPS always
- Version your API
- Return appropriate status codes
- Include pagination for lists
- Document everything
- Use consistent naming
- Handle errors gracefully

### Don't

- Expose internal IDs without consideration
- Return stack traces in production
- Break backward compatibility without versioning
- Use verbs in URLs
- Ignore caching headers
- Forget rate limiting

---

*This guide complements your project's API documentation and OpenAPI specification*
"""
