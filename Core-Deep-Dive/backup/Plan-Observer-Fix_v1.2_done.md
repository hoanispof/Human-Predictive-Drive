---
title: "Plan — Fix 'Observer' Bias Across Framework"
version: 1.2
created: 2026-07-01
updated: 2026-07-02 (v1.2 — DONE. X1-X4 complete. ~885 fixes / ~148 files. Final verification: 0 non-KEEP remaining.)
status: DONE ✅
purpose: |
  "Observer" đã bị dùng lạm phát trong framework, tạo bias ngôn ngữ:
    - PFC role: "PFC = Observer" (SAI — PFC receives/gates, không observe)
    - Consciousness: "the observer CAN access" (SAI — không có entity nào observe)
    - Disambiguation blocks: giải quyết collision giả giữa "observation parameter"
      và "consciousness observer" (THỪA — 2 khái niệm này hoàn toàn không liên quan)
  
  Root cause: framework cũ (v7.5→v8.0) dùng "observer" cho PFC role.
  Khi viết Consciousness.md, "observer" lan sang consciousness definitions.
  Khi phát hiện collision với "observation parameter" → viết disambiguation.
  Disambiguation giải quyết vấn đề do chính framework tạo ra, không phải vấn đề thực.
  
  Fix: xoá "observer" khỏi mechanism/definition contexts.
  Giữ "observation" trong "observation parameter" (tên đúng — methodology label).
  Giữ "Self-Observation" (APPLICATION-3 — ý nghĩa khác, legitimate).
scope: |
  TIER 1 — CORE (Consciousness.md + Core-Software.md): 35+ instances
  TIER 2 — PFC FILES (9 files in PFC/): 75 instances  
  TIER 3 — OTHER FRAMEWORK FILES: ~500+ instances (REVISED — see §3.1)
  TIER 4 — DRILL FILES (30+ files): ~264 instances (REVISED — see §3.1)
  TIER 5 — OLD DRILL FILES (2 files in Drill-Consciousness/backup/): 9 instances
  TOTAL: ~730+ instances across ~117 files (REVISED from ~350/~57)
  ROOT CAUSE: Feeling.md "PFC observation → reception" cascade (see §3.1)
confidence: 🟢 Research support | 🟡 Framework synthesis | 🔴 Hypothesis
---

# Plan — Fix "Observer" Bias Across Framework

> **Không có observer nào trong não bộ cả.**
> **Không có vùng não nào đi quan sát vùng khác.**
> **Toàn bộ là pattern firing + synchronization.**
>
> **"Observer" chỉ là phenomenal description —**
> **cách con người MÔ TẢ trải nghiệm "knowing" từ bên trong.**
> **Nó không phải mechanism, không phải entity, không phải component.**
>
> **"Observation parameter" = tên đúng, giữ nguyên.**
> **"Self-Observation" = APPLICATION-3, giữ nguyên.**
> **"PFC = Observer" = SAI → fix.**
> **"the observer CAN access" = SAI → fix.**

---

## §0 — VẤN ĐỀ

```
⭐ "OBSERVER" XUẤT HIỆN Ở 3 CONTEXT KHÁC NHAU:

  ① PFC ROLE NAME: "PFC = Observer + Orchestrator"
     → 113 lần across 28 files
     → SAI: PFC không "observe" — PFC receives pre-processed signals,
       gates (TRN), holds (WM), biases (top-down), suppresses
     → Evidence: damage PFC → mất gating, KHÔNG mất perception
     → PFC thiếu direct sensory input — nhận signal ĐÃ qua cortex processing

  ② CONSCIOUSNESS DEFINITION: "the observer CAN access"
     → 63 lần across 11 files
     → SAI: không có entity nào "observe" processing
     → Consciousness = pattern firing + thalamo-cortical synchronization
       → khi synchronize đủ → broadcast → "known"
     → "Observer" = phenomenal description (cách mô tả từ bên trong)

  ③ DISAMBIGUATION BLOCKS: "observation ≠ observer"
     → ~130 lines in Consciousness.md + ~46 lines in Core-Software.md
     → THỪA: "observation parameter" và "consciousness" hoàn toàn không liên quan
     → Disambiguation giải quyết collision do framework TỰ TẠO RA
     → Khi fix ① và ② → collision biến mất → disambiguation thừa


⭐ "OBSERVATION" GIỮA NGUYÊN Ở 2 CONTEXT:

  ④ OBSERVATION PARAMETER: "Novelty, Threat, Status..."
     → Tên đúng: pattern identified through observation methodology
     → Không liên quan consciousness — khác meta-level hoàn toàn
     → KHÔNG CẦN đổi tên, KHÔNG CẦN disambiguation

  ⑤ SELF-OBSERVATION: APPLICATION-3
     → Ý nghĩa khác: PFC application tự direct attention vào self
     → Legitimate terminology — everyday meaning "examine, pay attention"
     → KHÔNG liên quan "observer" bias
```

