# Plan: Abbreviation Cleanup — Loại bỏ viết tắt framework

```
Status:    ✅✅ COMPLETE
Created:   2026-05-23
Updated:   2026-05-23 (ALL 8/8 sessions done, final verify passed)
Scope:     ~2,280 replacements (30 framework + Hw/PFC-Ops + ~87 casual English), ~95 files, 8 sessions
Approach:  FILE-BY-FILE (xử lý tất cả abbreviations trong mỗi file cùng lúc)
Verify:    grep=0 cho TỪNG abbreviation sau khi hoàn thành
```

---

## 1. LÝ DO QUYẾT ĐỊNH

### Vấn đề hiện tại

Framework hiện đang dùng **30 viết tắt tự tạo** với tổng **~2,100+ occurrences** trải khắp ~80 production files.

### 5 lý do loại bỏ

**① Scope cực rộng → collision risk cao**

Framework cover neuroscience, psychology, education, social dynamics, AI, philosophy. Mỗi ngành có viết tắt riêng:
- "EA" = Entity-Access (framework) vs Electronic Arts vs Evolutionary Algorithm vs Expected Accuracy
- "BA" = Bond-Architecture (framework) vs Bachelor of Arts vs Brønsted Acid vs Business Analysis
- "BS" = By-Product-Scale (framework) vs ... (rõ ràng vấn đề)
- "GDP" = Gap-Distribution-Profile (framework) vs Gross Domestic Product (kinh tế)
- "IBM" = Inter-Body-Mechanism (framework) vs International Business Machines
- "RSA" = Reward-Signal-Architecture (framework) vs Rivest–Shamir–Adleman (mật mã)

Khi framework mở rộng thêm domain, collision tăng exponentially.

**② Readability cho người mới**

- "Entity-Access gradient replaces Entity-Owned binary" → đọc hiểu ngay
- "EA gradient replaces EO binary" → phải tra bảng viết tắt, flow đọc bị gián đoạn

Framework hướng đến clarity. Viết tắt phá vỡ mục tiêu.

**③ Search/grep reliability**

- Tìm "Entity-Access" → chính xác 100%
- Tìm "EA" → trùng hundreds từ khác (each, early, idea, area, tea, sea, year, ...)

Đặc biệt quan trọng cho AI-assisted reading — AI cần tìm chính xác khi cross-reference.

**④ Contextual shortening tự nhiên hơn**

Thay viết tắt cứng, dùng short form theo context:
- "By-Product-Gap-Resonance" → "By-Product" hoặc "Resonance" khi context rõ
- "Background-Pattern" → "Background" khi đang nói cluster
- "Resonance-Sustainability" → "Sustainability" khi đang thảo luận Resonance

Cách này vừa ngắn gọn vừa giữ nghĩa, không tạo ký hiệu mới.

**⑤ Future-proof**

Mỗi viết tắt mới = 1 "tên" cần nhớ. Với 30 viết tắt hiện tại, người đọc cần memorize 30 mappings. Nếu framework thêm 20 concept nữa → 50 viết tắt → không scalable.

### Quyết định

**KHÔNG viết tắt bất kỳ concept nào của framework. Hạn chế tối đa cả viết tắt tiếng Anh thông thường.**

**Lý do gốc:** Framework đã tạo rất nhiều tham số/concept mới (Entity-Access, Simulation Engine, Bond-Architecture, Hardware Subsidy, Satiation types, Resonance-Sustainability...). Người đọc từ nhiều domain khác nhau (neuroscience, psychology, education, philosophy, AI) đã phải học hàng chục concept mới. Nếu còn thêm viết tắt = **nhân đôi gánh nặng**: vừa phải hiểu concept, vừa phải tra cứu/đoán ký hiệu.

**Nguyên tắc ưu tiên:**
- Chất lượng nội dung > tiết kiệm ký tự
- Dễ nhận diện ngay > ngắn gọn
- Chấp nhận mở rộng bảng/text (tốn công hơn khi viết) để giảm gánh nặng cho người đọc
- Giảm thiểu tối đa "tra cứu hoặc đoán từ" — mỗi từ viết tắt là 1 lần người đọc phải dừng lại

