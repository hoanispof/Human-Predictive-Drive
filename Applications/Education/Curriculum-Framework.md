---
title: Curriculum Framework — Dạy Cái Gì, Khi Nào, Cho Ai v7.8
version: 2.0
created: 2026-04-03
updated: 2026-05-11
status: v2.0
scope: |
  DẠY CÁI GÌ, KHI NÀO, THEO THỨ TỰ NÀO, SÂU BAO NHIÊU.
  Knowledge domains × system stages × depth targets.
  Derived từ Domain-Knowledge-Map.md v1.0 (domain taxonomy) +
  Education-Mechanism.md v1.0 (arc design principles) +
  Education-System.md v2.0 (system stages).
purpose: |
  File NÀY = DELIVERY MATRIX — bridge giữa domain taxonomy trừu tượng
  với system design cụ thể.
  DKM = BẢN ĐỒ nhóm kiến thức (WHAT tồn tại).
  File này = WHAT × WHEN × HOW DEEP per stage.
  Education-System = HOW system vận hành.
position: |
  TẦNG 4 — Applications, DERIVED từ tất cả tầng trước.
  Trong folder: Education-System.md v2.0 (anchor) → file này (derived).
dependencies:
  - Domain-Knowledge-Map.md v1.0 — 3-tier domain taxonomy (NỀN TẢNG WHAT)
  - Education-Mechanism.md v1.0 — 8 nguyên lý arc design (NỀN TẢNG HOW)
  - Education-System.md v2.0 — system stages (NỀN TẢNG WHEN)
  - Core-Software.md v1.0 — cycle-based architecture
  - Core-Hardware.md v1.0 — 4 zones A/B/C/D
  - Child-Development-Mechanism.md v1.0 — developmental timeline
  - Cortisol-Baseline.md v2.0 — amplifier reframe
  - Imagine-Final.md — lifecycle, purpose engine
  - Agent-Mechanism.md v1.0 — SPM F1 (social processing)
  - Hardware-Calibration.md v1.0 — per-individual calibration
  - Reward-Signal-Architecture.md v1.0 — Type A/B reward
  - Body-Base.md v2.0 — Model 3+1
previous: backup/v1.0/Curriculum-Framework.md (641L, DRAFT, 2026-04-03)
changes_v2:
  - Re-base: "NL1-NL10" → Education-Mechanism.md v1.0 §2.x specific refs
  - Re-base: Education-Principles.md → Education-Mechanism.md v1.0
  - §1 Taxonomy: SLIM — reference DKM v1.0 thay vì repeat domain detail
  - §2 Matrix: depth levels aligned với chunk compilation levels (Mechanism §2.9)
  - §3 Era-specific: aligned DKM §2 (6 domains, +Basic Science Literacy)
  - §4 Sequencing: reference DKM §4 cho prerequisite logic detail
  - §5 "Cái cần bỏ": updated refs + v7.8 terminology
  - §6 Cross-refs: complete rewrite — organized per 5 tầng
  - Terminology: "mirror neurons" → SPM F1, approach/avoidance, Type A/B
language: Tiếng Việt primary + English technical terms
confidence: 🟢 Research support | 🟡 Framework synthesis | 🔴 Era prediction
durability: |
  §2 Foundation matrix: DURABLE (decades — brain-based depth targets)
  §3 Era-specific delivery: TIME-BOUND (update khi DKM §2 update)
  §4 Sequencing: SEMI-DURABLE (approximate, adjust per feedback)
  §5 Reduce: CONTEXT-DEPENDENT (per country/system)
---

# Curriculum Framework — Dạy Cái Gì, Khi Nào, Cho Ai v7.8

> **Domain-Knowledge-Map.md cho bạn BẢN ĐỒ — cây nào ở đâu.**
> **Education-Mechanism.md cho bạn NGUYÊN LÝ — trồng cây thế nào.**
> **File này cho bạn KẾ HOẠCH — trồng cây NÀO, KHI NÀO, SÂU bao nhiêu.**
>
> DKM = WHAT tồn tại. Mechanism = HOW brain học. File này = WHAT × WHEN × HOW DEEP.
>
> Foundation Matrix (§2) = durable decades.
> Era-specific (§3) = update khi DKM §2 đổi.
> Sequencing (§4) = approximate, per-individual varies.
>
> **"Dạy CÁI GÌ thay đổi mỗi era. Dạy KHI NÀO ổn định hơn — vì não ổn định."**

---

## Mục lục

0. Mục đích + Nguyên tắc curriculum
1. Taxonomy (brief — chi tiết xem DKM v1.0)
2. Foundation Delivery Matrix (DURABLE)
3. Era-specific Delivery (2025+, TIME-BOUND)
4. Sequencing by Stage
5. Cái cần GIẢM/BỎ từ curricula hiện tại
6. Honest Assessment + Kết nối

---

## 0. MỤC ĐÍCH + NGUYÊN TẮC CURRICULUM

