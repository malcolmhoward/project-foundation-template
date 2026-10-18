# core/principles/performance_standards.py
# Performance Standards principle (v2.10.0)

"""
Performance Standards Principle.

Performance standards define measurable benchmarks that ensure
software meets user expectations for speed and responsiveness.

Introduced in v2.10.0.
"""

PRINCIPLE_ID = "performance-standards"

PRINCIPLE = {
    "name": "Performance Standards",
    "why": "Users abandon software that feels slow",
    "what": "Documented performance budgets, benchmarks, and monitoring practices",
    "risk": "Without performance standards, gradual degradation goes unnoticed until users leave",
}

EDUCATION = """
📚 LEARNING: Small delays add up; agreed performance budgets catch regressions early.

Performance standards make speed a first-class requirement, not an afterthought.
They include:

**Performance Budgets:**
- Page load time targets (e.g., < 3 seconds on 3G)
- Bundle size limits (e.g., < 200KB JavaScript)
- Time to Interactive (TTI) targets
- Core Web Vitals thresholds (LCP, FID, CLS)

**Backend Benchmarks:**
- API response time targets (p50, p95, p99)
- Throughput requirements (requests per second)
- Database query time limits
- Memory and CPU usage bounds

**Monitoring and Alerting:**
- Real User Monitoring (RUM) for actual user experience
- Synthetic monitoring for consistent baselines
- Performance regression detection in CI/CD
- Alerting on budget violations

**Optimization Practices:**
- Code splitting and lazy loading
- Image optimization and responsive images
- Caching strategies (browser, CDN, application)
- Database query optimization and indexing

**Performance Testing:**
- Load testing for capacity planning
- Stress testing for breaking points
- Soak testing for memory leaks
- Baseline comparison in pull requests

Performance is a feature. Treat it like one - with requirements, testing, and
monitoring. The best time to prevent performance problems is before they ship.
"""
