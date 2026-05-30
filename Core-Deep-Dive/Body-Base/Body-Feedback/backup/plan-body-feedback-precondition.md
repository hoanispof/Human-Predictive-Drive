# Plan: Body-Feedback-Precondition — H10 Formalize + Rename + P→Precondition + Collision Fix

> **Mục tiêu**: Formalize H10 (5 Preconditions for Body-Feedback Signal Fire) thành file chính thức `Body-Feedback-Precondition.md`. Rename H10 + P1-P5 → Precondition-1 to Precondition-5 across framework. Fix GBN P1-P5 collision (→ Axis-1).
>
> **Ngày tạo**: 2026-05-30
> **Scope**: 1 NEW file (1,420L) + ~92 active files rename (H10 ~554 occ + P1-P5 → Precondition ~TBD occ) + GBN collision fix (~7 files, ~70 occ) + cross-ref updates (~6 files)
> **Nguyên tắc**: Chậm mà chắc. Content quality > speed. Không duplicate content từ RSA/BFM/DSA. KHÔNG viết tắt concept.
> **Status**: ✅✅ ALL 11/11 PHASES DONE — PROJECT COMPLETE
> **Cập nhật 2026-05-30**: Drill-Body-Feedback/ (4 files, H10 origin) → SKIP rename, add forward pointer only. Lý do: §0.4.
> **Cập nhật 2026-05-30 (session 3)**: C3a (Observation/), C3b (Body-Base/), C3c (PFC/Clarification/Root), C4 (Research/Public/Root) ALL DONE. C5 verification PASSED — H10 only in whitelist files.

---

## §0 — TẠI SAO

### §0.1 — H10 đang "homeless"

```
HIỆN TẠI:
  03-Reward.md (DRILL file)     ← ĐỊNH NGHĨA H10 (nguồn gốc, exploratory)
  Body-Feedback.md (SYNTHESIS)  ← CLAIM ownership, chỉ có 48-dòng summary
  RSA/BFM/DSA                   ← DÙNG H10, không define
  92 active files               ← DÙNG H10 như concept name

VẤN ĐỀ:
  ① "H10" là hypothesis number, vô nghĩa cho reader mới
  ② Canonical definition nằm trong drill file (không formal)
  ③ Framework đã phát triển vượt xa H10 gốc nhưng chưa back-propagate
  ④ P1-P5 collision với Gap-Body-Need.md (2 bộ P1-P5 khác nghĩa)
```

### §0.4 — Drill-Body-Feedback/ GIỮ H10 (origin files)

```
QUYẾT ĐỊNH (2026-05-30):
  Drill-Body-Feedback/ (4 files: 01-Foundation, 02-Dissonance, 03-Reward, 04-Integration)
  là GỐC DRILL ra H10. H10 = tên giả thuyết trong quá trình drill.

  → KHÔNG RENAME H10 trong 4 file này.
  → CHỈ thêm forward pointer: "H10 đã formalize → Body-Feedback-Precondition.md"

LÝ DO:
  ① H10 là TÊN RIÊNG của hypothesis trong quá trình khám phá. Rename = xóa lịch sử.
  ② P1-P5 trong drill = PHASE NUMBERS (P0→P5), KHÔNG PHẢI Precondition numbers.
     302 chữ P = phần lớn drill phases → rename = SAI NGHĨA.
  ③ Body-Feedback-Precondition.md đã có BRIDGE: "v1.0: Refine từ drill H10"
     + dependencies liệt kê "03-Reward.md §3 H10 drill origin".
  ④ Chỉ thiếu REVERSE bridge (drill → BFP.md) → thêm forward pointer.
  ⑤ Framework files (C1 DONE) đã dùng tên chính thức khi reference CONCEPT,
     dù pointer tới drill files vẫn chính xác (file names không đổi).

SCOPE IMPACT:
  - 92 H10 + 302 P = 394 occurrences KHÔNG CẦN RENAME → giảm effort + risk
  - Drill-Chunk/ (26 active files, ~112 H10) VẪN RENAME vì chúng DÙNG H10, không originate
```

### §0.2 — 5 GAPs phát hiện qua deep analysis

```
GAP 1: Dissonance preconditions — zero coverage → ✅ COVERED in BFP.md §9
GAP 2: Precondition-3 × Precondition-4 interaction — OPEN (BFP.md §10.2 Q1)
GAP 3: Precondition-1 thiếu direction component → ✅ RESOLVED (renamed Directed-Gap)
GAP 4: Direct-State simplified preconditions → ✅ COVERED in BFP.md §1.2
GAP 5: P1-P5 naming collision với GBN 5-Parameter → ✅ RESOLVED (Axis-1 to Axis-5)
```

