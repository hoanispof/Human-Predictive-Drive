# Plan — Education Applications Restructure v7.8

> **Ngày tạo:** 2026-05-11
> **Mục đích:** Tái cấu trúc bộ Applications/Education/ cho v7.8 alignment
> **Bối cảnh:** Research/Education/ đã rewrite xong (Mechanism v1.0 + DKM v1.0 + Empathy v2.0).
> Applications/ vẫn reference nền tảng CŨ đã backup.
> **Nguyên tắc:** Chậm mà chắc. Từng file một. Chất lượng cao nhất.

---

## 1. TẠI SAO CẦN TÁI CẤU TRÚC

### 1.1 Nền tảng đã thay đổi

```
Applications/ được xây TRÊN:                    Status hiện tại:
─────────────────────────────                    ────────────────
Education-Principles.md (10 NL)     →  ❌ BACKUP. Absorbed → Education-Mechanism.md v1.0
Education-Bridge.md (motivation)    →  ❌ BACKUP. Absorbed → Education-Mechanism.md v1.0
Core-v7.5-Draft.md                  →  ❌ BACKUP. Replaced → Core-Software/Hardware/Interface.md
Novelty-Loop.md                     →  ❌ BACKUP. Replaced → Observation/Novelty.md v1.0
Imagine-Final.md                    →  ✅ Vẫn active (đã refine)
Chunk.md                            →  ✅ Vẫn active (v2.0+)
Cortisol-Baseline.md                →  ✅ Vẫn active (v2.0)

Research/Education/ NỀN TẢNG MỚI:
  Education-Mechanism.md v1.0 (1,279L) — HOW: learning arc design, v7.8
    = Thay thế cả Education-Principles + Education-Bridge
    = §2 Arc Design Principles, §3 Bridge+Motivation, §4 AI-Assisted Model
  Domain-Knowledge-Map.md v1.0 (846L) — WHAT: domain groups
    = §1 Foundation Domains, §2 Era-Specific, §3 Per-Hardware
  Empathy-Education.md v2.0 (1,424L) — empathy observation
  Education-Arms-Race.md (1,057L) — competition dynamics (giữ nguyên)
```

### 1.2 Scope vấn đề — Numbers

```
10 active files, 9,273 lines total

Old refs (dead file names): 264 instances
  Core-v7.5-Draft.md, Education-Principles.md, Education-Bridge.md,
  Novelty-Loop.md, Imagine-Final.md (một số OK, một số cần update)

Old terminology: 176 instances
  Schema (OK trong nhiều context), L0/L1/L2/L3 (cũ),
  open loop (cũ), Reward Dual System (cũ)

BREAKDOWN:
  Phase 1 (main files):   5,352L | 173 old refs | 113 old terms
  Phase 2 (VN files):     3,921L |  91 old refs |  63 old terms
```

---

## 2. PHÂN TÍCH TỪNG FILE

### 2.1 Education-System.md (1,566L) — KHUNG CHÍNH

```
CONTENT:
  §0 Purpose + Imagine-Final (lý tưởng hệ thống giáo dục)
  §1 Kiến trúc tổng quan (4 stages brain-based)
  §2 Stage 2: Foundation Chunking (6-12)
  §3 Stage 3: Depth + Identity (12-18)
  §4 Stage 4: Specialization + Contribution (18-25+)
  §5 Bridge strategy tổng hợp
  §6 Assessment design
  §7 Vai trò Teacher/Mentor
  §8 Vai trò Parent/Family
  §9 Integration: School + Family + Self-learning + AI
  §10 Constraints + Reality
  §11 Honest Assessment
  §12 Kết nối

OLD REFS: 69 instances
  → "10 NL" referenced xuyên suốt (NL1-NL10)
  → "Education-Principles.md" × ~20+
  → "Education-Bridge.md" × ~10+
  → "Core-v7.5-Draft.md" × ~15+

OVERLAP VỚI RESEARCH/:
  §5 Bridge strategy ↔ Education-Mechanism §3 (Bridge+Motivation) → OVERLAP mechanism
  §9 AI Integration ↔ Education-Mechanism §4 (AI-Assisted) → OVERLAP AI model
  NHƯNG: Mechanism = brain-level PRINCIPLE, System = system-level DESIGN
  → KHÁC scope: Mechanism nói "tại sao bridge works", System nói "system implement bridge thế nào"

UNIQUE VALUE (không có ở Research/):
  ✅ System-level view: stages × roles × assessment × integration
  ✅ §6 Assessment design — cách đánh giá depth
  ✅ §7 Teacher role — practical guidance
  ✅ §8 Parent role — practical guidance
  ✅ §10 Constraints + Reality — honest limitations

VERDICT: GIỮ + REWRITE
  → Re-base "10 NL" → Education-Mechanism v1.0 concepts
  → Update "Core-v7.5" → Core-Software/Hardware v1.0
  → §5 Bridge: reference Mechanism §3 cho principle, keep system-level implementation
  → §9 AI: reference Mechanism §4 cho model, keep system-level integration
  → EFFORT: LỚN (69 old refs, re-base toàn bộ conceptual foundation)
```