```
TẠI SAO CẦN FILE NÀY (vị trí trong bộ 3):

  Domain-Knowledge-Map.md v1.0 = BẢN ĐỒ NHÓM KIẾN THỨC
    → 3 tiers: Foundation / Era-specific / Per-hardware
    → Per nhóm: WHY cần + prerequisite + timing hint
    → = WHAT tồn tại — chưa cho biết TEACH WHEN, HOW DEEP

  Education-Mechanism.md v1.0 = NGUYÊN LÝ THIẾT KẾ ARC
    → 8 nguyên lý brain-based (Direction > Level, Cost, Prerequisite...)
    → Valid mọi era, mọi domain
    → = HOW thiết kế bài — chưa cho biết TEACH WHAT

  File NÀY = DELIVERY MATRIX
    → Nối DKM (WHAT) × Mechanism (HOW) × ES stages (WHEN)
    → Per domain × per stage → depth target + delivery notes
    → + Sequencing: balance giữa 3 tiers per stage
    → + Cái cần giảm/bỏ (practical guidance)

  = "Dạy CÁI GÌ" + "KHI NÀO" + "SÂU bao nhiêu" + "BỎ CÁI GÌ"
  = Curriculum LAYER — bridge giữa abstract taxonomy và system stages


  Tại sao TÁCH từ Education-System.md:
    → "Dạy gì" THAY ĐỔI per era (content = variable)
    → "Cách tổ chức hệ thống" ÍT THAY ĐỔI hơn (system design = stable)
    → Tách → update curriculum KHÔNG cần rewrite system design
    → Era đổi → update file NÀY + DKM §2 → giữ System + Hardware


4 NGUYÊN TẮC CURRICULUM:

  ① FOUNDATION TRƯỚC, SPECIALIZATION SAU
     (Education-Mechanism §2.4 — prerequisite check)
     → Foundation domains = MỌI era, MỌI hardware cần
     → Specialization = emerge per-hardware + per-interest, Stage 3+
     → "Tất cả biết đọc, biết tính, biết giao tiếp → RỒI MỚI chuyên sâu"
     → ≠ "Specialization sớm" (nguy hiểm: build trên foundation yếu)

  ② MECHANISM-BASED DELIVERY
     (Education-Mechanism §2 — 8 nguyên lý arc design)
     → MỌI content → deliver qua đúng brain mechanism
     → Direction > Level: approach-direction, KHÔNG threat-direction (§2.2)
     → Content KHÔNG quyết định method → brain mechanism quyết định method
     → VD: "Dạy toán" → method depends on hardware + direction, NOT on "toán"

  ③ ADAPTABILITY SONG SONG VỚI CONTENT
     (DKM §1.6 — Meta-learning = foundation domain)
     → Meta-learning ≠ "dạy sau khi dạy content"
     → Meta-learning = SONG SONG: "trong khi học toán, cũng đang học CÁCH HỌC"
     → Mỗi content domain = vehicle for BOTH domain knowledge + meta-skill

  ④ ALIGN VỚI DEVELOPMENTAL TIMELINE
     (Child-Development-Mechanism §9 — sensitive periods)
     → Đúng skill + đúng window = compile dễ + sâu + approach-tagged
     → Sai timing = vẫn compile nhưng cost cao hơn + risk avoidance tag
     → Curriculum timing align với PFC development + sensitive periods
```

---

## 1. TAXONOMY (brief — chi tiết xem Domain-Knowledge-Map.md v1.0)

```
⭐ DKM v1.0 ĐÃ MÔ TẢ CHI TIẾT 3-TIER TAXONOMY.
   Section này CHỈ TỔNG HỢP — context cho §2-§5.
   Per-domain detail (WHY, prerequisite, timing) → xem DKM v1.0.


3 TIERS — từ durable đến flexible:

  ┌──────────────────────────────────────────────────────────────┐
  │ TIER 1: FOUNDATION DOMAINS (6 nhóm — DKM §1)                │
  │   Cross-era, mọi hardware cần, DURABLE (decades)            │
  │   ① Literacy/Communication  ② Numeracy/Logic                │
  │   ③ Somatic/Physical        ④ Social/Emotional              │
  │   ⑤ Creative/Expressive     ⑥ Meta-learning                 │
  ├──────────────────────────────────────────────────────────────┤
  │ TIER 2: ERA-SPECIFIC DOMAINS (6 nhóm — DKM §2)              │
  │   2025+ specific, TIME-BOUND (update khi era đổi)            │
  │   ① AI Literacy             ② Information Curation           │
  │   ③ Systems Thinking        ④ Basic Science Literacy         │
  │   ⑤ Cross-cultural Awareness ⑥ Digital Wellbeing             │
  ├──────────────────────────────────────────────────────────────┤
  │ TIER 3: PER-HARDWARE DOMAINS (vô tận — DKM §3)              │
  │   Emerge per individual, KHÔNG plan trước                    │
  │   Observe hardware tendencies → support per-direction         │
  └──────────────────────────────────────────────────────────────┘


NGUYÊN TẮC CHUNG:
  → Foundation TRƯỚC, specialization SAU (DKM §4 — prerequisite logic)
  → Tier 1 rộng → Tier 2 thêm → Tier 3 sâu
  → Mỗi domain = 1 "cây" — gốc ai cũng cần, nhánh vô tận (DKM §0.2)
  → CÁCH đạt depth = KHÁC per hardware (Hardware-Calibration.md v1.0)


🟡 Taxonomy là framework synthesis — ranh giới Tier 1/2 có chỗ fuzzy
   (VD: Basic Science = Foundation hay Era-specific? → DKM §2.4 acknowledge)
```