### §0.3 — 5 Preconditions cần refine

```
┌──────────────────┬─────────────────────┬───────────────────────┬──────────────────────────────────────────┐
│ Formal ID        │ Tên cũ (H10)        │ Tên mới               │ Thay đổi chính                           │
├──────────────────┼─────────────────────┼───────────────────────┼──────────────────────────────────────────┤
│ Precondition-1   │ Schema pending      │ Directed-Gap          │ +hw/schema distinction                   │
│                  │                     │                       │ +direction implicit                      │
│                  │                     │                       │ +Precondition-2 prerequisite for schema   │
├──────────────────┼─────────────────────┼───────────────────────┼──────────────────────────────────────────┤
│ Precondition-2   │ Chunks base adequate│ Chunk-Substrate       │ +Precondition-2a genesis vs 2b decode    │
│                  │                     │                       │ +Eval/DS difference                      │
│                  │                     │                       │ +Van Gogh = Precondition-2 not 4         │
├──────────────────┼─────────────────────┼───────────────────────┼──────────────────────────────────────────┤
│ Precondition-3   │ Prediction-delta    │ Delta-Gate            │ +scope: Evaluative ONLY                  │
│                  │                     │                       │ +boredom ≠ Precondition-3 (1+4 co-fail)  │
│                  │                     │                       │ +sequential before Precondition-4        │
├──────────────────┼─────────────────────┼───────────────────────┼──────────────────────────────────────────┤
│ Precondition-4   │ Goldilocks zone     │ Match-Range           │ +direction-match component               │
│                  │                     │                       │ +dynamic zone (not fixed 40-70%)         │
│                  │                     │                       │ +expertise shift                         │
├──────────────────┼─────────────────────┼───────────────────────┼──────────────────────────────────────────┤
│ Precondition-5   │ Chunk tag binary    │ Compile-Gate          │ +NT7 direction gate model                │
│                  │                     │                       │ +4-pathway × quality ceiling             │
│                  │                     │                       │ +N/A for Direct-State                    │
│                  │                     │                       │ +re-association 3 paths                  │
└──────────────────┴─────────────────────┴───────────────────────┴──────────────────────────────────────────┘

Số lượng: VẪN 5 preconditions (gap-direction absorbed vào Precondition-1 + Precondition-4)
Scope: "ALL 5 required" chỉ cho EVALUATIVE. Direct-State = simplified Precondition-1 + hardware Precondition-4.
⭐ Naming: "P1-P5" là viết tắt → đổi thành Precondition-1 to Precondition-5 (framework rule: KHÔNG viết tắt concept).
```

---

## §1 — TÊN + DEFINITIONS

### §1.1 — File name: Body-Feedback-Precondition.md

```
Lý do chọn:
  ① Fit naming pattern: Body-Feedback-Mechanism, Body-Feedback-Label, Body-Feedback-Precondition
  ② "Body-Feedback" = đúng concept cha (folder name)
  ③ "Precondition" = WHEN/WHETHER signal fires (phân biệt Mechanism = HOW)
  ④ Hoàn thành bộ 3 siblings: Mechanism → Label → Precondition

Rejected:
  "Body-Signal-Precondition" — "Body-Signal" mơ hồ, không dùng trong folder
  "Signal-Gate" — metaphor, không framework vocab
  "Signal-Fire-Condition" — action verb breaks naming pattern
```

### §1.2 — Concept name trong text (inline references)

