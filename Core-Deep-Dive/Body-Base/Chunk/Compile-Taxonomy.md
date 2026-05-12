---
title: Compile-Taxonomy — 3 Loại Compile + 6 Trade-offs
version: 1.1
created: 2026-05-08
updated: 2026-05-10 (v1.1 — §3 reward implication cross-ref)
status: v1.1
scope: |
  PHÂN LOẠI CHÍNH THỨC 3 loại compile (A/B/C) + 6 trade-offs.
  Giải đáp: tại sao brain compile ngắn, tại sao "biết mà không làm",
  tại sao collective chain gãy → cá nhân gánh.
  DỰA TRÊN Drill sessions S1-S6 (§2, §3, §4, §7, §19, §22).
  KHÔNG suy đoán — mỗi claim có drill source reference.
purpose: |
  GAP 11 (CRITICAL): Compile taxonomy chưa formalize.
  GAP 14: "PFC-directed compile" terminology chưa chính thức.
  File này resolve CẢ HAI.
  Body-Base.md §4.2 reference đến file này cho chi tiết.
parent: Chunk.md v2.1 (§2 compile mechanisms = foundation)
related: |
  Body-Base.md §4 — summary 3 Loại (reference tới file này)
  Collective-Body.md §2 — 4 compile pathways + Type C × 3 cấp
  VP v1.4 §4 — clarification: VP chains = explanatory, not processing
  PFC-Function.md v1.1 §4/§6/§9 — PFC = director, confabulation
  Chunk.md v2.1 §2 — 4 compile mechanisms + trust gate + external install
  Blackbox-Map.md — 5 gaps + 2 complexity dimensions (supersedes Framework-Boundaries.md)
sources: |
  Drill-Compile-Short-Collective.md §2 — 3 hardware constraints
  Drill-Compile-Short-Collective.md §3 — 3 Loại A/B/C
  Drill-Compile-Short-Collective.md §4 — Trust-to-compile 5 bước
  Drill-Compile-Short-Collective.md §7 — 6 trade-offs
  Drill-Compile-Short-Collective.md §19 — PFC = director, body = compiler
  Drill-Compile-Short-Collective.md §22 — 4 compile pathways + BB2 reframe
  Drill-Compile-Short-Collective.md §5 — Model 3 cấp
language: Tiếng Việt primary + English technical terms
confidence: 🟢 Research support | 🟡 Framework synthesis | 🔴 Hypothesis
---

# Compile-Taxonomy — 3 Loại Compile + 6 Trade-offs

> **Cùng là "đi học toán" — 4 đứa trẻ, 4 cơ chế compile KHÁC NHAU.**
>
> Đứa thích toán → body tự reward (Hardware Fit).
> Đứa nghe mẹ → trust compile [học→tốt] (Trust Install).
> Đứa thấy bạn bè đều đi → đương nhiên (Social Default).
> Đứa sợ bị mắng → avoid threat (Threat Avoidance).
>
> **TẤT CẢ compile NGẮN ở cấp cá nhân (1-2 nodes).**
> Chain dài [toán→đại học→việc→lương→body-base] nằm ở CẤP 2 (collective).
> Cá nhân chỉ cần trust + compile short → collective deliver kết quả.
>
> File này: TẠI SAO ngắn, MẤY LOẠI, TRADE-OFFS gì.

---

## MỤC LỤC

- §0 — Vị Trí Trong Framework
- §1 — Tại Sao Brain Compile Ngắn: 3 Hardware Constraints
- §2 — 3 Loại Compile (A/B/C): Core Taxonomy
- §3 — 4 Compile Pathways: Cùng Output, Khác Cơ Chế
- §4 — Trust-to-Compile: 5 Bước
- §5 — PFC = Director, Body = Compiler
- §6 — 6 Trade-offs Của Compile Ngắn
- §7 — Interactions: A vs C, "Biết Mà Không Làm", Chain Break
- §8 — Honest Assessment
- §9 — Cross-References

---

## §0 — Vị Trí Trong Framework

```
⭐ FILE NÀY FORMALIZE HAI KHÍA CẠNH CHƯA ĐƯỢC GHI NHẬN ĐỦ:

  1. COMPILE TAXONOMY:

     Chunk.md §2 đã mô tả 4 compile MECHANISMS (repetition, emotional peak,
     multi-modal, sleep) + external install.

     Nhưng CHƯA phân loại: cùng 4 mechanisms đó HOẠT ĐỘNG THEO MẤY LOẠI?
     Brain compile ngắn → tại sao? Trade-offs gì?

     → File này: 3 Loại (A/B/C) = taxonomy TRÊN CƠ SỞ 4 mechanisms.
     → GAP 11 (CRITICAL) → RESOLVED.

  2. "PFC-DIRECTED COMPILE" TERMINOLOGY:

     Framework nói "PFC ~5%, vô thức ~95%" → ĐÚNG.
     Nhưng ranh giới "PFC compile" vs "body compile" → CHƯA rõ.
     Drill §19 xác lập: PFC KHÔNG BAO GIỜ compile. Body LUÔN compile.
     "PFC-directed compile" = thuật ngữ CHÍNH XÁC.

     → File này: formalize terminology + spectrum.
     → GAP 14 → RESOLVED.


  VỊ TRÍ TRONG FILE HIERARCHY:

    Body-Base.md §4 (summary) → [file này] (chi tiết taxonomy)
    Chunk.md §2 (4 mechanisms) → [file này] (3 loại SỬ DỤNG 4 mechanisms)
    Collective-Body.md §2 (4 pathways × 3 cấp) → [file này] (chi tiết pathways)
    PFC-Function.md §9 (PFC tạo context) → [file này] (formalize director/compiler)

    Đọc Chunk.md §2 trước → đọc file này → đọc Collective-Body.md §2-§3.
```

---

## §1 — Tại Sao Brain Compile Ngắn: 3 Hardware Constraints

