# Plan: NT-Label Rename — NT1-NT7 → Descriptive Names

```
Status:    🔲 NOT STARTED
Created:   2026-05-23
Scope:     ~50 active files, ~319 replacements
Approach:  FOCUS on cross-file NTs (NT4, NT6, NT7) → then local NTs
Depends:   KHÔNG. Chạy ĐỘC LẬP.
Verify:    grep "\bNT[0-9]\b" = 0 trong active files
Special:   Many NTs already appear WITH inline description
```

---

## §0 — TẠI SAO ĐỔI TÊN

```
  "NT7" — New Thesis 7 — ai biết thesis gì?
  → Phải tra 99-Master-Synthesis.md hoặc Chunk.md

  "Direction-At-Compile" — ngay lập tức hiểu:
  → Body-state direction (novelty vs threat) được tag lúc compile

  NT labels là PROVENANCE MARKERS từ Chunk drill.
  → Đã trở thành CONCEPT NAMES cross-file → đáng có tên riêng.
```

---

## §1 — ĐỊNH NGHĨA TÊN MỚI

```
  Source: 99-Master-Synthesis.md, Chunk.md

  ┌──────────┬───────────────────────────┬──────────────────────────────┐
  │ Hiện tại │ Tên mới                   │ Nghĩa                        │
  ├──────────┼───────────────────────────┼──────────────────────────────┤
  │ NT1      │ Compile-Gradient          │ Compilation is gradient, not │
  │          │                           │ discrete. Proto-chunks = weak│
  │          │                           │ chunks.                      │
  ├──────────┼───────────────────────────┼──────────────────────────────┤
  │ NT2      │ Compile-4-Channel         │ 4-channel × 5-parameter rate │
  │          │                           │ formula for compilation.     │
  ├──────────┼───────────────────────────┼──────────────────────────────┤
  │ NT3      │ Emergent-Binding          │ Multi-modal binding = 4      │
  │          │                           │ concurrent mechanisms. No    │
  │          │                           │ single binder module.        │
  ├──────────┼───────────────────────────┼──────────────────────────────┤
  │ NT4      │ PFC-From-Birth            │ PFC hardware online from     │
  │          │                           │ prenatal. Developmental      │
  │          │                           │ behavior = chunks-missing,   │
  │          │                           │ NOT hardware-missing.        │
  ├──────────┼───────────────────────────┼──────────────────────────────┤
  │ NT5      │ Receptive-Productive-Gap  │ = H11. Productive bundle ≈   │
  │          │                           │ 3× receptive. Rename cùng   │
  │          │                           │ H11 (plan-h-label-rename).   │
  ├──────────┼───────────────────────────┼──────────────────────────────┤
  │ NT6      │ Label-As-Handle           │ Verbal labels = retrieval    │
  │          │                           │ path + symbolic compression. │
  │          │                           │ NOT 5th modality.            │
  ├──────────┼───────────────────────────┼──────────────────────────────┤
  │ NT7      │ Direction-At-Compile      │ Body-state DIRECTION (novelty│
  │          │                           │ vs threat) determines chunk  │
  │          │                           │ association tag at compile.  │
  └──────────┴───────────────────────────┴──────────────────────────────┘
```

---

## §2 — PRIORITY

```
  CROSS-FILE (High priority — appear outside Chunk/ folder):
  ⭐ NT7 (Direction-At-Compile): Cortisol-Baseline, Protect, Quote-Analysis, Logic-Planning
  ⭐ NT4 (PFC-From-Birth): Core-Hardware, Core-Software
  ⭐ NT6 (Label-As-Handle): Modality references, Feeling files

  LOCAL (Lower priority — mostly within Chunk/ subfolders):
  → NT1, NT2, NT3 — primarily Chunk.md + Chunk-Internal/External files
  → NT5 — same as H11, shared plan

  → S1: Cross-file NTs (NT4, NT6, NT7)
  → S2: Local NTs (NT1-NT3, NT5) + Chunk/ files
  → S3: Verification sweep
```

---

## §3 — REPLACE APPROACH

```
  NT labels are SHORT + UNIQUE → replace_all SAFE in most files.

  Per file:
  Pass 1: "NT7" → "Direction-At-Compile"
  Pass 2: "NT4" → "PFC-From-Birth"
  Pass 3: "NT6" → "Label-As-Handle"
  (etc. for NT1-NT3)

  ⚠️ CHECK: "NT" inside other words?
  → "NTrk" (neurotrophic receptor)? Unlikely in framework files.
  → "\bNT[0-9]\b" word-boundary → SAFE for replace_all

  ⚠️ REDUNDANCY after rename:
  → "NT7 direction tag" → "Direction-At-Compile direction tag"
  → Sửa: "Direction-At-Compile" (bỏ "direction tag" redundant)
```

---

## §4 — FILE INVENTORY (tóm tắt)

```
  ~50 active files, ~319 occurrences.
  Mostly in Chunk/ ecosystem + scattered cross-refs.

  HEAVY: 99-Master-Synthesis.md, Chunk.md, Child-Chunk-Dev files
  LIGHT: 1-4 occ in Research, Observation, PFC files

  → 3 sessions (cross-file NTs → local NTs → verification)
```
