# core/principles/container_support.py
# Container Support principle (v3.0.0)

"""
Container Support Principle.

Container support enables consistent deployment across environments,
improving development workflows and production reliability.

Introduced in v3.0.0.
"""

PRINCIPLE_ID = "container-support"

PRINCIPLE = {
    "name": "Container Support",
    "why": "Containers eliminate 'works on my machine' problems and enable consistent deployments",
    "what": "Dockerfiles, compose configurations, and container best practices",
    "risk": "Without containerization, deployments are inconsistent and environment setup is error-prone",
}

EDUCATION = """
📚 LEARNING: 92% of organizations use containers in production, up from 23% in 2016.

Containers package applications with their dependencies, ensuring consistent
behavior from development laptop to production cluster. Best practices include:

**Dockerfile Best Practices:**
- Use official base images from trusted registries
- Pin specific image versions (not 'latest')
- Multi-stage builds to minimize final image size
- Run as non-root user for security
- Order instructions for optimal layer caching

**Security Considerations:**
- Scan images for vulnerabilities before deployment
- Use minimal base images (Alpine, distroless)
- Never embed secrets in images
- Implement read-only filesystems where possible
- Set resource limits (CPU, memory)

**Development Workflow:**
- Docker Compose for local multi-service development
- Consistent development and production configurations
- Volume mounts for code hot-reloading in development

**Production Readiness:**
- Health checks for orchestrator integration
- Graceful shutdown signal handling
- Structured logging to stdout/stderr
- Externalized configuration via environment variables

Containers are the standard deployment unit. Supporting them isn't optional
for modern projects - it's expected.
"""
