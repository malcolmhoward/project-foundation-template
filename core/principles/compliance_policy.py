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
📚 LEARNING: Data protection regulators can impose large fines for non-compliance.

⚖️  """ + COMPLIANCE_DISCLAIMER + """

Under the GDPR, the most serious infringements can be fined up to EUR 20 million
or, for an undertaking, 4% of its worldwide annual turnover, whichever is higher
(Regulation (EU) 2016/679, Art. 83(5)).
(Reference: https://eur-lex.europa.eu/eli/reg/2016/679/oj)

Which of these apply depends on where you operate, the data you handle and your
industry. Frameworks to know (sources checked October-November 2026):

- **GDPR** (EU law): data protection, that is, the protection of people with
  regard to the processing of their personal data. It applies to
  organizations established in the EU, and to those offering goods or services
  to, or monitoring the behaviour of, people in the EU (Art. 3).
  (Reference: https://eur-lex.europa.eu/eli/reg/2016/679/oj)
- **HIPAA** (US law): health information privacy and security. Its security
  standards require covered entities and their business associates to ensure the
  confidentiality, integrity and availability of electronic protected health
  information (45 CFR 164.302, 164.306(a)); subpart E, "Privacy of
  Individually Identifiable Health Information", sets which uses and
  disclosures are permitted or required.
  (Reference: https://www.ecfr.gov/current/title-45/part-164/section-164.306)
- **SOC 2**: an examination by a CPA of a service organization's controls
  relevant to security, availability, processing integrity, confidentiality or
  privacy; it is an examination report, not a law.
  (Reference: https://www.aicpa-cima.com/topic/audit-assurance/audit-and-assurance-greater-than-soc-2)
- **PCI DSS** (v4.0.1): the payment card industry's security standard for
  entities that store, process or transmit cardholder data.
  (Reference: https://www.pcisecuritystandards.org/standards/pci-dss/)
- **CCPA** (California law): consumer privacy rights.
  (Reference: https://oag.ca.gov/privacy/ccpa)

Compliance policy documentation should cover:
- Data collection, storage, and retention practices
- User consent and data subject rights (access, deletion, portability)
- Security controls and incident response procedures
- Third-party data sharing and processor agreements
- Regular compliance audits and assessments

Building compliance into your development process from the start is usually
easier than retrofitting it later. Under the GDPR, data protection by design and
by default is already an obligation of the controller (Art. 25).
"""
