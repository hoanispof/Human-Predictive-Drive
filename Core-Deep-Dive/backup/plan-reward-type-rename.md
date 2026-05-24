# Plan: Reward Type Rename — Type A/B → Evaluative/Direct-State

```
Status:    🟡 IN PROGRESS — S1+S2 DONE (9 files, ~350 replacements)
Created:   2026-05-23
Scope:     ~60 active files, ~650-800 replacements (Type A/B + A₀→A₃ → E₀→E₃)
Approach:  CLUSTER-BY-CLUSTER (Core Definition → Deep-Dive → Research → Application)
Verify:    grep=0 cho TỪNG pattern cũ sau khi hoàn thành mỗi session
```

---

## §0 — TẠI SAO ĐỔI TÊN

### 3 lý do chính

**① TRÙNG KÝ HIỆU VỚI COMPILE-TAXONOMY**

Framework có 2 hệ thống "Type" hoàn toàn khác nhau:

```
  REWARD (file này đổi):                COMPILE (KHÔNG đổi):
  ─────────────────────                  ────────────────────
  Type A = Evaluative (opioid)           Loại A = Direct Experience
  Type B = Direct State (non-opioid)     Loại B = Compiled Expertise
                                         Loại C = Trust Install

  → Cùng chữ "A", "B" — KHÁC concept
  → Người đọc gặp "Type A" phải suy context
  → Rename reward types → phân biệt NGAY LẬP TỨC
```

**② NHẤT QUÁN VỚI QUY TẮC FRAMEWORK**

Framework dùng descriptive names cho hầu hết mọi concept:
- Chunk-Miss, Gap-Direction, Prediction-Delta, By-Product-Gap-Resonance
- Entity-Compiled, Resonance-Sustainability, Hidden-Quality-Perception
- CHỈ Type A/B reward là dùng label không mang nghĩa

**③ FILE GỐC ĐÃ CÓ TÊN SẴN**

Reward-Signal-Architecture.md §1.1 đã viết:
- "TYPE A — EVALUATIVE CONFIRM"
- "TYPE B — DIRECT STATE CONFIRM"

→ Chỉ cần nâng lên thành tên chính thức.

---

## §1 — ĐỊNH NGHĨA TÊN MỚI

### §1.1 — Tên chính thức

```
  ┌──────────────────┬──────────────────────┬──────────────────────────┐
  │ Hiện tại         │ Tên mới              │ Lý do                    │
  ├──────────────────┼──────────────────────┼──────────────────────────┤
  │ Type A reward    │ Evaluative Reward    │ Reward từ evaluation.    │
  │                  │                      │ Opioid-based. Cần H10.  │
  │                  │                      │ Đã dùng "Evaluative     │
  │                  │                      │ Confirm" trong file gốc. │
  ├──────────────────┼──────────────────────┼──────────────────────────┤
  │ Type B reward    │ Direct-State Reward  │ Body-state change trực   │
  │                  │                      │ tiếp = reward. Non-opioid│
  │                  │                      │ Hardware. Ít habituate.  │
  │                  │                      │ Đã dùng "Direct State   │
  │                  │                      │ Confirm" trong file gốc. │
  └──────────────────┴──────────────────────┴──────────────────────────┘
```

### §1.2 — Viết hoa / viết thường

```
  ⭐ QUY TẮC:

  Evaluative Reward / Direct-State Reward = CAPITALIZED (concept name)
  → Nhất quán với: Entity-Compiled, Gap-Direction, Prediction-Delta, ...

  Viết tắt contextual (khi context ĐÃ rõ là reward):
  → "Evaluative" / "Direct-State" — OK (giống "Background" cho Background-Pattern)
  → KHÔNG bao giờ viết tắt thành ER/DSR/E/DS

  Tổ hợp:
  → "Evaluative/Direct-State" thay cho "Type A/B"
  → "Evaluative complexity gradient" thay cho "Type A complexity gradient"
```

### §1.3 — A₀→A₃ → E₀→E₃: ĐỔI NOTATION

