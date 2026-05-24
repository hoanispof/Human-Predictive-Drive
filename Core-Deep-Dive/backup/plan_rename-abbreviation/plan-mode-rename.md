# Plan: Mode 1-6 Rename — 3 Systems × Descriptive Names

```
Status:    🔲 NOT STARTED
Created:   2026-05-23
Scope:     ~35 active files, ~270 replacements (3 colliding "Mode N" systems)
Approach:  SYSTEM-BY-SYSTEM (identify system per file → rename)
Depends:   KHÔNG. Chạy ĐỘC LẬP.
Verify:    grep "Mode [1-6]" = 0 trong active files (trừ legitimate non-framework uses)
Special:   MOSTLY MANUAL — replace_all chỉ dùng cho pure-system files
```

---

## §0 — TẠI SAO ĐỔI TÊN

### 2 lý do chính

**① 3 HỆ THỐNG DÙNG CÙNG "Mode N" — COLLISION NGUY HIỂM**

```
  "Mode 3" xuất hiện trong text — ý nghĩa phụ thuộc FILE:

  FILE = Valence-Propagation.md:
    Mode 3 = Context-Trigger (entity absent, cue-triggered L2 fire)

  FILE = Drive.md:
    Mode 3 = Spinning (PFC 30-50% nhưng KHÔNG hiệu quả)

  → CÙNG "Mode 3", KHÁC concept hoàn toàn
  → File dùng CẢ HAI systems → reader KHÔNG biết Mode 3 nào
```

**② ĐÃ CÓ TÊN DESCRIPTIVE — chỉ cần bỏ "Mode N"**

```
  Framework ĐÃ viết inline:
  → "Mode 1 (Maintenance)" → chỉ cần "Maintenance"
  → "Mode 3 (Spinning)" → chỉ cần "PFC-Spinning"
  → "Mode 2 schema override" → chỉ cần "Schema-Simulation"
```

---

## §1 — ĐỊNH NGHĨA TÊN MỚI

### §1.1 — System A: Valence Firing Modes (3 modes)

```
  Source: Valence-Propagation.md v3.0 §6 (3 Firing Modes taxonomy)

  ┌──────────┬─────────────────────┬──────────────────────────────────┐
  │ Hiện tại │ Tên mới             │ Cơ chế                           │
  ├──────────┼─────────────────────┼──────────────────────────────────┤
  │ Mode 1   │ Firing-Maintenance  │ Entity present. Daily routine.   │
  │          │                     │ Opioid low-level, VTA habituated.│
  │          │                     │ Background warmth = INVISIBLE.   │
  ├──────────┼─────────────────────┼──────────────────────────────────┤
  │ Mode 2   │ Firing-Absence      │ Entity removed acutely.          │
  │          │                     │ Compiled routine fires → no      │
  │          │                     │ response = PAIN. Bowlby grief.   │
  ├──────────┼─────────────────────┼──────────────────────────────────┤
  │ Mode 3   │ Firing-Trigger      │ Entity absent. External cue      │
  │          │                     │ matches Entity-Compiled spoke    │
  │          │                     │ → L2 fire unexpectedly.          │
  └──────────┴─────────────────────┴──────────────────────────────────┘

  Grouped: "3 Firing Modes" → "3 Firing Modes" (GIỮ — đã descriptive)
  Short: "Maintenance / Absence / Trigger" (khi context = Firing)
```

### §1.2 — System B: PFC Drive Modes (6 modes)

```
  Source: Drive.md v1.0 §2

  ┌──────────┬─────────────────────┬──────────────────────────────────┐
  │ Hiện tại │ Tên mới             │ Cơ chế                           │
  ├──────────┼─────────────────────┼──────────────────────────────────┤
  │ Mode 1   │ PFC-Absent          │ PFC ~0-5%. Fully automatic.      │
  │ Mode 2   │ PFC-Monitor         │ PFC ~5-15%. Background scan.     │
  │ Mode 3   │ PFC-Spinning        │ PFC ~30-50%. Active but          │
  │          │                     │ INEFFECTIVE (chunks missing).    │
  │ Mode 4   │ PFC-Resolve         │ PFC ~20-40%. Effective problem   │
  │          │                     │ solving (chunks sufficient).     │
  │ Mode 5   │ PFC-Strategic       │ PFC ~60-80%. Deliberate          │
  │          │                     │ optimization + meta-cognitive.   │
  │ Mode 6   │ PFC-Override        │ PFC ~80-95%. Against body-base   │
  │          │                     │ at high cost.                    │
  └──────────┴─────────────────────┴──────────────────────────────────┘

  Grouped: "Mode 1-2" → "PFC-Absent/Monitor" (hoặc "PFC low-engagement")
           "Mode 3-6" → "PFC-Spinning through Override" (hoặc "PFC high-engagement")
  Short: "Absent / Monitor / Spinning / Resolve / Strategic / Override"
         (khi context = PFC Drive)
```

