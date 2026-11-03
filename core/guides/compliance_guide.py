# core/guides/compliance_guide.py
# Compliance Guide (v2.10.0)

"""
Compliance Guide.

Provides practical guidance on ensuring software compliance
with regulatory requirements, standards, and organizational policies.

Introduced in v2.10.0.
"""

from core.utils import COMPLIANCE_DISCLAIMER

GUIDE_ID = "compliance-guide"

GUIDE = {
    "title": "Compliance Guide",
    "purpose": "Learn how to ensure regulatory and policy compliance",
    "audience": "Tech leads, architects, and compliance officers",
    "complexity": "advanced",
}

RELATED_PRINCIPLES = ["security", "adr", "compliance-policy"]

CONTENT = """
# Compliance Guide

> **""" + COMPLIANCE_DISCLAIMER + """**

## Overview

Software compliance ensures your project meets:
- Laws and regulations (GDPR, HIPAA, CCPA)
- Industry standards (ISO/IEC 27001, PCI DSS) and audit reports (SOC 2)
- Organizational policies
- Contractual obligations

The sources below were checked in October and November 2026. Laws and standards change, so
check the current text before relying on any detail here. `docs/sources.md` in
the Project Foundation Template repository records how each was checked.

## Common Compliance Frameworks

### GDPR (General Data Protection Regulation)

Regulation (EU) 2016/679: https://eur-lex.europa.eu/eli/reg/2016/679/oj

**Applies to:** Organizations established in the EU, and organizations elsewhere
that offer goods or services to, or monitor the behaviour of, people in the EU
(Art. 3)

**Key Requirements:**
- A lawful basis for processing (Art. 6)
- Data minimisation (Art. 5(1)(c))
- Rights of access (Art. 15), erasure (Art. 17, which has exceptions in
  Art. 17(3)) and data portability (Art. 20)
- Breach notification (Arts. 33-34): the controller notifies the supervisory
  authority without undue delay and, where feasible, within 72 hours of becoming
  aware of a breach, unless it is unlikely to result in a risk to people's rights
  and freedoms; people affected are told without undue delay when the risk is
  high, with exceptions (Art. 34(3)); a processor notifies the controller
  without undue delay
- Data protection by design and by default (Art. 25)

**Implementation Checklist:**
- [ ] Document all personal data processing
- [ ] Implement consent management
- [ ] Enable data export (portability)
- [ ] Enable data deletion
- [ ] Encrypt personal data
- [ ] Maintain processing records
- [ ] Conduct privacy impact assessments

### SOC 2

AICPA: https://www.aicpa-cima.com/topic/audit-assurance/audit-and-assurance-greater-than-soc-2

**What it is:** an examination, by a CPA, of a service organization's
description of its system and its controls, which produces an examination
report. It is not a law.

**Trust Services categories:**
- Security
- Availability
- Processing Integrity
- Confidentiality
- Privacy

**Implementation Checklist:**
- [ ] Access control policies
- [ ] Change management procedures
- [ ] Incident response plan
- [ ] Encryption at rest and in transit
- [ ] Regular security assessments
- [ ] Vendor management
- [ ] Employee training

### HIPAA (Health Insurance Portability and Accountability Act)

45 CFR Part 164: https://www.ecfr.gov/current/title-45/part-164

**Applies to:** Covered entities and their business associates
(45 CFR 164.104, 164.302)

**Key Requirements (45 CFR Part 164):**
- Safeguards for electronic protected health information (ePHI)
- Access control, including encryption (164.312(a))
- "Addressable" specifications, such as encryption: assess each one, and
  implement it if reasonable and appropriate, or document why not and use an
  equivalent measure if that is reasonable and appropriate (164.306(d)(3))
- Business associate contracts (164.308(b), 164.314(a), 164.504(e))

### PCI DSS (Payment Card Industry Data Security Standard)

PCI Security Standards Council: https://www.pcisecuritystandards.org/standards/pci-dss/
(v4.0.1 is the only active version since v4.0 was retired on 31 December 2024)

**Applies to:** Entities that store, process or transmit cardholder data or
sensitive authentication data, or that could affect the security of the
cardholder data environment

**Requirement areas (examples; the standard lists the full requirements):**
- Protection of cardholder data
- Access control
- Regular testing
- Security policies

Network segmentation can reduce the scope of a PCI DSS assessment
(PCI SSC FAQ 1135: https://www.pcisecuritystandards.org/faqs/1135).

## Implementing Compliance

### 1. Identify Requirements

```markdown
## Compliance Requirements Matrix (example)

| Requirement | Framework | Implementation | Owner |
|-------------|-----------|----------------|-------|
| Data encryption | GDPR Art. 32 (encryption is one example measure) | AES-256 at rest (your choice) | Security |
| Access logging | <the frameworks your assessor maps this to> | Audit log service | Platform |
| Consent tracking | GDPR | Consent service | Product |
```

### 2. Design for Compliance

**Data Classification:**

```python
class DataClassification:
    PUBLIC = "public"           # No restrictions
    INTERNAL = "internal"       # Employee access only
    CONFIDENTIAL = "confidential"  # Need-to-know basis
    RESTRICTED = "restricted"   # Regulatory protection required
```

**Privacy by Design:**

```python
class UserService:
    def create_user(self, data: dict) -> User:
        # Data minimization: only collect what's needed
        allowed_fields = ["email", "name"]
        filtered_data = {k: v for k, v in data.items() if k in allowed_fields}

        # Consent tracking
        user = User(**filtered_data)
        user.consent_given_at = datetime.utcnow()
        user.consent_version = CURRENT_CONSENT_VERSION

        return self.repository.save(user)
```

### 3. Implement Controls

**Access Control:**

```python
def require_permission(permission: str):
    def decorator(func):
        def wrapper(*args, **kwargs):
            user = get_current_user()
            if not user.has_permission(permission):
                audit_log.record(
                    event="access_denied",
                    user=user.id,
                    resource=func.__name__,
                    permission=permission
                )
                raise PermissionDenied()
            return func(*args, **kwargs)
        return wrapper
    return decorator

@require_permission("view_customer_data")
def get_customer(customer_id: str) -> Customer:
    return customer_repository.find(customer_id)
```

**Audit Logging:**

```python
class AuditLogger:
    def record(self, event: str, **context):
        entry = {
            "timestamp": datetime.utcnow().isoformat(),
            "event": event,
            "user_id": context.get("user_id"),
            "ip_address": context.get("ip_address"),
            "resource": context.get("resource"),
            "action": context.get("action"),
            "result": context.get("result"),
        }
        # Immutable storage
        self.storage.append(entry)
```

**Data Encryption:**

```python
class EncryptedField:
    def __init__(self, key_id: str):
        self.key_id = key_id

    def encrypt(self, value: str) -> str:
        key = key_management.get_key(self.key_id)
        return encrypt_aes256(value, key)

    def decrypt(self, encrypted: str) -> str:
        key = key_management.get_key(self.key_id)
        return decrypt_aes256(encrypted, key)
```

### 4. Document Everything

**Required Documentation:**

- Data flow diagrams
- Privacy impact assessments
- Security policies
- Incident response procedures
- Access control policies
- Change management procedures
- Training records

**Documentation Template (example values):**

```markdown
# Control Documentation

## Control ID
CTRL-001

## Control Name
Data Encryption at Rest

## Framework Mapping
- SOC 2: <the criterion your auditor maps this control to>
- GDPR: Article 32(1)(a) (lists encryption as an example of an appropriate measure)

## Description
All sensitive data must be encrypted at rest using AES-256 (our chosen standard).

## Implementation
- Database: Transparent Data Encryption (TDE)
- File storage: Server-side encryption (SSE)
- Backups: Encrypted with separate key

## Evidence
- Configuration screenshots
- Encryption key rotation logs
- Annual review records

## Owner
Security Team

## Review Frequency
Quarterly
```

## Compliance Testing

### Automated Compliance Checks

```yaml
# Example compliance check pipeline
compliance_checks:
  - name: "No hardcoded secrets"
    tool: gitleaks
    fail_on: any

  - name: "Dependencies vulnerability scan"
    tool: snyk
    severity_threshold: high

  - name: "SAST security scan"
    tool: semgrep
    ruleset: owasp-top-ten

  - name: "License compliance"
    tool: license-checker
    allowed: ["MIT", "Apache-2.0", "BSD"]
```

### Compliance Test Categories

**Security Testing:**
- Vulnerability scanning
- Penetration testing
- Code analysis (SAST/DAST)

**Access Control Testing:**
- Permission verification
- Authentication testing
- Session management

**Data Protection Testing:**
- Encryption verification
- Data handling procedures
- Deletion/anonymization

## Audit Preparation

### Audit Trail Requirements

Maintain records of:
- Who accessed what data
- When changes were made
- What changes were made
- Why changes were made (linked to tickets)

### Evidence Collection

```markdown
## Evidence Checklist

### Access Control
- [ ] User access reviews (quarterly)
- [ ] Permission change logs
- [ ] Terminated user removal evidence

### Change Management
- [ ] Change request tickets
- [ ] Approval records
- [ ] Deployment logs
- [ ] Rollback procedures

### Security
- [ ] Vulnerability scan reports
- [ ] Penetration test results
- [ ] Incident response records
- [ ] Security training completion
```

### Audit Response Process

1. **Preparation**
   - Gather requested evidence
   - Identify control owners
   - Prepare walkthrough environments

2. **During Audit**
   - Provide requested documentation
   - Demonstrate controls
   - Answer questions accurately
   - Document gaps identified

3. **Remediation**
   - Address findings promptly
   - Document remediation actions
   - Verify fixes

## Data Subject Rights

### Implementing GDPR Rights

Access (Art. 15), erasure (Art. 17) and portability (Art. 20):
https://eur-lex.europa.eu/eli/reg/2016/679/oj. Erasure has exceptions
(Art. 17(3)), and portability applies only to data the person provided, where
processing is based on consent or a contract and is automated (Art. 20(1)).

**Right to Access:**
```python
def get_user_data_export(user_id: str) -> dict:
    # Export all user data for data subject access request.
    return {
        "profile": user_repo.get(user_id).to_dict(),
        "orders": [o.to_dict() for o in order_repo.find_by_user(user_id)],
        "preferences": preference_repo.get(user_id).to_dict(),
        "audit_log": audit_repo.find_by_user(user_id),
        "export_date": datetime.utcnow().isoformat(),
    }
```

**Right to Deletion:**
```python
def delete_user_data(user_id: str) -> DeletionReport:
    # Delete all user data for erasure request.
    report = DeletionReport(user_id=user_id)

    # Delete from each system
    report.add(user_repo.delete(user_id))
    report.add(order_repo.anonymize_user(user_id))  # Keep for accounting
    report.add(preference_repo.delete(user_id))

    # Audit the deletion
    audit_log.record(
        event="user_data_deleted",
        user_id=user_id,
        reason="gdpr_erasure_request"
    )

    return report
```

## Vendor Compliance

### Vendor Assessment

Before using third-party services:

- [ ] Review their certifications and audit reports (for example ISO/IEC 27001 certification, a SOC 2 report)
- [ ] Sign Data Processing Agreements (DPA)
- [ ] Verify data handling practices
- [ ] Assess security controls
- [ ] Review incident history

### Third-Party Risk Management

```markdown
## Vendor Risk Assessment (example values)

### Vendor: Cloud Provider X

| Category | Risk Level | Mitigation |
|----------|------------|------------|
| Data location | Medium | Contractual data residency |
| Security | Low | Current SOC 2 report reviewed |
| Availability | Low | 99.99% SLA |
| Vendor lock-in | Medium | Abstract storage layer |
```

## Continuous Compliance

### Monitoring

- Real-time access monitoring
- Configuration drift detection
- Compliance dashboard
- Automated policy enforcement

### Regular Reviews

| Activity | Frequency |
|----------|-----------|
| Access reviews | Quarterly |
| Policy reviews | Annually |
| Penetration testing | Annually |
| Compliance training | Annually |
| Risk assessment | Annually |

### Incident Response

```markdown
## Compliance Incident Procedure

1. **Detect** - Identify potential compliance breach
2. **Assess** - Determine scope and severity
3. **Contain** - Limit further exposure
4. **Notify** - Inform required parties (GDPR: the supervisory authority within 72 hours where feasible, see Art. 33)
5. **Remediate** - Fix the root cause
6. **Document** - Record all actions taken
7. **Review** - Update controls to prevent recurrence
```

---

*This guide complements your organization's compliance policies and security framework*
"""
