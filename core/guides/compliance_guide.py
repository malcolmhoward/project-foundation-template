# core/guides/compliance_guide.py
# Compliance Guide (v3.0.0)

"""
Compliance Guide.

Provides practical guidance on ensuring software compliance
with regulatory requirements, standards, and organizational policies.

Introduced in v3.0.0.
"""

GUIDE_ID = "compliance-guide"

GUIDE = {
    "title": "Compliance Guide",
    "purpose": "Learn how to ensure regulatory and policy compliance",
    "audience": "Tech leads, architects, and compliance officers",
    "complexity": "advanced",
}

RELATED_PRINCIPLES = ["security", "adr", "code-review"]

CONTENT = """
# Compliance Guide

## Overview

Software compliance ensures your project meets:
- Regulatory requirements (GDPR, HIPAA, SOC2)
- Industry standards (ISO 27001, PCI-DSS)
- Organizational policies
- Contractual obligations

## Common Compliance Frameworks

### GDPR (General Data Protection Regulation)

**Applies to:** Processing EU residents' personal data

**Key Requirements:**
- Lawful basis for processing
- Data minimization
- Right to access and deletion
- Data breach notification (72 hours)
- Privacy by design

**Implementation Checklist:**
- [ ] Document all personal data processing
- [ ] Implement consent management
- [ ] Enable data export (portability)
- [ ] Enable data deletion
- [ ] Encrypt personal data
- [ ] Maintain processing records
- [ ] Conduct privacy impact assessments

### SOC 2

**Applies to:** Service organizations handling customer data

**Trust Service Criteria:**
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

**Applies to:** Healthcare data in the US

**Key Requirements:**
- Protected Health Information (PHI) safeguards
- Access controls
- Audit trails
- Encryption
- Business Associate Agreements

### PCI-DSS (Payment Card Industry Data Security Standard)

**Applies to:** Handling credit card data

**Key Requirements:**
- Network segmentation
- Encryption of cardholder data
- Access control
- Regular testing
- Security policies

## Implementing Compliance

### 1. Identify Requirements

```markdown
## Compliance Requirements Matrix

| Requirement | Framework | Implementation | Owner |
|-------------|-----------|----------------|-------|
| Data encryption | GDPR, SOC2 | AES-256 at rest | Security |
| Access logging | SOC2, HIPAA | Audit log service | Platform |
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

**Documentation Template:**

```markdown
# Control Documentation

## Control ID
CTRL-001

## Control Name
Data Encryption at Rest

## Framework Mapping
- SOC2: CC6.1
- GDPR: Article 32

## Description
All sensitive data must be encrypted at rest using AES-256.

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

- [ ] Review their compliance certifications
- [ ] Sign Data Processing Agreements (DPA)
- [ ] Verify data handling practices
- [ ] Assess security controls
- [ ] Review incident history

### Third-Party Risk Management

```markdown
## Vendor Risk Assessment

### Vendor: Cloud Provider X

| Category | Risk Level | Mitigation |
|----------|------------|------------|
| Data location | Medium | Contractual data residency |
| Security | Low | SOC2 Type II certified |
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
4. **Notify** - Inform required parties (72h for GDPR)
5. **Remediate** - Fix the root cause
6. **Document** - Record all actions taken
7. **Review** - Update controls to prevent recurrence
```

---

*This guide complements your organization's compliance policies and security framework*
"""
