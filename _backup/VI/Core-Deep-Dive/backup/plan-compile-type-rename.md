# Plan: Compile Type Rename — Loại A/B/C → Experience/Expertise/Trust Compile

```
Status:    🔲 NOT STARTED (chạy SAU plan-reward-type-rename.md)
Created:   2026-05-23
Scope:     ~40 active files, ~400-500 replacements
Approach:  CLUSTER-BY-CLUSTER (Core Definition → Deep-Dive → Research → Application)
Depends:   plan-reward-type-rename.md PHẢI XONG TRƯỚC
Verify:    grep "Type A/B/C" + "Loại A/B/C" = 0 trong active files sau khi hoàn thành
```

---

## §0 — TẠI SAO ĐỔI TÊN

### 3 lý do chính

**① CÙNG LÝ DO VỚI REWARD — GENERIC LETTER LABELS KHÔNG MANG NGHĨA**

```
  "Loại A" — trải nghiệm trực tiếp? hay cái gì khác?
  "Loại C" — trust install? hay compile complex?
  → Phải tra bảng mỗi lần gặp

  "Experience Compile" — ngay lập tức hiểu: compile qua trải nghiệm
  "Trust Compile" — ngay lập tức hiểu: compile qua trust
  → Tự giải thích, không cần tra bảng
```

**② SAU REWARD RENAME, "Type A" CÒN LẠI = CHỈ COMPILE → VẪN MƠ HỒ**

```
  Sau plan-reward-type-rename.md:
  → "Type A" (reward) ĐÃ BIẾN MẤT → thành "Evaluative Reward"
  → "Type A" CÒN LẠI = chỉ Compile context
  → NHƯNG vẫn là generic "A" — ai biết "A" nghĩa gì?

  File Compile-Type-Learning.md: 164 occurrences "Type A/B/C"
  File Compile-Taxonomy.md CHÍNH NÓ cũng dùng "Type A" (line 391)
  → Rename compile types → HOÀN TOÀN loại bỏ generic letter labels
```

**③ FILE GỐC ĐÃ CÓ DESCRIPTIVE SUBTITLES**

```
  Compile-Taxonomy.md:
  → §2.1: "Loại A: Direct Short Compile"
  → §2.2: "Loại B: Compiled Expertise"
  → §2.3: "Loại C: Installed + Collective"

  → Chỉ cần nâng lên thành tên chính thức.
```

---

## §1 — ĐỊNH NGHĨA TÊN MỚI

### §1.1 — Tên chính thức

```
  ┌──────────┬────────────────────┬──────────────────────────────────┐
  │ Hiện tại │ Tên mới            │ Lý do                            │
  ├──────────┼────────────────────┼──────────────────────────────────┤
  │ Loại A   │ Experience Compile │ Compile qua trải nghiệm trực    │
  │          │                    │ tiếp. Body experience → body     │
  │          │                    │ compile. ~90% behavior.          │
  │          │                    │ (§2.1 "Direct Short Compile")    │
  ├──────────┼────────────────────┼──────────────────────────────────┤
  │ Loại B   │ Expertise Compile  │ PFC-directed compile qua nhiều  │
  │          │                    │ năm → expert intuition. ~5%.     │
  │          │                    │ (§2.2 "Compiled Expertise")      │
  ├──────────┼────────────────────┼──────────────────────────────────┤
  │ Loại C   │ Trust Compile      │ Trust source → compile short +   │
  │          │                    │ collective hold long. ~85%+      │
  │          │                    │ social behavior.                 │
  │          │                    │ (§2.3 "Installed + Collective")  │
  └──────────┴────────────────────┴──────────────────────────────────┘

  Pattern: [Descriptor] Compile — nhất quán với:
    [Evaluative] Reward, [Direct-State] Reward (plan-reward-type-rename.md)
    [Experience] Compile, [Expertise] Compile, [Trust] Compile
    = Descriptor trước, Category sau
```