---

## 2. FOUNDATION DELIVERY MATRIX (DURABLE)

```
MỤC ĐÍCH:
  → 6 Foundation domains (DKM §1) × 4 system stages (ES v2.0 §1) = MATRIX
  → Per domain × per stage → DEPTH TARGET + delivery notes
  → = "Mọi người ĐỀU cần gì, ở mức nào, khi nào"
  → = DURABLE — valid decades (brain-based depth targets)
  → DKM mô tả per domain CHI TIẾT (WHY, prerequisite, timing hint)
  → File này THÊM: delivery matrix per stage (DKM không có)


DEPTH LEVELS = CHUNK COMPILATION LEVELS:
  (Education-Mechanism §2.9 + Chunk.md v2.0 §1)

  L1 = RECOGNIZE — "nghe quen"
    → Proto-chunk: fire sometimes, partial match
    → Nhận ra, nhớ được, nhưng chưa giải thích tại sao

  L2 = EXPLAIN — "nói lại được, giải thích được"
    → Compiled chunk: PFC hold reliably, liên kết với chunks khác
    → Hiểu tại sao, articulate được

  L3 = APPLY — "dùng trong context MỚI"
    → Compiled + linked: transfer across contexts
    → Apply knowledge trong tình huống chưa gặp

  L4 = CREATE/TRANSFER — "kết hợp tạo cái mới"
    → Meta-chunk: nhiều sub-chunks merge → 1 unit vô thức
    → Sáng tạo, transfer cross-domain, expert-level


FOUNDATION MATRIX — 6 DOMAINS × 4 STAGES:

  ┌──────────────────┬──────────┬──────────┬──────────┬──────────┐
  │ Domain           │ Stage 2  │ Stage 3  │ Stage 4  │ Lifelong │
  │ (DKM §1)        │ (6-12)   │ (12-18)  │ (18-25)  │          │
  ├──────────────────┼──────────┼──────────┼──────────┼──────────┤
  │ ① Literacy       │ L1→L2    │ L2→L3    │ L3→L4    │ Maintain │
  │                  │ read+    │ analyze+ │ create+  │ + expand │
  │                  │ express  │ argue    │ publish  │          │
  ├──────────────────┼──────────┼──────────┼──────────┼──────────┤
  │ ② Numeracy       │ L1→L2    │ L2→L3    │ L3(→L4)  │ Maintain │
  │                  │ concrete │ abstract │ apply+   │ per need │
  │                  │ → begin  │ reasoning│ model    │          │
  │                  │ abstract │          │          │          │
  ├──────────────────┼──────────┼──────────┼──────────┼──────────┤
  │ ③ Somatic        │ L1→L2    │ L2→L3    │ L3→L4    │ Maintain │
  │                  │ coord+   │ sport/   │ mastery  │ health+  │
  │                  │ body-    │ craft+   │ per      │ body-    │
  │                  │ awareness│ health   │ domain   │ listen   │
  ├──────────────────┼──────────┼──────────┼──────────┼──────────┤
  │ ④ Social/        │ L1→L2    │ L2→L3    │ L3→L4    │ Maintain │
  │   Emotional      │ basic+   │ complex+ │ lead+    │ + deepen │
  │                  │ empathy+ │ self-reg+│ mentor+  │          │
  │                  │ cooperate│ conflict │ relate   │          │
  ├──────────────────┼──────────┼──────────┼──────────┼──────────┤
  │ ⑤ Meta-learning  │ Seeds    │ L1→L2    │ L2→L3    │ L3→L4   │
  │                  │ "cái này │ "tôi học │ self-    │ lifelong │
  │                  │ khó/dễ  │ tốt khi" │ directed │ adapt    │
  │                  │ với tôi" │          │ learning │          │
  ├──────────────────┼──────────┼──────────┼──────────┼──────────┤
  │ ⑥ Creative       │ L1→L2    │ L2→L3    │ L3→L4    │ Maintain │
  │                  │ explore+ │ develop+ │ personal │ + evolve │
  │                  │ express  │ style    │ voice    │          │
  └──────────────────┴──────────┴──────────┴──────────┴──────────┘


KEY OBSERVATIONS:

  → MỌI domain: bắt đầu Stage 2 (6-12) → build liên tục
    (Stage 1 = Child-Dev bộ 4 → foundation wiring đã xảy ra)

  → Meta-learning: BẮT ĐẦU CHẬM (seeds Stage 2) → TĂNG DẦN
    → PFC chưa đủ cho full meta-cognition ở 6-8
      (PFC-Hardware.md v1.1 — development pace parameter)
    → Stage 3: meta-learning BẮT ĐẦU thực sự → Stage 4: tự directed
    → Lifelong: domain DUY NHẤT tiếp tục phát triển L3→L4

  → Somatic: KHÔNG phải "phụ" → = foundation NGANG các domain khác
    → Body-base = processing channel
      (Body-Base.md v2.0 — Model 3+1, Education-Mechanism §2.2)
    → ≠ "Giờ thể dục" → = experiential learning channel
    → Multi-modal binding (Child-Dev-Mechanism §2 kênh ③) CẦN body channel

  → Social/Emotional: TĂNG complexity per stage
    → SPM F1 (Agent-Mechanism.md v1.0) = cơ chế xã hội chính
    → SPM bootstrap: cần self-chunks ĐỦ trước khi empathy phát triển sâu
      (Empathy.md — Self-Pattern-Match requires self-pattern)
    → Stage 2: basic cooperation → Stage 3: complex negotiation → Stage 4: leadership
    → ≠ "Môn đạo đức" → = practical skills qua TRẢI NGHIỆM

  → Creative: ALWAYS present → purpose thay đổi per stage
    → Stage 2: explore + express (hardware tendencies lộ)
    → Stage 3: develop style (identity + Imagine-Final form)
    → Stage 4: personal voice (unique contribution)
    → Creativity = novel chunk combinations → human differentiator vs AI
      (Imagine-Final emerge qua creative expression — Mechanism §2.6)

  → ⭐ APPROACH/AVOIDANCE ACROSS ALL DOMAINS:
    (Education-Mechanism §2.2 — Direction > Level)
    → Depth target = CHƯA ĐỦ — phải xét DIRECTION
    → L3 approach-tagged > L4 avoidance-tagged (về lifelong value)
    → "Ghét toán ở L3" < "thích toán ở L2" (lifelong engagement)
    → = CÁCH ĐẠT depth quyết định giá trị depth


NGUYÊN TẮC FOUNDATION:

  ① EVERYONE — bất kể hardware:
     → Foundation = same depth targets cho TẤT CẢ
     → CÁCH ĐẠT depth = KHÁC per hardware (Hardware-Calibration.md v1.0)
     → "Biết đọc, biết tính, biết giao tiếp, biết cảm nhận,
        biết sáng tạo, biết TỰ HỌC" = UNIVERSAL targets

  ② RỘNG + VỪA SÂU (Stage 2) → SÂU + CHỌN LỌC (Stage 3-4):
     → Stage 2: 6 domains ĐỒNG ĐỀU → explore all → hardware tendencies lộ
     → Stage 3: foundation MAINTAIN + depth ở hardware-matched domains
     → Stage 4: foundation maintain + DEEP specialization
     → = "T-shape": rộng ở base + sâu ở 1-2 domains

  ③ DEPTH > VOLUME:
     → "Hiểu TOÁN ở L3" > "biết NHIỀU MÔN ở L1"
     → L3 compiled + linked = transfer được, durable
     → L1 proto-chunks = "biết tên nhiều thứ, HIỂU không thứ nào"
     → Type A evaluative reward (RSA v1.0) chỉ fire khi depth ĐỦ
       → Shallow learning = miss Type A → miss real satisfaction signal

  🟡 Foundation matrix = derived from developmental research + mechanism principles
     Specific depth targets per stage = framework estimate, not proven benchmarks
```

