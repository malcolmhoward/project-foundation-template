# Dogfooding Procedure

This document explains how Project Foundation Template validates itself through dogfooding.

## What is Dogfooding?

**Dogfooding** (or "eating your own dog food") is the practice of using your own product to validate its quality. For PFT, this means running the template generator against itself and comparing the output to existing governance files.

See [GLOSSARY.md](../../GLOSSARY.md#dogfooding) for the formal definition.

## Why Dogfood PFT?

| Purpose | Benefit |
|---------|---------|
| **Validation** | Verify template quality through real-world application |
| **Credibility** | Demonstrate commitment to our own principles ("practice what you preach") |
| **Discovery** | Identify template improvements through self-application |
| **Documentation** | Create provenance records for PFT's governance files |

## When to Dogfood

Trigger a dogfooding exercise when:

1. **Major/minor releases** - Before releasing v3.x.0, validate templates still align with PFT's own governance
2. **Significant template changes** - After modifying principle or guide templates
3. **New preset introduction** - Verify new presets generate coherent governance
4. **Periodic review** - At least annually to catch drift

## How to Dogfood

### Step 1: Generate Comparison Output

```bash
python generate_foundation.py \
  --preset strict \
  --project-name "Project Foundation Template" \
  --author-name "Malcolm Howard" \
  --output-dir ./pft-dogfood-output \
  --include-generation-log \
  --log-format both \
  --non-interactive \
  --accept-terms
```

**Why strict preset?** PFT is a security-conscious project that generates governance for others. The strict preset (12 principles) is appropriate for this context.

### Step 2: Compare Generated vs Existing

For each generated file, compare against existing:

```bash
# Example comparison
diff pft-dogfood-output/README.md README.md
diff pft-dogfood-output/CONTRIBUTING.md CONTRIBUTING.md
# ... etc
```

Document findings for each file:
- **Structural alignment**: Do sections match in intent?
- **Where existing exceeds template**: Template improvement candidates
- **Where generated has features existing lacks**: Potential additions

### Step 3: Document Findings

Update or create `docs/dogfood/DELTA_ANALYSIS.md` with:

1. Executive summary of findings
2. File-by-file comparison table
3. Template improvement opportunities (prioritized)
4. Files to adopt vs keep existing

### Step 4: Update Provenance

Update `GENERATION_LOG.md` with current file statuses:

| Status | Meaning |
|--------|---------|
| pre-existing, aligned | Matches template intent |
| pre-existing, enhanced | Exceeds template quality |
| unique | PFT-specific, not in template output |
| generated | Adopted from generator output |
| generated, customized | Adopted and customized |

### Step 5: Create/Update ADR

If this is a significant dogfooding exercise, update or reference [ADR-0011](../adr/0011-pft-self-governance.md).

### Step 6: Clean Up

After review, decide whether to keep or remove `pft-dogfood-output/`:
- **Keep**: If useful as ongoing reference
- **Remove**: If comparison is complete and documented

## Expected Outputs

A complete dogfooding exercise produces:

| Deliverable | Purpose |
|-------------|---------|
| `pft-dogfood-output/` | Generated comparison files (temporary) |
| `docs/dogfood/DELTA_ANALYSIS.md` | Comparison insights and recommendations |
| `GENERATION_LOG.md` | Updated file provenance |
| GitHub issues (optional) | Template improvement tracking |

## Governance Alignment

Dogfooding supports these PFT principles:

- **Education-First**: Learning from our own output
- **Transparency**: Documenting file provenance
- **Continuous Improvement**: Identifying template enhancements
- **Credibility**: Practicing what we preach

## History

| Date | Version | Notes |
|------|---------|-------|
| 2026-01-30 | v3.7.0 | Initial dogfooding exercise, created this procedure |

## Related Documents

- [DELTA_ANALYSIS.md](DELTA_ANALYSIS.md) - Comparison findings from strict preset generation
- [FILE_INVENTORY_ANALYSIS.md](FILE_INVENTORY_ANALYSIS.md) - Complete project file analysis
- [GENERATION_LOG.md](../../GENERATION_LOG.md) - File provenance tracking
- [ADR-0011](../adr/0011-pft-self-governance.md) - Self-governance decision
- [GLOSSARY.md](../../GLOSSARY.md#dogfooding) - Term definition
