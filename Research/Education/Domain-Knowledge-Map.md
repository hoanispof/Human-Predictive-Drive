---
title: Domain-Knowledge-Map — Bản Đồ Nhóm Kiến Thức v7.8
version: 1.0
created: 2026-04-21
status: v1.0
scope: |
  WHAT nhóm kiến thức/kỹ năng cần cho thời đại hiện đại.
  Bản đồ domain — KHÔNG liệt kê hết, chỉ nhóm baseline.
  Update khi era đổi (thêm/bớt nhóm), CẤU TRÚC giữ nguyên.
purpose: |
  File NÀY = BẢN ĐỒ NHÓM — không phải danh sách môn học.
  Mỗi nhóm = 1 "cây" — gốc ai cũng cần, nhánh vô tận.
  AI + Education-Mechanism (HOW) + file này (WHAT)
  → generate arc cho BẤT KỲ topic, BẤT KỲ level, BẤT KỲ student.
position: |
  Research/Education/ — TẦNG 3 trong kiến trúc.
  Bộ 2 files: Education-Mechanism (HOW) + Domain-Knowledge-Map (WHAT — file này).
dependencies:
  - Education-Mechanism.md — HOW learning arc design (bộ đôi)
  - Child-Development-Mechanism.md — developmental timeline, sensitive periods
  - Skill-Introduction.md — 0-6 skill exposure timing
  - Chunk.md v2.0 — prerequisite chains, chunk hierarchy
  - Imagine-Final.md — purpose engine, lifecycle
  - Core-v7.8-Draft.md — cycle architecture
language: Tiếng Việt primary + English technical terms
confidence: 🟢 Research support | 🟡 Framework synthesis | 🔴 Era prediction
durability: |
  §1 Foundation Domains = DURABLE (decades — brain-based)
  §2 Era-Specific = TIME-BOUND (update 3-5 năm khi era đổi)
  §3 Per-Hardware = STABLE principle (emerge per individual)
---

# Domain-Knowledge-Map — Bản Đồ Nhóm Kiến Thức v7.8

> **Kiến thức là VÔ TẬN. Cách dạy là VÔ TẬN. Cách học là VÔ TẬN.**
>
> File này KHÔNG liệt kê hết — và KHÔNG NÊN liệt kê hết.
>
> File này là BẢN ĐỒ: nhóm nào AI CẦN BIẾT TỒN TẠI,
> nhóm nào là nền tảng cross-era, nhóm nào era-dependent.
>
> Mỗi nhóm = 1 CÂY:
>   Gốc = ai cũng cần (foundation chunks)
>   Thân = everyone builds to some depth
>   Nhánh = per-interest, per-hardware, per-era
>   Lá = vô tận, luôn mọc thêm, luôn thay đổi
>
> AI + Education-Mechanism.md (HOW) + file này (WHAT)
> → generate arc cho BẤT KỲ lá nào trên BẤT KỲ cây nào.
>
> **"Bản đồ giúp biết CÂY NÀO ở ĐÂU — không phải đếm từng chiếc lá."**

---

## Mục lục

- §0 — VỊ TRÍ VÀ CÁCH ĐỌC
- §1 — FOUNDATION DOMAINS (cross-era, mọi người cần)
- §2 — ERA-SPECIFIC DOMAINS (2025+, time-bound)
- §3 — PER-HARDWARE DOMAINS (emerge per individual)
- §4 — TIMING + PREREQUISITE LOGIC
- §5 — HONEST ASSESSMENT
- §6 — CROSS-REFERENCES

---

## §0 — VỊ TRÍ VÀ CÁCH ĐỌC

### §0.1 — Bộ đôi: HOW + WHAT

```
2 FILES EDUCATION — ĐỌC CÙNG NHAU:

  Education-Mechanism.md = HOW
    → 8 nguyên lý brain-based cho arc design
    → Direction > Level, cost formula, prerequisite, mini-arcs,
      Imagine-Final, feedback, consolidation, depth
    → Valid MỌI era, MỌI domain

  Domain-Knowledge-Map.md = WHAT (file này)
    → Nhóm kiến thức/kỹ năng cần trong era hiện đại
    → Foundation (cross-era) + Era-specific (2025+) + Per-hardware
    → Update §2 khi era đổi, §1 + §3 giữ nguyên


  AI SỬ DỤNG CẢ HAI:

    ① AI nhận topic từ teacher/parent/student
    ② AI check: topic thuộc NHÓM NÀO? (file này)
       → Foundation? Era-specific? Per-hardware?
    ③ AI check prerequisite: student đã có chunks nền chưa? (§4)
    ④ AI apply mechanism principles (Education-Mechanism §2)
       → Design arc phù hợp per student
    ⑤ Teacher calibrate + Student verify

    = 2 files + AI = generate arc cho BẤT KỲ lá nào trên BẤT KỲ cây nào
```

### §0.2 — 3-Tier Taxonomy