---

## 3. ERA-SPECIFIC DELIVERY (2025+, TIME-BOUND)

```
⚠️ SECTION NÀY CÓ HẠN SỬ DỤNG — update khi DKM §2 update.
   Era context chi tiết → xem Era-Analysis-2025.md.
   Per-domain WHY + prerequisite → xem DKM §2.

MỤC ĐÍCH:
  → 6 Era-specific domains (DKM §2) → depth targets per stage
  → = "Era NÀY cần THÊM → dạy KHI NÀO, SÂU bao nhiêu"


① AI LITERACY (DKM §2.1):

  Stage 2 (6-12): EXPOSURE — L1
    → "AI là gì" (phù hợp tuổi): "máy có thể học pattern"
    → Dùng AI tools cơ bản (với supervision)
    → "AI CÓ THỂ SAI" — critical awareness seed
    → ⚠️ Age-appropriate: KHÔNG cần "LLM architecture" cho 8 tuổi

  Stage 3 (12-18): CRITICAL USE — L2→L3
    → Đánh giá AI output: bias, hallucination, limits
    → WHEN to use vs WHEN NOT to use AI
    → Human-AI collaboration skills bắt đầu
    → Ethics: privacy, fairness, impact on jobs

  Stage 4 (18+): PROFESSIONAL — L3→L4
    → AI trong professional domain (per-specialization)
    → Advanced human-AI collaboration
    → AI as thinking partner, not just tool


② INFORMATION CURATION (DKM §2.2):

  Stage 2: BASICS — L1
    → "Không phải mọi thứ trên internet đều đúng"
    → Source evaluation cơ bản: "ai nói? tại sao?"
    → Compare sources: "2 bài khác nhau → cái nào đáng tin?"

  Stage 3: CRITICAL CURATION — L2→L3
    → Advanced source evaluation: bias, methodology, evidence
    → Synthesize từ NHIỀU sources → own understanding
    → "Biết hỏi ĐÚNG câu hỏi" = core era-skill

  Stage 4: PROFESSIONAL — L3→L4
    → Domain-specific information evaluation
    → Research methodology, evidence hierarchy


③ SYSTEMS THINKING (DKM §2.3):

  Stage 2: SEEDS — L1
    → Cause and effect: "nếu X → thì Y"
    → Simple systems: ecosystem, water cycle

  Stage 3: DEVELOP — L2→L3
    → Feedback loops, interconnections, unintended consequences
    → Apply: economics, environment, social systems
    → Cross-domain connections begin (convergence)

  Stage 4: COMPLEX — L3→L4
    → Model complex systems, predict behavior, design interventions


④ BASIC SCIENCE LITERACY (DKM §2.4):

  Stage 2: EXPERIENCE — L1→L2
    → Thế giới vật chất hoạt động thế nào (qua trải nghiệm)
    → Scientific method seeds: observe, hypothesize, test
    → ⚠️ Approach-direction crucial: hands-on + wonder, NOT memorize facts
      (Education-Mechanism §2.2 — Direction > Level)

  Stage 3: METHOD — L2→L3
    → Scientific reasoning, evidence-based thinking
    → Hypothesis-testing, experimental design

  Stage 4: APPLICATION — L3→L4
    → Science per-domain, research methodology
    → Evaluate scientific claims = critical era-skill

  🟡 Basic Science = boundary Foundation / Era-specific (DKM §2.4 acknowledge)
     Gốc = arguably cross-era, depth emphasis = era-dependent


⑤ CROSS-CULTURAL AWARENESS (DKM §2.5):

  Stage 2: EXPOSURE — L1
    → "Thế giới có nhiều cultures khác nhau → đều có giá trị"
    → Basic: languages, customs, celebrations

  Stage 3: UNDERSTANDING — L2→L3
    → Cultural perspectives, collaboration challenges
    → Cross-cultural communication (practical skill)

  Stage 4: PROFESSIONAL — L3
    → Global collaboration, cross-cultural leadership


⑥ DIGITAL WELLBEING (DKM §2.6):

  Stage 2: BASICS — L1
    → Screen time awareness: "bao nhiêu là đủ?"
    → Online safety basics
    → "Body CẢM THẤY thế nào sau screen?" (body-base awareness)
      (Body-Base.md v2.0 — interoception channel)

  Stage 3: SELF-MANAGEMENT — L2→L3
    → Attention management: "tôi bị distract bởi cái gì?"
    → Social media literacy: comparison, addiction patterns, FOMO
    → Cortisol management: recognize information overload signals
      (Cortisol-Baseline.md v2.0 — chronic low-grade amplification)

  Stage 4: LIFESTYLE DESIGN — L3
    → Technology serves ME, not reverse
    → Professional digital boundaries


🔴 Era-specific = prediction-based → WILL need updates
   "AI literacy" của 2025 ≠ của 2030 ≠ của 2035
   DKM §2 update → file này §3 update theo
   = Teach PRINCIPLES of tools → not specific tools
```

