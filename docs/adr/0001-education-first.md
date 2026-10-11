# ADR 0001: Education-First Approach

## Status

Accepted

## Date

2025-10-29

## Context

The original Project Foundation Template (v1.x and early v2.x) was a comprehensive governance generator with:
- ~6,500 lines of code
- 23 governance principles
- 20 documentation modules
- 5 preset configurations (minimal → enterprise)

While powerful, this approach created several problems:

### The Automation Trap
Users could generate complete governance suites without understanding what any of it did. This led to:
- Governance theater (appearance of compliance without substance)
- Copy-paste culture (templates used verbatim without customization)
- False confidence (believing generated files = actual security/compliance)

### Exploitation Potential
A tool that generates professional-looking governance at scale enables:
- Supply chain attacks via legitimate-looking malicious packages
- Phishing via professional-appearing project facades
- Legal misrepresentation (templates claimed as actual compliance)

### Environmental Concerns
Full governance suites include CI/CD workflows that:
- Run on every commit regardless of necessity
- Consume compute resources and energy
- Provide false confidence through green checkmarks

## Decision

We will adopt an **education-first approach** where:

1. **Understanding precedes generation**: Users must engage with educational content before receiving templates

2. **Less is more**: The "lite" edition includes only 5 core principles instead of 23, forcing users to consciously add complexity

3. **Templates are starting points**: Generated files explicitly mark themselves as templates requiring customization

4. **Safeguards are mandatory**: Ethical agreement, educational delays, and usage logging cannot be bypassed

5. **Features return gradually**: Enterprise features will be reintroduced over versions 2.2.x through 3.0.0, each with educational context

### The Lite Edition Philosophy

```
Enterprise (v2.0.1)          →    Lite (v2.1.0)
─────────────────────────────────────────────────
6,500 lines                  →    ~900 lines
23 principles                →    5 principles
20 documentation modules     →    Core docs only
5 presets                    →    1 preset
Automation-focused           →    Education-focused
```

## Consequences

### Positive

1. **Better Understanding**: Users who take time to learn create better governance
2. **Reduced Exploitation**: Harder to mass-generate professional facades
3. **Appropriate Complexity**: Projects get governance proportional to their needs
4. **Forced Customization**: Templates that obviously need editing get edited
5. **Ethical Foundation**: Principle Zero ("Do no harm") is now central, not peripheral

### Negative

1. **Slower Adoption**: Users wanting quick solutions may look elsewhere
2. **More Effort Required**: Proper governance now requires learning
3. **Gradual Feature Return**: Enterprise users must wait for full feature set
4. **Perception Challenge**: "Lite" may be perceived as "incomplete"

### Neutral

1. **Community Filtering**: Attracts users who value understanding over speed
2. **Documentation Burden**: More educational content must be written and maintained

## Alternatives Considered

### 1. Keep Enterprise Edition
Continue with full feature set but add warnings.

**Rejected because**: Warnings are easily ignored. The exploitation potential remained too high.

### 2. Paid Enterprise / Free Lite
Commercial model for full features.

**Rejected because**: Paywalling governance tools contradicts open source values and doesn't address education problem.

### 3. Certification Requirement
Require quiz completion before full features.

**Rejected because**: Gameable and creates friction without guaranteeing understanding.

### 4. Gradual Unlock (Chosen)
Start with educational lite, add features over time with context.

**Selected because**: Balances immediate utility with long-term understanding, allows course correction, demonstrates commitment to education.

## Implementation

### Phase 1: Lite Release (v2.1.0) ✓
- Strip to 5 core principles
- Add ethical framework
- Implement safeguards
- Release as starting point

### Phase 2: Feature Reintroduction (v2.2.0 - v2.5.0)
- Each version adds principles with educational context
- Priority assessment gates additions (impact, effort, risk)
- Documentation explains WHAT/WHY/HOW for each feature

### Phase 3: Modular Enterprise (v3.0.0)
- Plugin architecture for governance modules
- Preset system returns (minimal → enterprise)
- Full feature parity with original, plus education

## Related Decisions

- [ADR 0002: Semantic Versioning Strategy](0002-semantic-versioning-strategy.md) (v2.6.0)
- [ADR 0003: Advisory Expiration System](0003-advisory-expiration.md) (v2.6.0)
- [ADR 0004: Modular Package Architecture](0004-modular-package-architecture.md) (v2.6.0)
- [ADR 0005: Governance Preset System](0005-preset-system.md) (v2.7.0)
- ADR 0006: Plugin Architecture (v2.11.0)

## References

- [ETHICS.md](../../ETHICS.md) - Full ethical framework
- [ROADMAP.md](../../ROADMAP.md) - Feature reintroduction timeline
- [MIGRATION.md](../../MIGRATION.md) - Upgrade guidance

---

*This ADR follows the education-first approach it describes: explaining WHAT the decision is, WHY it was made, and HOW it will be implemented.*