### Ngoại lệ (giữ nguyên)

| Loại | Ví dụ | Lý do giữ |
|------|-------|-----------|
| Thuật ngữ học thuật mainstream | PFC, VTA, vmPFC, DRN, fMRI, EEG, HRV, COMT, NAcc, mOFC, CT afferents | Đã established trong ngành, ai cũng biết |
| SPM (Self-Pattern-Modeling) | SPM | Abbreviation DUY NHẤT framework tạo ra, đã quá established, dùng rộng rãi |
| Label/numbering systems | M1-M4, H1-H12, §1-§7, Mức 0-5 | Đây là nhãn đánh số, không phải viết tắt concept |
| Version notation | v1.0, v2.0, v3.1 | Notation chuẩn |
| File version references | "Entity-Access v1.2 §6" | Đầy đủ tên file + version — đây là format ĐÚNG |

---

## 2. INVENTORY: 30 VIẾT TẮT — VERIFIED PRODUCTION COUNTS (2026-05-23)

⚠️ Scan trước (plan gốc) ước ~800. Scan verified bằng grep cho ~2,100+. Sai lệch do:
- Plan gốc count trên sample nhỏ, verified scan toàn bộ production files
- Nhiều abbreviation phổ biến hơn dự kiến (BP ×8.7, VP ×7.9, RSA ×4.7)
- Scope: CHỈ production files (không backup, drill, plan, outline)

### Tần suất VERIFIED (sorted descending)

| # | Viết tắt | Thay bằng | Production | Plan gốc | ×Lệch | Ghi chú |
|---|----------|-----------|-----------|----------|--------|---------|
| 1 | **BP** | Background-Pattern | **~564** | ~65 | ×8.7 | 390 trong Background-Pattern.md! |
| 2 | **VP** | Valence-Propagation | **~220** | ~28 | ×7.9 | ⚠️ DUAL: Ventral Pallidum (GIỮ) vs framework (THAY) |
| 3 | **RSA** | Reward-Signal-Architecture | **~135** | ~29 | ×4.7 | |
| 4 | **BFM** | Body-Feedback-Mechanism | **~131** | ~30 | ×4.4 | |
| 5 | **EC** | Entity-Compiled | **~108** | ~128 | ×0.8 | Khá chính xác |
| 6 | **BPGR** | By-Product-Gap-Resonance | **~92** | ~71 | ×1.3 | Short form tùy context |
| 7 | **BA** | Bond-Architecture | **~72** | ~28 | ×2.6 | |
| 8 | **EA** | Entity-Access | **~66** | ~35 | ×1.9 | |
| 9 | **SAL** | Somatic-Articulation-Loop | **~51** | ~6 | ×8.5 | Plan gốc bỏ sót! |
| 10 | **RPE** | Resonance-Per-Entity | **~51** | ~9 | ×5.7 | |
| 11 | **Hw** | Hardware | **~48** | ~98 | ×0.5 | Nhiều đã nằm trong backup |
| 12 | **CAD** | Collective-Arc-Dynamics | **~48** | ~5 | ×9.6 | |
| 13 | **GDP** | Gap-Distribution-Profile | **~46** | ~3 | ×15 | ⚠️ Collision GDP kinh tế |
| 14 | **IBM** | Inter-Body-Mechanism | **~45** | ~16 | ×2.8 | ⚠️ Collision IBM corp |
| 15 | **SE** | Simulation-Engine | **~43** | ~8 | ×5.4 | |
| 16 | **BS** | By-Product-Scale | **~41** | ~6 | ×6.8 | ⚠️ Collision rõ ràng |
| 17 | **RS** | Resonance-Sustainability | **~38** | ~21 | ×1.8 | |
| 18 | **GBN** | Gap-Body-Need | **~37** | ~21 | ×1.8 | |
| 19 | **PFC-Ops** | PFC-Operations | **~31** | ~60 | ×0.5 | |
| 20 | **EAC** | Entity-Access-Calibration | **~30** | ~20 | ×1.5 | |
| 21 | **EAE** | Entity-Access-Excess | **~20** | ~11 | ×1.8 | |
| 22 | **CN** | Coordination-Node | **~20** | ~7 | ×2.9 | |
| 23 | **BFL** | Body-Feedback-Label | **~19** | ~5 | ×3.8 | |
| 24 | **CB** | Collective-Body | **~11** | ~5 | ×2.2 | |
| 25 | **AM** | Agent-Mechanism | **~10** | ~3 | ×3.3 | |
| 26 | **BC** | Body-Coupling | **~7** | ~3 | ×2.3 | |
| 27 | **CF** | Compliance-Floor | **~6** | labels | — | CF-1~6 labels |
| 28 | **DMD** | Domain-Mapping-Drive | **~4** | ~4 | ×1.0 | |
| 29 | **Sat.** | Satiation | **~2** | ~2 | — | Table headers |
| 30 | **LR** | Love-Romantic | **~1** | ~1 | — | |
| 31 | **LU** | Love-Unified | **~1** | ~1 | — | |
| | Casual Eng | (xem Nhóm G) | **~58** | ~58 | — | |
| | **TỔNG** | | **~2,107** | ~800 | **×2.6** | |

