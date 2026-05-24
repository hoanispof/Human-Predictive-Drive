# Plan: Stream 1/2 Rename — Stream 1/2 → Hardware-Stream/Modeling-Stream

```
Status:    ✅ COMPLETE (2026-05-24)
Created:   2026-05-24
Scope:     ~7 active files, ~119 "Stream 1/2" replacements + S1/S2 manual
Approach:  replace_all cho "Stream 1"/"Stream 2" + MANUAL cho "S1"/"S2"
Depends:   KHÔNG. Chạy ĐỘC LẬP.
Verify:    grep "Stream 1" + "Stream 2" = 0 trong active files
Source:    Tách từ plan-s-stream-rename.md §1.1 (chỉ Streams, KHÔNG Dunbar)
```

---

## §0 — TẠI SAO ĐỔI TÊN

```
  "Stream 1" / "Stream 2" không mang nghĩa — phải tra context mỗi lần gặp.

  "Hardware-Stream" → ngay lập tức hiểu: unidirectional, reward INDEPENDENT,
    habituates, animal-level.
  "Modeling-Stream" → ngay lập tức hiểu: Self-Pattern-Modeling mutual,
    bidirectional, anti-habituation, human-specific.

  ⚠️ "S1"/"S2" standalone CÒN COLLISION với 5 nghĩa khác:
  ① Somatosensory S1/S2 (neuroscience) → GIỮ
  ② Session S1-S12 (drill) → GIỮ
  ③ Phase S1/S2 (plan execution) → GIỮ
  ④ Schema S1/S2 (open questions) → GIỮ
  ⑤ Dunbar S1-S6 (separate plan) → GIỮ
```

---

## §1 — ĐỊNH NGHĨA TÊN MỚI

```
  Source: Agent-Mechanism.md v2.1 §4.2

  ┌────────────┬─────────────────────┬──────────────────────────────────┐
  │ Hiện tại   │ Tên mới             │ Cơ chế                           │
  ├────────────┼─────────────────────┼──────────────────────────────────┤
  │ Stream 1   │ Hardware-Stream     │ Unidirectional. Each side gets   │
  │ S1 (stream)│                     │ reward INDEPENDENTLY. No mutual  │
  │            │                     │ engagement needed. HABITUATES.   │
  ├────────────┼─────────────────────┼──────────────────────────────────┤
  │ Stream 2   │ Modeling-Stream     │ Self-Pattern-Modeling compiled   │
  │ S2 (stream)│                     │ mutual (bidirectional). Both     │
  │            │                     │ engage. Feedback loop. ANTI-     │
  │            │                     │ HABITUATION (Hebbian).           │
  └────────────┴─────────────────────┴──────────────────────────────────┘

  KHÔNG viết tắt: HS/MS KHÔNG BAO GIỜ.
```

---

## §2 — QUY TẮC THAY THẾ

### §2.1 — SAFE replace_all (full-text "Stream 1"/"Stream 2")

```
  "Stream 1" → "Hardware-Stream"        (replace_all — AN TOÀN)
  "Stream 2" → "Modeling-Stream"        (replace_all — AN TOÀN)

  ⭐ AN TOÀN vì: "Stream 1"/"Stream 2" chỉ dùng cho concept này.
  Không có nghĩa khác nào dùng "Stream 1" hay "Stream 2".
```

### §2.2 — MANUAL (standalone "S1"/"S2")

```
  "S1" / "S2" cần ĐỌC CONTEXT từng dòng:
  → Nếu = Stream context → "Hardware-Stream" / "Modeling-Stream"
  → Nếu = somatosensory / session / phase / Dunbar → GIỮ NGUYÊN

  Tips phân biệt:
  → "S1+S2" / "S1 habituates" / "S1 only" = STREAM → đổi
  → "S1 cortex" / "Session S1" / "Dunbar S1" = KHÁC → giữ
```

### §2.3 — Compound patterns

