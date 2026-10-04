# core/principles/deprecation_policy.py
# Deprecation Policy principle (v3.0.0)

"""
Deprecation Policy Principle.

A deprecation policy provides users with advance notice and migration paths
when features or APIs are being removed.

Introduced in v3.0.0.
"""

PRINCIPLE_ID = "deprecation-policy"

PRINCIPLE = {
    "name": "Deprecation Policy",
    "why": "Surprise breaking changes damage user trust and cause integration failures",
    "what": "Documented timelines and procedures for deprecating features and APIs",
    "risk": "Without a deprecation policy, users can't plan migrations and may abandon your project",
}

EDUCATION = """
📚 LEARNING: Projects with clear deprecation policies have 3x better upgrade adoption rates.

Deprecation policies help users plan for change. They transform breaking changes
from unpleasant surprises into manageable migrations. Key elements include:

**Timeline Standards:**
- Minimum notice period before removal (e.g., 6 months, 2 major versions)
- Grace period where deprecated features still work but warn
- Clear end-of-life dates announced in advance

**Communication:**
- Deprecation notices in release notes and changelogs
- Runtime warnings when deprecated features are used
- Documentation updates marking deprecated features
- Migration guides with code examples

**Migration Support:**
- Codemods or automated migration tools when possible
- Parallel support during transition periods
- Clear upgrade paths with step-by-step instructions

**Policy Documentation:**
- Public deprecation policy document
- List of currently deprecated features and removal dates
- Archive of past deprecations for reference

A good deprecation policy says: 'We respect your investment in our project
and will give you time to adapt to changes.'
"""