### 2.2 Hardware-Calibration.md (1,456L) — DURABLE

```
CONTENT:
  §0 Tại sao cần per-individual
  §1 "Hardware" là gì trong education context
  §2 Observable indicators — đo qua hành vi
  §3 Calibration per major dimensions (6 dimensions)
  §4 Neurodiversity — variation, not disorder
  §5 Common miscalibrations — labels sai phổ biến
  §6 Practical calibration process
  §7 Honest Assessment + Kết nối

OLD REFS: 20 instances (ÍT NHẤT)
  → "Core-v7.5-Draft.md" × ~8
  → "Education-Principles.md NL3" × ~5
  → "Education-System.md" × ~5 (internal ref, sẽ auto-update khi System rewrites)

OVERLAP VỚI RESEARCH/:
  ↔ Domain-Knowledge-Map §3 (Per-Hardware Domains) → DKM chỉ brief, HC DEEP
  → MINIMAL overlap — HC là file UNIQUE nhất

UNIQUE VALUE:
  ✅✅ 6 hardware dimensions × observable indicators per age
  ✅✅ Calibration strategies — practical
  ✅✅ Neurodiversity reframe
  ✅✅ Miscalibration examples (labels sai phổ biến)
  → KHÔNG có file nào khác cover depth này

VERDICT: GIỮ + REFINE
  → Update refs (20 instances — manageable)
  → Update terminology nếu có old v7.5 terms
  → Keep content nguyên (brain-based → still valid)
  → Add v7.8 connections: PFC-Configuration, Sensitivity-Classification, Type A/B?
  → EFFORT: TRUNG BÌNH (content solid, chỉ update refs + add connections)
```

### 2.3 Era-Analysis-2025.md (569L)

```
CONTENT:
  §0 Purpose + Disclaimer
  §1 Tech landscape 2025
  §2 Changing skills
  §3 Stable skills (8 brain constants)
  §4 Key uncertainties (6)
  §5 Implications for education
  §6 Honest Assessment + Kết nối

OLD REFS: 14 instances
AGE: 2026-04-03 (~5 tuần)
  → AI landscape đã shift (Claude 4.x series, Opus, competition)
  → Core observations vẫn valid nhưng cần refresh

UNIQUE VALUE:
  ✅ Era context — KHÔNG có file khác cover
  ✅ Uncertainty analysis — honest, practical
  ✅ "8 brain constants" = cái KHÔNG đổi → durable component

VERDICT: GIỮ + UPDATE
  → Refresh AI landscape cho 2026
  → Update refs
  → Consider rename → Era-Analysis-2026.md? Hay giữ 2025+ (vẫn valid)?
  → EFFORT: NHỎ-TRUNG BÌNH
```

### 2.4 Curriculum-Framework.md (641L)

