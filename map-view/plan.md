# Plan: HTML Framework Viewer

> **Mục tiêu:** Trang web tĩnh giúp mọi người (đặc biệt tech experts + domain experts) dễ dàng
> khám phá ~170+ files của Human Predictive Drive framework.
> Đơn giản tối đa. Focus nội dung. Không hiệu ứng cầu kỳ.
>
> **Ngày tạo:** 2026-05-25
> **Cập nhật:** 2026-05-25 (v0.2 — resolve Q1-Q6, hosting path, refine phases)
> **Vị trí:** Human-Predictive-Drive/html-page/
> **Trạng thái:** PLANNING — REFINED

---

## Mục lục

- §0 — DỮ LIỆU NGUỒN
- §1 — PHÂN TÍCH MULTI-LAYER CATEGORY
- §2 — GLOBAL-INDEX.JSON STRUCTURE
- §3 — HTML-FILE-VIEWER DESIGN
- §4 — MD-VIEWER DESIGN
- §5 — YÊU CẦU KỸ THUẬT
- §6 — PHASES TRIỂN KHAI
- §7 — FILES SẼ TẠO

---

## §0 — DỮ LIỆU NGUỒN

```
3 FILE-INDEX.MD:
  Core-Deep-Dive/01-File-Index.md    ~127 files
  Applications/01-File-Index.md      ~12 files
  Research/01-File-Index.md          ~46 files
  ─────────────────────────────────
  TỔNG: ~185 files (không backup, không VI/)

37 unique folders (physical location)
59 unique groups (conceptual sub-group trong File-Index)

NGUỒN EXPERT MAP:
  expert-verification-map.md — 20 nhóm chuyên gia × 4 tiers
```

---

## §1 — PHÂN TÍCH MULTI-LAYER CATEGORY

### §1.1 Vấn đề: Tại sao cần multi-layer?

```
FILE-INDEX hiện tại có 2 chiều:
  folder = vị trí vật lý (Observation/, Body-Feedback/, PFC/...)
  group = nhóm khái niệm (Primitive drives, Core model, Analysis...)

NHƯNG HTML viewer cần phục vụ MỤC ĐÍCH KHÁC:
  ① URL sharing → "?category=neuroscience" cho cộng đồng neuroscience
  ② Navigation → nhóm file theo phần nào của framework
  ③ Reading guide → biết file nào là entry point, file nào là deep drill

1 layer KHÔNG ĐỦ:
  Nếu chỉ dùng expert domain → neuroscientist thấy 50 files lẫn lộn
  Nếu chỉ dùng framework area → không share URL cho cộng đồng được
  Nếu chỉ dùng content type → mất bối cảnh hoàn toàn
```

### §1.2 So sánh: 2-Layer vs 3-Layer

```
┌───────────────────────────────────────────────────────────┐
│ 2-LAYER SYSTEM                                            │
│                                                           │
│ Layer 1: Expert Domain (AI VERIFY / CHIA SẺ)              │
│   ~9 categories, multi-tag per file                       │
│   → URL: ?domain=neuroscience                             │
│                                                           │
│ Layer 2: Framework Area (PHẦN NÀO CỦA FRAMEWORK)         │
│   ~15 areas, 1 tag per file                               │
│   → Nhóm file trong kết quả filter                        │
│                                                           │
│ PRO: Đơn giản, dễ hiểu, đủ dùng                          │
│ CON: Drill files lẫn với mechanism files                  │
│      Không phân biệt entry point vs deep dive             │
└───────────────────────────────────────────────────────────┘

┌───────────────────────────────────────────────────────────┐
│ 3-LAYER SYSTEM                                            │
│                                                           │
│ Layer 1: Expert Domain (AI VERIFY / CHIA SẺ)              │
│   ~9 domains, multi-tag per file                          │
│   → URL: ?domain=neuroscience                             │
│   → "Tôi là ai?" — cho ai xem?                           │
│                                                           │
│ Layer 2: Framework Area (PHẦN NÀO CỦA FRAMEWORK)         │
│   ~15 areas, 1 tag per file                               │
│   → Nhóm file trong kết quả filter                        │
│   → "Về cái gì?" — nội dung thuộc phần nào?              │
│                                                           │
│ Layer 3: Content Type (LOẠI NỘI DUNG)                     │
│   ~6 types, 1 tag per file                                │
│   → Filter phụ (checkbox hoặc dropdown)                   │
│   → "Dạng gì?" — cơ chế, phân tích, hay tham khảo?      │
│                                                           │
│ PRO: Rất chính xác, hỗ trợ đọc có chiến lược             │
│      Expert chỉ cần mechanism? Filter được                │
│      Người mới chỉ cần overview? Filter được              │
│ CON: Build phức tạp hơn, cần classify ~185 files × 3     │
│      UI phải thiết kế cẩn thận để không overwhelm         │
└───────────────────────────────────────────────────────────┘
```