```
  ┌────────────────────────────────────┬──────────────────────────────────────┐
  │ Hiện tại                           │ Sau rename                           │
  ├────────────────────────────────────┼──────────────────────────────────────┤
  │ Stream 1/2 strong                  │ Hardware-Stream/Modeling-Stream strong│
  │ S1+S2                              │ Hardware-Stream+Modeling-Stream       │
  │ S1 habituates, S2 atrophies        │ HW-Stream habituates, M-Stream...   │
  │ "S1 only"                          │ "Hardware-Stream only"               │
  │ Stream 1 → Stream 2               │ Hardware-Stream → Modeling-Stream    │
  └────────────────────────────────────┴──────────────────────────────────────┘

  ⚠️ Trong bảng hẹp, có thể viết "HW-Stream" / "M-Stream" NẾU CẦN.
  Nhưng ưu tiên tên đầy đủ.
```

### §2.4 — KHÔNG thay

```
  ① Backup files → KHÔNG SỬA
  ② Plan files (trừ plan này) → KHÔNG SỬA
  ③ Dunbar S1-S6 → KHÔNG thuộc plan này
  ④ Somatosensory S1/S2 → neuroscience term, giữ nguyên
  ⑤ Session / Phase / Schema labels → giữ nguyên
```

---

## §3 — FILE INVENTORY (7 ACTIVE FILES)

### §3.1 — Session 1: Source + Heavy

```
  ┌───┬─────────────────────────────────────────┬────────┬──────────────┐
  │ # │ File                                    │ Occ    │ Note         │
  ├───┼─────────────────────────────────────────┼────────┼──────────────┤
  │ 1 │ Agent-Mechanism.md                      │ ~36    │ SOURCE DEF   │
  │   │ (+ ~19 S1/S2 standalone MIXED)          │        │ MANUAL S1/S2 │
  │ 2 │ Connection.md                           │ ~24    │              │
  │ 3 │ Gap-Direction.md                        │ ~23    │              │
  │ 4 │ Empathy.md                              │ ~15    │              │
  │ 5 │ Love-Romantic.md                        │ ~12    │              │
  │ 6 │ Body-Feedback-Label.md                  │ ~7     │              │
  │ 7 │ By-Product-Gap-Resonance.md             │ ~2     │              │
  ├───┼─────────────────────────────────────────┼────────┼──────────────┤
  │   │ TOTAL                                   │ ~119   │ 1 session    │
  └───┴─────────────────────────────────────────┴────────┴──────────────┘

  ⭐ CÓ THỂ LÀM TRONG 1 SESSION:
  → replace_all "Stream 1" / "Stream 2" cho cả 7 files
  → MANUAL S1/S2 chỉ trong Agent-Mechanism.md (~19 occ cần đọc context)
```

---

## §4 — EXECUTION STEPS (1 SESSION)

```
  ① replace_all "Stream 1" → "Hardware-Stream" (7 files)
  ② replace_all "Stream 2" → "Modeling-Stream" (7 files)
  ③ Agent-Mechanism.md: đọc ~19 "S1"/"S2" standalone → rename nếu stream context
  ④ Grep verify "Stream 1" = 0, "Stream 2" = 0
  ⑤ Grep confirm "Hardware-Stream" > 0, "Modeling-Stream" > 0
```

---

## §5 — VERIFICATION

### §5.1 — FINAL VERIFY

```
  ① grep "Stream 1" = 0 trong active files (trừ backup/)
  ② grep "Stream 2" = 0 trong active files (trừ backup/)
  ③ grep "Hardware-Stream" > 0 (xác nhận tồn tại)
  ④ grep "Modeling-Stream" > 0 (xác nhận tồn tại)
  ⑤ MANUAL CHECK: Agent-Mechanism.md — tất cả "S1"/"S2" stream context đã đổi
```

---

> *Plan: Stream Rename — Stream 1/2 → Hardware-Stream/Modeling-Stream.*
> *7 active files. ~119 replacements. 1 session.*
> *replace_all AN TOÀN cho "Stream 1"/"Stream 2" — không collision.*
> *"S1"/"S2" standalone chỉ manual trong Agent-Mechanism.md.*
> *"Stream 1" = 0 + "Stream 2" = 0 trong active files = DONE indicator.*