```
  ⭐ A₀→A₃ → E₀→E₃ (E = Evaluative)

  ┌──────────┬──────────┬──────────────────────────────────┐
  │ Hiện tại │ Mới      │ Nghĩa                            │
  ├──────────┼──────────┼──────────────────────────────────┤
  │ A₀       │ E₀       │ Hardware-installed evaluation     │
  │ A₁       │ E₁       │ Simple compiled evaluation        │
  │ A₂       │ E₂       │ Domain-specific expertise         │
  │ A₃       │ E₃       │ Cross-domain insight/creativity   │
  └──────────┴──────────┴──────────────────────────────────┘

  LÝ DO ĐỔI:
  ① "A" trong A₀ = "Type A" — nếu Type A không còn, "A₀" trở thành
     notation mồ côi, không ai biết "A" nghĩa gì
  ② "E₀" = Evaluative Level 0 — tự giải thích, nhất quán với tên mới
  ③ Cùng độ dài (A₀ vs E₀) — KHÔNG phá layout tables/formulas
  ④ Active scope nhỏ: ~17 files, ~133 replacements
     (460 total nhưng phần lớn ở backup/drill files — SKIP)
  ⑤ Hầu hết files ĐÃ NẰM trong session plan (gộp chung, không tốn thêm)

  CÁCH THAY:
  → A₀ → E₀, A₁ → E₁, A₂ → E₂, A₃ → E₃
  → "A₀→A₃" → "E₀→E₃"
  → "A₀→A₃ complexity gradient" → "E₀→E₃ Evaluative complexity gradient"
  → Headers: "§2 — E₀→E₃: EVALUATIVE COMPLEXITY GRADIENT"
```

### §1.4 — Compound terms

```
  ┌──────────────────────────┬──────────────────────────────────────┐
  │ Hiện tại                 │ Sau rename                           │
  ├──────────────────────────┼──────────────────────────────────────┤
  │ Type A reward            │ Evaluative Reward                    │
  │ Type B reward            │ Direct-State Reward                  │
  │ Type A/B                 │ Evaluative/Direct-State              │
  │ Type A/B reward          │ Evaluative/Direct-State Reward       │
  │ Type A vs Type B         │ Evaluative vs Direct-State           │
  │                          │ (hoặc: Evaluative Reward vs          │
  │                          │  Direct-State Reward nếu cần rõ)     │
  │ A Gates B                │ Evaluative Gates Direct-State        │
  │ A/B ratio                │ Evaluative/Direct-State ratio        │
  │ Type A pathway           │ Evaluative pathway                   │
  │ Type B pathway           │ Direct-State pathway                 │
  │ Type A dominant          │ Evaluative dominant                  │
  │ Type B dominant          │ Direct-State dominant                │
  │ pure B                   │ pure Direct-State                    │
  │ A₀→A₃                   │ E₀→E₃ (xem §1.3)                    │
  │ A₀ / A₁ / A₂ / A₃      │ E₀ / E₁ / E₂ / E₃                   │
  │ 5 Profiles               │ 5 Profiles (KHÔNG ĐỔI)              │
  └──────────────────────────┴──────────────────────────────────────┘
```

---

## §2 — QUY TẮC THAY THẾ

### §2.1 — PHẢI thay

```
  ① "Type A" khi nói về REWARD (evaluative, opioid) → "Evaluative Reward"
  ② "Type B" khi nói về REWARD (direct state, non-opioid) → "Direct-State Reward"
  ③ "Type A/B" khi nói về REWARD → "Evaluative/Direct-State"
  ④ Headers/titles chứa "Type A" / "Type B" reward → đổi tương ứng
  ⑤ Frontmatter (scope, purpose, dependencies) chứa "Type A/B" → đổi
  ⑥ A₀ → E₀, A₁ → E₁, A₂ → E₂, A₃ → E₃ (gradient notation)
```

### §2.2 — KHÔNG thay