---

## §1 — REPLACEMENT RULES

```
⭐ RULE 1 — PFC ROLE (context ①):

  OLD: "PFC = Observer + Orchestrator"
  NEW: "PFC = Orchestrator"
  → Drop "Observer" entirely. "Orchestrator" already covers all PFC functions.
  → Analogy: nhạc trưởng — dàn nhạc vẫn chơi được khi không có nhạc trưởng
    (consciousness exists without PFC: dreaming, hydranencephaly),
    nhưng có nhạc trưởng thì phối hợp tốt hơn (PFC upgrades L1→L2→L3).
    Nhạc trưởng không tạo ra âm nhạc (content = posterior cortex).

  OLD: "PFC = Observer, NOT Controller"
  NEW: "PFC = Orchestrator, NOT Controller"

  OLD: "PFC observes..."
  NEW: "PFC receives..." / "PFC orchestrates..." / "PFC processes..."

  OLD: "PFC (Observer + Orchestrator)" in headers
  NEW: "PFC (Orchestrator)" — single role name, simpler


⭐ RULE 2 — CONSCIOUSNESS DEFINITION (context ②):

  OLD: "the observer CAN access"
  NEW: "the brain can self-access" / "processing is known"

  OLD: "accessible to the observer"
  NEW: "self-accessible" / "known"

  OLD: "the observer can:"
  NEW: "'Known' means the brain can:"

  OLD: "the observer KNOWS"
  NEW: "processing is KNOWN" / "patterns are KNOWN"

  OLD: "from the observer's perspective"
  NEW: "from experiential perspective"

  PRINCIPLE: chuyển từ ENTITY language (ai đó observe)
    → STATE language (processing ở trạng thái known)


⭐ RULE 3 — DISAMBIGUATION BLOCKS (context ③):

  ACTION: REMOVE entirely
  
  In Consciousness.md:
    → Header lines 73-78: REMOVE obs params comparison + warning
    → §0 lines 171-174: REMOVE obs params meta-level
    → §1.4 lines 335-342: REMOVE obs params comparison
    → §1.5 lines 359-363: REMOVE obs params from Property ①
    → §1.5 lines 386-391: REMOVE "RELATIONSHIP TO OBS PARAMS"
    → §1.5 lines 397-439: REMOVE "DISAMBIGUATION: 2 MEANINGS"
    → §10 lines 1841-1846: SIMPLIFY to standard cross-ref only
    → Total: ~80 lines removed

  In Core-Software.md:
    → §0.3 line 125: "not an observation parameter" → remove phrase
    → §8.1 line 1415: REMOVE obs params = LABELS line
    → §8.2 lines 1448-1494: REMOVE entire section (~46 lines)
    → §12 Reframe #26 lines 1819-1825: simplify, remove disambiguation
    → Total: ~55 lines removed


⭐ RULE 4 — KEEP AS-IS (contexts ④ ⑤):

  "observation parameter" → KEEP (tên đúng)
  "Self-Observation" → KEEP (APPLICATION-3, ý nghĩa khác)
  "observer" as phenomenal language → KEEP nếu rõ context
    Example OK: "it feels as though there is an observer"
    Example OK: "the experience of knowing, phenomenally described as 'observing'"
```

---

## §2 — SCOPE BY TIER