```
3 TẦNG — từ durable đến flexible:

  ┌──────────────────────────────────────────────────────────────┐
  │ TIER 1: FOUNDATION DOMAINS (§1)                              │
  │   Cross-era, mọi hardware cần, DURABLE (decades)            │
  │   = "Bất kỳ era nào, bất kỳ ai, đều CẦN gốc này"          │
  │   → 6 nhóm: Literacy, Numeracy, Somatic, Social,            │
  │     Creative, Meta-learning                                  │
  ├──────────────────────────────────────────────────────────────┤
  │ TIER 2: ERA-SPECIFIC DOMAINS (§2)                            │
  │   2025+ specific, TIME-BOUND (update khi era đổi)            │
  │   = "Era NÀY cần THÊM — era sau CÓ THỂ khác"              │
  │   → 6 nhóm: AI Literacy, Information Curation,              │
  │     Systems Thinking, Basic Science, Cross-cultural,         │
  │     Digital Wellbeing                                        │
  ├──────────────────────────────────────────────────────────────┤
  │ TIER 3: PER-HARDWARE DOMAINS (§3)                            │
  │   Emerge per individual, KHÔNG plan trước                    │
  │   = "NGƯỜI NÀY mạnh CÁI GÌ → đi sâu CÁI ĐÓ"             │
  │   → Vô tận — observe + support                              │
  └──────────────────────────────────────────────────────────────┘

  NGUYÊN TẮC CHUNG:
    → Foundation TRƯỚC, specialization SAU
      (Education-Mechanism §2.4 — prerequisite check)
    → Tier 1 rộng → Tier 2 thêm → Tier 3 sâu
    → Mỗi domain = "CÂY" — gốc+thân = file này, nhánh+lá = vô tận
```

### §0.3 — Scope

```
FILE NÀY LÀM:
  ✓ Liệt kê SƠ LƯỢC nhóm kiến thức (baseline, không exhaustive)
  ✓ Per nhóm: WHY foundation + prerequisite logic + timing hint
  ✓ Phân biệt rõ: cross-era vs era-specific vs per-individual
  ✓ Cung cấp "bản đồ" cho AI navigate domain landscape

FILE NÀY KHÔNG LÀM:
  ✗ Không liệt kê exhaustive (kiến thức = vô tận)
  ✗ Không prescribe cách dạy (→ Education-Mechanism.md)
  ✗ Không cho per-age sequencing tables (AI calibrate per student)
  ✗ Không là curriculum — là DOMAIN MAP cho AI engine

⚠️ §2 CÓ HẠN SỬ DỤNG — update khi era đổi
```

---

## §1 — FOUNDATION DOMAINS (cross-era, mọi người cần)

> **6 nhóm gốc. Bất kỳ era nào, bất kỳ ai, bất kỳ hardware nào — đều CẦN.**
> **100 năm trước cần. 100 năm sau vẫn cần. Vì não cần.**

### §1.1 — Literacy / Communication

```
🟢 NGÔN NGỮ + GIAO TIẾP:

  CÂY:
    Gốc  → Đọc, viết, nói, nghe (decode + encode)
    Thân → Biểu đạt ý tưởng, lập luận, thuyết phục
    Nhánh → Literature, journalism, public speaking, poetry,
            academic writing, storytelling, debate, translation...
    Lá   → Vô tận — mỗi domain có ngôn ngữ riêng

  TẠI SAO FOUNDATION:
    → Mọi domain khác CẦN literacy để ACCESS
    → Không đọc được → không learn được (mọi era)
    → Dù AI đọc/viết hộ → "HIỂU ý nghĩa" = human skill
    → Language processing = core brain function 🟢

  PREREQUISITE:
    → Foundation chunks từ 0-6 (Child-Dev: language exposure)
    → Phonemic awareness → decoding → fluency → comprehension → expression
    → = Prerequisite chain DÀI NHẤT và SỚM NHẤT

  TIMING:
    → Bắt đầu sớm nhất (sensitive period 0-6 cho language)
    → Continues lifelong — depth luôn có thể tăng
    → AI era: literacy KHÔNG giảm giá trị — thay đổi FORMAT
      (typing vs writing, prompting vs commanding)
```

### §1.2 — Numeracy / Logic