```
  ① "Type A" / "Loại A" khi nói về COMPILE TAXONOMY → GIỮ NGUYÊN
     (Compile-Type-Learning.md, Compile-Taxonomy.md, ...)
  ② A₀, A₁, A₂, A₃ → E₀, E₁, E₂, E₃ (đổi cùng lúc — xem §1.3)
  ③ Profile ①-⑤ → KHÔNG ĐỔI
  ④ Backup files (backup/, _backup/) → KHÔNG SỬA
  ⑤ Drill files (backup/Drill-*) → KHÔNG SỬA (historical record)
  ⑥ "Type C" (Compile Taxonomy) → KHÔNG LIÊN QUAN, giữ nguyên
```

### §2.3 — CẦN REVIEW CẨN THẬN (mixed context)

```
  Một số files dùng "Type A" cho CẢ 2 contexts (Reward VÀ Compile):

  ⚠️ Body-Base.md — §4 references Compile Taxonomy, other sections = Reward
  ⚠️ Collective-Body.md — references cả 2 systems
  ⚠️ Core-Software.md — header references cả 2
  ⚠️ PFC-Operations.md — references cả 2
  ⚠️ Self-Created-Threat.md — "Type C" = Compile, but cũng reference Reward

  → MỖI OCCURRENCE cần đọc context trước khi thay
  → KHÔNG dùng replace_all cho các files này
```

---

## §3 — FILE INVENTORY (ACTIVE FILES ONLY)

### §3.1 — Tổng quan

```
  Total active files cần sửa:  ~60 files
  Total estimated replacements: ~500-600 (reward-specific)
  Backup/Drill files (SKIP):   ~50+ files

  KHÔNG SỬA:
  → Compile-Type-Learning.md (89 "Type A" = ALL Compile types)
  → Compile-Taxonomy.md (Compile definition)
  → Mọi file trong backup/, _backup/
```

### §3.2 — Cluster 1: CORE DEFINITION (Session 1)

```
  ⭐ PRIORITY HIGHEST — Establish new names tại đây TRƯỚC.
  Các file khác reference tới cluster này.

  ┌───┬────────────────────────────────────────────┬───────┬──────────┐
  │ # │ File                                       │ ~repl │ Note     │
  ├───┼────────────────────────────────────────────┼───────┼──────────┤
  │ 1 │ Body-Feedback/Reward-Signal-Architecture.md│ ~162  │ PRIMARY  │
  │   │                                            │       │ +72 E₀E₃ │
  │ 2 │ Body-Feedback/Body-Feedback-Label.md       │ ~33   │ VOCAB    │
  │   │                                            │       │ +7 E₀E₃  │
  │ 3 │ Body-Feedback/03-Reward.md                 │ ~4    │          │
  │ 4 │ Body-Feedback/Body-Feedback.md             │ ~28   │ +7 E₀E₃  │
  │ 5 │ Body-Feedback/Body-Feedback-Mechanism.md   │ ~11   │ +1 E₀E₃  │
  ├───┼────────────────────────────────────────────┼───────┼──────────┤
  │   │ SUBTOTAL                                   │ ~238  │ 5 files  │
  └───┴────────────────────────────────────────────┴───────┴──────────┘
```

### §3.3 — Cluster 2: BODY-FEEDBACK FOLDER (Session 2)

```
  ┌───┬────────────────────────────────────────────┬───────┬──────────┐
  │ # │ File                                       │ ~repl │ Note     │
  ├───┼────────────────────────────────────────────┼───────┼──────────┤
  │ 6 │ Body-Feedback/Gap-Body-Need.md             │ ~59   │ +8 E₀E₃  │
  │ 7 │ Body-Feedback/Reward-Calibration.md        │ ~42   │ +18 E₀E₃ │
  │ 8 │ Body-Feedback/Gap-Distribution-Profile.md  │ ~16   │          │
  │ 9 │ Body-Feedback/Hidden-Quality-Perception.md │ ~5    │ CHECK    │
  ├───┼────────────────────────────────────────────┼───────┼──────────┤
  │   │ SUBTOTAL                                   │ ~122  │ 4 files  │
  └───┴────────────────────────────────────────────┴───────┴──────────┘
```

### §3.4 — Cluster 3: BODY-BASE + FEELING (Session 3)

