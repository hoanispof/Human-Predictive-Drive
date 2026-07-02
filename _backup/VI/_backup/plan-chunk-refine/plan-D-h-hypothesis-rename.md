# Plan D: H-Hypothesis Labels Rename — H1-H9 + H12

```
Status:      ✅ DONE (2026-05-30)
Created:     2026-05-30
Scope:       10 labels, ~103 occurrences, ~11 active files
Collision:   MODERATE (H1-H9 short patterns → false positives possible)
Depends:     Plan C (H11) ✅ DONE
Verify:      grep "\bH[1-9]\b" + "\bH12\b" = 0 in active files ✅ VERIFIED
             (excluding Drill-*/backup/VI/_backup/)
             Exception: Resonance-Per-Entity.md lines 1535-1540 (research questions, not hypothesis labels)
Estimate:    3-4 sessions → completed in 1 session
Related:     plan-C-h11-rename.md (H11, ✅ DONE)
             backup/plan_rename-abbreviation/plan-h-label-rename.md (old H10 plan)
Bonus:       Fixed corrupted "VEReward-Signal-ArchitectureTILE" → "VERSATILE" in 01-File-Index.md line 86
```

---

## §0 — BỐI CẢNH

```
  H1-H12 = hypothesis system from Chunk drill (99-Master-Synthesis.md §2)
  → 12 hypotheses tested qua 4 drill fronts (F1/F3/F4 + Agent)
  → ALL reached committable confidence (🟡 hoặc 🟡🟢)
  → H labels xuất hiện trong active framework files

  VẤN ĐỀ:
    → "H5" = hypothesis number, reader phải tra drill source
    → "Multi-Weak-Signal-Convergence" tự giải thích
    → Convention: "KHÔNG viết tắt concept"
    → H labels = abbreviations for hypothesis concepts

  PHẠM VI PLAN NÀY: H1-H9 + H12 (10 labels)
  KHÔNG BAO GỒM:
    → H10 (522 occ, 87 files) — separate plan, MUCH larger scope
    → H11 (14 occ, 6 files) — Plan C
```

---

## §1 — ĐỊNH NGHĨA TÊN MỚI

### §1.1 — Naming table

```
  ┌───────┬────────────────────────────────┬──────────────────────────────────────┐
  │ Label │ Tên mới                        │ Nghĩa (from 99-Master §2)           │
  ├───────┼────────────────────────────────┼──────────────────────────────────────┤
  │ H1    │ Chunk-Substrate                │ Chunks = substrate layer của         │
  │       │                                │ cognitive architecture. Feeling,     │
  │       │                                │ Schema, Domain operate on chunks.    │
  ├───────┼────────────────────────────────┼──────────────────────────────────────┤
  │ H2    │ Static-Logical-Linking         │ Type 4 connection: PFC intentional   │
  │       │                                │ hold + body vote. "Thinking = Type 4 │
  │       │                                │ chain." Distinct từ 3 types đã có.  │
  ├───────┼────────────────────────────────┼──────────────────────────────────────┤
  │ H3    │ Grammar-Versatile-Anchor       │ Grammar = most VERSATILE external    │
  │       │                                │ anchor (~100K years refinement).     │
  │       │                                │ Không nhất ở mọi chiều — Math >     │
  │       │                                │ precision, Code > executable.        │
  ├───────┼────────────────────────────────┼──────────────────────────────────────┤
  │ H4    │ Abstract-Metaphysical-Grounding│ Abstract vs Metaphysical differ      │
  │       │                                │ by GROUNDING + MODALITY encoding.    │
  ├───────┼────────────────────────────────┼──────────────────────────────────────┤
  │ H5    │ Multi-Weak-Signal-Convergence  │ "Vague" = multi-weak-signal          │
  │       │                                │ convergence. Expert intuition =      │
  │       │                                │ large database + calibrated signals. │
  │       │                                │ 6-point gradient clear↔vague.        │
  ├───────┼────────────────────────────────┼──────────────────────────────────────┤
  │ H6    │ Anchor-Decay                   │ Chunks need anchor to persist.       │
  │       │                                │ Decay theo Ebbinghaus khi không có   │
  │       │                                │ anchor. 5 anchor types with ranking. │
  ├───────┼────────────────────────────────┼──────────────────────────────────────┤
  │ H7    │ Valence-Chunk-Interaction      │ Valence = chunk × schema interaction,│
  │       │                                │ NOT property of chunk alone.         │
  ├───────┼────────────────────────────────┼──────────────────────────────────────┤
  │ H8    │ Learning-Dissonance-Cycle      │ Learning = cycle (not event). 3      │
  │       │                                │ concurrent signals: reward + fatigue │
  │       │                                │ + dissonance nhẹ. Sleep resolution.  │
  ├───────┼────────────────────────────────┼──────────────────────────────────────┤
  │ H9    │ Agent-Unified-Mechanism        │ Agent-reading = Self-Pattern-Modeling │
  │       │                                │ + Resonance unified. Solo forward    │
  │       │                                │ simulation + emergent mutual.        │
  ├───────┼────────────────────────────────┼──────────────────────────────────────┤
  │ H12   │ Gap2-Language-Evolution        │ Gap 2 drives language evolution      │
  │       │                                │ (coin words for unlabeled            │
  │       │                                │ experiences). Post-verbal bypass.    │
  └───────┴────────────────────────────────┴──────────────────────────────────────┘

  NOTE: Tên mới = EXISTING concept names đã dùng trong framework
  → H5 LUÔN kèm "multi-weak-signal convergence" → drop H5, giữ concept
  → H6 LUÔN kèm "anchor-decay" → drop H6, giữ concept
  → Không phát minh tên mới — chỉ thay provenance label bằng tên đã có
```