```
⭐ RENAME RULES — 2 TRACKS (thực hiện đồng thời per file):

  ═══════════════════════════════════════════════════════════════
  TRACK 1: H10 → Body-Feedback-Precondition (thực hiện TRƯỚC)
  ═══════════════════════════════════════════════════════════════

  Pass 1: "H10 5 preconditions"     → "5 Body-Feedback-Preconditions"
  Pass 2: "H10 5 Preconditions"     → "5 Body-Feedback-Preconditions"
  Pass 3: "H10 Precondition"        → "Body-Feedback-Precondition"
  Pass 4: "H10 preconditions"       → "Body-Feedback-Preconditions"
  Pass 5: "H10 precondition"        → "Body-Feedback-Precondition"
  Pass 6a: "H10 P1"                 → "Precondition-1 Directed-Gap"
  Pass 6b: "H10 P2"                 → "Precondition-2 Chunk-Substrate"
  Pass 6c: "H10 P3"                 → "Precondition-3 Delta-Gate"
  Pass 6d: "H10 P4"                 → "Precondition-4 Match-Range"
  Pass 6e: "H10 P5"                 → "Precondition-5 Compile-Gate"
  Pass 7:  "H10" (remaining)        → "Body-Feedback-Precondition"

  ═══════════════════════════════════════════════════════════════
  TRACK 2: P1-P5 → Precondition-1 to Precondition-5 (SAU Track 1)
  ⭐ Framework rule: KHÔNG viết tắt concept
  ═══════════════════════════════════════════════════════════════

  Phase A: Combo/range patterns TRƯỚC (tránh substring conflict)
    "P1,P3-P5"     → "Precondition-1, Precondition-3–Precondition-5"
    "P1-P3,P5"     → "Precondition-1–Precondition-3, Precondition-5"
    "P1,P2,P4,P5"  → "Precondition-1, Precondition-2, Precondition-4, Precondition-5"
    "P1-P5"        → "Precondition-1–Precondition-5"
    "P2-P5"        → "Precondition-2–Precondition-5"
    "P1-P4"        → "Precondition-1–Precondition-4"
    (các range khác nếu có)

  Phase B: Individual replace_all
    "P5" → "Precondition-5"
    "P4" → "Precondition-4"
    "P3" → "Precondition-3"
    "P2" → "Precondition-2"
    "P1" → "Precondition-1"

  Phase C: Standalone fixes
    "P-fail"  → "Precondition-fail" (nếu có)
    "per-P "  → "per-Precondition " (nếu có)
    "Each P " → "Each Precondition " (nếu có)

  ═══════════════════════════════════════════════════════════════
  POST-REPLACE CHECKS (cả 2 tracks)
  ═══════════════════════════════════════════════════════════════

  → "Body-Feedback-Precondition Precondition" → fix (remove duplicate)
  → "Body-Feedback-Precondition check/met" → OK (keep)
  → False match check: PFC, DRD4, COMT KHÔNG bị ảnh hưởng
    (P1-P5 = "P" + digit, PFC = "P" + letter → safe)
  → Box-drawing tables → fix alignment (column widths thay đổi)
  → Sub-variants: Precondition-1a, Precondition-1b, Precondition-2a, Precondition-2b
    (tự động đúng vì P1a chứa P1 as substring)

  ⚠️ Precondition-labels per file:
  → First use: "Precondition-2 Chunk-Substrate (Body-Feedback-Precondition.md §3)"
  → Subsequent: "Precondition-2 Chunk-Substrate" hoặc "Precondition-2"
```

### §1.3 — P1-P5 collision fix — ✅ DONE 2026-05-30

```
COLLISION: Gap-Body-Need.md dùng P1-P5 cho 5-Parameter model
  (P1=Hardware Source, P2=Satiation Profile, P3=Reward Composition,
   P4=Chain to Body-Base, P5=Collective Dependency)
  → HOÀN TOÀN KHÁC nghĩa với Precondition P1-P5

GIẢI PHÁP: Rename Gap-Body-Need P1-P5 → Axis-1 to Axis-5
  → GBN's model mô tả 5 TRỤC quan sát gap → "Axis" semantically chính xác
  → Framework rule: KHÔNG viết tắt concept → "Axis-1" not "Ax1"
  → GBN labels chỉ xuất hiện trong ~7 files, ~70 occ → disruption thấp
  → Precondition P1-P5 xuất hiện trong ~92 files, ~554 occ → giữ nguyên

✅ FILES ĐÃ FIX (7 files, ~70 occ):
  ① Gap-Body-Need.md — 39 occ P1-P5 → Axis-1 to Axis-5 ✅
  ② Gap-Distribution-Profile.md — ~20 occ cross-refs ✅
  ③ 07-Music-Entrainment-Reward-Dynamics.md — 5 occ ✅
  ④ Resonance-Per-Entity.md — 3 occ ✅
  ⑤ 01-File-Index.md — 2 occ ✅
  ⑥ expert-verification-map.md — 1 occ ✅
  ⑦ Body-Feedback.md — P1-P5 here = Precondition (NO change needed) ✅

VERIFIED: grep P1-P5 in GBN context = 0 in active files.
```

---

## §2 — FILE STRUCTURE (Body-Feedback-Precondition.md)

### §2.1 — Câu hỏi file trả lời