### §1.2 — Viết hoa / viết thường

```
  ⭐ QUY TẮC:

  Experience Compile / Expertise Compile / Trust Compile = CAPITALIZED
  → Nhất quán với Evaluative Reward, Direct-State Reward

  Short form contextual (khi context ĐÃ rõ là compile):
  → "Experience" / "Expertise" / "Trust" — OK
  → KHÔNG viết tắt thành EC/ExC/TC

  Tổ hợp:
  → "Experience/Trust Compile" thay cho "Loại A/C"
  → "3 Compile Types" thay cho "3 Loại"
```

### §1.3 — Compound terms

```
  ┌──────────────────────────────┬──────────────────────────────────┐
  │ Hiện tại                     │ Sau rename                       │
  ├──────────────────────────────┼──────────────────────────────────┤
  │ Loại A / Type A (compile)    │ Experience Compile               │
  │ Loại B / Type B (compile)    │ Expertise Compile                │
  │ Loại C / Type C              │ Trust Compile                    │
  │ 3 Loại / 3 Loại Compile      │ 3 Compile Types                  │
  │ Loại A + C                   │ Experience + Trust Compile        │
  │ Loại A vs Loại C             │ Experience vs Trust Compile       │
  │ Type C chain break           │ Trust Compile chain break         │
  │ Type C installed             │ Trust Compile installed           │
  │ Loại B = expert domain       │ Expertise Compile = expert domain│
  │ "Type C trust-compile"       │ "Trust Compile" (bỏ redundant)   │
  │ compile ngắn (Loại A)        │ compile ngắn (Experience)        │
  └──────────────────────────────┴──────────────────────────────────┘
```

---

## §2 — QUY TẮC THAY THẾ

### §2.1 — PHẢI thay

```
  ① "Loại A" (compile context) → "Experience Compile"
  ② "Loại B" (compile context) → "Expertise Compile"
  ③ "Loại C" (compile context) → "Trust Compile"
  ④ "Type A" (compile context, CÒN LẠI sau Reward rename) → "Experience Compile"
  ⑤ "Type B" (compile context, nếu còn) → "Expertise Compile"
  ⑥ "Type C" → "Trust Compile" (Type C = LUÔN compile, không ambiguity)
  ⑦ "3 Loại" / "3 loại" (compile context) → "3 Compile Types"
  ⑧ Headers/titles chứa Loại A/B/C → đổi tương ứng
  ⑨ Frontmatter chứa Loại/Type A/B/C compile refs → đổi
```

### §2.2 — KHÔNG thay

```
  ① Backup files (backup/, _backup/) → KHÔNG SỬA
  ② Drill files (backup/Drill-*) → KHÔNG SỬA (historical record)
  ③ "loại" khi dùng như từ thông thường (ví dụ: "loại bỏ", "phân loại")
     → CHỈ đổi khi "Loại A/B/C" = compile taxonomy label
  ④ "3 loại" khi không nói về compile taxonomy (ví dụ: "3 loại tế bào")
```

### §2.3 — CẦN REVIEW CẨN THẬN

```
  ⚠️ "Loại" = từ thông thường trong tiếng Việt
     → grep "Loại A" có thể catch "Loại A" compile VÀ "loại A" khác
     → MỖI occurrence cần đọc context
     → Tuy nhiên: "Loại A" (capital L, viết hoa) hầu như luôn = compile taxonomy

  ⚠️ Files đã xử lý trong plan-reward-type-rename.md:
     → "Type A" reward ĐÃ đổi → CÒN LẠI = compile
     → Nhưng vẫn cần verify context

  ⚠️ "Type C" = LUÔN compile → an toàn nhất để replace_all
     → KHÔNG CÓ "Type C" nào trong Reward system
```

---

## §3 — ORDERING: CHẠY SAU REWARD RENAME