### §1.3 Đề xuất: 3-LAYER — nhưng UI chỉ hiện 2 layer mặc định

```
GIẢI PHÁP: Build 3 layers trong data, UI mặc định hiện 2:

  DEFAULT VIEW:
    [Layer 1 checkboxes: expert domain]     ← hiện
    [Layer 2 grouping: framework area]      ← hiện
    [Layer 3: content type]                 ← ẩn, toggle "Advanced filter"

  → Đơn giản cho người mới (chỉ thấy 2 layer)
  → Đủ mạnh cho expert (bật advanced filter)
  → Data đầy đủ ngay từ đầu (không cần rebuild sau)
```

### §1.4 Layer 1: Expert Domain (~9 domains, multi-tag)

```
MỤC ĐÍCH: Ai nên đọc file này? Share URL cho cộng đồng nào?
MULTI-TAG: 1 file có thể thuộc 2-3 domains.

  ID                  TÊN HIỂN THỊ               VÍ DỤ COMMUNITY SHARE
  ─────────────────────────────────────────────────────────────────────
  core                Core Architecture           Mọi người
  neuroscience        Neuroscience                r/neuroscience, neuro forums
  psychology          Psychology                  r/psychology, r/cogsci
  behavioral          Behavioral Science          r/behavioraleconomics, LessWrong
  development         Human Development           child-dev forums, parenting
  education           Education                   r/education, education researchers
  clinical            Health & Clinical           r/psychiatry, clinical forums
  social-collective   Social & Collective         r/sociology, social psych
  ai-tech             AI & Technology             HN, r/MachineLearning, LessWrong
  philosophy          Philosophy & Meta           r/philosophy, SSC

  "core" = đặc biệt: files nền tảng mà BẤT KỲ AI cũng nên đọc trước
  (Core-Hardware, Core-Software, Body-Base, Chunk, Feeling, PFC-Function...)

MAPPING TỪ expert-verification-map.md:
  neuroscience     ← Tier 1 (①②③④⑤) + Tier 4 (⑯⑰⑱)
  psychology       ← Tier 2 (⑥⑨) + ⑳
  behavioral       ← Tier 2 (⑩)
  development      ← Tier 2 (⑦) + Tier 1 (④)
  education        ← Tier 3 (⑬)
  clinical         ← Tier 2 (⑥) + Tier 3 (⑮)
  social-collective← Tier 2 (⑧) + ⑲
  ai-tech          ← Tier 3 (⑭)
  philosophy       ← Tier 3 (⑪⑫)
```

### §1.5 Layer 2: Framework Area (~16 areas, single-tag)

