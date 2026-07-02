# Plan: Tầng A/B Rename — Tầng A/B → Tầng Hardware/Tầng PFC

```
Status:    ✅ COMPLETE (2026-05-24)
Created:   2026-05-23
Scope:     5 active files, ~27 replacements
Approach:  SINGLE SESSION (scope nhỏ nhất trong tất cả rename plans)
Depends:   KHÔNG. Chạy ĐỘC LẬP.
Verify:    grep "Tầng A\b" + "Tầng B\b" = 0 trong active files (trừ "Tầng Appraisal" etc.)
```

---

## §0 — TẠI SAO ĐỔI TÊN

### 2 lý do chính

**① "A" VÀ "B" KHÔNG MANG NGHĨA**

```
  "Tầng A" — tier gì? hardware? PFC? cái nào?
  "Tầng B" — cái nào còn lại?
  → Phải tra bảng mỗi lần gặp

  "Tầng Hardware" — ngay lập tức hiểu: hardware-driven, automatic, invisible
  "Tầng PFC" — ngay lập tức hiểu: PFC-computed, deliberate, visible per episode
  → Tự giải thích
```

**② DỄ NHẦM VỚI REWARD TYPE A/B (ĐÃ ĐỔI)**

```
  Trước rename Plan 1:
  → "Type A" = Evaluative Reward (ĐÃ ĐỔI)
  → "Tầng A" = Hardware visibility tier (CHƯA ĐỔI)
  → Cùng chữ "A" — reader dễ nhầm

  Sau rename:
  → "Tầng Hardware" — rõ ràng, không liên quan reward
```

---

## §1 — ĐỊNH NGHĨA TÊN MỚI

### §1.1 — Tên chính thức

```
  ┌────────────┬──────────────────┬─────────────────────────────────────┐
  │ Hiện tại   │ Tên mới          │ Lý do                               │
  ├────────────┼──────────────────┼─────────────────────────────────────┤
  │ Tầng A     │ Tầng Hardware    │ Valence driven by HARDWARE          │
  │            │                  │ (oxytocin, cortisol, VTA baseline). │
  │            │                  │ Automatic. Cost ≈ 0. INVISIBLE     │
  │            │                  │ most of the time — chỉ visible     │
  │            │                  │ khi disrupted (mất mát, xa cách).   │
  │            │                  │ Source: VP v3.0 §7 line 594.        │
  ├────────────┼──────────────────┼─────────────────────────────────────┤
  │ Tầng B     │ Tầng PFC         │ Valence computed by PFC             │
  │            │                  │ (Self-Pattern-Modeling evaluation). │
  │            │                  │ Deliberate. Has PFC cost. VISIBLE  │
  │            │                  │ per episode — PFC "sees" it.       │
  │            │                  │ Source: VP v3.0 §7 line 601.        │
  └────────────┴──────────────────┴─────────────────────────────────────┘

  GIỮ "Tầng" prefix:
  → "Tầng" = Vietnamese "tier/level" — meaningful, không phải label rỗng
  → Nhất quán với "2-tầng" model terminology
  → Chỉ thay "A"/"B" → "Hardware"/"PFC"

  TẠI SAO "PFC" KHÔNG PHẢI ABBREVIATION:
  → PFC (PreFrontal Cortex) = standard neuroscience term
  → Framework dùng PFC xuyên suốt (PFC-Hardware.md, PFC-Operations.md, ...)
  → plan-abbreviation-cleanup.md giữ PFC làm exception (domain term)
```

### §1.2 — Compound terms

```
  ┌───────────────────────────────────┬────────────────────────────────┐
  │ Hiện tại                          │ Sau rename                     │
  ├───────────────────────────────────┼────────────────────────────────┤
  │ Tầng A                            │ Tầng Hardware                  │
  │ Tầng B                            │ Tầng PFC                       │
  │ Tầng A dominant                   │ Tầng Hardware dominant         │
  │ Tầng B dominant                   │ Tầng PFC dominant              │
  │ Tầng A DOMINANT                   │ Tầng Hardware DOMINANT         │
  │ Tầng A SIMULATED                  │ Tầng Hardware SIMULATED        │
  │ Tầng A hardware                   │ Tầng Hardware (bỏ redundant)   │
  │ 2-tầng: Tầng A dominant           │ 2-tầng: Tầng Hardware dominant │
  │ A→B shift (tầng context)          │ Hardware→PFC shift             │
  │ A+B balanced (tầng context)       │ Hardware+PFC balanced          │
  │ Connection Tầng A                 │ Connection Tầng Hardware       │
  │ Connection Tầng B                 │ Connection Tầng PFC            │
  └───────────────────────────────────┴────────────────────────────────┘

  ⚠️ REDUNDANCY CHECK:
  → "Tầng A hardware" (VP line 1037) → "Tầng Hardware" (bỏ "hardware" thừa)
  → "Tầng A (hardware)" → "Tầng Hardware" (bỏ parenthetical thừa)
```