```
CONTENT:
  §0 Purpose + 4 nguyên tắc curriculum
  §1 Taxonomy: 3 tiers (Foundation / Era / Per-Hardware)
  §2 Foundation Curriculum (Foundation Matrix)
  §3 Era-Specific Curriculum (2025+)
  §4 Sequencing by Stage
  §5 "Cái cần GIẢM/BỎ" từ curricula hiện tại
  §6 Honest Assessment + Kết nối

OLD REFS: 8 instances
OLD TERMS: 38 instances (NHIỀU — "mirror neurons", NL refs, Schema)

OVERLAP VỚI RESEARCH/:
  §1 Taxonomy 3-tier ≈ Domain-Knowledge-Map structure → OVERLAP CẤU TRÚC
  §1 "6 Foundation Domains" ≈ DKM §1 Foundation Domains → OVERLAP NỘI DUNG
  NHƯNG:
    §2-3 HOW to deliver each domain = UNIQUE
    §4 Sequencing per stage = UNIQUE
    §5 "Cái cần bỏ" = UNIQUE + practical

VERDICT: GIỮ + REFINE (slim down overlap)
  → §1 Taxonomy: SLIM DOWN, reference DKM v1.0 thay vì repeat 6+4 domains
  → §2-3: Keep HOW to deliver (unique)
  → §4: Keep sequencing (unique)
  → §5: Keep "cái cần bỏ" (unique + practical)
  → Update "mirror neurons" → SPM
  → Update terminology
  → EFFORT: TRUNG BÌNH (38 old terms cần update)
```

### 2.5 Country/VN/ (4 files, 3,921L)

```
FILES:
  VN-Education-Status.md  (1,316L) — tình trạng hiện tại
  VN-Cultural-Factors.md  (1,169L) — đặc tính văn hóa
  VN-Recommendations.md   (1,144L) — hướng đi
  PLAN.md                 (292L)   — plan triển khai

OLD REFS: 91 instances
OLD TERMS: 63 instances

CONTENT ASSESSMENT:
  Status: chủ yếu FACTS → vẫn valid
  Cultural: chủ yếu OBSERVATION → vẫn valid
  Recommendations: DERIVED từ old "10 NL" → cần re-evaluate
  → Nhiều content contextual (VN-specific) → less affected by v7.8 reframe

VERDICT: ĐỂ PHASE SAU
  → Phase 1 xong trước (main 4 files)
  → VN files phụ thuộc Education-System → System rewrite xong mới update VN
  → Separate session(s)
  → EFFORT: LỚN (3,921L, 91+63 old refs/terms)
```

### 2.6 Support files

```
00_Overview.md (286L):
  → REWRITE SAU CÙNG — follows new folder structure
  → Write AFTER all main files done
  → EFFORT: NHỎ

PLAN.md (834L):
  → KEEP as historical record
  → ADD tracking section cho restructure progress
  → EFFORT: MINIMAL
```

---

## 3. QUYẾT ĐỊNH CẤU TRÚC

### 3.1 Files GIỮ

```
✅ Education-System.md         → REWRITE (re-base lên Mechanism v1.0)
✅ Hardware-Calibration.md     → REFINE (update refs + terminology + v7.8 notes)
✅ Era-Analysis-2025.md        → UPDATE (refresh landscape + refs)
✅ Curriculum-Framework.md     → REFINE (slim overlap + update terms)
✅ 00_Overview.md              → REWRITE (follows new structure)
✅ Country/VN/ (4 files)       → PHASE SAU (separate sessions)
```

### 3.2 Files BỎ

```
Không bỏ file nào — tất cả có unique value.
NHƯNG: backup/v1.0/ đã có → current files AN TOÀN để rewrite.
```

### 3.3 "10 NL" → Mechanism v1.0 Mapping

```
Đây là mapping QUAN TRỌNG NHẤT — mọi file đều reference "10 NL":

OLD (Education-Principles.md):            NEW (Education-Mechanism.md v1.0):
──────────────────────────────            ─────────────────────────────────
NL1: Mechanism-based delivery    →  §2 Arc Design Principles
NL2: Foundation-first            →  §2 + §1 (context shift 0-6 → 6+)
NL3: Per-hardware calibration    →  §2.x (per-individual arc)
NL4: Purpose-driven (Imagine-Final) → §3 Bridge + Motivation
NL5: Bridge strategy             →  §3 Bridge + Motivation
NL6: Cortisol inverted-U         →  §2 (approach/avoidance from Child-Dev-Mech)
NL7: Adaptability > specific     →  §4 AI-Assisted Model + DKM §2
NL8: Depth assessment            →  §2 (compile depth signals)
NL9: Individual-society balance  →  DKM §3 (per-hardware emerge)
NL10: Education as ecosystem     →  §4 AI-Assisted (distributed learning)
"8 brain constants"              →  Child-Development-Mechanism.md §1-§3
"Education-Bridge.md"            →  Education-Mechanism.md §3

⚠️ "10 NL" KHÔNG 1:1 map — Mechanism v1.0 tổ chức KHÁC:
  → Mechanism = organized by MECHANISM (arc design, bridge, AI)
  → Principles = organized by PRINCIPLE NUMBER (NL1-NL10)
  → Rewrite cần RE-ORGANIZE, không chỉ find-and-replace
```