```
MỤC ĐÍCH: File này thuộc phần nào của framework?
SINGLE-TAG: Mỗi file thuộc đúng 1 area.
DÙNG ĐỂ: Nhóm file trong kết quả filter (visual grouping)

  ID                  TÊN HIỂN THỊ               FILE COUNT (ước tính)
  ──────────────────────────────────────────────────────────────────────
  core-foundation     Core Foundation             ~8 (Core-HW, Core-SW, Neural...)
  body-feedback       Body-Feedback System        ~15
  chunk-system        Chunk System                ~5 (+drill ~25)
  agent-mechanism     Agent & Entity              ~13
  pfc-system          PFC & Simulation            ~12
  feeling-system      Feeling System              ~12
  observation-params  Observation Parameters      ~13
  schema-anchor       Schema & Anchor             ~4
  collective          Collective & Coordination   ~5
  domain-theory       Domain Theory               ~7
  health-conditions   Health Conditions           ~10
  child-development   Child Development           ~4
  education-app       Education Applications      ~12
  global-analysis     Global & Economic Analysis  ~18
  meta-epistemology   Meta & Epistemology         ~3
  reference-tools     Reference & Tools           ~6
  melody-lens         Melody Lens                 ~4
  clarification       Clarification               ~4
```

### §1.6 Layer 3: Content Type (~6 types, single-tag)

```
MỤC ĐÍCH: Loại nội dung — giúp đọc có chiến lược.
SINGLE-TAG: Mỗi file thuộc đúng 1 type.
DÙNG ĐỂ: Filter phụ ("chỉ xem mechanism files")

  ID           TÊN HIỂN THỊ       MÔ TẢ
  ────────────────────────────────────────────────────────────
  mechanism    Mechanism           Mô tả CƠ CHẾ (HOW it works)
  analysis     Analysis            Phân tích chuyên sâu 1 chủ đề
  observation  Observation         Observation parameter file
  practical    Practical Guide     Hướng dẫn thực hành, ứng dụng
  drill        Drill & Deep Dive   Drill files, deep exploration
  reference    Reference           Vocabulary, labels, tools, index
  overview     Overview & Synthesis Tổng hợp, synthesis, entry point

READING STRATEGY:
  Người mới:     overview → mechanism → observation
  Expert verify: mechanism → analysis → drill (evidence trail)
  Ứng dụng:      practical → observation → analysis
```

### §1.7 Ví dụ: 1 file × 3 layers

```
VÍ DỤ 1: Dopamine-Is-Not-Reward.md
  Layer 1 (Domain):  [neuroscience, psychology, ai-tech]
  Layer 2 (Area):    clarification
  Layer 3 (Type):    mechanism

VÍ DỤ 2: OCD-Analysis.md
  Layer 1 (Domain):  [clinical, neuroscience, psychology]
  Layer 2 (Area):    health-conditions
  Layer 3 (Type):    analysis

VÍ DỤ 3: Education-Mechanism.md
  Layer 1 (Domain):  [education, development, psychology]
  Layer 2 (Area):    education-app
  Layer 3 (Type):    mechanism

VÍ DỤ 4: Body-Feedback-Label.md
  Layer 1 (Domain):  [core]
  Layer 2 (Area):    body-feedback
  Layer 3 (Type):    reference

VÍ DỤ 5: 99-Master-Synthesis.md
  Layer 1 (Domain):  [core]
  Layer 2 (Area):    chunk-system
  Layer 3 (Type):    overview
```

---

## §2 — GLOBAL-INDEX.JSON STRUCTURE

### §2.1 Schema per file entry

```json
{
  "files": [
    {
      "id": "dopamine-is-not-reward",
      "fileName": "Dopamine-Is-Not-Reward.md",
      "path": "Core-Deep-Dive/Clarification/Dopamine-Is-Not-Reward.md",
      "domains": ["neuroscience", "psychology", "ai-tech"],
      "area": "clarification",
      "contentType": "mechanism",
      "shortDescription": "Dopamine is a salience signal, not a reward signal",
      "fullDescription": "This file challenges the popular claim that dopamine equals reward..."
    }
  ],
  "meta": {
    "totalFiles": 185,
    "generatedDate": "2026-05-25",
    "frameworkVersion": "v7.8",
    "layers": {
      "domains": [...],
      "areas": [...],
      "contentTypes": [...]
    }
  }
}
```

