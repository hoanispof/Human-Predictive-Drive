---
title: Education Applications — Bản Đồ Folder v2.0
version: 2.0
updated: 2026-05-11
status: v2.0
purpose: |
  "Bắt đầu đọc từ đây" — map tất cả files, flow, cách dùng.
  Reflects v7.8 restructure: re-based trên Education-Mechanism v1.0 + DKM v1.0.
position: TẦNG 4 — Applications/Education (era-specific, derived từ Tầng 3)
previous: backup/v1.0/00_Overview.md (286L, DRAFT, 2026-04-03)
changes_v2:
  - Tầng 1 refs: Core-v7.5 → Core-Software + Core-Hardware + Core-Interface
  - Tầng 2 refs: Child-Dev bộ 3 → bộ 4 (+ Child-Dev-Mechanism)
  - Tầng 3 refs: Education-Principles + Bridge → Mechanism v1.0 + DKM v1.0
  - All file descriptions + statistics updated for v2.0 rewrites
  - Flow diagram redrawn for new foundation
  - Reading order updated
---

# Education Applications — Bản Đồ Folder v2.0

> **Bắt đầu đọc từ đây.**
> Map tất cả files trong folder, flow giữa chúng, cách dùng per audience.
>
> **Vị trí:** TẦNG 4 — ứng dụng nguyên lý bất biến cho era hiện tại.
> **Nền tảng:** Education-Mechanism.md v1.0 (HOW) + Domain-Knowledge-Map.md v1.0 (WHAT).
> **Mọi file v2.0 đã re-base lên nền tảng mới (2026-05-11).**

---

## Mục lục

0. Mục đích folder
1. Bản đồ files + Flow
2. Cách đọc — thứ tự recommended
3. Kết nối với Tầng 3 (Research/Education/)
4. Kết nối với Tầng 1-2 (Core + Child-Dev)
5. Durability guide + Statistics

---

## 0. MỤC ĐÍCH FOLDER NÀY

```
FOLDER NÀY LÀM GÌ:

  Tầng 1-3 (ĐÃ CÓ) trả lời:
    → Não HOẠT ĐỘNG thế nào? (Core-Deep-Dive/)
    → Trẻ PHÁT TRIỂN thế nào 0-6? (Research/Child-Development/)
    → Nguyên lý giáo dục BẤT BIẾN là gì? (Research/Education/)

  Folder NÀY (Tầng 4) trả lời:
    → Cho thời đại HIỆN TẠI, hệ thống giáo dục NÊN thế nào?
    → Dạy CÁI GÌ, khi nào, cho ai, sâu bao nhiêu?
    → Nhận diện per-individual hardware THẾ NÀO?
    → Thời đại 2025+ ĐANG thay đổi gì?

  = ỨNG DỤNG nguyên lý bất biến → cho era cụ thể


FOLDER NÀY KHÔNG LÀM GÌ:

  ❌ Thay thế Tầng 1-3 → PHẢI đọc nền tảng trước
  ❌ Cho giải pháp per-country → xem Country/ (Phase F)
  ❌ Cho lesson plans cụ thể → file = FRAMEWORK level
  ❌ Dự đoán tương lai chính xác → mọi prediction = sẽ sai 1 phần
```

---

## 1. BẢN ĐỒ FILES + FLOW

