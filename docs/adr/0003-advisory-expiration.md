# ADR 0003: Advisory Expiration System

## Status

Accepted

## Date

2026-01-18

## Context

Governance templates can become dangerous when outdated:

### The Stale Template Problem

1. **Security practices evolve**: What was secure in 2024 may have known vulnerabilities in 2026
2. **Compliance requirements change**: Regulations update, templates don't
3. **Best practices shift**: Community standards improve over time
4. **False confidence**: Old templates look professional but teach outdated patterns

### Traditional Approaches

| Approach | Problem |
|----------|---------|
| No expiration | Templates used indefinitely, becoming stale |
| Hard expiration (blocks usage) | Breaks CI/CD, frustrates users, paternalistic |
| "Latest version" checks | Requires network, privacy concerns |
| Manual "check for updates" | Easily ignored |

### The Philosophical Tension

We want to:
- **Encourage updates** without **forcing them**
- **Warn about staleness** without **blocking work**
- **Prompt review** without **creating friction**

This aligns with Principle Zero: "Do no harm, allow no harm" — we shouldn't harm users by blocking legitimate work, but we shouldn't allow harm from dangerously outdated templates.

## Decision

We implement an **Advisory Expiration System** with the following characteristics:

### 1. Date-Based Expiration

Each version has a hardcoded expiration date:

```python
# core/utils.py
SCRIPT_VERSION = "2.6.0-lite"
EXPIRATION_DATE = date(2026, 3, 1)  # ~6 months from release
```

### 2. Advisory, Not Blocking

When expired, the tool:
- **Displays a prominent warning**
- **Explains why expiration matters**
- **Provides update instructions**
- **Allows continuation after acknowledgment**

```
⚠️  VERSION OUTDATED - SECURITY RISK

This version expired on 2026-03-01.
Security practices and compliance requirements have likely changed.

Using outdated templates may introduce vulnerabilities or compliance issues.

Get the latest version at: https://github.com/malcolmhoward/project-foundation-template
```

### 3. Acknowledgment Required (Interactive Mode)

In interactive mode, users must type a specific phrase:

```
Type 'I understand the risks' to continue anyway: _
```

This ensures:
- Users consciously acknowledge the risk
- The warning cannot be accidentally dismissed
- There's an audit trail of informed consent

### 4. Bypass for Automation (Non-Interactive Mode)

In non-interactive mode (CI/CD):
- Warning is displayed but doesn't block
- `--accept-terms` flag implies awareness
- Log entry records outdated usage

### 5. Expiration Window

Standard expiration is **6 months** from release:

| Version | Release | Expiration |
|---------|---------|------------|
| v2.6.0 | ~2025-09 | 2026-03-01 |
| v2.7.0 | TBD | +6 months |

**Rationale**: 6 months balances:
- Enough time for users to adopt and use
- Not so long that templates become dangerously stale
- Aligns with typical security review cycles

## Consequences

### Positive

1. **Promotes currency**: Users are regularly reminded to update
2. **Non-blocking**: Legitimate work continues even with warnings
3. **Educational**: Warning explains WHY updates matter
4. **Auditable**: Usage logs record when expired versions are used
5. **Privacy-respecting**: No network calls to check versions

### Negative

1. **Warning fatigue**: Frequent warnings may be ignored
2. **Arbitrary dates**: 6 months is a heuristic, not precise
3. **Offline scenarios**: Can't know if newer version exists
4. **Maintenance burden**: Must update expiration with each release

### Neutral

1. **Friction by design**: The friction is intentional — it prompts review
2. **Local enforcement**: No server dependency, works offline

## Alternatives Considered

### 1. No Expiration
Let templates be used indefinitely.

**Rejected because**: Enables "set and forget" with potentially dangerous stale templates.

### 2. Hard Expiration (Blocking)
Refuse to run after expiration date.

**Rejected because**:
- Breaks CI/CD pipelines unexpectedly
- Paternalistic — users should make informed choices
- Could block critical work in emergencies

### 3. Online Version Check
Check GitHub for latest version on each run.

**Rejected because**:
- Privacy concerns (network traffic reveals usage)
- Fails in air-gapped environments
- Adds latency and failure modes

### 4. Subscription/License Model
Require active subscription for updates.

**Rejected because**: Contradicts open-source values and accessibility goals.

### 5. No Bypass Option
Require acknowledgment even in CI/CD.

**Rejected because**: Would require interactive input in automated pipelines.

## Implementation

### Expiration Check

```python
# core/utils.py
def check_expiration() -> bool:
    """Check if the script has expired."""
    return date.today() > EXPIRATION_DATE
```

### Warning Display

```python
# setup_foundation_lite.py
def check_version_advisory(self):
    """Advisory version check - warns but doesn't block."""
    if date.today() > EXPIRATION_DATE:
        print(f"""
⚠️  VERSION OUTDATED - SECURITY RISK

This version expired on {EXPIRATION_DATE.isoformat()}.
...
""")
        if self.is_interactive:
            response = input("Type 'I understand the risks' to continue anyway: ")
            if response.strip() != "I understand the risks":
                print("❌ Exiting for your safety. Please get the latest version.")
                return False
    return True
```

### Usage Logging

Expiration status is logged locally:

```python
log_entry = {
    "timestamp": datetime.now().isoformat(),
    "version": SCRIPT_VERSION,
    "outdated": date.today() > EXPIRATION_DATE,  # Tracks expired usage
    ...
}
```

### Distinct from Versioning

| Concept | Purpose | Mechanism | Example |
|---------|---------|-----------|---------|
| Version | Track changes | SemVer | v2.6.0 |
| Expiration | Prompt updates | Date check | 2026-03-01 |

A template can be the **latest version** but still **expired** — this means "even the newest version is old."

## Migration Path

When updating versions:

1. Set new `SCRIPT_VERSION`
2. Set new `EXPIRATION_DATE` (release date + 6 months)
3. Document in CHANGELOG

## Related Decisions

- ADR 0001: Education-First Approach (expiration supports continuous learning)
- ADR 0002: Semantic Versioning Strategy (expiration complements versioning)
- ADR 0004: Modular Package Architecture (v2.6.0)

## References

- [SEMANTIC_VERSIONING.md](../../SEMANTIC_VERSIONING.md) - Explains expiration vs. versioning
- [ETHICS.md](../../ETHICS.md) - Lists expiration as ethical safeguard
- `core/utils.py:50-57` - Implementation of `check_expiration()`

---

*Expiration is not punishment — it's a gentle nudge toward currency. The goal is informed users, not blocked users.*