### §2.2 Build process — 4 passes

```
PASS 1: Extract file list
  INPUT: 3 File-Index.md
  OUTPUT: ~185 entries với path + fileName
  METHOD: Parse pipe-delimited format

PASS 2: Full descriptions (item4) — HEAVIEST PASS
  INPUT: File-Index descriptions + đọc thêm file gốc nếu cần
  OUTPUT: fullDescription (1-3 đoạn văn, HTML-friendly)
  METHOD:
    - File-Index descriptions = base (đã rất chi tiết)
    - Rewrite thành đoạn văn dễ đọc (không bullet/notation)
    - Đọc thêm file gốc cho ~20 file quan trọng nhất
  ⚠️ ~185 files × mỗi file 3-5 câu = ~600-900 câu

PASS 3: Expert domain mapping (item2)
  INPUT: expert-verification-map.md §2-§8 routing table
  OUTPUT: domains[] per file
  METHOD:
    - §8 Research Files × Expert Group = direct mapping
    - §6 Divergence × Expert = indirect mapping
    - Core files = "core" domain
    - Drill files = inherit parent domain

PASS 4: Short descriptions (item3)
  INPUT: fullDescription từ Pass 2
  OUTPUT: shortDescription (1 câu, <100 ký tự)
  METHOD: Tóm tắt essence từ fullDescription
```

---

## §3 — HTML-FILE-VIEWER DESIGN

### §3.1 Layout

```
┌──────────────────────────────────────────────────────┐
│  HUMAN PREDICTIVE DRIVE — File Explorer              │
│  ~185 files | Framework v7.8                         │
├──────────────────────────────────────────────────────┤
│                                                      │
│  FILTER BY EXPERT DOMAIN:                            │
│  [x] All  [ ] Core  [ ] Neuroscience                 │
│  [ ] Psychology  [ ] Behavioral  [ ] Development     │
│  [ ] Education  [ ] Clinical  [ ] Social             │
│  [ ] AI & Tech  [ ] Philosophy                       │
│                                                      │
│  [Advanced filter ▼]  ← toggle Layer 3               │
│    Content Type: [All ▼]                              │
│                                                      │
│  ──── Search: [________________] ────                │
│                                                      │
│  Showing 185 files                                   │
│                                                      │
│  ═══ CORE FOUNDATION (8 files) ═══                   │
│                                                      │
│  📄 Core-Software.md                                 │
│     [core] [neuroscience] — mechanism                │
│     Cycle-based architecture of human cognition      │
│     ▸ hover → tooltip with full description          │
│     ▸ click → md-viewer.html?file=...                │
│                                                      │
│  📄 Core-Hardware.md                                 │
│     [core] [neuroscience] — mechanism                │
│     Physical brain architecture: 4 zones...          │
│                                                      │
│  ═══ BODY-FEEDBACK SYSTEM (15 files) ═══             │
│  ...                                                 │
└──────────────────────────────────────────────────────┘
```

### §3.2 Tính năng

```
① Filter by domain (Layer 1)
   - Checkboxes, multi-select
   - URL sync: ?domain=neuroscience,clinical
   - "All" = hiện tất cả

② Group by area (Layer 2)
   - Tự động nhóm kết quả theo area
   - Collapsible sections
   - File count per section

③ Advanced filter (Layer 3)
   - Dropdown: All / Mechanism / Analysis / Drill / ...
   - Ẩn mặc định, toggle hiện

④ Search
   - Full-text search trên fileName + descriptions
   - Instant filter khi gõ

⑤ Hover tooltip
   - Hiện fullDescription
   - Panel bên phải hoặc popup nhẹ

⑥ Click → md-viewer
   - Link tới md-viewer.html?file=<path>

⑦ URL sharing
   - ?domain=neuroscience → auto-check neuroscience
   - ?domain=core,neuroscience&type=mechanism
   - Share URL giữ nguyên filter state
```

