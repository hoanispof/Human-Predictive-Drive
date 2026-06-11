# Education Rewrite PLAN — Bộ 2 Core Files + Observation

> **Created:** 2026-04-21
> **Purpose:** Cold-start reference cho session triển khai bộ Education mới
> **Context:** Thay thế bộ Education cũ bằng 2 core files tinh gọn + Observation folder

---

## 1. TẠI SAO REWRITE

```
INSIGHT CỐT LÕI:

  Child-Development = HARDWARE (ổn định)
    → Framework mô tả được chi tiết, comprehensive
    → 4 files, ~8,722 lines, v7.8-aligned ✅

  Education = SOFTWARE (era-dependent)
    → Càng tạo khung prescriptive → càng TỰ GIỚI HẠN
    → Kiến thức VÔ TẬN, cách dạy VÔ TẬN
    → Không thể liệt kê hết (và không nên)

  VẤN ĐỀ BỘ CŨ:
    → 15 files, ~14,000+ lines — quá prescriptive
    → Prescribe "dạy thế nào" = sẽ outdated
    → 3+2=5 có vô vàn cách dạy, tập nhạc có vô vàn cách
    → Framework KHÔNG THỂ và KHÔNG NÊN enumerate


MÔ HÌNH MỚI — GIỐNG AI-SCHEMA-DETECTION:

  AI-Schema: schema vô tận → framework cho NGUYÊN LÝ nhận diện, không cho GPS
  Education: cách dạy vô tận → framework cho NGUYÊN LÝ build arc, không cho lesson plan

  Framework = ENGINE cho AI optimize
    → Phụ huynh/giáo viên feed: "bài này, học sinh này"
    → AI + framework principles → generate arc phù hợp
    → Teacher/parent calibrate → student feedback → adjust
    → Từ cơ bản → nâng cao MÃI MÃI (với AI support)
```

---

## 2. FOLDER STRUCTURE SAU REWRITE

```
Research/Education/
  ├── Education-Mechanism.md          ← Core 1: HOW (bất biến, brain-based)
  ├── Domain-Knowledge-Map.md         ← Core 2: WHAT (era-level, update khi era đổi)
  ├── Observation/
  │   ├── Education-Arms-Race.md      ← Quan sát vấn đề (giữ nguyên, không cần refine)
  │   └── Empathy-Education.md        ← Quan sát giải pháp (CẦN VIẾT MỚI — empathy core đã cải tiến)
  │                                      Empathy trong education → thói quen hợp tác, làm việc,
  │                                      sinh sống sau này = observation về ứng dụng rộng hơn education
  ├── backup/v1.1/                    ← Source material cho core files mới
  │   ├── Education-Principles.md     (1,838L) → absorbed vào Education-Mechanism.md
  │   └── Education-Bridge.md         (1,606L) → nguyên lý absorbed vào Mechanism §2-§3,
  │                                      prescriptive parts (per-age, per-hardware, withdrawal) BỎ
  └── PLAN.md

Applications/Education/backup/v1.0/   ← Toàn bộ Applications files
  ├── 00_Overview.md                   (286L)
  ├── Education-System.md              (1,566L)
  ├── Hardware-Calibration.md          (1,456L)
  ├── Era-Analysis-2025.md             (569L)
  ├── Curriculum-Framework.md          (641L) → domain taxonomy rút cho Domain-Knowledge-Map
  ├── PLAN.md                          (292L)
  └── Country/VN/
      ├── VN-Education-Status.md       (1,316L)
      ├── VN-Cultural-Factors.md       (1,169L)
      ├── VN-Recommendations.md        (1,144L)
      └── PLAN.md                      (292L)

ĐÃ MOVE (không backup — content valid, đúng vị trí mới):
  → Domain-Mapping-Drive.md → Core-Deep-Dive/Domain/ (mechanism, not education)
  → Education-Arms-Race.md → Research/Education/Observation/
  → Empathy-Education.md → Research/Education/Observation/
```