```
🟢🟡 3 CONSTRAINTS ĐỘC LẬP CÙNG CHỈ VỀ COMPILE NGẮN (Drill §2):


  ① PFC ~4±1 SLOTS = PHYSICS LIMIT:

     PFC-Hold-Dimensions.md §2: 6 lực ĐỘC LẬP hội tụ tại ~4:
       Toán tổ hợp: marginal gain đạt đỉnh ở 3→4
       Cấu trúc thế giới: ~2-4 biến nhân quả chính per situation
       False positive: >4 chiều → signal-to-noise SỤP
       Interference: >4 → oscillations collide
       Energy: maintain mỗi chiều = TỐN metabolic
       Evolution: không ĐỦ áp lực chọn lọc cho >4

     → Chain > 4 nodes = VƯỢT single PFC processing capacity
     → PFC KHÔNG THỂ chain [toán→điểm→đại học→việc→lương→body] TRONG 1 LẦN
     → = Hardware limit, KHÔNG phải "lười biếng"

     🟢 Working memory ~4±1: Cowan 2001 (highly cited meta-analysis)


  ② PROCESSING SPEED: PFC ~200ms+, AMYGDALA ~12ms:

     PFC-Function §6: PFC LUÔN CHẬM hơn subcortical response.
     → Chain dài = PFC process CHẬM → body ĐÃ respond trước
     → Evolution ưu tiên NHANH cho survival:
       "Tránh hổ trước, hiểu tại sao sau"
     → Compile ngắn = nhanh hơn = survival advantage

     🟢 Amygdala response ~12ms: LeDoux 1996
     🟢 PFC response ~200ms+: established neuroscience


  ③ CORTISOL COST: CHAIN DÀI = ACTIVE LOCK → CORTISOL SUSTAINED:

     PFC-Function §2 ⑧: Active Lock = PFC hold chunks → cortisol
     Cortisol-Baseline.md: sustained cortisol → neural wear
     → Chain dài → PFC hold LÂU hơn → cortisol LÂU hơn → TỐN chi phí
     → Compile ngắn → PFC hold ÍT → cortisol ÍT → tiết kiệm sinh học

     🟢 Cortisol + sustained cognitive load: Lupien et al. 2009


  ⭐ CONVERGENCE — 3 CONSTRAINTS CÙNG HƯỚNG:

    PFC capacity:     chain dài = VƯỢT giới hạn
    Processing speed:  chain dài = QUÁ CHẬM
    Energy cost:       chain dài = QUÁ ĐẮT
    → Brain BUỘC compile ngắn = KHÔNG phải lựa chọn

    Analogy: mắt con người chỉ có 3 loại cone (RGB).
    Phổ ánh sáng = liên tục (vô hạn tần số).
    Nhưng survival chỉ CẦN 3 trục → evolution KHÔNG thêm.
    → PFC ~4 slots: nhân quả survival chỉ cần ~4 chiều → KHÔNG thêm.

    → "Lý do brain compile ngắn" = KHÔNG vì design xấu
    → MÀ VÌ 3 constraints ĐỘC LẬP cùng hội tụ tại ĐÓ
    → = Tối ưu cho survival environment

  🟡 3-constraint convergence model: framework synthesis (Drill §2)
  🟢 Components individually established (Cowan 2001, LeDoux 1996, Lupien 2009)
```

---

## §2 — 3 Loại Compile (A/B/C): Core Taxonomy

### §2.1 — Loại A: Direct Short Compile (~90% behavior)

```
🟡🟢 LOẠI A — BODY EXPERIENCE → BODY COMPILE → CHUNKS FORM (Drill §3):


  MECHANISM:
    [action → sensory result → body evaluation → compile]
    = Body trải nghiệm trực tiếp → body tự wire → chunk hình thành
    = 4 compile mechanisms (Chunk.md §2.1) hoạt động tự nhiên

  CHAIN LENGTH: 1-2 nodes
  PFC ROLE: KHÔNG CẦN — vô thức compile trực tiếp
  TRUST ROLE: CÓ THỂ accelerate (mẹ nói lửa nóng → compile TRƯỚC bị bỏng)


  VÍ DỤ:
    [cho → người nhận vui → ấm]      → compiled [cho → ấm]
    [chạm lửa → nóng → đau]         → compiled [lửa → tránh]
    [học → mẹ khen → ấm]            → compiled [học → tốt]
    [ăn ngon → opioid]              → compiled [quán này → tốt]
    [không học → mẹ mắng → đau]     → compiled [không học → nguy hiểm]

    Lưu ý: 2 VD cuối TRÔNG giống nhau nhưng KHÁC mechanism:
    [học → mẹ khen → ấm] = approach (positive reinforcement)
    [không học → mẹ mắng] = avoidance (negative reinforcement)
    = CẢ HAI đều Loại A (direct, 1-2 nodes), chỉ khác direction.


  ĐẶC ĐIỂM:

    ✅ MẠNH NHẤT:
       Multi-modal (thấy + nghe + chạm + cảm xúc → wire deep)
       Direct experience = compile SÂU nhất, BỀN nhất
       Chunk.md §2.1: multi-modal = 1 trong 4 mechanisms chính

    ✅ NHANH NHẤT:
       Không cần PFC deliberation
       Body detect + evaluate + compile = tự động
       Amygdala pathway ~12ms → compile bắt đầu TRƯỚC PFC nhận ra

    ❌ NHƯNG: PHẠM VI HẸP:
       Chỉ compile cái ĐÃ trải nghiệm trực tiếp
       Không thể compile kiến thức abstract (e.g., vật lý, lịch sử)
       Không thể compile domain chưa tiếp xúc
       → Nếu CHỈ Loại A → bị giới hạn bởi personal experience


  LOẠI A = PHẦN LỚN CUỘC SỐNG:
    Habit, skill, routine, emotional conditioning
    ~90% behavior hàng ngày = Loại A compiled patterns fire tự động
    = Chunk.md §8.1: vô thức ~95% ≈ Loại A + Loại C compiled running

  🟢 Hebbian learning: Hebb 1949
  🟢 Flashbulb memories: Brown & Kulik 1977
  🟢 Positive/negative reinforcement: Skinner 1953, Rescorla & Wagner 1972
  🟡 ~90% estimate: framework synthesis (Drill §3)
```

### §2.2 — Loại B: Compiled Expertise (~5% behavior)

```
🟡🟢 LOẠI B — PFC-DIRECTED COMPILE QUA NHIỀU NĂM (Drill §3 + §19):


  MECHANISM:
    Experience NHIỀU LẦN → chunks → meta-chunks → pyramidal compression
    PFC DIRECT attention qua nhiều năm → vô thức compile SÂU
    = "PFC-directed body compile" (thuật ngữ chính xác — Drill §19)

  CHAIN LENGTH: BÊN NGOÀI "ngắn" (3-4 items), BÊN TRONG = decades compiled
  PFC ROLE: DIRECT attention + hold + imagine + domain-check (5 vai trò)
  TRUST ROLE: THẤP — direct experience + deliberate practice là chính


  VÍ DỤ:
    Expert chess: 50,000+ patterns → "cảm nhận" thế cờ = compiled depth
    Bác sĩ 20 năm: "nhìn bệnh nhân biết ngay" = compiled diagnosis
    Einstein: decades → E=mc² = 1 meta-chunk (bên trong = decades compiled)
    Nhạc sĩ jazz: nghe hợp âm → ngón tay tự phản ứng = compiled motor-auditory

    VP §5b Tầng 3: PFC "thấy ngắn" nhưng thực ra = compiled CỰC SÂU
    → 4×4×4 = 64 thông tin gốc compressed vào 1 PFC slot
    → Expert "thấy 4 thứ" = thực ra thấy CẢ VŨ TRỤ domain đó


  CÁCH LOẠI B HOẠT ĐỘNG (Drill §19 + §22E):

    PFC KHÔNG compile — PFC DIRECT body compile:

    ① PFC DIRECT ATTENTION: chọn CHÚ Ý vào domain cụ thể
    ② PFC HOLD IN WM: giữ ~4 chunks active → co-fire → body wire
    ③ PFC IMAGINE: simulate scenario → body REACT + compile
    ④ PFC DOMAIN-CHECK: verify smooth vs reality (1A vs 1B)
    ⑤ PFC CHANGE ENVIRONMENT: thay đổi context → body-input mới

    MỖI BƯỚC: PFC direct. Body compile.
    = Repetition ×1000 + emotional peaks + multi-modal + sleep
    = 4 compile mechanisms (Chunk.md §2.1) ĐƯỢC PFC HƯỚNG DẪN

    External tools EXTEND: giấy, bút, máy tính = "Cấp 2 cá nhân"
    → PFC hold 4 → viết ra → PFC freed → hold 4 tiếp → STACK
    → Trust past self → build on verified chunks → recursive compile
    = Collective-Body.md §3.3 (external tools = Cấp 2 cá nhân)


  ĐẶC ĐIỂM:

    ✅ CHÍNH XÁC NHẤT:
       Calibrated qua domain feedback (Body-Feedback §1 — 1A check)
       Direct experience + domain-check = compile ĐỦ ĐỘ TIN CẬY
       = Expert intuition reliable (F4 02: feeling-intuition gradient)

    ❌ NHƯNG: CHẬM NHẤT:
       Cần YEARS trong 1 domain → compiled expertise
       Chase & Simon 1973: ~10 years to expert
       = Cá nhân CÓ THỂ chain dài ĐÔI KHI, nhưng hiếm + costly

    ❌ NHƯNG: DOMAIN-SPECIFIC:
       Einstein = expert vật lý + novice cooking
       Đổi domain → chunks mới chưa compile → chain ngắn lại
       = Loại B KHÔNG transfer across domains


  LOẠI B = EXPERTISE:
    ~5% behavior = khi cá nhân hoạt động TRONG expert domain
    Ngoài domain → quay về Loại A + Loại C
    → MỌI NGƯỜI = Loại B ở VÀI domain + Loại A/C ở HẦU HẾT domain

  🟢 Expert chess 50,000+ patterns: Chase & Simon 1973
  🟢 Neural efficiency (expert fire ÍT hơn): Haier 1992, Neubauer & Fink 2009
  🟢 Deliberate practice ~10 years: Ericsson et al. 1993
  🟡 Pyramidal compression model: framework synthesis (VP §5b Tầng 3)
  🟡 "PFC-directed body compile": framework terminology (Drill §19)
```