---

## §4 — MD-VIEWER DESIGN

### §4.1 Layout

```
┌──────────────────────────────────────────────────────┐
│  ← Back to File List    |    📄 Chunk.md             │
│                         |    Area: Chunk System       │
│                         |    Domains: core            │
├──────────────────────────────────────────────────────┤
│                                                      │
│  [Rendered Markdown Content]                         │
│                                                      │
│  # Chunk — Core Reference                            │
│                                                      │
│  ## §1 — Definition                                  │
│  ...                                                 │
│                                                      │
│  ── Clean typography, optimized for reading ──       │
│  ── Max-width ~800px, generous line-height ──        │
│  ── Code blocks styled, tables readable ──           │
│                                                      │
└──────────────────────────────────────────────────────┘
```

### §4.2 Technical

```
MARKDOWN RENDERING:
  Library: marked.js (CDN: https://cdn.jsdelivr.net/npm/marked/marked.min.js)
  Lightweight (~40KB), zero dependencies, excellent .md support
  Fallback: nếu CDN fail → hiện raw markdown

FILE LOADING:
  fetch('../../<path>') → response.text() → marked.parse(text)
  ⚠️ Chỉ hoạt động qua HTTP server (không file://)

URL FORMAT:
  md-viewer.html?file=Core-Deep-Dive/Body-Base/Chunk/Chunk.md

TYPOGRAPHY:
  Font: system font stack (không load thêm)
  Max-width: 800px
  Line-height: 1.7
  Code: monospace, background nhẹ
  Headers: clear hierarchy
  Tables: bordered, readable

NAVIGATION:
  ← Back to File List (giữ filter state)
  Previous / Next file (trong cùng area)
```

---

## §5 — YÊU CẦU KỸ THUẬT

### §5.1 Stack

```
STACK:
  Vanilla HTML + CSS + JavaScript
  Không framework, không build tool
  1 CDN: marked.js (cho markdown rendering)

BROWSER:
  Modern browsers (Chrome, Firefox, Safari, Edge)
  ES6+ (const, let, arrow, template literals, fetch)
  Không cần hỗ trợ IE
```

### §5.2 Hosting + Path Resolution (CONFIRMED: sẽ đặt trên hosting)

```
HOSTING:
  html-page/ sẽ deploy trên hosting (GitHub Pages, Vercel, Netlify, hoặc tương đương)
  → fetch() hoạt động bình thường (không có CORS issue)
  → Toàn bộ Human-Predictive-Drive/ = site root

FOLDER STRUCTURE trên hosting:
  Human-Predictive-Drive/           ← SITE ROOT
  ├── html-page/                    ← viewer lives here
  │   ├── plan.md
  │   ├── global-index.json
  │   ├── index.html                ← entry point
  │   └── reader.html               ← markdown viewer
  ├── Core-Deep-Dive/               ← framework files
  │   ├── Observation/
  │   ├── Body-Base/
  │   └── ...
  ├── Applications/
  ├── Research/
  └── README.md

PATH RESOLUTION:
  reader.html nằm tại:    /html-page/reader.html
  .md files nằm tại:      /Core-Deep-Dive/.../file.md
                           /Research/.../file.md
                           /Applications/.../file.md

  fetch path = '../' + path_from_index
  VD: reader.html?file=Core-Deep-Dive/Body-Base/Chunk/Chunk.md
      → fetch('../Core-Deep-Dive/Body-Base/Chunk/Chunk.md')

CROSS-LINK HANDLING (reader.html):
  .md files chứa relative links tới .md files khác
  VD: [Body-Feedback.md](../Body-Feedback/Body-Feedback.md)
  → reader.html intercept click → rewrite to reader.html?file=<resolved-path>
  → Người đọc ở lại reader.html, không bị out ra raw .md

LOCAL DEVELOPMENT:
  python -m http.server 8000 (từ Human-Predictive-Drive/)
  hoặc VS Code Live Server
```