---

## 4. SEQUENCING BY STAGE

```
MỤC ĐÍCH:
  → Tổng hợp: Foundation (§2) + Era-specific (§3) → balance per stage
  → = "Ở MỖI stage, tỉ lệ giữa 3 tiers THẾ NÀO?"
  → Prerequisite logic chi tiết → xem DKM §4


BALANCE GIỮA 3 TIERS PER STAGE:

  ┌──────────┬─────────────┬─────────────┬─────────────┐
  │ Stage    │ Tier 1      │ Tier 2      │ Tier 3      │
  │          │ Foundation  │ Era-specific│ Per-hardware │
  ├──────────┼─────────────┼─────────────┼─────────────┤
  │ 2 (6-12) │ ████████    │ ██          │ ░           │
  │          │ 70-80%      │ 15-20%      │ 5-10%       │
  │          │ DOMINANT    │ exposure    │ seeds       │
  ├──────────┼─────────────┼─────────────┼─────────────┤
  │ 3 (12-18)│ █████       │ ████        │ ███         │
  │          │ 40-50%      │ 25-30%      │ 20-30%      │
  │          │ maintain+   │ develop     │ BEGIN       │
  │          │ deepen      │             │ specialize  │
  ├──────────┼─────────────┼─────────────┼─────────────┤
  │ 4 (18+)  │ ███         │ ███         │ ██████      │
  │          │ 20-30%      │ 20-25%      │ 45-55%      │
  │          │ maintain    │ maintain    │ DOMINANT    │
  └──────────┴─────────────┴─────────────┴─────────────┘


PER STAGE — PHƯƠNG CHÂM:

  STAGE 2 (6-12) — "Rộng + vừa sâu — xây foundation CHẮC":
    → Foundation 70-80%: 6 domains ĐỒNG ĐỀU → hardware tendencies lộ
    → Era-specific 15-20%: exposure (biết AI tồn tại, biết internet có sai)
    → Per-hardware 5-10%: observe tendencies, cho explore per interest
    → Bridge cần NHIỀU nhất (Mechanism §3.4 — nguồn ④ dominant ở age này)
    → ⚠️ Ép specialization sớm = build trên foundation yếu

  STAGE 3 (12-18) — "Foundation giữ + era-skills develop + direction emerge":
    → Foundation 40-50%: maintain + deepen (L2→L3 cho most domains)
    → Era-specific 25-30%: critical use (AI evaluation, info synthesis, systems)
    → Per-hardware 20-30%: hardware tendencies VISIBLE → cho chọn depth
    → Bridge giảm DẦN (nguồn ①② mạnh dần — Mechanism §3.4)
    → Imagine-Final bắt đầu form → respect lifecycle (Mechanism §2.6)

  STAGE 4 (18+) — "Deep in 1-2 + maintain rest + contribute":
    → Foundation 20-30%: maintain (không bỏ, duy trì lifelong health)
    → Era-specific 20-25%: professional application
    → Per-hardware 45-55%: DEEP specialization → hardware-matched domain
    → Bridge gần không cần (nguồn ①②③ dominant — self-directed)
    → Cross-domain integration begins (convergence across domains)


PREREQUISITE LOGIC (brief — chi tiết xem DKM §4):

  → Tier 1 Foundation = TRƯỚC
    (Literacy + Numeracy = prerequisite hầu hết Tier 2)
  → Tier 2 Era-specific = SAU KHI foundation CƠ BẢN đủ
  → Tier 3 Per-hardware = SAU KHI tendencies LỘ (không ép sớm)
  → OVERLAP đáng kể: tiers KHÔNG sequential hoàn toàn
    (Tier 2 bắt đầu khi Tier 1 CƠ BẢN đủ, không chờ HOÀN THÀNH)
  → AI check per student: KHÔNG dùng age → dùng CHUNK STATUS
    (DKM §4: cùng tuổi, khác chunk status → khác readiness)


🟡 Percentages = APPROXIMATE → per-individual varies
   Early direction rõ: Tier 3 cao hơn sớm hơn = bình thường
   Late bloomer: Tier 1 extend vào Stage 3 = bình thường
   Multi-talent: Tier 3 chia nhiều nhánh = bình thường
```