### §2.3 — Loại C: Installed + Collective

```
🟡 LOẠI C — TRUST → INSTALL SHORT + COLLECTIVE HOLD LONG (Drill §3 + §22):


  MECHANISM:
    Trust source → body nhận input → compile [action→result] SHORT
    Chain dài NẰM Ở collective (CẤP 2), KHÔNG ở individual (CẤP 1)
    Cá nhân compile SHORT → collective deliver kết quả dài hạn

  CHAIN LENGTH:
    Individual = SHORT (1-2 nodes)
    Collective = LONG (5+ nodes, distributed)
  PFC ROLE: CHỌN trust ai → compile → PFC explain post-hoc (confabulation)
  TRUST ROLE: CỐT LÕI — gate cho toàn bộ quá trình


  VÍ DỤ:
    Trẻ: trust mẹ → compile [học → tốt]
      Collective hold: [học → đại học → việc → lương → body-base feed]

    Tín đồ: trust giáo lý → compile [cầu nguyện → bình an]
      Collective hold: [cầu nguyện → contemplative → cortisol giảm →
                        vmPFC train → bình an dài hạn]

    Chiến sĩ: trust lãnh đạo → compile [chiến đấu → ý nghĩa]
      Collective hold: [chiến đấu → chiến thắng → đàm phán →
                        hòa bình → body-base toàn dân]

    Ngôn ngữ: trust môi trường → compile [từ → nghĩa]
      Collective hold: [hệ thống ngữ pháp + từ vựng + pragmatics]

    Đạo đức: trust cộng đồng → compile [trộm → xấu]
      Collective hold: [luật pháp + enforcement + cultural norms]


  ĐẶC ĐIỂM:

    ✅ NHANH:
       Bypass chain verification qua trust (Drill §4)
       Compile [action → result] trong VÀI LẦN tiếp xúc
       Không cần PFC deliberate chain logic

    ✅ RỘNG:
       Access collective knowledge mà không cần experience riêng
       "Biết lửa nóng" mà không cần bị bỏng (mẹ install)
       = Phần lớn kiến thức con người = installed, NOT compiled direct

    ❌ NHƯNG: PHỤ THUỘC COLLECTIVE:
       Collective chain gãy → cá nhân gánh hậu quả
       VD: [học → việc] chain gãy do AI → "học làm gì?"
       Individual KHÔNG biết chain gãy ở ĐÂU vì KHÔNG hold chain

    ❌ NHƯNG: DỄ BỊ EXPLOIT:
       Trust wrong source → compiled pattern sai
       VP §2 ④: trust = per-entity, MODULATE toàn bộ valence profile
       → Trust CAO trên NGƯỜI → TẤT CẢ từ người đó amplified
       → = KOL cross-domain trust transfer (Drill §22D)
       → = Cult install qua trust weaponized


  ⭐⭐ LOẠI C = PHẦN LỚN BEHAVIOR HÀNG NGÀY — FRAMEWORK CHƯA NHẬN RA ĐỦ:

    Ngôn ngữ, đạo đức, skill xã hội, world knowledge,
    religious beliefs, political views, dietary habits,
    fashion norms, career expectations, parenting styles
    = TẤT CẢ Loại C installed qua trust từ collective.

    Trước drill: framework focus chủ yếu Loại A + Loại B.
    Drill §3 insight: Loại C = CƠ CHẾ CHÍNH cho ~phần lớn social behavior.
    → Cá nhân "tự do lựa chọn" phần lớn = Loại C installed + PFC confabulate.


  3 LOẠI × TƯƠNG TÁC:

    LOẠI A + C = ~95% BEHAVIOR HÀNG NGÀY:
      Type A: [experience → compile short]
      Type C: [trust source → compile short]
      → CẢ HAI compile ngắn. CẢ HAI chạy tự động.
      → Phân biệt: A = internal experience. C = external install.
      → NHƯNG: Chunk §1.1 — NO SOURCE TAG → body treat BÌNH ĐẲNG.

    LOẠI B = ~5%:
      Chỉ khi CÁ NHÂN hoạt động trong EXPERT DOMAIN
      → Ngoài domain: quay về A + C

    ⭐ "Compile ngắn" = DOMINANT mode, không phải ONLY mode = SPECTRUM

  🟡 Loại C dominance insight: framework synthesis (Drill §3)
  🟢 Cultural transmission: Boyd & Richerson 1985
  🟢 Social learning: Bandura 1977
  🟢 Trust as gate: established social psychology
```

### §2.4 — Bảng So Sánh 3 Loại

