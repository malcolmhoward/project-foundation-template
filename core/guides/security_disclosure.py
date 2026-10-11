# core/guides/security_disclosure.py
# Security Disclosure Guide (v2.9.0)

"""
Security Disclosure Guide.

Provides practical guidance on handling security vulnerabilities
responsibly, both as a reporter and as a maintainer.

Introduced in v2.9.0.
"""

GUIDE_ID = "security-disclosure"

GUIDE = {
    "title": "Security Disclosure Guide",
    "purpose": "Learn how to handle security vulnerabilities responsibly",
    "audience": "Maintainers and security researchers",
    "complexity": "advanced",
}

RELATED_PRINCIPLES = ["security", "enhanced-security"]

CONTENT = """
# Security Disclosure Guide

## Overview

Responsible disclosure protects users while giving maintainers
time to fix vulnerabilities before they're exploited.

## For Security Researchers

### Finding Vulnerabilities

When you discover a security issue:

1. **Don't panic** - Document carefully
2. **Don't exploit** - Stop at proof of concept
3. **Don't disclose** - Keep it private initially

### Reporting Process

1. **Find the contact**
   - Check SECURITY.md
   - Look for security@domain.com
   - Check for bug bounty programs

2. **Write a clear report**
   ```
   Subject: Security Vulnerability in [Component]

   Summary: Brief description

   Severity: Critical/High/Medium/Low

   Details:
   - Affected versions
   - Attack vector
   - Impact

   Steps to Reproduce:
   1. Step one
   2. Step two

   Proof of Concept: (minimal, non-destructive)

   Suggested Fix: (if you have ideas)
   ```

3. **Wait for response**
   - Allow 72 hours for initial response
   - Be patient but follow up if needed

### Disclosure Timeline

Standard responsible disclosure:
- **Day 0**: Report to maintainer
- **Day 1-7**: Initial response and assessment
- **Day 7-90**: Fix development and testing
- **Day 90**: Public disclosure (with or without fix)

## For Maintainers

### Setting Up Security Processes

1. **Create SECURITY.md**
   - How to report vulnerabilities
   - What to include in reports
   - Expected response times

2. **Set up secure communication**
   - Dedicated security email
   - Consider PGP for sensitive reports

3. **Define response process**
   - Who handles security issues?
   - What's the escalation path?
   - Who can approve patches?

### Handling Reports

1. **Acknowledge quickly**
   - Respond within 72 hours
   - Thank the reporter
   - Provide a timeline

2. **Assess severity**

   | Severity | Impact | Timeline |
   |----------|--------|----------|
   | Critical | RCE, data breach | 24-48 hours |
   | High | Auth bypass, XSS | 1-2 weeks |
   | Medium | Information leak | 2-4 weeks |
   | Low | Minor issues | Next release |

3. **Develop fix**
   - Work privately (don't push to public repo)
   - Get security review
   - Prepare advisory

4. **Coordinate disclosure**
   - Agree on timeline with reporter
   - Prepare communications
   - Have fix ready before disclosure

5. **Disclose**
   - Release fixed version
   - Publish security advisory
   - Credit reporter (if they want)

### Security Advisory Template

```markdown
# Security Advisory

## Summary
Brief description of the vulnerability.

## Affected Versions
- 1.0.0 - 1.5.2

## Fixed Versions
- 1.5.3

## Severity
High (CVSS: 7.5)

## Description
Detailed description of the vulnerability and its impact.

## Mitigation
Steps users can take before updating.

## Timeline
- 2024-01-01: Reported by [name]
- 2024-01-02: Acknowledged
- 2024-01-15: Fix developed
- 2024-01-20: Fix released
- 2024-01-20: Public disclosure

## Credit
Thanks to [reporter] for responsible disclosure.
```

## CVE Process

For significant vulnerabilities:

1. **Request CVE** from cve.org or through GitHub
2. **Include CVE** in advisory
3. **Update** NVD with details

## Common Mistakes

### Reporters
- Public disclosure before giving time to fix
- Demanding payment/bounty without program
- Exaggerating severity

### Maintainers
- Ignoring reports
- Downplaying severity
- Shooting the messenger
- Delaying fixes indefinitely

## Resources

- [CERT/CC Vulnerability Disclosure](https://vuls.cert.org/)
- [ISO 29147](https://www.iso.org/standard/72311.html) - Disclosure standard
- [GitHub Security Advisories](https://docs.github.com/en/code-security)

---

*This guide complements your project's SECURITY.md*
"""