```
KIẾN TRÚC TỔNG THỂ — 5 TẦNG:

  ┌─────────────────────────────────────────────────────────────────┐
  │ TẦNG 1: Core-Deep-Dive/                                        │
  │   Não hoạt động thế nào (KHÔNG ĐỔI)                           │
  │   Core-Software.md (cycle), Core-Hardware.md (zones),           │
  │   Core-Interface.md (observer), Chunk.md, Cortisol-Baseline.md, │
  │   Imagine-Final.md, Body-Feedback-Mechanism.md,                │
  │   Reward-Signal-Architecture.md, Agent-Mechanism.md...          │
  ├─────────────────────────────────────────────────────────────────┤
  │ TẦNG 2: Research/Child-Development/                             │
  │   Con người phát triển thế nào 0-6 (KHÔNG ĐỔI)               │
  │   Child-Dev-Mechanism.md → Mother-Opt → Natural-Dev → Skill-In │
  ├─────────────────────────────────────────────────────────────────┤
  │ TẦNG 3: Research/Education/                                     │
  │   Nguyên lý giáo dục BẤT BIẾN (KHÔNG ĐỔI)                   │
  │   Education-Mechanism.md v1.0 ⭐ (HOW — 8 nguyên lý arc design)│
  │   Domain-Knowledge-Map.md v1.0 (WHAT — 3-tier domain taxonomy)  │
  │   Observation/ (Education-Arms-Race, Empathy-Education)         │
  ├─────────────────────────────────────────────────────────────────┤
  │ TẦNG 4: Applications/Education/ [FOLDER NÀY]                   │
  │   Ứng dụng cho thời đại hiện tại (SEMI-DURABLE)               │
  │   → Chi tiết bên dưới                                         │
  ├─────────────────────────────────────────────────────────────────┤
  │ TẦNG 5: Applications/Education/Country/                         │
  │   Per-country analysis + recommendations                        │
  │   VN/ (đầu tiên) → countries khác nếu mở rộng                │
  └─────────────────────────────────────────────────────────────────┘


FILES TRONG FOLDER NÀY:

  ┌──────────────────────────────────────────────────────────────────┐
  │                                                                  │
  │  00_Overview.md (file này)                                       │
  │    = Bản đồ — đọc TRƯỚC TIÊN                                   │
  │                                                                  │
  │  Education-System.md v2.0 ⭐ KHUNG CHÍNH (~1,554 dòng)         │
  │    = "Nếu làm ĐÚNG, education trông thế nào?"                  │
  │    → 4 stages (brain-based), 5 roles, bridge strategy,          │
  │      assessment, teacher/parent, integration, constraints        │
  │    → TẤT CẢ files khác CONNECT qua file này                    │
  │    → Re-based: Education-Mechanism v1.0 (8 nguyên lý arc design)│
  │                                                                  │
  │  Hardware-Calibration.md v1.0 (~1,538 dòng)                     │
  │    = "Nhận diện + điều chỉnh per-individual THẾ NÀO?"          │
  │    → 6 hardware dimensions, observable indicators per age,       │
  │      calibration strategies, neurodiversity, miscalibrations     │
  │    → FILE DURABLE NHẤT (brain-based → decades)                  │
  │    → Re-based: Core-Hardware + PFC-Hardware + Modality + Body-B │
  │                                                                  │
  │  Curriculum-Framework.md v2.0 (~754 dòng)                        │
  │    = "DẠY CÁI GÌ, khi nào, sâu bao nhiêu?"                    │
  │    → Foundation matrix (6 domains × 4 stages × depth targets),   │
  │      era-specific delivery, sequencing, cái cần giảm/bỏ        │
  │    → DERIVED từ DKM (taxonomy) × ES (stages) × Mechanism (HOW)  │
  │                                                                  │
  │  Era-Analysis-2025.md v2.0 (~724 dòng)                           │
  │    = "Thời đại 2025+ ĐANG XẢY RA GÌ cho education?"            │
  │    → Tech landscape, changing/stable skills, 6 uncertainties,    │
  │      6 era themes, era-specific skill domains                   │
  │    → ⚠️ FILE CÓ HẠN SỬ DỤNG (2-3 năm)                        │
  │                                                                  │
  │  plan-education-restructure.md                                   │
  │    = Plan restructure v7.8 — tracking progress + decisions       │
  │                                                                  │
  │  PLAN.md                                                         │
  │    = Plan triển khai folder — lịch sử quyết định gốc            │
  │                                                                  │
  │  backup/v1.0/ — bản cũ (pre-v7.8 restructure)                   │
  │                                                                  │
  └──────────────────────────────────────────────────────────────────┘


FLOW GIỮA FILES:

  Research/Education/ (Tầng 3):
    Education-Mechanism.md v1.0 (HOW — 8 nguyên lý)
    Domain-Knowledge-Map.md v1.0 (WHAT — 3-tier taxonomy)
           │
           ↓
    Education-System.md v2.0 ⭐ (KHUNG — stages, roles, assessment)
           │
      ┌────┴──────────────────┐
      ↓                        ↓
    Hardware-              Era-Analysis-
    Calibration.md v1.0    2025.md v2.0
    (per-individual)       (era context)
      │                        │
      └────┬───────────────────┘
           ↓
    Curriculum-Framework.md v2.0 (WHAT × WHEN × HOW DEEP)
           │
           ↓
    Country/ files (Phase F — per-country application)
```

---

## 2. CÁCH ĐỌC — THỨ TỰ RECOMMENDED

