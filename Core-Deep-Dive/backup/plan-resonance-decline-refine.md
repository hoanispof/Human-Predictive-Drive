# Plan — Resonance Decline Full Refine

```
Status:    ✅✅ CLOSED — ALL 10 sessions + FINAL VERIFY DONE (2026-05-29)
Created:   2026-05-29
Scope:     ~46 active files, ~545 M-label occurrences
Model:     4 mechanisms (M1-M4) → 2 Forces + 1 Fuel + Gap Drift
Source:    Plan-R-v2-Reframe.md §1 (conceptual foundation)
           Plan-rename-m1-Mn/ (L/E/F sub-plans)
Survey:    2026-05-29 full framework rà soát
```

---

## §0 — BỐI CẢNH

Plan này **THAY THẾ** session plan trong Plan-R-v2-Reframe.md §4 (R1-R7).
Plan-R-v2 vẫn giữ §1-§3 (conceptual model + naming + file categorization) làm REFERENCE.
File này = EXECUTION PLAN sau khi survey toàn framework.

### Tại sao plan mới?

Survey 2026-05-29 phát hiện:
1. **Category B bị underestimate**: 5 files (Empathy, Love-Romantic, Body-Coupling, Love-Unified, Connection-Education) có PER-MECHANISM analysis sections → cần conceptual reframe, KHÔNG chỉ rename
2. **"M2+M3+M4" grouping invalid**: Mọi chỗ group "M2+M3+M4" cần careful rewrite (② = force, M3+M4 = fuel)
3. **Version refs lỗi thời**: ~40+ files ghi "Bond-Architecture v1.0" → v2.0
4. **Boredom scope lớn hơn dự kiến**: 50 occ across ~10 sections (không chỉ §3)

---

## §1 — CONCEPTUAL MODEL (Quick Reference)

```
2 FORCES (observable, ĐO ĐƯỢC):
  ① COMPILED-SUPPRESS — tấn công NGUỒN (★ LEVERAGE POINT)
  ② REWARD-HABITUATED — hardware adaptation (Weber-Fechner)

1 FUEL (calibration parameter — threshold-based, KHÔNG đo chính xác):
  NOVELTY ≥ THRESHOLD?
    Absorbs cũ M3 (prediction-delta=0) + M4 (Entity-Compiled saturated)
    = 2 lenses cùng 1 phenomenon

CONTEXTUAL FACTOR:
  GAP DRIFT — direction match ↓

INTERACTION: ① accelerate ② + drain novelty. Fix ① = leverage.
SATIATION: ① attacks Tonic+Generative. ② = Tonic declining. Novelty = Generative alive/dead.

Chi tiết: Plan-R-v2-Reframe.md §1
```

---

## §2 — FILE RECLASSIFICATION (6 Tiers)

### Tier 1: SOURCE DEFINITION ✅ DONE

```
┌──────────────────────────────────┬──────┬────────────────────────────┐
│ File                             │ ~Occ │ Status                     │
├──────────────────────────────────┼──────┼────────────────────────────┤
│ Bond-Architecture.md §4          │  42  │ ✅ R1 DONE (v1.0→v2.0)     │
│ Resonance-Sustainability.md §9   │  18  │ ✅ R2 DONE                  │
│ By-Product-Gap-Resonance.md §10  │  43  │ ✅ R2 DONE                  │
└──────────────────────────────────┴──────┴────────────────────────────┘
```

### Tier 2: DEEP CONCEPTUAL REWRITE (per-mechanism sections → 2 Forces + 1 Fuel)