```
03-Reward.md (drill):             H10 origin, 7-step VTA, 7 cases
Reward-Signal-Architecture.md:    WHAT KINDS of reward signal
Dissonance-Signal-Architecture.md: WHAT KINDS of dissonance signal
Body-Feedback-Mechanism.md:       HOW chunks fire (dynamics)
Body-Feedback-Precondition.md:    ⭐ WHEN does ANY signal fire? What must be true?
```

### §2.2 — Section outline

```
§0  — POSITION + SCOPE + READING GUIDE                     ~100L
      Frontmatter, position diagram, reading prerequisites
      KHÔNG duplicate: RSA §1.3, BFM §6.2, BF §5.2

§1  — FORMAL STATEMENT                                     ~60L
      Logical conjunction: signal fires IFF all 5 Preconditions met
      Falsifiability claim. Scope qualifier (Evaluative vs Direct-State)

§2  — Precondition-1: DIRECTED-GAP                         ~180L
      §2.1 Precondition-1a Hardware-driven (Sensory-Driven, infant từ sinh)
      §2.2 Precondition-1b Pattern-driven (schema pending, cần Precondition-2 trước)
      §2.3 Direction implicit (Gap-Direction insight absorbed)
      Failure: satiated / no active goal / empty scroll

§3  — Precondition-2: CHUNK-SUBSTRATE                      ~200L
      §3.1 Precondition-2a Genesis ("chưa biết = không gap", Tầng 0)
      §3.2 Precondition-2b Decode (evaluation at stimulus moment)
      §3.3 Evaluative vs Direct-State difference
      Failure: confusion / Van Gogh untrained / musical anhedonia

§4  — Precondition-3: DELTA-GATE                           ~160L
      §4.1 Mechanism: VTA habituation-based detection
      §4.2 Scope: Evaluative ONLY (Direct-State bypass VTA)
      §4.3 Boredom disambiguation (boredom ≠ Precondition-3, = 1+4 co-fail)
      §4.4 DRD4 modulation (Step 3 downstream, not Precondition-3 itself)
      Failure: routine / habituated / no delta detected

§5  — Precondition-4: MATCH-RANGE                          ~200L
      §5.1 Direction-match (not just magnitude)
      §5.2 Dynamic zone (not fixed 40-70%, per-gap/person/context)
      §5.3 Expertise shift (E₀→E₃ gradient narrows/shifts zone)
      §5.4 Failure asymmetry (reward vs dissonance firing)
      Failure: too alien / too familiar / direction mismatch

§6  — Precondition-5: COMPILE-GATE                         ~220L
      §6.1 Scope: Evaluative ONLY (Direct-State = N/A)
      §6.2 NT7 direction gate model (replace binary opioid/cortisol)
      §6.3 4-Pathway × quality ceiling (HwFit/Trust/Social/Threat)
      §6.4 Re-association 3 paths (overlay, not deletion)
      §6.5 Precondition-5 ≠ Precondition-2 distinction (substrate vs tag)
      Failure: threat-tagged → relief only / "giỏi mà ko thích"

§7  — CONJUNCTION LOGIC + FAILURE MODE TABLE                ~180L
      AND-gate structure. Per-precondition failure → specific outcome
      Partial cases ("almost" = mild reward). Clinical implications
      Precondition-3→Precondition-4 sequential dependency
      Precondition-2→Precondition-1 dependency for schema-level gaps

§8  — DEVELOPMENTAL ARC                                    ~160L
      Infant: Precondition-1a only, 2 minimal, 3 available, 4 wide, 5 default
      Child: Precondition-2 accumulates, 5 compiles from social feedback
      Adult: Precondition-2 differentiated, 4 narrows, 5 full biographical
      Aging/burnout: Precondition-1 weakens, 3 erodes, 4 can re-widen

§9  — DISSONANCE APPLICATION                               ~140L
      How Precondition-1–Precondition-5 apply to dissonance (not just reward)
      Precondition-5 inverted: threat-tag LOWERS dissonance threshold
      Cross-ref DSA without duplication

§10 — HONEST ASSESSMENT                                    ~80L
      Confidence per precondition (🟢/🟡/🔴)
      Open questions (3-4 items)
      Falsifiable predictions

§11 — CROSS-REFERENCES                                     ~60L
      Pointers: 03-Reward.md, RSA, DSA, BFM §6.2, BF §5.2,
      Cortisol-Baseline, Chunk.md, Compile-Taxonomy, Gap-Direction

TOTAL ESTIMATED: ~1,740L
```