```
  ⭐ CRITICAL: Plan này PHẢI chạy SAU plan-reward-type-rename.md HOÀN TẤT.

  LÝ DO:
  ① Plan Reward đổi "Type A" (reward) → "Evaluative Reward"
  ② Sau đó, "Type A" CÒN LẠI = chỉ compile context
  ③ Plan này đổi "Type A" CÒN LẠI → "Experience Compile"
  ④ = Không bao giờ có ambiguity

  NẾU CHẠY SONG SONG hoặc ĐẢO THỨ TỰ:
  → Không biết "Type A" nào là Reward, nào là Compile
  → Dễ sửa nhầm → chất lượng giảm

  THỨ TỰ:
  1. plan-reward-type-rename.md — ALL 8 sessions XONG
  2. VERIFY: grep "Type A" = chỉ compile context remaining
  3. plan-compile-type-rename.md — bắt đầu (file này)
```

---

## §4 — FILE INVENTORY (ACTIVE FILES ONLY)

### §4.1 — Tổng quan

```
  Total active files:          ~40 files
  Total estimated replacements: ~400-500
  Backup/Drill files (SKIP):   ~30+ files

  PATTERN DISTRIBUTION:
  → "Loại A/B/C":   ~200 occ / ~27 active files
  → "Type C":        ~210 occ / ~22 active files  (EXCLUSIVELY compile)
  → "Type A/B" (compile, remaining after Reward rename): ~50-100 occ / ~5-10 files
  → "3 Loại":        ~30 occ / ~15 files

  BIGGEST FILES:
  → Compile-Type-Learning.md:        ~164 occ (Type A/B/C)
  → Compile-Taxonomy.md:             ~59 occ (Loại A/B/C)
  → AI-Schema-Detection.md:          ~34 occ (Loại A/B/C)
  → Hidden-Quality-Perception.md:    ~32 occ (Loại A/B/C)
  → Coordination-Node.md:            ~26 occ (Loại A/B/C)
```

### §4.2 — Cluster 1: CORE DEFINITION (Session 1)

```
  ⭐ PRIORITY HIGHEST — Establish new names tại đây.

  ┌───┬────────────────────────────────────────────┬───────┬──────────┐
  │ # │ File                                       │ ~repl │ Note     │
  ├───┼────────────────────────────────────────────┼───────┼──────────┤
  │ 1 │ Chunk/Compile-Taxonomy.md                  │ ~76   │ PRIMARY  │
  │   │                                            │       │ 59 Loại  │
  │   │                                            │       │ +15 "3L" │
  │   │                                            │       │ +2 Type  │
  │ 2 │ Body-Base/Body-Base.md                     │ ~7    │ §4 refs  │
  │ 3 │ Core-Software.md                           │ ~11   │ header   │
  │ 4 │ Core-Hardware.md                           │ ~2    │          │
  ├───┼────────────────────────────────────────────┼───────┼──────────┤
  │   │ SUBTOTAL                                   │ ~96   │ 4 files  │
  └───┴────────────────────────────────────────────┴───────┴──────────┘
```

### §4.3 — Cluster 2: COMPILE APPLICATION FILE (Session 2)

```
  ⭐ FILE LỚN NHẤT — cần session riêng.

  ┌───┬────────────────────────────────────────────┬───────┬──────────┐
  │ # │ File                                       │ ~repl │ Note     │
  ├───┼────────────────────────────────────────────┼───────┼──────────┤
  │ 5 │ Education/Compile-Type-Learning.md         │ ~167  │ DENSE    │
  │   │                                            │       │ 164 Type │
  │   │                                            │       │ +3 Loại  │
  ├───┼────────────────────────────────────────────┼───────┼──────────┤
  │   │ SUBTOTAL                                   │ ~167  │ 1 file   │
  └───┴────────────────────────────────────────────┴───────┴──────────┘
```

### §4.4 — Cluster 3: COLLECTIVE + OBSERVATION (Session 3)