```
Files có SEPARATE per-mechanism analysis (M1/M2/M3/M4 phân tích riêng).
Cần: đọc kỹ → merge M3+M4 vào novelty → thêm Gap Drift → rewrite interaction.

┌──────────────────────────────────┬──────┬─────────────────────────────────────┐
│ File                             │ ~Occ │ Section + Notes                     │
├──────────────────────────────────┼──────┼─────────────────────────────────────┤
│ Boredom.md                       │  50  │ §3 (4 sub-mechanisms) + §9 diagno- │
│                                  │      │ stic + §10 fix + scattered.         │
│                                  │      │ DEEPEST rewrite after Tier 1.       │
├──────────────────────────────────┼──────┼─────────────────────────────────────┤
│ Connection.md                    │  42  │ §4.5 (120L per-mechanism + gap      │
│                                  │      │ clone + anti-suppress) + scattered. │
├──────────────────────────────────┼──────┼─────────────────────────────────────┤
│ Resonance-Per-Entity.md §14      │ ~20  │ §14 "Chán" per-entity (M1-M4 per   │
│  (Decline portion only)          │      │ entity type) + D3 columns.          │
│                                  │      │ ⚠️ AFTER Plan E (§3-§9 Entity Prof) │
├──────────────────────────────────┼──────┼─────────────────────────────────────┤
│ Empathy.md                       │  28  │ §8.7 (M1-M4 per-bond analysis)     │
│                                  │      │ + §8.2 burnout (M1) + scattered.    │
├──────────────────────────────────┼──────┼─────────────────────────────────────┤
│ Love-Romantic.md                 │  29  │ §11.8 (M1-M4 × romantic, full per- │
│                                  │      │ mechanism + interaction model) +     │
│                                  │      │ §P10 research prediction.           │
├──────────────────────────────────┼──────┼─────────────────────────────────────┤
│ Body-Coupling.md                 │  22  │ §2.3 (M1-M4 × entanglement, per-   │
│                                  │      │ mechanism) + scattered.             │
├──────────────────────────────────┼──────┼─────────────────────────────────────┤
│ Love-Unified.md                  │  35  │ §6.2 (M1-M4 × 6 love types, per-  │
│                                  │      │ mechanism risk breakdown).           │
│                                  │      │ ⚠️ AFTER Plan L (§5 Quality Dims)   │
├──────────────────────────────────┼──────┼─────────────────────────────────────┤
│ Connection-Education.md          │  30  │ §6.2 (M1-M4 per-mechanism +         │
│                                  │      │ 4 countermeasures). Education app.  │
└──────────────────────────────────┴──────┴─────────────────────────────────────┘

Tier 2 total: 8 files, ~256 occ
```

### Tier 3: PREREQUISITE PLANS (L + E + F)

```
Phải hoàn thành TRƯỚC Tier 4+ vì:
- Plan L: xóa Love Quality M-labels → Love-Unified chỉ còn Decline
- Plan E: xóa Entity Profile M-labels → RPE chỉ còn Decline
- Plan F: xóa Firing Mode M-labels → Body-Base/Discovery/DMD chỉ còn Decline

┌──────────────────────────────────┬──────┬─────────────────────────────────────┐
│ Plan                             │ ~Occ │ Scope + Files                       │
├──────────────────────────────────┼──────┼─────────────────────────────────────┤
│ Plan L (Love Quality Dims)       │   5  │ Love-Unified §5 (1 file)            │
│                                  │      │ Plan: Plan-L-Love-Quality.md        │
├──────────────────────────────────┼──────┼─────────────────────────────────────┤
│ Plan E (Entity Profile Params)   │ ~80  │ RPE §3-§9 (1-2 files, MANUAL)      │
│                                  │      │ Plan: Plan-E-Entity-Profile.md      │
├──────────────────────────────────┼──────┼─────────────────────────────────────┤
│ Plan F (Firing Modes)            │ ~30  │ Body-Base, Discovery, DMD (3 files) │
│                                  │      │ + cross-ref fixes                   │
│                                  │      │ Plan: Plan-F-Firing-Modes.md        │
└──────────────────────────────────┴──────┴─────────────────────────────────────┘

Tier 3 total: ~115 occ, 5-6 files
```

### Tier 4: STANDARD PROPAGATION (rename + minor reframe)

```
Brief M-label refs, deps, cross-refs. KHÔNG có per-mechanism sections.
Verified: Agent-Mechanism, Education-System, Core-Software = STANDARD.

┌──────────────────────────────────┬──────┬──────────────┐
│ File                             │ ~Occ │ Notes        │
├──────────────────────────────────┼──────┼──────────────┤
│ Agent-Mechanism.md               │  21  │ Brief list   │
│ Education-System.md              │  20  │ Brief list   │
│ Core-Software.md                 │  16  │ Inline       │
│ Education-Arms-Race.md           │  13  │ VERIFY       │
│ Status.md                        │  12  │              │
│ Idol-Phenomenon.md               │  10  │              │
│ Skill-Introduction.md            │   9  │              │
│ Domain-Knowledge-Map.md          │   9  │ VERIFY       │
│ 01-File-Index.md (CDD)           │   9  │              │
│ Protect.md                       │   8  │              │
│ Self-Pattern-Modeling.md         │   8  │              │
│ Natural-Development.md           │   8  │              │
│ Child-Development-Mechanism.md   │   8  │              │
│ Education-Mechanism.md           │  18  │ VERIFY       │
│ Religion.md                      │  17  │ VERIFY       │
│ Melody-Technology-Overview.md    │   6  │              │
│ By-Product-Scale.md              │   5  │              │
│ Inter-Body-Mechanism.md          │   5  │              │
└──────────────────────────────────┴──────┴──────────────┘

VERIFY = chưa confirmed, đọc khi thực hiện.
Nếu phát hiện per-mechanism section → escalate lên Tier 2.

Tier 4 total: ~18 files, ~202 occ
```