```
🟡 COMPARISON TABLE — 3 LOẠI COMPILE:

  ┌────────────────────────────────────────────────────────────────────┐
  │                    │ LOẠI A          │ LOẠI B          │ LOẠI C    │
  │                    │ Direct Short    │ Compiled Expert │ Installed │
  ├────────────────────┼─────────────────┼─────────────────┼───────────┤
  │ % behavior         │ ~90%            │ ~5%             │ overlap   │
  │                    │                 │ (in-domain)     │ với A     │
  ├────────────────────┼─────────────────┼─────────────────┼───────────┤
  │ Chain length (C1)  │ 1-2 nodes       │ 3-4 visible     │ 1-2      │
  │                    │                 │ (compiled deep) │ nodes     │
  ├────────────────────┼─────────────────┼─────────────────┼───────────┤
  │ PFC role           │ Minimal/none    │ Director (high) │ Chọn trust│
  │                    │                 │ qua nhiều năm   │ + post-hoc│
  ├────────────────────┼─────────────────┼─────────────────┼───────────┤
  │ Trust role          │ Low/optional   │ Low (self-      │ CỐT LÕI  │
  │                    │                 │ verify via 1A)  │ = gate    │
  ├────────────────────┼─────────────────┼─────────────────┼───────────┤
  │ Speed              │ Fastest         │ Slowest         │ Fast      │
  │                    │ (ms → hours)    │ (years)         │ (install) │
  ├────────────────────┼─────────────────┼─────────────────┼───────────┤
  │ Accuracy           │ Domain-limited  │ Highest         │ Phụ thuộc │
  │                    │ (chỉ experience)│ (calibrated)    │ source    │
  ├────────────────────┼─────────────────┼─────────────────┼───────────┤
  │ Scope              │ Hẹp (personal)  │ Domain-specific │ Rộng nhất │
  │                    │                 │                 │(all human)│
  ├────────────────────┼─────────────────┼─────────────────┼───────────┤
  │ Vulnerability      │ Personal bias   │ Domain lock-in  │ Collective│
  │                    │                 │                 │ chain gãy │
  ├────────────────────┼─────────────────┼─────────────────┼───────────┤
  │ Verify mechanism   │ Direct body     │ Domain feedback │ KHÔNG     │
  │                    │ feedback (1A)   │ (1A repeated)   │ (trust    │
  │                    │                 │                 │ bypass)   │
  └────────────────────┴─────────────────┴─────────────────┴───────────┘


  ⚠️ LƯU Ý QUAN TRỌNG VỀ ~90%/~5%:

    Số liệu ƯỚC LƯỢNG, không chính xác.
    "~90% Loại A" = PHẦN LỚN behavior hàng ngày là direct compiled.
    NHƯNG: Loại C OVERLAP với Loại A ở nhiều behavior:
      [ăn ngon → ấm] = Loại A (direct)
      NHƯNG "ngon" = partially Loại C (cultural definition of "ngon")
    → Ranh giới A/C KHÔNG binary → SPECTRUM.
    → ~90% + ~5% + C = KHÔNG cộng thành 100% vì overlapping.

  🟡 Percentage estimates: framework approximation, not precise measurement
```

---

## §3 — 4 Compile Pathways: Cùng Output, Khác Cơ Chế

```
🟡 4 PATHWAYS — TEST CASE: "CÙNG LÀ HỌC SINH ĐI HỌC TOÁN" (Drill §22A):


  VP §4 mô tả chain: [toán → điểm → đại học → việc → lương → body-base]
  = CẤP 3 analysis (explanatory, VP v1.4 §4 clarification).
  ĐÚNG nhưng KHÔNG phải cách brain process ở CẤP 1.

  THỰC TẾ — 4 đứa trẻ, 4 compile pathways KHÁC NHAU:


  ① HARDWARE FIT (Loại A — direct short):

     [toán → brain fire → Goldilocks zone → VTA → opioid]
     = "Tự thấy thú vị." CẤP 1 direct.
     Trust: KHÔNG CẦN. Body verify trực tiếp.
     Chain length individual: 1 node.
     PFC accuracy: ~90% ("tôi thích toán" = đúng).

     Novelty.md: Goldilocks zone = task difficulty ≈ current capacity
     → VTA fire → dopamine (salience) → body pursue → opioid (reward)
     → = Hardware fit. Không phải "thông minh" hay "có năng khiếu bẩm sinh"
     → = Chunk system phù hợp + domain → Goldilocks → reward


  ② TRUST + MODERATE FIT (Loại C — installed + verified):

     Bố mẹ nói "học quan trọng" → trust → compile [học → tốt]
     + Tự học → hợp hardware → cost vừa phải → status trên lớp
     = CẤP 1: [học → mẹ khen + điểm + status → body ấm] (2 nodes)
     = CẤP 2: bố mẹ hold chain dài [học → tương lai → body-base]
     Trust: HIGH (bố mẹ). Verify: PARTIAL (tự trải nghiệm confirm).

     → COMPOUND: Loại C (trust install) + Loại A (direct verify)
     → = Phổ biến nhất? Nhiều học sinh = MIX pathway ①②


  ③ SOCIAL DEFAULT (Loại C — installed pure):

     "Thấy ai cũng đi học → đương nhiên mình cũng đi"
     = VP §3 ③ schema inheritance từ cộng đồng
     = CẤP 1: [mọi người đều học → bình thường → tôi cũng] (1 node)
     Trust source: QUANTITY (social proof — Cialdini 1984)
     Không cần hardware fit. Không cần chain logic.

     → Drill §4 bước 1: trust source = tập thể (consensus trust)
     → = "Compile" thậm chí KHÔNG CẦN body experience mạnh
     → Chỉ cần social environment → body auto-conform


  ④ THREAT AVOIDANCE (Loại A — direct short):

     [không học → mẹ mắng / bị đánh → L0 threat → học để avoid]
     = CẤP 1 direct. Chain length: 1-2 nodes.
     PFC accuracy: ~90% ("tôi học vì sợ bị mắng" = đúng mechanism).
     Trust: KHÔNG CẦN (direct threat experience).

     → Chunk.md §2.4: threat direction → compile WITH avoidance association
     → = Cortisol-tagging: compiled [không học → nguy hiểm]
     → = Approach vs avoidance: CẢ HAI Loại A, khác DIRECTION


  ⭐ HỘI TỤ — 4 PATHWAYS, 1 OUTPUT:

     4 pathways KHÁC NHAU → cùng output: "đi học"
     TẤT CẢ compile SHORT ở CẤP 1 (1-2 nodes)
     Chain DÀI [toán → ... → body-base] NẰM Ở CẤP 2 (collective)
     VP §4 GIẢI THÍCH (CẤP 3) tại sao TẤT CẢ đều đi học

     → "Trưởng thành vẫn có công việc (hầu hết)" =
        CẤP 2 (collective infrastructure) HOLD chain dài cho cá nhân
     → Individual chỉ cần trust + compile short → collective deliver kết quả


  GIÁ TRỊ THỰC CỦA 4 PATHWAYS:

    ① Hiểu tại sao CÙNG hành vi = KHÁC mechanism
       → Can thiệp giáo dục CẦN biết học sinh đi theo pathway nào
    ② Pathway ④ (threat) = compile tốt nhưng cortisol cost CAO
       → Chunk.md §2.4: threat direction → neural wear compounds
    ③ Pathway ①② = sustainable hơn (approach direction)
       → Giáo dục TỐT = tạo điều kiện cho pathway ①② thay vì ④
    ④ PFC accuracy THAY ĐỔI theo pathway:
       ① ~90% (direct). ② ~60% (mix). ③ ~30% (social). ④ ~90% (direct).
       → Pathway ③ = PFC confabulate NHIỀU NHẤT

  🟡 4 compile pathways model: framework synthesis (Drill §22A)
  🟢 Social proof: Cialdini 1984
  🟢 Approach vs avoidance motivation: Elliot 2006

  🟡 REWARD IMPLICATION (v1.1 — Reward-Signal-Architecture.md §8.4):
    4 pathways tạo DIFFERENT P5 tags → khác reward capacity ở người lớn:
    → ① HW Fit → approach tag → Profile ② coherence NATURAL, flow accessible
    → ② Trust + moderate → moderate approach → depends on collective chain
    → ③ Social Default → neutral tag → Profile ④ relief dominant ("xong rồi" > "hay")
    → ④ Threat Avoidance → avoidance tag → Profile ④ relief ONLY, burnout trajectory
    → Chi tiết: Reward-Signal-Architecture.md §8.4 (4-Pathway × P5 Tag Model)
```