```
🟢 TOÁN + LOGIC + PATTERN RECOGNITION:

  CÂY:
    Gốc  → Đếm, cộng trừ nhân chia, so sánh, đo lường
    Thân → Logic reasoning, pattern recognition, problem-solving
    Nhánh → Algebra, geometry, statistics, probability,
            programming logic, data analysis, financial literacy...
    Lá   → Vô tận — toán ứng dụng mọi nơi

  TẠI SAO FOUNDATION:
    → Logical thinking = SUBSTRATE cho mọi analysis
    → Pattern recognition = cách não HIỂU thế giới 🟢
    → Dù AI tính hộ → "HIỂU logic" ≠ "nhấn nút"
    → Số học cơ bản = prerequisite cho science, technology, economics

  PREREQUISITE:
    → Concrete → abstract (PFC development timeline)
    → Đếm → phép tính → logic → abstract reasoning
    → ⚠️ Abstract math quá sớm (PFC chưa đủ) = avoidance tag phổ biến
      → Nhiều "ghét toán" = wrong timing, KHÔNG phải khả năng kém

  TIMING:
    → Concrete math: sớm (3-6, qua trải nghiệm vật lý)
    → Abstract math: sau khi PFC đủ (~10-12+)
    → AI era: "biết hỏi đúng câu toán" > "tính nhanh"
```

### §1.3 — Somatic / Physical

```
🟢 VẬN ĐỘNG + CƠ THỂ + INTEROCEPTION:

  CÂY:
    Gốc  → Coordination, balance, gross motor, fine motor
    Thân → Body awareness, health habits, hands-on skills
    Nhánh → Sports, dance, martial arts, craft, surgery,
            cooking, gardening, instrument playing...
    Lá   → Vô tận — body = processing channel cho mọi skill

  TẠI SAO FOUNDATION:
    → Body-base = processing channel (Child-Dev-Mechanism §2, Education-Mechanism §2.2)
    → Physical health = prerequisite cho brain function
    → Multi-modal compile MẠNH hơn verbal-only 🟢
    → Hands-on experience = kênh ③ compile (multi-modal binding)
    → Interoception = body-listening → foundation cho self-awareness

  PREREQUISITE:
    → Gross motor → fine motor → complex coordination → skill mastery
    → Body awareness → interoception → self-regulation
    → = Prerequisite chain CHO CHÍNH NÓ + cho Social/Emotional domain

  TIMING:
    → Bắt đầu sớm nhất (motor sensitive periods 0-6)
    → ⚠️ Trend giảm thể dục = NGUY HIỂM cho brain development
    → ≠ "Giờ thể dục" → = body AS learning channel trong MỌI domain
    → AI era: body skills = human differentiator MẠNH NHẤT
      (AI không có body → body skills = irreplaceable)
```

### §1.4 — Social / Emotional

```
🟢 XÃ HỘI + CẢM XÚC + COLLABORATION:

  CÂY:
    Gốc  → Empathy cơ bản, cooperation, emotion recognition
    Thân → Emotion regulation, conflict resolution, communication
    Nhánh → Leadership, negotiation, mentoring, therapy,
            teamwork, teaching, parenting, diplomacy...
    Lá   → Vô tận — human connection = core of civilization

  TẠI SAO FOUNDATION:
    → Human = social animal → social skills = survival MỌI era 🟢
    → Empathy = Self-Pattern-Match function (Empathy.md) — cần chunks đủ
    → Emotion regulation = cortisol management (Cortisol-Baseline.md v2.0)
    → AI era: human connection = DIFFERENTIATOR
      (AI collaborate tốt nhưng không thay thế human-human connection)

  PREREQUISITE:
    → Attachment chunks từ 0-3 (Mother-Opt, Natural-Dev)
    → Emotion recognition → regulation → social skills → complex relations
    → SPM bootstrap: cần self-chunks ĐỦ trước khi empathize
      (Child-Dev-Mechanism §6)

  TIMING:
    → Attachment: 0-3 (sensitive period QUAN TRỌNG NHẤT)
    → Basic social: 3-6 qua play (Natural-Dev)
    → Complex social: 6-12+ (school environment)
    → ⚠️ Post-COVID: social skill decline observed → CẦN TĂNG, không giảm
```

### §1.5 — Creative / Expressive

```
🟡 SÁNG TẠO + BIỂU ĐẠT + AESTHETIC:

  CÂY:
    Gốc  → Explore, experiment, express freely
    Thân → Develop aesthetic sense, personal style, create novel combinations
    Nhánh → Visual art, music, writing, design, architecture,
            film, photography, fashion, game design...
    Lá   → Vô tận — creativity = infinite domain

  TẠI SAO FOUNDATION:
    → Creativity = novel chunk combinations → human differentiator vs AI
    → Channel cho Imagine-Final emerge
      (Education-Mechanism §2.6 — purpose engine cần có gì để imagine)
    → Window cho hardware tendencies lộ qua expression
      → Somatic-dominant express qua movement, visual-dominant qua drawing
    → Approach-tagged creative experience → lifelong creative identity

  PREREQUISITE:
    → Exposure rộng TRƯỚC (0-6: Natural-Dev, Skill-Intro)
    → Safe environment (no shame for "weird" expression)
    → → Creative compile CẦN novelty-direction (Education-Mechanism §2.2)
    → → Ép sáng tạo (threat-direction) = paradox → kill creativity

  TIMING:
    → Bắt đầu sớm — explore + express từ 2-3 tuổi
    → ⚠️ Trend "nghệ thuật = không thực tế" → NGƯỢC LẠI:
      AI era = creativity CẦN HƠN (AI replicate cái cũ, human tạo cái mới)
    → Style emerge Stage 3 (12-18), voice mature Stage 4 (18+)

  🟡 Creativity as foundation domain = framework position
     Debatable — some frameworks put it under "skills" not "domain"
     Framework argument: creativity cần PRACTICE domain riêng, không tự emerge
```