### 3.4 Core refs mapping

```
OLD                              →  NEW
────                                ────
Core-v7.5-Draft.md               →  Core-Software.md v1.0 (cycle)
                                    Core-Hardware.md v1.0 (zones)
                                    Core-Interface.md (observer)
Core-v7.5-Draft.md §1.5 (DRD4)  →  PFC-Hardware.md (PFC/)
"Body Baseline"                  →  Body-Base.md v2.0 (Body-Base/)
"Reward Dual System"             →  Reward-Signal-Architecture.md v1.0 (Type A/B)
"Schema drive"                   →  observation parameter (Core-Software §8)
"open loop"                      →  chunk dynamics (Body-Feedback-Mechanism v1.2)
"L0/L1/L2/L3"                   →  cycle-based: Domain→Body-Input→Unconscious→Feeling→PFC
Novelty-Loop.md                  →  Observation/Novelty.md v1.0
"Satisfaction Signal"            →  Reward-Signal-Architecture.md (Type A/B)
"mirror neurons"                 →  SPM F1 (Agent-Mechanism.md v1.0)
Modality-Analysis.md             →  Modality.md (Core-Deep-Dive/)
Connection.md §4                 →  Connection.md v3.1 (Observation/)
Boredom-Analysis.md              →  Observation/Boredom.md v1.0
```

---

## 4. PLAN TRIỂN KHAI

### Phase A: Education-System.md REWRITE

```
ƯU TIÊN: CAO — ANCHOR file, mọi file khác phụ thuộc
EFFORT: LỚN (~1,566L, 69 old refs, re-base toàn bộ)
ƯỚC TÍNH: 1-2 sessions

CẦN LÀM:
  1. Đọc kỹ Education-Mechanism.md v1.0 TOÀN BỘ
  2. Map "10 NL" → Mechanism concepts (§3.3 mapping)
  3. Rewrite frontmatter + dependencies
  4. §0 Purpose: re-base lên Mechanism v1.0 thay vì "10 NL"
  5. §1 Architecture: update refs, giữ 4-stage structure (brain-based → valid)
  6. §2-§4 Stages: update terminology, keep stage-level design
  7. §5 Bridge: reference Mechanism §3, keep system-level implementation
  8. §6 Assessment: update, keep (unique)
  9. §7-§8 Teacher/Parent: update refs, keep (unique + practical)
  10. §9 Integration: reference Mechanism §4, update AI landscape
  11. §10 Constraints: keep (standalone)
  12. §11-§12: update Honest Assessment + all cross-refs

TIỀN ĐỀ ĐỌC:
  → Education-Mechanism.md v1.0 (TOÀN BỘ — 1,279L)
  → Domain-Knowledge-Map.md v1.0 (headers + §0)
  → Core-Software.md v1.0 (headers + §0-§1)
  → Child-Development-Mechanism.md (headers)
```

### Phase B: Hardware-Calibration.md REFINE

```
ƯU TIÊN: CAO — UNIQUE nhất, ít effort nhất relative to value
EFFORT: TRUNG BÌNH (~1,456L, 20 old refs, content solid)
ƯỚC TÍNH: 1 session (có thể gộp với Phase C)

CẦN LÀM:
  1. Update frontmatter + dependencies
  2. Fix 20 old refs (Core-v7.5 → Core maps, NL3 → Mechanism concepts)
  3. Update terminology nếu có v7.5 terms
  4. §1 "Hardware": add connection to Core-Hardware.md zones
  5. §3 Calibration: add notes cho PFC-Configuration, Type A/B nếu relevant
  6. §4 Neurodiversity: check alignment với Sensitivity-Classification v1.0
  7. §7 Cross-refs: complete rewrite với current paths
  8. Bump → v1.0

TIỀN ĐỀ ĐỌC:
  → Core-Hardware.md v1.0 (zones)
  → PFC-Hardware.md (DRD4, COMT)
  → Sensitivity-Classification.md v1.0 (vừa refine)
```