---

## §4 — Trust-to-Compile: 5 Bước

```
🟡 LOẠI C COMPILE QUA 5 BƯỚC CỤ THỂ (Drill §4):


  ⭐ NGUYÊN TẮC CỐT LÕI:

    Compile ≠ "PFC hiểu rồi nạp vào não"
    Compile = "Body nhận experience từ trusted source → vô thức tự wire"


  BƯỚC 1 — SOURCE ĐÁNG TRUST TỒN TẠI:

    5 dạng trust source (Chunk.md §2.3, Drill §4):

    ① Mẹ / caregiver: FOUNDATIONAL trust
       → Repetition CỰC CAO + multi-modal + sleep
       → = Compile SÂU NHẤT (trust ĐẦU ĐỜI)

    ② Thầy/cô: DELEGATED trust
       → Mẹ trust thầy → con OBSERVE mẹ trust → con trust thầy
       → = Trust INHERIT (không phải verify trực tiếp)

    ③ Tập thể: CONSENSUS trust
       → "Mọi người đều làm vậy" = social proof → trust auto
       → = Quantity install ("ai cũng nói thế → chắc đúng")

    ④ Kinh sách / hệ thống: COMPILED trust
       → Hàng ngàn năm tối ưu → unfalsifiable → KHÔNG BAO GIỜ bị challenge
       → = Deepest installed chains (Religion.md §2.1)

    ⑤ Lãnh đạo: L2 COUPLING trust
       → Body-Coupling.md §2: L2 extend → agent = body-base extension
       → Trust THROUGH coupling, không chỉ qua logic


  BƯỚC 2 — BODY NHẬN INPUT TỪ SOURCE ĐÁNG TRUST:

    KHÔNG phải PFC chain logic "tại sao phải làm thế"
    MÀ LÀ body nhận experience: nhìn, nghe, làm cùng, cảm xúc
    = Multi-modal compile (Chunk.md §2.1 ③)

    VD: Trẻ KHÔNG nghe mẹ giải thích chain [học→đại học→việc→lương]
    Trẻ THẤY mẹ khen khi làm bài, CẢM ấm, NGHE giọng vui
    → Multi-modal input → body compile [làm bài → ấm]


  BƯỚC 3 — PATTERN COMPILE VÀO B+C ZONES:

    KHÔNG qua PFC deliberate linking
    MÀ QUA vô thức compile tự động (~95% — PFC-Function §8)
    = Hebbian LTP: neurons fire together → wire together
    = Trust tag trên source → AMPLIFY compile rate (VP §2)


  BƯỚC 4 — BODY HÀNH ĐỘNG THEO COMPILED PATTERN:

    TỰ ĐỘNG, không cần PFC chain lại mỗi lần.
    VD: tín đồ cầu nguyện, học sinh đi học, chiến sĩ sẵn sàng
    = Compiled pattern fire → body respond → action xuất hiện
    = PFC KHÔNG tham gia quá trình fire


  BƯỚC 5 — PFC TRẢ LỜI (POST-HOC) NẾU AI HỎI "TẠI SAO":

    PFC KHÔNG biết full chain → confabulation (VP §7, PFC-Function §6)
    PFC label ≠ actual mechanism

    VD: "Tại sao bạn đi chùa?"
    PFC: "vì tôi tin Phật" / "vì bình an" / "vì gia đình truyền thống"
    THẬT: trust source (mẹ/cộng đồng) → compile [chùa → ấm] (Loại C)
    + Repetition (đi nhiều lần) → compile deep (Loại A confirm)
    + PFC confabulate "lý do" = label post-hoc, KHÔNG phải mechanism


  ⭐ BƯỚC 5 = KEY INSIGHT:

    "Tại sao tôi làm vậy?" → KHÔNG CÓ 1 ĐÁP ÁN ĐÚNG
    Body compile COMPOUND (nhiều sources), PFC KHÔNG tag nguồn
    → PFC chọn 1 "lý do" → THIẾU toàn bộ compound

    Chunk.md §1.1: NO SOURCE TAG
    → Chunks from trust install = chunks from direct experience = BÌNH ĐẲNG
    → PFC cannot distinguish → confabulate nguồn gốc

  🟡 5-step trust-to-compile model: framework synthesis (Drill §4)
  🟢 Confabulation: Nisbett & Wilson 1977
  🟢 Schema inheritance: established social psychology
```

---

## §5 — PFC = Director, Body = Compiler