### §1.2 — Edge cases

```
  ① GROUPED REFERENCES: "H3/H4/H7" hoặc "H2/H5/H6/H12"
    → Expand each: "Grammar-Versatile-Anchor/Abstract-Metaphysical-Grounding/
       Valence-Chunk-Interaction"
    → DÀI NHƯNG ĐÚNG — self-documenting

  ② RANGE NOTATION: "H1-H12" (Chunk.md line 1387)
    → "TOTAL: 15 hypothesis entries (H1-H12 + 7 verdicts)"
    → REWRITE: "TOTAL: 15 hypothesis entries (12 main hypotheses + 7 verdicts)"
    → OR keep "H1-H12" as system reference (acceptable exception since
       it refers to the NUMBERING SYSTEM, not individual hypotheses)

  ③ COMPOUND "H12p" (Chunk.md line 1420)
    → "H12p" = H12 partial verdict
    → Rename: "Gap2-Language-Evolution-partial" hoặc "Gap2-Language-Evolution (partial)"

  ④ PAIRED "H1/H11" (4 locations)
    → Plan C handles H11 → "H1/Receptive-Productive-Asymmetry"
    → Plan D renames remaining H1 → "Chunk-Substrate/Receptive-Productive-Asymmetry"

  ⑤ REDUNDANT REPETITION: "H5 multi-weak-signal convergence"
    → Drop H5, keep concept: "Multi-Weak-Signal-Convergence"
    → Section titles like "### 7.3 H5: 'Vague' = Multi-Weak-Signal Convergence"
      → "### 7.3 Multi-Weak-Signal-Convergence"
```

---

## §2 — FILE INVENTORY (per-label, per-file)

### §2.1 — H5: Multi-Weak-Signal-Convergence (51 occ, 8 files) ← LARGEST