### VP: TRƯỜNG HỢP ĐẶC BIỆT

"VP" xuất hiện với 2 nghĩa:
1. **Ventral Pallidum** (vùng não) — thuật ngữ học thuật mainstream → **GIỮ**
2. **Valence-Propagation** (framework concept) → **THAY** bằng "Valence-Propagation"

Khi thay, cần đọc context từng dòng để phân biệt. Files nặng nhất: Body-Coupling.md (54), Collective-Body.md (22), Background-Pattern.md (19), Empathy.md (16).

### BPGR: SHORT FORM TÙY CONTEXT

- "By-Product" (nói về mechanism)
- "Resonance" (nói về output)
- "Gap-Resonance" (nói về gap matching process)
- Full name khi lần đầu trong section hoặc context chưa rõ

### Nhóm G: VIẾT TẮT TIẾNG ANH THÔNG THƯỜNG

| Viết tắt | Thay bằng | ~Số lần | Files chính |
|----------|-----------|---------|-------------|
| dom. / domin. | dominant / dominance | ~4 | Empathy.md, Entity-Access.md, Resonance-Per-Entity.md |
| pred. | prediction | ~5 | Threat.md, Autonomy-Hardware.md, Body-Feedback-Mechanism.md |
| req. | required / requirement | ~15 | 09-Event-Chunks-Inference-Matrix.md |
| Phase-dep. | Phase-dependent | ~1 | Empathy.md |
| dep. | dependent | ~2 | Gap-Body-Need.md |
| freq | frequency | ~1 | Inter-Body-Mechanism.md |
| obs. | observation | ~3 | Self-Pattern-Modeling.md |
| prev. | preview | ~1 | Autonomy-Hardware.md |
| Conf | Confidence | ~12 | 09-Event-Chunks-Inference-Matrix.md |
| mech. | mechanism | ~12 | 09-Event-Chunks-Inference-Matrix.md |
| chr | chronic | ~1 | PFC-Configuration.md |
| Gap dom. | Gap domain | ~1 | Entity-Access.md |

---

## 3. EXECUTION PLAN: FILE-BY-FILE

### Phương pháp

**Thay vì chia theo abbreviation → chia theo FILE.** Mỗi file chỉ đọc 1 lần, sửa TẤT CẢ abbreviations cùng lúc.

Ưu điểm:
- Hiểu context đầy đủ → không sót, không nhầm
- Consistency trong file (không có tình trạng "Entity-Compiled" dòng 50 nhưng "EC" dòng 200)
- Hiệu quả hơn (đọc 1 lần vs đọc lại nhiều lần cho mỗi abbreviation)

Verify cuối: grep=0 cho TỪNG abbreviation → bắt bất kỳ sót nào.

### Per-file density map (sorted descending, production only)