### §2.3 — KHÔNG duplicate (boundary rules)

```
NỘI DUNG THUỘC FILE KHÁC — CHỈ CROSS-REF:

  RSA §1.3:  Evaluative/Direct-State × Precondition-1–Precondition-5 comparison table
             → BFP reference: "For type-split per precondition, see RSA §1.3"

  BFM §6.2: Chunk-Shift/Miss/Gap × Precondition-1–Precondition-5 mapping table
             → BFP reference: "For chunk dynamics × preconditions, see BFM §6.2"

  BF §5.2:  48-line H10 summary table (stays as synthesis summary)
             → Update pointer: "Detail: Body-Feedback-Precondition.md"

  DSA:      Timing asymmetry (dissonance→reward slow because preconditions re-check)
             → BFP reference at §9
```

### §2.4 — Dependencies (reading order)

```
PREREQUISITES (đọc trước BFP):
  01-Foundation.md — dual-pull, interface loop, body-base
  02-Dissonance.md — 3 genuine sources, spectrum
  03-Reward.md — H10 drill origin, 7-step VTA, 7 cases
  Chunk.md v2.2+ — chunk substrate, context-tag
  Compile-Taxonomy.md v2.0 — 4 pathways (for Precondition-5)

PARALLEL (đọc song song):
  RSA — WHAT KINDS reward (→ type-split per precondition)
  DSA — WHAT KINDS dissonance (→ dissonance application)
  BFM — HOW chunks fire (→ dynamics × preconditions)
```

---

## §3 — PHASES

### Phase A: Create Body-Feedback-Precondition.md — ✅ DONE 2026-05-30

```
✅ Session A1: §0-§6 — Core definitions (942L)
  Frontmatter, position, formal statement, Precondition-1–5 full definitions
  Source: 03-Reward.md §3 + Gap-Direction + RSA §1.3 + Cortisol-Baseline NT7
         + Compile-Taxonomy 4-pathway + Reward-Calibration + Boredom

✅ Session A2: §7-§11 — Analysis + assessment (478L)
  Conjunction logic, developmental arc, dissonance application,
  honest assessment, cross-references
  Source: BFM §6.2 + DSA §3/§7.5 + Child-Dev-Mechanism + 04-Integration

✅ Session A3: P → Precondition-1 to Precondition-5 rename WITHIN BFP.md
  ~100+ occurrences renamed. Framework rule: KHÔNG viết tắt concept.
  6 phases: combo patterns → range patterns → standalone → individual → box tables → verify
  Sub-variants: Precondition-1a, 1b, 2a, 2b (tự động đúng)
  Ranges: Precondition-1–Precondition-5 (en-dash)
  Verified: grep P[1-5] = 0, PFC/DRD4/COMT nguyên vẹn

RESULT: Body-Feedback-Precondition.md v1.0 — 1,420L (§0-§11 complete, Precondition naming)
```

### Phase B: P1-P5 Collision Fix — ✅ DONE 2026-05-30

```
✅ Session B1: Gap-Body-Need P1-P5 → Axis-1 to Axis-5 (7 files, ~70 occ)
  → Framework rule: KHÔNG viết tắt → "Axis-1" not "Ax1"
  ① Gap-Body-Need.md — 39 occ ✅
  ② Gap-Distribution-Profile.md — ~20 occ ✅
  ③ 07-Music-Entrainment-Reward-Dynamics.md — 5 occ ✅
  ④ Resonance-Per-Entity.md — 3 occ ✅
  ⑤ 01-File-Index.md — 2 occ ✅
  ⑥ expert-verification-map.md — 1 occ ✅
  ⑦ Body-Feedback.md — NO change (P1-P5 = Preconditions here) ✅

RESULT: 0 collision remaining. P1-P5 = Preconditions only. VERIFIED.
```

### Phase C: Rename H10 + P→Precondition (~92 files, H10 ~554 occ + P→Precondition ~TBD occ)