```
  ⭐ H5 chiếm ~50% total workload của Plan D

  File A: Core-Deep-Dive/Body-Base/Feeling/Feeling.md (12 occ)
    Lines: 71, 876, 1148, 1188, 1199, 1202, 1254, 1561, 1831, 1978, 2009, 2171
    Patterns:
      "§7 — FEELING GRADIENT: Clear ↔ Vague (H5 + Convergence Zone)"
      "### 7.3 H5: 'Vague' = Multi-Weak-Signal Convergence"
      "⭐ H5 — HYPOTHESIS TRUNG TÂM:"
      "H5 multi-weak-signal convergence" (multiple)
      "H5 multi-weak-signal" (shorthand)

  File B: Core-Deep-Dive/Body-Base/Feeling/Feeling-Mechanism-Deep-Draft.md (15 occ)
    Lines: 18, 548, 988, 1038, 1055, 1058, 1067, 1123, 1265, 1272, 1279,
           1425, 1469, 1568, 1626
    Patterns: same as Feeling.md — dense usage throughout

  File C: Core-Deep-Dive/Body-Base/Feeling/Body-Knowing.md (7 occ)
    Lines: 914, 942, 1083, 1088, 1351, 1555, 1985
    Patterns:
      "H5 multi-weak-signal convergence (Feeling.md §7.3)"
      "### §5.4 — Mechanism: H5 + Convergence Zone"
      "H5 MULTI-WEAK-SIGNAL CONVERGENCE (Feeling.md §7.3):"

  File D: Core-Deep-Dive/Body-Base/Chunk/Chunk.md (7 occ)
    Lines: 574, 938, 1189, 1276, 1356, 1427, 1587
    Patterns:
      "🟡 H5 SUPPORTED (F4 02):"
      "= H5 multi-weak-signal convergence at concept level"
      "6-point feeling-intuition gradient (H5)"
      "02 → H5 feeling-intuition gradient (🟡)"

  File E: Core-Deep-Dive/Body-Base/Feeling/Feeling-Literacy-Training-Draft.md (4 occ)
    Lines: 20, 214, 927, 1793

  File F: Core-Deep-Dive/Body-Base/Feeling/Feeling-Chunk-Bridge-Draft.md (2 occ)
    Lines: 20, 434

  File G: Core-Deep-Dive/PFC/Imagination/Somatic-Articulation-Loop.md (1 occ)
    Line 2702: "§7: Feeling gradient clear↔vague (H5, convergence zone = felt sense)"

  File H: Core-Deep-Dive/01-File-Index.md (3 occ)
    Lines: 79, 81, 83
    Pattern: "H5: Spectrum feeling → intuition → hunch"
```

### §2.2 — H9: Agent-Unified-Mechanism (12 occ, 1 file)

```
  File: Core-Deep-Dive/Body-Base/Chunk/Agent-Mechanism/Agent-Mechanism.md

  Lines: 119, 135, 143, 145, 326, 1257, 1336, 1345, 1987, 2176, 2312, 2352

  Patterns:
    "§0 — Thesis + H9"
    "§0.1 — H9 Hypothesis (v2.0 unified)"
    "§9 — Gradient validation (H9 evidence)"
    "H9 falsified if:"
    "§16 — H9 falsifiable predictions (12 predictions)"
    "H9 core (unified mechanism): 🟢 Consistent"
    Changelog: "H9 falsifiable predictions (10 → 12)"

  ⚠️ NOTE: Agent-Mechanism.md IS essentially "the H9 file" — toàn bộ file
     formalize hypothesis H9. Nên:
     → "§0.1 — H9 Hypothesis" → "§0.1 — Agent-Unified-Mechanism Hypothesis"
     → "H9 falsifiable predictions" → "Agent-Unified-Mechanism predictions"
     → "H9 falsified if" → "Agent-Unified-Mechanism falsified if"
```

### §2.3 — H1: Chunk-Substrate (9 occ, 5 files)

```
  File: Chunk.md (3 occ)
    Line 81:   "(H1 🟡🟢)" → "(Chunk-Substrate 🟡🟢)"
    Line 1387: "(H1-H12 + 7 verdicts)" → REWRITE (see §1.2 edge case ②)
    Line 1391: "(H1 substrate, ...)" → "(Chunk-Substrate, ...)"

  File: Agent-Mechanism.md (2 occ)
    Line 172: "supports H1 (chunk = substrate)" → "supports Chunk-Substrate hypothesis"
    Line 205: "contradicts H1 unified chunk" → "contradicts Chunk-Substrate"

  File: 01-File-Index.md (1 occ)
    Line 63: "H1/H11" → "Chunk-Substrate/Receptive-Productive-Asymmetry"
             (hoặc "Chunk-Substrate/H11" nếu Plan C chưa chạy)

  File: Child-Development-Mechanism.md (2 occ)
    Lines 30, 2531: "H1/H11" → paired references

  File: Natural-Development.md (1 occ)
    Line 2366: "H1/H11" → paired reference
```

