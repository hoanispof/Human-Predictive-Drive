# Plan: S-Stream Rename — S1/S2 Streams + Dunbar S1-S6 → Descriptive Names

```
Status:    🔲 NOT STARTED
Created:   2026-05-23
Scope:     ~7 files for Streams (~156 occ) + Dunbar in ~10 files
Approach:  MANUAL (too many colliding S-meanings for replace_all)
Depends:   KHÔNG. Chạy ĐỘC LẬP.
Verify:    All "S1"/"S2" in Agent-Mechanism context = renamed
Special:   "S" has 6 DIFFERENT MEANINGS — mostly manual work
```

---

## §0 — TẠI SAO ĐỔI TÊN

```
  "S1" trong Agent-Mechanism.md — nghĩa gì?
  → S1 = Hardware-Stream? S1 = Dunbar layer 1? S1 = Drill session 1?
  → CÙNG FILE có CẢ 3 nghĩa!

  6 nghĩa của "S1" / "S2":
  ① Stream 1/2 (Resonance Architecture) — concept name → ĐỔI
  ② Dunbar S1-S6 (social circle layers) — concept name → ĐỔI
  ③ Somatosensory S1/S2 (brain regions) — neuroscience term → GIỮ
  ④ Session S1-S12 (drill sessions) — provenance marker → GIỮ
  ⑤ Phase S1/S2 (plan execution) — local labels → GIỮ
  ⑥ Schema S1/S2 (open questions) — local labels → GIỮ
```

---

## §1 — ĐỊNH NGHĨA TÊN MỚI

### §1.1 — Streams (Agent-Mechanism 2-Stream Architecture)

```
  Source: Agent-Mechanism.md v2.1 §4.2

  ┌──────────┬─────────────────────┬──────────────────────────────────┐
  │ Hiện tại │ Tên mới             │ Cơ chế                           │
  ├──────────┼─────────────────────┼──────────────────────────────────┤
  │ S1       │ Hardware-Stream     │ Unidirectional. Each side gets   │
  │ Stream 1 │                     │ reward INDEPENDENTLY. No mutual  │
  │          │                     │ engagement needed. HABITUATES.   │
  ├──────────┼─────────────────────┼──────────────────────────────────┤
  │ S2       │ Modeling-Stream     │ Self-Pattern-Modeling compiled   │
  │ Stream 2 │                     │ mutual (bidirectional). Both     │
  │          │                     │ engage. Feedback loop. ANTI-     │
  │          │                     │ HABITUATION (Hebbian).           │
  └──────────┴─────────────────────┴──────────────────────────────────┘

  Formulas:
  → "S1+S2 strong" → "Hardware-Stream+Modeling-Stream strong"
  → "S1 habituates, S2 atrophies" → "Hardware-Stream habituates, Modeling-Stream atrophies"
  → "S1 only" → "Hardware-Stream only"
```

### §1.2 — Dunbar Layers (secondary)

```
  Source: Agent-Mechanism.md v2.1 (cross-ref Dunbar 1992-2024)

  ┌──────────┬─────────────────────┬──────────────────────────────────┐
  │ Hiện tại │ Tên mới             │ Nghĩa                            │
  ├──────────┼─────────────────────┼──────────────────────────────────┤
  │ S1       │ Dunbar-Intimate     │ ~5 entities (inner circle)       │
  │ S2       │ Dunbar-Close        │ ~15 entities                     │
  │ S3       │ Dunbar-Friend       │ ~50 entities                     │
  │ S4       │ Dunbar-Acquaintance │ ~150 entities (Dunbar number)    │
  │ S5       │ Dunbar-Known        │ ~500 entities                    │
  │ S6       │ Dunbar-Recognized   │ ~1500 entities                   │
  └──────────┴─────────────────────┴──────────────────────────────────┘

  ⚠️ Dunbar labels CẦN VERIFY exact definitions trước khi rename.
  → Đọc Agent-Mechanism.md section chứa Dunbar references.
```

---

## §2 — APPROACH

```
  ⭐ 100% MANUAL — không thể replace_all vì 6 nghĩa collision

  Per file:
  ① Đọc full file context
  ② Identify mỗi "S1"/"S2" thuộc system nào
  ③ Rename chỉ Stream + Dunbar occurrences
  ④ GIỮ NGUYÊN: session numbers, phase labels, neuroscience S1/S2

  Files cần xử lý (Streams): ~7 files
  → Agent-Mechanism.md (source, ~21 occ — MIXED Streams + Dunbar)
  → Background-Pattern.md, Connection.md, Love-Romantic.md,
     Love-Unified.md, Body-Coupling.md, Empathy.md

  → 2 sessions (source + consumers)
```
