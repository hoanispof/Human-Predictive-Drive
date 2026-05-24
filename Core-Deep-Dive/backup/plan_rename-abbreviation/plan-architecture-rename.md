# Plan: Architecture Rename — Architecture A/B → Hardwired/Compilable

```
Status:    🔲 NOT STARTED
Created:   2026-05-23
Scope:     ~63 active files, ~512 replacements (Architecture A → Hardwired, Architecture B → Compilable)
Approach:  CLUSTER-BY-CLUSTER (Core Definition → Heavy → Medium → Light)
Verify:    grep=0 cho "Architecture A" + "Architecture B" sau khi hoàn thành
```

---

## §0 — TẠI SAO ĐỔI TÊN

### Lý do

```
① "A" và "B" không mang nghĩa — vi phạm quy tắc descriptive names
② Sau khi Reward Type A/B → Evaluative/Direct-State, "Architecture A/B"
   là label A/B duy nhất CÒN LẠI trong framework
③ File gốc (Inter-Body-Mechanism.md §1.2) ĐÃ mô tả rõ:
   - Architecture A = "specific-reward" — hardwired circuits
   - Architecture B = "general-purpose" — compilable mechanism
④ Đổi tên → framework KHÔNG CÒN bất kỳ "A/B" vô nghĩa nào
```

---

## §1 — ĐỊNH NGHĨA TÊN MỚI

### §1.1 — Tên chính thức

```
  ┌──────────────────┬───────────────────────────┬──────────────────────────────────┐
  │ Hiện tại         │ Tên mới                   │ Lý do                            │
  ├──────────────────┼───────────────────────────┼──────────────────────────────────┤
  │ Architecture A   │ Hardwired Architecture    │ Hardwired BEHAVIOR circuits.     │
  │                  │                           │ Fixed: food→reward, mate→reward. │
  │                  │                           │ Côn trùng, động vật đơn giản.    │
  ├──────────────────┼───────────────────────────┼──────────────────────────────────┤
  │ Architecture B   │ Compilable Architecture   │ General-purpose MECHANISM.        │
  │                  │                           │ Content LEARNED from experience. │
  │                  │                           │ Humans: 15-20 năm compile.       │
  └──────────────────┴───────────────────────────┴──────────────────────────────────┘
```

### §1.2 — Viết hoa / viết thường

```
  ⭐ QUY TẮC:

  Hardwired Architecture / Compilable Architecture = CAPITALIZED (concept name)

  Viết tắt contextual (khi context ĐÃ rõ là architecture):
  → "Hardwired" / "Compilable" — OK
  → KHÔNG bao giờ viết tắt thành HA/CA/H/C

  Tổ hợp:
  → "Hardwired/Compilable Architecture" thay cho "Architecture A/B"
  → "Hardwired/Compilable" thay cho "A/B" khi context rõ
```

### §1.3 — Compound terms

```
  ┌────────────────────────┬──────────────────────────────────────────┐
  │ Hiện tại               │ Sau rename                               │
  ├────────────────────────┼──────────────────────────────────────────┤
  │ Architecture A         │ Hardwired Architecture                   │
  │ Architecture B         │ Compilable Architecture                  │
  │ Architecture A/B       │ Hardwired/Compilable Architecture        │
  │ Architecture B ①       │ Compilable Architecture ①                │
  │ Architecture B ②       │ Compilable Architecture ②                │
  │ Architecture B ③       │ Compilable Architecture ③                │
  │ Architecture A (spec.) │ Hardwired Architecture (spec.)           │
  │ Architecture B (gen.)  │ Compilable Architecture (gen.)           │
  └────────────────────────┴──────────────────────────────────────────┘
```

---

## §2 — QUY TẮC THAY THẾ

### §2.1 — Quy tắc chính

```
  ⭐ ĐƠN GIẢN hơn Reward rename vì:
  ① "Architecture" prefix LUÔN CÓ — không có standalone "A"/"B" nhầm
  ② KHÔNG có mixed context — Architecture A/B chỉ 1 concept duy nhất
  ③ replace_all AN TOÀN cho hầu hết files

  THAY:
  ① "Architecture A" → "Hardwired Architecture" (replace_all)
  ② "Architecture B" → "Compilable Architecture" (replace_all)
  ③ "Architecture A/B" → "Hardwired/Compilable Architecture"

  KIỂM TRA SAU:
  → grep "Architecture A" = 0
  → grep "Architecture B" = 0
  → grep "Hardwired Architecture" > 0
  → grep "Compilable Architecture" > 0
```

