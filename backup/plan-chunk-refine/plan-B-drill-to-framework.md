# Plan B: Drill-to-Framework Integration — R-F1/R-F3 + Standalone Evaluation

```
Status:      ✅ COMPLETE (2026-05-30, Phase B1 status check → 13 DONE, 2 SKIP, 1 SKIP-partial)
Created:     2026-05-30
Scope:       16 R-recommendations + standalone file evaluation
Depends:     KHÔNG bắt buộc phụ thuộc Plan A, nhưng NÊN chạy SAU
Verify:      Mỗi R-item checked (done/skip/execute)
Result:      13/16 DONE (qua sessions trước), 2 SKIP (obsolete), 1 SKIP (partial — mechanism đã ở Core)
             B3 standalone: DECIDED NOT NEEDED (Cortisol-Baseline.md đã cover)
Related:     plan-A-nt-label-rename.md (Track A, ✅ COMPLETE)
```

---

## §0 — BỐI CẢNH

```
  PHÁT HIỆN 2026-05-30:
    → Drill-Chunk/ = 40 files, ~20,000+ lines
    → Chunk/ chỉ có 3 formal files (Chunk.md, Background-Pattern, Compile-Taxonomy)
    → Tỉ lệ formal/drill THẤP NHẤT trong framework
    → NHƯNG: Chunk.md v2.3 ĐÃ INTEGRATE tất cả concepts
    → VẤN ĐỀ: 16 R-recommendations từ drill CHƯA execute ra target files

  GỐC CỦA R-RECOMMENDATIONS:
    → 99-Master-Synthesis.md §5: 10 R-F1-* + 6 R-F3-*
    → Đề xuất update CÁC FILE KHÁC (PFC, Modality, Valence, Education...)
    → Mục đích: propagate drill insights ra framework

  SO SÁNH VỚI CÁC FOLDER KHÁC:
    Body-Feedback/:     12 formal files, ~20,800L
    Agent-Mechanism/:   11 formal files, ~15,900L
    Observation/:       16 formal files, ~26,500L
    Chunk/:              3 formal files,  ~5,400L ← nhưng Chunk.md là unified ref
```

---

## §1 — TRACK B1: R-F1 RECOMMENDATIONS (10 items)

```
  VERIFIED 2026-05-30 — tất cả 10 items checked against current files.

  R-F1-1:  ✅ DONE — PFC-Development.md line 30: "chưa có COMPILED CHUNKS"
  R-F1-2:  ✅ DONE — Child-Development-Mechanism.md lines 348-365 (đơ mặt L2 marker)
           Target gốc "Body-Parenting-Optimization.md" KHÔNG TỒN TẠI → đúng target = Mechanism.md
  R-F1-3:  ✅ DONE — Chunk.md line 109 "Emergent-Binding: 4 concurrent mechanisms" + §2.1
  R-F1-4:  ✅ DONE — Body-Feedback-Precondition.md §3 (1,420L full formalization)
  R-F1-5:  SKIP — Target = Draft file, cross-refs lỗi thời nhanh, low value
  R-F1-6:  ✅ DONE — Self-referential, delivered by 99-Master itself
  R-F1-7:  SKIP — Target gốc KHÔNG TỒN TẠI. 5/8 items DONE (Mechanism.md + Natural-Dev).
           3/8 partial = APPLICATION detail, mechanism đã ở Core (Threat.md, Cortisol-Baseline.md).
  R-F1-8:  ✅ DONE — Agent-Mechanism v2.1 massive rewrite (11 files)
  R-F1-9:  ✅ DONE — Chunk.md line 200 + 827: "NOT 5th modality" explicit
  R-F1-10: ✅ DONE — Chunk.md line 387: "GRADIENT COMPILE" + Compile-Gradient throughout
```

---

## §2 — TRACK B1: R-F3 RECOMMENDATIONS (6 items)

```
  VERIFIED 2026-05-30 — tất cả 6 items checked against current files.

  R-F3-1: SKIP — Concept covered ở Chunk.md §2.3. Modality.md focus encoding, not install
  R-F3-2: ✅ DONE — Chunk.md line 266: "BEYOND 4 internal mechanisms"
  R-F3-3: ✅ DONE — VP v4.1: "4 nguồn" + L0+L1 substrate model fully integrated
  R-F3-4: SKIP — Chunk.md line 750 đã có "Grammar = most versatile (H3)". Minor cross-ref
  R-F3-5: SKIP — Direction A/B OBSOLETE. Logic-Feeling v4.0 dùng Compiled/Fresh axis.
           Concept covered ở Chunk.md §2 (internal vs external compile)
  R-F3-6: ✅ DONE — Education-Mechanism.md v2.0 §2.2 "Direction > Level" = evolved terminology.
           "Direction B" → "External install (Kênh 5)". 4 failure modes distributed
```