### Tier 5: LIGHT CLEANUP (1-3 occ each)

```
Dep-list updates, brief cross-refs, 1-dòng references.

┌──────────────────────────────────┬──────┐
│ File                             │ ~Occ │
├──────────────────────────────────┼──────┤
│ Background-Pattern.md            │   4  │
│ Chunk.md                         │   3  │
│ Valence-Propagation.md           │   3  │
│ Drill-Emergent-Pattern.md        │   3  │
│ Hardware-Calibration.md          │   3  │
│ Entity-Valence-Dynamics.md       │  11  │
│ Body-Base.md                     │  14  │
│ Gap-Distribution-Profile.md      │   2  │
│ Collective-Body.md               │   2  │
│ Coordination-Node.md             │   2  │
│ Expansion-Saturation-Crisis.md   │   2  │
│ Curriculum-Framework.md          │   2  │
│ VN-Recommendations.md            │   2  │
│ 01-File-Index.md (Research)      │   2  │
│ Entity-Access-Calibration.md     │   2  │
│ Gap-Body-Need.md                 │   1  │
│ Core-Hardware.md                 │   1  │
│ Neural-Processing-Flow.md        │   1  │
│ Entity-Access.md                 │   1  │
│ 00-Parameter-Overview.md         │   1  │
│ 00-Glossary.md                   │   1  │
│ 00_Overview.md (Edu-System)      │   1  │
│ Money-Education.md               │   1  │
│ VN-Education-Status.md           │   1  │
└──────────────────────────────────┴──────┘

⚠️ Body-Base.md (14 occ) và Entity-Valence-Dynamics.md (11 occ): 
  Cao hơn typical Tier 5. Verify khi thực hiện — có thể cần Tier 4.
  Body-Base cũng có firing mode refs (Plan F scope).

Tier 5 total: ~24 files, ~65 occ
```

### Tier 6: VERSION REF + DEP-LIST UPDATES

```
Sau khi TẤT CẢ M-labels đã refine:
  - Bond-Architecture v1.0 → v2.0 trong dep-lists (~40+ files)
  - "M1-M4 decline" → "Resonance Decline" trong dep descriptions
  - "4 mechanisms" → "2 Forces + 1 Fuel" trong summaries
  - Confidence markers: "🟡 4-mechanism model" → "🟡 2 Forces + 1 Fuel model"
  
Có thể batch xử lý CUỐI CÙNG hoặc CÀI VÀO mỗi session.
```

---

## §3 — SESSION PLAN