```
528  Background-Pattern.md              ← Session 1 (dedicated)
194  Body-Coupling.md                   ← Session 2
126  Resonance-Per-Entity.md            ← Session 3
123  Agent-Mechanism.md                 ← Session 3
 75  Gap-Distribution-Profile.md        ← Session 5
 68  Entity-Access.md                   ← Session 4
 64  Empathy.md                         ← Session 6
 55  01-File-Index.md                   ← Session 7
 51  Valence-Propagation.md             ← Session 2
 46  Collective-Body.md                 ← Session 7
 45  Hidden-Quality-Perception.md       ← Session 5
 43  Protect.md                         ← Session 6
 43  Gap-Body-Need.md                   ← Session 5
 41  Gap-Direction.md                   ← Session 5
 38  Connection.md                      ← Session 6
 38  Coordination-Node.md               ← Session 7
 38  Bond-Architecture.md               ← Session 4
 36  Entity-Access-Excess.md            ← Session 4
 33  Reward-Calibration.md              ← Session 5
 32  Self-Pattern-Modeling.md           ← Session 4
 26  Feeling-Literacy-Training.md       ← Session 7
 26  By-Product-Gap-Resonance.md        ← Session 4
 25  Resonance-Sustainability.md        ← Session 4
 24  Body-Feedback.md                   ← Session 5
 22  AI-Schema-Detection.md             ← Session 6
 20  By-Product-Scale.md                ← Session 4
 18  Compile-Taxonomy.md                ← Session 7
 17  PFC-Operations.md                  ← Session 7
 17  Boredom.md                         ← Session 6
 16  Status.md                          ← Session 6
 14  Entity-Compiled.md                 ← Session 4
 13  Chunk.md                           ← Session 7
 12  PFC-Label.md                       ← Session 7
 11  Meaning.md                         ← Session 6
 11  Feeling.md                         ← Session 7
 11  Entity-Access-Calibration.md       ← Session 4
 10  Imagine-Final.md                   ← Session 7
  9  Reward-Signal-Architecture.md      ← Session 5
  9  Body-Base.md                       ← Session 2
  8  Gratitude.md                       ← Session 6
  8  Autonomy-Hardware.md               ← Session 6
  7  Logic-Feeling.md                   ← Session 7
  7  Obligation.md                      ← Session 6
  7  Compliance-Floor.md                ← Session 7
  7  Body-Feedback-Label.md             ← Session 5
  6  Threat.md                          ← Session 6
  5  Domain-Mapping-Drive.md            ← Session 7
  5  Collective-Arc-Dynamics.md         ← Session 7
  5  Feeling-Mechanism-Deep.md          ← Session 7
  5  02-Cross-Network-Transfer.md       ← Session 7
4-1  ~35 files nhỏ (1-4 each)           ← Session 7/8
~58  Casual English abbreviations       ← Session 8
```

### 8 Sessions