### §1.3 — System C: Schema Override Modes (2 modes)

```
  Source: Agent-Mechanism.md v2.1 §10

  ┌──────────┬─────────────────────┬──────────────────────────────────┐
  │ Hiện tại │ Tên mới             │ Cơ chế                           │
  ├──────────┼─────────────────────┼──────────────────────────────────┤
  │ Mode 1   │ Schema-Trust        │ Zero modeling. Schema defines    │
  │          │                     │ entity absolutely. Daily prayer. │
  │ Mode 2   │ Schema-Simulation   │ Self-Pattern-Modeling fires onto │
  │          │                     │ schema-provided virtual agent.   │
  │          │                     │ Intense prayer dialogue.         │
  └──────────┴─────────────────────┴──────────────────────────────────┘

  Grouped: "2 Schema Override modes" → "Schema-Trust / Schema-Simulation"
```

---

## §2 — QUY TẮC THAY THẾ

### §2.1 — Approach: FILE-LEVEL SYSTEM IDENTIFICATION

```
  ⭐ KHÁC VỚI CÁC PLAN KHÁC:
  → KHÔNG THỂ dùng replace_all "Mode 1" → X cho toàn bộ framework
  → Vì "Mode 1" có 3 nghĩa khác nhau
  → PHẢI xác định SYSTEM trước, rồi rename theo system đó

  BƯỚC 1: Xác định file thuộc system nào:
  → File chỉ dùng PFC modes (Mode 1-6) = PURE PFC → replace_all OK
  → File chỉ dùng Firing modes (Mode 1-3) = PURE FIRING → replace_all OK
  → File dùng CẢ HAI systems = MIXED → MANUAL

  BƯỚC 2: Replace_all cho PURE files, manual cho MIXED files

  BƯỚC 3: Verify grep "Mode [1-6]" = 0
```

### §2.2 — Replace_all cho PURE PFC files

```
  Pass 1: "Mode 1-2" → "PFC-Absent/Monitor"  (grouped low)
  Pass 2: "Mode 3-6" → "PFC-Spinning through Override"  (grouped high)
  Pass 3: "Mode 1"   → "PFC-Absent"
  Pass 4: "Mode 2"   → "PFC-Monitor"
  Pass 5: "Mode 3"   → "PFC-Spinning"
  Pass 6: "Mode 4"   → "PFC-Resolve"
  Pass 7: "Mode 5"   → "PFC-Strategic"
  Pass 8: "Mode 6"   → "PFC-Override"
```

### §2.3 — Replace_all cho PURE FIRING files

```
  Pass 1: "3 Firing Modes" → "3 Firing Modes" (GIỮ — đã descriptive)
  Pass 2: "Mode 1"   → "Firing-Maintenance"
  Pass 3: "Mode 2"   → "Firing-Absence"
  Pass 4: "Mode 3"   → "Firing-Trigger"
```

### §2.4 — MIXED files: MANUAL per occurrence

```
  Đọc context 3-5 dòng → xác định system → rename tương ứng.

  CONTEXT CLUES:
  → "PFC %", "PFC engagement", "drive" context → PFC modes
  → "entity present/absent", "firing", "L2", "valence" → Firing modes
  → "schema", "virtual agent", "prayer", "modeling overlay" → Schema modes
```

---

## §3 — FILE INVENTORY

### §3.1 — PURE PFC FILES (replace_all safe)