### §2.4 — H2: Static-Logical-Linking (8 occ, 2 files)

```
  File: Chunk.md (6 occ)
    Line 471:  "🟡 H2 SUPPORTED (F4 01):" → "🟡 Static-Logical-Linking SUPPORTED (F4 01):"
    Line 486:  "Linking (H2)" → "Static-Logical-Linking"
    Line 521:  "TYPE 4 — STATIC LOGICAL LINKING (H2 🟡):" → drop "(H2 🟡)" hoặc keep as reference
    Line 1343: "4-type connection taxonomy (H2)" → "4-type connection taxonomy (Static-Logical-Linking)"
    Line 1424: "01 → H2 4-type connections (🟡)" → "01 → Static-Logical-Linking 4-type connections (🟡)"
    Line 1581: "§3: 4-type connection taxonomy (H2)" → same pattern

  File: 01-File-Index.md (2 occ)
    Lines 76, 83: references to drill file descriptions containing "H2"
```

### §2.5 — H3: Grammar-Versatile-Anchor (6 occ, 2 files)

```
  File: Chunk.md (3 occ)
    Line 729:  "(H3: 'jack..." → "(Grammar-Versatile-Anchor: 'jack..."
    Line 750:  "(H3 — ~100K years)" → "(Grammar-Versatile-Anchor — ~100K years)"
    Line 1420: "H3 🟡 + H4 🟡 + H7 🟡 + H12p 🟡" → expand ALL (see §1.2 edge ①)

  File: 01-File-Index.md (3 occ)
    Lines 85, 86, 88: references containing "H3"
```

### §2.6 — H6: Anchor-Decay (6 occ, 2 files)

```
  File: Chunk.md (4 occ)
    Line 709:  "🟡 H6 SUPPORTED WITH REFINEMENT (F4 03):" → "🟡 Anchor-Decay SUPPORTED..."
    Line 756:  "🟡 H6 REFINEMENT:" → "🟡 Anchor-Decay REFINEMENT:"
    Line 1428: "03 → H6 anchor-decay (🟡)" → "03 → Anchor-Decay (🟡)"
    Line 1583: "§5: Anchor-decay model (H6)" → "§5: Anchor-Decay model"

  File: 01-File-Index.md (2 occ)
    Lines 80, 83
```

### §2.7 — H12: Gap2-Language-Evolution (5 occ, 2 files)

```
  File: Chunk.md (3 occ)
    Line 956:  "🟡 H12: Gap 2 drives language evolution" → "🟡 Gap2-Language-Evolution:"
    Line 1387: "H1-H12" range → REWRITE (§1.2 edge ②)
    Line 1430: "05 → H12 insight + tacit + Gap 2 (🟡)" → "05 → Gap2-Language-Evolution + insight + tacit (🟡)"

  File: 01-File-Index.md (2 occ)
    Lines 82, 83
```

### §2.8 — H4, H7, H8: Low-count labels (2 occ each)

```
  H4: Abstract-Metaphysical-Grounding
    Chunk.md line 1420: "(H4 🟡)" → part of grouped reference
    01-File-Index.md line 85: "H3/H4/H7" → expand

  H7: Valence-Chunk-Interaction
    Chunk.md line 1420: "(H7 🟡)" → part of grouped reference
    01-File-Index.md line 85: "H3/H4/H7" → expand

  H8: Learning-Dissonance-Cycle
    Chunk.md line 1434: "H8 learning cycle" → "Learning-Dissonance-Cycle"
    01-File-Index.md line 60: "H8: learning = chu kỳ..." → "Learning-Dissonance-Cycle: learning = chu kỳ..."
```