```
  ┌──────┬──────────────────────────────────┬───────┬──────┬──────────────────────┐
  │  #   │ Scope                            │ Files │ ~Occ │ Depends              │
  ├──────┼──────────────────────────────────┼───────┼──────┼──────────────────────┤
  │  S1  │ ★ Boredom REWRITE                │   1   │  50  │ Tier 1 (✅)           │
  │      │ §3+§9+§10+all scattered          │       │      │                      │
  │      │ = Tier 2 DEEPEST                 │       │      │                      │
  ├──────┼──────────────────────────────────┼───────┼──────┼──────────────────────┤
  │  S2  │ ★ Connection §4.5 REWRITE        │   1   │  42  │ Tier 1 (✅)           │
  │      │ + §4.6 refs + all scattered      │       │      │                      │
  ├──────┼──────────────────────────────────┼───────┼──────┼──────────────────────┤
  │  S3  │ Plans L + E                      │  2-3  │ ~85  │ None                 │
  │      │ L: Love-Unified §5 (5 occ)      │       │      │                      │
  │      │ E: RPE §3-§9 (~80 occ, MANUAL)  │       │      │                      │
  ├──────┼──────────────────────────────────┼───────┼──────┼──────────────────────┤
  │  S4  │ Plan F                           │  3-4  │ ~30  │ None                 │
  │      │ Body-Base + Discovery + DMD      │       │      │                      │
  │      │ + cross-ref fixes                │       │      │                      │
  ├──────┼──────────────────────────────────┼───────┼──────┼──────────────────────┤
  │  S5  │ ★ RPE §14 + Love-Unified §6.2   │   2   │ ~55  │ S3 (L+E done)        │
  │      │ Per-entity decline reframe       │       │      │                      │
  ├──────┼──────────────────────────────────┼───────┼──────┼──────────────────────┤
  │  S6  │ ★ Empathy §8.7 + Love-Romantic   │   2   │ ~57  │ Tier 1 (✅)           │
  │      │ §11.8                            │       │      │                      │
  │      │ Per-mechanism → 2 Forces + 1 Fuel            │       │      │                      │
  ├──────┼──────────────────────────────────┼───────┼──────┼──────────────────────┤
  │  S7  │ ★ Body-Coupling §2.3 +           │   2   │ ~52  │ Tier 1 (✅)           │
  │      │ Connection-Education §6.2        │       │      │                      │
  ├──────┼──────────────────────────────────┼───────┼──────┼──────────────────────┤
  │  S8  │ Tier 4 Batch A (9 files)         │   9   │~105  │ S1-S7                │
  │      │ AM, Edu-System, Core-Software,   │       │      │                      │
  │      │ Edu-Arms-Race, Status, Idol,     │       │      │                      │
  │      │ Skill-Intro, Domain-Knowledge,   │       │      │                      │
  │      │ 01-File-Index CDD                │       │      │                      │
  ├──────┼──────────────────────────────────┼───────┼──────┼──────────────────────┤
  │  S9  │ Tier 4 Batch B (9 files)         │   9   │ ~97  │ S1-S7                │
  │      │ Protect, Self-Pattern-Modeling,  │       │      │                      │
  │      │ Natural-Dev, Child-Dev-Mech,     │       │      │                      │
  │      │ Edu-Mechanism, Religion,         │       │      │                      │
  │      │ Melody-Tech-Overview, BPS, IB    │       │      │                      │
  ├──────┼──────────────────────────────────┼───────┼──────┼──────────────────────┤
  │ S10  │ Tier 5 ALL (24 files)            │  24   │ ~65  │ S1-S9                │
  │      │ + Tier 6 version ref sweep       │       │      │                      │
  │      │ + FINAL VERIFY                   │       │      │                      │
  └──────┴──────────────────────────────────┴───────┴──────┴──────────────────────┘

  S1-S2:  Conceptual depth — 1-2 files/session, quality-focused
  S3-S4:  Prerequisites — unlock mixed files
  S5-S7:  Deep propagation — per-mechanism reframe
  S8-S9:  Standard propagation — batch rename+reframe
  S10:    Cleanup + final verify

  ★ = conceptual quality session (slow, careful)
  Est. total: 10 sessions
```

### Session Ordering Rationale

```
  S1 Boredom TRƯỚC vì:
    → Deepest rewrite (50 occ, 10+ sections)
    → Independent (no prerequisite beyond Tier 1)
    → Sets quality bar cho remaining files
    
  S2 Connection TIẾP vì:
    → Second deepest (42 occ, §4.5 is 120 lines)
    → Independent of L/E/F
    
  S3-S4 Prerequisites GIỮA vì:
    → Unlock S5 (RPE + Love-Unified)
    → L is trivial (5 occ), E requires attention (80 occ manual)
    → F is moderate (30 occ) but has cross-ref fixes
    
  S5-S7 Deep propagation SAU prerequisites vì:
    → RPE §14 needs Plan E done first
    → Love-Unified §6.2 needs Plan L done first
    → Empathy, Love-Romantic, Body-Coupling, Conn-Edu independent

  S8-S10 Batch propagation CUỐI vì:
    → Tier 2 conceptual work defines the template
    → Batch work follows established patterns
    → Final verify catches any missed refs
```

---

## §4 — QUALITY PROTOCOL

### Per-Session Protocol