---

## 5. CÁI CẦN GIẢM / BỎ TỪ CURRICULA HIỆN TẠI

```
⚠️ CONTROVERSIAL NHƯNG CẦN THIẾT:

  Thêm Tier 2 + Tier 3 = THÊM content → nhưng time = LIMITED.
  → Nếu chỉ THÊM mà không BỎ → overload:
    → Cortisol amplification (Cortisol-Baseline.md v2.0 — Role ① amplifier)
    → Threat-direction → avoidance tags cho domain liên quan
    → = NGƯỢC mục đích (Education-Mechanism §2.2 — Direction > Level)
  → PHẢI giảm/bỏ CÁI GÌ ĐÓ để CÓ CHỖ cho cái mới
  → "BỎ" ≠ "xóa sổ" → = "GIẢM TỈ TRỌNG" hoặc "ĐỔI CÁCH DẠY"


CÁI GIẢM:

  ① ROTE MEMORIZATION OF FACTS
     → AI lookup facts trong giây → memorize facts = giá trị GIẢM
     → ≠ "Không cần nhớ gì" → = "nhớ FOUNDATION chunks, lookup DETAILS"
     → VD: nhớ "F=ma" CẦN (compiled chunk) → nhớ 118 nguyên tố = AI lookup
     → = GIẢM drill/memorize → TĂNG understand/apply (L1→L2/L3 shift)

  ② EXCESSIVE STANDARDIZED TESTING
     → Test culture = optimize surface (L1 proto-chunk) → miss depth (L2-L4)
     → Time dành cho test prep → CÓ THỂ dùng cho project, depth, meta-learning
     → ≠ "Bỏ hết thi" → = "GIẢM high-stakes test + TĂNG formative assessment"
     → Type A evaluative reward (RSA v1.0) cần depth
       → Surface test = miss Type A → miss real satisfaction signal
     → (ref: Education-System v2.0 §6 — assessment per depth level)

  ③ CONTENT ONLY RELEVANT CHO FORMAT CŨ
     → Kỹ năng CHỈ hữu ích trong system hiện tại, KHÔNG transferable
     → VD: "thuộc lòng bài thơ để đọc trước lớp" → test memory, NOT understanding
     → = Giữ bài thơ → ĐỔI "thuộc lòng" → "phân tích ý nghĩa" (L1→L2/L3)

  ④ PASSIVE LECTURE TIME
     → Lecture = weakest compile mechanism:
       single-modal, low multi-modal richness (Education-Mechanism §2.3)
     → KHÔNG bỏ hết → GIẢM tỉ lệ → TĂNG experiential + project + discussion
     → Balance: lecture 20-30% (intro + framework) + active 70-80% (practice + apply)
     → Multi-modal binding (Child-Dev-Mechanism §2 kênh ③) CẦN active engagement


CÁI KHÔNG BỎ (dù có áp lực "bỏ"):

  ✓ Foundation domains — KHÔNG BAO GIỜ bỏ
    → "AI đọc hộ → bỏ dạy đọc?" → KHÔNG → "đọc" = HIỂU ý nghĩa, không chỉ decode
    → "AI tính hộ → bỏ dạy toán?" → KHÔNG → "toán" = logical thinking
    → Foundation chunks = prerequisite cho mọi Tier 2 + Tier 3 (DKM §4)

  ✓ Physical education — KHÔNG bỏ
    → Body-base = processing channel (Body-Base.md v2.0 — Model 3+1)
    → Somatic domain = brain development domain, không chỉ "sức khỏe"
    → ⚠️ Trend giảm Physical education → damage brain development
      (Multi-modal binding cần body — Education-Mechanism §2.3)

  ✓ Arts/Creative — KHÔNG bỏ
    → Creativity = human differentiator → era NÀY cần HƠN
    → "Arts = không thực tế" → NGƯỢC LẠI: arts = hardware expression channel
    → Imagine-Final emerge qua creative expression (Mechanism §2.6)

  ✓ Social interaction — KHÔNG bỏ (dù online learning tăng)
    → SPM F1 (Agent-Mechanism.md v1.0) cần real human interaction data
    → AI/online ≠ substitute cho face-to-face social processing
    → ⚠️ Post-COVID: social skill decline observable → CẦN TĂNG, không giảm


TỔNG KẾT:

  ┌──────────────────────┬───────────────────────────────┐
  │ GIẢM                  │ THAY THẾ BẰNG                 │
  ├──────────────────────┼───────────────────────────────┤
  │ Rote memorization    │ Understanding + application    │
  │ Excessive testing    │ Formative + depth assessment  │
  │ Format-only content  │ Transferable skills           │
  │ Passive lecture      │ Active + experiential learning│
  └──────────────────────┴───────────────────────────────┘

  = KHÔNG phải "bỏ toán" → mà "bỏ CÁCH dạy toán bằng drill vô nghĩa"
  = KHÔNG phải "bỏ văn" → mà "bỏ CÁCH dạy văn bằng thuộc lòng"
  = Giữ DOMAIN → đổi METHOD + DEPTH TARGET
  = Giữ cái GÌ dạy → đổi CÁCH dạy + độ SÂU đo
```

