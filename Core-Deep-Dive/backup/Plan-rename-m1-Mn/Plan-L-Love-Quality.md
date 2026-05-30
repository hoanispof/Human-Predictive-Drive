# Plan L — Love Quality Dimensions M1-M4

```
Status:    🔲 NOT STARTED
Created:   2026-05-29
Scope:     1 file, ~6 occurrences
Depends:   KHÔNG. Chạy ĐỘC LẬP. Chạy TRƯỚC Plan R.
Verify:    grep "\bM[1-4]\b" trong Love-Unified §5 (lines ~760-850) = 0
```

---

## §1 — Hệ M-Label: Love Quality Dimensions

Love-Unified.md §5 define "4 Quality Dimensions" cho 6 love types.
Dùng M1-M4 labels KHÁC NGHĨA hoàn toàn với Resonance Decline:

```
  ┌──────────┬───────────────────────────┬───────────────────────────────────┐
  │ Hiện tại │ Nghĩa                     │ So sánh Decline (KHÁC HỆ)        │
  ├──────────┼───────────────────────────┼───────────────────────────────────┤
  │ M1       │ Compiled Quality           │ Decline M1 = Compiled-Suppress   │
  │          │ (empathy accuracy)         │ (suppress gap riêng)             │
  ├──────────┼───────────────────────────┼───────────────────────────────────┤
  │ M2       │ Hardware Seed              │ Decline M2 = Habituation         │
  │          │ (relationship substrate)   │ (Weber-Fechner)                  │
  ├──────────┼───────────────────────────┼───────────────────────────────────┤
  │ M3       │ Calibration Quality        │ Decline M3 = Prediction-Complete │
  │          │ (self-correction capacity) │ (hết novelty)                    │
  ├──────────┼───────────────────────────┼───────────────────────────────────┤
  │ M4       │ Compile Accelerator        │ Decline M4 = Entity-Saturation   │
  │          │ (speed-up factors)         │ (plateau)                        │
  └──────────┴───────────────────────────┴───────────────────────────────────┘
```

---

## §2 — Tên Mới

Tên mô tả ĐÃ CÓ SẴN inline → chỉ cần BỎ M-prefix:

```
  M1 — Compiled QUALITY      → "Compiled Quality" (bỏ "M1 —")
  M2 — HARDWARE SEED         → "Hardware Seed" (bỏ "M2 —")
  M3 — CALIBRATION QUALITY   → "Calibration Quality" (bỏ "M3 —")
  M4 — COMPILE ACCELERATOR   → "Compile Accelerator" (bỏ "M4 —")
```

---

## §3 — File Inventory

### Love-Unified.md (Research/Love-Unified.md)

**RENAME (§5, lines ~760-850):**

```
  Line 766: "M1 — Compiled QUALITY (empathy accuracy):"
            → subsection header → bỏ "M1 — "

  Line 772: "M2 — HARDWARE SEED:"
            → subsection header → bỏ "M2 — "

  Line 780: "M3 — CALIBRATION QUALITY:"
            → subsection header → bỏ "M3 — "

  Line 787: "M4 — COMPILE ACCELERATOR:"
            → subsection header → bỏ "M4 — "

  Line 844: "v1.2 gọi là 'Compile Accelerator' (M2 modifier)"
            → inline reference → "...Compile Accelerator (Hardware Seed modifier)"
            → hoặc context-dependent, đọc khi thực hiện
```

**⛔ KHÔNG ĐỘNG VÀO (Resonance Decline — Plan R scope):**

```
  Lines 1032, 1078-1137: §6.2 M1-M4 Resonance Decline × Love Types
  Lines 1218, 1316:      §7-§8 M1 compiled suppress references
  Line 1703:             Comparison table M1-M4 risk per love type
  Lines 2333-2516:       §14-§16 cross-refs, open questions, changelog
  Lines 18, 52, 208, 218: Metadata/dep-list decline cross-refs
```

---

## §4 — Thực Hiện

```
  1. Read Love-Unified.md lines 750-860 (§5 full context)
  2. Verify: 5 occurrences match expected lines (766/772/780/787/844)
  3. Edit 4 subsection headers: bỏ "M# — " prefix
  4. Edit line 844: fix inline M2 reference → "Hardware Seed"
  5. Verify: grep "\bM[1-4]\b" trong lines 750-860 = 0
  6. Verify: grep "\bM[1-4]\b" trong lines 1000+ = UNCHANGED
  7. Cập nhật Status → ✅ DONE
```

---

## §5 — An Toàn

```
  ① CHỈ sửa lines 760-850 (§5). KHÔNG sửa DƯỚI line 1000.
  ② Nếu phát hiện M-label ngoài 5 expected → DỪNG, verify context.
  ③ Sau khi xong: Love-Unified.md mọi M-labels còn lại = Resonance Decline
     → Plan R sẽ xử lý.
```