```
════════════════════════════════════════════════════
TIER 1 — CORE FILES (execute with Consciousness.md v1.5)
════════════════════════════════════════════════════

  File: Consciousness.md v1.4 → v1.5
  Instances: ~20 "observer" + ~80 lines obs params removal
  Integrated with: Grand-Synthesis E1 + E2 (items T1, T3, T4)
  
  File: Core-Software.md v3.4 → v3.5
  Instances: ~13 "observer" + ~55 lines obs params removal
  Integrated with: Grand-Synthesis E3 (items T-CS1, T-CS2, T-CS3)


════════════════════════════════════════════════════
TIER 2 — PFC FILES (execute after Tier 1, or standalone)
════════════════════════════════════════════════════

  ┌──────────────────────────────────┬──────────┐
  │ File                             │ Instances│
  ├──────────────────────────────────┼──────────┤
  │ PFC/Logic-Feeling.md             │ 28       │
  │ PFC/PFC-Label.md                 │ 16       │
  │ PFC/Logic-Feeling-Balance.md     │ 14       │
  │ PFC/Self-Observation.md          │ 5 *      │
  │ PFC/Logic-Planning.md            │ 5        │
  │ PFC/PFC-Operations.md            │ 4        │
  │ PFC/Simulation-Engine.md         │ 1        │
  │ PFC/Logic-Feeling-Failure-Ex.md  │ 1        │
  │ PFC/Imagination/Imagine-Final.md │ 1        │
  ├──────────────────────────────────┼──────────┤
  │ TOTAL                            │ 75       │
  └──────────────────────────────────┴──────────┘
  
  * Self-Observation.md: "observer" references cần review —
    some may be legitimate (APPLICATION-3 context)


════════════════════════════════════════════════════
TIER 3 — OTHER FILES (gradual fix, lowest priority)
════════════════════════════════════════════════════

  ┌──────────────────────────────────┬──────────┐
  │ File                             │ Instances│
  ├──────────────────────────────────┼──────────┤
  │ Core-Hardware.md                 │ 5        │
  │ Body-Base/Feeling/Drill-*        │ ~18      │
  │ Body-Base/Chunk/Drill-*          │ ~5       │
  │ docs/_posts/ (blog)              │ ~10      │
  │ Ask-AI.md                        │ 2        │
  │ Body-Base/Body-Base.md           │ 2        │
  │ Body-Base/Schema/Schema.md       │ 1        │
  │ Neural-Processing-Flow.md        │ 1        │
  │ Consciousness-Accessibility.md   │ 2        │
  │ 01-File-Index.md                 │ 3        │
  │ README.md                        │ 1        │
  │ Reading-Roadmap.md               │ 1        │
  │ Other misc files                 │ ~5       │
  ├──────────────────────────────────┼──────────┤
  │ TOTAL                            │ ~56      │
  └──────────────────────────────────┴──────────┘
  
════════════════════════════════════════════════════
TIER 4 — DRILL & PLAN FILES (fix bias ngay cả trong analysis records)
════════════════════════════════════════════════════

  ┌───────────────────────────────────────────────────┬──────────┐
  │ File                                              │ Instances│
  ├───────────────────────────────────────────────────┼──────────┤
  │ Drill-Consciousness-Terminology-Analysis.md       │ 104 *    │
  │ Grand-Synthesis-Execution-Plan.md                 │ 53       │
  │ Plan-Foundation-Clarification.md                  │ 13       │
  │ Drill-CE-Split-Brain.md                           │ 3        │
  │ Drill-Thalamo-Cortical-Mechanism.md               │ 1        │
  │ Drill-CE-Dreaming.md                              │ 1        │
  ├───────────────────────────────────────────────────┼──────────┤
  │ TOTAL                                             │ ~175     │
  └───────────────────────────────────────────────────┴──────────┘
  
  * Drill-Consciousness-Terminology-Analysis.md: 104 instances vì file này
    PHÂN TÍCH chính vấn đề observer. Nhiều chỗ là context mô tả vấn đề
    (OLD → NEW). Cần review case-by-case: giữ trong context "đây là cái cũ"
    nhưng fix trong context recommendation/conclusion.

  RATIONALE: Drill files tuy là historical records, nhưng nếu giữ bias
  trong đó thì reader đọc lại sẽ bị ảnh hưởng. Fix toàn bộ để
  tránh tối đa bias lan truyền.

════════════════════════════════════════════════════
TIER 5 — OLD DRILL FILES (Drill-Consciousness/backup/)
════════════════════════════════════════════════════

  ┌───────────────────────────────────────────────────┬──────────┐
  │ File                                              │ Instances│
  ├───────────────────────────────────────────────────┼──────────┤
  │ Drill-Consciousness-Knowing.md                    │ 7        │
  │ Drill-Consciousness-Compiled-Fresh.md             │ 2        │
  ├───────────────────────────────────────────────────┼──────────┤
  │ TOTAL                                             │ 9        │
  └───────────────────────────────────────────────────┴──────────┘
  
  3 files CLEAN (0 instances):
    → Drill-Consciousness-Architecture.md ✅
    → Drill-Consciousness-Bridge.md ✅
    → Drill-VTA-Dopamine-Consciousness.md ✅

  FILES EXCLUDED:
    → Plan-Observer-Fix.md (this plan — uses "observer" to describe the problem)


════════════════════════════════════════════════════
VI/ FILES — translation sync (separate scope)
════════════════════════════════════════════════════

  N/A — VI/ moved to _backup/, no longer active.
```

