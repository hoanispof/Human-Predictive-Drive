# Rewrite Plan v3 — Quality Sweep

> **Created**: 2026-06-10
> **Supersedes**: plan-rewrite v2 (R01–R19 ALL COMPLETE)
> **Source**: [audit-translation-comparison.md](audit-translation-comparison.md) (re-audit 2026-06-10) + TOC audit
> **Status**: ACTIVE

---

## §0 — Criteria

**Rule**: Rewrite if **Char% < 99.5%** OR **English missing TOC while source has one**.

**Rationale**:
- v2 plan (R01–R19) fixed 19 files — all confirmed complete via re-audit
- Re-audit with proper Unicode counting shows 15 files still below 99.5%
- TOC audit found 3 files where English lacks Table of Contents (all 3 already captured by Char% rule)
- Threshold raised from v2's 97% → 99.5% because framework quality standard demands near-parity
- Action: delete English file, retranslate from scratch. Same workflow as plan-english-translation.md v5.0

**Method**: Delete current English file → Deep Read source → Plan → Execute (3-phase per file)

---

## §1 — Summary

| | Files | Source Chars | % of framework |
|---|---:|---:|---:|
| **REWRITE** | **15** | **1,443,293** | **10.0%** |
| OK (>= 99.5%) | 230 | 12,982,766 | 90.0% |
| **TOTAL** | **245** | **14,426,059** | |

| Phase | Files | Source Chars |
|---|---:|---:|
| C — Chunk | 2 | 192,860 |
| D — PFC | 1 | 105,752 |
| E — Feeling | 1 | 99,337 |
| F — Body-Base Root | 1 | 39,562 |
| G — Observation | 1 | 138,346 |
| H — Collective+Domain | 4 | 269,782 |
| I — Research | 5 | 597,654 |

### Special flags

| File | Extra issue |
|---|---|
| Somatic-Articulation-Loop.md | English MISSING Table of Contents |
| Child-Development-Mechanism.md | English MISSING Table of Contents |
| Love-Romantic.md | English MISSING Table of Contents |

---

## §2 — Rewrite List (15 files, dependency order)

### Phase C — Chunk (2 files)

| # | Source (Vietnamese) | English (xoa + tao lai) | S.Lines | S.Chars | E.Lines | E.Chars | Char% |
|---:|---|---|---:|---:|---:|---:|---:|
| R01 | [By-Product-Gap-Resonance.md](../Core-Deep-Dive/Body-Base/Chunk/Agent-Mechanism/By-Product-Gap-Resonance.md) | [English](../English/Core-Deep-Dive/Body-Base/Chunk/Agent-Mechanism/By-Product-Gap-Resonance.md) | 1,711 | 73,392 | 1,810 | 70,874 | 96.6% |
| R02 | [Agent-Mechanism.md](../Core-Deep-Dive/Body-Base/Chunk/Agent-Mechanism/Agent-Mechanism.md) | [English](../English/Core-Deep-Dive/Body-Base/Chunk/Agent-Mechanism/Agent-Mechanism.md) | 2,363 | 119,468 | 2,348 | 116,597 | 97.6% |

- [x] R01 By-Product-Gap-Resonance.md (96.6%) — COMPLETE 2026-06-11
- [x] R02 Agent-Mechanism.md (97.6%) — COMPLETE 2026-06-11

---

### Phase D — PFC (1 file)

| # | Source (Vietnamese) | English (xoa + tao lai) | S.Lines | S.Chars | E.Lines | E.Chars | Char% | Note |
|---:|---|---|---:|---:|---:|---:|---:|---|
| R03 | [Somatic-Articulation-Loop.md](../Core-Deep-Dive/PFC/Imagination/Somatic-Articulation-Loop.md) | [English](../English/Core-Deep-Dive/PFC/Imagination/Somatic-Articulation-Loop.md) | 2,860 | 105,752 | 2,690 | 104,807 | 99.1% | MISSING TOC |

- [x] R03 Somatic-Articulation-Loop.md (99.1%, missing TOC) — COMPLETE 2026-06-11

---

### Phase E — Feeling (1 file)

| # | Source (Vietnamese) | English (xoa + tao lai) | S.Lines | S.Chars | E.Lines | E.Chars | Char% |
|---:|---|---|---:|---:|---:|---:|---:|
| R04 | [Feeling.md](../Core-Deep-Dive/Body-Base/Feeling/Feeling.md) | [English](../English/Core-Deep-Dive/Body-Base/Feeling/Feeling.md) | 2,244 | 99,337 | 2,178 | 97,489 | 98.1% |

- [x] R04 Feeling.md (98.1%) — COMPLETE 2026-06-11

---

### Phase F — Body-Base Root (1 file)

| # | Source (Vietnamese) | English (xoa + tao lai) | S.Lines | S.Chars | E.Lines | E.Chars | Char% |
|---:|---|---|---:|---:|---:|---:|---:|
| R05 | [Valence-Propagation.md](../Core-Deep-Dive/Body-Base/Valence-Propagation.md) | [English](../English/Core-Deep-Dive/Body-Base/Valence-Propagation.md) | 943 | 39,562 | 897 | 38,372 | 97.0% |

- [x] R05 Valence-Propagation.md (97.0%) — COMPLETE 2026-06-11

---

### Phase G — Observation (1 file)

| # | Source (Vietnamese) | English (xoa + tao lai) | S.Lines | S.Chars | E.Lines | E.Chars | Char% |
|---:|---|---|---:|---:|---:|---:|---:|
| R06 | [Empathy.md](../Core-Deep-Dive/Observation/Empathy.md) | [English](../English/Core-Deep-Dive/Observation/Empathy.md) | 2,905 | 138,346 | 2,918 | 134,365 | 97.1% |