```
NẾU MỚI BẮT ĐẦU (chưa đọc nền tảng):
  1. Education-Mechanism.md v1.0 (Tầng 3) — 8 nguyên lý arc design
  2. Domain-Knowledge-Map.md v1.0 (Tầng 3) — domain taxonomy
  3. Education-System.md v2.0 ⭐ — khung system design
  4. Era-Analysis-2025.md v2.0 — context thời đại
  5. Curriculum-Framework.md v2.0 — delivery matrix
  6. Hardware-Calibration.md v1.0 — per-individual
  → = Mechanism → Domains → System → Context → Delivery → Individual


NẾU MUỐN SÂU (đọc từ Core):
  1. Core-Software.md v1.0 (cycle) + Core-Hardware.md v1.0 (zones)
  2. Chunk.md v2.0, Cortisol-Baseline.md v2.0, Imagine-Final.md
  3. Child-Development-Mechanism.md v1.0 + bộ 3 (Mother/Natural/Skill)
  4. Education-Mechanism.md v1.0 + Domain-Knowledge-Map.md v1.0
  5. → Rồi folder này theo thứ tự trên


NẾU LÀ GIÁO VIÊN / PHỤ HUYNH (muốn thực hành):
  1. Education-System.md v2.0 §7 (Teacher) hoặc §8 (Parent)
  2. Hardware-Calibration.md v1.0 §2-§3 (observe + calibrate)
  3. Hardware-Calibration.md v1.0 §5 (labels sai phổ biến)
  4. Curriculum-Framework.md v2.0 §4 (sequencing per stage)
  → = Practical sections TRƯỚC, theory SAU nếu muốn


NẾU MUỐN ÁP DỤNG CHO QUỐC GIA (VN):
  1. Education-System.md v2.0 (khung)
  2. Era-Analysis-2025.md v2.0 (context)
  3. → Country/VN/ files (Phase F)


NẾU MUỐN CẬP NHẬT (era đổi):
  1. Era-Analysis-2025.md → UPDATE (era context)
  2. Curriculum-Framework.md §3 → UPDATE (era-specific delivery)
  3. DKM §2 → UPDATE (era-specific domain list)
  4. Các files khác → REVIEW nhưng likely GIỮ NGUYÊN
  → = Modular design: update 1-2 files ≠ rewrite tất cả
```

---

## 3. KẾT NỐI VỚI TẦNG 3 (Research/Education/)

```
NỀN TẢNG MỚI (v7.8 — thay thế Education-Principles + Bridge cũ):


Education-Mechanism.md v1.0 ⭐ = NGUYÊN LÝ ARC DESIGN (HOW)
  → 8 nguyên lý brain-based cho learning arc design:
    §2.2 Direction > Level, §2.3 Cost Formula, §2.4 Prerequisite,
    §2.5 Mini-arcs, §2.6 Imagine-Final, §2.7 Feedback,
    §2.8 Consolidation, §2.9 Depth Assessment
  → §3 Bridge + Motivation (4 nguồn fill, 3 ORIGIN, transition)
  → §4 AI-Assisted Model (3-layer: AI + Teacher + Student)
  → = ENGINE cho tất cả files trong folder này

Domain-Knowledge-Map.md v1.0 = BẢN ĐỒ DOMAIN (WHAT)
  → 3-tier taxonomy: Foundation (6) + Era-specific (6) + Per-hardware
  → Prerequisite logic per domain
  → = FUEL — "nhóm kiến thức nào cần per era"

Observation/Empathy-Education.md v2.0 = Empathy per age
  → Self-Pattern-Modeling-based (Agent-Mechanism.md), per-age development guide
  → Social/Emotional domain application

Observation/Education-Arms-Race.md v1.2 = Competition dynamics
  → Societal pressure patterns affecting education
  → Context cho Era-Analysis + Country/ files

Expansion-Saturation-Crisis.md v1.0 = Expansion dynamics
  → Global grad unemployment, discovery shift
  → Macro context cho education system design
```

---

## 4. KẾT NỐI VỚI TẦNG 1-2 (Core + Child-Dev)

```
CORE-DEEP-DIVE/ (TẦNG 1) — BRAIN MECHANISMS:

  → Education-System: 4 stages based on PFC development
  → Hardware-Calibration: 6 dimensions from Core hardware parameters
  → Era-Analysis: brain mechanism = "cái KHÔNG đổi" per era
  → Curriculum: mechanism-based delivery per domain

  Key Core files referenced:
    Core-Software.md v1.0 — cycle-based architecture, chunks = sole substrate
    Core-Hardware.md v1.0 — 4 zones A/B/C/D, hardware profiles
    Core-Interface.md — observer interface
    Chunk.md v2.0 — compile, strength levels, prerequisite chains
    Cortisol-Baseline.md v2.0 — amplifier reframe, 5 Roles, direction > level
    Imagine-Final.md — purpose engine, lifecycle 5 phases
    Body-Feedback-Mechanism.md v1.2 — 2 sources × 3 dynamics
    Reward-Signal-Architecture.md v1.0 — Evaluative / Direct-State
    Agent-Mechanism.md v1.0 — Self-Pattern-Modeling Compiled/Fresh, social processing
    PFC-Hardware.md v1.1 — DRD4, COMT, individual parameters
    PFC-Configuration.md v1.0 — 6 dynamic modes
    Modality.md v1.0 — 6 encoding channels
    Body-Base.md v2.0 — Model 3+1, interoception
    Sensitivity-Classification.md v1.0 — 3 hardware sensitivity groups


RESEARCH/CHILD-DEVELOPMENT/ (TẦNG 2) — 0-6 FOUNDATION:

  → Education-System §1: Stage 1 = Child-Dev bộ 4 (KHÔNG repeat)
  → Education-System §8: parent role continues from Child-Dev
  → Hardware-Calibration §2: early indicators (0-6 observation)
  → Curriculum §2: foundation begins ON TOP of 0-6 wiring

  Child-Dev bộ 4:
    Child-Development-Mechanism.md v1.0 — khung nguyên lý (4+1 compile,
      approach/avoidance, cortisol, sensitive periods)
    Mother-Optimization.md — prenatal hardware quality
    Natural-Development.md — 0-6 brain tự wire
    Skill-Introduction.md — 0-6 giới thiệu kỹ năng
```