```
  ┌───┬────────────────────────────────────────────┬───────┬──────────┐
  │ # │ File                                       │ ~repl │ Note     │
  ├───┼────────────────────────────────────────────┼───────┼──────────┤
  │10 │ Body-Base/Why-Body-Knows.md                │ ~25   │ +13 E₀E₃ │
  │11 │ Body-Base/Valence-Propagation.md           │ ~13   │          │
  │12 │ Body-Base/Body-Coupling.md                 │ ~3    │          │
  │13 │ Body-Base/Body-Base.md                     │ ~4    │ ⚠️ MIXED │
  │14 │ Feeling/Feeling.md                         │ ~17   │ +7 E₀E₃  │
  │15 │ Feeling/Feeling-Mechanism-Deep.md          │ ~10   │          │
  ├───┼────────────────────────────────────────────┼───────┼──────────┤
  │   │ SUBTOTAL                                   │ ~72   │ 6 files  │
  └───┴────────────────────────────────────────────┴───────┴──────────┘
```

### §3.5 — Cluster 4: PFC + AGENT-MECHANISM (Session 4)

```
  ┌───┬────────────────────────────────────────────┬───────┬──────────┐
  │ # │ File                                       │ ~repl │ Note     │
  ├───┼────────────────────────────────────────────┼───────┼──────────┤
  │16 │ PFC/PFC-Hardware.md                        │ ~11   │          │
  │17 │ PFC/PFC-Configuration.md                   │ ~11   │          │
  │18 │ PFC/PFC-Operations.md                      │ ~4    │ ⚠️ MIXED │
  │19 │ PFC/Logic-Feeling.md                       │ ~10   │          │
  │20 │ PFC/Imagination/Imagine-Final.md           │ ~2    │          │
  │21 │ Agent-Mechanism/Resonance-Per-Entity.md    │ ~14   │          │
  │22 │ Agent-Mechanism/Agent-Mechanism.md         │ ~9    │          │
  │23 │ Agent-Mechanism/Resonance-Sustainability.md│ ~3    │          │
  ├───┼────────────────────────────────────────────┼───────┼──────────┤
  │   │ SUBTOTAL                                   │ ~64   │ 8 files  │
  └───┴────────────────────────────────────────────┴───────┴──────────┘
```

### §3.6 — Cluster 5: OTHER CORE (Session 5)

```
  ┌───┬────────────────────────────────────────────┬───────┬──────────┐
  │ # │ File                                       │ ~repl │ Note     │
  ├───┼────────────────────────────────────────────┼───────┼──────────┤
  │24 │ Core-Software.md                           │ ~5    │ ⚠️ MIXED │
  │25 │ Collective/Collective-Body.md              │ ~6    │ ⚠️ MIXED │
  │26 │ Blackbox-Map.md                            │ ~3    │          │
  │27 │ Clarification/Dopamine-Is-Not-Reward.md    │ ~6    │          │
  │28 │ Clarification/Prediction-Error-Is-Not-Rew..│ ~6    │          │
  │29 │ Observation/Connection.md                  │ ~4    │          │
  │30 │ Observation/Gratitude.md                   │ ~2    │          │
  │31 │ 01-File-Index.md (Core-Deep-Dive)          │ ~7    │          │
  │32 │ plan-abbreviation-cleanup.md               │ ~1    │          │
  ├───┼────────────────────────────────────────────┼───────┼──────────┤
  │   │ SUBTOTAL                                   │ ~40   │ 9 files  │
  └───┴────────────────────────────────────────────┴───────┴──────────┘
```

### §3.7 — Cluster 6: RESEARCH — Heavy files (Session 6)

```
  ┌───┬────────────────────────────────────────────┬───────┬──────────┐
  │ # │ File                                       │ ~repl │ Note     │
  ├───┼────────────────────────────────────────────┼───────┼──────────┤
  │33 │ Climate-Cognition.md                       │ ~61   │ DENSE    │
  │34 │ Love-Romantic.md                           │ ~26   │          │
  │35 │ Addiction-Analysis.md                      │ ~33   │ DENSE    │
  │36 │ Fidgeting-Analysis.md                      │ ~10   │          │
  ├───┼────────────────────────────────────────────┼───────┼──────────┤
  │   │ SUBTOTAL                                   │ ~130  │ 4 files  │
  └───┴────────────────────────────────────────────┴───────┴──────────┘
```