---

## §3 — FALSE POSITIVES (⚠️ CRITICAL)

```
  ⚠️ Resonance-Per-Entity.md lines 1535-1540:

  "🔴 HYPOTHESIS (insufficient data)"
    H1. Exact Reward-Signal-Architecture Evaluative:Direct-State ratios...
    H2. Exact "existence-based gap" neural mechanism...
    H3. Tool→Agent threshold...
    H4. "Click" → sustained resonance prediction accuracy
    H5. AI impact on human resonance landscape...
    H6. Phantom resolution timeline per entity type...

  → "H1." through "H6." = NUMBERED LIST for research questions
  → KHÔNG PHẢI hypothesis H1-H6 references
  → PHẢI SKIP — do NOT rename

  DETECTION: Pattern "H[1-6]." (with period) in Resonance-Per-Entity.md
  PREVENTION: Manual per-file review, NOT blind replace_all
```

---

## §4 — WHITELIST (KHÔNG thay)

```
  ① Drill-Chunk/          — H labels are HOME here (source of hypotheses)
  ② Drill-Body-Feedback/  — drill files reference H8, H9, H10
  ③ Drill-Reward-Feeling/ — drill files
  ④ Drill-Bond-Architecture/ — drill files (if exists)
  ⑤ backup/               — skip
  ⑥ VI/                   — skip
  ⑦ _backup/              — skip
  ⑧ plan-*.md files       — references OK to rename or skip (low priority)

  ALSO SKIP:
  ⑨ Resonance-Per-Entity.md lines 1535-1540 — FALSE POSITIVES (§3)
```

---

## §5 — EXECUTION PHASES

### Phase 1: H5 — Feeling/ folder (1.5 sessions)

```
  WHY FIRST: H5 = 51 occ = ~50% of total work
  
  Session 1A: Feeling.md (12 occ) + Body-Knowing.md (7 occ)
    → 19 replacements, manual review each
    → Pattern: mostly "H5 multi-weak-signal convergence" → "Multi-Weak-Signal-Convergence"
    → Drop redundant "H5 " prefix where concept name follows

  Session 1B: Feeling-Mechanism-Deep-Draft.md (15 occ)
              + Feeling-Chunk-Bridge-Draft.md (2 occ)
              + Feeling-Literacy-Training-Draft.md (4 occ)
              + Somatic-Articulation-Loop.md (1 occ)
    → 22 replacements

  VERIFY Phase 1: grep "\bH5\b" in active Feeling/ files = 0
```

### Phase 2: H9 — Agent-Mechanism.md (1 session)

```
  12 occ trong 1 file
  → Section headers, predictions, status markers
  → All straightforward: "H9" → "Agent-Unified-Mechanism"
  → Agent-Mechanism.md IS the H9 hypothesis file

  VERIFY Phase 2: grep "\bH9\b" in Agent-Mechanism.md = 0
```

### Phase 3: H1+H2+H3+H6+H12 — Chunk.md + 01-File-Index.md (1 session)

```
  Chunk.md: H1(3) + H2(6) + H3(3) + H6(4) + H12(3) = 19 occ
  01-File-Index.md: H1(1) + H2(2) + H3(3) + H6(2) + H12(2) + H4(1) + H5(3) + H7(1) + H8(1) = 16 occ
  → 35 replacements across 2 files

  ⚠️ TRỌNG ĐIỂM:
    → Chunk.md line 1387 "H1-H12" range → REWRITE
    → Chunk.md line 1420 "H3 🟡 + H4 🟡 + H7 🟡 + H12p 🟡" → expand ALL
    → 01-File-Index.md: multiple grouped refs → expand

  VERIFY Phase 3: grep "\bH[1-9]\b" + "\bH12\b" in Chunk.md + 01-File-Index = 0
                  (excluding Drill-Chunk/ file descriptions in 01-File-Index
                   that REFERENCE drill content)
```