---

## 6. HONEST ASSESSMENT + KẾT NỐI

```
⭐ CÁI FILE NÀY CÓ THỂ LÀM:

  ✅ Delivery matrix: 6 foundation domains × 4 stages × depth targets (§2)
  ✅ Era-specific delivery: 6 domains × per stage (§3)
  ✅ Sequencing: balance 3 tiers per stage (§4)
  ✅ Practical guidance: cái cần giảm/bỏ (§5)
  ✅ Bridge DKM taxonomy với system stages thành delivery plan


⭐ CÁI FILE NÀY KHÔNG THỂ LÀM:

  ❌ Prescribe SPECIFIC lesson plans hoặc textbooks
     → File = FRAMEWORK level → lesson plans = implementation level
  ❌ Apply uniformly across cultures
     → Foundation = universal → HOW teach literacy VN ≠ Finland
     → Per-country → Country/ files
  ❌ Guarantee era-specific skill list = correct
     → Era-specific = prediction-based → WILL need updates (DKM §2)
  ❌ Provide assessment tools
     → Assessment = Education-System v2.0 §6 → file này = WHAT, not MEASURE


⭐ ĐỘ TIN CẬY:

  CAO 🟢→🟡:
    → §2: Foundation matrix — derived from developmental timeline + research
    → §1: 6 foundation domains — brain-based (UNESCO, OECD, neuroscience consistent)
    → §0: 4 curriculum principles — derived from Mechanism §2

  TRUNG BÌNH 🟡:
    → §4: Sequencing percentages — approximate, not tested
    → §5: What to reduce — logical but politically charged

  THẤP 🔴:
    → §3: Era-specific delivery details — prediction-based
    → §4: Tier 3 timing — too individual to generalize


⭐ RỦI RO:

  ⚠️ "6 FOUNDATION = ĐỦ?" — có thể thiếu
     VD: Ethical reasoning? Environmental awareness?
     6 = framework synthesis → OPEN to revision (DKM §5 acknowledge)

  ⚠️ REDUCTION RESISTANCE
     "Giảm memorization" = logical → nhưng exam system = memorization-based
     Change curriculum WITHOUT change assessment = FAIL
     → §5 CẦN ES v2.0 §6 (assessment reform) để work

  ⚠️ FALSE PRECISION
     Depth target "L2→L3 ở Stage 3" = framework estimate
     Reality: per-individual variation cao
     AI + teacher calibrate per student → file cho DIRECTION, không cho GPS
```