### §3.8 — Cluster 7: RESEARCH — Remaining (Session 7)

```
  ┌───┬────────────────────────────────────────────┬───────┬──────────┐
  │ # │ File                                       │ ~repl │ Note     │
  ├───┼────────────────────────────────────────────┼───────┼──────────┤
  │37 │ Self-Created-Threat.md                     │ ~5    │          │
  │38 │ Melody-Technology/Religion.md              │ ~10   │          │
  │39 │ Melody-Technology/Idol-Phenomenon.md       │ ~8    │          │
  │40 │ Melody-Technology/Melody-Technology-Overv.. │ ~4    │          │
  │41 │ Money-Analysis.md                          │ ~4    │          │
  │42 │ Health/Hijack/Nicotine-Brain-Mechanism.md  │ ~3    │          │
  │43 │ Health/Neurodiversity/Autism-Observation.md│ ~1    │          │
  │44 │ Health/PTSD-Analysis.md                    │ ~1    │          │
  │45 │ Human-Learning/Money-Education.md          │ ~2    │          │
  │46 │ Neuro-Measurement/00-Goals.md              │ ~3    │          │
  │47 │ Quote-Analysis/Work-Stay-Hungry-Stay-Fool..│ ~1    │          │
  │48 │ Sensitivity-Classification.md              │ ~5    │          │
  │49 │ 01-File-Index.md (Research)                │ ~4    │          │
  ├───┼────────────────────────────────────────────┼───────┼──────────┤
  │   │ SUBTOTAL                                   │ ~51   │ 13 files │
  └───┴────────────────────────────────────────────┴───────┴──────────┘
```

### §3.9 — Cluster 8: APPLICATIONS + PUBLIC + CHILD-DEV (Session 8)

```
  ┌───┬────────────────────────────────────────────┬───────┬──────────┐
  │ # │ File                                       │ ~repl │ Note     │
  ├───┼────────────────────────────────────────────┼───────┼──────────┤
  │50 │ Education/Hardware-Calibration.md          │ ~8    │          │
  │51 │ Education/VN/VN-Recommendations.md         │ ~15   │          │
  │52 │ Education/VN/VN-Education-Status.md        │ ~9    │          │
  │53 │ Education/Curriculum-Framework.md          │ ~11   │          │
  │54 │ Education/Education-System.md              │ ~8    │          │
  │55 │ Education/Era-Analysis-2025.md             │ ~5    │          │
  │56 │ Education/00_Overview.md                   │ ~3    │          │
  │57 │ Applications/01-File-Index.md              │ ~2    │          │
  │58 │ Public-Plan/plan-public.md                 │ ~9    │          │
  │59 │ Public-Plan/summary-paper-outline.md       │ ~1    │          │
  │60 │ Child-Chunk-Development/ (5-6 files, 1-2ea)│ ~8    │          │
  │61 │ Chunk-Internal-Processing/ (2 files)       │ ~3    │          │
  ├───┼────────────────────────────────────────────┼───────┼──────────┤
  │   │ SUBTOTAL                                   │ ~82   │ ~14 files│
  └───┴────────────────────────────────────────────┴───────┴──────────┘
```

### §3.10 — Files KHÔNG SỬA

```
  ⭐ SKIP HOÀN TOÀN:

  ① Compile-Type-Learning.md (89 "Type A" = ALL Compile types, KHÔNG phải Reward)
  ② Compile-Taxonomy.md (Compile definition — "Loại A/B/C")
  ③ Mọi file trong backup/ và _backup/ (~50+ files)
  ④ Drill files (historical record)
  ⑤ Mismatch-Patterns/backup/Mismatch-Patterns.md (backup)
  ⑥ Love-Romantic-v2.4-backup.md (backup)
  ⑦ Tất cả *-backup.md files
```

---

## §4 — SESSION PLAN