### §5.3 Ngôn ngữ (CONFIRMED: English)

```
LANGUAGE DECISION:
  global-index.json descriptions = ENGLISH
  .md file content = VIETNAMESE (framework's native language)

  WHY OK:
    - INDEX (English) = international tech audience navigation
    - CONTENT (Vietnamese) = framework itself
    - Tech experts dùng AI translate content nếu cần
    - Consistent với plan-overview-distribution.md strategy

  NOTE trong index.html:
    "Framework content is written in Vietnamese.
     Use AI translation tools for English reading."
```

---

## §6 — PHASES TRIỂN KHAI

```
PHASE 0: PLAN ✅ DONE
  - Phân tích multi-layer category ✅
  - Chốt thiết kế ✅
  - Resolve Q1-Q6 ✅

PHASE 1: GLOBAL-INDEX.JSON — skeleton (file list + 3 layers)
  INPUT: 3 File-Index.md + expert-verification-map.md
  OUTPUT: global-index.json với ~185 entries, mỗi entry có:
    - path, fileName
    - domains[] (Layer 1)
    - area (Layer 2)
    - contentType (Layer 3)
    - shortDescription (placeholder hoặc tạm)
    - fullDescription = "" (placeholder, fill ở Phase 2)
  + meta block (domains list, areas list, contentTypes list)
  METHOD:
    - Parse 3 File-Index.md → extract all file paths
    - Map domains dựa trên expert-verification-map.md routing
    - Map areas dựa trên folder structure
    - Map contentType dựa trên group field + filename patterns
    - shortDescription tạm = extract từ File-Index description (1 câu đầu)
  ⚡ Bulk classification ~185 files × 4 fields
  ⏱️ Ước tính: 1-2 sessions
  DELIVERABLE: Functional global-index.json (đủ để build HTML)

PHASE 2: GLOBAL-INDEX.JSON — descriptions (HEAVIEST)
  INPUT: File-Index descriptions + đọc thêm .md files khi cần
  OUTPUT: fullDescription (English, 2-4 sentences per file) +
          shortDescription refined (English, 1 sentence, <120 chars)
  METHOD:
    - File-Index descriptions = base (đã rất chi tiết, tiếng Việt)
    - Rewrite sang English, dạng đoạn văn đọc được
    - Đọc thêm file gốc cho ~20 file phức tạp/quan trọng nhất
    - Đánh dấu "recommended" cho ~10-15 entry-point files (Q8)
  BATCHING: ~30-40 files/session
    Batch A: Core-Deep-Dive root + Observation + Clarification (~25 files)
    Batch B: Body-Feedback + Body-Base (~20 files)
    Batch C: Chunk + Agent-Mechanism (~20 files)
    Batch D: PFC + Feeling + Schema + Melody (~30 files)
    Batch E: Collective + Domain + Drill subfolders (~30 files)
    Batch F: Research (Health + Global + Love + Meta) (~40 files)
    Batch G: Applications + remaining (~20 files)
  ⏱️ Ước tính: 4-7 sessions
  DELIVERABLE: Complete global-index.json

PHASE 3: INDEX.HTML (file viewer)
  BUILD:
    - Load global-index.json via fetch
    - Layer 1: domain checkboxes (multi-select)
    - Layer 2: area grouping (collapsible sections)
    - Layer 3: content type dropdown (advanced filter, hidden default)
    - Search bar (fileName + descriptions)
    - Hover/click → fullDescription popup
    - Click → reader.html?file=<path>
    - URL params: ?domain=X,Y&type=Z (sync with checkboxes)
    - File count badge per section
    - "Start here" highlight cho recommended files
  STYLE:
    - Minimal, clean, no effects
    - System font stack
    - Dark/light preference (prefers-color-scheme)
    - Mobile-friendly layout (responsive grid)
  ⏱️ Ước tính: 1-2 sessions
  DELIVERABLE: Functional index.html

PHASE 4: READER.HTML (markdown viewer)
  BUILD:
    - Load .md file via fetch('../' + path)
    - Render via marked.js (CDN)
    - Auto-generate TOC from headings (Q9)
    - Navigation: ← Back to list (preserve filter state)
    - File metadata header (area, domains, short description)
    - Cross-link interception: .md links → reader.html?file=<path> (Q7)
  STYLE:
    - Typography optimized for long-form reading
    - Max-width: 800px centered
    - Line-height: 1.7
    - Code blocks: monospace, subtle background
    - Tables: bordered, scrollable on mobile
    - Headings: clear hierarchy, linkable anchors
  ⏱️ Ước tính: 1 session
  DELIVERABLE: Functional reader.html

PHASE 5: TEST + REFINE
  TEST:
    - All ~185 file links resolve correctly
    - All filter combinations work (domain × type × search)
    - URL sharing preserves state
    - reader.html renders all .md flavors (code, tables, nested lists)
    - Cross-links between .md files work in reader.html
    - Responsive check (index on mobile, reader on desktop)
  REFINE:
    - Description quality review (random sample ~20 files)
    - Domain/area classification review
    - Loading performance (large JSON parse time)
    - 404 handling (file not found)
  ⏱️ Ước tính: 1 session
  DELIVERABLE: Production-ready html-page/

TỔNG: ~8-13 sessions
  Phase 1: 1-2 sessions (skeleton)
  Phase 2: 4-7 sessions (descriptions — heaviest, có thể song song với Phase 3-4)
  Phase 3: 1-2 sessions (index.html)
  Phase 4: 1 session (reader.html)
  Phase 5: 1 session (test)

NOTE: Phase 3+4 có thể bắt đầu ngay sau Phase 1 (dùng placeholder descriptions).
      Phase 2 có thể chạy song song — fill descriptions dần.
      → Có thể thấy kết quả visual sớm nhất sau 2-3 sessions.
```