---

## 3. SOURCE MATERIAL MAP

```
Education-Principles.md (backup) cung cấp:
  → 9 brain constants        → Education-Mechanism.md §1
  → 10 nguyên lý bất biến   → Education-Mechanism.md §2
  → 4-tầng architecture      → Education-Mechanism.md §0

Education-Bridge.md (backup) cung cấp:
  → Bridge = scaffolding, 4 loại              → Mechanism §3
  → Curiosity KHÔNG phải bridge               → Mechanism §3
  → 3 ORIGIN threat taxonomy                  → Mechanism §3
  → Transition 4 nguồn fill                   → Mechanism §3
  → Arc design (§5.5)                         → Mechanism §2
  → Per-age/per-hardware/withdrawal/mistakes  → BỎ (prescriptive, AI handle)

Curriculum-Framework.md (backup) cung cấp:
  → 3-tier domain taxonomy     → Domain-Knowledge-Map §1-§3
  → Foundation matrix 6×4      → Domain-Knowledge-Map §4 (simplified)
  → 4 curriculum principles    → Mechanism §2 (absorbed)

Domain-Mapping-Drive.md (Core-Deep-Dive/Domain/) cung cấp:
  → WHY humans drive map domain → cross-reference, không duplicate
```

---

## 4. FILE 1: Education-Mechanism.md (BẤT BIẾN — brain-based)

```
MỤC ĐÍCH:
  HOW não build chunks từ bài học BẤT KỲ
  = Nguyên lý thiết kế learning arc — valid MỌI era
  = "100 năm trước đúng, 100 năm sau vẫn đúng"

OUTLINE DỰ KIẾN:

  §0 — VỊ TRÍ + TẠI SAO CHỈ 2 FILES
     → Child-Dev = hardware (4 files, comprehensive)
     → Education = software (2 files, principles + map)
     → Tại sao không prescribe: vô tận cách dạy, era thay đổi
     → Mô hình: Framework = engine, AI = runtime optimizer
     → Bộ 2 files diagram

  §1 — NÃO HỌC NHƯ THẾ NÀO (Brain Constants for Learning)
     → Rút gọn từ Education-Principles.md §2 (9 brain constants)
     → Chunks = đơn vị học
     → Prerequisite chains: chunk B cần chunk A trước
     → Consolidation: sleep, repetition spacing, emotional peak
     → Multi-modal: càng nhiều modality → compile càng sâu
     → Body-base: body = processing channel, không chỉ "ngồi nghe"
     → PFC development timeline: không ép chunk chưa có hardware

  §2 — ARC DESIGN PRINCIPLES (Nguyên lý thiết kế bài học)
     → Arc = 1 đơn vị học từ A→B (compile chunk mới)
     → Cost formula: cost thấp nhất cho HỌC SINH NÀY
     → Direction: novelty (hứng thú) > threat (sợ sai)
     → Prerequisite check: verify chunks nền trước
     → Arc length ↔ chunk threshold (quá dài = mất hứng)
     → Feedback loop: student response → adjust
     → "Vô vàn cách dạy 3×5" — tất cả valid NẾU follow principles

  §3 — BRIDGE + MOTIVATION (Rút gọn từ Education-Bridge.md)
     → Bridge = scaffolding tạm thời (4 loại: carrot/threat/social/identity)
     → Curiosity KHÔNG phải bridge — là target của transition
     → Transition: bridge → intrinsic (4 nguồn fill)
     → 3 loại threat origin: Domain (feature) / Peer (feature) / Imposed (tool)
     → Arc tốt = ÍT cần bridge (giảm discomfort > ép chịu đựng)

  §4 — AI-ASSISTED EDUCATION MODEL
     → 3 tầng: AI generate arc + Teacher/Parent calibrate + Student feedback
     → Flow: feed topic + student profile → AI + mechanism principles → arc options
     → AI biết THÊM gì nhờ framework: prerequisite, direction, body-base, cost...
     → Từ cơ bản → nâng cao mãi mãi: AI adjust per level
     → Giống AI-Schema: navigate tool, không phải GPS chính xác

  §5 — HONEST ASSESSMENT
     → 🟢/🟡/🔴 per concept
     → Cái framework THÊM được vs cái KHÔNG LÀM ĐƯỢC

  §6 — CROSS-REFERENCES
     → Child-Dev bộ 4 (hardware foundation)
     → Core files (Chunk, Cortisol, PFC, Body-Feedback...)
     → Domain-Mapping-Drive.md (Core-Deep-Dive/Domain/) — WHY drive
     → AI-Schema-Detection.md (cùng mô hình gateway)
     → Domain-Knowledge-Map.md (File 2 — WHAT)


KEY PRINCIPLES KHI VIẾT:
  → KHÔNG prescribe cách dạy cụ thể
  → CHỈ cung cấp NGUYÊN LÝ brain-based
  → Ví dụ minh hoạ (3×5, tập nhạc...) = illustrate principle, không phải recipe
  → Compact: target ~1,200-1,500 lines (tinh gọn, không padding)
  → v7.8 aligned: chunks compile, direction>level, approach/avoidance, 3-tier confidence


REFERENCE FILES CẦN ĐỌC KHI TRIỂN KHAI:
  → Education-Principles.md (backup) — rút 9 brain constants + 10 NL
  → Education-Bridge.md (backup) — rút bridge nguyên lý (bỏ prescriptive parts)
  → Domain-Mapping-Drive.md (Core-Deep-Dive/Domain/) — WHY drive, cross-ref
  → Child-Development-Mechanism.md — pattern: HOW file structure
  → AI-Schema-Detection.md — pattern: gateway + 3-layer model
  → Core-v7.8-Draft.md — v7.8 terminology
  → Chunk.md v2.0 — chunk mechanics
  → Cortisol-Baseline.md v2.0 — cortisol as amplifier
```

