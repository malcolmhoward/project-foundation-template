# core/guides/dependency_guide.py
# Dependency Management Guide (v3.0.0)

"""
Dependency Management Guide.

Provides practical guidance on managing project dependencies
including versioning, security, and update strategies.

Introduced in v3.0.0.
"""

GUIDE_ID = "dependency-guide"

GUIDE = {
    "title": "Dependency Management Guide",
    "purpose": "Learn how to manage project dependencies effectively",
    "audience": "All developers",
    "complexity": "intermediate",
}

RELATED_PRINCIPLES = ["security", "versioning"]

CONTENT = """
# Dependency Management Guide

## Overview

Effective dependency management ensures your project remains:
- Secure (no known vulnerabilities)
- Stable (compatible versions)
- Maintainable (manageable update burden)

## Dependency Types

### Direct Dependencies
Dependencies your code directly imports/uses.

```
your-project
├── requests      <- Direct dependency
└── flask         <- Direct dependency
```

### Transitive Dependencies
Dependencies of your dependencies.

```
your-project
├── requests
│   ├── urllib3   <- Transitive
│   └── certifi   <- Transitive
└── flask
    ├── werkzeug  <- Transitive
    └── jinja2    <- Transitive
```

## Version Specification

### Version Constraints

| Syntax | Meaning | Example |
|--------|---------|---------|
| `==1.2.3` | Exact version | Only 1.2.3 |
| `>=1.2.3` | Minimum version | 1.2.3 or higher |
| `~=1.2.3` | Compatible release | 1.2.x (>=1.2.3, <1.3.0) |
| `^1.2.3` | SemVer compatible | >=1.2.3, <2.0.0 |
| `>=1.2,<2.0` | Range | Between 1.2 and 2.0 |

### Choosing Constraints

**For applications:**
- Use exact versions or tight ranges
- Lock all transitive dependencies
- Prioritize stability and reproducibility

**For libraries:**
- Use flexible version ranges
- Don't lock transitive dependencies
- Allow consumers to resolve versions

## Lock Files

### Purpose

Lock files ensure reproducible builds by recording:
- Exact versions of all dependencies
- Checksums/hashes for integrity
- Resolution of version conflicts

### Common Lock Files

| Language | Lock File |
|----------|-----------|
| Python | `requirements.txt`, `poetry.lock` |
| JavaScript | `package-lock.json`, `yarn.lock` |
| Ruby | `Gemfile.lock` |
| Rust | `Cargo.lock` |
| Go | `go.sum` |

### Best Practices

```bash
# Always commit lock files for applications
git add package-lock.json
git commit -m "Update lock file"

# Regenerate when changing dependencies
npm install  # Updates lock file
```

## Adding Dependencies

### Before Adding

Ask yourself:
1. Is this dependency necessary?
2. Is it well-maintained?
3. What's the security track record?
4. How large is it (bundle size)?
5. What are its dependencies?

### Evaluation Checklist

- [ ] Active maintenance (recent commits)
- [ ] Reasonable number of open issues
- [ ] Good test coverage
- [ ] No known critical vulnerabilities
- [ ] Acceptable license
- [ ] Reasonable size

### Research Commands

```bash
# npm - Check package info
npm info package-name

# Python - Check package info
pip show package-name

# Check for vulnerabilities
npm audit
pip-audit
```

## Updating Dependencies

### Update Strategies

**Conservative (Recommended for production):**
- Update patch versions regularly
- Update minor versions monthly
- Update major versions deliberately

**Aggressive (For active development):**
- Stay on latest versions
- Update frequently
- Accept higher change risk

### Update Process

1. **Review changes**
   ```bash
   npm outdated
   pip list --outdated
   ```

2. **Read changelogs**
   - Check for breaking changes
   - Review security fixes

3. **Update incrementally**
   ```bash
   # Update one at a time
   npm update package-name
   pip install --upgrade package-name
   ```

4. **Run tests**
   ```bash
   npm test
   pytest
   ```

5. **Commit separately**
   ```bash
   git commit -m "deps: update package-name to 2.0.0"
   ```

### Automated Updates

Tools for automated dependency updates:

- **Dependabot** (GitHub)
- **Renovate** (Multi-platform)
- **Snyk** (Security-focused)

Example Dependabot config:

```yaml
# .github/dependabot.yml
version: 2
updates:
  - package-ecosystem: "npm"
    directory: "/"
    schedule:
      interval: "weekly"
    groups:
      development:
        patterns:
          - "*"
        exclude-patterns:
          - "react*"
```

## Security

### Vulnerability Scanning

Run security scans regularly:

```bash
# npm
npm audit
npm audit fix

# Python
pip-audit
safety check

# Multi-language
snyk test
```

### Responding to Vulnerabilities

1. **Assess severity**
   - Critical/High: Update immediately
   - Medium: Update within days
   - Low: Update in next cycle

2. **Check exploitability**
   - Is the vulnerable code path used?
   - Is the vulnerability relevant to your use case?

3. **Update or mitigate**
   ```bash
   # Direct dependency - update
   npm update vulnerable-package

   # Transitive dependency - override
   npm pkg set overrides.vulnerable-package="^2.0.0"
   ```

### Security Best Practices

- Enable automated security alerts
- Use lock files
- Pin exact versions in production
- Review new dependencies before adding
- Monitor security advisories

## Dependency Conflicts

### Common Causes

- Incompatible version requirements
- Peer dependency mismatches
- Circular dependencies

### Resolution Strategies

**1. Update to compatible versions**
```bash
# Find a version that satisfies all requirements
npm ls conflicting-package
```

**2. Use resolutions/overrides**
```json
// package.json
{
  "overrides": {
    "conflicting-package": "^2.0.0"
  }
}
```

**3. Replace problematic dependencies**
- Find alternatives with better compatibility
- Consider removing if not essential

## License Compliance

### Common Licenses

| License | Type | Requirements |
|---------|------|--------------|
| MIT | Permissive | Include license |
| Apache 2.0 | Permissive | Include license + notice |
| GPL | Copyleft | Open source derivative works |
| BSD | Permissive | Include license |

### License Checking

```bash
# npm
npx license-checker

# Python
pip-licenses
```

### License Policy

Define what's acceptable for your project:

```yaml
# Example policy
allowed:
  - MIT
  - Apache-2.0
  - BSD-2-Clause
  - BSD-3-Clause
forbidden:
  - GPL-3.0
  - AGPL-3.0
```

## Monorepo Dependencies

### Shared Dependencies

```
monorepo/
├── packages/
│   ├── app-a/
│   │   └── package.json
│   └── app-b/
│       └── package.json
└── package.json  <- Shared dependencies
```

### Version Synchronization

- Keep shared dependencies at same version
- Use workspace features
- Consider tools like Lerna, Nx, or Turborepo

## Documentation

### Document Your Dependencies

In your README or docs:

```markdown
## Dependencies

### Runtime
- **requests** (2.28+): HTTP client
- **pydantic** (2.0+): Data validation

### Development
- **pytest**: Testing framework
- **black**: Code formatter
```

### Document Update Policy

```markdown
## Dependency Update Policy

- Security updates: Within 24 hours
- Patch updates: Weekly
- Minor updates: Monthly
- Major updates: Quarterly review
```

## Quick Reference

### Commands Cheat Sheet

```bash
# List outdated packages
npm outdated          # npm
pip list --outdated   # pip

# Update all
npm update            # npm (within semver range)
pip-compile --upgrade # pip-tools

# Security audit
npm audit
pip-audit

# Check licenses
npx license-checker
pip-licenses
```

---

*This guide complements your project's package configuration and security practices*
"""