---

## §3 — TRACK B2: STANDALONE FILE EVALUATION

```
  CÂU HỎI: Có concept nào DESERVE file riêng bên ngoài Chunk.md?

  CRITERIA CHO STANDALONE FILE:
    ① Cross-file references CAO (>50 occ) — many files need concept
    ② Chunk.md section NGẮN (<50 lines) vs drill content SÂU (>300 lines)
    ③ Concept là BRIDGE giữa nhiều domain (Chunk ↔ Body-Feedback ↔ Feeling)
    ④ Reader benefit: standalone file giúp navigate tốt hơn

  CANDIDATES:

  ★★ NT7 Direction-At-Compile — EVALUATED 2026-05-30
    Verdict: ✅ KHÔNG CẦN STANDALONE
    Lý do: Cortisol-Baseline.md v2.2 (3,059L) ĐÃ COVER extensively:
      → §3.3 Direction-At-Compile gate model (~100+ lines)
      → §7.3 Direction-At-Compile + developmental context
      → 4-threshold, 3 mechanism sources, neural wear = all present
    Chunk.md §2.4 + Cortisol-Baseline.md = đủ depth cho reader

  ★ NT3 Emergent-Binding — MODERATE CANDIDATE
    Cross-file refs:  41 occ
    Chunk.md §1.2:    ~30 lines
    Drill source:     07-Social §6 (~200+ lines)
    Content:
      → 4 concurrent mechanisms: temporal co-occ, multisensory neurons,
        DMN scaffolding, amygdala tagging
      → E12 social smile keystone
      → No single binder module — emergent property
    Verdict: ⚠️ EVALUATE — có thể expand Chunk.md §1.2
      thay vì tạo standalone

  NT6 Label-As-Handle — WEAK CANDIDATE
    Cross-file refs:  90 occ
    Chunk.md §6:      ~60 lines (3 sub-sections)
    PFC-Label.md:     exists (but = vocab reference, different purpose)
    Verdict: KHÔNG cần standalone — §6 đã đủ depth
```

---

## §4 — PHASES

```
  PHASE B1: STATUS CHECK (1 session) — ✅ COMPLETE 2026-05-30
    → ALL 16 R-items checked against current files
    → Result: 13 DONE, 3 SKIP
    → No items need execution

  PHASE B2-B4: SKIPPED — không cần execute (all items DONE or SKIP)

  PHASE B3: NT7 STANDALONE — ✅ DECIDED: KHÔNG CẦN (see §3)
    → Cortisol-Baseline.md v2.2 (3,059L) đã cover extensively

  PHASE B5: VERIFICATION — ✅ COMPLETE 2026-05-30
    → ALL 16 R-items verified (§1 + §2 updated with evidence)
    → ALL 3 standalone candidates evaluated (§3 updated)
    → No execution needed

  TỔNG: 1 session (vs estimated 6-9) — vì phần lớn đã done qua sessions trước

  TỔNG: 6-9 sessions (tùy bao nhiêu R-items cần execute)
```

---

## §5 — DRILL FILE AUDIT SUMMARY (reference cho execution)