### Phase C: Curriculum-Framework.md REFINE

```
ƯU TIÊN: TRUNG BÌNH
EFFORT: TRUNG BÌNH (~641L, 38 old terms, overlap cần slim)
ƯỚC TÍNH: 1 session (có thể gộp với Phase B)

CẦN LÀM:
  1. Update frontmatter + dependencies
  2. §1 Taxonomy: SLIM DOWN — reference Domain-Knowledge-Map v1.0 thay vì repeat
     → Giữ 3-tier structure diagram
     → 6 Foundation Domains → brief list + "chi tiết xem DKM §1"
     → Era-Specific → brief + "chi tiết xem DKM §2"
  3. §2-§3 HOW to deliver: keep (unique), update terms
  4. §4 Sequencing: keep (unique), align with Education-System stages
  5. §5 "Cái cần bỏ": keep (unique + practical)
  6. "mirror neurons" → SPM F1
  7. §6 Cross-refs: complete rewrite
  8. Bump → v1.0

TIỀN ĐỀ ĐỌC:
  → Domain-Knowledge-Map.md v1.0 (hiểu overlap chính xác)
```

### Phase D: Era-Analysis UPDATE

```
ƯU TIÊN: THẤP-TRUNG BÌNH (time-bound file, ít urgent)
EFFORT: NHỎ-TRUNG BÌNH (~569L, 14 old refs, refresh landscape)
ƯỚC TÍNH: 1 session ngắn

CẦN LÀM:
  1. Update frontmatter + date
  2. §1 Tech landscape: refresh cho mid-2026 (Claude 4.x, competition, regulation)
  3. §2 Changing skills: review, likely still valid
  4. §3 Stable skills: update "8 brain constants" refs
  5. §4 Uncertainties: review, update if resolved/new ones
  6. §5 Implications: update per §1-§4 changes
  7. §6 Cross-refs: complete rewrite
  8. Bump → v1.0 hoặc rename → Era-Analysis-2026.md

CÂN NHẮC: có cần rename? "2025" → "2026"?
  → Nếu content thay đổi đáng kể → rename
  → Nếu chỉ refresh → giữ "2025+" (vì predictions vẫn cho 2025+ era)
```

### Phase E: 00_Overview.md REWRITE

```
ƯU TIÊN: THẤP — viết SAU CÙNG
EFFORT: NHỎ (~286L, follows structure)
ƯỚC TÍNH: 30 phút

CẦN LÀM:
  1. Update BẢN ĐỒ FILES để reflect new foundation
  2. Update FLOW giữa files
  3. Update Tầng 3 refs: Education-Principles → Education-Mechanism
  4. Update Tầng 1 refs: Core-v7.5 → 3 Core Maps
  5. Update durability guide
  6. Update reading order
```

### Phase F: Country/VN/ (SEPARATE — sessions riêng)

```
ƯU TIÊN: SAU Phase A-E
EFFORT: LỚN (3,921L, 91+63 old refs/terms)
ƯỚC TÍNH: 2-3 sessions

CẦN LÀM:
  1. Re-read after Education-System rewrite → check recommendations validity
  2. VN-Education-Status: mostly facts → REFINE (update refs)
  3. VN-Cultural-Factors: mostly observation → REFINE (update refs + terms)
  4. VN-Recommendations: DERIVED from old NL → RE-EVALUATE qua Mechanism v1.0
  5. VN/PLAN.md: update tracking

⚠️ ĐỂ SAU Phase A-E vì:
  → VN files DEPEND ON Education-System (anchor)
  → System rewrite → VN recommendations cần re-check
  → Separate scope → separate sessions
```

---

## 5. THỨ TỰ ĐỀ XUẤT