---

## §3 — EXECUTION ORDER

```
⭐ CHOSEN: STANDALONE OBSERVER FIX FIRST (Option B)
  
  Rationale: "đảm bảo chất lượng nền tảng đã" — dọn sạch bias trước,
  viết nội dung mới trên nền đã fix. Tránh tối đa bias lan truyền.


  Session X1: TIER 1 — Consciousness.md + Core-Software.md
    → Rules 1+2+3 applied to both files
    → Consciousness.md: ~20 observer edits + ~80 lines obs params removal
    → Core-Software.md: ~13 observer edits + ~55 lines obs params removal
    → Version bump: v1.4.1 + v3.4.1 (terminology fix, not content rewrite)

  Session X2: TIER 2 — PFC files (9 files)
    → Rule 1 applied: "Observer" → "Orchestrator" throughout
    → ~75 edits across 9 files
    → Largest: Logic-Feeling.md (28), PFC-Label.md (16), Logic-Feeling-Balance.md (14)

  Session X3: TIER 3 — Framework files (REVISED SCOPE)
    → Rules 1+2 applied
    → ORIGINAL ESTIMATE: ~56 edits / ~20 files
    → ACTUAL: ~500+ edits / ~85+ files (see §3.1 for root cause)
    → Split into Phases A-H due to scope

  Session X4: TIER 4 + TIER 5 — Drill, plan, & old drill files
    → ORIGINAL ESTIMATE: ~175 edits / 8 files
    → ACTUAL: ~260+ edits / 30+ files (many Drill-Feeling, Drill-Chunk)
    → Feel-Example-Draft.md alone = 80 instances
    → Grand-Synthesis-Execution-Plan.md: update to reflect completed observer fix

  Session X5: VERIFY
    → Grep verification across entire framework
    → Read key sections for coherence
    → Update Grand-Synthesis-Execution-Plan.md:
      T1, T3, T4, T-CS1, T-CS2, T-CS3 = ALREADY DONE
      → Execution plan items reduce significantly

  THEN: Grand Synthesis E1-E5 continues on clean base
    → Content-only changes (M1-M4, S1-S10, C1-C8)
    → No more terminology fixes needed

  AFTER: VI/ translation sync


⭐ §3.1 — SCOPE REVISION NOTE (added 2026-07-01)

  ROOT CAUSE of underestimate:
    ① Plan counted "observer" (PFC role + consciousness entity) only
    ② Feeling.md definition change "PFC observation → PFC reception"
       created CASCADE of ~300+ cross-ref updates not anticipated:
       - "PFC observation interface" → "PFC reception interface"
       - "PFC observation of body-chunk interaction" → "PFC reception of..."
       - "PFC observation threshold" → "PFC reception threshold"
       - "PFC observes [X]" → "PFC receives [X]"
    ③ Research/, Applications/, Observation/ folders not scanned in original plan
    ④ Drill folders beyond Drill-Consciousness/ not scanned

  REVISED TOTAL:
    Original: ~350 instances / ~57 files
    Actual:   ~885 instances / ~148 files (DONE)

  ADDITIONAL RULE (decided during X3):
    Rule 1 addendum: "PFC-observable" → "PFC-accessible"
      (not "PFC-receivable" — chosen for naturalness)
```

---

## §3.2 — EXECUTION TRACKING