```
REPLACE RULES: Xem §1.2 (2 tracks chi tiết)

  TRACK 1: H10 → Body-Feedback-Precondition (7 passes)
  TRACK 2: P1-P5 → Precondition-1 to Precondition-5 (3 phases)

  Thực hiện ĐỒNG THỜI per file:
    ① Track 1 trước (H10 P1 → Precondition-1 Directed-Gap, etc.)
    ② Track 2 sau (remaining P1-P5 → Precondition-1 to 5)
    ③ Post-replace checks (redundancy, false match, alignment)

  ⚠️ POST-REPLACE CHECKS:
  → "Body-Feedback-Precondition Precondition" → fix (remove duplicate)
  → "Body-Feedback-Precondition Hypothesis" → OK (keep)
  → Section headers containing "H10" → update title
  → Dependency lists: add Body-Feedback-Precondition.md, remove "H10" refs
  → PFC/DRD4/COMT không bị ảnh hưởng (verify mỗi session)
  → Box-drawing tables → fix alignment

SKIP:
  ① backup/ files — SKIP
  ② _backup/ files — SKIP
  ③ plan-*.md files — SKIP (trừ plan ĐANG active)
  ④ html-page/ — SKIP

SESSION GROUPING (by folder):

  ✅ Session C1: Body-Feedback/ folder (8 active files) — DONE 2026-05-30
    Body-Feedback.md (25 H10 + 10 P), RSA (17 H10 + 44 P), BFM (9 H10),
    Gap-Direction (24 H10 + 36 P), Reward-Calibration (8 H10 + 1 P),
    BFL (5 H10 + 1 P), DSA (3 H10), Drill-Evolutionary-Sensor (2 H10)
    → ALL verified H10=0, P[1-5] correct (skips documented per file)
    → 4 box-drawing tables restructured (RSA §1.3, GD §6.3, BF §5.2, BFM §6.2)

  ✅ Session C2a: Drill-Body-Feedback/ forward pointer (4 files) — DONE 2026-05-30
    01-Foundation, 02-Dissonance, 03-Reward, 04-Integration
    → KHÔNG RENAME H10/P1-P5 (origin files — xem §0.4 lý do)
    → Forward pointer thêm ở blockquote header mỗi file:
      "⚠️ H10 formalized: H10 đã được formalize thành Body-Feedback-Precondition.md"
    → 4 edits hoàn tất

  ✅ Session C2b: Drill-Chunk/ active files (~30 files) — DONE 2026-05-30
    C2b-light: Chunk-Internal-Processing/ (3 files, 3 H10) ✅
    C2b-master: 99-Master-Synthesis.md (6 H10 → 5 renamed + 1 whitelist, 11 P) ✅
    C2b-heavy-EN: Modality-Arcs/ 8 files + Foundation/ 3 files + 09-Event + 10-F1 ✅
    C2b-heavy-VI: All 12 VI mirror files ✅
    → SKIP: backup/ (3 files)
    → H10 whitelist: 00-Chunk-System-Sketch EN+VI (hypothesis table ID col),
                     99-Master-Synthesis (hypothesis table ID col)
    → P[1-5] 3-type collision resolved:
      Type 1 (Precondition refs): ALL renamed ✅
      Type 2 (Pain event IDs P1-P4 in 09-Event + 10-F1): preserved ✅
      Type 3 (Drill phase markers F1-P[n], N+4a P[n]): preserved ✅
    → ~200+ individual renames applied
    → Verified: H10=2 (whitelist), P[1-5] = Pain events + drill phases only

  ✅ Session C3: Core-Deep-Dive/ other (~20+ files) — DONE (sessions 2-3)
    C3a: Observation/ (Liking-Wanting 27, Gratitude 15, Status, Boredom, etc.) ✅
    C3b: Body-Base/ (Feeling 5+6, Body-Base 6, Why-Body-Knows 6+20,
                      Cortisol 8+8, Schema 2, Chunk 1, etc.) ✅
    C3c: PFC/ + Clarification/ + Root (PFC-Hardware, PFC-Config, LFB,
          Imagine-Final, SAL, Neural-Arch, Blackbox, Modality,
          Prediction-Error-Is-Not-Reward 15+15, Dopamine-Is-Not-Reward 10,
          01-File-Index 4+1) ✅
    → ~150+ occ. across 30+ files
    → "Precondition [space] [number]" (missing dash) found+fixed in 3 places
    → P collision correctly skipped: Body-Coupling P1-P7, Agent-Mechanism P1-P12,
      PTSD P1-P5, 01-File-Index "P1-P3" drill phases

  ✅ Session C4: Research/ + Root + Public-Plan/ (~29 files) — DONE (session 3)
    Drill-Sound-Brain/ (03-Sound 12+18, 06-Music 3+12, 10-Synthesis, etc.)
    Health-Conditions/ (Addiction 20+10, Nicotine 2, Alcohol 2,
                        Autism 3, ADHD 2)
    Human-Learning/ (Education-Mechanism 3+1+1, Child-Dev 6+3)
    Melody-Technology/ (Religion 7, Idol 11, Overview 4)
    Global/ (AI-Self-Model 2, Social-Calibration 6, Fidgeting 2)
    Climate-Cognition 3
    Root: Core-Software 8, 00-Parameter-Overview 2, Ask-AI 4
    Public-Plan/ (5 files), Plan-Translate/ (3 files)
    → ~174 occ. H10+P renamed
    → ADHD P1-P5 correctly skipped (ADHD predictions)
    → 07-Music-Entrainment P0-P4 correctly skipped (timeline labels)

  ✅ Session C5: Verification pass — DONE (session 3)
    grep "\bH10\b" toàn bộ framework → 62 files remaining, ALL in:
      ① Whitelist: Drill-Body-Feedback/ (4 files), Body-Feedback-Precondition.md,
         00-Chunk-System-Sketch EN+VI, 99-Master-Synthesis
      ② plan-*.md files (SKIP per rules)
      ③ backup/ and _backup/ files (SKIP per rules)
    → 0 active non-whitelist files with H10
    → "Precondition [space] [number]" (missing dash): 0 in active non-whitelist files
    → 2 missed files (Social-Calibration 6, Fidgeting 2) caught+fixed during C5
```