```
  ┌─────────┬────────────────────────────────┬───────┬────────┬──────────┐
  │ Session │ Cluster                        │ Files │ ~Repl  │ Priority │
  ├─────────┼────────────────────────────────┼───────┼────────┼──────────┤
  │ S1      │ Core Definition                │ 5     │ ~238   │ ⭐⭐⭐     │
  │ S2      │ Body-Feedback folder           │ 4     │ ~122   │ ⭐⭐⭐     │
  │ S3      │ Body-Base + Feeling            │ 6     │ ~72    │ ⭐⭐       │
  │ S4      │ PFC + Agent-Mechanism          │ 8     │ ~66    │ ⭐⭐       │
  │ S5      │ Other Core                     │ 9     │ ~41    │ ⭐⭐       │
  │ S6      │ Research heavy                 │ 4     │ ~133   │ ⭐        │
  │ S7      │ Research remaining             │ 13    │ ~54    │ ⭐        │
  │ S8      │ App + Public + Child-Dev       │ ~14   │ ~85    │ ⭐        │
  ├─────────┼────────────────────────────────┼───────┼────────┼──────────┤
  │ TOTAL   │                                │ ~63   │ ~811   │          │
  └─────────┴────────────────────────────────┴───────┴────────┴──────────┘

  Mỗi session:
  1. Đọc file → xác nhận context (Reward vs Compile)
  2. Thay thế Type A/B + A₀→A₃ → E₀→E₃ (edit hoặc replace_all nếu THUẦN reward)
  3. Grep verify: 0 remaining "Type A"/"Type B" reward + 0 remaining A₀/A₁/A₂/A₃
  4. Grep confirm: "Evaluative Reward" + "Direct-State Reward" + "E₀" tồn tại
```

---

## §5 — EDGE CASES + QUY TẮC ĐẶC BIỆT

### §5.1 — Mixed-context files

```
  5 files có CẢ Reward "Type A" VÀ Compile "Type A/Loại A":

  ┌──────────────────────────┬──────────────────────────────────────┐
  │ File                     │ Approach                             │
  ├──────────────────────────┼──────────────────────────────────────┤
  │ Body-Base.md             │ §4 = Compile refs → SKIP.            │
  │                          │ Other sections = Reward → RENAME.    │
  ├──────────────────────────┼──────────────────────────────────────┤
  │ Core-Software.md         │ Header/dependency = both systems.    │
  │                          │ Read context per occurrence.         │
  ├──────────────────────────┼──────────────────────────────────────┤
  │ Collective-Body.md       │ §2 = Compile. Other = Reward.       │
  │                          │ Read context per occurrence.         │
  ├──────────────────────────┼──────────────────────────────────────┤
  │ PFC-Operations.md        │ References both systems.             │
  │                          │ Read context per occurrence.         │
  ├──────────────────────────┼──────────────────────────────────────┤
  │ Self-Created-Threat.md   │ "Type C" = Compile. But cũng has    │
  │                          │ Reward Type A/B refs → rename those. │
  └──────────────────────────┴──────────────────────────────────────┘

  → KHÔNG dùng replace_all cho các files này
  → Mỗi occurrence = read context → decide
```

### §5.2 — Header / title patterns

```
  Hiện tại:
    "## §1 — TYPE A/B: 2 LOẠI BODY-BASE CONFIRM SIGNAL"
    "### §1.1 — Core distinction"
    "Type A/B + 5 Profiles + Interaction Model"

  Sau rename:
    "## §1 — EVALUATIVE/DIRECT-STATE: 2 LOẠI BODY-BASE CONFIRM SIGNAL"
    "Evaluative/Direct-State Reward + 5 Profiles + Interaction Model"
    (hoặc ngắn hơn nếu header quá dài)
```

### §5.3 — Table cells

```
  Tables thường có columns "Type A" / "Type B":

  Hiện:    │ Type A          │ Type B         │
  Sau:     │ Evaluative      │ Direct-State   │

  → Trong table: dùng short form ("Evaluative" / "Direct-State")
  → KHÔNG cần viết full "Evaluative Reward" trong table cell
  → Table header hoặc caption nên nói rõ context
```

### §5.4 — Inline formulas / code blocks

```
  Hiện: "Type A = evaluative, opioid-based"
  Sau:  "Evaluative Reward = opioid-based" (bỏ "= evaluative" vì redundant)

  Hiện: "f(Type A × chunk_library)"
  Sau:  "f(Evaluative × chunk_library)"
```

