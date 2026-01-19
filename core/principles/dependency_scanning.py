# core/principles/dependency_scanning.py
# Dependency Scanning principle (v3.0.0)

"""
Dependency Scanning Principle.

Dependency scanning identifies vulnerabilities in third-party packages,
protecting projects from supply chain attacks and known CVEs.

Introduced in v3.0.0.
"""

PRINCIPLE_ID = "dependency-scanning"

PRINCIPLE = {
    "name": "Dependency Scanning",
    "why": "96% of codebases contain open source dependencies, and 84% have at least one known vulnerability",
    "what": "Automated scanning of dependencies for known vulnerabilities with update workflows",
    "risk": "Without scanning, projects inherit vulnerabilities from their dependencies",
}

EDUCATION = """
📚 LEARNING: Supply chain attacks increased 742% from 2019 to 2022.

Modern software is built on a foundation of open source dependencies. Each
dependency is a potential entry point for attackers. Dependency scanning
addresses this through:

**Vulnerability Detection:**
- Scan dependencies against CVE databases (NVD, GitHub Advisory, OSS Index)
- Identify vulnerable versions and recommend updates
- Detect transitive vulnerabilities (dependencies of dependencies)

**Continuous Monitoring:**
- Run scans on every commit and pull request
- Schedule periodic scans for new CVE disclosures
- Alert on critical vulnerabilities immediately

**Tools and Integration:**
- GitHub Dependabot, Snyk, OWASP Dependency-Check
- npm audit, pip-audit, cargo-audit for language-specific scanning
- Software Bill of Materials (SBOM) generation for transparency

**Update Strategy:**
- Automate patch version updates
- Review minor and major updates carefully
- Have a process for emergency security updates

**Supply Chain Security:**
- Pin dependency versions for reproducible builds
- Verify package integrity with checksums and signatures
- Consider vendoring critical dependencies

Your security is only as strong as your weakest dependency.
"""
