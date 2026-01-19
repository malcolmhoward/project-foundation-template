# ADR 0001: Education-First Approach

## Status

Accepted

## Date

2025-10-29 (Updated: 2026-01-18)

## Context

The original Project Foundation Template (v1.x and early v2.x) was a comprehensive governance generator with:
- ~6,500 lines of code
- 23 governance principles
- 20 documentation modules
- 5 preset configurations (minimal through enterprise)

While powerful, this approach created several problems:

### The Automation Trap

Users could generate complete governance suites without understanding what any of it did. This led to:
- **Governance theater**: Appearance of compliance without substance
- **Copy-paste culture**: Templates used verbatim without customization
- **False confidence**: Believing generated files equals actual security or compliance
- **Skill atrophy**: Developers who could generate but not explain their governance

### Exploitation Potential

A tool that generates professional-looking governance at scale enables:
- **Supply chain attacks**: Legitimate-looking malicious packages with trustworthy governance
- **Phishing**: Professional-appearing project facades designed to deceive
- **Legal misrepresentation**: Templates claimed as actual compliance
- **Social engineering**: Trust signals weaponized for manipulation

### Environmental Concerns

Full governance suites include CI/CD workflows that:
- Run on every commit regardless of necessity
- Consume compute resources and energy
- Provide false confidence through green checkmarks
- Contribute to carbon footprint without proportional value

### The Core Problem

The tool was optimized for the wrong metric. It measured success by how many governance files it could generate, not by how well users understood what they were generating. This created a perverse incentive: the more comprehensive the tool, the less users needed to learn.

## Decision

We will adopt an **education-first approach** where:

### 1. Understanding Precedes Generation

Users must engage with educational content before receiving templates. Each template is preceded by:
- **WHAT**: A clear definition of what this template is
- **WHY**: Why it matters and what problem it solves
- **HOW**: How to customize it properly

### 2. Less Is More

The "lite" edition includes only 5 core principles instead of 23, forcing users to:
- Consciously add complexity as needed
- Justify each addition
- Understand what they are adding
- Start simple and grow deliberately

### 3. Templates Are Starting Points

Generated files explicitly mark themselves as templates requiring customization:
- Clear warnings at the top of each file
- Placeholder text that must be replaced
- Educational comments explaining each section
- Links back to documentation

### 4. Safeguards Are Mandatory

Ethical agreement, educational delays, and usage logging cannot be bypassed:
- No "skip intro" option
- No bulk generation without acknowledgment
- No silent operation that hides the educational content

### 5. Features Return Gradually

Enterprise features will be reintroduced over versions 2.2.x through 3.0.0, each with:
- Educational context explaining the feature
- Priority assessment of impact, effort, and risk
- Ethical review for potential misuse
- Documentation following WHAT/WHY/HOW pattern

### The Lite Edition Philosophy

```
Enterprise (v2.0.1)          -->    Lite (v2.1.0)
-------------------------------------------------
6,500 lines                  -->    ~820 lines
23 principles                -->    5 principles
20 documentation modules     -->    Core docs only
5 presets                    -->    1 preset
Automation-focused           -->    Education-focused
Speed optimized              -->    Understanding optimized
```

## Consequences

### Positive

1. **Better Understanding**: Users who take time to learn create better governance that actually serves their needs
2. **Reduced Exploitation**: Harder to mass-generate professional facades for malicious purposes
3. **Appropriate Complexity**: Projects get governance proportional to their needs, not maximum possible
4. **Forced Customization**: Templates that obviously need editing actually get edited
5. **Ethical Foundation**: Principle Zero ("Do no harm") is now central, not peripheral
6. **Sustainable Growth**: Features return with education, building understanding incrementally
7. **Community Quality**: Attracts users who value substance over appearance

### Negative

1. **Slower Adoption**: Users wanting quick solutions may look elsewhere
2. **More Effort Required**: Proper governance now requires learning
3. **Gradual Feature Return**: Enterprise users must wait for full feature set
4. **Perception Challenge**: "Lite" may be perceived as "incomplete" or "inferior"
5. **Documentation Burden**: More educational content must be written and maintained
6. **Competitive Disadvantage**: Other tools offer faster, less educational paths

### Neutral