```
  MỖI session follow 5 bước:

  ① READ FULL: Đọc toàn bộ file (hoặc relevant sections).
     Nếu file > 1000L → đọc TOC + relevant sections + cross-refs.

  ② ANALYZE: Map M-label occurrences → classify:
     - Conceptual (needs rewrite to 2 Forces + 1 Fuel model)
     - Reference (M1-M4 → Resonance Decline simple replace)
     - Cross-ref (dep-list, version ref)
     - SKIP (other M-system, Plan L/E/F scope)

  ③ DRAFT: Viết nội dung mới cho conceptual sections.
     Key transforms (Plan-R-v2 §5):
       "4 mechanisms" → "2 decline forces + novelty threshold"
       "M1" → "Compiled-Suppress" (force ①)
       "M2" → "Reward-Habituated" (force ②)
       "M3" + "M4" → absorb vào novelty threshold discussion
       "M1 accelerate M2+M3+M4" → "① accelerate ② + drain novelty"
       "M2+M3+M4" → rewrite per context (② ≠ fuel)
       + Add Gap Drift where appropriate

  ④ IMPLEMENT: Edit file (MANUAL cho Tier 2, batch cho Tier 4-5).

  ⑤ VERIFY: grep "\bM[1-4]\b" = 0 in Resonance Decline context.
     Remaining M-labels = ONLY other systems (L/E/F scope hoặc SKIP).
```

### Quality Checks

```
  ⭐ CONCEPTUAL CONSISTENCY:
    - Force ① (Compiled-Suppress): attacks SOURCE, accelerates ②, drains novelty
    - Force ② (Reward-Habituated): hardware, INDEPENDENT, Weber-Fechner
    - Novelty threshold: FUEL (not force), probabilistic, 2 lenses
    - Gap Drift: CONTEXTUAL, direction ≠ novelty, proximity paradox
    - ① accelerate ② + drain novelty (NOT "① accelerate ②+③")
    - Satiation: ① attacks Tonic+Generative, ② = Tonic declining, Novelty = Generative

  ⭐ KHÔNG để:
    - M3 hoặc M4 as SEPARATE concepts (phải merge vào novelty)
    - "M2+M3+M4" grouped (② is force, M3+M4 is fuel — KHÁC category)
    - ①②③ labels trong text (dùng tên descriptive)
    - Abbreviations (KHÔNG viết tắt concept names)

  ⭐ PHẢI GIỮ:
    - Research citations (move dưới correct concept, KHÔNG xóa)
    - Per-entity analysis (reframe to 2 Forces + 1 Fuel, KHÔNG bỏ per-entity insight)
    - Confidence markers (update accuracy, KHÔNG xóa)
    - Cross-refs (update version, KHÔNG xóa)
```

---

## §5 — DEPENDENCIES

```
                    ┌──────────┐
                    │ Tier 1   │ ✅ DONE
                    │ BA+RS+   │
                    │ BPGR     │
                    └────┬─────┘
                         │
            ┌────────────┼────────────┐
            ▼            ▼            ▼
      ┌──────────┐ ┌──────────┐ ┌──────────┐
      │ S1       │ │ S2       │ │ S3 L+E   │
      │ Boredom  │ │ Connect  │ │ S4 F     │
      └────┬─────┘ └────┬─────┘ └────┬─────┘
           │            │            │
           │            │      ┌─────┴─────┐
           │            │      ▼           ▼
           │            │ ┌──────────┐ ┌──────────┐
           │            │ │ S5       │ │ S6-S7    │
           │            │ │ RPE+LU   │ │ Emp+LR   │
           │            │ │          │ │ BC+CE    │
           │            │ └────┬─────┘ └────┬─────┘
           │            │      │            │
           ▼            ▼      ▼            ▼
      ┌────────────────────────────────────────┐
      │           S8-S9 Tier 4 Batch           │
      └────────────────┬───────────────────────┘
                       ▼
              ┌──────────────────┐
              │ S10 Tier 5+6     │
              │ Cleanup + Verify │
              └──────────────────┘


  S1, S2: PARALLEL OK (independent files)
  S3, S4: PARALLEL OK with S1/S2
  S5: AFTER S3 (needs Plan L+E done)
  S6, S7: PARALLEL OK after Tier 1
  S8-S9: AFTER S1-S7 (template established)
  S10: LAST (final sweep)
```

---

## §6 — EDGE CASES + SAFETY