```
🟡🟢 "PFC-DIRECTED COMPILE" = THUẬT NGỮ CHÍNH XÁC (Drill §19 — GAP 14):


  ⭐⭐ PFC KHÔNG BAO GIỜ TRỰC TIẾP COMPILE. LUÔN LUÔN.

    PFC-Function.md §6: "PFC KHÔNG THỂ: Compile chunks tự động"
    PFC-Function.md §9: "PFC tạo CONTEXT, B+C+D TỰ HỌC"
    PFC-Function.md ⑬: "PFC imagine → body check → compile nếu ok"


  5 VAI TRÒ CỦA PFC (KHÔNG vai trò nào là compile):

    ① DIRECT ATTENTION (PFC-Function ⑮⑯):
       Chọn CHÚ Ý vào đâu
       → Chunks được chú ý → fire nhiều → body compile mạnh hơn

    ② HOLD IN WM (PFC-Function ⑤⑧):
       Giữ ~4 chunks cùng active
       → Co-fire → Hebbian → body wire together

    ③ IMAGINE (PFC-Function ⑩):
       Simulate scenario bằng chunk combinations
       → Body PHẢN ỨNG với imagination → body compile nếu coherent

    ④ DOMAIN-CHECK (PFC-Function ⑪):
       Verify smooth vs reality (1A vs 1B)
       → KHÔNG compile — verify để body compile ĐÚNG HƯỚNG

    ⑤ CHANGE ENVIRONMENT (PFC-Function ⑳):
       Thay đổi context → body-input thay đổi → body compile KHÁC

    → PFC = 5 việc. Body = compile. Luôn luôn.


  IMAGINATION = NỘI BỘ BODY EXPERIENCE (key insight):

    PFC-Function ⑩: "body reacts to imagination"
    → Imagine chanh → nước bọt THẬT
    → Imagine chó cắn → tim đập THẬT
    → Imagine giải bài → opioid THẬT (nhẹ hơn real, nhưng THẬT)

    = Imagination = body experience (internal, KHÔNG phải external)
    = CÙNG pathways, CÙNG molecules, khác INTENSITY
    = Ranh giới "PFC create vs body compile" KHÔNG TỒN TẠI
    = PFC direct + body compile = always collaborative, never separate


  3 GIỚI HẠN IMAGINATION COMPILE (so với direct experience):

    ① Multi-modal NGHÈO hơn:
       Imagine lửa: visual (mờ) + heat (rất nhẹ)
       Touch lửa: visual (rõ) + heat + pain + smell = RICH
       → Direct = compile SÂU + NHANH hơn imagination

    ② 1B RISK (self-referencing):
       Imagination alone = test chunks against EXISTING chunks (1B)
       Direct experience = test chunks against REALITY (1A)
       → Imagination CÓ THỂ consistent với SELF mà SAI với DOMAIN
       → CẦN domain feedback: peer review, experiments, real results

    ③ Intensity THẤP hơn:
       Imagine vui → opioid nhẹ. THẬT SỰ vui → opioid MẠNH.
       → Imagination compile = CHẬM hơn, cần LẶP NHIỀU hơn


  KHI NÀO IMAGINATION COMPILE ĐỦ:

    KHẢ THI (abstract domains):
      Toán: equations + logic → imagination-mediated compile
      Vật lý lý thuyết: thought experiments + peer review
      Tôn giáo: imagination + ritual + community reinforce
      Philosophy: concepts + argumentation + body evaluate coherence

    KHÔNG ĐỦ (embodied domains):
      Piano: CẦN motor + auditory + tactile = multi-modal DIRECT
      Thể thao: CẦN proprioception + timing + body-feedback THẬT
      Tình yêu/L2: CẦN bidirectional interaction (real agent respond)
      Nấu ăn: CẦN taste + smell + texture = body channels THẬT


  SPECTRUM — TỪ "THUẦN BODY" TỚI "PFC-DIRECTED":

    Thuần body (PFC ≈ 0%): bé bú mẹ, phản xạ rụt tay, Pavlov's dog
    PFC thấp (direct only):  trẻ chơi đất nặn, routine tập thể dục
    PFC trung bình (hold):   học sinh làm toán, thợ mộc kỹ thuật mới
    PFC cao (imagine+check):  nhà văn, kỹ sư, Einstein (Loại B)

    ĐẶC ĐIỂM CHUNG: actual compilation = LUÔN body
    PFC CAO = body được DIRECT tốt hơn, KHÔNG phải PFC compile nhiều hơn

    = Loại A: thuần body → PFC thấp (spectrum trái)
    = Loại B: PFC trung bình → PFC cao (spectrum phải)
    = Loại C: PFC ~ chọn trust ai (vai trò khác: gate, không direct)


  ⭐ TERMINOLOGY CHÍNH THỨC (GAP 14 RESOLVED):

    ❌ "PFC compile" = SAI (PFC không compile)
    ❌ "Brain process chain dài" = SAI (PFC 4±1 limit)
    ✅ "PFC-directed body compile" = Loại B = thuật ngữ CHÍNH XÁC
    ✅ "Trust-gated body compile" = Loại C = thuật ngữ CHÍNH XÁC
    ✅ "Direct body compile" = Loại A = thuật ngữ CHÍNH XÁC

  🟢 PFC from birth online: Hodel 2018 (5 empirical pillars)
  🟢 Motor imagery → body response: Jeannerod 2001
  🟢 Mental simulation → physiological response: established (e.g., salivation)
  🟡 Director/compiler distinction: framework synthesis (Drill §19)
  🟡 Imagination = internal body experience: framework synthesis
```

---

## §6 — 6 Trade-offs Của Compile Ngắn

```
🟡 COMPILE NGẮN = DOMINANT MODE VÀ CÓ 6 TRADE-OFFS RÕ RÀNG (Drill §7):


  T1 — NHANH NHƯNG DỄ BỊ LỪA (trust wrong source):

    Compile ngắn + trust = bypass verification
    → Nếu source SAI → compiled SAI → body hành động theo pattern sai

    Ví dụ:
      Bố mẹ: "phụ nữ không cần học cao" → trust → compile SÂU
        → 30 tuổi: body compiled [học = không cần] → KHÓ thay đổi
      "Đầu tư bitcoin = giàu" (nhiều người nói) → social trust giả → mất tiền
      Cult: install chain qua trust → compile SÂU → weaponized trust

    Root cause: Loại C bypass verification VÌ trust = gate.
    Trust ĐÚNG → compile đúng → tiết kiệm. Trust SAI → compile sai → tốn kém.

    🟢 Cult persuasion: Cialdini 2006


  T2 — PFC KHÔNG THỂ SELF-CORRECT (confabulation):

    PFC explain post-hoc → label ≠ mechanism → fix SAI CHỖ → loop kéo dài

    Ví dụ:
      "Sao tôi cưới người này?" (marriage stress)
        PFC: "bị lừa" / "PFC tính sai"
        THẬT: body compiled [partner → ấm] từ experience
        → Context thay đổi → pattern KHÔNG MATCH → confused

      "Sao tôi học ngành này?" (AI disruption)
        PFC: "xã hội ép" / "không suy nghĩ kỹ"
        THẬT: trust + compile [ngành → việc] vào thời điểm ĐÓ
        → Collective chain GÃY ở [ngành → việc] do AI

    ⭐ Trade-off CHỈ LỘ khi context thay đổi hoặc chain gãy.
    Khi mọi thứ smooth → trade-off này INVISIBLE.

    🟢 Confabulation: Nisbett & Wilson 1977


  T3 — COMPILED PATTERN BỀN HƠN CONTEXT (lag):

    Compile = Hebbian LTP → KHÔNG thể xóa (Chunk.md §2.5)
    → Context thay đổi NHANH → compiled pattern thay đổi CHẬM → LAG

    Ví dụ:
      Code HTML compiled SÂU → HTML obsolete → body VẪN fire "tôi giỏi HTML"
      Chia tay → body VẪN fire [tối → gọi điện partner] → Chunk-Miss
      Di cư → compiled [quê = bình thường] → KHÔNG match environment mới

    Root cause: chunks KHÔNG CÓ cơ chế "unwire" chủ động.
    "Bỏ thói cũ" = chunk MỚI compile ĐỦ MẠNH → ĐÈ chunk cũ (§2.5).
    Trong khi chunk mới chưa đủ mạnh → old pattern VẪN fire.


  T4 — "TẠI SAO TÔI LÀM VẬY?" = KHÔNG CÓ 1 ĐÁP ÁN ĐÚNG:

    Body compile compound (nhiều sources), PFC KHÔNG tag nguồn → confabulation

    Ví dụ:
      "Tại sao muốn sinh con?"
        PFC: "bản năng" / "muốn gia đình" / "mọi người đều làm"
        THẬT: hormone + collective + L2 + identity + meaning = COMPOUND
        → PFC chọn 1 → THIẾU toàn bộ compound

      "Tại sao sợ thay đổi?"
        PFC: "lười" / "thiếu tự tin"
        THẬT: compiled baseline + threat cortisol + Background Pattern
        → PFC label "lười" = MISATTRIBUTE → fix SAI ("cần cố gắng hơn")

    Root cause: NO SOURCE TAG (Chunk §1.1) + confabulation (PFC-Function §6).
    → PFC CÓ THỂ confabulate về cả CẢ 3 LOẠI compile cùng lúc.


  T5 — PHỤ THUỘC COLLECTIVE (collective gãy → individual gánh):

    Loại C compile = individual SHORT + collective LONG
    → Khi collective chain GÃY → individual thiệt hại mà KHÔNG biết tại sao

    Ví dụ:
      Kinh tế suy thoái: [làm việc → lương] GÃY → "tôi đã cố gắng mà sao?"
        → Chain gãy ở collective, KHÔNG phải lỗi cá nhân

      AI disruption: [ngành X → việc X] GÃY → "mình học làm gì?"
        → Context thay đổi → body circuit-break (Body-Base.md §7)
        → PFC wake → hỏi lại lý do → re-evaluate

      Chế độ sụp đổ: [tuân thủ → được bảo vệ] GÃY → existential crisis
        → Chain TOÀN BỘ collapse → Meaning.md anchor disrupted

    Root cause: Loại C = individual KHÔNG hold chain → KHÔNG biết gãy ở đâu.
    → PFC tìm lý do → thường blame MÌNH (vì PFC chỉ thấy Cấp 1).
    → = "Tôi tệ" thay vì "chain collective gãy" = MISATTRIBUTE phổ biến.


  T6 — "BIẾT MÀ KHÔNG LÀM" (PFC logic ≠ compiled pattern):

    PFC chain logic "nên làm X" (Type 4 link) →
    NHƯNG body compiled [KHÔNG X → thoải mái] (Loại A)

    Ví dụ:
      "Biết nên tập thể dục" → body: compiled [sáng → ngủ → thoải mái]
        → PFC chain = LOẠI C (installed). Body = LOẠI A (direct). LOẠI A thắng.

      "Biết cần bảo vệ môi trường" → body: compiled [lái xe → tiện]
        → LOẠI A (direct) > LOẠI C (installed) = vẫn lái xe

      "Biết nên tha thứ" → body: compiled [phản bội → đau → tránh]
        → LOẠI A (emotional peak) >> LOẠI C (verbal install) = không tha

    VP §5 ④: conflicting chains → chain MẠNH HƠN thắng.
    → LOẠI A (multi-modal, direct) THƯỜNG mạnh hơn LOẠI C (verbal install).
    → = Tại sao "biết mà không làm" = PHỔ BIẾN — KHÔNG phải "yếu ý chí."

    Root cause: 2 loại compile cạnh tranh. Loại A > Loại C trong hầu hết cases.
    → CAN THIỆP: chuyển từ LOẠI C (hiểu) → LOẠI A (direct experience)
    → VD: muốn tập thể dục → ĐI TẬP (dù PFC resist) → body compile [tập → ấm]
    → = Body-Base.md §4.2: "PFC-directed compile" = dùng PFC để TẠO BODY EXPERIENCE


  ⭐ 6 TRADE-OFFS = KHÔNG PHẢI BUG, MÀ LÀ FEATURE:

    Compile ngắn + trust = TỐI ƯU cho survival environment:
      Nhanh (ms, không ngày)
      Rộng (access collective knowledge)
      Rẻ (ít cortisol cost)

    Trade-offs = GIÁ CỦA TỐI ƯU HÓA:
      T1: nhanh → dễ lừa
      T2: auto → khó tự sửa
      T3: bền → lag khi context đổi
      T4: compound → PFC confused
      T5: phụ thuộc → collective gãy = gánh
      T6: A > C → "biết mà không làm"

    → Evolution KHÔNG minimize trade-offs
    → Evolution MAXIMIZE survival probability
    → 6 trade-offs = chi phí hợp lý cho compile ngắn dominant mode

  🟡 6 trade-offs framework: drill synthesis (Drill §7)
  🟢 Components individually established (see references above)
```