```
  ┌───┬────────────────────────────────────────────────┬───────┬──────────┐
  │ # │ File                                           │ ~occ  │ Note     │
  ├───┼────────────────────────────────────────────────┼───────┼──────────┤
  │ 1 │ PFC/PFC-Configuration.md                       │ ~30   │ HEAVY    │
  │ 2 │ Observation/Drive.md                           │ ~25   │ SOURCE   │
  │ 3 │ Quote-Analysis/Move-Fast-Break-Things.md       │ ~14   │          │
  │ 4 │ Health/ADHD-Observation.md                     │ ~9    │          │
  │ 5 │ Feeling/Feeling-Literacy-Training.md           │ ~5    │          │
  │ 6 │ Quote-Analysis/Journey-Destination-Cluster.md  │ ~5    │          │
  │ 7 │ Quote-Analysis/Stay-Hungry-Stay-Foolish.md     │ ~3    │          │
  │ 8 │ Quote-Analysis/Adversity-Fear-Cluster.md       │ ~3    │          │
  │ 9+│ ~8 light files (1-2 occ each)                 │ ~12   │          │
  ├───┼────────────────────────────────────────────────┼───────┼──────────┤
  │   │ SUBTOTAL                                       │ ~106  │ ~16 files│
  └───┴────────────────────────────────────────────────┴───────┴──────────┘
```

### §3.2 — PURE FIRING FILES (replace_all safe)

```
  ┌───┬────────────────────────────────────────────────┬───────┬──────────┐
  │ # │ File                                           │ ~occ  │ Note     │
  ├───┼────────────────────────────────────────────────┼───────┼──────────┤
  │17 │ Body-Base/Valence-Propagation.md               │ ~13   │ SOURCE   │
  │18 │ Body-Base/Body-Coupling.md                     │ ~10   │          │
  ├───┼────────────────────────────────────────────────┼───────┼──────────┤
  │   │ SUBTOTAL                                       │ ~23   │ 2 files  │
  └───┴────────────────────────────────────────────────┴───────┴──────────┘
```

### §3.3 — MIXED / VERIFY FILES (manual)

```
  ⚠️ Files dùng NHIỀU Mode systems — cần per-occurrence review

  ┌───┬────────────────────────────────────────────────┬───────┬──────────┐
  │ # │ File                                           │ ~occ  │ Systems  │
  ├───┼────────────────────────────────────────────────┼───────┼──────────┤
  │19 │ Love-Romantic.md                               │ ~22   │ PFC+Fire │
  │20 │ Love-Unified.md                                │ ~22   │ PFC+Fire │
  │21 │ Observation/Empathy.md                         │ ~14   │ PFC+Fire │
  │22 │ Observation/Connection.md                      │ ~7    │ VERIFY   │
  │23 │ Observation/Boredom.md                         │ ~3    │ VERIFY   │
  │24 │ Observation/Gratitude.md                       │ ~2    │ VERIFY   │
  │25 │ Observation/Meaning.md                         │ ~2    │ VERIFY   │
  │26 │ Uncanny-Valley.md                              │ ~3    │ VERIFY   │
  │27 │ Human-AI-Future.md                             │ ~2    │ VERIFY   │
  │28 │ Quote-Analysis/Goal-And-Why.md                 │ ~2    │ VERIFY   │
  │29+│ ~6 light files                                 │ ~8    │ VERIFY   │
  ├───┼────────────────────────────────────────────────┼───────┼──────────┤
  │   │ SUBTOTAL                                       │ ~87   │ ~15 files│
  └───┴────────────────────────────────────────────────┴───────┴──────────┘
```

### §3.4 — SCHEMA MODE FILES (likely only Agent-Mechanism reference)

```
  Agent-Mechanism.md §10 defines Schema modes.
  Cross-references appear in VP, Religion.md.
  → Small scope — handle within MIXED session.
```

---

## §4 — SESSION PLAN

```
  ┌─────┬─────────────────────────────┬───────┬───────┬──────────────────┐
  │ Ses │ Cluster                     │ Files │ ~Occ  │ Note             │
  ├─────┼─────────────────────────────┼───────┼───────┼──────────────────┤
  │ S1  │ Source files (Drive, VP, AM)│   3   │  ~40  │ DEFINE new names │
  │ S2  │ Pure PFC files              │ ~16   │ ~106  │ replace_all OK   │
  │ S3  │ Pure Firing + light Mixed   │ ~10   │  ~40  │ replace_all + manual │
  │ S4  │ Heavy Mixed files           │  ~6   │  ~80  │ ALL MANUAL       │
  ├─────┼─────────────────────────────┼───────┼───────┼──────────────────┤
  │     │ TOTAL                       │ ~35   │ ~266  │ 4 sessions       │
  └─────┴─────────────────────────────┴───────┴───────┴──────────────────┘
```