- [x] R06 Empathy.md (97.1%) — COMPLETE 2026-06-11

---

### Phase H — Collective + Domain (4 files)

| # | Source (Vietnamese) | English (xoa + tao lai) | S.Lines | S.Chars | E.Lines | E.Chars | Char% |
|---:|---|---|---:|---:|---:|---:|---:|
| R07 | [Collective-Body.md](../Core-Deep-Dive/Collective/Collective-Body.md) | [English](../English/Core-Deep-Dive/Collective/Collective-Body.md) | 1,903 | 89,106 | 1,813 | 86,554 | 97.1% |
| R08 | [Coordination-Node.md](../Core-Deep-Dive/Collective/Coordination-Node.md) | [English](../English/Core-Deep-Dive/Collective/Coordination-Node.md) | 2,221 | 103,095 | 2,145 | 100,478 | 97.5% |
| R09 | [Discovery-vs-Expansion.md](../Core-Deep-Dive/Domain/Discovery-vs-Expansion.md) | [English](../English/Core-Deep-Dive/Domain/Discovery-vs-Expansion.md) | 1,067 | 47,853 | 1,013 | 46,909 | 98.0% |
| R10 | [Domain.md](../Core-Deep-Dive/Domain/Domain.md) | [English](../English/Core-Deep-Dive/Domain/Domain.md) | 716 | 29,728 | 682 | 29,290 | 98.5% |

- [x] R07 Collective-Body.md (97.1%) — COMPLETE 2026-06-11
- [x] R08 Coordination-Node.md (97.5%) — COMPLETE 2026-06-11
- [x] R09 Discovery-vs-Expansion.md (98.0%) — COMPLETE 2026-06-11
- [x] R10 Domain.md (98.5%) — COMPLETE 2026-06-11

---

### Phase I — Research (5 files)

| # | Source (Vietnamese) | English (xoa + tao lai) | S.Lines | S.Chars | E.Lines | E.Chars | Char% | Note |
|---:|---|---|---:|---:|---:|---:|---:|---|
| R11 | [Child-Development-Mechanism.md](../Research/Human-Learning/Child-Development/Child-Development-Mechanism.md) | [English](../English/Research/Human-Learning/Child-Development/Child-Development-Mechanism.md) | 3,276 | 140,634 | 2,680 | 129,187 | 91.9% | MISSING TOC |
| R12 | [Love-Romantic.md](../Research/Love-Romantic.md) | [English](../English/Research/Love-Romantic.md) | 3,297 | 157,020 | 2,655 | 147,944 | 94.2% | MISSING TOC |
| R13 | [Love-Unified.md](../Research/Love-Unified.md) | [English](../English/Research/Love-Unified.md) | 2,556 | 123,327 | 2,451 | 120,631 | 97.8% | |
| R14 | [ADHD-Observation.md](../Research/Health-Conditions/Neurodiversity/ADHD-Observation.md) | [English](../English/Research/Health-Conditions/Neurodiversity/ADHD-Observation.md) | 2,182 | 88,656 | 2,143 | 87,244 | 98.4% | |
| R15 | [OCD-Analysis.md](../Research/Health-Conditions/OCD-Analysis.md) | [English](../English/Research/Health-Conditions/OCD-Analysis.md) | 1,540 | 69,067 | 1,479 | 68,202 | 98.7% | |

- [x] R11 Child-Development-Mechanism.md (91.9%, missing TOC) — COMPLETE 2026-06-10
- [x] R12 Love-Romantic.md (94.2%, missing TOC) — COMPLETE 2026-06-11
- [x] R13 Love-Unified.md (97.8%) — COMPLETE 2026-06-11
- [x] R14 ADHD-Observation.md (98.4%) — COMPLETE 2026-06-11
- [x] R15 OCD-Analysis.md (98.7%) — COMPLETE 2026-06-11

---

## §3 — Workflow

```
Step 1: Tao plan v3                            ← DONE
Step 2: Rewrite R01 → R15 theo dependency order ← NEXT
Step 3: Re-audit sau khi xong → verify ALL Char% >= 99.5% AND TOC present
```

**Suggested execution order** (dependency-first, then lowest Char% first):

| Priority | Files | Rationale |
|---|---|---|
| 1st | R11 (91.9%), R12 (94.2%) | Lowest Char% + missing TOC — most urgent |
| 2nd | R01 (96.6%) → R02 (97.6%) | C phase dependency chain (R02 hub needs R01 first) |
| 3rd | R03 (99.1%) | Missing TOC, otherwise near-complete |
| 4th | R04–R06 | One file each, independent |
| 5th | R07–R10 | H phase cluster, can parallelize |
| 6th | R13–R15 | Research files, independent, highest Char% |

## §4 — History

| Version | Date | Files | Status |
|---|---|---:|---|
| v2 | 2026-06-10 | 19 (R01–R19) | ALL COMPLETE |
| **v3** | **2026-06-10** | **15 (R01–R15)** | **ACTIVE** |

## §5 — Notes

- v2 plan (19 files) is 100% complete — all R01–R19 confirmed via re-audit
- v3 raises quality bar from Char% 97% → 99.5%
- 3 files with missing TOC are all captured by Char% criterion (no extra files needed)
- Glossary: 00-Glossary.md — terminology established, load every session
- Estimated sessions: ~10-14