```
KẾT NỐI:

═══════════════════════════════════════════════════════
TẦNG 3 — NỀN TẢNG TRỰC TIẾP (Research/Education/)
═══════════════════════════════════════════════════════

→ Domain-Knowledge-Map.md v1.0 — ⭐ BẢN ĐỒ DOMAIN
  §1 Foundation (6 nhóm), §2 Era-specific (6 nhóm),
  §3 Per-hardware, §4 Prerequisite logic.
  File NÀY derive delivery matrix TỪ taxonomy DKM.

→ Education-Mechanism.md v1.0 — ⭐ NGUYÊN LÝ ARC DESIGN
  §2 8 nguyên lý (Direction>Level, Cost, Prerequisite, Mini-arcs,
  Imagine-Final, Feedback, Consolidation, Depth Assessment).
  File NÀY apply principles vào delivery decisions.

→ Observation/Empathy-Education.md v2.0 — Empathy per age
  SPM-based framework cho Social/Emotional domain (§2 ④).

→ Observation/Education-Arms-Race.md v1.2 — Competition dynamics
  Societal pressure affecting all domains — overload context cho §5.


═══════════════════════════════════════════════════════
TẦNG 4 — CÙNG FOLDER (Applications/Education/)
═══════════════════════════════════════════════════════

→ Education-System.md v2.0 — ⭐ KHUNG CHÍNH
  §1 4-stage architecture, §2-§4 stage details, §6 assessment.
  File NÀY align depth targets PER stage từ ES.

→ Hardware-Calibration.md v1.0 — Per-individual calibration
  6 dimensions → CÁCH đạt depth targets KHÁC per hardware.
  File NÀY = universal depth targets, HC = per-individual path.

→ Era-Analysis-2025.md — Era context
  AI revolution, skill shifts → context cho §3 era-specific delivery.

→ 00_Overview.md — Map vị trí file trong folder


═══════════════════════════════════════════════════════
TẦNG 1-2 — CORE + CHILD-DEV
═══════════════════════════════════════════════════════

→ Core-Software.md v1.0 — Cycle-based architecture
  Chunks = sole substrate. Learning = compile new chunks.

→ Core-Hardware.md v1.0 — 4 zones A/B/C/D
  Hardware parameters → per-hardware domain strengths (Tier 3).

→ Child-Development-Mechanism.md v1.0 — Developmental timeline
  §2 4+1 compile, §3 Approach/avoidance tags, §9 Sensitive periods.
  Foundation cho timing decisions trong matrix.

→ Agent-Mechanism.md v1.0 — SPM F1
  Social processing mechanism → Social/Emotional domain (§2 ④).

→ Cortisol-Baseline.md v2.0 — Amplifier reframe
  Direction > level. Overload = amplified threat → context cho §5.

→ Reward-Signal-Architecture.md v1.0 — Type A/B reward
  A = evaluative (depth), B = hardware-direct.
  Depth assessment (§2 L1-L4) connects to Type A quality signal.

→ Body-Base.md v2.0 — Model 3+1
  Somatic domain (§2 ③) = body as processing channel.

→ Imagine-Final.md — Lifecycle 5 phases
  Creative domain (§2 ⑥) + direction emergence → Tier 3 navigation.

→ Imagine-Final-Evaluation.md v1.1 — 4 góc quality
  Hardware × Domain fit → Tier 3 direction quality check.


═══════════════════════════════════════════════════════
TẦNG 5 — COUNTRY (Applications/Education/Country/)
═══════════════════════════════════════════════════════

→ Country/VN/ — Localize curriculum per culture
  File NÀY = universal framework → VN files = VN-specific application.


UPDATE SCHEDULE:
  → §2 Foundation matrix: DURABLE — review per decade
  → §3 Era-specific: TIME-BOUND — update khi DKM §2 update
  → §4 Sequencing: SEMI-DURABLE — adjust per feedback
  → §5 Reduce: CONTEXT-DEPENDENT — per country/system
```
