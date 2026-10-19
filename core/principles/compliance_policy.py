# core/principles/compliance_policy.py
# Compliance Policy principle (v2.10.0)

"""
Compliance Policy Principle.

Compliance policies ensure software meets regulatory requirements,
protecting both users and the organization from legal and financial risks.

Introduced in v2.10.0.
"""

from core.utils import COMPLIANCE_DISCLAIMER

PRINCIPLE_ID = "compliance-policy"

PRINCIPLE = {
    "name": "Compliance Policy",
    "why": "Regulatory non-compliance can result in fines, lawsuits, and loss of operating licenses",
    "what": "Documented policies for GDPR, HIPAA, SOC2, PCI-DSS, and other relevant regulations",
    "risk": "Without compliance policies, organizations face legal liability and cannot serve regulated industries",
}

EDUCATION = """
📚 LEARNING: Data protection regulators can, and do, impose large fines for non-compliance.

⚖️  """ + COMPLIANCE_DISCLAIMER + """

Compliance isn't optional when handling user data or operating in regulated industries.
Key regulations include:

- **GDPR** (EU): Data protection and privacy for EU residents
- **HIPAA** (US): Healthcare information privacy and security
- **SOC 2**: Security, availability, and confidentiality for service providers
- **PCI-DSS**: Payment card data security standards
- **CCPA** (California): Consumer privacy rights

Compliance policy documentation should cover:
- Data collection, storage, and retention practices
- User consent and data subject rights (access, deletion, portability)
- Security controls and incident response procedures
- Third-party data sharing and processor agreements
- Regular compliance audits and assessments

Building compliance into your development process from the start is far cheaper
than retrofitting it later. Privacy by design isn't just good ethics - it's
increasingly a legal requirement.
"""
