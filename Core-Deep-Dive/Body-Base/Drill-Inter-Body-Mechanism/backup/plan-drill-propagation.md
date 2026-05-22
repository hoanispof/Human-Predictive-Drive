# Plan: Drill Propagation — 4 File Mới/Rewrite + Framework Integration

> **Mục tiêu**: Propagate 87 insights từ 4 drill files vào framework.
> **4 file chính**: Entity-Compiled.md + PFC-Operations.md + Self-Pattern-Modeling.md (rename) + Imagine-Final.md (rewrite)
> **Nguyên tắc**: Chậm mà chắc. Distill, KHÔNG copy-paste. Chất lượng > tốc độ.
> **Cập nhật**: 2026-05-19 v2 — thêm Imagine-Final rewrite, clone hypothesis, framework scan results.

---

## TỔNG QUAN KIẾN TRÚC SAU PROPAGATION

```
Agent-Mechanism/ (integration hub + 4 mechanism files)
  ├── Agent-Mechanism.md         (hub — v2.0 → v2.1)
  ├── Self-Pattern-Modeling.md   (RENAMED + v3.1: drill insights)
  ├── By-Product-Gap-Resonance.md (v1.0 → v1.1)
  └── Entity-Compiled.md        ★ NEW (distilled from Drill-Entity-Compiled v2.0)

PFC/ (processing mechanism files)
  ├── PFC-Operations.md          ★ NEW (distilled from Drill-Compiled-Fresh v2.0)
  ├── Logic-Feeling.md           (v2.1 → add cross-ref)
  └── Imagination/
      └── Imagine-Final.md       ★ REWRITE (stale DRAFT → v2.0)

Drill-Inter-Body-Mechanism/ (DRILL files — remain as detailed references)
  ├── Drill-Compiled-Fresh-Mechanics.md v2.0 (1,265L)
  ├── Drill-Entity-Compiled.md v2.0 (1,340L)
  ├── Drill-SPM-Mechanism-Analysis.md v2.1 (1,752L)
  ├── Drill-PR-Definition.md v1.0 (591L)
  └── Inter-Body-Mechanism.md v1.0
```

---

## FRAMEWORK SCAN RESULTS (2026-05-19)

### Tình trạng hiện tại:
```
✅ Hầu hết files đã updated 2026-05-16~19. Terminology đồng nhất.
✅ Không có file nào CONFLICT với 3 file mới planned.
✅ Không cần refine file nào TRƯỚC khi tạo file mới.

⚠️ PHÁT HIỆN QUAN TRỌNG:
  1. Imagine-Final.md = STALE DRAFT (2026-04-18, không version header)
     → Cần REWRITE, không chỉ cross-ref
  2. "Over-clone" = ZERO occurrences toàn framework → concept hoàn toàn MỚI
  3. By-Product-Gap-Resonance đã có "5 TRỤC" — drill nói "4 conditions"
     → 2 framing BỔ SUNG, không conflict (trục = continuous, conditions = binary)
  4. "Clone within window" cần drill sâu hơn → có thể là compiled suppress
     chứ không phải clone thật (xem OPEN QUESTION bên dưới)
```

---

## ✅ RESOLVED: "OVER-CLONE" = OBSERVATION LABEL. MECHANISM = COMPILED SUPPRESS.
> **Resolved 2026-05-20. Xem Drill-Over-SPM-Clarification.md (REFERENCE file).**