### §1.6 — Meta-learning

```
🟡 HỌC CÁCH HỌC:

  CÂY:
    Gốc  → Self-awareness ("cái này khó/dễ với tôi")
    Thân → Learning strategies, self-assessment, error analysis
    Nhánh → Research methodology, critical thinking, self-directed learning,
            knowledge management, transfer across domains...
    Lá   → Vô tận — meta-learning = engine cho ALL other domains

  TẠI SAO FOUNDATION:
    → Era speed → specific knowledge obsolete nhanh
    → Meta-learning = "kỹ năng TỰ LEARN bất kỳ cái mới"
    → = Adaptability > specific knowledge (Education-Mechanism §0.3)
    → Meta-learning chunks = chunks VỀ CÁCH compile chunks
      → Người có meta-chunks → era đổi → TỰ compile chunks mới
      → Người thiếu → era đổi → stuck

  PREREQUISITE:
    → PFC cần đủ cho meta-cognition (~10-12+ cho explicit meta-learning)
    → Foundation domains khác = "vehicle" cho meta-learning emerge
      (trong khi học toán → cũng đang học CÁCH HỌC toán)
    → = Meta-learning KHÔNG dạy riêng → EMERGE song song với domain learning

  TIMING:
    → Seeds: 6-8 (implicit — "cái này khó/dễ với tôi")
    → Explicit: 10-12+ (PFC đủ cho reflection)
    → Self-directed: 15-18+ (PFC ~70-90%)
    → Lifelong: domain DUY NHẤT tiếp tục phát triển suốt đời
    → = Meta-learning BẮT ĐẦU CHẬM NHẤT nhưng KÉO DÀI NHẤT

  🟡 Meta-learning as foundation = framework emphasis
  🟢 "Learning to learn" validated: Hattie 2009, OECD Learning Compass 2030
```

### §1.7 — Tổng hợp Foundation

```
  ┌──────────────────┬──────────────────────────────────────────────┐
  │ Domain           │ Tại sao Foundation (1 dòng)                  │
  ├──────────────────┼──────────────────────────────────────────────┤
  │ ① Literacy       │ Mọi domain khác CẦN literacy để ACCESS      │
  │ ② Numeracy       │ Logic thinking = substrate cho mọi analysis │
  │ ③ Somatic        │ Body = processing channel, không chỉ "sức   │
  │                  │ khỏe" → brain development channel            │
  │ ④ Social         │ Human = social animal, connection =          │
  │                  │ survival mọi era + AI differentiator         │
  │ ⑤ Creative       │ Novel combinations = human differentiator    │
  │                  │ vs AI + Imagine-Final emerge channel          │
  │ ⑥ Meta-learning  │ "Học cách học" = adaptability engine.        │
  │                  │ Era đổi → tự compile chunks mới              │
  └──────────────────┴──────────────────────────────────────────────┘

  MỖI DOMAIN = 1 CÂY:
    → Gốc: ai cũng cần (foundation chunks)
    → Thân: everyone builds to some depth
    → Nhánh: per-interest, per-hardware → vô tận
    → AI navigate cây nào, nhánh nào → per student

  NGUYÊN TẮC:
    → Foundation RỘNG trước, specialization SÂU sau
    → 6 gốc ĐỒNG ĐỀU → hardware tendencies lộ → direction emerge
    → Mỗi domain = vehicle cho meta-learning song song
    → CÁCH ĐẠT depth = KHÁC per hardware (AI + Mechanism handle)
    → "Biết đọc, biết tính, biết giao tiếp, biết cảm nhận,
       biết sáng tạo, biết TỰ HỌC" = UNIVERSAL targets

  🟡 6-domain foundation = framework synthesis
  🟢 Literacy + Numeracy + Social = well-established in education research
  🟢 UNESCO 4 Pillars (1996): Know, Do, Live Together, Be
  🟢 OECD Learning Compass 2030: Knowledge, Skills, Attitudes, Values
```

---

## §2 — ERA-SPECIFIC DOMAINS (2025+, time-bound)

> **⚠️ SECTION NÀY CÓ HẠN SỬ DỤNG.**
> **Nội dung valid cho era 2025+. Update khi era đổi.**
> **Foundation (§1) giữ nguyên. Section này = biến số.**

### §2.1 — AI Literacy