---

## 5. FILE 2: Domain-Knowledge-Map.md (ERA-DEPENDENT nhưng ở GROUP level)

```
MỤC ĐÍCH:
  WHAT nhóm kiến thức/kỹ năng cần cho thời đại hiện đại
  = Bản đồ domain — KHÔNG liệt kê hết, chỉ baseline
  = Update khi era đổi (thêm/bớt nhóm), CẤU TRÚC giữ nguyên

OUTLINE DỰ KIẾN:

  §0 — VỊ TRÍ + TẠI SAO FILE NÀY
     → Mechanism (File 1) = HOW → file này = WHAT
     → Không liệt kê hết → chỉ nhóm baseline cho era hiện đại
     → Mỗi nhóm = 1 "cây" — gốc ai cũng cần, nhánh vô tận
     → AI + File 1 + File 2 → generate arc cho BẤT KỲ level

  §1 — FOUNDATION DOMAINS (cross-era, mọi người cần)
     → Ngôn ngữ + Giao tiếp (literacy)
     → Toán + Logic (numeracy, pattern recognition)
     → Vận động + Cơ thể (somatic, coordination, health)
     → Xã hội + Cảm xúc (empathy, collaboration, regulation)
     → Sáng tạo + Biểu đạt (art, music, expression)
     → Meta-learning (learn how to learn)
     → Per domain: prerequisite chunks, timing gợi ý,
        WHY foundation (link to brain mechanism)

  §2 — ERA-SPECIFIC DOMAINS (thời đại 2025+)
     → AI Literacy (dùng, đánh giá, hiểu giới hạn)
     → Information Curation (lọc, đánh giá source, synthesize)
     → Systems Thinking (complexity, feedback loops)
     → Khoa học cơ bản (biology, chemistry, physics — mức literacy)
     → Cross-cultural awareness
     → Digital wellbeing
     → ⚠️ ERA-BOUND: update khi era đổi

  §3 — PER-HARDWARE DOMAINS (emerge per individual)
     → KHÔNG prescribe → observe + support
     → Specialization emerge từ hardware tendencies
     → AI detect patterns → suggest domains phù hợp
     → "Cây" mỗi domain: gốc → thân → nhánh → lá (vô tận)

  §4 — TIMING + PREREQUISITE MAP
     → Nhóm nào cần từ sớm (foundation chunks)
     → Nhóm nào emerge sau (cần prerequisite)
     → KHÔNG fixed stages → tùy chunk tích lũy của từng người
     → AI check prerequisite → suggest timing per student

  §5 — HONEST ASSESSMENT
     → Domain listing = INCOMPLETE by design
     → Timing = approximate, varies per individual
     → Era-specific sections = sẽ cần update

  §6 — CROSS-REFERENCES


KEY PRINCIPLES KHI VIẾT:
  → LIỆT KÊ SƠ LƯỢC — không cố exhaustive
  → Mỗi domain: 1 paragraph WHY + prerequisite + timing suggestion
  → Compact: target ~800-1,200 lines
  → Explicit: "đây là NHÓM, không phải MÔN CỤ THỂ"
  → v7.8 aligned


REFERENCE FILES CẦN ĐỌC KHI TRIỂN KHAI:
  → Curriculum-Framework.md (backup) — rút domain taxonomy
  → Education-Principles.md (backup) — brain constants per domain
  → Hardware-Calibration.md (backup) — per-hardware tendencies
  → Child-Development bộ 4 — developmental timeline
  → Skill-Introduction.md v2.0 — kỹ năng intro timing
```