```
⭐ GIẢ THIẾT CẦN DRILL THÊM (chưa chốt):

  OBSERVATION (6 research lines confirm):
    Hiểu nhau quá mức + không còn novelty → passion decline
    "Closeness WITHOUT otherness" → desire declines (Muise & Goss 2024)

  DRILL BAN ĐẦU GỌI: "Over-clone kills resonance"
    → Clone quá sâu → own patterns REPLACED → resonance dies

  GIẢ THIẾT MỚI (có thể chính xác hơn):
    → 2 body KHÔNG THỂ có gap giống hệt (khác hardware, khác Background-Pattern)
    → SPM clone (behavioral mimic, state convergence) VẪN xảy ra = F1 output bình thường
    → Nhưng cái "giết" resonance có thể KHÔNG phải clone thật
    → Mà là COMPILED SUPPRESS gap riêng trong relationship context:
      ① Schema "phải giống nhau" → suppress gap differences
      ② Sợ "theo gap riêng → mất nhau" → suppress growth
      ③ Gap riêng bị buried (Outcome B from PFC-Operations)
      ④ Body-base vẫn có gap → khó chịu + xung đột
      ⑤ PFC label = "chán" → nhưng PFC KHÔNG observe suppressed gap
      ⑥ = Gap bị compiled suppress, PFC invisible (Background-Pattern §5)

  REFRAME PATTERN (tương tự framework đã làm):
    "Logic / Feeling"   = observation labels → Compiled/Fresh = mechanism
    "Over-clone"         = observation label  → Compiled suppress = mechanism?

  STATUS: GIẢ THIẾT — cần drill riêng. 6 research lines vẫn valid (confirm
  HIỆN TƯỢNG). Chỉ CƠ CHẾ cần refine.

  KHI VIẾT Self-Pattern-Modeling §3b:
    → Giữ "clone spectrum" (predict→mimic→adopt→converge) = F1 output, confirmed
    → "Over-clone kills resonance": present as OBSERVATION + flag cơ chế mở
    → Reference compiled suppress (PFC-Operations §4) as alternative mechanism
    → KHÔNG chốt 1 cơ chế duy nhất — flag cho drill sau
```

---

## THỨ TỰ PHASES + DEPENDENCIES

```
Phase 1 (Entity-Compiled.md)    ← không dependency
Phase 2 (PFC-Operations.md)     ← không dependency
  Phase 1 + 2 có thể SONG SONG (independent)

Phase 3 (Self-Pattern-Modeling v3.1) ← sau Phase 1+2
  Vì SPM cần reference cả Entity-Compiled.md + PFC-Operations.md

Phase 4 (Imagine-Final.md REWRITE) ← sau Phase 3
  Vì Imagine-Final cần reference SPM §10b (same engine)

Phase 5 (SPM Rename Propagation ~30 files) ← sau Phase 3

Phase 6 (B-files refine) ← sau Phase 1+2+3+4
  Phase 4+5+6 có thể interleave trong 1-2 sessions

Phase 7 (C-files refine ~13 files) ← sau Phase 5+6

Phase 8 (File-Index + verify) ← cuối cùng
```

---

## PHASE 1: ENTITY-COMPILED.md ★ NEW

**Mục tiêu**: Tạo framework-level file cho Entity-Compiled full lifecycle.
**Nguồn**: Drill-Entity-Compiled.md v2.0 (1,340L, 39 insights, 71 citations)
**Output**: ~800-1000L framework file, distilled quality
**Vị trí**: `Core-Deep-Dive/Body-Base/Chunk/Agent-Mechanism/Entity-Compiled.md`
**Ước tính**: 1 session

### Vai trò trong kiến trúc:
```
Valence-Propagation.md §3  = OVERVIEW (concept, 3 subtypes, 2-luồng) — 240L, giữ nguyên
Body-Coupling.md            = COUPLING MECHANISM cụ thể (depth × direction)
★ Entity-Compiled.md        = FULL LIFECYCLE (formation → capacity → dynamics → grief → decay)
Inter-Body-Mechanism.md §8  = REFRAME TERMINOLOGY (brief)
```

### Cấu trúc đề xuất:

```
§0 — DEFINITION + POSITION
  Entity-Compiled = brain compile agent vào body-base ở structural level
  3 subtypes (positive/negative/mixed) — reference Valence-Propagation §3
  Vị trí: Agent-Mechanism/ sibling với Self-Pattern-Modeling + By-Product-Gap-Resonance
  Valence-Propagation §3 = overview → file này = full lifecycle

§1 — NEURAL ARCHITECTURE
  Hub-and-Spoke model (Patterson & Lambon Ralph)
  Body simulation for close person (Beckes & Coan 2012)
  8 research streams hội tụ (condensed)
  Alexithymia = broken readout proof (Bird & Cook 2013)

§2 — FORMATION: TIMELINE + MECHANISM
  Hall 2018: 40→80→200h active interaction
  Schema acceleration (Tse 2007): 48h not weeks
  Neural compatibility predict friendship (Parkinson 2025)
  Sleep = compiler (CA2 neurons, oxytocin REM)
  F2 Loại A vs B (learn new vs override old)
  Hormone boost (mẹ-con = fastest, evolution-protected)
  2 acceleration points: ~40-60h (schema forms) + ~200h (F1 dominates)

§3 — CAPACITY: DUNBAR + CEILING
  Dunbar layers = Entity-Compiled depth gradient
  3 ceiling mechanisms: chunk library + maintenance + interference
  3 strategies (ít+sâu / nhiều+medium / nhiều+nông)
  Kin cost < Friend cost (4 reasons)

§4 — "HỢP TÍNH": 2D MATRIX + META-MATCH
  Shared chunks → shared body → mutual accurate SPM
  2D matrix: Chunk Overlap × Direction Compatibility → 4 quadrants
  Meta-level match > surface match (Parkinson 2025: OFC key)
  "Hợp tính qua effort" = F2 Loại A possible
  Authenticity gate (efference copy detect fake)

§5 — CONVERGENCE
  State converge (emotion, cortisol, HRV, immune, gene expression)
  Trait KHÔNG converge (Big Five, values, political)
  Tolerance band = hardware arousal window + Background-Pattern accumulated
  Evolution: 2 independent mechanisms (pairs + population)

§6 — LOSS + GRIEF
  6 TP chain: routine fire → chunk-miss → L1 stops → L2 collapse → identity → offload
  Grief intensity = A(gap-feed loss) + B(fresh-rebuild) + C(phantom firing)
  Opioid withdrawal model (Robinaugh 2021)
  4 trajectories (Bonanno): resilience 50-60%, recovery, chronic, delayed

§7 — LOVE ↔ HATE SHIFT + DECAY
  Shared neural substrate (Zeki & Romaya 2008)
  3 shift pathways (shared extreme, arousal transfer, dissonance)
  Asymmetry: destroy easy, build hard
  Decay 3-layer: schema persist / affect fade moderate / episode fade fast
  Maintenance cost: kin resilient, friends need active investment

§8 — SOCIAL PORTFOLIO + MACHINE LOGIC
  Roommate→Solo: 3 mechanisms (impression, amygdala, autonomy)
  Solo = MORE social not less (Klinenberg 2012)
  3 vulnerabilities by design
  Modern mismatch: brain designed for ~150, low turnover

§9 — HONEST ASSESSMENT
§10 — CROSS-REFERENCES + CITATIONS (~30 key, distilled from drill's 71)
```

### Cùng phase — VP §3 Update:
- Giữ Valence-Propagation §3 overview (240L)
- THÊM ở cuối §3: "Entity-Compiled.md = full lifecycle deep-dive"
- Tương tự cách §3.3 đã point tới Body-Coupling.md

---

## PHASE 2: PFC-OPERATIONS.md ★ NEW

**Mục tiêu**: Tạo framework-level file cho PFC operations trên Compiled/Fresh spectrum.
**Nguồn**: Drill-Compiled-Fresh-Mechanics.md v2.0 (1,265L, 20 insights, 36 citations)
**Output**: ~800-1000L framework file, distilled quality
**Vị trí**: `Core-Deep-Dive/PFC/PFC-Operations.md`
**Ước tính**: 1 session

### Vai trò trong kiến trúc:
```
Inter-Body-Mechanism.md §3  = SOURCE-OF-TRUTH cho Compiled/Fresh AXIS
Logic-Feeling.md v2.1       = WHY "Logic"/"Feeling" LABELS emerge (observer perspective)
★ PFC-Operations.md         = HOW PFC OPERATES on spectrum (mechanism perspective)
PFC-Function.md             = WHAT PFC does (24 functions catalog)
```

### Cấu trúc đề xuất:

```
§0 — DEFINITION + POSITION
§1 — COMPILED/FRESH SPECTRUM (brief recap, reference Inter-Body-Mechanism §3)
§2 — 2 PFC OPERATIONS: HOLD + SUPPRESS
§3 — 4 TỔ HỢP + 3 OUTCOMES
§4 — COMPILED SUPPRESS (meta-pattern concept)
§5 — COMPILED QUALITY DIMENSION (genuine / schema / threat) ★ KEY
§6 — B vs C DETERMINANT (7 factors)
§7 — PATTERN SHIFTABILITY × Background-Pattern QUADRANTS
§8 — COMPILED SUPPRESS PATHWAYS (→ helplessness, reversal, ego depletion)
§9 — PFC-FRESH: UNIVERSAL RESOURCE
§10 — ARCHITECTURE B INTEGRATION
§11 — HONEST ASSESSMENT
§12 — CROSS-REFERENCES + CITATIONS
```

### Cùng phase — cross-ref updates:
- Inter-Body-Mechanism §3: thêm "PFC-Operations.md = deep-dive cho Hold/Suppress"
- Logic-Feeling.md: thêm "companion: PFC-Operations.md (mechanism perspective)"

---

## PHASE 3: SELF-PATTERN-MATCH.md → SELF-PATTERN-MODELING.md v3.1

**Mục tiêu**: Rename + integrate drill insights vào SPM framework file.
**Nguồn**: Drill-SPM-Mechanism-Analysis.md v2.1 (1,752L, 18 insights)
**Output**: v3.0 (2,618L) → v3.1 (~3,300L)
**Vị trí**: `Core-Deep-Dive/Body-Base/Chunk/Agent-Mechanism/Self-Pattern-Modeling.md`
**Ước tính**: 1-2 sessions (biggest single update)

### A. RENAME toàn file:
- Self-Pattern-Match → Self-Pattern-Modeling (all internal references)
- Backup v3.0

### B. ADD NEW SECTIONS (~710L):

```
+ §2.1b: 1 mechanism × 3 dimensions (not "4 skills")           ~40L
+ §3b:   Clone spectrum + ceiling                               ~120L
          ⚠️ "Over-clone" = present as OBSERVATION + flag open mechanism
          Reference compiled suppress (PFC-Operations §4) as alternative
+ §4b:   SPM scope + boundary (4 agent properties)              ~80L
+ §4c:   SPM → Resonance (4 conditions, reconcile with 5 TRỤC) ~60L
+ §5b:   Abstract entities (fires on chunks not ontology)       ~60L
+ §6b:   Background-Pattern × SPM triple bias                   ~80L
+ §7b:   Transfer + interference (4 types, Freud reframe)       ~80L
+ §8b:   8 failure modes → 3 categories                         ~100L
+ §10b:  SPM × Imagine-Final (same engine, different target)    ~50L
+ §7:    Expand developmental lifecycle table                    ~40L
```

### C. UPDATE EXISTING:
- §12 Alexithymia → merge with failure mode FM6 reference
- §16 Open Questions → add new gaps
- §17 Honest Assessment → update
- §18 Cross-References → add Entity-Compiled.md, PFC-Operations.md, Imagine-Final.md

---

## PHASE 4: IMAGINE-FINAL.md ★ REWRITE

**Mục tiêu**: Upgrade stale DRAFT → framework-quality v2.0.
**Nguồn hiện tại**: DRAFT (2026-04-18, không version header, minimal SPM integration)
**Nguồn mới**: Drill-SPM §10 (SPM × Imagine-Final = same engine), + existing Imagine-Final content
**Output**: v2.0 framework file
**Vị trí**: `Core-Deep-Dive/PFC/Imagination/Imagine-Final.md`
**Ước tính**: 1 session

### Tại sao cần rewrite:
```
① File cũ nhất trong nhóm affected (2026-04-18 — 1 tháng stale)
② Không có version header, không structured như framework standard
③ Drill phát hiện SPM × Imagine-Final = same engine, different target
④ Chưa tích hợp Compiled/Fresh, Entity-Compiled, PFC = Lawyer
⑤ Imagine-Final = concept CỰC QUAN TRỌNG (body pre-feel reference)
   nhưng file chưa match chất lượng framework hiện tại
```