```
⭐ X1: TIER 1 — COMPLETE ✅ (2026-07-01)
  Consciousness.md v1.4 → v1.4.1: ~16 observer fixes + ~80 lines disambiguation removed
  Core-Software.md v3.4 → v3.4.1: ~23 observer fixes + §8.2 removed (~47 lines)

⭐ X2: TIER 2 — COMPLETE ✅ (2026-07-01)
  10 PFC files: ~60 edits total
  PFC-Label, PFC-Function, PFC-Configuration, Self-Observation,
  Simulation-Engine, Logic-Feeling-Balance, Logic-Feeling,
  Logic-Feeling-Failure-Examples, Imagine-Final, PFC-Operations

⭐ X3: TIER 3+4 — COMPLETE ✅ (2026-07-01 → 2026-07-02)
  Phase A (3 files, 22 fixes): Core-Hardware, Neural-Processing-Flow, Consciousness-Accessibility ✅
  Phase B (3 files, ~62 fixes): Feeling.md (core definition change!), Body-Feedback-Label, Body-Feedback-Mechanism ✅
  Phase C (4 files, 39 fixes): Body-Base, Valence-Propagation, Why-Body-Knows, Body-Coupling ✅
  Phase D (7 files, 39 fixes): Chunk/, Agent-Mechanism/, Background-Pattern ✅
  Phase E (16 files, 65 fixes): Self-Pattern-Modeling, Schema, Personal-Melody, etc. ✅
  Phase F (26 files, ~100 fixes): Neural-Architecture, Entity-Valence, Observation/, etc. ✅
  Phase G (21 files, ~57 fixes): Research/ + Applications/ ✅
  Phase H1 (1 file, ~95 fixes): Feel-Example-Draft ✅
  Phase H2 (7 files, ~137 fixes): Drill-Feeling-Knowning/ ✅
  Phase H3 (~30 files, ~142 fixes): Drill-Body-Feedback/, Drill-Chunk/, Drill-Consciousness/,
    Feel-Development, + earlier-phase cleanup (~20 misses across 11 files) ✅

  TOTAL X3: ~118 files, ~758 fixes

⭐ X4: VERIFY — COMPLETE ✅ (2026-07-02)
  8 verification grep sweeps across entire framework:
    ① PFC.*observ broad → 267 matches → ALL classified KEEP
    ② Targeted (PFC = Observer, PFC observes, PFC observation interface/threshold) → 0 non-KEEP
    ③ Category refs (OBSERVE.*HOLD) → 0 stale
    ④ Rule 2 patterns (the observer CAN/KNOWS/sees/accesses) → ALL KEEP
    ⑤ observation threshold/interface without PFC prefix → 6 MISSES FOUND → FIXED
    ⑥ PFC observing, observing body-chunk → 0 non-KEEP
    ⑦ Applications/, docs/, Observation/ → 0 non-KEEP
    ⑧ 7-layer observ, observation model, observational → ALL KEEP (general English)
  
  X4 fixes: 18 files, 28 fixes
    - Consciousness.md stale cross-refs (2)
    - PFC-Function.md §1 OBSERVE→RECEIVE rename (3) + cross-ref cascade (7)
    - 01-File-Index.md stale PFC-Label description (1)
    - Research/ PFC verb fixes: OCD, Autism, Love-Romantic, Parkinson, Alzheimer,
      Work-Adversity, ADHD-Attention-Optimization (7)
    - observation threshold/interface without PFC prefix: Body-Knowing,
      Feeling-Mechanism-Deep-Draft, 01-Theme-A-Architecture,
      Feel-Example-Draft, Feeling-Literacy-Training-Draft,
      Feeling-Chunk-Bridge-Draft (6)
    - 01-File-Index.md PFC-Label description update (1)
    - Religion.md PFC-Function category refs (2)

  RESULT: 0 non-KEEP "observ*" instances remaining across entire framework.

  REMAINING "observ*" matches — ALL legitimate KEEP:
    Self-Observation APPLICATION-3 (~80), Feel-Observation layer name (~30),
    Observer labels concept (~20), Observation parameters (~20),
    Plan/meta/analysis docs (~80), General English (~50), External observer (~10)

════════════════════════════════════════════════════
GRAND TOTAL
════════════════════════════════════════════════════

  │ Phase          │ Files │ Fixes │
  ├────────────────┼───────┼───────┤
  │ X1 TIER 1      │   2   │  ~39  │
  │ X2 TIER 2      │  10   │  ~60  │
  │ X3 TIER 3+4    │ ~118  │ ~758  │
  │ X4 VERIFY      │  18   │   28  │
  ├────────────────┼───────┼───────┤
  │ TOTAL          │ ~148  │ ~885  │

  VI/ FILES: N/A — VI/ moved to _backup/, no longer active.
```

---

## §4 — GRAND SYNTHESIS UPDATES NEEDED