```
  CHUNK-INTERNAL-PROCESSING (9 files, ~7,464L):
    00-Internal-Mechanism-Overview.md  (738L)  — F4 territory map
    01-Chunk-Connection-Logical.md     (916L)  — 4-type taxonomy, body vote
    01b-Chunk-Activation-Dynamics.md   (806L)  — CORE: probability, trigger, re-link
    01c-Chunk-Discovery-Lifecycle.md   (1181L) — 7-step cycle, convergence zone
    02-Feeling-Intuition-Gradient.md   (768L)  — H5 mechanism, 6-point gradient
    03-Chain-Anchor-Decay.md           (854L)  — Anchor types, retrieval vs substrate
    04-Right-Wrong-Vague.md            (875L)  — ACC detection, 3 modes
    05-Insight-Tacit-Upgrade.md        (787L)  — Gap 2, Piaget, insight 4-stage
    06-Internal-Synthesis.md           (484L)  — H2/H5/H6/H12 verdicts

    KEY: Tất cả concepts đã INTEGRATE vào Chunk.md v2.3
    → Drill files giữ nguyên = depth reference
    → KHÔNG cần extract thêm

  CHUNK-EXTERNAL-DEVELOPMENT (6 files, ~5,394L):
    00-External-Mechanism.md           (816L)  — 5 install mechanisms, Direction B
    01-External-Synthesis.md           (466L)  — H3/H4/H7/H12 verdicts
    02-Cross-Network-Transfer.md       (1437L) — Analogy 4 risks, mini-gap chain
    Language-Structure-Analysis/:
      01-Natural-Language-Architecture (974L)  — 3 ngôn ngữ, classifier forcing
      02-Mathematical-Language-Arch    (1134L) — Math as modality, notation climb
      03-Musical-Notation-Arch         (567L)  — Music bypasses L2-L3

    KEY: External install đã cover ở Chunk.md §2.3
    → Language-Structure-Analysis = reference (ít cross-file impact)
    → 02-Cross-Network-Transfer: concepts = ASK-AI.md v3.1 foundation

  CHILD-CHUNK-DEVELOPMENT (12 files, ~11,100L+):
    Foundation/:
      00-Chunk-System-Sketch.md        (~650L) — Orientation, 3-layer architecture
      01-PFC-Hardware-Reframe.md       (~900L) — 5 evidence pillars, NT4 PRIMARY
      02-Womb-to-Birth-Baseline.md     (~950L) — Prenatal state, birth moment
    Modality-Arcs/:
      03-Visual-System-Arc.md          (~1900L) — V1-V16 events
      04-Auditory-System-Arc.md        (~2200L) — NT1 PRIMARY, phoneme gradient
      05-Motor-Output-Arc.md           (~1600L) — Gesture-verbal gap
      06a-Interoceptive-Bladder.md     (~2800L) — NT2+NT5+NT7 PRIMARY, đơ mặt
      06b-Interoceptive-Other.md       (~2200L) — Cross-state validation
      07-Social-Recognition-Arc.md     (~2300L) — NT3 PRIMARY, E12 keystone
      08-Verbal-Production-Arc.md      (~2100L) — NT5+NT6 PRIMARY, H11 full
    EN Synthesis:
      09-Event-Chunks-Inference.md     (~890L) — 80+ events master matrix
      10-F1-Synthesis.md               (~890L) — 7 NT verdicts final
    VI versions: mirror of EN (skip)

    KEY: F1 drill = deepest, most files
    → NT PRIMARY homes identified for all 7 NTs
    → PFC-Inference Ladder (5 levels, 10 L2 markers) = novel contribution
    → Tất cả đã integrate vào Chunk.md v2.3

  99-MASTER-SYNTHESIS.MD (1,408L):
    → Unified lifecycle (§1), hypothesis table (§2), contributions (§3)
    → Predictions (§4), R-recommendations (§5), gaps (§6)
    → Chunk.md v2.0 direction (§7)
    → 16 R-recommendations: source of this plan's Track B1
```

---

## §6 — DEPENDENCY MAP

```
  plan-A-nt-label-rename.md
    ↓ (nên chạy trước — rename labels)
  plan-B-drill-to-framework.md (file này)
    ↓ (sau khi R-items done)
  plan-concept-cascade-refine.md (existing, ~27 files)
    ↓ (may overlap — coordinate)
  Generic Label Audit Plans 4-10

  OVERLAP RISK VỚI CONCEPT CASCADE:
    → Concept Cascade refine ~27 files
    → Một số R-items CÓ THỂ đã done qua Cascade
    → Phase B1 (status check) sẽ clarify
```

---

## §7 — HONEST ASSESSMENT

```
  STRENGTHS:
    → Chunk.md v2.3 đã rất tốt — unified reference cover tất cả
    → Drill files organized clean (F1/F3/F4 + synthesis files)
    → R-recommendations well-documented trong 99-Master

  UNCERTAINTIES:
    → Bao nhiêu R-items đã done qua sessions trước? (Phase B1 sẽ clarify)
    → NT7 standalone: cần hay không? (Phase B3 sẽ evaluate)
    → Overlap với Concept Cascade Plan: scope nào thuộc plan nào?

  WHAT THIS PLAN DOES NOT COVER:
    → H11 rename (556 occ) — separate plan
    → H12 rename (145 occ) — separate plan
    → Body-Feedback v3.0 rewrite — separate plan
    → Education restructure — separate plan
    → Generic Label Audit Plans 4-10 — separate plans
```