### Cần đọc trước khi rewrite:
- Imagine-Final.md current DRAFT (full content)
- Imagine-Final-Evaluation.md (companion file)
- Imagination.md (parent file?)
- Somatic-Articulation-Loop.md (related?)
- Drill-SPM §10 (same engine analysis)

### Key additions:
```
+ Version header + proper metadata
+ Compiled/Fresh integration
+ SPM × Imagine-Final connection (same engine, different target)
+ Entity-Compiled reference (future self = "agent")
+ Anchor-Schema connection
+ PFC = Lawyer caveat for Imagine-Final
+ Honest Assessment section
```

---

## PHASE 5: SPM RENAME PROPAGATION

**Mục tiêu**: "Self-Pattern-Match" → "Self-Pattern-Modeling" across framework.
**Scope**: ~48 active files, ~500+ occurrences (excluding backup/)
**Ước tính**: 1 session (mechanical but careful)

### Rules:
```
① FULL NAME: "Self-Pattern-Match" → "Self-Pattern-Modeling" EVERYWHERE
② ACRONYM: "SPM" → KHÔNG ĐỔI
③ FILE REFERENCES: "Self-Pattern-Match.md" → "Self-Pattern-Modeling.md"
④ VERSION: "Self-Pattern-Match v3.0" → "Self-Pattern-Modeling v3.1"
⑤ BACKUP files: KHÔNG đổi
```

### FULL LIST — files cần rename (grouped by occurrence count):

```
HIGH (10+ occurrences):
  Agent-Mechanism.md                    23
  Empathy.md                            18
  AI-Schema-Detection.md                11
  Empathy-Education.md                   9

MEDIUM (3-9 occurrences):
  By-Product-Gap-Resonance.md            8
  Connection.md                          7
  Mirror-Neuron-Rejection.md             7
  Valence-Propagation.md                 6
  Uncanny-Valley.md                      6
  Compliance-Floor.md                    5
  99-Master-Synthesis.md                 5
  Gratitude.md                           5
  10-F1-Synthesis-VI.md                  5
  Coordination-Node.md                   4
  Idol-Phenomenon.md                     4
  Personal-Melody.md                     4
  01-File-Index.md                       3
  Religion.md                            3
  Love-Unified.md                        3
  Love-Romantic.md                       3
  Meta-Impact.md                         3
  Background-Pattern.md                  3
  02-Dissonance.md                       3

LOW (1-2 occurrences):
  Core-Software.md                       2
  Collective-Body.md                     2
  Why-Body-Knows.md                      2
  Emergent-Patterns.md                   2
  Status.md                              2
  Protect.md                             2
  Body-Coupling.md                       2
  Human-AI-Future.md                     2
  09-Event-Chunks-Inference-Matrix-VI.md 2
  Ask-AI.md                              1
  Curriculum-Framework.md                1
  summary-paper-outline.md               1
  plan-public.md                         1
  Collective-Arc-Dynamics.md             1
  PFC-Function.md                        1
  Gap-Direction.md                       1
  Imagine-Final.md                       1
  Obligation.md                          1
  Domain-Knowledge-Map.md               1
  04-Integration.md                      1
  Epistemological-Position.md            1
  AI-Self-Model.md                       1
  outline-Love-Romantic-Paradox.md       1
  02-Womb-to-Birth-Baseline-VI.md        1
  08-Verbal-Production-Arc-VI.md         1
```

---

## PHASE 6: B-FILES REFINE (nội dung thay đổi đáng kể)

**Mục tiêu**: Integrate drill insights vào 5 framework files.
**Ước tính**: 1-2 sessions

### B1: By-Product-Gap-Resonance.md v1.0 → v1.1
```
+ Reconcile "4 conditions" (drill) vs "5 TRỤC" (current)
  → 5 TRỤC = evaluation axes (continuous). 4 conditions = necessary (binary). BỔ SUNG.
+ "Resonance decline khi by-product match dừng" — observation from drill + 6 research
  ⚠️ Mechanism = open (clone observation vs compiled suppress hypothesis)
+ Resonance Core vs Enhancers distinction (from Drill-PR-Definition §1)
+ "Duyên số" filtering cost (from Drill-PR-Definition §7)
+ Cross-ref: Entity-Compiled.md, PFC-Operations.md
```

