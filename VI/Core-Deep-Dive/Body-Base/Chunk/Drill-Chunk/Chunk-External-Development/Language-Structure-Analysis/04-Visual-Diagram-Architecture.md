---
title: Visual & Diagram Architecture — Cấu trúc ngôn ngữ hình ảnh
created: 2026-04-16 (N+5 exploration session)
status: REFERENCE — tài liệu tham khảo, đọc nghiền ngẫm
scope: Hệ thống visual/diagram như communication format — bản đồ, sơ đồ, biểu đồ, bản vẽ kỹ thuật, icon, emoji
purpose: Hiểu visual/diagram encode GÌ mà text và math KHÔNG encode hiệu quả: SPATIAL RELATIONSHIPS + SIMULTANEOUS OVERVIEW
parent: ../../plan.md (F3 Chunk-External-Development)
language: Tiếng Việt primary + English technical
---

# Visual & Diagram Architecture — Cấu trúc ngôn ngữ hình ảnh

> **Mục đích**: "1 hình = 1,000 chữ" — nhưng TẠI SAO? File này "mổ xẻ" cấu trúc visual/diagram như 1 communication format. Visual encode thứ mà text KHÔNG encode hiệu quả: **spatial relationships + simultaneous overview** (nhìn toàn cảnh 1 lúc).
>
> **So sánh**: NL = sequential meaning. Math = precise quantity. Music = temporal emotion. Visual = **spatial relationships + instant overview**.

---

## MỤC LỤC

- §1 — "Từ vựng" visual: Các thành phần cơ bản
- §2 — Các loại visual system
- §3 — Hierarchy: Element → Group → Composition → System
- §4 — So sánh: Visual vs Text vs Math vs Music
- §5 — Visual encode gì mà format khác KHÔNG encode được
- §6 — Lịch sử phát triển
- §7 — Framework lens + Câu hỏi mở

---

## §1 — "Từ vựng" visual: Các thành phần cơ bản

### §1.1 — Primitive elements (Nguyên tố hình ảnh)

```
Mọi visual system đều BUILD từ vài nguyên tố cơ bản:

POINT (Điểm)        •                          = vị trí, không có kích thước
LINE (Đường)         ───, ╱, ╲, ⌇, ∿           = kết nối, hướng, ranh giới
SHAPE (Hình)         □ ○ △ ◇ ☆                 = vùng, đối tượng, container
COLOR (Màu)          🔴🟢🔵🟡⚫⚪              = phân loại, trạng thái, cảm xúc
TEXT (Chữ)           "Label"                    = tên, giá trị, chú thích
ICON (Biểu tượng)   🏠 👤 ⚙️ ⚠️ ✅ ❌        = concept nén thành 1 hình

→ Chỉ 6 nguyên tố → build TOÀN BỘ visual communication
→ Giống: 26 chữ cái → build toàn bộ English text
→ Giống: 12 nốt → build toàn bộ Western music
```

### §1.2 — Visual properties (Thuộc tính hình ảnh)

```
Mỗi element có PROPERTIES điều chỉnh ý nghĩa:

POSITION (Vị trí)      = ở đâu trên canvas → spatial relationship
SIZE (Kích thước)       = to/nhỏ → importance, quantity
COLOR (Màu sắc)        = đỏ/xanh/vàng → category, status, emotion
OPACITY (Độ trong)      = đậm/mờ → emphasis, active/inactive
ORIENTATION (Hướng)     = xoay, nghiêng → direction, flow
SHAPE (Hình dạng)       = tròn/vuông/tam giác → type, category
LINE STYLE              = ── (thực), --- (đứt), ═══ (đôi) → strength, certainty
LINE THICKNESS          = mỏng/dày → importance, flow volume
GROUPING (Nhóm)         = proximity, enclosure → belongs together
LAYERING (Lớp)          = trước/sau → depth, priority

→ Gestalt principles (1920s):
  Proximity:    items GẦN nhau → perceive as GROUP
  Similarity:   items GIỐNG nhau → perceive as GROUP
  Closure:      items GẦN kín → perceive as SHAPE
  Continuity:   items THẲNG HÀNG → perceive as LINE/FLOW
  Figure-Ground: FOREGROUND tách khỏi BACKGROUND

→ Đây là "ngữ pháp" vô thức của visual — não apply TỰ ĐỘNG
→ Designer biết: dùng proximity thay vì border để group → cleaner
→ Game dev biết: UI layout = Gestalt principles applied
```