### §2.2 — KHÔNG thay

```
  ① Backup files (backup/, _backup/) → KHÔNG SỬA
  ② Drill files (historical record) → KHÔNG SỬA
  ③ Plan files (plan-reward-type-rename.md, etc.) → KHÔNG SỬA
     (plan files reference old names IN CONTEXT of explaining the change)
```

---

## §3 — FILE INVENTORY (63 ACTIVE FILES)

### §3.1 — Cluster 1: CORE DEFINITION (Session 1)

```
  ⭐ PRIORITY HIGHEST — Establish new names tại đây TRƯỚC.

  ┌───┬──────────────────────────────────────┬────────┬──────────────┐
  │ # │ File                                 │ A + B  │ Note         │
  ├───┼──────────────────────────────────────┼────────┼──────────────┤
  │ 1 │ Inter-Body-Mechanism.md              │ 3 + 14 │ PRIMARY DEF  │
  │ 2 │ Reward-Signal-Architecture.md        │ 1 + 14 │ đã rename    │
  │ 3 │ Why-Body-Knows.md                    │ 4 + 29 │ HEAVY        │
  │ 4 │ Body-Base.md                         │ 3 + 13 │              │
  │ 5 │ Neural-Processing-Flow.md            │ 1 + 16 │              │
  ├───┼──────────────────────────────────────┼────────┼──────────────┤
  │   │ SUBTOTAL                             │ 12 + 86│ 5 files      │
  └───┴──────────────────────────────────────┴────────┴──────────────┘
```

### §3.2 — Cluster 2: HEAVY FILES (Session 2)

```
  ┌───┬──────────────────────────────────────┬────────┬──────────────┐
  │ # │ File                                 │ A + B  │ Note         │
  ├───┼──────────────────────────────────────┼────────┼──────────────┤
  │ 6 │ Agent-Mechanism.md                   │ 2 + 44 │ HEAVIEST     │
  │ 7 │ Gap-Direction.md                     │ 4 + 25 │ HEAVY        │
  │ 8 │ Valence-Propagation.md               │ 20 + 2 │ HEAVY A      │
  │ 9 │ Resonance-Per-Entity.md              │ 14 + 0 │ HEAVY A      │
  ├───┼──────────────────────────────────────┼────────┼──────────────┤
  │   │ SUBTOTAL                             │ 40 + 71│ 4 files      │
  └───┴──────────────────────────────────────┴────────┴──────────────┘
```

### §3.3 — Cluster 3: BODY + FEELING + CONNECTION (Session 3)

```
  ┌───┬──────────────────────────────────────┬────────┬──────────────┐
  │ # │ File                                 │ A + B  │ Note         │
  ├───┼──────────────────────────────────────┼────────┼──────────────┤
  │10 │ Body-Feedback.md                     │ 1 + 19 │              │
  │11 │ Feeling.md                           │ 1 + 17 │              │
  │12 │ Connection.md                        │ 1 + 14 │              │
  │13 │ Collective-Body.md                   │ 0 + 13 │              │
  │14 │ Autonomy.md                          │ 3 + 12 │              │
  │15 │ Autonomy-Hardware.md                 │ 1 + 10 │              │
  │16 │ Gratitude.md                         │ 1 + 12 │              │
  ├───┼──────────────────────────────────────┼────────┼──────────────┤
  │   │ SUBTOTAL                             │ 8 + 97 │ 7 files      │
  └───┴──────────────────────────────────────┴────────┴──────────────┘
```

### §3.4 — Cluster 4: MEDIUM FILES (Session 4)

```
  ┌───┬──────────────────────────────────────┬────────┬──────────────┐
  │ # │ File                                 │ A + B  │ Note         │
  ├───┼──────────────────────────────────────┼────────┼──────────────┤
  │17 │ Boredom.md                           │ 1 + 11 │              │
  │18 │ Meaning.md                           │ 2 + 11 │              │
  │19 │ Obligation.md                        │ 2 + 11 │              │
  │20 │ Drive.md                             │ 3 + 9  │              │
  │21 │ Empathy.md                           │ 2 + 9  │              │
  │22 │ Protect.md                           │ 3 + 9  │              │
  │23 │ Status.md                            │ 2 + 9  │              │
  │24 │ Threat.md                            │ 2 + 10 │              │
  │25 │ Novelty.md                           │ 1 + 10 │              │
  ├───┼──────────────────────────────────────┼────────┼──────────────┤
  │   │ SUBTOTAL                             │ 18 + 89│ 9 files      │
  └───┴──────────────────────────────────────┴────────┴──────────────┘
```