### B2: Connection.md v4.0 → v4.1
```
+ Formation timeline refs → Entity-Compiled.md §2
+ "Hợp tính" refs → Entity-Compiled.md §4
+ Decay 3-layer model refs → Entity-Compiled.md §7
+ Compiled quality × connection (genuine vs schema friend)
```

### B3: Background-Pattern.md v1.1 → v1.2
```
+ §6 đã có Background-Pattern × SPM content — ENRICH:
  → Explicitly name "triple bias" (retrieval + template + interpretation)
  → Self-fulfilling prophecy loop via SPM (detailed mechanism)
+ Background-Pattern × Compiled Quality interaction
+ Cross-ref: PFC-Operations.md §5
```

### B4: Empathy.md v3.0 → v3.1
```
+ Reference 8 failure modes taxonomy (Self-Pattern-Modeling §8b)
+ Transfer/interference between models
+ Background-Pattern triple bias → empathy accuracy
```

### B5: Agent-Mechanism.md v2.0 → v2.1
```
+ supporting_files: add Entity-Compiled.md
+ §4: 3-concept → 4 mechanism files (add Entity-Compiled)
+ SPM preview: rename Self-Pattern-Match → Self-Pattern-Modeling
+ Cross-refs: PFC-Operations.md, Entity-Compiled.md
```

---

## PHASE 7: C-FILES REFINE (~18 files, cross-ref + minor content)

**Mục tiêu**: Cross-refs, terminology alignment, minor content additions.
**Ước tính**: 1 session
**Lưu ý**: Files đã done trong Phase 1/2 ghi (done Px). KHÔNG làm lại.

### Cross-ref + Minor Content:
```
C1  Body-Coupling.md          + Resonance decline cross-ref + compiled suppress in relationship
C2  Autonomy-Hardware.md       + Clone ceiling × vmPFC/DRN cross-ref
C3  Cortisol-Baseline.md       + Compiled suppress pathways cross-ref
C4  Religion.md                + Abstract entities cross-ref (Self-Pattern-Modeling §5b)
C5  Idol-Phenomenon.md         + Parasocial SPM cross-ref
C6  AI-Schema-Detection.md     + SPM on AI entities cross-ref
C7  Love-Romantic.md           + Relationship resonance decline + compiled suppress ref
C8  Love-Unified.md            + 4 conditions resonance cross-ref
C9  OCD-Analysis.md            + SPM failure modes cross-ref
C10 Social-Calibration.md      + Transfer/interference cross-ref
```

### Cross-ref + Content (từ drill, thiếu trong plan v1):
```
C11 Uncanny-Valley.md          + SPM on AI entities (6 occurrences SPM) + agency risk
C12 PFC-Function.md            + PFC-Operations.md companion cross-ref
C13 Empathy-Education.md       + PFC-Fresh universal resource + compiled quality × education
C14 Education-Mechanism.md     + PFC-Fresh universal, compiled quality
C15 AI-Self-Model.md           + SPM cross-ref update
C16 Human-AI-Future.md         + SPM on AI cross-ref
```

### Done trong Phase khác (KHÔNG làm lại):
```
C17 Valence-Propagation.md     + Entity-Compiled.md pointer (done Phase 1)
C18 Inter-Body-Mechanism.md    + PFC-Operations.md cross-ref (done Phase 2)
C19 Logic-Feeling.md           + PFC-Operations companion cross-ref (done Phase 2)
```

### Rename-only (không cần content, CHỈ rename trong Phase 5):
```
Các file còn lại (~25 files) CHỈ cần rename "Self-Pattern-Match" → "Self-Pattern-Modeling".
Không cần content additions. Covered bởi Phase 5.
VD: Gratitude.md, Status.md, Protect.md, Obligation.md, Personal-Melody.md,
    Compliance-Floor.md, Coordination-Node.md, Collective-Body.md,
    Mirror-Neuron-Rejection.md, Gap-Direction.md, Core-Software.md, Ask-AI.md,
    01-File-Index.md, 99-Master-Synthesis.md, Why-Body-Knows.md,
    Emergent-Patterns.md, Meta-Impact.md, Epistemological-Position.md,
    04-Integration.md, 02-Dissonance.md, Domain-Knowledge-Map.md,
    Curriculum-Framework.md, summary-paper-outline.md, plan-public.md,
    Collective-Arc-Dynamics.md, + VI files (4 files)
```