```
🔴 ERA-BOUND — update khi AI capabilities đổi

  CÂY:
    Gốc  → AI tồn tại, AI có thể sai, AI = tool
    Thân → Dùng AI hiệu quả, đánh giá output, biết giới hạn
    Nhánh → AI trong từng nghề (medicine, law, engineering, art...),
            prompt engineering, AI ethics, AI development...
    Lá   → Thay đổi NHANH NHẤT trong tất cả domains

  TẠI SAO ERA-SPECIFIC (2025+):
    → AI tools thay đổi mọi cách con người access + process knowledge
    → "Biết hỏi đúng" > "biết đáp án" (Era-Analysis-2025.md)
    → Human-AI collaboration = skill MỚI chưa từng tồn tại
    → ⚠️ DẠY PRINCIPLES of AI, không phải specific tools
      (tools đổi nhanh, principles ổn định hơn)

  PREREQUISITE:
    → Literacy (đọc AI output), Numeracy (basic logic),
      Meta-learning (evaluate AI vs own understanding)
    → = AI Literacy BUILD TRÊN foundation — không thay thế foundation

  LƯU Ý:
    → "AI Literacy" của 2025 ≠ của 2030 ≠ của 2035
    → Teach: principles (AI = pattern matcher, AI có thể sai,
      AI amplify human, AI không thay thế judgment)
    → Teach: CÁCH ĐÁNH GIÁ, không phải CÁI CỤ THỂ

  🔴 Era prediction — sẽ cần update
```

### §2.2 — Information Curation

```
🟡 ERA-ENHANCED — đã luôn cần nhưng era này CẤP BÁCH hơn

  CÂY:
    Gốc  → "Không phải mọi thứ đều đúng" + source evaluation cơ bản
    Thân → Synthesize từ nhiều sources, evaluate methodology, detect bias
    Nhánh → Research methodology, fact-checking, academic evaluation,
            media literacy, data journalism...
    Lá   → Vô tận — mỗi domain có curation riêng

  TẠI SAO ERA-SPECIFIC (2025+):
    → Information UNLIMITED → curation = survival skill
    → AI generate content → harder to evaluate authenticity
    → "Biết lọc + tổng hợp" > "biết nhiều"
    → Pre-internet: scarcity of info → Post-internet: overload of info
      → = Skill set KHÁC HOÀN TOÀN

  PREREQUISITE:
    → Literacy (đọc hiểu), Numeracy (basic stats for evidence),
      Meta-learning (self-assess: "tôi biết cái gì, không biết cái gì?")

  🟡 Arguable: thời nào cũng cần evaluate info
     Nhưng SCALE đã thay đổi qualitatively → era-specific emphasis
```

### §2.3 — Systems Thinking

```
🟡 ERA-ENHANCED — luôn hữu ích nhưng era phức tạp = cấp bách

  CÂY:
    Gốc  → Cause and effect, "nếu X → thì Y"
    Thân → Feedback loops, interconnections, unintended consequences
    Nhánh → Ecology, economics, urban planning, public health,
            climate science, organizational design...
    Lá   → Vô tận — mọi hệ thống phức tạp đều cần

  TẠI SAO ERA-SPECIFIC (2025+):
    → Thế giới interconnected hơn → effects cascade
    → Global problems (climate, economy, health) = systems problems
    → AI giúp MODEL systems → nhưng cần người HIỂU systems
    → Cross-domain thinking = convergence opportunity

  PREREQUISITE:
    → Numeracy (logic, cause-effect), Literacy (articulate complex ideas)
    → Cần chunks từ NHIỀU domain → systems thinking emerge MUỘN
    → = Tier 2 domain builds TRÊN Tier 1 foundation

  🟡 Systems thinking = important mọi era
     Framework puts here vì EMPHASIS tăng do complexity era
```

### §2.4 — Basic Science Literacy

```
🟡 ARGUABLE — có thể Foundation, framework đặt ở Tier 2

  CÂY:
    Gốc  → Thế giới vật chất hoạt động thế nào (basic physics,
            chemistry, biology concepts)
    Thân → Scientific method, hypothesis-testing, evidence-based thinking
    Nhánh → Mỗi nhánh science = 1 career path (biology, physics,
            chemistry, medicine, engineering, environmental science...)
    Lá   → Vô tận — science knowledge expands daily

  TẠI SAO Ở ĐÂY (thay vì Foundation):
    → Gốc science = arguably cross-era (gravity luôn tồn tại)
    → NHƯNG: depth CẦN và CÁCH dạy science = rất era-dependent
    → Pre-industrial: science ≈ craft knowledge → informal
    → Industrial: science = formal discipline → school subject
    → AI era: science literacy = evaluate claims, understand tech
    → = Vị trí: giữa Foundation và Era-specific → framework đặt Tier 2
      với lưu ý "gốc có thể xem là foundation"

  PREREQUISITE:
    → Numeracy (math for science), Literacy (read + write science)
    → Curiosity (approach-tagged science experiences từ sớm)
    → ⚠️ "Ghét khoa học" thường = avoidance-tagged từ cách dạy sai direction

  🟡 Placement debatable — gốc science = cross-era
     Framework acknowledges: boundary Foundation vs Era-specific = fuzzy
```