### Phase 4: H1 paired refs + H4+H7+H8 remaining (0.5 session)

```
  Child-Development-Mechanism.md: H1 via "H1/H11" pairs (2 occ)
  Natural-Development.md: H1 via "H1/H11" pair (1 occ)
  H4, H7, H8 remaining: 01-File-Index only (already done in Phase 3)

  VERIFY Phase 4: grep "\bH[1-9]\b" + "\bH12\b" across ALL active files = 0
```

### Final Verification

```
  FULL SWEEP:
    grep "\bH[1-9]\b" + "\bH1[012]\b" excluding Drill-*/backup/VI/_backup/
    → Expected: 0 (active files)
    → EXCEPTION: Resonance-Per-Entity.md lines 1535-1540 (numbered list, false positives)
       → These use "H[1-6]." pattern — consider renaming to "Q1."-"Q6." to
         eliminate confusion permanently (OPTIONAL)
```

---

## §6 — DEPENDENCY MAP

```
  Plan A (NT rename) ✅ DONE
    ↓
  Plan B (drill-to-framework) ✅ DONE
    ↓
  Plan C (H11 rename, 14 occ) ← NÊN chạy trước Plan D
    ↓
  Plan D (H1-H9+H12, ~103 occ) ← file này
    ↓ (independent)
  Plan H10 (Body-Signal-Precondition, ~522 occ) ← separate, MUCH larger
    ↓
  Generic Label Audit Plans 4-10 (~7,600 occ)

  INTERNAL DEPENDENCIES:
    → Phase 1 (H5) → Phase 2 (H9) → Phase 3 (multi-label Chunk.md) → Phase 4 (H1 pairs)
    → Sequential vì Phase 3 touches Chunk.md which Phase 1 may also touch (H5 in Chunk.md)
    → CAN reorder phases nếu cần — không có hard dependency giữa phases
    → CHỈ CẦN Phase 3+4 chạy SAU Plan C (để "H1/H11" pairs resolved)
```

---

## §7 — HONEST ASSESSMENT

```
  STRENGTHS:
    → H labels đều ĐÃ CÓ concept names trong framework — chỉ drop provenance label
    → ~103 occ manageable scope (so với H10: 522, generic audit: 7,600)
    → Collision risk identified và documented (Resonance-Per-Entity false positives)
    → Phasing cho phép validate từng bước

  CHALLENGES:
    → H5 (51 occ) cần manual review — KHÔNG thể blind replace_all
      vì pattern varies: "H5 multi-weak-signal", "H5 SUPPORTED", "(H5)", "H5:"
    → Grouped references "H3/H4/H7" become LONG khi expand
    → "H1-H12" range notation → rewrite strategy needed
    → 01-File-Index.md describes Drill-Chunk/ files — renaming H labels
      in INDEX but not in DRILL FILES creates asymmetry
      → ACCEPTABLE: Index là reader entry point, nên dùng readable names
      → Drill files giữ H labels vì đó là provenance system của drill

  UNCERTAINTIES:
    → H9 trong Agent-Mechanism.md: "Agent-Unified-Mechanism" là tên tốt nhất?
      → Alternative: "Core-Thesis" (ngắn hơn, vì reader ĐÃ Ở TRONG Agent-Mechanism file)
      → Decide during Phase 2 execution
    → 01-File-Index.md: rename H labels in DRILL FILE DESCRIPTIONS?
      → YES — index serves framework readers, not drill system
      → Drill files themselves keep H labels

  RISK MITIGATION:
    → Manual review EVERY occurrence — no blind replace_all
    → Verify per-phase with grep
    → Spot-check 3 files after each phase for readability

  WHAT THIS PLAN DOES NOT COVER:
    → H10 rename (522 occ) — separate plan
    → H11 rename — Plan C
    → R-F labels in Chunk.md §13 — kept intentionally (reference drill contracts)
    → Drill-Chunk/ internal labels — kept (provenance system)
    → "P-H5-2" prediction labels in drill files — kept (drill internal)
```
