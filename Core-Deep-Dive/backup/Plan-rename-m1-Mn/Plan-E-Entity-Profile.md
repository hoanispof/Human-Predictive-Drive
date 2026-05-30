# Plan E — Entity Profile Parameters M1-M5

```
Status:    🔲 NOT STARTED
Created:   2026-05-29
Scope:     1-2 files, ~80 occurrences (MANUAL từng dòng)
Depends:   Plan L xong trước (không bắt buộc, chỉ best practice).
           Chạy TRƯỚC Plan R.
Verify:    grep "\bM5\b" = 0 trong target files
           (M5 chỉ có Entity Profile → 0 = profile fully cleaned)
```

---

## §1 — Hệ M-Label: Entity Profile

Resonance-Per-Entity.md §3 define "3-Tầng per-entity model."
TẦNG 2 (MECHANISM) gồm 5 parameters dùng M1-M5:

```
  M1. Hardware subsidy level (anti-habituation)
  M2. Compilation path (standard / accelerated / skip)
  M3. Cost profile (3-cost: PFC draft + suppress + uncertainty)
  M4. 2-tầng proportion (Hardware-driven A : Self-Pattern-Modeling-driven B)
  M5. 2-luồng proportion (L1 momentary : L2 structural)
```

⚠️ File này CŨNG CHỨA Resonance Decline M1-M4 (§14, D3 columns).
2 hệ thống ĐAN XEN — phải phân biệt TỪNG DÒNG.

---

## §2 — Tên Mới

```
  ┌──────────┬───────────────────────────┬─────────────────────────────────────┐
  │ Hiện tại │ Tên mới                   │ Lý do                               │
  ├──────────┼───────────────────────────┼─────────────────────────────────────┤
  │ M1.      │ ① Hardware subsidy        │ Circled number + tên mô tả          │
  │ M2.      │ ② Compilation path        │ Tên đã có sẵn inline               │
  │ M3.      │ ③ Cost profile            │ Bỏ M-prefix, giữ nội dung          │
  │ M4.      │ ④ 2-tầng proportion       │                                     │
  │ M5.      │ ⑤ 2-luồng proportion      │ M5 unique → dấu hiệu verify        │
  └──────────┴───────────────────────────┴─────────────────────────────────────┘
```

---

## §3 — Phân Biệt 2 Hệ Thống

```
  ┌─────────────────────┬─────────────────────────────────────────────┐
  │ DẤU HIỆU            │ ENTITY PROFILE              │ DECLINE      │
  ├─────────────────────┼─────────────────────────────────────────────┤
  │ Format              │ "M1. Hardware subsidy"      │ "M1 — COMPILED│
  │                     │ (dấu chấm + colon)          │  SUPPRESS"    │
  │                     │                             │ (em-dash)     │
  ├─────────────────────┼─────────────────────────────────────────────┤
  │ Có M5?              │ ✅ CÓ (5 params)            │ ⛔ KHÔNG      │
  │                     │                             │ (chỉ M1-M4)  │
  ├─────────────────────┼─────────────────────────────────────────────┤
  │ Section context     │ §3-§9 (3-tầng mapping)      │ §14 + D3     │
  │                     │ Supply / Mechanism /         │ "Chán" /     │
  │                     │ Dynamics per entity          │ decline /    │
  │                     │                             │ vulnerability│
  ├─────────────────────┼─────────────────────────────────────────────┤
  │ Nội dung kèm theo   │ Hardware subsidy /           │ Compiled     │
  │                     │ Compilation path /           │ suppress /   │
  │                     │ Cost profile /               │ Habituation /│
  │                     │ 2-tầng / 2-luồng            │ Prediction / │
  │                     │                             │ Saturation   │
  └─────────────────────┴─────────────────────────────────────────────┘
```