```
  ┌───┬────────────────────────────────────────────┬───────┬──────────┐
  │ # │ File                                       │ ~repl │ Note     │
  ├───┼────────────────────────────────────────────┼───────┼──────────┤
  │ 6 │ Collective/Coordination-Node.md            │ ~26   │          │
  │ 7 │ Collective/Collective-Body.md              │ ~19   │ +8 TypeC │
  │ 8 │ Collective/Collective-Arc-Dynamics.md      │ ~1    │          │
  │ 9 │ Observation/AI-Schema-Detection.md         │ ~34   │ DENSE    │
  │10 │ Observation/Gratitude.md                   │ ~14   │ Type C   │
  │11 │ Observation/Meaning.md                     │ ~1    │          │
  ├───┼────────────────────────────────────────────┼───────┼──────────┤
  │   │ SUBTOTAL                                   │ ~95   │ 6 files  │
  └───┴────────────────────────────────────────────┴───────┴──────────┘
```

### §4.5 — Cluster 4: BODY-BASE + AGENT-MECHANISM (Session 4)

```
  ┌───┬────────────────────────────────────────────┬───────┬──────────┐
  │ # │ File                                       │ ~repl │ Note     │
  ├───┼────────────────────────────────────────────┼───────┼──────────┤
  │12 │ Body-Feedback/Hidden-Quality-Perception.md │ ~32   │ DENSE    │
  │13 │ Agent-Mechanism/Entity-Compiled.md         │ ~11   │          │
  │14 │ Agent-Mechanism/By-Product-Gap-Resonance.md│ ~4    │          │
  │15 │ Body-Coupling.md                           │ ~3    │          │
  │16 │ Chunk/Background-Pattern.md                │ ~1    │          │
  │17 │ PFC/PFC-Operations.md                      │ ~6    │          │
  │18 │ Body-Feedback/Gap-Distribution-Profile.md  │ ~5    │ Type C   │
  │19 │ Body-Feedback/Gap-Body-Need.md             │ ~1    │ Type C   │
  │20 │ Chunk-Internal/03-Chain-Anchor-Decay.md    │ ~1    │ Type C   │
  ├───┼────────────────────────────────────────────┼───────┼──────────┤
  │   │ SUBTOTAL                                   │ ~64   │ 9 files  │
  └───┴────────────────────────────────────────────┴───────┴──────────┘
```

### §4.6 — Cluster 5: RESEARCH (Session 5)

```
  ┌───┬────────────────────────────────────────────┬───────┬──────────┐
  │ # │ File                                       │ ~repl │ Note     │
  ├───┼────────────────────────────────────────────┼───────┼──────────┤
  │21 │ Self-Created-Threat.md                     │ ~16   │ Type C   │
  │22 │ Melody-Technology/Religion.md              │ ~13   │          │
  │23 │ Expansion-Saturation-Crisis.md             │ ~16   │          │
  │24 │ Mismatch/Collective-Schema-Pressure.md     │ ~12   │          │
  │25 │ Love-Romantic.md                           │ ~6    │ Type C   │
  │26 │ Global/AI-Self-Model.md                    │ ~11   │          │
  │27 │ Global/Social-Calibration.md               │ ~7    │          │
  │28 │ Money-Analysis.md                          │ ~4    │          │
  │29 │ Addiction-Analysis.md                      │ ~4    │          │
  │30 │ Meta-Impact/Meta-Impact.md                 │ ~2    │          │
  │31 │ Money-Education.md                         │ ~2    │          │
  ├───┼────────────────────────────────────────────┼───────┼──────────┤
  │   │ SUBTOTAL                                   │ ~93   │ 11 files │
  └───┴────────────────────────────────────────────┴───────┴──────────┘
```

### §4.7 — Cluster 6: REMAINING (Session 6)