---

## PHASE 8: FILE-INDEX + VERIFY

**Ước tính**: 0.5 session

```
① Update 01-File-Index.md (Core-Deep-Dive)
② Verify: mỗi new file ĐƯỢC reference bởi ít nhất 3 files
③ Verify: mỗi drill insight ĐÃ ĐƯỢC propagate
④ Verify: SPM rename COMPLETE (0 occurrences "Self-Pattern-Match")
⑤ Update plan status
```

---

## TỔNG HỢP

```
┌──────────────────────────────────────────────────────────────────┐
│ Phase │ Công việc                        │ Sessions │ Dep.      │
├───────┼──────────────────────────────────┼──────────┼───────────┤
│   1   │ Entity-Compiled.md (NEW)         │ 1        │ none      │
│       │ + Valence-Propagation §3 pointer │          │           │
│   2   │ PFC-Operations.md (NEW)          │ 1        │ none      │
│       │ + Inter-Body-Mechanism cross-ref │          │           │
│       │ + Logic-Feeling cross-ref        │          │           │
│   3   │ Self-Pattern-Modeling v3.1       │ 1-2      │ P1+P2    │
│   4   │ Imagine-Final.md REWRITE         │ 1        │ P3       │
│   5   │ SPM Rename (~48 files)           │ 1        │ P3       │
│   6   │ B-files refine (5 files)         │ 1-2      │ P1+2+3+4 │
│   7   │ C-files refine (~16 files)       │ 1        │ P5+P6    │
│   8   │ File-Index + verify              │ 0.5      │ P7       │
├───────┼──────────────────────────────────┼──────────┼───────────┤
│ TOTAL │                                  │ 7.5-9.5  │           │
└──────────────────────────────────────────────────────────────────┘

FULL FILE COUNT:
  Phase 1-4: 4 file mới/rewrite (~3,400-4,000L total)
  Phase 5:   ~48 files rename (mechanical)
  Phase 6:   5 B-files (significant content additions)
  Phase 7:   ~16 C-files (cross-ref + minor content)
             + 3 done trong Phase 1/2 (Valence-Propagation, Inter-Body, Logic-Feeling)
             + ~25 rename-only (covered Phase 5)
  Phase 8:   File-Index + verification
  ─────────────────────────────────────────
  TOTAL TOUCHED: ~70 files (4 new/rewrite + 5 B-refine + 16 C-refine + ~48 rename)
  (Nhiều file overlap giữa rename + refine → counted once)

  87 insights propagated
  4 drill files maintained as detailed references
  1 open question flagged (clone vs compiled suppress)
```

---

## NGUYÊN TẮC PROPAGATION

```
① DISTILL, KHÔNG COPY-PASTE
② FRAMEWORK FILE ≠ DRILL FILE
③ MAINTAIN DRILL FILES as references
④ CROSS-REF BIDIRECTIONAL
⑤ VERSION BUMPS: new = v1.0, renamed = v3.1, updated = minor bump
⑥ NAMING: "Self-Pattern-Modeling" (American, 1 chữ L). Acronym SPM giữ nguyên.
⑦ HẠN CHẾ TỐI ĐA VIẾT TẮT:
   → Viết đầy đủ tên concept trong nội dung
   → CHỈ viết tắt established: SPM, PFC
   → KHÔNG dùng: BFM, EC, CF, BPGR trong prose
   → Table/diagram OK nhưng PHẢI có legend
⑧ OPEN QUESTIONS: flag rõ ràng, KHÔNG chốt khi chưa drill đủ
```

---

**Created**: 2026-05-19
**Updated**: 2026-05-19 (v2 — Imagine-Final rewrite, clone hypothesis, scan results)
**Status**: PLAN v2 READY — chờ user approve.