### §2.5 — Cross-cultural Awareness

```
🟡 ERA-ENHANCED — connected world = cấp bách

  CÂY:
    Gốc  → "Thế giới có nhiều cách sống khác nhau → đều có giá trị"
    Thân → Cultural perspectives, collaboration across differences
    Nhánh → International business, diplomacy, translation,
            cultural studies, anthropology, global development...
    Lá   → Vô tận — mỗi cross-cultural encounter = unique

  TẠI SAO ERA-SPECIFIC (2025+):
    → Internet + travel + global work = daily cross-cultural contact
    → AI translation lowers language barrier → cultural barrier REMAINS
    → Collaboration across cultures = workplace norm, not exception

  PREREQUISITE:
    → Social/Emotional (empathy = foundation), Literacy (communicate)
    → Exposure to diversity (trải nghiệm trực tiếp > lý thuyết)

  🟡 Some level always existed (trade routes, migration)
     Era emphasis: SCALE + FREQUENCY of cross-cultural contact
```

### §2.6 — Digital Wellbeing

```
🟡 ERA-SPECIFIC — mới hoàn toàn

  CÂY:
    Gốc  → Screen awareness, online safety, "body cảm thấy thế nào
            sau khi dùng screen?"
    Thân → Attention management, social media literacy,
            information overload management
    Nhánh → Digital detox design, tech-life balance,
            professional digital boundaries, UX ethics...
    Lá   → Evolving nhanh — new platforms = new challenges

  TẠI SAO ERA-SPECIFIC (2025+):
    → Information overload = NEW cortisol source
      (Cortisol-Baseline.md v2.0 — chronic low-grade)
    → Attention hijacking = designed into platforms
    → Social comparison at scale = new peer threat source
    → = "DÙNG technology" + "QUẢN LÝ technology impact on brain"
    → Chưa từng tồn tại trước ~2010

  PREREQUISITE:
    → Somatic (body awareness — "body nói gì sau 3 giờ scroll?")
    → Meta-learning (self-assess habits)
    → Social/Emotional (recognize comparison patterns)

  🟡 Digital wellbeing = new domain, research still emerging
  🟢 Screen time effects: Twenge 2017 (correlational, debated)
  🟢 Attention economy: Wu 2016 (The Attention Merchants)
```

### §2.7 — Tổng hợp Era-Specific

```
  ┌──────────────────┬──────────────────────────────────────────────┐
  │ Domain           │ Era tại sao (1 dòng)                         │
  ├──────────────────┼──────────────────────────────────────────────┤
  │ ① AI Literacy    │ AI thay đổi mọi cách access knowledge        │
  │ ② Info Curation  │ Unlimited info → curation = survival         │
  │ ③ Systems Think  │ Interconnected world → cascade effects        │
  │ ④ Basic Science  │ Evaluate claims + understand tech (gốc =     │
  │                  │ arguably cross-era, depth = era-specific)     │
  │ ⑤ Cross-cultural │ Daily cross-cultural contact = norm           │
  │ ⑥ Digital Well.  │ Info overload + attention hijack = NEW threat │
  └──────────────────┴──────────────────────────────────────────────┘

  ⚠️ ERA-BOUND:
    → 6 domains trên = VALID cho 2025+
    → Era sau CÓ THỂ: thêm mới, bỏ bớt, reframe
    → CẤU TRÚC file giữ nguyên — content §2 update
    → VD: 2035 có thể thêm "Brain-Computer Interface Literacy"
      hoặc bỏ "Digital Wellbeing" nếu self-regulating tech emerge
    → = §2 là BIẾN SỐ, §1 và §3 là HẰNG SỐ
```

---

## §3 — PER-HARDWARE DOMAINS (emerge per individual)