```
  ┌───┬────────────────────────────────────────────┬───────┬──────────┐
  │ # │ File                                       │ ~repl │ Note     │
  ├───┼────────────────────────────────────────────┼───────┼──────────┤
  │32 │ Health/Neurodiversity/Autism-Observation.md │ ~3    │ Type C   │
  │33 │ Health/Neurodiversity/ADHD-Observation.md  │ ~3    │ Type C   │
  │34 │ Health/Hijack/Nicotine-Brain-Mechanism.md  │ ~2    │ Type C   │
  │35 │ Global/Birth-Rate/03_China_Analysis.md     │ ~2    │ Type C   │
  │36 │ Global/Birth-Rate/00_Overview.md           │ ~3    │ Type C   │
  │37 │ Public-Plan/plan-public.md                 │ ~5    │ Type C   │
  │38 │ Public-Plan/summary-paper-outline.md       │ ~1    │          │
  │39 │ Core-Deep-Dive/01-File-Index.md            │ ~3    │          │
  │40 │ Research/01-File-Index.md                  │ ~5    │          │
  │41 │ Child-Chunk-Dev/ (3-4 files, 1 each)       │ ~4    │ Type C   │
  │42 │ Blackbox-Map.md                            │ ~1    │ Type C   │
  ├───┼────────────────────────────────────────────┼───────┼──────────┤
  │   │ SUBTOTAL                                   │ ~32   │ ~12 files│
  └───┴────────────────────────────────────────────┴───────┴──────────┘
```

### §4.8 — Files KHÔNG SỬA

```
  ⭐ SKIP HOÀN TOÀN:

  ① Mọi file trong backup/ và _backup/ (~30+ files)
  ② Drill files (historical record)
  ③ plan-reward-type-rename.md (meta — references old names for documentation)
  ④ plan-compile-type-rename.md (file này — self-reference)
```

---

## §5 — SESSION PLAN

```
  ┌─────────┬────────────────────────────────┬───────┬────────┬──────────┐
  │ Session │ Cluster                        │ Files │ ~Repl  │ Priority │
  ├─────────┼────────────────────────────────┼───────┼────────┼──────────┤
  │ S1      │ Core Definition                │ 4     │ ~96    │ ⭐⭐⭐     │
  │ S2      │ Compile-Type-Learning          │ 1     │ ~167   │ ⭐⭐⭐     │
  │ S3      │ Collective + Observation       │ 6     │ ~95    │ ⭐⭐       │
  │ S4      │ Body-Base + Agent-Mechanism    │ 9     │ ~64    │ ⭐⭐       │
  │ S5      │ Research                       │ 11    │ ~93    │ ⭐        │
  │ S6      │ Remaining + FINAL VERIFY       │ ~12   │ ~32    │ ⭐        │
  ├─────────┼────────────────────────────────┼───────┼────────┼──────────┤
  │ TOTAL   │                                │ ~43   │ ~547   │          │
  └─────────┴────────────────────────────────┴───────┴────────┴──────────┘

  Mỗi session:
  1. Đọc file → xác nhận Loại/Type = compile context (không phải từ thông thường)
  2. Thay thế (replace_all an toàn cho "Type C" vì luôn = compile)
  3. Grep verify: 0 remaining Loại A/B/C + Type A/B/C compile refs
  4. Grep confirm: "Experience Compile" + "Expertise Compile" + "Trust Compile" tồn tại
```

---

## §6 — VERIFICATION

### §6.1 — Sau mỗi session

```
  grep "Loại A" [cluster files] — kiểm tra = 0
  grep "Loại B" [cluster files] — kiểm tra = 0
  grep "Loại C" [cluster files] — kiểm tra = 0
  grep "Type C" [cluster files] — kiểm tra = 0
  grep "Type A" [cluster files] — kiểm tra = 0 (sau Reward rename, không còn)
```

### §6.2 — FINAL VERIFY (sau session cuối)