---

## §7 — Interactions: A vs C, "Biết Mà Không Làm", Chain Break

### §7.1 — Loại A vs Loại C: Khi nào cạnh tranh, khi nào hợp lực

```
🟡 A × C INTERACTIONS (Drill §7 T6 + §22):


  ⭐ HỢP LỰC — khi A confirm C:

    C install [học → tốt] (trust mẹ)
    + A confirm [học → mẹ khen → ấm] (direct experience)
    = COMPOUND STRONG. Cả 2 loại cùng hướng → pattern cực bền.
    = Đây là "educated + enjoy" case. Lý tưởng.


  ⭐ CẠNH TRANH — khi A contradict C:

    C install [rượu → xấu] (trust xã hội)
    + A compile [rượu → vui → ấm] (direct experience party)
    = VP §5 ④: competing chains → chain MẠNH HƠN thắng.
    → A thường thắng (multi-modal, direct) > C (verbal install).
    = "Biết rượu xấu mà vẫn uống."


  ⭐ C OVERRIDE A — hiếm nhưng xảy ra:

    Điều kiện: C install CỰC SÂU + A compile NÔNG.
    VD: Religious prohibition mạnh (trust deep + community reinforce + repeated)
      → Body compiled [rượu → tội] CỰC SÂU qua NHIỀU NĂM
      → Direct experience [rượu → vui] = 1 lần → NÔNG
      → C > A trong case này.

    Hoặc: C + emotional peak:
    Mẹ khóc "con uống rượu mẹ buồn" = emotional peak (Loại A)
      → NHƯNG gắn VỚI C content → reinforced

    → C override A = CẦN: trust deep + repetition + emotional reinforcement
    → = Tại sao education + culture CAN work, nhưng cần THỜI GIAN + INTENSITY


  ⭐ OVERLAPPING — ranh giới mờ:

    [ăn ngon → ấm] = Loại A (direct)
    NHƯNG "ngon" = partially Loại C (cultural: phở ngon, sushi ngon...)
    → Body experience (A) + cultural framing (C) = INTERTWINED
    → Phần lớn adult behavior = A × C overlap, KHÔNG purely 1 loại

  🟡 A × C interaction dynamics: framework synthesis (Drill §7 + §22)
```

### §7.2 — Chain Break: Collective gãy, cá nhân detect

```
🟡 KHI COLLECTIVE CHAIN GÃY — BODY DETECT TRƯỚC PFC (Drill §22B):


  Chain collective: [học → đại học → việc → lương → body-base feed]
  Individual compile: [học → tốt] (trust-gated SHORT — Loại C)

  PFC KHÔNG TỰ NHIÊN SUY NGHĨ "chain gãy."
  BODY circuit-break TRƯỚC → PFC wake SAU (Body-Base.md §7).


  ① COST TĂNG — "Lên lớp cao hơn, mệt hơn":

     Baseline compiled = "học → vừa phải"
     Reality mới = "học → mệt quá" → cost >> baseline
     = Body-Feedback-Mechanism §3 Chunk-Miss:
       VTA negative delta → dissonance signal
     → Body circuit-break: "output KHÔNG feed body-base nữa"
     → PFC wake → "tại sao mệt?" → re-evaluate


  ② LINK GÃY — "Kiến thức không giúp giải quyết thực tế":

     Collective chain GÃY ở link [đại học → việc TỐT]
     = VP §5 ②: chain trust ≈ product of trust at each link
     → Link [đại học → việc] trust COLLAPSE → toàn bộ chain ẢNH HƯỞNG
     → "Học vô ích" = chain đứt → valence "học" FLIP negative


  ③ COMPOUND — nhiều dissonance cùng lúc:

     Cost TĂNG (①) + link GÃY (②) + trust COLLAPSE
     = Body-Feedback-Mechanism §4 COMPOUND: multiple dynamics × intensity
     → PFC wake MẠNH → "học làm gì" = PFC RE-EVALUATE toàn bộ chain


  ⭐ KEY INSIGHT:

    "Học làm gì" KHÔNG phải PFC tự phát suy nghĩ triết học.
    = Body circuit-break TRƯỚC → PFC wake → PFC TÌM lý do.
    = Collective chain GÃY → individual body DETECT → PFC engage.
    = Individual KHÔNG biết gãy ở ĐÂU (vì KHÔNG hold chain)
    → PFC thường blame MÌNH thay vì detect collective chain break.
    → T5 trade-off in action.

  🟡 Chain break detection model: framework synthesis (Drill §22B)
  🟢 Circuit breaker concept: established neuroscience (NE α1 disconnect)
```

