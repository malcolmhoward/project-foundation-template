# core/principles/quality_assurance.py
# Quality Assurance principle (v3.0.0)

"""
Quality Assurance Principle.

Quality assurance ensures software meets defined standards before release,
catching defects early and building confidence in the product.

Introduced in v3.0.0.
"""

PRINCIPLE_ID = "quality-assurance"

PRINCIPLE = {
    "name": "Quality Assurance",
    "why": "Defects found late in development cost 10-100x more to fix than those caught early",
    "what": "Systematic testing, code reviews, and quality gates throughout the development lifecycle",
    "risk": "Without QA processes, bugs reach production, eroding user trust and increasing maintenance costs",
}

EDUCATION = """
📚 LEARNING: Projects with formal QA processes have 40% fewer production defects.

Quality Assurance is more than just testing - it's a mindset that permeates the
entire development process. It includes:

- **Automated Testing**: Unit, integration, and end-to-end tests that run on every change
- **Code Reviews**: Human oversight to catch logic errors and maintain code quality
- **Quality Gates**: Automated checks that prevent merging code that doesn't meet standards
- **Static Analysis**: Tools that find potential bugs before code even runs

The cost of fixing a bug increases exponentially as it moves through the pipeline.
A bug caught in development might take minutes to fix; the same bug in production
could require emergency patches, customer communication, and reputation repair.

QA isn't a phase - it's a continuous practice woven into every commit.
"""
