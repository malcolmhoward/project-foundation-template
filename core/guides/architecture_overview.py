# core/guides/architecture_overview.py
# Architecture Overview Guide (v3.2.0)

"""
Architecture Overview Guide.

Provides a high-level overview of the system architecture,
key components, and design decisions.

Introduced in v3.2.0.
"""

GUIDE_ID = "architecture-overview"

GUIDE = {
    "title": "Architecture Overview",
    "purpose": "Document system architecture and design decisions",
    "audience": "Developers and architects",
    "complexity": "intermediate",
}

RELATED_PRINCIPLES = ["adr", "code-standards"]

CONTENT = """
# Architecture Overview

## Purpose

This document provides a high-level overview of the system architecture,
helping developers understand how components interact and why design
decisions were made.

## System Overview

### High-Level Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                        Clients                               │
│  (Web Browser, Mobile App, API Consumers)                   │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                    Load Balancer / CDN                       │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                    API Gateway                               │
│  (Authentication, Rate Limiting, Routing)                   │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                    Application Layer                         │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐   │
│  │ Service  │  │ Service  │  │ Service  │  │ Service  │   │
│  │    A     │  │    B     │  │    C     │  │    D     │   │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘   │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                    Data Layer                                │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐   │
│  │ Primary  │  │  Cache   │  │  Search  │  │  Queue   │   │
│  │    DB    │  │ (Redis)  │  │(Elastic) │  │ (RMQ)    │   │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘   │
└─────────────────────────────────────────────────────────────┘
```

### Key Components

| Component | Technology | Purpose |
|-----------|------------|---------|
| API Gateway | Kong/Nginx | Request routing, auth |
| Application | Python/Node | Business logic |
| Database | PostgreSQL | Persistent storage |
| Cache | Redis | Session, hot data |
| Queue | RabbitMQ | Async processing |
| Search | Elasticsearch | Full-text search |

## Application Architecture

### Layered Architecture

```
┌───────────────────────────────────────┐
│          Presentation Layer           │  ← API endpoints, serialization
├───────────────────────────────────────┤
│           Application Layer           │  ← Use cases, orchestration
├───────────────────────────────────────┤
│            Domain Layer               │  ← Business logic, entities
├───────────────────────────────────────┤
│         Infrastructure Layer          │  ← DB, external services
└───────────────────────────────────────┘
```

**Layer Responsibilities:**

1. **Presentation Layer**
   - Handle HTTP requests/responses
   - Input validation
   - Response formatting
   - Authentication/authorization

2. **Application Layer**
   - Orchestrate use cases
   - Transaction management
   - Cross-cutting concerns

3. **Domain Layer**
   - Business rules and logic
   - Domain entities
   - Value objects
   - Domain services

4. **Infrastructure Layer**
   - Database access
   - External service integration
   - File system operations
   - Message queue interaction

### Directory Structure

```
src/
├── api/                    # Presentation layer
│   ├── routes/             # Route definitions
│   ├── middleware/         # Request middleware
│   └── serializers/        # Response formatting
├── application/            # Application layer
│   ├── services/           # Application services
│   └── dto/                # Data transfer objects
├── domain/                 # Domain layer
│   ├── entities/           # Domain entities
│   ├── repositories/       # Repository interfaces
│   └── services/           # Domain services
└── infrastructure/         # Infrastructure layer
    ├── database/           # Database implementations
    ├── cache/              # Cache implementations
    └── external/           # External service clients
```

## Data Architecture

### Database Schema Overview

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│   users     │────<│   orders    │>────│  products   │
├─────────────┤     ├─────────────┤     ├─────────────┤
│ id          │     │ id          │     │ id          │
│ email       │     │ user_id     │     │ name        │
│ name        │     │ status      │     │ price       │
│ created_at  │     │ total       │     │ stock       │
└─────────────┘     │ created_at  │     └─────────────┘
                    └─────────────┘
                           │
                           ▼
                    ┌─────────────┐
                    │ order_items │
                    ├─────────────┤
                    │ order_id    │
                    │ product_id  │
                    │ quantity    │
                    │ price       │
                    └─────────────┘
```

### Data Flow

```
Request → Validation → Business Logic → Repository → Database
                                              ↑
                                          Cache Check
```

**Caching Strategy:**
- Cache-aside pattern for read-heavy data
- Write-through for critical updates
- TTL-based expiration

## Integration Architecture

### External Services

| Service | Purpose | Integration |
|---------|---------|-------------|
| Payment Gateway | Process payments | REST API |
| Email Service | Notifications | SMTP/API |
| Storage | File uploads | S3 API |
| Analytics | Usage tracking | Events |

### Event-Driven Communication

```
┌──────────┐         ┌──────────┐         ┌──────────┐
│ Service  │ ──────> │  Queue   │ ──────> │ Consumer │
│    A     │  Event  │          │  Event  │          │
└──────────┘         └──────────┘         └──────────┘
```

**Event Types:**
- Domain events (e.g., OrderPlaced)
- Integration events (e.g., PaymentReceived)
- System events (e.g., HealthCheck)

## Security Architecture

### Authentication Flow

```
┌────────┐                    ┌────────┐                    ┌────────┐
│ Client │                    │  Auth  │                    │  API   │
└────────┘                    │ Server │                    │ Server │
     │                        └────────┘                    └────────┘
     │  1. Login Request          │                             │
     │ ─────────────────────────> │                             │
     │                            │                             │
     │  2. JWT Token              │                             │
     │ <───────────────────────── │                             │
     │                            │                             │
     │  3. API Request + Token    │                             │
     │ ───────────────────────────────────────────────────────> │
     │                            │                             │
     │                            │  4. Validate Token          │
     │                            │ <─────────────────────────  │
     │                            │                             │
     │  5. Response               │                             │
     │ <─────────────────────────────────────────────────────── │
```

### Authorization Model

**Role-Based Access Control (RBAC):**

| Role | Permissions |
|------|-------------|
| Admin | Full access |
| Manager | Read/write own domain |
| User | Read/write own data |
| Guest | Read public data |

## Scalability Considerations

### Horizontal Scaling

```
                    ┌──────────┐
                    │   LB     │
                    └──────────┘
                         │
          ┌──────────────┼──────────────┐
          │              │              │
     ┌─────────┐    ┌─────────┐    ┌─────────┐
     │ App 1   │    │ App 2   │    │ App 3   │
     └─────────┘    └─────────┘    └─────────┘
          │              │              │
          └──────────────┼──────────────┘
                         │
                    ┌─────────┐
                    │   DB    │
                    └─────────┘
```

### Database Scaling

- Read replicas for read-heavy workloads
- Connection pooling
- Query optimization
- Consider sharding for large datasets

### Caching Layers

1. **Application cache** - In-memory, fastest
2. **Distributed cache** - Redis, shared state
3. **CDN** - Static assets, geographic distribution

## Monitoring and Observability

### Metrics

- Request rate and latency
- Error rates
- Resource utilization
- Business metrics

### Logging

- Structured JSON logs
- Correlation IDs for tracing
- Log levels (DEBUG, INFO, WARN, ERROR)

### Tracing

- Distributed tracing with OpenTelemetry
- Request flow visualization
- Performance bottleneck identification

## Deployment Architecture

### Environment Progression

```
Development → Staging → Production
     │            │          │
     │            │          └── Blue/Green deployment
     │            └── Integration testing
     └── Local development
```

### Infrastructure as Code

- Terraform for infrastructure
- Docker for containerization
- Kubernetes for orchestration

## Decision Records

Architecture decisions are documented in ADRs (Architecture Decision Records)
located in `docs/adr/`. Key decisions include:

- ADR-001: Monolith vs Microservices
- ADR-002: Database Selection
- ADR-003: Authentication Strategy
- ADR-004: Caching Approach

## Further Reading

- **Code Standards** - Development conventions
- **Deployment Guide** - Deployment procedures
- **API Documentation** - Endpoint specifications
- **Security Policy** - Security requirements

---

*This document should be updated when significant architectural changes are made.*
"""