```
  ① FILES MIXED (>1 M-system):
    Love-Unified: §5 = Plan L, §6.2 = Plan R → L before R
    RPE: §3-§9 = Plan E, §14 = Plan R → E before R
    Body-Base: §5.3 = Plan F, others = Plan R → F before R
    Discovery/DMD: firing = Plan F, decline refs = Plan R → F before R
    
  ② "M2+M3+M4" REWRITE RULES:
    Context "M2+M3+M4 independent":
      → "Reward-Habituated (force) + novelty exhaustion (fuel) — independent of each other but compound"
    Context "M1 accelerate M2+M3+M4":
      → "Compiled-Suppress accelerate Reward-Habituated + drain novelty fuel"
    Context "counter M2+M3+M4":
      → "counter Reward-Habituated (②) + restore novelty fuel"
    Context "M2+M3 HIGH" (per-entity):
      → rewrite: "Reward-Habituated + novelty below threshold"
    
  ③ PER-ENTITY ANALYSIS REFRAME:
    Old: "M1 YES, M2 SLOW, M3 COUNTERED, M4 COUNTERED"
    New: "Compiled-Suppress: [yes/no]. Reward-Habituated: [rate]. Novelty: [above/below threshold]."
    Keep per-entity specifics, change framework labels.
    
  ④ BACKUP POLICY:
    Tier 1 files: backup/ done (BA v1.0 backed up)
    Tier 2+ files: NO backup needed (changes are label updates, not structural rewrite)
    Exception: if §section is FULLY REWRITTEN → backup section text in plan notes
    
  ⑤ FILES SKIP (UNCHANGED — same as plan-m1-m4-rename.md §3.3):
    - PFC Damage M1-M2 (Drill-Body-Feedback 01-04)
    - Micro Examples M1-M5 (convention code)
    - Motor Arc V/A/M/B/I (modality code)
    - Quote-Analysis M1-M4 (local enumeration)
    - ALL backup/ and _backup/ files
    - ALL plan files (Plan-R-v2, Plan-L, Plan-E, Plan-F, plan-m1-m4-rename)
    
  ⑥ ESCALATION:
    If a Tier 4 file turns out to have per-mechanism sections → treat as Tier 2.
    Files marked VERIFY: Education-Mechanism, Education-Arms-Race, 
    Domain-Knowledge-Map, Religion, Body-Base, Entity-Valence-Dynamics.
```

---

## §7 — FINAL VERIFY

```
  Sau TẤT CẢ sessions (S1-S10):

  1. grep "\bM[1-4]\b" toàn Human-Predictive-Drive (exclude backup/_backup)
     → Remaining = CHỈ CÒN files SKIP (§6⑤)

  2. grep "Bond-Architecture.*v1\.0" (exclude backup/_backup/plan)
     → 0 (tất cả đã update v2.0)

  3. CONCEPTUAL SPOT-CHECK:
     - Bond-Architecture §4 = source → 2 Forces + 1 Fuel + Gap Drift ✅
     - Boredom §3 = consistent ✅
     - Connection §4.5 = consistent ✅
     - RPE §14 = per-entity reframed ✅
     - 5 random Tier 4 files = labels correct ✅

  4. CROSS-REF INTEGRITY:
     - Mọi file trỏ Bond-Architecture → v2.0
     - "M1-M4" in dep descriptions → "Resonance Decline"
     - No orphaned "4 mechanisms" references
```

---

## §8 — STATUS TRACKER

```
  ┌──────┬──────────────────────────────┬────────┬─────────────┐
  │  #   │ Scope                        │ Status │ Date        │
  ├──────┼──────────────────────────────┼────────┼─────────────┤
  │ Tier1│ BA + RS + BPGR              │   ✅   │ 2026-05-29  │
  │  S1  │ Boredom                     │   ✅   │ 2026-05-29  │
  │  S2  │ Connection                  │   ✅   │ 2026-05-29  │
  │  S3  │ Plan L + Plan E            │   ✅   │ 2026-05-29  │
  │  S4  │ Plan F                     │   ✅   │ 2026-05-29  │
  │  S5  │ RPE §14 + Love-Unified §6.2│   ✅   │ 2026-05-29  │
  │  S6  │ Empathy + Love-Romantic    │   ✅   │ 2026-05-29  │
  │  S7  │ Body-Coupling + Conn-Edu   │   ✅   │ 2026-05-29  │
  │  S8  │ Tier 4 Batch A             │   ✅   │ 2026-05-29  │
  │  S9  │ Tier 4 Batch B             │   ✅   │ 2026-05-29  │
  │ S10  │ Tier 5 + 6 + Final Verify  │   ✅   │ 2026-05-29  │
  └──────┴──────────────────────────────┴────────┴─────────────┘
```