---

## §2 — Các loại visual system

### §2.1 — Maps (Bản đồ) — encode SPATIAL REALITY

```
MỤC ĐÍCH: Biểu diễn vị trí + quan hệ KHÔNG GIAN THỰC TẾ

  World map         = continents, countries, oceans
  City map          = streets, buildings, landmarks
  Floor plan        = rooms, walls, doors, furniture
  Game map          = level layout, spawn points, paths

PROPERTIES:
  Scale:    1:1,000 (city map) → 1:50,000,000 (world map)
  Projection: Mercator, Robinson, Peters (trade-off: shape vs area vs direction)
  Legend:   color + icon = category (🔵 = water, 🟢 = park, 🔴 = emergency)

⭐ MAP vs TEXT cho cùng information:
  Text: "Từ nhà đi thẳng 200m, rẽ trái, đi 100m, rẽ phải, đi 50m đến tiệm"
  Map:  [nhà] → → → ↰ → → ↱ → [tiệm]
  → Map: NHÌN 1 LẦN hiểu toàn cảnh. Text: phải đọc TUẦN TỰ + imagine.
  → "1 bản đồ = 1,000 chữ" ĐÚNG cho spatial information
  → NHƯNG: map KHÔNG thể encode "tiệm đó ngon lắm" (cần text)
```

### §2.2 — Charts & Graphs (Biểu đồ) — encode QUANTITATIVE RELATIONSHIPS

```
MỤC ĐÍCH: Biểu diễn DỮ LIỆU SỐ dưới dạng hình ảnh

BAR CHART (Biểu đồ cột):
  ████████████  Sales Q1: $120k
  ████████      Sales Q2: $80k
  ██████████████ Sales Q3: $140k
  → Encode: so sánh GIỮA categories

LINE CHART (Biểu đồ đường):
       /\
      /  \  /
  ___/    \/
  → Encode: TREND theo thời gian

PIE CHART (Biểu đồ tròn):
  → Encode: TỈ LỆ các phần trong tổng thể

SCATTER PLOT (Biểu đồ phân tán):
  → Encode: TƯƠNG QUAN giữa 2 biến (correlation)

HEATMAP:
  → Encode: CƯỜNG ĐỘ trên grid 2D (game dev: damage heatmap)

⭐ CHART vs MATH vs TEXT:
  Math:  μ = 120, σ = 15, n = 100, t-test p < 0.05
  Chart: [hình: 2 phân bố overlap nhau, vùng overlap nhỏ]
  Text:  "Nhóm A trung bình cao hơn nhóm B đáng kể"

  → CÙNG information, nhưng:
    Math = CHÍNH XÁC NHẤT
    Chart = TRỰC QUAN NHẤT (nhìn thấy pattern INSTANT)
    Text = ACCESSIBLE NHẤT (ai cũng hiểu)
  → Scientist dùng CẢ 3: chart để thấy, math để chứng minh, text để giải thích
```

### §2.3 — Diagrams (Sơ đồ) — encode ABSTRACT RELATIONSHIPS

```
MỤC ĐÍCH: Biểu diễn QUAN HỆ giữa concepts (không phải spatial/numerical)

FLOWCHART (Lưu đồ):
  [Start] → [Input] → <Decision?> → [Process A] → [End]
                           ↓ No
                       [Process B] → [End]
  → Encode: PROCESS flow, decision logic
  → Game dev: AI behavior tree, quest flow, UI flow

ORG CHART (Sơ đồ tổ chức):
           [CEO]
          /     \
      [CTO]    [CFO]
     /    \      |
  [Dev]  [QA]  [Finance]
  → Encode: HIERARCHY, reporting structure

MIND MAP:
                 ┌─ Physics
     ┌─ Science ─┼─ Chemistry
     │           └─ Biology
  Knowledge ─┼─ Math
     │       ├─ Language
     └─ Art  ─┼─ Music
              └─ Visual
  → Encode: BRANCHING relationships, brainstorm, categories

ENTITY-RELATIONSHIP (ER) Diagram:
  [User] 1──n [Order] n──m [Product]
  → Encode: data RELATIONSHIPS (game dev: database schema)

UML Class Diagram:
  ┌──────────────┐       ┌──────────────┐
  │ GameObject    │       │ Component    │
  ├──────────────┤  has  ├──────────────┤
  │ + name       │ 1───n │ + enabled    │
  │ + transform  │       │ + Update()   │
  └──────────────┘       └──────────────┘
  → Encode: CLASS hierarchy, relationships (game dev: architecture)

STATE DIAGRAM:
  [Idle] →(attack)→ [Attack] →(hit)→ [Stun] →(recover)→ [Idle]
    ↑                                                      |
    └──────────────(die)→ [Dead]───────────────────────────┘
  → Encode: STATE transitions (game dev: enemy AI, animation state machine)

NETWORK DIAGRAM:
  [Server] ←→ [Client 1]
     ↕
  [Database] ←→ [Client 2]
  → Encode: CONNECTION topology

⭐ DIAGRAMS = ABSTRACT visual language
  → Maps = physical space. Charts = quantities. 
  → Diagrams = CONCEPTUAL space (relationships, flows, hierarchies)
  → Đây là cái game dev dùng HÀNG NGÀY mà có thể không nhận ra = "visual language"
```