### Phase D: Cross-Reference Updates (~6 files) — ✅ DONE 2026-05-30

```
✅ Session D1: Update pointers + file registries — DONE (session 3)

  ① Body-Feedback.md:
     → ✅ Added BFP.md to folder tree (new PRECONDITION section)
     → ✅ Added BFP.md to reading guide Tier 2 (③b)
     → ✅ Updated file count 16→17, ~26,100→~27,500L (all 8 occurrences)

  ② RSA.md:
     → ✅ Added Body-Feedback-Precondition.md v1.0 to dependency list

  ③ BFM.md:
     → ✅ Added Body-Feedback-Precondition.md v1.0 to dependency list

  ④ DSA.md:
     → ✅ Added Body-Feedback-Precondition.md v1.0 to dependency list

  ⑤ 01-File-Index.md:
     → ✅ Added Body-Feedback-Precondition.md entry (full description, 1,420L)

  ⑥ Core-Software.md:
     → ✅ Updated §4.2 reference: "(Body-Feedback.md §5)" → "(Body-Feedback-Precondition.md)"
     → ✅ Added BFP.md to §13.5 file list
```

---

## §4 — VERIFICATION

```
PHASE A VERIFY: ✅ ALL PASSED
  ① File exists: Body-Feedback-Precondition.md ✅
  ② Line count: 1,420L (compact hơn dự kiến, đủ content) ✅
  ③ All 5 preconditions defined with refinements ✅
  ④ §9 dissonance application present ✅
  ⑤ No duplication with RSA §1.3 / BFM §6.2 ✅
  ⑥ P → Precondition-1 to Precondition-5 naming (A3) ✅
  ⑦ grep P[1-5] = 0, PFC/DRD4/COMT safe ✅

PHASE B VERIFY: ✅ ALL PASSED
  ① grep "P1.*Hardware Source" Gap-Body-Need.md → 0 (renamed to Axis-1) ✅
  ② grep "Axis-1.*Hardware Source" Gap-Body-Need.md → present ✅
  ③ No remaining P1-P5 collision in active files ✅
  ④ Zero "Ax1" abbreviation in data files (only in plan explanatory text) ✅

PHASE C1 VERIFY: ✅ ALL PASSED 2026-05-30
  ① H10=0 in all 8 Body-Feedback/ active files ✅
  ② P[1-5] correctly skipped where = drill phases/file sequence/prediction labels ✅
  ③ 4 box-drawing tables restructured (RSA §1.3, GD §6.3, BF §5.2, BFM §6.2) ✅
  ④ "Body-Feedback-Precondition Precondition" redundancy = 0 ✅
  ⑤ PFC/DRD4/COMT nguyên vẹn ✅

PHASE C2-C4 VERIFY:
  ① grep "\bH10\b" active files → 0
     WHITELIST (allowed H10):
       Drill-Body-Feedback/ (4 files — origin, forward pointer added)
       Body-Feedback-Precondition.md (historical context intentional)
       00-Chunk-System-Sketch EN+VI (hypothesis table ID column)
       99-Master-Synthesis (hypothesis table ID column)
     EXCLUDE: backup/, _backup/, plan-*.md, html-page/
  ② grep "Precondition Precondition" → 0 (no redundancy)
  ③ grep "Body-Feedback-Precondition" → present (all non-origin H10 replaced)
  ④ grep "\bP[1-5]\b" active files → 0 (all P→Precondition replaced)
     ⚠️ Drill-Chunk/: assess P1-P5 per file (may be drill-internal, not precondition)
  ⑤ grep "PFC" → nguyên vẹn (not broken by Track 2)
  ⑥ Spot-check top 10 heaviest files: context correct

PHASE D VERIFY:
  ① Body-Feedback.md §5.2 has pointer to Body-Feedback-Precondition.md
  ② RSA dependencies include Body-Feedback-Precondition.md
  ③ 01-File-Index.md lists Body-Feedback-Precondition.md
  ④ Core-Software.md references updated
```

