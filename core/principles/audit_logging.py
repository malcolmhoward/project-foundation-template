# core/principles/audit_logging.py
# Audit Logging principle (v3.0.0)

"""
Audit Logging Principle.

Audit logs provide an immutable record of system activities,
enabling security analysis, compliance verification, and incident investigation.

Introduced in v3.0.0.
"""

PRINCIPLE_ID = "audit-logging"

PRINCIPLE = {
    "name": "Audit Logging",
    "why": "Security incidents require forensic data to understand scope and impact",
    "what": "Immutable, tamper-evident logs of security-relevant events with proper retention",
    "risk": "Without audit logs, breaches go undetected and incident response is impossible",
}

EDUCATION = """
📚 LEARNING: Organizations with mature logging detect breaches 74% faster than those without.

Audit logging is different from application logging - it's specifically designed
for security, compliance, and forensics. Key principles include:

**What to Log:**
- Authentication events (login, logout, failed attempts)
- Authorization decisions (access granted, denied)
- Data access and modifications (who accessed what, when)
- Administrative actions (user creation, permission changes)
- Security events (password changes, MFA enrollment)

**How to Log:**
- Include timestamp, actor, action, resource, and outcome
- Use structured formats (JSON) for machine parsing
- Ensure logs are tamper-evident (append-only, signed)
- Log at the application layer, not just infrastructure

**Log Management:**
- Define retention periods based on compliance requirements
- Implement secure log storage with access controls
- Set up real-time alerting for suspicious patterns
- Regularly review logs for anomalies

**What NOT to Log:**
- Passwords and credentials (even hashed)
- Sensitive personal data (unless legally required)
- Encryption keys or tokens

Audit logs are your security camera footage. Without them, you're investigating
blindfolded.
"""
