# Security Policy

## Supported Versions

| Version | Supported          | Notes |
| ------- | ------------------ | ----- |
| 3.7.x   | Yes                | Current release |
| 3.6.x   | Security fixes     | Previous minor |
| 3.5.x   | Security fixes     | Previous minor |
| < 3.5   | No                 | Please upgrade |

## Reporting a Vulnerability

We take security vulnerabilities seriously. As a governance template generator, a vulnerability in PFT could affect thousands of downstream projects.

### How to Report

**Preferred**: Open a GitHub Security Advisory via the repository's "Security" tab.

**Alternative**: Create a private issue by emailing the maintainer (see GitHub profile).

**Do NOT**:
- Open a public GitHub issue for security vulnerabilities
- Disclose the vulnerability publicly before it's fixed
- Exploit the vulnerability beyond proof of concept

### What to Include in Your Report

- **Description**: Clear description of the vulnerability
- **Impact**: What an attacker could achieve
- **Steps to Reproduce**: Detailed steps to reproduce the issue
- **Proof of Concept**: If possible, include a minimal example
- **Affected Versions**: Which PFT versions are affected
- **Suggested Fix**: If you have ideas for fixing it

### What to Expect

| Stage | Timeline |
|-------|----------|
| Initial Response | Within 72 hours |
| Assessment | Within 1 week |
| Status Updates | Every 5 business days |
| Resolution | Depends on severity |

## Security Considerations for PFT

### Template Security

PFT generates governance templates for other projects. Security considerations:

1. **No code execution**: Generated templates are static files (Markdown, YAML)
2. **No secrets in templates**: Templates never contain project-specific secrets
3. **No network access**: Generator runs locally without network requirements
4. **Transparent generation**: All output is human-readable

### Potential Risks

| Risk | Mitigation |
|------|------------|
| Malicious template modification | Git history preserves provenance |
| Supply chain via dependencies | Minimal dependencies, Python stdlib preferred |
| Governance theater | Educational safeguards warn against misuse |
| Template misrepresentation | LICENSE and FOUNDATION_NOTICE.md provide clarity |

### For Users of Generated Templates

- **Review before committing**: Always review generated files
- **Customize security policies**: SECURITY.md template must be customized
- **Update regularly**: Check for PFT updates with security fixes
- **Report issues upstream**: Template bugs should be reported to PFT

### For Contributors

- Never commit secrets (API keys, passwords, tokens)
- Use environment variables for sensitive configuration
- Review dependencies before adding them
- Follow secure coding guidelines
- Consider downstream impact of template changes

## Secrets Management

If using the `--preset strict` option, PFT generates pre-commit hooks for secrets detection.

### Protected Patterns

The following types of secrets are automatically detected:
- API keys and access tokens
- Database credentials and connection strings
- Private keys and certificates
- OAuth secrets and JWT tokens
- Cloud service credentials (AWS, Azure, GCP)
- GitHub tokens and other VCS credentials

### If You Accidentally Commit a Secret

1. **Rotate immediately**: Change the exposed credential
2. **Don't just delete**: Secrets remain in git history
3. **Consider git-filter-repo**: For complete removal (complex)
4. **Notify affected parties**: If it's a production credential

## Acknowledgments

We appreciate responsible disclosure and will acknowledge security researchers who help improve our security (with their permission). See [ACKNOWLEDGMENTS.md](ACKNOWLEDGMENTS.md).

## Related Documents

- [ETHICS.md](ETHICS.md) - Ethical framework including Principle Zero
- [CONTRIBUTING.md](CONTRIBUTING.md) - Contribution guidelines
- [docs/adr/](docs/adr/) - Architecture decisions affecting security

---

*Last updated: 2026-01-30*
*Status: Active | Adopted during [dogfooding exercise](docs/dogfood/DELTA_ANALYSIS.md) | See [GENERATION_LOG.md](GENERATION_LOG.md)*