```
SESSION 1 (cold start — đọc kỹ + bắt đầu):
  → Đọc Education-Mechanism.md v1.0 TOÀN BỘ (1,279L)
  → Đọc Education-System.md TOÀN BỘ (1,566L)
  → Bắt đầu Phase A: Education-System.md rewrite (phần 1)

SESSION 2:
  → Hoàn thành Phase A: Education-System.md rewrite
  → Bắt đầu Phase B: Hardware-Calibration.md refine

SESSION 3:
  → Hoàn thành Phase B
  → Phase C: Curriculum-Framework.md refine
  → Phase D: Era-Analysis update (nếu kịp)

SESSION 4:
  → Phase D hoàn thành (nếu chưa)
  → Phase E: 00_Overview.md rewrite
  → Review toàn bộ Phase 1

SESSION 5+ (nếu cần):
  → Phase F: Country/VN/ files
```

---

## 6. TRACKING

| Phase | File | Action | Status | Session | Notes |
|---|---|---|---|---|---|
| A | Education-System.md | REWRITE | ✅ | 2026-05-11 | v2.0 (1,554L). Re-based: "10 NL"→Mechanism 8 nguyên lý, Bridge→§3, Core-v7.5→3 Maps. +Type A/B, +3 ORIGIN, +4 nguồn fill |
| B | Hardware-Calibration.md | REWRITE | ✅ | 2026-05-11 | v1.0 (1,538L). Re-based: Core-v7.5→Core-Hardware+PFC-Hardware+Modality+Body-Base. NL→Mechanism. +SPM F1, +Sensitivity groups, +Type A/B, +PFC-Configuration |
| C | Curriculum-Framework.md | REWRITE | ✅ | 2026-05-11 | v2.0 (754L). Re-based: NL→Mechanism §2.x. §1 SLIM (→ref DKM). Depth=chunk levels. +Basic Science (DKM §2.4). +SPM F1, +Type A/B, +approach/avoidance. §6 complete rewrite |
| D | Era-Analysis-2025.md | REWRITE | ✅ | 2026-05-11 | v2.0 (724L). NL1-NL10→6 era themes. §1 refreshed mid-2026. §5 re-organized. DKM §2 aligned (6 domains). +approach/avoidance, +cortisol v2.0, +SPM F1. All refs updated |
| E | 00_Overview.md | REWRITE | ✅ | 2026-05-11 | v2.0 (363L). All refs updated: Core-v7.5→3 Maps, Principles→Mechanism+DKM, bộ 3→4. Flow redrawn. Stats updated. Reading order per audience |
| F1 | VN-Education-Status.md | REWRITE | ✅ | 2026-05-11 | v2.0 (~1,350L). §1 RE-ORGANIZED: NL1-NL10→3 nhóm (Arc Design 8 nguyên lý + Bridge+Motivation + System-Level). +3 ORIGIN threat, +4 nguồn fill, +approach/avoidance, +Type A/B, +chunk compilation levels, +Imagine-Final 4 góc. All refs updated |
| F2 | VN-Cultural-Factors.md | REWRITE | ✅ | 2026-05-11 | v2.0 (~1,200L). §0+§1: "10 NL"→Mechanism concepts. §1: "NL MAP"→"MECHANISM MAP" per factor. §2: TABLE redesigned 10 cột NL→8 cột Mechanism (Dir/Found/Indiv/ImgF/Bridg/3ORI/Depth/I×S). §3-§4: NL→Mechanism refs. +3 ORIGIN permission structure, +4 nguồn, +approach/avoidance, +anchor legacy, +Imagine-Final 4 góc |
| F3 | VN-Recommendations.md | REWRITE | ✅ | 2026-05-11 | v2.0 (~1,180L). QW-1 REFRAMED: "giảm cortisol"→"Shift Direction (Imposed→Domain)" (v7.8 deepest). All "NL targeted"→"Mechanism §x.x". §0: derive từ Ed-System v2.0. §1-§3: +3 ORIGIN actions, +4 nguồn redirect, +approach/avoidance, +Type A/B assessment, +3-layer AI, +4 góc Imagine-Final. GDPT 2018 synergy remapped. Kết nối v2.0 complete |
| F4 | VN/PLAN.md | MOVED→BACKUP | ✅ | 2026-05-11 | Moved to backup/v1.0/Country/VN/PLAN.md. Lý do: plan gốc đã hoàn thành, refs cũ (10 NL), tracking đã có ở plan-education-restructure.md. Chỉ còn giá trị historical |