### §2.4 — Technical Drawings (Bản vẽ kỹ thuật) — encode PRECISE PHYSICAL FORM

```
MỤC ĐÍCH: Biểu diễn HÌNH DẠNG VẬT THỂ chính xác để SẢN XUẤT

  Engineering drawing: kích thước chính xác ±0.01mm
  Architectural blueprint: tỉ lệ 1:100, mặt bằng + mặt cắt + mặt đứng
  Circuit diagram: linh kiện điện tử + kết nối
  3D CAD: mô hình 3 chiều quay được

⭐ PRECISION LEVEL:
  → Text: "cái hộp khoảng 10cm" (mơ hồ)
  → Math: l = 10.00 ± 0.05 cm (chính xác nhưng không thấy hình)
  → Drawing: [hình hộp với kích thước ghi trên mỗi cạnh] (vừa thấy vừa chính xác)
  → 3D CAD: xoay, cắt, zoom, measure bất kỳ điểm nào

→ Technical drawing = HYBRID: visual form + mathematical precision
→ Đây là visual system CHÍNH XÁC NHẤT — dùng để sản xuất thực tế
```

### §2.5 — Icons & Emoji — encode CONCEPT COMPRESSION

```
MỤC ĐÍCH: Nén 1 concept phức tạp thành 1 hình đơn giản

ICON (thiết kế cho rõ ràng):
  🏠 Home       = trang chủ, nhà (metaphor: "về nhà" = "về trang chính")
  ⚙️ Settings   = cài đặt (metaphor: gear = machinery = adjust)
  🔍 Search     = tìm kiếm (metaphor: kính lúp = tìm)
  ❌ Close      = đóng, hủy
  ✅ Confirm    = xác nhận, đồng ý
  ⚠️ Warning    = cảnh báo
  🔔 Notification = thông báo (metaphor: chuông = alert)
  ♻️ Refresh    = làm mới

EMOJI (thiết kế cho cảm xúc):
  😀 Happy     😢 Sad      😡 Angry    🤔 Thinking
  ❤️ Love      👍 Good     🎉 Celebrate 🔥 Hot/trending

⭐ ICON/EMOJI = COMPRESSED CHUNKS
  → 1 icon = 1 concept nén thành ~100 pixels
  → Không cần đọc text, nhìn = hiểu INSTANT
  → Cross-language: 🏠 hiểu giống nhau ở mọi nước (hầu hết)
  → Game dev: toàn bộ UI = icons + minimal text

  Speed comparison:
  Text:  "Click here to go back to the home page"  (đọc ~2 giây)
  Icon:  🏠 (nhìn ~0.1 giây)
  → 20x nhanh hơn cho concept quen thuộc!
  → NHƯNG: icon chỉ cho concept ĐÃ BIẾT. Concept MỚI vẫn cần text.
```

### §2.6 — Infographic — HYBRID: visual + text + data

```
INFOGRAPHIC = kết hợp TẤT CẢ visual elements:
  → Icons + Charts + Text + Colors + Layout + Numbers
  → Mục đích: truyền tải complex information NHANH + HẤP DẪN

Cấu trúc infographic tốt:
  1. Title (text) — nói về cái gì
  2. Key number (math) — fact nổi bật nhất
  3. Chart (visual) — trend/comparison
  4. Icons (visual) — category markers
  5. Color scheme — emotional tone + categorization
  6. Flow (layout) — reading order

→ Infographic = "meta-format" kết hợp mọi format
→ Giống: bài văn (text) + bảng số (math) + hình minh họa (visual) + layout
→ Modern communication trend: infographic thay thế pure text report
```