---

## 6. IMPLEMENTATION ORDER

```
SESSION SAU — TẬP TRUNG VÀO EDUCATION-MECHANISM.MD TRƯỚC:

  Phase 0: BACKUP
    → Move 2 Research/Education/ files → backup/v1.1/
    → Move 10 Applications/Education/ files → backup/v1.0/
    → Verify backups

  Phase 1: FILE 1 — Education-Mechanism.md (FOCUS)
    → Đọc reference files (Education-Principles, Bridge, 
       Child-Dev-Mechanism, AI-Schema-Detection, Chunk.md, Cortisol-Baseline)
    → Phân tích kỹ trước khi viết
    → Viết từng section, chậm mà chắc
    → Convention check

  Phase 2: FILE 2 — Domain-Knowledge-Map.md (sau khi File 1 xong)
    → Đọc reference files (Curriculum-Framework, Hardware-Calibration,
       Skill-Introduction, Natural-Development)
    → Viết từng section
    → Convention check

  Phase 3: VERIFY + MEMORY UPDATE

  ⚠️ FILE PHỤ: KHÔNG plan trước
    → Companion files sẽ EMERGE tự nhiên trong quá trình viết
    → Nếu content quan trọng nhưng không fit → tách lúc đó
    → Pattern đã chứng minh: Logic-Feeling → Balance + Examples,
      Body-Feedback → 01-Foundation + 02-Dissonance + 03-Reward
```

---

## 7. CONSTRAINTS

```
  ✅ DO:
    → Brain-based principles (bất biến)
    → Ví dụ minh hoạ (illustrate, không prescribe)
    → v7.8 aligned (chunks compile, direction>level, 3-tier confidence)
    → Compact (2 core files total ~2,000-2,700 lines)
    → Gateway style (như AI-Schema — dẫn dắt, không đóng khung)

  ❌ DON'T:
    → Prescribe cách dạy cụ thể
    → Liệt kê exhaustive (kiến thức vô tận)
    → Fixed stages/roles (quá rigid)
    → Country-specific content (tách concern)
    → Padding (no filler — mỗi dòng phải có giá trị)
    → Plan file phụ trước (để emerge tự nhiên)
```