---

## 5. DURABILITY GUIDE + STATISTICS

```
  ┌────────────────────────────┬────────────┬─────────────────────┐
  │ File                       │ Durability │ Update khi nào       │
  ├────────────────────────────┼────────────┼─────────────────────┤
  │ Hardware-Calibration.md    │ ██████████ │ Khi neuroscience     │
  │ v1.0 (brain-based)        │ DECADES    │ advance (hiếm)       │
  ├────────────────────────────┼────────────┼─────────────────────┤
  │ Education-System.md        │ ███████░░░ │ Brain design: giữ    │
  │ v2.0 (brain + era format)  │ SEMI       │ Era format: 3-5 năm  │
  ├────────────────────────────┼────────────┼─────────────────────┤
  │ Curriculum-Framework.md    │ █████░░░░░ │ §2 Foundation: giữ   │
  │ v2.0 (foundation + era)    │ MIXED      │ §3 Era-skills: 3-5y  │
  ├────────────────────────────┼────────────┼─────────────────────┤
  │ Era-Analysis-2025.md       │ ██░░░░░░░░ │ Review: 12-18 tháng  │
  │ v2.0 (era snapshot)        │ TIME-BOUND │ Major update: 2-3 năm│
  │                            │            │ ⚠️ Hạn sử dụng NGẮN │
  ├────────────────────────────┼────────────┼─────────────────────┤
  │ 00_Overview.md             │ ████████░░ │ Khi thêm/bỏ files    │
  │ v2.0 (follows folder)      │ FOLLOWS    │                      │
  └────────────────────────────┴────────────┴─────────────────────┘

  KHI ERA ĐỔI (VD: major AI breakthrough):
    → Era-Analysis: VIẾT LẠI (§1 tech landscape + §5 implications)
    → Curriculum §3: update era-specific delivery
    → DKM §2: update era-specific domain list
    → Education-System §9: review AI integration section
    → Hardware-Calibration: GIỮ NGUYÊN (brain không đổi)
    → = Modular design: update 1-2 files ≠ rewrite tất cả


THỐNG KÊ — PHASE 1 (main files) v2.0:

  ┌────────────────────────────┬───────────┬─────────────────────┐
  │ File                       │ Lines     │ Sections            │
  ├────────────────────────────┼───────────┼─────────────────────┤
  │ Education-System.md v2.0 ⭐ │ ~1,554    │ §0-§12 (13 sections)│
  │ Hardware-Calibration v1.0  │ ~1,538    │ §0-§7 (8 sections)  │
  │ Curriculum-Framework v2.0  │ ~754      │ §0-§6 (7 sections)  │
  │ Era-Analysis-2025 v2.0     │ ~724      │ §0-§6 (7 sections)  │
  │ 00_Overview.md v2.0        │ ~363      │ §0-§5 (6 sections)  │
  ├────────────────────────────┼───────────┼─────────────────────┤
  │ TOTAL Tầng 4               │ ~4,933    │ 41 sections         │
  └────────────────────────────┴───────────┴─────────────────────┘

  + Tầng 3 nền tảng:
    Education-Mechanism.md v1.0 (~1,279 dòng)
    Domain-Knowledge-Map.md v1.0 (~846 dòng)
  = TỔNG BỘ KHUNG (Tầng 3+4): ~7,058 dòng

  + Country/VN/ (Phase F — chưa restructure):
    4 files, ~3,921 dòng, 91 old refs cần update


RESTRUCTURE HISTORY:

  v1.0 (2026-04-03): Initial draft, based on Education-Principles "10 NL"
  v2.0 (2026-05-11): Full rewrite all 5 files
    → Re-based: "10 NL" → Education-Mechanism v1.0 (8 nguyên lý)
    → Re-based: Core-v7.5 → 3 Core Maps
    → Re-based: Education-Bridge → Mechanism §3
    → Added: v7.8 concepts (Evaluative/Direct-State, approach/avoidance, Self-Pattern-Modeling Compiled,
             chunk compilation levels, 4 nguồn fill, 3 ORIGIN)
    → All cross-refs → current file paths
    → v1.0 → backup/v1.0/
```
