# Ethical Framework

This document establishes the ethical foundation for Project Foundation Template. It is not advisory—it is the primary design constraint that governs all decisions.

## Principle Zero: "Do No Harm, Allow No Harm"

Inspired by GAIA from [Horizon Zero Dawn®](https://www.playstation.com/games/horizon-zero-dawn/), harm prevention is not an afterthought or optional guideline. It is the **primary design constraint** from which all other decisions flow.

### What This Means in Practice

Every feature, every template, every line of code must pass this test:
1. **Direct Harm**: Could this directly cause harm to individuals, organizations, or systems?
2. **Enabling Harm**: Could this enable others to cause harm more easily?
3. **Passive Harm**: Could inaction or negligence in implementing this cause harm?

If the answer to any question is "yes" without adequate safeguards, the feature does not ship.

### Why GAIA?

In Horizon Zero Dawn®, GAIA was designed as a terraforming AI with one unbreakable constraint: preserve and restore life. This constraint couldn't be overridden, negotiated, or bypassed. Our Principle Zero operates the same way—it's not a preference, it's an axiom.

> *Horizon Zero Dawn is a registered trademark of Sony Interactive Entertainment ([Trademark Notice](https://sonyinteractive.com/en/copyright-and-trademark-notice/)). This project is not affiliated with or endorsed by Sony Interactive Entertainment or Guerrilla Games.*

---

## Core Ethical Principles

### Mutual Fallibility

Both humans and AI systems have biases, make errors, and have blind spots. This template is designed with this reality in mind:

- **Human fallibility**: Developers may copy templates without understanding them, skip customization, or misapply governance frameworks
- **AI fallibility**: AI assistants may generate plausible-but-wrong content, miss context, or optimize for metrics that don't capture real value

**Design implication**: Build redundant safeguards that assume both parties will make mistakes.

### Ethical Pause

Before any release or significant change, pause to consider:
1. Who could be harmed by this?
2. How could this be misused?
3. What would happen if this scaled 1000x?
4. Would we be comfortable if this appeared in a news headline?

This pause is mandatory, not optional. Fast shipping is not more important than responsible shipping.

---

## Template vs. Implementation Philosophy

### The Problem with Governance Theater

"Governance Theater" is the appearance of compliance, security, or quality without the substance. It's:
- A security policy that no one reads or follows
- A code of conduct with no enforcement mechanism
- CI/CD badges that run but test nothing meaningful

This template explicitly fights governance theater by:
1. **Requiring acknowledgment** before generating any files
2. **Including educational content** that explains WHY each element matters
3. **Marking templates clearly** as starting points, not finished products
4. **Building in expiration dates** to force periodic review

### Templates Teach, They Don't Comply

A generated template does not make you compliant, secure, or professional. It gives you:
- A starting point for understanding what governance looks like
- Educational context for why each element matters
- A structure to customize for your specific needs

The learning is the point, not the artifact.

---

## Educational-First Commitment

### WHAT Before WHY Before HOW

Every piece of documentation, every generated file, every feature follows this pattern:

1. **WHAT**: What is this thing? Define it clearly.
2. **WHY**: Why does it matter? What problem does it solve?
3. **HOW**: How do you implement or use it?

Most documentation skips straight to HOW. This creates users who can follow steps but can't adapt when circumstances change. We prioritize understanding.

### The Anti-Pattern: Automation Without Understanding

```
# BAD: Copy-paste governance
git clone template-repo
rm -rf .git
git init
# "We have governance now!"

# GOOD: Understanding-driven governance
# Read the educational content
# Customize for your context
# Understand what each file does
# Make informed decisions about what to keep/modify/remove
```

---

## Version Advisory Expiration

### Why Templates Expire

Software evolves. Best practices change. Security vulnerabilities are discovered. A template from 2020 may actively harm projects in 2025 by:
- Recommending outdated dependencies with known vulnerabilities
- Suggesting deprecated practices
- Missing important new governance standards

### The Expiration Mechanism

Every version of this template has an advisory expiration date. After this date:
1. The generator displays a prominent warning
2. Users must acknowledge they're using an outdated version
3. Documentation points to checking for updates

This is not DRM or forced obsolescence—the code still runs. It's a safeguard against stale governance.

---

## Identified Risks

### 1. Governance Theater
**Risk**: Templates create the appearance of governance without substance.
**Mitigation**: Educational content, customization requirements, template warnings.

### 2. AI Exploitation
**Risk**: Bad actors use AI to mass-generate professional-looking repositories for malicious purposes (supply chain attacks, phishing, scams).
**Mitigation**: Usage logging, ethical agreement, educational delays, distinctive template markers.

### 3. Environmental Impact
**Risk**: Unnecessary CI/CD pipelines contribute to carbon footprint without providing value.
**Mitigation**: Minimal default templates, education about when CI/CD is actually needed.

### 4. Social Engineering
**Risk**: Professional-looking governance documents make malicious projects appear legitimate.
**Mitigation**: Template watermarks, version expiration, educational content about verification.

### 5. Legal Exploitation
**Risk**: Templates misrepresented as actual compliance (e.g., claiming GDPR compliance because you have a privacy policy template).
**Mitigation**: Clear disclaimers, educational content about what compliance actually requires.

---

## Ethical Safeguards

### 1. Ethical Use Agreement
Before generating any templates, users must acknowledge:
- They understand these are templates, not compliance
- They commit to customization
- They accept responsibility for how templates are used

### 2. Education First
Every template generation includes educational content explaining:
- What the template is for
- Why it matters
- How to customize it properly

### 3. Usage Logging
Local logging (never transmitted) creates accountability:
- Who generated templates
- When they were generated
- What project they were for

This creates a paper trail without surveillance.

### 4. Template Warnings
Generated files include clear markers:
- "This is a template - customize before use"
- Version and generation date
- Links to educational resources

### 5. Advisory Expiration
Templates have expiration dates that:
- Warn users of potentially outdated content
- Encourage checking for updates
- Prevent indefinite use of stale practices

---

## The Ouroboros Ecosystem

### Beneficial Recursive Improvement

This template can generate governance for:
- Individual projects (any software project)
- Coordination layers (meta-projects that manage other projects)
- Itself (the template uses itself)

This creates an ouroboros—a snake eating its own tail—but in a beneficial way:

```
Template generates project governance
    ↓
Projects discover improvements
    ↓
Improvements feed back to template
    ↓
Template generates better governance
    ↓
(cycle continues)
```

### Three Mechanisms

1. **Self-generating**: Template uses itself to define its own governance
2. **Ecosystem bootstrap**: Template creates frameworks that use the template
3. **Learning cycle**: Each instance teaches lessons that improve the source

### Why This Isn't Circular Dependency

Circular dependency is bad because it creates:
- Unresolvable build orders
- Infinite loops
- Unclear ownership

Our recursive structure is different because:
- Each cycle adds value (not just complexity)
- The template is a snapshot, not a live dependency
- Improvements are optional, not required for function

---

## Applying These Principles

### For Contributors

Before submitting any PR, ask:
1. Does this pass Principle Zero? (Do no harm, allow no harm)
2. Does it maintain educational value? (WHAT/WHY/HOW)
3. Have I taken an ethical pause? (Considered misuse potential)
4. Does it avoid governance theater? (Substance over appearance)

### For Users

Before using generated templates, remember:
1. Templates are starting points, not finished products
2. Customization is required, not optional
3. Understanding matters more than having files
4. Check for newer versions periodically

### For the Ecosystem

This ethical framework applies to:
- Project Foundation Template itself
- All instances generated by the template
- All projects that adopt these principles
- Any coordination layers built using this template

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0 | 2025-10-29 | Initial ethical framework |

---

*This document is itself subject to the principles it describes. It should be reviewed periodically, updated as understanding evolves, and never treated as final or complete.*