**Decision tree:**
```
  Dòng có M5? → Entity Profile (chắc chắn)
  Dòng nói về "chán"/decline/vulnerability? → Resonance Decline
  Dòng có dấu chấm "M1." + parameter name? → Entity Profile
  Dòng có em-dash "M1 —" + mechanism name? → Resonance Decline
  Dòng trong §3-§9 S/M/D mapping? → Entity Profile
  Dòng trong §14, §16, D3 column? → Resonance Decline
```

---

## §4 — File Inventory

### File 1: Resonance-Per-Entity.md (MAIN — ~80 Entity Profile occ)

**RENAME sections (Entity Profile M1-M5):**
```
  §3 (lines ~389-436):     5 parameter DEFINITIONS → rename M1.→① ...
  §4 mẹ→con (~463-488):    3-tầng mapping (S1-S3 / M1-M5 / D1-D3)
  §4 con→mẹ:               3-tầng mapping
  §5 bạn thân (~594-622):  3-tầng mapping
  §6 romantic (~646-751):   Phase 1 + Phase 2 mapping
  §8 professional (~816-950): Tool-mode / Therapist / AI mapping
  §9 table (~954-1018):    Consolidated M1-M5 × all entity types
```

**⛔ KHÔNG ĐỘNG (Resonance Decline — Plan R scope):**
```
  §14 (lines ~1241-1307):  Decline M1-M4 definitions (Bond-Architecture §4)
  §4-§8 D3 columns:        "Which decline M1-M4 mechanisms attack?"
                            VD: "M1+M2 không attack" / "M2+M3 HIGH"
  §16 cases (~1375-1451):  Applied decline analysis
  §1-§2 cross-refs:        Decline cross-refs in metadata
```

### File 2: Drill-By-Product-Resonance-Entity.md (VERIFY-AT-EXEC)

```
  Lines ~308-312+: Per-bond M1-M5 profiles
  → Đọc khi thực hiện. Nếu dùng Entity Profile M1-M5 → rename.
  → Nếu chỉ Decline → để cho Plan R.
```

---

## §5 — Thực Hiện

```
  ⚠️ MANUAL TỪNG OCCURRENCE. KHÔNG dùng replace_all.

  1. Read Resonance-Per-Entity.md FULL (nắm toàn bộ context)
  2. §3 definitions (lines ~406-410): rename M1.→①, M2.→②, M3.→③, M4.→④, M5.→⑤
  3. §4-§9 per-entity sections: rename TỪNG DÒNG Entity Profile
     → Check decision tree cho mỗi occurrence
     → D3 columns (decline) → SKIP
  4. §9 comparison table: rename column headers + cells
  5. Read Drill-By-Product-Resonance-Entity.md → rename nếu Entity Profile
  6. Verify (xem §6)
  7. Cập nhật Status → ✅ DONE
```

---

## §6 — Verify

```
  Resonance-Per-Entity.md:
    ✅ grep "\bM5\b" = 0  (M5 chỉ Entity Profile → 0 = fully cleaned)
    ✅ grep "\bM[1-4]\b" → remaining = TẤT CẢ Decline (§14, D3, §16)
       → Đếm: should be ~48-50 occ (chờ Plan R)
    ✅ Spot check: §3 definitions dùng ①②③④⑤
    ✅ Spot check: §9 table dùng ①②③④⑤

  Drill-By-Product-Resonance-Entity.md:
    ✅ grep "\bM5\b" = 0
```

---

## §7 — Edge Cases

```
  ① Trong §4-§8, dòng D3 (Dynamics) hỏi "which M1-M4 mechanisms attack?"
     → ĐÂY LÀ DECLINE, không phải Profile, dù ở TRONG section mapping.
     → SKIP (Plan R scope).

  ② Dòng liệt kê cả Profile lẫn Decline (VD: "M1. Hardware subsidy: MAX
     → M2 habituation slow"):
     → Rename "M1." phần Profile, GIỮA "M2 habituation" phần Decline.
     → Đọc kỹ context.

  ③ Table header nếu dùng "M1" generic column → kiểm tra nội dung column.
     Nếu column chứa parameter values → Entity Profile → rename.
```