### §5.5 — Cross-references dạng "(Reward-Signal-Architecture §1: Type A/B)"

```
  → Đổi thành: "(Reward-Signal-Architecture §1: Evaluative/Direct-State)"
  → Nhất quán với tên mới
```

---

## §6 — VERIFICATION

### §6.1 — Sau mỗi session

```
  grep "Type A" [files-in-cluster] — kiểm tra 0 reward-context remaining
  grep "Type B" [files-in-cluster] — kiểm tra 0 reward-context remaining

  ⚠️ Lưu ý: grep có thể vẫn thấy "Type A" trong mixed-context files
     → Đó là COMPILE refs → OK, không cần sửa
     → Verify bằng cách đọc context
```

### §6.2 — Sau session cuối (FINAL VERIFY)

```
  Toàn bộ framework (trừ backup/):

  ① grep "Type A" — kiểm tra MỌI remaining = Compile context ONLY
  ② grep "Type B" — kiểm tra = 0 (Type B chỉ dùng cho Reward, không Compile)
  ③ grep "Evaluative Reward" — xác nhận tồn tại ở các files đã sửa
  ④ grep "Direct-State Reward" — xác nhận tồn tại ở các files đã sửa
  ⑤ grep "A₀\|A₁\|A₂\|A₃" — kiểm tra = 0 trong active files
     (tất cả đã đổi thành E₀/E₁/E₂/E₃)
  ⑥ grep "E₀" — xác nhận notation mới tồn tại

  Type B = indicator tốt nhất:
    → Compile system KHÔNG CÓ "Type B" (chỉ Loại A/B/C)
    → Nếu còn "Type B" = chắc chắn chưa sửa hết
    → grep "Type B" = 0 trong active files = ĐÃ XONG
```

---

## §7 — GHI CHÚ BỔ SUNG

### §7.1 — Compile-Taxonomy "Loại A/B/C" — KHÔNG trong scope

```
  Plan này CHỈ rename REWARD Type A/B.
  Compile-Taxonomy "Loại A/B/C" vẫn giữ nguyên.

  TƯƠNG LAI (separate plan nếu cần):
  → Loại A → "Direct-Experience Compile" (?)
  → Loại B → "Expertise Compile" (?)
  → Loại C → "Trust-Install Compile" (?)
  → Nhưng: "Loại" (Vietnamese) vs "Type" (English) đã phân biệt PHẦN NÀO
  → SAU KHI Reward rename xong, evaluate xem Compile có cần rename không
```

### §7.2 — Version bump policy

```
  Files có version trong frontmatter:
  → KHÔNG bump version chỉ vì rename terminology
  → Rename = maintenance, không phải content change
  → Chỉ note trong frontmatter: "terminology: Type A/B → Evaluative/Direct-State"
  → Giống cách abbreviation cleanup đã xử lý
```

### §7.3 — Precedent

```
  Framework đã thực hiện renames tương tự thành công:

  ① SPM cleanup: 2,468 repl, 105 files, 1 session
     (Self-Pattern-Match → Self-Pattern-Modeling)

  ② Abbreviation cleanup: ~2,280 repl, ~95 files, 8 sessions
     (30 framework abbreviations → full names)

  ③ By-Product-Gap-Resonance rename: ~1,200 repl, ~82 files
     ("Pattern Resonance" → "By-Product-Gap-Resonance")

  → Precedent rõ ràng. Quy trình đã proven.
  → ~800 repl, ~63 files = nhỏ hơn các lần trước.
  → DUY NHẤT khác biệt: cần PHÂN BIỆT Reward vs Compile context.
```

---

> *Plan: Reward Type Rename — Type A/B → Evaluative/Direct-State.*
> *~60 active files. ~650-800 replacements. 8 sessions.*
> *Core rule: Type A → Evaluative Reward. Type B → Direct-State Reward.*
> *A₀→A₃ → E₀→E₃ (E = Evaluative). Compile Loại A/B/C không đổi.*
> *"Type B" = 0 + "A₀" = 0 trong active files = DONE indicator.*
