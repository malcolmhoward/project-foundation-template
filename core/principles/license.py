# core/principles/license.py
# License Selection principle

"""
License Selection Principle.

A license defines the legal terms for use and contribution. Without one,
copyright gives others no permission to reuse the work, which prevents adoption.
"""

PRINCIPLE_ID = "license"

PRINCIPLE = {
    "name": "License Selection",
    "why": "Defines legal terms for use and contribution",
    "what": "Clear intellectual property terms",
    "risk": "Without it, legal ambiguity prevents adoption",
}

EDUCATION = """
📚 LEARNING: No license means no permission to reuse your code.

In the US, copyright applies automatically when a work is created, and only the
copyright owner may reproduce it, adapt it or distribute copies. Without a
license, others have no permission to do those things; other countries' rules
differ. (Reference: https://www.copyright.gov/circs/circ01.pdf)
On GitHub, making a repository public lets others view it and fork it, making
their own copies within GitHub (GitHub Terms of Service, D.5).
(Reference: https://docs.github.com/en/site-policy/github-terms/github-terms-of-service#5-license-grant-to-other-users)

Common choices: MIT, a short permissive license; Apache 2.0, a permissive license
with an explicit patent grant; or the GPL, a copyleft license whose permissions
depend on making the complete source code available. The right choice depends
on how you want others to use your work.
(Reference: https://opensource.org/license/mit, https://opensource.org/license/apache-2-0,
https://opensource.org/license/gpl-3-0, https://choosealicense.com/licenses/)
"""