---

## §7 — FILES SẼ TẠO

```
Human-Predictive-Drive/
├── html-page/
│   ├── plan.md                  ← file này (DONE)
│   ├── global-index.json        ← Phase 1+2 (data)
│   ├── index.html               ← Phase 3 (file viewer — entry point)
│   └── reader.html              ← Phase 4 (markdown viewer)
│
├── Core-Deep-Dive/              ← existing framework files
├── Applications/                ← existing framework files
├── Research/                    ← existing framework files
└── README.md                    ← existing
```

---

## §8 — CÂU HỎI — RESOLVED + REMAINING

### §8.1 Resolved

```
Q1: Drill files → ✅ INCLUDE tất cả (trừ backup). Layer 3 "drill" giúp filter.
Q2: Ngôn ngữ   → ✅ ENGLISH cho descriptions. Content (.md) = Vietnamese.
Q4: JSON format → ✅ FILE RIÊNG (global-index.json). Dễ maintain, dễ update.
Q5: Path        → ✅ html-page/ ở root → fetch('../' + path). RESOLVED.
Q6: Layers      → ✅ 3-LAYER (build cả 3, UI default hiện 2). Confirmed.
Q3: Thứ tự     → ✅ Theo area (Layer 2), trong area theo File-Index order.
```

### §8.2 Remaining — cần phân tích thêm