---

## §2 — QUY TẮC THAY THẾ

### §2.1 — Replace_all passes (per file)

```
  ⭐ THỨ TỰ:

  Pass 1: "Tầng A" → "Tầng Hardware"    (catch most occurrences)
  Pass 2: "Tầng B" → "Tầng PFC"         (catch most occurrences)

  ⚠️ SAU replace_all: MANUAL REVIEW cho:
  → Redundancy: "Tầng Hardware hardware" → sửa thành "Tầng Hardware"
  → "Tầng Hardware (hardware)" → sửa thành "Tầng Hardware"
  → Standalone "A" / "B" trong context tầng:
     "A→B shift" → "Hardware→PFC shift"
     "A+B balanced" → "Hardware+PFC balanced"
     "Tầng A dom." → "Tầng Hardware dom." (table abbreviation)
  → Table headers: check width vẫn OK
```

### §2.2 — KHÔNG thay

```
  ① "Tầng PFC" / "Tầng Body" (line 1741 VP) — khác concept, dùng "tầng" chung
  ② "Tầng Appraisal" (backup file) — khác concept, backup = skip
  ③ "Tầng 1/2/3" (3-Tầng model) — KHÁC SYSTEM (resonance model tiers)
  ④ "2-tầng" (standalone, no A/B) — giữ nguyên (refers to model, not tier label)
  ⑤ Backup files — SKIP
```

---

## §3 — FILE INVENTORY

```
  ⭐ SINGLE SESSION — chỉ 5 files, ~27 replacements

  ┌───┬──────────────────────────────────────────────────┬───────┬──────────┐
  │ # │ File                                             │ ~occ  │ Note     │
  ├───┼──────────────────────────────────────────────────┼───────┼──────────┤
  │ 1 │ Body-Base/Valence-Propagation.md                 │ ~14   │ SOURCE   │
  │ 2 │ Agent-Mechanism/Resonance-Per-Entity.md          │ ~8    │          │
  │ 3 │ Agent-Mechanism/Entity-Access.md                 │ ~2    │          │
  │ 4 │ Observation/Empathy.md                           │ ~2    │          │
  │ 5 │ Observation/Gratitude.md                         │ ~1    │          │
  ├───┼──────────────────────────────────────────────────┼───────┼──────────┤
  │   │ TOTAL                                            │ ~27   │ 5 files  │
  └───┴──────────────────────────────────────────────────┴───────┴──────────┘

  WORKFLOW:
  ① Valence-Propagation.md TRƯỚC (source definition)
  ② Resonance-Per-Entity.md (heaviest consumer)
  ③ Remaining 3 files (light, 1-2 occ each)
  ④ Verification grep across ALL active folders
```

---

## §4 — GHI CHÚ

```
  ⚠️ LIÊN QUAN PLAN KHÁC:

  Plan 4 (L0-L3): Valence-Propagation dùng "L1/L2" CHO 2-luồng model
  → Tầng A/B rename KHÔNG ảnh hưởng L1/L2 — 2 concepts ĐỘC LẬP
  → Nhưng SAU rename, formula sẽ đọc tốt hơn:
     Trước: "L2 dominant + Tầng A dominant = MOST INVISIBLE"
     Sau:   "L2 dominant + Tầng Hardware dominant = MOST INVISIBLE"
  → Khi L-labels cũng được rename (Plan 4), sẽ càng rõ hơn

  Plan 3 (F1/F2): Nhiều files chung (VP, RPE, Empathy, EA)
  → Rename Tầng A/B TRƯỚC hoặc SAU F1/F2 đều OK — không conflict
```