```
🟡 TIER 3 — KHÔNG PLAN TRƯỚC, OBSERVE + SUPPORT:

  Mỗi người có hardware RIÊNG (gen + development + environment):
    → Somatic-dominant: body processing mạnh → sports, craft, surgery, dance
    → Verbal-dominant: language processing mạnh → literature, law, teaching
    → Visual-dominant: spatial processing mạnh → design, architecture, art
    → High-VTA: novelty-seeking cao → innovation, entrepreneurship
    → High-detail: pattern precision → research, engineering, programming
    → Social-dominant: connection drive mạnh → therapy, leadership, diplomacy
    → ... vô tận combinations

  CÂY PER-HARDWARE:
    → Gốc = Foundation (Tier 1) — EVERYONE cần
    → Thân = Foundation + Era-specific (Tier 1+2) — EVERYONE builds
    → NHÁNH = emerge từ hardware tendencies — PER INDIVIDUAL
    → Nhánh → cành → lá: đi sâu mãi trong domain phù hợp

  NGUYÊN TẮC:
    → KHÔNG prescribe: "con phải theo STEM" hay "con phải theo nghệ thuật"
    → OBSERVE: hardware tendencies lộ qua cách trẻ engage với 6 foundation domains
    → SUPPORT: khi direction emerge → provide depth opportunity
    → AI detect patterns: "student này engage mạnh với domain X" → suggest depth

  TIMING:
    → Seeds: 6-12 (expose rộng → tendencies LỘ)
    → Direction: 12-16 (tendencies rõ → begin depth)
    → Depth: 16+ (hardware-matched specialization)
    → ⚠️ Late bloomer = BÌNH THƯỜNG → không ép direction sớm
    → ⚠️ Multi-domain = BÌNH THƯỜNG → không ép chọn 1

  KẾT NỐI VỚI IMAGINE-FINAL:
    → Hardware tendencies + exposure → Imagine-Final emerge
    → Imagine-Final = navigation tool cho direction (Education-Mechanism §2.6)
    → 4 góc quality check: Sweet Spot (domain ✓ + hardware ✓) = target
    → AI + Teacher help student navigate → KHÔNG dictate direction

  🟡 Per-hardware domain emergence = framework application
  🟢 Individual differences in aptitude: well-established in differential psychology
```

---

## §4 — TIMING + PREREQUISITE LOGIC

```
🟡 KHÔNG FIXED STAGES — TÙY CHUNK TÍCH LŨY CỦA TỪNG NGƯỜI:


  PREREQUISITE LOGIC (không phải age-based):

    Tier 1 Foundation = TRƯỚC:
      → Literacy + Numeracy = prerequisite cho hầu hết Tier 2
      → Somatic + Social = prerequisite cho healthy learning process
      → Creative + Meta-learning = develop SONG SONG với domain learning

    Tier 2 Era-specific = SAU KHI CÓ FOUNDATION:
      → AI Literacy CẦN: literacy + numeracy + meta-learning chunks
      → Info Curation CẦN: literacy + numeracy + meta-learning chunks
      → Systems Thinking CẦN: numeracy + chunks từ NHIỀU domain
      → Basic Science CẦN: numeracy + literacy
      → Cross-cultural CẦN: social/emotional + literacy
      → Digital Wellbeing CẦN: somatic (body awareness) + meta-learning

    Tier 3 Per-hardware = SAU KHI TENDENCIES LỘ:
      → Foundation RỘNG → tendencies emerge → direction → depth

    → = HIERARCHY: Tier 1 → Tier 2 → Tier 3
    → NHƯNG: overlap đáng kể (Tier 2 bắt đầu khi Tier 1 CƠ BẢN đủ,
      không cần chờ Tier 1 HOÀN THÀNH)


  BALANCE TRAJECTORY (approximate):

    Tuổi 6-12: Foundation DOMINANT
      → Tier 1: ~70-80% effort → build gốc CHẮC
      → Tier 2: ~15-20% → exposure level (biết AI tồn tại, biết internet có sai)
      → Tier 3: ~5-10% → observe tendencies, cho explore

    Tuổi 12-18: TRANSITION
      → Tier 1: ~40-50% → maintain + deepen
      → Tier 2: ~25-30% → develop (AI critical use, info synthesis)
      → Tier 3: ~20-30% → begin specialization (direction emerge)

    Tuổi 18+: SPECIALIZATION
      → Tier 1: ~20-30% → maintain
      → Tier 2: ~20-25% → maintain + professional application
      → Tier 3: ~45-55% → deep (hardware-matched domain)

    ⚠️ % = APPROXIMATE → per-individual varies:
      → Early direction rõ: Tier 3 cao hơn sớm hơn
      → Late bloomer: Tier 1 extend → BÌNH THƯỜNG
      → Multi-talent: Tier 3 chia nhiều nhánh → T-shape rộng


  AI CHECK PREREQUISITE PER STUDENT:

    AI KHÔNG dùng age → dùng CHUNK STATUS:
      → Student A (10 tuổi) có literacy L3 → sẵn sàng info curation
      → Student B (10 tuổi) có literacy L1 → cần build literacy trước
      → CÙNG tuổi, KHÁC chunk status → KHÁC readiness
      → = Per-student, không per-age

  🟡 Trajectory percentages = framework estimate, not proven benchmarks
  🟢 Prerequisite learning: Gagné 1985, Ausubel 1968
```

---

## §5 — HONEST ASSESSMENT