1. **Community Filtering**: Attracts users who value understanding over speed (positive for community quality, negative for adoption numbers)
2. **Documentation Investment**: More educational content to maintain (burden but also differentiator)
3. **Version Complexity**: Gradual feature return requires careful version management

## Alternatives Considered

### 1. Keep Enterprise Edition

Continue with full feature set but add warnings.

**Rejected because**: Warnings are easily ignored. The exploitation potential remained too high. Users proved they would click through any warning to get their files faster.

### 2. Paid Enterprise / Free Lite

Commercial model for full features.

**Rejected because**: Paywalling governance tools contradicts open source values. Does not address education problem. Creates perverse incentive to make lite version worse.

### 3. Certification Requirement

Require quiz completion before full features.

**Rejected because**: Gameable (answers can be shared). Creates friction without guaranteeing understanding. Feels patronizing without being effective.

### 4. Time-Based Unlock

Require minimum time before generation completes.

**Rejected because**: Annoying for legitimate users. Does not guarantee engagement. Can be circumvented with automation.

### 5. Gradual Unlock (Chosen)

Start with educational lite, add features over time with context.

**Selected because**: Balances immediate utility with long-term understanding. Allows course correction based on feedback. Demonstrates commitment to education. Creates natural pacing for learning.

## Implementation

### Phase 1: Lite Release (v2.1.0) - COMPLETED

- Stripped to 5 core principles
- Added ethical framework
- Implemented all 5 safeguards
- Released as educational starting point
- Documented rationale in this ADR

### Phase 2: Core Infrastructure (v2.2.0) - COMPLETED

- Added `--non-interactive` mode for CI/CD
- Added `.foundationrc` configuration support
- Added `--export-json` for machine-readable output
- Added `--quiet` mode with educational minimum
- Improved error messages with guidance

### Phase 3: Community Governance (v2.3.0) - COMPLETED

- Added Issue templates (bug, feature request)
- Added PR template
- Added CHANGELOG.md generation
- Principles 6-10 added with education

### Phase 4: Security Features (v2.4.0) - COMPLETED

- Added enhanced SECURITY.md option
- Added secrets detection pre-commit hooks
- Principles 11-15 added with education

### Phase 5: Advanced Governance (v2.5.0) - COMPLETED

- Added ADR system
- Added CI workflow generation
- Principles 16-20 added with education
- Documentation guides system added

### Phase 6: Modular Architecture (v2.6.0 - v2.9.0) - IN PROGRESS

- Extracting to `core/` package structure
- Creating separate modules for principles, presets, guides
- Building comprehensive test suite
- Preparing for v3.0.0 plugin architecture

### Phase 7: Full Plugin Architecture (v3.0.0) - PLANNED

- Plugin system for governance modules
- All 5 presets (minimal through enterprise) available
- Full 23 principle set with education
- Complete 20 documentation modules
- Comprehensive test coverage

## Metrics for Success

How we know this decision is working:

1. **Usage Quality**: Projects using templates show evidence of customization
2. **Community Feedback**: Users report better understanding of governance
3. **Exploitation Reports**: No significant reports of templates used for malicious purposes
4. **Contribution Quality**: PRs show understanding of educational philosophy
5. **Support Requests**: Questions shift from "how to generate" to "how to customize"

## Related Decisions

- [ADR 0002: Semantic Versioning Strategy](0002-semantic-versioning-strategy.md) (v2.6.0)
- [ADR 0003: Advisory Expiration System](0003-advisory-expiration.md) (v2.6.0)
- [ADR 0004: Modular Package Architecture](0004-modular-package-architecture.md) (v2.6.0)
- [ADR 0005: Governance Preset System](0005-preset-system.md) (v2.7.0)
- [ADR 0006: Plugin Architecture](0006-plugin-architecture.md) (v2.11.0)

## References

- [ETHICS.md](../../ETHICS.md) - Full ethical framework with Five Risks and Five Safeguards
- [ROADMAP.md](../../ROADMAP.md) - Feature reintroduction timeline
- [MIGRATION.md](../../MIGRATION.md) - Upgrade guidance between versions
- [SEMANTIC_VERSIONING.md](../../SEMANTIC_VERSIONING.md) - Version numbering strategy

---

*This ADR follows the education-first approach it describes: explaining WHAT the decision is, WHY it was made, and HOW it will be implemented.*