```
  Toàn bộ framework (trừ backup/):

  ① grep "Type A" = 0
     (Reward: đã đổi → Evaluative Reward)
     (Compile: đã đổi → Experience Compile)
     → KHÔNG CÒN "Type A" NÀO trong active files

  ② grep "Type B" = 0
     (Reward: đã đổi → Direct-State Reward)
     (Compile: đã đổi → Expertise Compile)

  ③ grep "Type C" = 0
     (Compile: đã đổi → Trust Compile)

  ④ grep "Loại A" = 0 (trừ "loại" thông thường: "loại bỏ", "phân loại")
  ⑤ grep "Loại B" = 0
  ⑥ grep "Loại C" = 0

  ⑦ grep "Experience Compile" — xác nhận tồn tại
  ⑧ grep "Expertise Compile" — xác nhận tồn tại
  ⑨ grep "Trust Compile" — xác nhận tồn tại

  ⭐ KHI CẢ 9 ĐIỀU KIỆN ĐẠT → CẢ 2 PLANS ĐÃ HOÀN TẤT.
  Framework không còn BẤT KỲ generic letter label nào.
```

---

## §7 — GHI CHÚ BỔ SUNG

### §7.1 — "Type C" = an toàn nhất để replace

```
  "Type C" LUÔN = compile context (không có "Type C" trong Reward system).
  → Có thể dùng replace_all cho "Type C" → "Trust Compile"
  → Chỉ cần verify KHÔNG nằm trong backup file
  → = Nhanh nhất, ít rủi ro nhất
```

### §7.2 — "Loại" = từ thông thường tiếng Việt

```
  ⚠️ "loại" xuất hiện trong:
  → "loại bỏ" (eliminate)
  → "phân loại" (classify)
  → "loại trừ" (exclude)

  → CHỈ đổi khi "Loại A" / "Loại B" / "Loại C" = compile taxonomy label
  → Pattern: "Loại" + space + "A/B/C" = gần như chắc chắn compile taxonomy
  → Nhưng vẫn cần glance context mỗi occurrence
```

### §7.3 — Version bump policy

```
  Giống plan-reward-type-rename.md:
  → KHÔNG bump version chỉ vì rename terminology
  → Rename = maintenance, không phải content change
  → Chỉ note trong frontmatter nếu cần: "terminology: Loại A/B/C → Experience/Expertise/Trust Compile"
```

### §7.4 — Precedent + Combined scope

```
  CẢ 2 PLANS CỘNG LẠI:

  ┌─────────────────────────────────┬────────┬────────┐
  │ Plan                            │ Files  │ ~Repl  │
  ├─────────────────────────────────┼────────┼────────┤
  │ plan-reward-type-rename.md      │ ~63    │ ~811   │
  │ plan-compile-type-rename.md     │ ~43    │ ~547   │
  ├─────────────────────────────────┼────────┼────────┤
  │ TOTAL (nhưng nhiều overlap)     │ ~80    │ ~1,358 │
  └─────────────────────────────────┴────────┴────────┘

  So với precedent:
  → SPM cleanup: 2,468 repl, 105 files → 1 session
  → Abbreviation cleanup: ~2,280 repl, ~95 files → 8 sessions
  → By-Product-Gap-Resonance: ~1,200 repl, ~82 files

  → ~1,358 repl, ~80 files = TRONG TẦM → 14 sessions tổng (8+6)
  → Chậm mà chắc — từng session verify chặt.
```

---

> *Plan: Compile Type Rename — Loại A/B/C → Experience/Expertise/Trust Compile.*
> *~43 active files. ~547 replacements. 6 sessions.*
> *CHẠY SAU plan-reward-type-rename.md.*
> *Experience Compile (trải nghiệm). Expertise Compile (chuyên gia). Trust Compile (trust install).*
> *Final state: "Type A/B/C" = 0 + "Loại A/B/C" = 0 trong TOÀN BỘ active files.*