---

## §3 — Hierarchy: Element → Group → Composition → System

```
LEVEL 1 — ELEMENT (Phần tử) = "Từ"
  1 point, 1 line, 1 shape, 1 icon, 1 color block
  → Atom nhỏ nhất có ý nghĩa

LEVEL 2 — GROUP (Nhóm) = "Cụm từ"
  Cluster of elements: [icon + label], [bar + value], [node + connections]
  → Gestalt grouping: proximity + similarity

LEVEL 3 — COMPOSITION (Bố cục) = "Câu" / "Đoạn"
  Complete chart, complete diagram, complete map section
  → Truyền tải 1 ý chính: "sales tăng", "flow đi từ A→B→C"

LEVEL 4 — LAYOUT (Trang) = "Bài văn"
  Full page/screen: multiple compositions arranged
  → Dashboard, infographic, presentation slide, game UI screen

LEVEL 5 — SYSTEM (Hệ thống) = "Cuốn sách"
  Design system: consistent icons + colors + typography + layouts
  → Brand identity, game art style guide, UI kit

MAPPING VÀO FRAMEWORK:
  Level 1 Element      ↔ Chunk (atom)
  Level 2 Group        ↔ Chunk compound
  Level 3 Composition  ↔ Schema (has purpose)
  Level 4 Layout       ↔ Plan (organized for goal)
  Level 5 System       ↔ Domain knowledge (full consistent system)
```

---

## §4 — So sánh: Visual vs Text vs Math vs Music

| Đặc điểm | Natural Language | Math | Music | Visual/Diagram |
|---|---|---|---|---|
| **Encode chính** | Meaning | Quantity | Emotion × Time | ⭐ Spatial Relationships |
| **Processing** | Sequential (đọc từng chữ) | Sequential (tính từng bước) | Temporal (nghe theo thời gian) | ⭐ SIMULTANEOUS (nhìn cả 1 lúc) |
| **"1,000 words"** | 1,000 words = 1,000 words | 1 equation = ~10 words | 1 song = ~500 words? | ⭐ 1 image = 1,000 words |
| **Spatial info** | Kém (phải mô tả tuần tự) | Kém (chỉ coordinates) | Không | ⭐ TRỰC TIẾP |
| **Temporal info** | Trung (tường thuật) | Trung (equations) | ⭐ TRỰC TIẾP | Kém (phải animate) |
| **Precision** | Thấp | ⭐ Cực cao | Cao (pitch) | Trung-Cao |
| **Emotional** | Trung (từ ngữ) | Không | ⭐ TRỰC TIẾP | Trung (color, composition) |
| **Accessibility** | Cần biết ngôn ngữ | Cần training | Universal (nghe) | ⭐ Mostly universal |
| **Ambiguity** | Cao | Không | Trung | Trung (interpretive) |
| **Information density** | Thấp (1 word = 1 concept) | Cao (1 symbol = 1 operation) | Trung | ⭐ Rất cao (spatial packing) |

```
ĐIỂM ĐỘC ĐÁO CỦA VISUAL:

1. ⭐ SIMULTANEOUS PROCESSING (nhìn cùng lúc):
   → Text: phải đọc TUẦN TỰ, từ → câu → đoạn → hiểu
   → Visual: nhìn 1 LẦN → OVERVIEW INSTANT → rồi zoom in detail
   → Đây là "1 hình = 1,000 chữ" — bạn CẦN 1,000 từ text
     để MÔ TẢ cái mà 1 diagram SHOW trong 1 giây nhìn

2. ⭐ SPATIAL ENCODING DIRECT:
   → Text: "A ở bên trái B, C ở phía trên B" → reader phải IMAGINE
   → Visual: [A][B]    → reader NHÌN THẤY LUÔN, không cần imagine
              [C]
   → Spatial information → visual = ZERO DECODE overhead

3. ⭐ PATTERN RECOGNITION leverage:
   → Con người visual cortex = CỰC MẠNH (chiếm ~30% cortex!)
   → Nhìn chart → THẤY trend INSTANT (line goes up = tăng)
   → Đọc numbers → phải TÍNH TOÁN mới thấy trend
   → Visual leverages hardware visual cortex → fast pattern match

4. ⭐ MULTI-DIMENSIONAL:
   → Text: 1D (sequential string)
   → Math: 1D (sequential expression) with 2D notation
   → Music: 2D (pitch × time)
   → Visual: 2D native + depth/color/size = effectively 4-5D
   → Encode NHIỀU dimension hơn bất kỳ format nào khác
```