```
⭐ 5 ITEMS CẦN CẬP NHẬT TRONG GRAND-SYNTHESIS-EXECUTION-PLAN.md:

  1. T3-expanded scope:
     OLD: "Remove obs params contamination + brief note §10"
     NEW: "Remove ALL obs params mentions. No note needed."

  2. T4 scope:
     OLD: "Thu gọn §1.5 + add 'See Core-Software.md §8.2'"
     NEW: "Thu gọn §1.5 + NO pointer (§8.2 removed entirely)"

  3. T-CS2 scope:
     OLD: "Thu gọn §8.2 from ~40 → ~15 lines"
     NEW: "REMOVE §8.2 entirely (nothing to disambiguate)"

  4. §0.3 Design Principle 8:
     OLD: "not a cycle component, not an observation parameter"
     NEW: "not a cycle component" (sufficient)

  5. Reframe #26:
     OLD: "repositioned + disambiguation"
     NEW: "repositioned from footnote to dedicated §8" (no disambiguation)

  6. NEW — TIER 2 scope for E4:
     ADD: PFC files observer fix (75 instances, 9 files)
     E4 grows from "~15-25 lines" to "~75 edits across 9 files + 15-25 lines"
```

---

## §5 — VERIFICATION

```
  GREP CHECKS (after each tier):

  TIER 1:
    grep "observer" Consciousness.md → 0 non-phenomenal uses
    grep "observer" Core-Software.md §6+§8 → 0 non-phenomenal uses
    grep "observation parameter" Consciousness.md §0-§8 → 0
    grep "disambiguation" Consciousness.md → 0
    grep "disambiguation" Core-Software.md → 0

  TIER 2:
    grep "PFC = Observer" PFC/ → 0
    grep "PFC.*observer" PFC/ → 0 non-phenomenal
    
  TIER 3:
    grep "PFC.*observer" across framework → 0 non-phenomenal
    grep "the observer" across framework → 0 non-phenomenal

  COHERENCE:
    Read Consciousness.md §0 → §1.1 → no "observer" in definitions
    Read Core-Software.md §6 → "Orchestrator" not "Observer"
    Read Core-Software.md §8 → no §8.2, clean §8.0+§8.1 only
    Read PFC-Label.md §2 → role label updated
```

---

## §6 — BIAS CHECK

```
  □ OVER-CORRECTION: removing "observer" from phenomenal contexts
    → "It feels like observing" = OK (describing experience, not mechanism)
    → Only remove from DEFINITIONS and MECHANISM descriptions
    
  □ CASCADE ANXIETY: 350+ instances feels overwhelming
    → TIER system prevents scope creep
    → TIER 1 (core files) = most impact, smallest scope
    → TIER 3 = gradual, no rush

  □ NAME SIMPLIFICATION: "Orchestrator" thay "Observer + Orchestrator"
    → Drop "Observer" entirely — "Orchestrator" already covers all PFC functions
    → Analogy: nhạc trưởng (dàn nhạc chơi được khi không có, nhưng hay hơn khi có)
    → PFC không tạo content (posterior cortex does) — nhạc trưởng không tạo âm nhạc
    → "Observer" = metaphor sai (PFC không observe gì cả)

  □ SELF-OBSERVATION confusion: fix "observer" → break Self-Observation?
    → Self-Observation = APPLICATION-3 (PFC directs attention to self)
    → "Observation" ở đây = everyday meaning "examine, pay attention"
    → DIFFERENT from "observer" as consciousness entity
    → KEEP Self-Observation name — no conflict after fix
```

---

## CROSS-REFERENCES

```
  Source analysis:
    → Drill-Consciousness/Drill-Consciousness-Terminology-Analysis.md v2.1
      Finding 1 (F1): PFC ≠ Observer → Biased Orchestrator
      Finding 3 (F3): "Observer" = phenomenal description only
    → Drill-Consciousness/Grand-Synthesis-Execution-Plan.md v1.0
      Items T1, T3, T4, T-CS1, T-CS2, T-CS3

  Target files:
    → Consciousness.md v1.4 (TIER 1)
    → Core-Software.md v3.4 (TIER 1)
    → PFC/ folder: 9 files (TIER 2)
    → ~20 other files (TIER 3)

  Related plans:
    → Grand-Synthesis-Execution-Plan.md v1.0 (needs §4 updates)
    → Plan-Foundation-Clarification.md (master plan)
```

---

> **Plan-Observer-Fix.md v1.2 — DONE ✅**
> **Problem: "observer" + "PFC observation" dùng lạm phát → bias ngôn ngữ.**
> **Fix: 4 replacement rules + Feeling.md "PFC observation→reception" cascade.**
> **Final: ~885 fixes across ~148 files (original estimate: ~350/~57).**
> **Verification: 8 grep sweeps → 0 non-KEEP instances remaining.**
> **Next: Grand Synthesis E1-E5 on clean base (separate plan).**