```
Q7: Intra-link handling trong reader.html
    .md files chứa relative links tới .md khác
    (VD: [Chunk.md](../Chunk/Chunk.md))
    → Cần intercept + rewrite to reader.html?file=<path>
    → HOW: resolve relative path vs absolute path?
    APPROACH: intercept all .md link clicks, resolve relative to current file,
              rewrite to reader.html?file=<resolved>
    COMPLEXITY: Medium — cần parse relative paths (../ chains)
    PRIORITY: Phase 3 (nice-to-have, có thể Phase 5)

Q8: "Start here" / recommended reading order
    ~185 files quá nhiều cho người mới
    → Nên có 1 "guided path" (5-10 files) cho newcomers?
    APPROACH: Thêm field "recommended": true/false + "readingOrder": number
             trong global-index.json cho ~10-15 key files
    PRIORITY: Phase 2 (khi viết descriptions, đánh dấu luôn)

Q9: Mục lục (Table of Contents) trong reader.html
    .md files dài (1,000-3,000+ lines) → cần TOC sidebar?
    APPROACH: Parse headings (## §1, ## §2...) → generate TOC
    COMPLEXITY: Low (marked.js hỗ trợ heading extraction)
    PRIORITY: Phase 4

Q10: Search scope
     Hiện tại search trên fileName + descriptions
     → Có nên search TRONG nội dung .md files không?
     APPROACH: Full-text search cần pre-index → phức tạp
     DECISION: Phase 1 = search descriptions only. Full-text = future.

Q11: Mobile responsive
     Framework audience chủ yếu đọc trên desktop (long-form reading)
     NHƯNG index.html nên responsive (tìm file trên phone)
     DECISION: index.html responsive, reader.html desktop-optimized
               (readable on mobile, NOT optimized for mobile)
```

---

## §9 — TECHNICAL DETAILS CHUẨN BỊ TRƯỚC

### §9.1 reader.html — Cross-link resolution algorithm

```
KHI NGƯỜI ĐỌC CLICK 1 LINK TRONG .md:

  1. Intercept tất cả <a> clicks trong rendered content
  2. Nếu href kết thúc bằng .md:
     a. Resolve relative path:
        currentFile = "Core-Deep-Dive/Body-Base/Chunk/Chunk.md"
        href = "../Body-Feedback/Body-Feedback.md"
        → resolved = "Core-Deep-Dive/Body-Base/Body-Feedback/Body-Feedback.md"
     b. Check resolved path có trong global-index.json không
     c. Nếu có → redirect to reader.html?file=<resolved>
     d. Nếu không → open raw file (fallback)
  3. Nếu href là external (http/https) → open bình thường
  4. Nếu href là anchor (#) → scroll bình thường
```

### §9.2 index.html — URL state management

```
URL FORMAT:
  index.html                                    → all files, no filter
  index.html?domain=neuroscience                → 1 domain
  index.html?domain=neuroscience,clinical       → 2 domains (OR)
  index.html?type=mechanism                     → 1 content type
  index.html?domain=neuroscience&type=mechanism → combined
  index.html?search=dopamine                    → search term
  index.html?domain=core&search=body            → combined

STATE SYNC:
  - On page load: parse URL params → set checkboxes/search
  - On filter change: update URL params (history.replaceState)
  - Copy URL → share → recipient sees same filter
```

### §9.3 global-index.json size estimate

```
~185 entries × ~500 bytes/entry (avg) = ~90KB
+ meta block = ~2KB
TOTAL: ~92KB (acceptable, loads fast)

fullDescription ~200 words avg × 185 = ~37,000 words
→ JSON file ~150-200KB with descriptions
→ Still fast enough (< 1s on most connections)
```

---

## Cross-references

```
plan.md (file này)
  ← html-viewer.txt (yêu cầu gốc)
  ← expert-verification-map.md (nguồn Layer 1 domains)
  ← 3× File-Index.md (nguồn file list + descriptions)
  → plan-overview-distribution.md (context: overview blog distribution)
  → framing-engagement-value.md (context: how to present value)
  → plan-public.md (context: general distribution strategy)
```