---

## §5 — Visual encode gì mà format khác KHÔNG encode được

### §5.1 — Topology (cấu trúc kết nối)

```
Text: "A kết nối B, B kết nối C và D, D kết nối A"
      → Phải đọc → imagine → reconstruct → thấy rằng A-B-C-D forms cycle

Visual:
  [A] ←→ [B]
   ↕       ↕
  [D] ←→ [C]
      → Nhìn = THẤY NGAY: cycle, 4 nodes, fully connected

→ Topology (ai nối ai, cấu trúc thế nào) = NATIVE cho visual
→ Game dev: node graph, shader graph, behavior tree = VISUAL tốt hơn text
```

### §5.2 — Proportions & Comparisons (Tỉ lệ và so sánh)

```
Text: "Công ty A doanh thu 50 tỷ, B 30 tỷ, C 15 tỷ, D 5 tỷ"
Math: A=50, B=30, C=15, D=5 (tỉ lệ 10:6:3:1)

Visual (bar chart):
  A: ██████████████████████████████████████████████████  50
  B: ██████████████████████████████                      30
  C: ███████████████                                     15
  D: █████                                                5

→ NHÌN = THẤY NGAY tỉ lệ: A > B > C > D, A gấp đôi B
→ Đọc số: phải TÍNH mới thấy tỉ lệ
→ Visual: tỉ lệ → perception INSTANT (size comparison = pre-attentive)
```

### §5.3 — Process flow (Luồng xử lý)

```
Text: "User đăng nhập. Nếu đúng password, vào dashboard. 
       Nếu sai, hiện lỗi. Nếu sai 3 lần, khóa tài khoản."

Visual (flowchart):
  [Login] → <Password OK?> ──Yes──→ [Dashboard]
                |
               No
                ↓
           <3 fails?> ──Yes──→ [Lock Account]
                |
               No
                ↓
           [Show Error] → [Login]

→ Visual: THẤY NGAY mọi path, mọi decision, mọi loop
→ Text: phải đọc tuần tự, dễ MISS edge case
→ Đây là lý do game dev dùng flowchart/state diagram cho game logic
```

---

## §6 — Lịch sử phát triển

```
~40,000 TCN   Cave paintings (Lascaux, Altamira) — hình vẽ trên vách hang
               → Visual communication CỔ NHẤT còn sót lại
               → Vẽ bò, ngựa, tay — có thể là ritual, teaching, storytelling
~3,200 TCN    Egyptian hieroglyphs — icon-based writing (hình vẽ = chữ)
               → RANH GIỚI giữa "visual" và "writing" — hieroglyph = cả 2
~2,500 TCN    Babylon: bản đồ đất sét — earliest known maps
~300 TCN      Euclid: geometric diagrams kèm proof — VISUAL + MATH kết hợp
~1400s        Leonardo da Vinci: technical drawings — anatomy, machines, architecture
               → Visual precision for SCIENCE + ENGINEERING
~1600s        Cartography boom: accurate world maps (Mercator 1569)
~1786         William Playfair: PHÁT MINH bar chart, line chart, pie chart
               → TRƯỚC 1786: dữ liệu SỐ chỉ có TABLE (bảng số)
               → SAU 1786: dữ liệu số VISUAL HÓA → revolution in data communication
               → ⭐ Statistical chart chỉ mới ~240 năm!
~1850s        Florence Nightingale: polar area chart → convinced government
               → Dùng VISUAL để thuyết phục chính sách y tế
~1933         Harry Beck: London Underground map — topology not geography
               → ⭐ INSIGHT: map KHÔNG CẦN chính xác địa lý — chỉ cần TOPOLOGY
               → Ảnh hưởng mọi transit map trên thế giới sau này
~1972         Xerox PARC: GUI (Graphical User Interface) — desktop metaphor
               → ⭐ Computer chuyển từ TEXT (command line) → VISUAL (icons, windows)
~1990s        World Wide Web: visual layout (HTML + CSS) for information
~2000s        Data visualization boom: D3.js, Tableau, infographics
~2010s        Emoji standardization (Unicode) — visual language GLOBAL
~2020s        AI image generation (DALL-E, Midjourney, Stable Diffusion)

⭐ INSIGHT:
  1. Cave painting (~40,000 năm) CỔ HƠN writing (~5,000 năm) rất nhiều
     → Visual communication = NATURAL cho human brain
     → Text = INVENTED technology (sau này)
  2. Statistical chart chỉ mới ~240 năm (Playfair 1786)
     → TRƯỚC ĐÓ: mọi data = bảng số hoặc text mô tả
     → SAU ĐÓ: revolution — "seeing" data thay vì "reading" data
  3. GUI chỉ mới ~50 năm (Xerox 1972)
     → TRƯỚC ĐÓ: computer = text only (command line)
     → SAU ĐÓ: ai cũng dùng computer được (visual = accessible)
  4. Emoji ~15 năm (Unicode 2010)
     → Visual MICRO-language global — 😀 hiểu giống nhau khắp thế giới
```