```
⭐ CÁI FILE NÀY CÓ THỂ LÀM:

  ✅ Cung cấp BẢN ĐỒ nhóm kiến thức cho AI navigate
     → 3-tier taxonomy: Foundation / Era-specific / Per-hardware
  ✅ Per nhóm: WHY + prerequisite + timing logic
     → AI biết domain nào cần trước, domain nào build sau
  ✅ Phân biệt rõ: cross-era vs era-dependent
     → Biết cái gì giữ nguyên, cái gì update
  ✅ Kết hợp với Education-Mechanism.md
     → HOW + WHAT = AI generate arc cho bất kỳ topic


⭐ CÁI FILE NÀY KHÔNG THỂ LÀM:

  ❌ Liệt kê exhaustive — kiến thức = vô tận, listing = incomplete by design
  ❌ Prescribe cách dạy — → Education-Mechanism.md
  ❌ Cho per-student recommendations — AI + teacher calibrate
  ❌ Predict future domains chính xác — §2 = best guess, sẽ cần update


⭐ ĐỘ TIN CẬY:

  CAO:
    🟢 Foundation domains (literacy, numeracy, social) = well-established
    🟢 Prerequisite logic (Gagné, Ausubel) = replicated
    🟢 Sensitive periods (language, motor, attachment) = verified

  TRUNG BÌNH:
    🟡 6-domain taxonomy = framework synthesis (could be 5 or 7)
    🟡 "Tree" metaphor = useful but approximate
    🟡 Balance percentages = estimate, not proven

  THẤP:
    🔴 Era-specific domains (§2) = prediction, sẽ cần update
    🔴 "AI Literacy" definition = evolving rapidly
    🔴 Timing trajectories = approximate, individual variation cao


⭐ RỦI RO:

  ⚠️ FALSE COMPLETENESS:
     12 domains listed = CẢM GIÁC đầy đủ. Thực tế = INCOMPLETE by design.
     Có thể thiếu domains quan trọng chưa tồn tại hoặc chưa nhận ra.

  ⚠️ ERA BIAS:
     §2 = 2025 perspective. Biased bởi current technology + concerns.
     2030 sẽ có concerns KHÁC mà 2025 chưa biết.

  ⚠️ WESTERN/GLOBAL NORTH BIAS:
     Domain taxonomy thiên về global education discourse.
     Indigenous knowledge systems, non-Western categories = underrepresented.

  ⚠️ PLACEMENT DEBATES:
     Basic Science: Foundation hay Era-specific? (§2.4 acknowledged)
     Meta-learning: Domain hay meta-skill? (§1.6 acknowledged)
     = Boundaries = fuzzy by nature → framework makes CHOICES, not truths
```

---

## §6 — CROSS-REFERENCES

```
═══════════════════════════════════════════════════════
BỘ ĐÔI EDUCATION
═══════════════════════════════════════════════════════

→ Education-Mechanism.md — ⭐ HOW (bộ đôi)
  8 nguyên lý arc design. File NÀY cung cấp WHAT, Mechanism cung cấp HOW.
  AI dùng CẢ HAI: domain map + mechanism principles → generate arc.


═══════════════════════════════════════════════════════
NỀN TẢNG
═══════════════════════════════════════════════════════

→ Child-Development-Mechanism.md — Developmental timeline
  §2 4+1 compile (foundation cho mọi domain learning),
  §3 Approach/avoidance (direction cho mọi domain experience),
  §9 Sensitive periods + Imagine-Final emergence.

→ Skill-Introduction.md — 0-6 skill timing
  EXPOSURE trước, TRAINING sau. Foundation starts HERE.

→ Chunk.md v2.0 — Prerequisite chains
  §2 Compile, §4 Activation dynamics (prior knowledge effect).

→ Core-v7.8-Draft.md — Cycle architecture
  Chunks = sole substrate. Learning = compile new chunks.


═══════════════════════════════════════════════════════
MOTIVATION + DIRECTION
═══════════════════════════════════════════════════════

→ Imagine-Final.md — §1.5 Lifecycle
  Imagine-Final emerge từ domain EXPOSURE → direction cho Tier 3.

→ Imagine-Final-Evaluation.md — 4 góc quality
  Sweet Spot = domain fit + hardware fit → guide Tier 3 direction.

→ Domain-Mapping-Drive.md (Core-Deep-Dive/Domain/)
  WHY humans drive map domain. Reward từ PROCESS, không phải destination.

→ Anchor-Schema.md — 4 nguồn fill
  Education installs anchor, không chỉ chunks (§1 all domains contribute).


═══════════════════════════════════════════════════════
ERA CONTEXT
═══════════════════════════════════════════════════════

→ Applications/Education/backup/v1.0/Era-Analysis-2025.md
  Era context chi tiết cho §2 (AI revolution, skill shifts, uncertainties).

→ Applications/Education/backup/v1.0/Curriculum-Framework.md
  Source material cho file này (3-tier taxonomy, foundation matrix).

→ Applications/Education/backup/v1.0/Hardware-Calibration.md
  Per-hardware tendencies chi tiết cho §3.


═══════════════════════════════════════════════════════
OBSERVATION
═══════════════════════════════════════════════════════

→ Observation/Education-Arms-Race.md
  Societal pressure patterns affecting ALL domains.

→ Observation/Empathy-Education.md (cần viết mới)
  Empathy in education → Social/Emotional domain (§1.4) application.
```