```
Session 1: Background-Pattern.md                          [~528 repl, 1 file]
    File nặng nhất. BP=390 + VP=19 + EC=17 + Hw=27 + PFC-Ops=10 + 
    EA=5 + BA=7 + BP-related refs
    ⚠️ VP: phân biệt Ventral Pallidum vs Valence-Propagation
    ⚠️ BP tự-refer 390 lần — bulk nhưng context rõ (luôn = Background-Pattern)

Session 2: Body-Base/ root files                          [~254 repl, 3-5 files]
    Body-Coupling.md (194) — second heaviest
    Valence-Propagation.md (51)
    Body-Base.md (9) + Why-Body-Knows.md + Inter-Body-Mechanism.md + Cortisol-Baseline.md
    ⚠️ Body-Coupling: VP=54 — dual meaning review nặng nhất

Session 3: Agent-Mechanism/ Part 1 — 2 heavy files        [~249 repl, 2 files]
    Agent-Mechanism.md (123) — foundational system
    Resonance-Per-Entity.md (126) — core mechanism

Session 4: Agent-Mechanism/ Part 2 — remaining 9 files     [~270 repl, 9 files]
    Entity-Access.md (68) + Bond-Architecture.md (38) +
    Entity-Access-Excess.md (36) + Self-Pattern-Modeling.md (32) +
    By-Product-Gap-Resonance.md (26) + Resonance-Sustainability.md (25) +
    By-Product-Scale.md (20) + Entity-Compiled.md (14) +
    Entity-Access-Calibration.md (11)

Session 5: Body-Feedback/ ALL files                        [~283 repl, ~14 files]
    Gap-Distribution-Profile.md (75) + Hidden-Quality-Perception.md (45) +
    Gap-Body-Need.md (43) + Gap-Direction.md (41) + Reward-Calibration.md (33) +
    Body-Feedback.md (24) + Reward-Signal-Architecture.md (9) +
    Body-Feedback-Label.md (7) + Body-Feedback-Mechanism.md (?) +
    01-Foundation.md (2) + 02-Dissonance.md (1) + 03-Reward.md (2) +
    04-Integration.md (1) + Action-Space.md (?)

Session 6: Observation/ ALL 16 files                       [~256 repl, 16 files]
    Empathy.md (64) + Protect.md (43) + Connection.md (38) +
    AI-Schema-Detection.md (22) + Boredom.md (17) + Status.md (16) +
    Meaning.md (11) + Gratitude.md (8) + Autonomy-Hardware.md (8) +
    Obligation.md (7) + Threat.md (6) + Drive.md (4) + Autonomy.md (4) +
    AI-Schema-Detection-update-draft.md (4) + Novelty.md (3) +
    Liking-Wanting.md (1)

Session 7: Remaining folders                               [~280 repl, ~30 files]
    Collective/ (5 files: ~96): Collective-Body (46), Coordination-Node (38),
        Compliance-Floor (7), Collective-Arc-Dynamics (5), Collective-Purpose (?)
    PFC/ (~53): PFC-Operations (17), PFC-Label (12), Imagine-Final (10),
        Logic-Feeling (7), Somatic-Articulation-Loop (2), PFC-Hardware (2),
        Simulation-Engine (2), others (1 each)
    Feeling/ (~48): Feeling-Literacy-Training (26), Feeling (11),
        Feeling-Mechanism-Deep (5), sub-files (~6)
    Chunk/ non-AM (~32): Compile-Taxonomy (18), Chunk (13), 99-Master-Synthesis (1)
    Domain/ (~8): Domain-Mapping-Drive (5), Knowledge-Flow (2), Discovery-vs-Expansion (1)
    Root (~59): 01-File-Index (55), Modality (4)
    Schema/ + Melody Lens/ + Chunk-Internal-Processing/ + Chunk-External-Development/
        + Child-Chunk-Development/ + Clarification/ (~30)

Session 8: Casual English + remaining + VERIFY ALL         [~100 + verify]
    Casual English (~58): dom., pred., req., Phase-dep., dep., freq, obs.,
        prev., Conf, mech., chr, Gap dom. — chủ yếu trong 09-Matrix + vài files
    Sat. (~2): table headers
    Remaining small files missed in Session 7

    VERIFY TOÀN BỘ:
    - Grep framework cho TỪNG abbreviation (30 framework + Hw + PFC-Ops + casual) → phải = 0
    - Spot-check 5-10 files xem context đúng
    - Check VP chỉ còn = Ventral Pallidum, không còn = Valence-Propagation
    - Check table formatting vẫn đọc được sau khi expand
```

---

## 4. QUY TẮC THAY THẾ

### 4.1 Format chuẩn khi cross-reference

**Trước (viết tắt):**
```
BPGR v1.4 §9
EC chunks
EA v1.2 Mức 0-5
BFM §3.3c
RSA A:B ratio
```

**Sau (đầy đủ):**
```
By-Product-Gap-Resonance v1.4 §9
Entity-Compiled chunks
Entity-Access v1.2 Mức 0-5
Body-Feedback-Mechanism §3.3c
Reward-Signal-Architecture Evaluative:Direct-State ratio
```

### 4.2 Contextual shortening (OK)

Khi context đã rõ, có thể dùng short form tự nhiên:

```
By-Product-Gap-Resonance v1.4 mô tả 5 drills...
...trong đó, By-Product match là cơ chế chính...
...Resonance sustainability phụ thuộc 4 layer...
```

"By-Product" và "Resonance" ở đây KHÔNG phải viết tắt — là cách nói tự nhiên.

### 4.3 Trong bảng/table (ngoại lệ có điều kiện)

Nếu bảng quá chật, CÓ THỂ dùng tên ngắn + legend bắt buộc:

```
| Bond-Arch | Entity-Comp | Resonance-Sust |
| (Bond-Architecture v1.0) | (Entity-Compiled v1.0) | (Resonance-Sustainability v1.0) |
```

Nhưng **KHÔNG DÙNG** dạng 2-3 chữ cái (BA, EC, RS). Dùng tên ngắn có nghĩa.

### 4.4 SPM — ngoại lệ duy nhất

SPM (Self-Pattern-Modeling) giữ nguyên vì:
- Đã quá established trong framework (hàng trăm occurrences)
- Đã qua rename chính thức (Match → Modeling)
- Là concept trung tâm, xuất hiện ở hầu hết mọi file
- Abbreviation KHÔNG trùng với mainstream nào đáng kể

---

## 5. PROGRESS TRACKING

```
✅ Session 1: Background-Pattern.md                    [~502 actual, 1 file] ← DONE 2026-05-23
✅ Session 2: Body-Base/ root files                    [~294 actual, 6 files] ← DONE 2026-05-23
✅ Session 3: Agent-Mechanism/ Part 1 (2 heavy)        [~267 actual, 2 files] ← DONE 2026-05-23
✅ Session 4: Agent-Mechanism/ Part 2 (9 remaining)    [~272 actual, 9 files] ← DONE 2026-05-23
✅ Session 5: Body-Feedback/ ALL                       [~282 actual, 10 files] ← DONE 2026-05-23
✅ Session 6: Observation/ ALL                         [~256 actual, 16 files] ← DONE 2026-05-23
✅ Session 7: Remaining folders                        [~320 actual, 36 files] ← DONE 2026-05-23
✅ Session 8: Casual English + VERIFY ALL              [~87 actual, 15 files] ← DONE 2026-05-23

TOTAL: ~2,280 replacements, ~95 files, 8 sessions
Done:  8/8 ✅✅ ALL COMPLETE

✅ Session 9: Research/ + Applications/ + top-level  [~447 actual, 27 files] ← DONE 2026-05-23
   Love-Romantic.md (164), Love-Unified.md (174+2 redundancy fix),
   25 remaining files (123 initial, 14 false positive reverts).
   FALSE POSITIVES correctly preserved:
     VP=Ventral Pallidum(2), EC=Entorhinal Cortex(1), BA=Vietnamese/Bachelor(12+),
     EA=numbered items(7), SE=Southeast Asia(1), BS=Bac si(27+), BP=blood pressure(1),
     GDP=economics(70+), CN=Vietnamese(12+), BC=historical dates(2).

GRAND TOTAL: ~4,727 replacements, ~200 files, 9 sessions (8 Core + 1 Research/Apps)
Done:  9/9 ✅✅ ALL PRODUCTION FILES COMPLETE
```

---

## 6. RELATIONSHIP VỚI CÁC PLAN KHÁC

| Plan | Quan hệ | Thứ tự |
|------|---------|--------|
| plan-concept-cascade-refine | Content additions (cross-refs) | ✅ ĐÃ XONG |
| plan-abbreviation-cleanup (NÀY) | Terminology cleanup | ② ĐANG LÀM |
| plan-education-restructure | Applications/ rewrite | ③ Độc lập |
| plan-core-3maps | Core restructure | ④ Độc lập |

---

## 7. SAU KHI HOÀN THÀNH

### Convention mới áp dụng vĩnh viễn:
1. KHÔNG tạo viết tắt mới cho bất kỳ concept nào
2. Viết đầy đủ tên concept trong mọi context
3. Contextual shortening OK (dùng 1-2 từ có nghĩa khi context rõ)
4. Trong bảng: dùng tên ngắn có nghĩa + legend, KHÔNG dùng 2-3 chữ cái
5. Ngoại lệ: thuật ngữ học thuật mainstream + labels (M1-M4, H1-H12)
   (SPM đã bị loại 2026-05-23 → viết đầy đủ Self-Pattern-Modeling)

### Files cần update convention note:
- feedback_conventions.md (memory) — strengthen existing rule
- Có thể thêm note vào CLAUDE.md hoặc CONTRIBUTING.md nếu có
