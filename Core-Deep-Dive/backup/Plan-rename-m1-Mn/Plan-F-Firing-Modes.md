# Plan F — Firing Modes M1-M4

```
Status:    🔲 NOT STARTED
Created:   2026-05-29
Scope:     3-4 files, ~30 occurrences
Depends:   Plan L + E xong trước (không bắt buộc, chỉ best practice).
           Chạy TRƯỚC Plan R.
Verify:    Firing-mode sections: no M-labels
           Cross-refs SAI → đã fix hoặc xóa
```

---

## §1 — Hệ M-Label: 2 Firing Mode Taxonomies

Framework có 2 taxonomy firing modes dùng M1-M4, + 1 canonical KHÔNG dùng M:

### ③ Body-Base + Discovery (Intensity/Pattern)

```
  M1 Tonic:     low-intensity, liên tục, duy trì baseline
  M2 Phasic:    burst cụ thể, response to event
  M3 Compound:  nhiều hệ fire ĐỒNG THỜI (VD: reunion = oxytocin+dopamine+opioid)
  M4 Cascade:   1 event trigger chain nhiều systems theo thứ tự
```

### ④ Domain-Mapping-Drive (BUILD step pattern)

```
  M1 Structural:     baseline, steady, low-resource (routine practice)
  M2 Current-Shift:  medium, VTA fire khi có delta (learning new)
  M3 Peak:           high, opioid+dopamine cùng fire (breakthrough "aha")
  M4 Compound:       mixed valence, nhiều systems cùng fire (complex tasks)
```

### Valence-Propagation §6 — CANONICAL (KHÔNG dùng M-label)

```
  Mode 1: Maintenance      entity PRESENT → routine fire → baseline invisible
  Mode 2: Chunk-Miss        entity ABSENT → misfires → pain
  Mode 3: Context-Trigger   entity ABSENT + cue → spoke activation
```

### ⭐ QUAN HỆ GIỮA 3 TAXONOMY

```
  VP 3-mode: KHI NÀO Entity-Compiled valence fire (presence state)
  ③ 4-mode:  CƯỜNG ĐỘ/PATTERN neurochemical fire (intensity)
  ④ 4-mode:  PATTERN per BUILD step trong domain-mapping
  → ORTHOGONAL (khác chiều) — KHÔNG conflict concept
  → CHỈ conflict LABEL M1-M4

  Quyết định: GIỮA ③④ là taxonomy riêng (KHÔNG merge vào VP).
  → Bỏ M-prefix, giữ tên mô tả.
```

---

## §2 — Tên Mới

BỎ M-prefix, giữ tên mô tả (đã có sẵn inline):

```
  ③ Body-Base + Discovery:
    M1 Tonic     → Tonic            (hoặc "Tonic mode")
    M2 Phasic    → Phasic           (hoặc "Phasic mode")
    M3 Compound  → Compound         (hoặc "Compound mode")
    M4 Cascade   → Cascade          (hoặc "Cascade mode")
    "M1-M4"      → "4 firing modes" (hoặc "Tonic/Phasic/Compound/Cascade")

  ④ Domain-Mapping-Drive:
    M1 Structural     → Structural
    M2 Current-Shift  → Current-Shift
    M3 Peak           → Peak
    M4 Compound       → Compound
    "M1-M4"           → "4 firing modes"
```

---

## §3 — File Inventory + Cross-ref SAI

### File 1: Body-Base.md (~8 firing-mode occ)

```
  ⚠️ FIRING MODE OCCURRENCES:

  Line 777-782 — §5.3 DEFINITION:
    "M1-M4: 4 FIRING MODES (Bond-Architecture.md v1.0):"
    "→ M1 Tonic: low-intensity, liên tục, duy trì baseline"
    "→ M2 Phasic: burst cụ thể, response to event"
    "→ M3 Compound: nhiều hệ fire ĐỒNG THỜI"
    "→ M4 Cascade: 1 event trigger chain"
    → RENAME: bỏ M-prefix
    → ⛔ CROSS-REF SAI: "(Bond-Architecture.md v1.0)" — Bond-Arch §4 = Decline!
       → XÓA cross-ref Bond-Architecture HOẶC trỏ đúng nơi

  Line 1294 — §11 Confidence:
    "⚠ M1-M4 firing modes (neurochemistry 🟢, 4-mode taxonomy = 🟡)"
    → RENAME: "4 firing modes (Tonic/Phasic/Compound/Cascade)"

  Lines 59, 70 — Dep-list:
    "Body-Coupling.md v3.0 — ... M1-M4"
    "Bond-Architecture.md v1.0 — ... M1-M4"
    → PHÂN BIỆT:
       Nếu dep-list nói firing modes → fix nhãn
       Nếu dep-list nói decline cross-ref → ĐỂ cho Plan R

  Lines 1119, 1323, 1345 — §10/§12 cross-refs:
    "M1-M4" trong reading guide / cross-ref list
    → PHÂN BIỆT context: firing vs decline per occurrence

  Line 1423 — Final summary:
    "§5: L0-L1 substrate + Hardware Subsidy + M1-M4 firing modes"
    → "... + 4 firing modes (Tonic/Phasic/Compound/Cascade)"

  Line 1466 — Changelog:
    "§5.3: +Hardware Subsidy mechanism, +M1-M4 firing modes"
    → "... +4 firing modes"
```

### File 2: Discovery-vs-Expansion.md (~11 occ, ALL firing mode)