---

## §7 — Framework lens + Câu hỏi mở

### §7.1 — Visual trong Processing Layers model

```
L0 (Body Input):    Nhìn hình ảnh (visual experience modality) 
L1 (Pattern Match): Nhận ra pattern (trend, cluster, outlier, shape)
                    → ⭐ Visual cortex = 30% cortex → pattern match CỰC MẠNH
L2 (Encoding):      Visual format (chart, diagram, map, icon)
L3 (Processing):    Analyze relationships, compare, trace flow
L4 (Plan/Execute):  Design, draw, create visualization

⭐ Visual VIEWER experience:
  L0 → L1 (instant pattern match) → understanding
  → L1 DOMINATES: nhìn chart → thấy trend NGAY → ít cần L3
  → Đây là strength: bypass L3 conscious processing → go straight to insight
  → Giống music listener: L0 → L1 → emotion (bypass L2+L3)

⭐ Visual CREATOR experience:
  L3 (what to communicate) → L2 (choose visual format) → L4 (design + create)
  → HEAVY L3 + L4: designing good visualization = hard
  → "Easy to read, hard to create" = asymmetry
  → Giống: writing a good book is hard, reading it is easy
```

### §7.2 — Câu hỏi mở

1. **"1 hình = 1,000 chữ" nhưng CHỈ cho spatial/quantitative info.** Thử encode "tôi yêu bạn nhưng không biết nói thế nào" bằng visual → KHÔNG THỂ (emotional complexity). Music có thể gần hơn. Text vẫn tốt nhất cho nuanced emotion + narrative.

2. **Game UI = visual language applied.** Game dev thiết kế UI = thiết kế VISUAL COMMUNICATION SYSTEM riêng cho game đó. Health bar = chart. Minimap = map. Inventory icons = icon system. Skill tree = diagram. → Game UI = micro visual language per game.

3. **Information overload**: khi visual có QUÁ NHIỀU elements → WORSE than text (cluttered chart, over-designed infographic). → Visual optimal cho ~5-20 elements. Beyond that → need hierarchy, filtering, interaction.

4. **Visual + AI**: DALL-E/Midjourney generate images từ TEXT prompt. = Text→Visual translation. Ngược: image captioning = Visual→Text. Tương lai: seamless bidirectional translation giữa formats?

5. **Why do developers love diagrams?** Code = text. Nhưng developers vẽ diagrams (whiteboard, architecture diagrams) khi THIẾT KẾ. Vì: design = SPATIAL RELATIONSHIP between components. Text (code) = SEQUENTIAL instructions. Design needs overview → visual. Implementation needs sequence → text.

### §7.3 — References

| Tác giả | Năm | Công trình | Liên quan |
|---|---|---|---|
| Tufte, E. | 1983 | The Visual Display of Quantitative Information | Data visualization principles |
| Bertin, J. | 1967 | Semiology of Graphics | Visual encoding theory |
| Wertheimer, M. | 1923 | Gestalt principles | Visual perception laws |
| Playfair, W. | 1786 | The Commercial and Political Atlas | Invented statistical charts |
| Norman, D. | 1988 | The Design of Everyday Things | Visual affordance design |
| Cairo, A. | 2012 | The Functional Art | Infographic design |
| Few, S. | 2004 | Show Me the Numbers | Effective data visualization |

---

> **04-Visual-Diagram-Architecture.md — End of file.**
>
> Visual = communication format encode spatial relationships + simultaneous overview. Unique: INSTANT pattern recognition leveraging 30% visual cortex. Game dev uses daily: UI, maps, diagrams, charts.
>
> Phiên bản: v1.0, 2026-04-16.