### §3.5 — Cluster 5: LIGHT FILES (Session 5)

```
  ┌───┬──────────────────────────────────────┬────────┬──────────────┐
  │ # │ File                                 │ A + B  │ Note         │
  ├───┼──────────────────────────────────────┼────────┼──────────────┤
  │26 │ Gap-Body-Need.md                     │ 1 + 6  │              │
  │27 │ Coordination-Node.md                 │ 1 + 5  │              │
  │28 │ Imagine-Final.md                     │ 0 + 5  │              │
  │29 │ PFC-Operations.md                    │ 0 + 6  │              │
  │30 │ Logic-Feeling-Balance.md             │ 0 + 6  │              │
  │31 │ Bond-Architecture.md                 │ 0 + 4  │              │
  │32 │ By-Product-Gap-Resonance.md          │ 0 + 4  │              │
  │33 │ Gap-Distribution-Profile.md          │ 0 + 4  │              │
  │34 │ Body-Feedback-Label.md               │ 1 + 3  │              │
  │35 │ Entity-Access.md                     │ 3 + 0  │              │
  │36 │ Simulation-Engine.md                 │ 0 + 3  │              │
  │37 │ Action-Space.md                      │ 0 + 2  │              │
  │38 │ By-Product-Scale.md                  │ 0 + 2  │              │
  │39 │ Self-Pattern-Modeling.md             │ 1 + 2  │              │
  │40 │ Resonance-Sustainability.md          │ 0 + 2  │              │
  │41 │ Valence-Propagation.md (2nd check)   │ 0 + 2  │              │
  │42 │ 04-Integration.md                    │ 2 + 2  │              │
  │43 │ 10-F1-Synthesis.md                   │ 2 + 1  │              │
  │44 │ Creator-Lens.md                      │ 1 + 1  │              │
  │45 │ 01-File-Index.md                     │ 1 + 1  │              │
  ├───┼──────────────────────────────────────┼────────┼──────────────┤
  │   │ SUBTOTAL                             │ 13 + 61│ 20 files     │
  └───┴──────────────────────────────────────┴────────┴──────────────┘
```

### §3.6 — Cluster 6: MINIMAL FILES (Session 6)

```
  ┌───┬──────────────────────────────────────┬────────┬──────────────┐
  │ # │ File                                 │ A + B  │ Note         │
  ├───┼──────────────────────────────────────┼────────┼──────────────┤
  │46 │ Body-Feedback-Mechanism.md           │ 0 + 1  │              │
  │47 │ Collective-Arc-Dynamics.md           │ 0 + 1  │              │
  │48 │ Entity-Compiled.md                   │ 0 + 1  │              │
  │49 │ Entity-Access-Excess.md              │ 1 + 0  │              │
  │50 │ Hidden-Quality-Perception.md         │ 0 + 1  │              │
  │51 │ Logic-Planning.md                    │ 0 + 1  │              │
  │52 │ Love-Unified.md                      │ 1 + 0  │              │
  │53 │ Meta-Impact.md                       │ 1 + 0  │              │
  │54 │ Reward-Calibration.md                │ 1 + 0  │              │
  │55 │ Social-Calibration.md                │ 0 + 1  │              │
  │56 │ pending-quotes.md                    │ 0 + 1  │              │
  │57 │ plan.md                              │ 0 + 1  │              │
  │58 │ Education-Arms-Race.md               │ 1 + 0  │              │
  │59 │ 01-PFC-Hardware-Reframe.md           │ 0 + 1  │              │
  │60 │ 02-Womb-to-Birth-Baseline.md         │ 1 + 0  │              │
  │61 │ 03-Theme-B-Verbal-Chain.md           │ 1 + 0  │              │
  │62 │ 07-Social-Recognition-Arc.md         │ 1 + 0  │              │
  │63 │ 09-Learning-Cycle.md                 │ 1 + 0  │              │
  │64 │ 10-F1-Synthesis-VI.md                │ 1 + 0  │              │
  ├───┼──────────────────────────────────────┼────────┼──────────────┤
  │   │ SUBTOTAL                             │ 10 + 8 │ 19 files     │
  └───┴──────────────────────────────────────┴────────┴──────────────┘
```

---

## §4 — SESSION PLAN