```
  Line 1036-1041 — DEFINITION:
    "M1-M4 × DISCOVERY (Bond-Architecture.md v1.0):"
    "M1 Tonic: background exploration → SENSE phase"
    "M2 Phasic: focused burst → VERIFY phase"
    "M3 Compound: multi-system convergence → EUREKA"
    "M4 Cascade: chain breakthroughs → PARADIGM SHIFT"
    → RENAME: bỏ M-prefix
    → ⛔ CROSS-REF SAI: "(Bond-Architecture.md v1.0)" → FIX

  Line 1042: "Discovery = primarily M1 (sense) + M2 (verify)"
    → "Discovery = primarily Tonic (sense) + Phasic (verify)"

  Line 1043: "Scale = primarily compiled (no M1-M4 needed)"
    → "Scale = primarily compiled (no firing modes needed)"

  Line 5, 18: YAML + dep-list
    → Fix "M1-M4" → "4 firing modes"
    → Fix "Bond-Architecture.md v1.0 — M1-M4 firing modes" cross-ref

  Line 1019: "Bond-Architecture.md v1.0: M1-M4 firing modes" → FIX
  Line 1055: "🟡 M1-M4 × discovery" → "🟡 4 firing modes × discovery"
```

### File 3: Domain-Mapping-Drive.md (~6 firing-mode occ)

```
  Lines 936-951 — DEFINITION:
    "M1-M4 Firing Modes — Mỗi BUILD step fire ở 1 trong 4 modes:"
    "M1 (Structural) — baseline, steady, low-resource"
    "M2 (Current-Shift) — medium, VTA fire khi có delta"
    "M3 (Peak) — high, opioid+dopamine cùng fire"
    "M4 (Compound) — mixed valence, nhiều systems cùng fire"
    → RENAME: bỏ M-prefix

  Line 950: "bị locked ở M1 hoặc crash"
    → "bị locked ở Structural mode hoặc crash"

  Line 951: "→ Xem Bond-Architecture.md v1.0 §M1-M4"
    → ⛔ CROSS-REF SAI → XÓA hoặc trỏ đúng nơi

  Line 47: Changelog "M1-M4" → "4 firing modes"

  Line 3568: Dep-list "Bond-Architecture.md v1.0 (4 bond types, M1-M4)"
    → "Bond-Architecture.md v1.0 (4 bond types, 4 Decline mechanisms)"
    → HOẶC tách: Bond-Arch = bond types; Decline = separate line
    → ⚠️ "M1-M4" ở đây có thể là DECLINE cross-ref → xác nhận context
```

---

## §4 — Cross-Ref SAI: Tổng Hợp

```
  5 cross-refs SAI trỏ Bond-Architecture cho firing modes:
    Body-Base line 777:     "(Bond-Architecture.md v1.0)" → XÓA/FIX
    Discovery line 1036:    "(Bond-Architecture.md v1.0)" → XÓA/FIX
    Discovery line 18:      dep-list → FIX
    Discovery line 1019:    cross-ref → FIX
    Domain-Mapping line 951: "→ Xem Bond-Architecture §M1-M4" → XÓA/FIX

  Bond-Architecture §4 = Resonance DECLINE, KHÔNG phải firing modes.
  → Firing modes không có 1 source-of-truth file riêng hiện tại.
  → Option A: Xóa cross-ref (firing modes = self-contained per file)
  → Option B: Trỏ về Valence-Propagation §6 (canonical firing modes,
              dù VP dùng 3-mode taxonomy khác) + ghi note "orthogonal"
  → ⭐ Quyết định khi thực hiện, sau khi đọc sâu từng file.
```

---

## §5 — Thực Hiện

```
  1. Read 3 files: Body-Base §5.3, Discovery lines 1030-1060,
     Domain-Mapping lines 930-960

  2. Per file:
     a. Mark ALL M-label occurrences → classify firing vs decline
     b. Rename firing-mode M-labels: bỏ M-prefix
     c. Fix cross-refs SAI (xóa hoặc trỏ đúng)
     d. Fix dep-list labels
     e. KHÔNG ĐỘNG decline cross-refs (Plan R scope)

  3. Verify (xem §6)
  4. Cập nhật Status → ✅ DONE
```

---

## §6 — Verify

```
  Body-Base §5.3:       no M-labels trong firing modes definition
  Body-Base dep-list:    firing-mode entries đã fix; decline entries unchanged
  Discovery:            no M-labels trong firing section
  Domain-Mapping:       no M-labels trong firing section
  Cross-refs:           KHÔNG CÒN trỏ Bond-Architecture cho firing modes
  Decline refs:         UNCHANGED (chờ Plan R)
```

---

## §7 — Note: 3-vs-4 Mode Reconciliation

```
  Khi thực hiện, ĐỌC Valence-Propagation §5-§13 trước để hiểu:
  - VP 3-mode = WHEN (Maintenance/Chunk-Miss/Context-Trigger)
  - ③④ 4-mode = HOW (intensity/pattern)
  - Nếu xác nhận ORTHOGONAL → bỏ M-prefix + note "khác chiều" là đủ
  - Nếu phát hiện OVERLAP → cần reconcile sâu hơn → hỏi user

  ⚠️ Có thể cần thêm 1 dòng ghi chú trong mỗi file:
  "4 firing modes (Tonic/Phasic/Compound/Cascade) mô tả CƯỜNG ĐỘ fire.
   Khác 3 Firing Modes trong Valence-Propagation §6 (mô tả KHI NÀO fire)."
```