---

## §5 — SESSION ESTIMATE

```
┌─────────┬──────────────────────────────────────────────────────────────────┬──────────┐
│ Session │ Nội dung                                                         │ Status   │
├─────────┼──────────────────────────────────────────────────────────────────┼──────────┤
│ A1      │ BFP.md §0-§6 (core definitions, 942L)                           │ ✅ DONE  │
│ A2      │ BFP.md §7-§11 (analysis, 478L)                                  │ ✅ DONE  │
│ A3      │ P → Precondition-1 to 5 rename IN BFP.md (~100+ occ)            │ ✅ DONE  │
│ B1      │ GBN P1-P5 → Axis-1 to Axis-5 (7 files)                         │ ✅ DONE  │
│ C1      │ H10 + P→Precondition rename: Body-Feedback/ (8 files)           │ ✅ DONE  │
│ C2a     │ Drill-Body-Feedback/ forward pointer only (4 files)             │ ✅ DONE  │
│ C2b     │ H10 + P→Precondition rename: Drill-Chunk/ (~30 files, ~200+ ren) │ ✅ DONE  │
│ C3      │ H10 + P→Precondition rename: Core-Deep-Dive/ other (30+ files) │ ✅ DONE  │
│ C4      │ H10 + P→Precondition rename: Research/ + Root (~29 files)        │ ✅ DONE  │
│ C5      │ Verification pass (H10=0 trừ origin, P[1-5]=0, PFC safe)        │ ✅ DONE  │
│ D1      │ Cross-ref updates (6 files: BF+RSA+BFM+DSA+FI+CS)               │ ✅ DONE  │
├─────────┼──────────────────────────────────────────────────────────────────┼──────────┤
│ TOTAL   │ 11/11 DONE                                                       │ COMPLETE │
└─────────┴──────────────────────────────────────────────────────────────────┴──────────┘

Recommended order: ✅A1 → ✅A2 → ✅A3 → ✅B1 → ✅C1 → C2a → C2b → C3 → C4 → C5+D1

Notes:
  Phase C2a = nhanh (~5 phút, 4 forward pointers). Làm đầu session tiếp.
  Phase C2b = Drill-Chunk/ dùng H10 (không originate) → rename bình thường.
  Phase C5 verification: Drill-Body-Feedback/ + BFP.md = WHITELIST cho H10.
  Drill-Body-Feedback/ SKIP rename: xem §0.4 lý do chi tiết.
```

---

## §6 — NGUỒN NỘI DUNG (Content Sources)

```
PRIMARY (drill origin):
  03-Reward.md §3 — H10 5 preconditions original definition
  04-Integration.md §9 — H10 refined + integrated

REFINEMENT SOURCES:
  Gap-Direction.md v2.0 — "chưa biết = không gap" → Precondition-2a, direction → 1/4
  RSA v2.1 §1.3 — Evaluative/Direct-State × Precondition-1–5 (reference, not copy)
  BFM v2.1 §6.2 — Chunk dynamics × Precondition-1–5 (reference, not copy)
  Cortisol-Baseline v2.0 §3.5 — NT7 direction gate → Precondition-5
  Compile-Taxonomy v1.0 — 4 pathways → Precondition-5 quality ceiling
  Reward-Calibration v1.1 — Goldilocks per-gap → Precondition-4 dynamic zone
  Boredom v2.0 §1 — boredom ≠ Precondition-3 → disambiguation
  Chunk.md v2.2+ §2.6 — 4-metadata context-tag → Precondition-5 expansion

ANALYTICAL (new content):
  §7 Conjunction logic — synthesize from multiple drill insights
  §8 Developmental arc — synthesize from Child-Dev + BFM + RSA
  §9 Dissonance application — NEW analysis (gap identified)
  §10 Honest assessment — consolidate confidence levels
```