### §7.3 — Loại B × External Tools: Cấp 2 cá nhân

```
🟡 LOẠI B EXTEND QUA EXTERNAL TOOLS (Drill §22E):


  EINSTEIN MODEL:

    ① WRITE DOWN = external memory
       PFC hold 4 → viết ra giấy → PFC freed → hold 4 tiếp
       = EXTERNAL STORAGE mở rộng PFC capacity

    ② TRUST PAST SELF
       "Công thức X tôi đã kiểm chứng tuần trước" → trust tag {+++}
       → PFC KHÔNG re-verify X → use X as compiled chunk
       → Build on top of X → recursive compile

    ③ ITERATIVE RECURSIVE
       Verify part A → trust A → build B → verify B → trust B → stack
       = Mỗi bước: PFC hold ≤4. Body verify. Trust. Stack.

    ④ SLEEP CONSOLIDATE giữa các bước
       Each sleep cycle = compression (Type 3 meta-chunk)


  HIERARCHY:
    PFC 4±1 (hardware limit)
    → ×4 pyramidal compression (vô thức compile — VP §5b)
    → ×∞ external tools (giấy, máy tính, database, AI)

  → External tools = "Cấp 2 cá nhân" (Collective-Body.md §3.3)
  → MỞ RỘNG individual compile BEYOND hardware limit
  → WHY civilization accelerates: mỗi thế hệ tạo tools tốt hơn
    → Individual capacity TĂNG → create MORE tools → compound loop

  🟢 Extended mind thesis: Clark & Chalmers 1998
  🟢 Epistemic actions: Kirsh & Maglio 1994
  🟡 "Cấp 2 cá nhân" model: framework synthesis (Drill §22E)
```

---

## §8 — Honest Assessment

```
🟢 ESTABLISHED (strong research support):

  PFC ~4±1 working memory limit (Cowan 2001)
  PFC response slower than subcortical (LeDoux 1996)
  Cortisol cost of sustained cognitive load (Lupien 2009)
  Hebbian learning: fire together wire together (Hebb 1949)
  No chunk deletion: reconsolidation window only (Nader 2000)
  Expert patterns 50,000+: (Chase & Simon 1973)
  Neural efficiency: experts fire less (Haier 1992, Neubauer & Fink 2009)
  Deliberate practice: ~10 years to expert (Ericsson 1993)
  Confabulation as rule: (Nisbett & Wilson 1977)
  Social proof: (Cialdini 1984)
  Cultural transmission: (Boyd & Richerson 1985)
  Extended mind: (Clark & Chalmers 1998)


🟡 FRAMEWORK SYNTHESIS (logic consistent, dựa trên established mechanisms):

  3 Loại Compile taxonomy (A/B/C):
    → Novel organization. Components individually established.
    → ~90%/~5% estimates = approximations, not precise measurement.

  4 Compile Pathways model:
    → Novel: 4 pathways = specific framework insight.
    → Components = combinations of established mechanisms.

  5-step Trust-to-Compile model:
    → Novel formalization. Steps individually established.

  Director/Compiler distinction:
    → Novel naming. PFC-Body relationship = established.
    → "PFC-directed body compile" = new terminology for known relationship.

  6 Trade-offs framework:
    → Novel organization. Each trade-off = established phenomenon.
    → T6 "biết mà không làm" = testable: Loại A > Loại C strength.

  PFC accuracy per pathway (§3):
    → Speculative estimates (90%/60%/30%/90%). Needs testing.


🔴 NEEDS MORE RESEARCH:

  Precise % breakdown across Loại A/B/C (currently approximations)
  Quantitative trust threshold for Loại C compile
  Cross-cultural variation in 4 compile pathways distribution
  Whether Loại C → Loại A conversion rate can be measured
  Neural signature differences between A/B/C compile
  Whether 4 pathways are exhaustive or if more exist
```

---

## §9 — Cross-References

```
CORE FRAMEWORK FILES:

  Chunk.md v2.1 §2 — 4 compile mechanisms = FOUNDATION for 3 Loại
  Chunk.md v2.1 §2.3 — External install + Trust gate (GAP 6 resolved)
  Chunk.md v2.1 §1.1 — No Source Tag (GAP 8 resolved)
  Body-Base.md v2.0 §4 — Summary 3 Loại (reference tới file này)
  VP v1.4 §4 — Clarification: VP chains = explanatory (GAP 13 resolved)
  VP v1.4 §5b — 4 tầng cơ chế chain dài
  PFC-Function.md v1.1 §6 — Confabulation principle (GAP 10 resolved)
  PFC-Function.md v1.1 §9 — "PFC tạo context, B+C+D tự học"
  PFC-Function.md v1.1 §4 — PFC Proxy Trigger (GAP-C5 resolved)
  Blackbox-Map.md — 5 gaps + 2 complexity dimensions (supersedes Framework-Boundaries.md)
  Collective-Body.md v1.0 §2 — 4 compile pathways × 3 cấp


BODY-BASE + BODY-FEEDBACK FILES:

  Body-Base.md v2.0 §7 — Circuit Breaker mechanism
  Body-Feedback-Mechanism.md §3 — Chunk-Miss (chain break detection)
  Body-Feedback-Mechanism.md §4 — Compound dynamics
  Cortisol-Baseline.md v2.0 — Sustained cortisol → neural wear
  Background-Pattern.md v1.0 — Background Pattern as Loại A deep compile


OBSERVATION FILES:

  Meaning.md v2.0 — Anchor disrupted = T5 chain break × identity
  Religion.md v2.0 §2.1 — External inject bypass PFC = Loại C mechanism
  Status.md v2.0 — Resource Access Map = Loại A (evolutionary direct)


DRILL SOURCE (read-only reference):

  Drill-Compile-Short-Collective.md §2 — 3 hardware constraints
  Drill-Compile-Short-Collective.md §3 — 3 Loại A/B/C core
  Drill-Compile-Short-Collective.md §4 — Trust-to-compile 5 bước
  Drill-Compile-Short-Collective.md §7 — 6 trade-offs
  Drill-Compile-Short-Collective.md §19 — PFC = director, body = compiler
  Drill-Compile-Short-Collective.md §22 — 4 pathways + BB2 reframe
  Drill-Compile-Short-Collective.md §5 — Model 3 cấp


PFC DETAIL FILES:

  PFC-Hold-Dimensions.md — 6 lực hội tụ tại 4±1
  PFC-Hardware.md — Individual variance (COMT, DRD4, NE)
  PFC-Development.md — PFC online from birth (5 pillars)
```