```
  ┌─────────┬────────────────────────────────┬───────┬────────┬──────────┐
  │ Session │ Cluster                        │ Files │ ~Repl  │ Priority │
  ├─────────┼────────────────────────────────┼───────┼────────┼──────────┤
  │ S1      │ Core Definition                │ 5     │ ~98    │ ⭐⭐⭐     │
  │ S2      │ Heavy Files                    │ 4     │ ~111   │ ⭐⭐⭐     │
  │ S3      │ Body + Feeling + Connection    │ 7     │ ~105   │ ⭐⭐       │
  │ S4      │ Medium Files                   │ 9     │ ~107   │ ⭐⭐       │
  │ S5      │ Light Files                    │ 20    │ ~74    │ ⭐        │
  │ S6      │ Minimal Files (1 occ. each)    │ 19    │ ~18    │ ⭐        │
  ├─────────┼────────────────────────────────┼───────┼────────┼──────────┤
  │ TOTAL   │                                │ ~64   │ ~512   │          │
  └─────────┴────────────────────────────────┴───────┴────────┴──────────┘

  Mỗi session:
  1. replace_all "Architecture A" → "Hardwired Architecture"
  2. replace_all "Architecture B" → "Compilable Architecture"
  3. Đọc lại → fix table alignment + redundancy nếu cần
  4. Grep verify: 0 remaining "Architecture A"/"Architecture B"
  5. Grep confirm: "Hardwired Architecture" + "Compilable Architecture" tồn tại

  ⭐ ĐƠN GIẢN HƠN REWARD RENAME vì:
  → Prefix "Architecture" LUÔN CÓ — không có standalone A/B nhầm
  → KHÔNG có mixed context
  → replace_all AN TOÀN cho hầu hết files
  → Sessions 5-6 có thể gộp nếu cần
```

---

## §5 — EDGE CASES

```
  ① "Architecture A/B" compound:
     → replace "Architecture A/B" TRƯỚC
     → Thành "Hardwired/Compilable Architecture"
     → Rồi mới replace "Architecture A" và "Architecture B" riêng

  ② Tables với column headers "Architecture A" / "Architecture B":
     → Short form "Hardwired" / "Compilable" nếu column width hẹp

  ③ File Reward-Signal-Architecture.md (đã rename reward):
     → "Architecture B" (14 occurrences) vẫn cần đổi → "Compilable Architecture"
     → "Architecture A" (1 occurrence, line 114) → "Hardwired Architecture"
     → Cẩn thận: file đã bị sửa trong Reward rename session

  ④ "Architecture B ①②③" numbered features:
     → Thành "Compilable Architecture ①②③" — giữ nguyên số

  ⑤ Plan files (plan-reward-type-rename.md, plan-compile-type-rename.md):
     → KHÔNG SỬA — historical context cho rename process
```

---

## §6 — VERIFICATION

### §6.1 — Sau mỗi session

```
  grep "Architecture A" [files-in-cluster] = 0
  grep "Architecture B" [files-in-cluster] = 0
  grep "Hardwired Architecture" [files-in-cluster] > 0
  grep "Compilable Architecture" [files-in-cluster] > 0
```

### §6.2 — Sau session cuối (FINAL VERIFY)

```
  Toàn bộ framework (trừ backup/):

  ① grep "Architecture A" = 0 trong active files
  ② grep "Architecture B" = 0 trong active files
  ③ grep "Hardwired Architecture" > 0 (xác nhận tồn tại)
  ④ grep "Compilable Architecture" > 0 (xác nhận tồn tại)
```

---

## §7 — ORDERING

```
  ⚠️ THỰC HIỆN SAU Plan 1 (Reward Type Rename) session nào đang chạy.
  Có thể XEN KẼ với Reward rename nếu cần nghỉ đổi context.
  KHÔNG phụ thuộc Plan 1 — Architecture A/B hoàn toàn independent.
  CÓ THỂ gộp Session 5+6 (light+minimal) thành 1 session.
```

---

> *Plan: Architecture Rename — Architecture A/B → Hardwired/Compilable.*
> *~64 active files. ~512 replacements. 6 sessions (có thể gộp 5+6).*
> *Core rule: Architecture A → Hardwired Architecture. Architecture B → Compilable Architecture.*
> *replace_all AN TOÀN — prefix "Architecture" luôn có, không mixed context.*
> *"Architecture A" = 0 + "Architecture B" = 0 trong active files = DONE indicator.*
