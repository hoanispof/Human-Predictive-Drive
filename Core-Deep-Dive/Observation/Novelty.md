---
title: Novelty — Observation Parameter
version: 1.2
created: 2026-04-20
updated: 2026-05-17
refined: 2026-05-23 (v1.2 — Concept Cascade: +Simulation-Engine, +Satiation types, +PFC Budget. Updated versions + cross-refs)
status: OBSERVATION PARAMETER v1.2
scope: |
  OBSERVATION FILE: Novelty = named pattern khi quan sát chunk dynamics.
  Novelty không phải component hay operator — là TÊN GỌI cho patterns
  emergent từ VTA detect positive prediction-delta + chunk-gap dynamics.
  File này mô tả: mechanism, 2 dạng, phanh, loop, depth/breadth, ứng dụng.
  v1.1 KEY CHANGES:
    ⑪ +Compilable Architecture: novelty = general-purpose system detect UNCOMPILED input
    ⑫ +Compiled/Fresh: novel = BY DEFINITION fresh (not yet compiled)
    ⑬ +2-tầng calibration: what counts as "novel" = per-individual
    ⑭ Version refs synced (Valence-Propagation v2.0, Body-Feedback-Mechanism v2.0, Feeling v3.0)
    ⑮ +Cross-refs: Inter-Body-Mechanism.md v1.0, Body-Feedback-Label.md v2.0
purpose: |
  Core v7.8 §8 define Novelty ngắn gọn ("Positive prediction-delta pattern").
  File này DEEP-DIVE: neuroscience mechanism, practical patterns,
  khi nào có lợi/có hại, loop dynamics. Dùng cho người cần hiểu chi tiết.
position: |
  Core-Deep-Dive/Observation/ — ngang hàng Schema.md, Empathy.md,
  AI-Schema-Detection.md, Liking-Wanting.md, Threat.md, Drive.md.
  Tất cả = observation parameter deep-dives, KHÔNG phải mechanism files.
dependencies:
  - Core-v7.8-Draft.md — cycle architecture, §8 observation parameters
  - Body-Feedback-Mechanism.md v2.0 — Chunk-Gap = foundation, Shift/Miss/Gap
  - Chunk.md v2.0 — chunk substrate, compilation, hierarchy
  - Cortisol-Baseline.md v2.0 — amplifier, sustained cortisol dynamics
  - Valence-Propagation.md v2.0 — body evaluation, delta rule
  - Modality.md v1.0 — encoding channels, depth = modality count
  - Feeling.md v3.0 — PFC observation interface
  - Somatic-Articulation-Loop.md — implicit >> explicit, felt sense
  - Inter-Body-Mechanism.md v1.0 — Compilable Architecture, Compiled/Fresh
  - Body-Feedback-Label.md v2.0 — vocabulary reference
  - PFC/Simulation-Engine.md v1.0 — novelty = prediction mismatch in simulation
  - Body-Feedback/Gap-Body-Need.md v1.0 — novelty satiation dynamics
  - PFC/PFC-Label.md v1.0 — vocabulary, PFC budget limit on novelty seeking
sources_backup: |
  Gộp + rewrite từ: Novelty.md v1.0 (1,225L) + Novelty-Loop.md (1,060L)
  Backup: _backup/Drive-v75-era/
language: Tiếng Việt primary + English technical terms
confidence: 🟢 Research support | 🟡 Framework synthesis | 🔴 Hypothesis
---

# Novelty — Observation Parameter

> Khi nhìn một đứa trẻ đuổi theo con cua, một nhà vật lý trăn trở suốt đêm,
> hay một người cuộn MXH không dừng được — chúng ta gọi tất cả là "Novelty."
>
> Nhưng bên trong, không có module nào tên "Novelty."
> Chỉ có: chunks fire → VTA detect delta → body-feedback → behavior emerge.
>
> Novelty là TÊN GỌI cho pattern đó — nhìn từ bên ngoài.
>
> File này mô tả: pattern đó trông thế nào, mechanism bên dưới,
> khi nào nó tự dừng, khi nào nó không dừng được, và tại sao điều đó quan trọng.

---

## Mục lục

- §0 — NOVELTY LÀ OBSERVATION PARAMETER
- §1 — MECHANISM: VTA + CHUNK DYNAMICS
- §2 — 2 DẠNG: SENSORY-DRIVEN vs IMAGINATION-DRIVEN
- §3 — 3 PHANH TỰ NHIÊN + KHI PHANH THẤT BẠI
- §4 — NOVELTY LOOP: KHI KHÔNG TỰ DỪNG
- §5 — DRD4: DEPTH vs BREADTH
- §6 — KHI CÓ LỢI vs KHI CÓ HẠI
- §7 — HONEST ASSESSMENT
- §8 — CROSS-REFERENCES

---

## §0 — NOVELTY LÀ OBSERVATION PARAMETER

```
⭐ REFRAME V7.8:

  Core v7.5 (cũ): Novelty = "L3 Pattern drive" — 1 trong 3 drives xã hội
  Core v7.8 (mới): Novelty = observation parameter — tên gọi cho pattern

  Novelty KHÔNG PHẢI:
    ✗ Component kiến trúc (không có "Novelty module" trong não)
    ✗ Drive operator (không có "Novelty engine" bật/tắt)
    ✗ Layer riêng (không có "L3 Novelty" — layer-model đã bỏ)
    ✗ Personality trait "tò mò" (pop psychology — mô tả, không giải thích)

  Novelty LÀ:
    ○ Tên gọi cho pattern observable: khi VTA detect positive prediction-delta
    ○ Emergent từ chunk dynamics — đặc biệt Chunk-Gap (§1)
    ○ Giá trị: predict, communicate, diagnose
      → "Người này thích novelty" = predict xu hướng hành vi
      → "Anh ấy đang trong novelty loop" = communicate trạng thái
      → "Thiếu novelty drive" = diagnose (boredom territory)
    ○ KHÔNG dùng để thiết kế can thiệp — can thiệp ở level mechanism:
      thay đổi body-input, compile chunks mới, adjust environment

  ANALOGY:
    "Novelty" giống "nhiệt độ" trong vật lý:
    → Không có particle nào tên "nhiệt độ"
    → Nhiệt độ = TÊN GỌI cho mức độ rung của các phân tử
    → Hữu ích: predict (sẽ sôi ở 100°C), communicate ("nóng quá!"), diagnose ("sốt")
    → Can thiệp: KHÔNG "thêm nhiệt độ" — mà thêm/bớt năng lượng cho phân tử

    Tương tự:
    → Không có neuron nào tên "novelty"
    → Novelty = TÊN GỌI cho VTA detect delta trong chunk network
    → Hữu ích: predict, communicate, diagnose
    → Can thiệp: KHÔNG "thêm novelty" — mà tạo environment có delta,
      hoặc compile chunks mới (combinatorial space)


⭐ COMPILABLE ARCHITECTURE → NOVELTY CẦN THIẾT (Inter-Body-Mechanism.md §1.2):

  HARDWIRED ARCHITECTURE (côn trùng, động vật đơn giản):
    Stimulus→Response HARDWIRED. Không cần "detect mới" — MỌI response CỐ ĐỊNH.
    Con ong: hoa→bay tới. Không có "tò mò" — chỉ có circuit.
    → KHÔNG CÓ "Novelty" vì KHÔNG CÓ prediction → không có delta.

  COMPILABLE ARCHITECTURE (humans):
    General-purpose reward system: LEARN content from environment.
    Content KHÔNG hardwired → phải DETECT: "input nào CHƯA compile?"
    → VTA = detector cho "UNCOMPILED INPUT" trong general-purpose system.
    → Novelty = signal "có input CHƯA TRONG BASELINE — attend + process."
    → = Compilable Architecture's MECHANISM để liên tục UPDATE world model.

  → Novelty = ARCHITECTURE REQUIREMENT cho general-purpose learning.
  → Không có novelty detection → Compilable Architecture không update → chết.

  🟡 Compilable Architecture framing = framework synthesis (Inter-Body-Mechanism.md §1.2).


NOVELTY TRONG CYCLE (Core v7.8 §1):

  Domain → Body-Input → Unconscious(Chunks) → Feeling → PFC → Body-Output → Domain
                              ↑
                      VTA detect delta ở đây
                      = "Novelty" được quan sát

  Novelty xuất hiện ở bước Unconscious Processing:
  → Chunks fire → VTA compare với baseline → delta > 0
  → Body-feedback fire (reward direction nếu positive delta)
  → Feeling bridge → PFC observe → có thể label "thú vị", "hay", "tò mò"
  → PFC có thể orchestrate → explore → body-output → domain → loop

  = Novelty KHÔNG PHẢI 1 bước riêng — mà là observation point
    trong cycle liên tục


GIÁ TRỊ CỦA FILE NÀY:

  Core v7.8 §8 chỉ nói: "Novelty = Positive prediction-delta pattern."
  File này DEEP-DIVE:
  → §1: Mechanism — VTA + chunk dynamics (neuroscience)
  → §2: 2 dạng — Sensory-Driven vs Imagination-Driven
  → §3: 3 phanh — tại sao tự dừng (hoặc không)
  → §4: Loop — khi phanh thất bại → vòng xoáy sáng tạo
  → §5: DRD4 — depth vs breadth (hardware variation)
  → §6: Lợi vs hại — cùng mechanism, khác output
```

---

## §1 — MECHANISM: VTA + CHUNK DYNAMICS

```
⭐ NOVELTY = VTA DETECT POSITIVE PREDICTION DELTA TRONG CHUNK NETWORK

  2 thành phần CỐT LÕI:
    ① VTA (Ventral Tegmental Area) — bộ phận detect
    ② Chunk dynamics — substrate tạo ra delta

  Cả 2 CẦN THIẾT. Thiếu 1 = không có Novelty:
    → VTA có nhưng chunks không thay đổi = VTA im lặng
    → Chunks thay đổi nhưng VTA hỏng = không detect được delta


§1.1 — VTA: "SEISMOGRAPH" CỦA NÃO

  VTA (Ventral Tegmental Area):
    → ~400,000 neurons ở midbrain (zona C subcortical)
    → Chức năng: detect DELTA (biến động), KHÔNG detect absolute values
    → = "Seismograph" — đo RUNG CHẤN, không đo độ cao mặt đất

  Cơ chế:
    → Chunks compile → fire pattern ỔN ĐỊNH → VTA habituate → IM LẶNG
    → Pattern THAY ĐỔI (chunks mới, tổ hợp mới) → VTA detect → FIRE
    → Trở lại ổn định ở level mới → VTA habituate lại → IM LẶNG

    = "baseline → detect change → fire → new baseline → habituate"

  Prediction delta (thuật ngữ framework):
    → Thay cho "prediction error" (Schultz 1997):
      → Cùng cơ chế — nhưng "error" gợi ý "sai", trong khi delta = TRUNG TÍNH
      → Delta > 0 (positive): pattern mới/mở rộng → Novelty direction
      → Delta < 0 (negative): pattern tệ hơn expected → Dissonance direction
      → Delta = 0: đúng expected → VTA im → no signal
    → Body-Feedback-Mechanism.md: Chunk-Miss = negative delta (§3.2)

  VTA fire → dopamine production (tyrosine → L-DOPA → dopamine):
    → Dopamine travel qua axons (cable VẬT LÝ, hình thành từ thai nhi, CỐ ĐỊNH)
    → Chỉ LƯỢNG dopamine thay đổi, không phải topology kết nối
    → Dopamine bind vào DRD4 receptors trên PFC neurons
    → = Signal "có gì đó MỚI — attend"

  ⭐ NOVELTY = BY DEFINITION FRESH (Inter-Body-Mechanism.md §3):

    Compiled/Fresh = trục thật của processing:
      Compiled = automatic, body-feedback direct, cost ≈ 0
      Fresh = PFC draft, deliberate, cost > 0

    → Novelty signal = "input NÀY chưa compiled" = BY DEFINITION fresh.
    → VTA fire = signal "SWITCH TO FRESH PROCESSING MODE."
    → PFC phải attend, draft, evaluate — cost > 0.

    Khi pattern compile xong:
      → VTA habituate → delta = 0 → novelty signal TẮT.
      → Processing chuyển Fresh→Compiled (fresh→compiled).
      → = "Hết mới" = "đã compile" = cùng 1 sự kiện nhìn từ 2 góc.

    Hệ quả:
      → "Tìm novelty" = "tìm input chưa compiled."
      → Expert có NHIỀU novelty hơn beginner (§1.4) vì:
        combinatorial space lớn → NHIỀU patterns chưa compiled hơn.
      → Education: dạy = cung cấp fresh input → student compile.

  🟢 VTA, dopamine pathway, habituation = neuroscience verified
  🟢 Schultz 1997: reward prediction error (cơ chế đã established)
  🟡 "Prediction delta" (neutral term) = framework terminology choice
  🟡 Novelty=fresh mapping = framework synthesis (consistent with Kahneman)


§1.2 — DRD4 THRESHOLD — FILTER VÔ THỨC

  ⚠️ CLARIFICATION QUAN TRỌNG:

  DRD4 threshold = filter ở VTA→PFC level (VÔ THỨC)
  = "Biến động nào ĐỦ LỚN để BÁO LÊN PFC"

  PFC khi ĐÃ FOCUS = xử lý MỌI chi tiết tinh vi
  → PFC KHÔNG bị giới hạn bởi DRD4
  → PFC bị giới hạn bởi CÁI GÌ ĐƯỢC BÁO VỀ (input filter)

  DRD4 repeat variants (2R → 11R) tạo SPECTRUM:
    → Repeat dài (7R+): threshold CAO → ít signal tới PFC → deep focus
    → Repeat ngắn (4R): threshold THẤP → nhiều signal → broad awareness
    → Chi tiết: §5

  🟢 DRD4 receptor variants = neuroscience verified
  🟡 Threshold → depth/breadth mapping = framework interpretation


§1.3 — CHUNK DYNAMICS NỀN TẢNG CHO NOVELTY

  Body-Feedback-Mechanism.md define 3 chunk dynamics.
  Novelty liên quan TRỰC TIẾP tới Chunk-Gap:

  ⭐ CHUNK-GAP = FOUNDATION CHO NOVELTY
    (Body-Feedback-Mechanism.md §3.3)

    Chunk-Gap = chunk network có HOLES (lỗ hổng) hoặc CONFLICTS (mâu thuẫn)
    → Pattern SHOULD exist nhưng DOESN'T
    → ACC/insula detect inconsistency → body signal "bứt rứt, chưa ổn"
    → Signal drive behavior: tìm, khám phá, giải quyết → fill gap
    → Fill gap → opioid reward

    = Novelty drive EMERGE từ Chunk-Gap dynamics:
    → Khi network detect GAP → body-feedback (dissonance) → drive explore
    → Explore → tìm thấy → fill gap → body-feedback (reward) → VTA fire
    → = "Tò mò" = tên gọi cho Chunk-Gap drive quan sát từ bên ngoài

    ⭐ GAP CÓ HƯỚNG (Gap-Direction.md):
    → Gap direction = f(surrounding chunk network structure)
    → Fill CHỈ reward khi MATCH direction (không chỉ "fill bất kỳ gap")
    → "Chưa biết = không có gap" → desire = f(chunks accumulated)
    → Oscillation: fill → new chunks → detect new gap → more novelty (§7.5)
    → = Novelty drive KHÔNG BAO GIỜ cạn vì mỗi fill = thêm detection power

  CHUNK-SHIFT cũng tham gia:
    → Khi chunks mới compile → valence network re-evaluate
    → Re-evaluation = delta → VTA detect → Novelty signal
    → Ví dụ: học thêm về vật lý → Newton chunks shift valence
      (từ "đúng tuyệt đối" → "đúng trong phạm vi") → delta → drive tìm hiểu thêm

  CHUNK-MISS ở hướng NGƯỢC (negative delta):
    → Pattern đã compile nhưng ABSENT → dissonance, KHÔNG phải novelty
    → NHƯNG: miss CÓ THỂ TRIGGER gap detect:
      "Cái này thiếu rồi... còn thiếu gì nữa?" → Chunk-Miss → Chunk-Gap → Novelty
    → = Miss dẫn tới Gap dẫn tới Novelty (cascade)


§1.4 — COMBINATORIAL SPACE: TẠI SAO EXPERT CÓ NHIỀU NOVELTY HƠN

  Chunks tích lũy → combinatorial space TĂNG:

    Ít chunks (beginner):
      → 10 chunks → ~45 cặp possible
      → Tổ hợp 3: ~120
      → NHANH hết combinations mới → VTA habituate → drive giảm

    Nhiều chunks (expert):
      → 1,000 chunks → ~500,000 cặp possible
      → Tổ hợp 3: ~166 TRIỆU
      → GẦN NHƯ KHÔNG THỂ hết → VTA LUÔN có delta mới

    + Chunks có HIERARCHY (meta-chunks, Chunk.md v2.0):
      → Combinatorial space thực tế CÒN LỚN HƠN nhiều
      → = Tại sao 1 expert CÓ THỂ nghiên cứu 1 domain CẢ ĐỜI

  Hệ quả:
    → "Tò mò" KHÔNG phải trait CỐ ĐỊNH
    → = Output của: chunks tích lũy × gap density × DRD4 threshold
    → Ai cũng CÓ THỂ → nếu tích đủ chunks + gặp đúng domain

  ⭐ 2-TẦNG CALIBRATION — "MỚI" = PER-INDIVIDUAL:

    Cái gì "mới" KHÔNG phải absolute — phụ thuộc BASELINE CỦA NGƯỜI ĐÓ:
      → Beginner: mọi thứ mới (baseline ít chunks) → VTA fire LIÊN TỤC
      → Expert: ít thứ mới ở bề mặt (baseline nhiều chunks)
        → NHƯNG: combinatorial patterns mới = delta MỚI ở SÂU HƠN
      → Ví dụ: cùng bài toán → beginner "WOW mới" vs expert "trivial"
      → Ví dụ: cùng cấu trúc toán → expert "WOW connection mới" vs beginner "???"

    2 tầng:
      ① HARDWARE tầng: DRD4 threshold (genetic — ít thay đổi)
      ② CHUNK tầng: chunk library size + gap density (thay đổi theo kinh nghiệm)
    → "Mới" = f(hardware threshold × chunk baseline) = calibrated per person.

  🟢 Combinatorial mathematics = verified
  🟢 Chunk hierarchy + meta-chunks = expertise research (Chase & Simon 1973)
  🟡 "Tò mò = mechanism output" = framework reframe (vs trait theory)
  🟡 2-tầng calibration = framework synthesis


§1.5 — NOVELTY × NEW CONCEPTS (28-session Drill Propagation)

  SIMULATION ENGINE (Simulation-Engine.md v1.0):
    → Novelty = prediction MISMATCH detected in Simulation Engine output
    → PFC simulate expected pattern → body compare actual → delta → novelty
    → Imagination-driven novelty (§2) = Simulation Engine draft WITHOUT external input
    → = Simulation Engine = machinery that GENERATES prediction for VTA to compare

  NOVELTY SATIATION (Gap-Body-Need.md v1.0):
    → Novelty drive có 3 satiation patterns:
      ENGINE: VTA receptor downregulation (dopamine tolerance) — hiếm ở novelty tự nhiên
      ROAD: cùng loại novelty quen → cần loại MỚI (VD: MXH feed lặp lại)
      VEHICLE: entity cụ thể hết novelty (VD: game mới → quen → bored)
    → MXH exploit ROAD satiation: đổi content liên tục → engine KHÔNG BAO GIỜ tắt
    → Expert: ROAD satiation ÍT hơn (combinatorial space lớn → paths luôn mới)

  PFC BUDGET (PFC-Label.md v1.0, Gap-Distribution-Profile.md v1.1):
    → Novelty seeking LIMITED BY PFC budget: processing fresh input = costly
    → PFC budget = finite per-day (metabolic, cortisol, sleep)
    → Quá nhiều novelty → PFC budget exhausted → shutdown → "overwhelmed"
    → = Tại sao novelty CŨNG CẦN phanh — không chỉ threat (§3 below)

  🟡 Simulation Engine × novelty = framework formalization
  🟡 3 satiation types × novelty = framework application
  🟡 PFC budget limit on novelty = framework inference
```

---

## §2 — 2 DẠNG: SENSORY-DRIVEN vs IMAGINATION-DRIVEN

```
⭐ 2 DẠNG NOVELTY — MAPS TRỰC TIẾP VÀO 2 NGUỒN BODY-FEEDBACK:

  Body-Feedback-Mechanism.md §2 define 2 nguồn body-feedback:
    ① Sensory-Driven: domain stimulus → chunks fire REACTIVE
    ② Pattern-Driven: chunks fire NỘI BỘ → body respond

  Novelty observation CÓ 2 DẠNG tương ứng:
    ① Sensory-Driven Novelty: external delta → VTA fire
    ② Imagination-Driven Novelty: internal chunk recombination → VTA fire


═══════════════════════════════════════════════════════
① SENSORY-DRIVEN NOVELTY
═══════════════════════════════════════════════════════

  = Input MỚI từ domain → chunks fire pattern KHÁC baseline → VTA detect

  FLOW (trong v7.8 cycle):
    Domain stimulus → Body-Input (receptors)
    → Unconscious: chunks fire pattern MỚI (khác baseline)
    → VTA detect positive delta → dopamine → DRD4 filter
    → Nếu vượt threshold → PFC attend → explore
    → Explore → chunks tích lũy → pattern quen dần
    → VTA habituate → dopamine GIẢM → dừng

  ĐẶC ĐIỂM:
    → Input từ BÊN NGOÀI — cần domain stimulus liên tục
    → Mọi loài có (VTA + sensory pathways = evolution cổ)
    → TỰ DỪNG nhờ 3 phanh (§3)
    → Cycle ngắn: phút → giờ

  VÍ DỤ — ĐỒ ĂN:
    → Tình huống A: Đồ ăn bình thường
      → Vị quen → prediction-delta NHỎ → ít reward
      → No (body-feedback: satisfaction) → DỪNG
      → Cycle: 10-30 phút

    → Tình huống B: Đồ ăn NGON lần đầu
      → Vị MỚI, texture MỚI → prediction-delta LỚN → dopamine mạnh
      → Body-feedback reward (opioid: pattern match Goldilocks)
      → No → satisfaction → DỪNG (dù còn ngon)
      → = Body satisfaction OVERRIDE novelty reward

    → Tình huống C: Đồ ăn ngon ĂN NHIỀU LẦN
      → Lần 1: WOW. Lần 3: bớt wow. Lần 10: quen.
      → = HABITUATION: cùng input → VTA habituate → delta → 0
      → Vẫn ngon (body-feedback reward còn) nhưng KHÔNG CÒN MỚI (novelty tắt)
      → PHÂN BIỆT: Reward ≠ Novelty
        → Reward = body-feedback khi pattern match tốt (có thể lặp lại)
        → Novelty = VTA detect pattern KHÁC baseline (chỉ khi delta > 0)

  VÍ DỤ — CON CUA TRÊN BÃI BIỂN:
    → Đứa trẻ lần đầu thấy con cua:
      → Hình dạng LẠ → VTA fire. Cua chạy → VTA fire thêm.
      → Mỗi behavior mới → VTA detect → dopamine → tiếp tục.
    → Sau 20-30 phút:
      → ALL behaviors → quen → VTA habituate → delta = 0
      → "Chán" = tên gọi cho VTA habituated + dopamine giảm
      → Quay đi → tìm thứ KHÁC (= tìm delta MỚI)
    → Pattern: Novelty vô thức BOUNDED bởi input depletion
      → Con cua CHỈ CÓ bấy nhiêu behaviors → hết delta → hết novelty

  VÍ DỤ — SCROLL MXH:
    → Tại sao KHÔNG DỪNG ĐƯỢC:
      → Mỗi post = micro-delta MỚI → VTA fire nhẹ
      → KHÔNG habituation: mỗi post KHÁC post trước
      → KHÔNG input depletion: algorithm cung cấp VÔ TẬN
      → = HACK 2/3 phanh tự nhiên (§3)
    → NHƯNG:
      → Mỗi delta RẤT NHỎ → reward RẤT NHỎ
      → Không có chunk TÍCH LŨY (mỗi post = isolated)
      → Body-feedback sau 1-2 giờ: dissonance ("thiếu gì đó")
      → = "Chán mà không dừng được":
        VTA CÒN fire (delta) nhưng body-feedback reward KHÔNG fire (no depth)
    → MXH = exploit Sensory-Driven Novelty:
      loại bỏ habituation + depletion, giữ delta > 0 liên tục nhưng NÔNG

  🟡 Analysis: consistent với observed behavior, derived từ framework


═══════════════════════════════════════════════════════
② IMAGINATION-DRIVEN NOVELTY
═══════════════════════════════════════════════════════

  = Chunks fire NỘI BỘ → tổ hợp mới → VTA detect delta
  = KHÔNG CẦN external input liên tục

  FLOW (trong v7.8 cycle):
    Chunks tích lũy (từ experience, domain exposure)
    → PFC mở workspace → set direction (hoặc vô thức tự recombine)
    → Chunks tổ hợp → pattern mới xuất hiện
    → VTA detect positive delta → dopamine → PFC attend → evaluate
    → Body-feedback respond (reward nếu pattern fit, dissonance nếu chưa)
    → Refine → chunks mới compile → thêm combinations possible
    → VTA detect delta MỚI → cycle TIẾP TỤC

  ĐẶC ĐIỂM:
    → Input từ BÊN TRONG — chunks tự tổ hợp
    → Chủ yếu ở species có PFC mạnh (con người)
    → KHÓ TỰ DỪNG — phanh yếu (§3)
    → Cycle dài: giờ → tháng → NĂM

  SO SÁNH 2 DẠNG:

    ┌──────────────────┬───────────────────────┬───────────────────────┐
    │                  │ Sensory-Driven        │ Imagination-Driven    │
    ├──────────────────┼───────────────────────┼───────────────────────┤
    │ Input source     │ Domain (external)     │ Chunks (internal)     │
    │ Input giới hạn?  │ CÓ (environment)      │ GẦN NHƯ KHÔNG        │
    │ Habituation      │ NHANH (phút→giờ)     │ CHẬM (giờ→năm)       │
    │ Depth            │ NÔNG (per stimulus)   │ SÂU (cross-domain)   │
    │ Chunk tích lũy   │ ÍT (isolated)         │ NHIỀU (connected)     │
    │ Tự dừng?         │ DỄ (3 phanh)         │ KHÓ (phanh yếu)      │
    │ Species          │ Mọi loài (VTA + sens.)│ Chủ yếu con người    │
    │ Body-Feedback src│ Sensory-Driven (§2.2) │ Pattern-Driven (§2.3) │
    │ Ví dụ            │ Đồ ăn, con cua, MXH   │ Einstein, đầu bếp    │
    └──────────────────┴───────────────────────┴───────────────────────┘

  TẠI SAO HABITUATION CHẬM Ở IMAGINATION:
    → Sensory: cua chạy → cua chạy → cua chạy → CÙNG delta → quen
    → Imagine: chunk A+B → insight → chunk C join → KHÁC delta → mới
    → Mỗi lần imagine → chunks TỔ HỢP KHÁC → pattern MỚI
    → VTA detect delta MỚI mỗi lần (không lặp cùng pattern)
    → = "Não tự feed novelty cho chính nó" (Pattern-Driven loop)

  IMAGINE-REWARD-REFINE LOOP:
    Khi chunk network có GAP (Body-Feedback-Mechanism.md §3.3):

    ┌─ Chunk-Gap → body-feedback (dissonance: "chưa ổn") → drive resolve
    │
    ├→ PFC mở workspace → vô thức simulate (chunk recombination)
    ├→ Pattern mới → chunks hội tụ CHÚT ÍT
    ├→ Gap PARTIALLY filled → body-feedback (reward: opioid) → LẬP TỨC
    ├→ VTA detect delta (pattern mới) → dopamine → tiếp tục
    ├→ Refine → pattern tốt hơn → reward nữa
    ├→ ...cycle tiếp...
    │
    └─ = VÒNG TỰ THƯỞNG — rất khó dừng

    Tại sao VÒNG này mạnh:
    → Mỗi bước nhỏ = reward NGAY (không cần chờ hoàn thành)
    → Dissonance GIẢM dần mỗi step
    → NHƯNG mỗi step MỞ RA gap mới
    → = Reward + Delta song song → 2 drives CÙNG kéo
    → = KHÔNG CHỈ "muốn biết" — CÒN "body cần resolve gap"

  CHUYỂN TIẾP: SENSORY → IMAGINATION:
    → 2 dạng KHÔNG tách biệt — có CHUYỂN TIẾP:
    → Sensory → Imagination: thấy cua (sensory) → "tại sao chạy ngang?" (imagine)
    → Imagination → Sensory: imagine "nếu trộn X+Y" → tay tự thử → domain feedback
    → Beginner: nhiều sensory, ít imagine (chưa đủ chunks)
    → Expert: ít sensory (habituate nhanh), nhiều imagine (chunks lớn)
    → = Education: giai đoạn đầu PHẢI cung cấp external input
      → giai đoạn sau DẦN chuyển sang tự imagine

  🟡 2 dạng Novelty mapping vào 2 nguồn Body-Feedback = framework synthesis
  🟢 Expertise → internal generation = expertise research (Ericsson)
```

---

## §3 — 3 PHANH TỰ NHIÊN + KHI PHANH THẤT BẠI

```
⭐ NOVELTY CÓ 3 PHANH BUILT-IN — TẤT CẢ HIỆU QUẢ CHO SENSORY,
  YẾU CHO IMAGINATION:


PHANH ① — HABITUATION (VTA quen)

  Cơ chế:
    → Cùng pattern fire nhiều lần → VTA habituate → delta → 0 → im lặng
    → = Không còn "mới" → không còn signal

  × Sensory-Driven: HIỆU QUẢ
    → Con cua chạy 10 lần → quen → VTA im → dừng quan sát
    → External input LẶP LẠI → delta giảm nhanh

  × Imagination-Driven: YẾU
    → Mỗi lần imagine → chunks tổ hợp KHÁC → pattern MỚI → VTA detect
    → = TỰ TẠO delta mới liên tục → VTA KHÔNG habituate
    → Chỉ habituate khi hết combinatorial space → rất lâu ở expert


PHANH ② — BODY SATISFACTION (nhu cầu đáp ứng)

  Cơ chế:
    → Body-need fulfilled → satisfaction signal fire → DỪNG drive
    → Hormones: leptin (no), insulin (glucose đủ), CCK (gut satiety)

  × Sensory-Driven: HIỆU QUẢ
    → Đồ ăn: ĂN → NO → satisfaction → dừng
    → Du lịch: KHÁM PHÁ → mệt + "thoải mãn" → dừng
    → = Body-need CÓ endpoint → satisfaction REACHABLE

  × Imagination-Driven: YẾU
    → "Hiểu hết vật lý" = KHÔNG BAO GIỜ đạt (domain vô tận)
    → Mỗi gap filled → MỞ RA gaps mới
    → = Body satisfaction cho Imagination Novelty = KHÓ ĐẠT
    → = "Đỉnh núi này → thấy đỉnh núi tiếp" → chưa bao giờ "tới nơi"


PHANH ③ — INPUT DEPLETION (hết input)

  Cơ chế:
    → Environment CHỈ CÓ bấy nhiêu stimulus → hết → VTA im → dừng

  × Sensory-Driven: HIỆU QUẢ
    → Con cua có ~10 behaviors → hết → delta = 0 → dừng
    → Exception: environment CỰC phong phú → dài hơn nhưng vẫn CÓ GIỚI HẠN

  × Imagination-Driven: KHÔNG HIỆU QUẢ
    → Input = internal chunks → combinatorial space → gần vô tận ở expert
    → KHÔNG hết input → phanh KHÔNG hoạt động


TÓM TẮT:

  ┌────────────────────┬─────────────────────┬─────────────────────┐
  │ Phanh              │ × Sensory-Driven    │ × Imagination-Driven│
  ├────────────────────┼─────────────────────┼─────────────────────┤
  │ ① Habituation      │ ĐỦ MẠNH            │ YẾU (tự tạo delta)  │
  │ ② Satisfaction     │ ĐỦ MẠNH            │ YẾU (domain vô tận) │
  │ ③ Input Depletion  │ ĐỦ MẠNH            │ KHÔNG (internal)     │
  ├────────────────────┼─────────────────────┼─────────────────────┤
  │ Kết luận           │ TỰ DỪNG ✓          │ KHÓ DỪNG → §4 Loop  │
  └────────────────────┴─────────────────────┴─────────────────────┘

  Phanh CÒN hoạt động cho Imagination:
    → Body-base survival: đói, khát, buồn ngủ → BẮT BUỘC dừng
    → Cortisol tích lũy: kiệt sức → BẮT BUỘC dừng (Cortisol-Baseline.md v2.0)
    → External interrupt: ai đó gọi, deadline, trách nhiệm
    → = Phanh TỪ BÊN NGOÀI, không phải internal mechanism

  → = Imagination Novelty có rất ÍT phanh tự nhiên
  → = Khi không tự dừng + gây hại → = NOVELTY LOOP (§4)

  🟢 Habituation = neuroscience verified
  🟢 Satiety hormones (leptin, CCK, insulin) = well-established
  🟡 3 phanh framework + sensory/imagination asymmetry = framework synthesis
```

---

## §4 — NOVELTY LOOP: KHI KHÔNG TỰ DỪNG

```
⭐ NOVELTY LOOP = IMAGINATION-DRIVEN NOVELTY KHI 3 PHANH THẤT BẠI

  DEFINE:
    Novelty Loop = vòng lặp KHÔNG CHỦ ĐỘNG:
    Chunk-Gap (chưa xong) → cortisol (change-readiness) → imagine (tìm giải pháp)
    → chưa ra → gap VẪN CÒN → cortisol VẪN CÒN → imagine TIẾP → ...

  ĐẶC ĐIỂM:
    → KHÔNG chọn vào → VÔ TÌNH bị cuốn
    → KHÔNG dễ dừng → dừng imagine ≠ dừng gap → cortisol VẪN CÒN
    → VỪA khó chịu VỪA hứng thú
    → CÓ GIÁ TRỊ (mỗi vòng gần domain reality hơn — nếu chunks đủ)
    → CÓ HẠI NẾU kéo dài + thiếu repair

  = Tính năng MẠNH NHẤT + NGUY HIỂM NHẤT:
    → Cho phép: E=mc², sáng tác nhạc, build framework
    → Gây hại: Newton mental health, Tesla OCD, burnout, mất ngủ


§4.1 — THREAT NỀN = SÀN GIỮ LOOP

  ⭐ INSIGHT CỐT LÕI:
  Novelty KHÔNG CẦN threat để BẮT ĐẦU.
  Nhưng CẦN threat để DUY TRÌ loop ĐỦ DÀI cho breakthrough.

  Novelty loop có giai đoạn TENSION (reward tạm = 0):

    ████░░░░████░░████░░░░░░░░████████
    ↑reward  ↑tension ↑reward ↑tension dài   ↑breakthrough

  Trong giai đoạn tension:
    KHÔNG CÓ threat nền:
      Drive = novelty(0) - cost(effort) = ÂM → body: "bỏ đi" → DỪNG
      = Phần lớn mọi người dừng ở đây

    CÓ threat nền:
      Drive = novelty(0) + threat-push(dương) - cost(effort)
      NẾU threat-push > cost → VẪN TIẾP dù không reward
      → Tới khi novelty spike lại → drive DƯƠNG MẠNH → euphoria
      → Euphoria CÀng MẠNH vì contrast effect (vừa thoát tension)

  → Threat = SÀN: giữ drive KHÔNG RƠI xuống ÂM

  ⭐ TENSION CẢM NHẬN KHÁC TÙY MODALITY (Modality.md v1.0):
    → Somatic-dominant: bồn chồn, ngồi không yên, "ngứa" bên trong
    → Verbal-dominant: suy nghĩ lặp lại, "quay vòng", nặng đầu
    → Visual-dominant: "hình ảnh giải pháp mờ mờ hiện lên"
    → = CÙNG mechanism → KHÁC trải nghiệm chủ quan tùy modality


§4.2 — 4 MỨC DEPTH

  MỨC 1 — PURE NOVELTY (không threat):
    Trigger: sensory-driven (con cá, video hay)
    Duration: PHÚT. Output: trải nghiệm thú vị.
    → = "Ăn vặt Novelty" — vui nhưng không sâu

  MỨC 2 — NOVELTY + MICRO-GAP NỘI TẠI:
    Trigger: "chưa xong" = Chunk-Gap nhỏ tự nhiên
    Duration: GIỜ. Output: hoàn thành task, học skill.
    → = "Bữa chính Novelty" — có depth, dừng được khi mệt

  MỨC 3 — NOVELTY + THREAT NỀN EXTERNAL:
    Trigger: chunks đủ + threat cuộc sống tạo cortisol nền
    Duration: THÁNG → NĂM. Output: breakthrough, phát minh.
    → Threat KHÔNG KIỂM SOÁT ĐƯỢC → risk burnout
    → Ví dụ: Einstein (nghèo + academic pressure), Newton (plague isolation)

  MỨC 4 — NOVELTY + THREAT TỰ TẠO (L3, controllable):
    Trigger: chunks đủ + TỰ TẠO threat (competition, mortality awareness)
    Duration: NĂM → CẢ ĐỜI. Output: sustained innovation.
    → Threat BẬT/TẮT ĐƯỢC (vì tự PFC tạo, PFC có thể dismiss)
    → = TỐI ƯU NHẤT: threat vừa đủ + tắt khi cần repair
    → Ví dụ: Jensen Huang ("cách phá sản 30 ngày" — dù NVIDIA lớn nhất)

  Tại sao Mức 4 BẬT/TẮT được mà Mức 3 không:
    → Mức 3: threat external (nghèo, deadline, áp lực gia đình) → PFC không dismiss được
    → Mức 4: threat PFC tự tạo ("đối thủ đang tiến") → PFC có thể dismiss
    → = Self-Created Threat = SKILL, không phải bẩm sinh
    → Sequence: trải nghiệm threat thật → quan sát pattern → tự tạo có ý thức
    → Chi tiết: Self-Created-Threat.md (4 loại, 3 giai đoạn, AI era, calibration)


§4.3 — NOVELTY LOOP vs ANXIETY LOOP

  Cùng loop — KHÁC output:

    ┌─────────────────┬──────────────────────┬──────────────────────┐
    │                 │ ANXIETY LOOP          │ NOVELTY LOOP         │
    ├─────────────────┼──────────────────────┼──────────────────────┤
    │ Trigger         │ Threat (sợ hậu quả)  │ Chunk-Gap (muốn fill)│
    │ Output mỗi vòng│ SỢ HƠN (tệ hơn)     │ GẦN HƠN (tiến triển) │
    │ Dopamine        │ THẤP                 │ CÓ (gần insight)     │
    │ Body feel       │ Thuần khó chịu       │ Khó chịu + hứng thú │
    │ Giá trị         │ KHÔNG (loop vô ích)  │ CÓ (dần tới kết quả) │
    │ Dừng khi        │ Threat hết / crash   │ Gap filled / break    │
    └─────────────────┴──────────────────────┴──────────────────────┘

  MIXED LOOP (phổ biến nhất):
    → "Muốn fill gap" (Novelty) + "Sợ không fill được" (Threat) = CÙNG LÚC
    → Tỉ lệ Novelty:Threat quyết định CHẤT LƯỢNG trải nghiệm:
      80:20 → hào hứng + chút áp lực → flow territory
      50:50 → vừa thích vừa stress → productive nhưng MỆT
      20:80 → chủ yếu sợ, chút thích → burnout risk CAO


§4.4 — SLEEP × LOOP

  PARADOX:
    → Muốn fill gap → CẦN cortisol (change-readiness mode)
    → Muốn repair não → CẦN cortisol THẤP (sleep)
    → NẾU loop KHÔNG dừng buổi tối → cortisol VẪN CAO → sleep KÉM

  VICIOUS CYCLE:
    Ngày: imagine → chưa ra → cortisol duy trì
    Tối: cortisol vẫn → nằm giường → đầu vẫn chạy → ngủ kém
    Sáng: PFC chưa repair → imagine chậm hơn
    → Chậm hơn → chưa ra → cortisol CÒN CAO hơn → ngủ TỆ hơn
    → = SPIRAL DOWN: mỗi vòng tệ hơn vòng trước

  NHƯNG — REM = "THỜI GIAN VÀNG":
    → Dù sleep quality kém → REM VẪN XẢY RA ở mức nào đó
    → REM: PFC offline → vô thức brainstorm TỰ DO
    → Kết nối "absurd" mà PFC sẽ filter → MỘT SỐ = ĐÚNG → compile blueprint
    → = "Tối lộn xộn → sáng mượt"
    → = "Ngủ = outsource imagine cho vô thức" — PFC nghỉ, vô thức LÀM

  🟢 Walker 2017: sleep deprivation → PFC performance GIẢM 30-40%
  🟢 Wagner et al. 2004: sleep → insight task → GẤP ĐÔI xác suất
  🟢 Stickgold 2005: sleep → insight +33%
  🟡 Loop dynamics = framework synthesis, consistent with observation
```

---

## §5 — DRD4: DEPTH vs BREADTH

```
⭐ DRD4 THRESHOLD TẠO SPECTRUM NOVELTY — KHÔNG PHẢI "TỐT HƠN / KÉM HƠN"

  DRD4 threshold (§1.2) = filter ở VTA→PFC level
  → Repeat dài (7R+) = threshold CAO → ÍT signal tới PFC
  → Repeat ngắn (4R) = threshold THẤP → NHIỀU signal tới PFC


7R × NOVELTY:

  Sensory-Driven:
    → VTA chỉ báo biến động LỚN → ÍT bị trigger
    → ÍT Novelty events per giờ
    → NHƯNG mỗi event = delta LỚN → ghi nhớ SÂU

  Imagination-Driven:
    → PFC ÍT bị interrupt → deep focus TỐT
    → Imagine-reward-refine loop: SUSTAINED, DEEP
    → = 7R THIÊN VỀ IMAGINATION NOVELTY

  Hệ quả: "Biết ÍT nhưng biết SÂU" (per thời điểm)
  Nguy cơ: drift xa domain (ít external check)
  Cần: external feedback loop


4R × NOVELTY:

  Sensory-Driven:
    → VTA báo MỌI biến động → LIÊN TỤC bị trigger
    → NHIỀU events per giờ, mỗi event = delta NHỎ
    → "Biết NHIỀU thứ ở MỖI NƠI"

  Imagination-Driven:
    → PFC LIÊN TỤC bị interrupt → khó sustain 1 workspace lâu
    → CÓ THỂ imagine deep → nhưng CẦN environment TĨNH

  Hệ quả: "Biết NHIỀU nhưng chưa chắc SÂU" (per thời điểm)
  Nguy cơ: scatter — nhiều events nhưng không build depth
  Cần: structured environment + deliberate focus


SO SÁNH:

    ┌──────────────────────┬────────────────────┬────────────────────┐
    │                      │ 7R (threshold CAO) │ 4R (threshold THẤP)│
    ├──────────────────────┼────────────────────┼────────────────────┤
    │ Sensory Novelty      │ ÍT events          │ NHIỀU events       │
    │ Per event            │ Delta LỚN          │ Delta NHỎ          │
    │ Imagination Novelty  │ DEEP, sustained    │ BROAD, interrupted │
    │ Focus style          │ Deep dive          │ Context switching  │
    │ Dạng Novelty chính  │ Imagination        │ Sensory            │
    │ Environment need     │ Ít cần stimulation │ Cần giảm noise     │
    └──────────────────────┴────────────────────┴────────────────────┘

  SPECTRUM, KHÔNG CHỈ 2 CỰC:
    → 2R, 3R, 4R, 5R, 6R, 7R, 8R,... = phổ LIÊN TỤC
    → DRD4 là 1 TRONG NHIỀU factors (COMT, MAO-A, baseline cortisol,...)
    → Framework dùng 7R/4R như archetype để giải thích
    → Thực tế: mỗi người ở VỊ TRÍ KHÁC trên spectrum

  🟢 DRD4 repeat variants (2R-11R) = neuroscience verified
  🟢 COMT, MAO-A interaction effects = pharmacogenomics
  🟡 Depth vs breadth mapping = framework interpretation
```

---

## §6 — KHI CÓ LỢI vs KHI CÓ HẠI

```
⭐ NOVELTY = TRUNG TÍNH — mechanism, không phải virtue hay vice


KHI NOVELTY CÓ LỢI:

  ① Explore → Learn → Adapt
    → Novelty drive khám phá environment → tích lũy chunks
    → Chunks = map thế giới → predict tốt hơn → adapt tốt hơn
    → = Chức năng evolution-driven

  ② Chunk-Gap fill → Understanding
    → Gap detect → imagine → resolve → body-feedback reward
    → = HỌC HỎI SÂU — không chỉ biết, mà HIỂU
    → = Tại sao "tại sao?" là biểu hiện của Chunk-Gap drive

  ③ Creative output
    → Cross-domain chunk recombination → patterns mới
    → = Novelty Imagination ở mức cao → output có giá trị

  ④ Flow state
    → Delta vừa đủ + chunks match + challenge phù hợp
    → = Conditions cho flow (Csikszentmihalyi)

  ⇒ ĐIỀU KIỆN: đủ chunks + domain check + repair


KHI NOVELTY CÓ HẠI:

  ① SCATTER — Sensory Novelty + threshold thấp + không focus
    → Nhiều delta nhỏ → KHÔNG deep → chunks rời rạc
    → "Biết nhiều, giỏi ít"

  ② BURNOUT — Imagination Novelty + không repair
    → Loop liên tục → cortisol tích lũy → kiệt sức
    → NHƯNG drive VẪN CÒN (gap chưa fill) → frustrated

  ③ DRIFT — Imagination Novelty + không domain check
    → Imagine sâu NHƯNG không verify với domain reality
    → "Đúng trong đầu, sai ngoài đời"
    → Body-feedback reward fire (pattern fit internally) nhưng domain mismatch

  ④ EXPLOIT — Sensory Novelty bị hệ thống lợi dụng
    → MXH scroll, gambling, clickbait
    → = Environment THIẾT KẾ để exploit mechanism
    → Delta > 0 liên tục nhưng KHÔNG depth → giờ → năm mất cho delta nông

  ⇒ CƠ CHẾ giống — CONDITIONS quyết định output


TÓM TẮT:

  ┌──────────────────────────────────────────────────────────┐
  │                                                          │
  │  NOVELTY + đủ chunks + domain check + repair = TỐT      │
  │  = Learn, create, flow, adapt                            │
  │                                                          │
  │  NOVELTY + ít chunks + không check + không repair = HẠI  │
  │  = Scatter, burnout, drift, exploit                      │
  │                                                          │
  │  → Cùng mechanism → khác conditions → khác output        │
  │                                                          │
  └──────────────────────────────────────────────────────────┘

  🟡 Classification = framework analysis
  🟢 Flow state conditions = Csikszentmihalyi
  🟢 Burnout mechanism (chronic stress) = well-established
  🟢 Dopamine exploit by tech (variable reward) = behavioral research
```

---

## §7 — HONEST ASSESSMENT

```
  TOÀN FILE — ĐÁNH GIÁ TRUNG THỰC:

  🟢 VERIFIED (neuroscience / established research):
    ┌────────────────────────────────────────────────────────────┐
    │ VTA structure + function (~400K neurons, midbrain)         │
    │ Dopamine pathway (tyrosine → dopamine → axon → receptor)  │
    │ Prediction delta mechanism (Schultz 1997)                  │
    │ DRD4 receptor variants (2R-11R repeat polymorphism)        │
    │ Habituation mechanism (neural adaptation)                  │
    │ Chunk compilation + hierarchy (Chase & Simon 1973)          │
    │ Satiety hormones (leptin, CCK, insulin)                    │
    │ Opioid/endorphin reward system                             │
    │ COMT, MAO-A gene interactions (pharmacogenomics)           │
    │ Flow state conditions (Csikszentmihalyi)                   │
    │ Chronic stress → neural damage (McEwen 1998, 2007)         │
    │ Variable reward → dopamine exploit (Skinner → tech)        │
    │ REM → insight (Wagner 2004, Stickgold 2005)                │
    │ Sleep deprivation → PFC decline (Walker 2017)              │
    │ Combinatorial mathematics                                  │
    └────────────────────────────────────────────────────────────┘

  🟡 FRAMEWORK SYNTHESIS (consistent logic, derived from 🟢):
    ┌────────────────────────────────────────────────────────────┐
    │ Novelty = observation parameter (not component)            │
    │ 2 dạng mapping vào 2 nguồn Body-Feedback (Sensory/Pattern)│
    │ 3 phanh + sensory/imagination asymmetry                    │
    │ Combinatorial space → imagination duration                 │
    │ MXH exploit = hack 2/3 phanh                              │
    │ Imagine-reward-refine loop mechanism                       │
    │ DRD4 threshold → depth/breadth types                       │
    │ Chunk-Gap = foundation cho Novelty                         │
    │ Threat nền = sàn giữ loop                                  │
    │ Self-Created Threat = learnable skill                       │
    │ Novelty Loop vs Anxiety Loop                               │
    │ Tension per modality                                        │
    │ 4 mức depth (pure → self-created threat)                   │
    │ 4 hại categories (scatter/burnout/drift/exploit)           │
    │ "Tò mò" = mechanism output (not fixed trait)               │
    │ Compilable Architecture → novelty = detect uncompiled input (v1.1)  │
    │ Novelty = by definition fresh processing (v1.1)            │
    │ 2-tầng calibration: "mới" = per-individual (v1.1)          │
    └────────────────────────────────────────────────────────────┘

  🔴 HYPOTHESIS (logical but unverified):
    ┌────────────────────────────────────────────────────────────┐
    │ Exact chunk count → imagination threshold — unknown        │
    │ Optimal environment per DRD4 variant — untested            │
    │ Transition point sensory → imagination — undefined         │
    │ Self-Created Threat effectiveness measure — no data        │
    │ Novelty:Threat ratio → flow/burnout threshold — unmeasured │
    └────────────────────────────────────────────────────────────┘
```

---

## §8 — CROSS-REFERENCES

```
  ← FOUNDATION (đọc trước hoặc cùng):
    Core-v7.8-Draft.md §8 — Novelty = observation parameter definition
    Body-Feedback-Mechanism.md v2.0 §3.3 — Chunk-Gap = Novelty foundation
    Body-Feedback-Mechanism.md v2.0 §2 — 2 nguồn (Sensory/Pattern-Driven)
    Chunk.md v2.3 — chunk substrate, compilation, hierarchy
    Cortisol-Baseline.md v2.0 — cortisol = amplifier, sustained dynamics
    Valence-Propagation.md v3.0 — body evaluation, 3 firing modes
    Reward-Signal-Architecture.md v1.0 — prediction-delta refined
    Inter-Body-Mechanism.md v1.0 §1.2 — Compilable Architecture (novelty = detect uncompiled)
    Inter-Body-Mechanism.md v1.0 §3 — Compiled/Fresh (novelty = fresh by definition)
    Simulation-Engine.md v1.0 — novelty = prediction mismatch in simulation
    Gap-Body-Need.md v1.0 — novelty satiation dynamics (3 types)
    Gap-Distribution-Profile.md v1.1 — PFC budget limits novelty seeking

  ↔ SONG SONG (cùng Observation/ folder):
    Observation/Threat.md v1.2 — PUSH away from harm (parallel với Novelty PULL)
    Observation/Drive.md v1.2 — HOW Novelty + Threat + other patterns → action
    Observation/Empathy.md v4.0 — Self-Pattern-Modeling function on chunks
    Observation/Liking-Wanting.md — Wanting overlap với Novelty (dopamine)

  → DOWNSTREAM (đọc sau):
    Modality.md v1.0 §3 — chunk depth = modality count
    Schema.md v2.0 — schema = observation parameter for chunk patterns
    Feeling.md v3.0 — PFC observation interface (Novelty → feeling "thú vị")
    Somatic-Articulation-Loop.md — Chunk-Gap felt sense → articulation
    Body-Feedback-Label.md v2.0 — vocabulary reference

  → ỨNG DỤNG:
    AI-Schema-Detection.md — AI detect Novelty patterns
    Domain-Mapping-Drive.md — Novelty trong education context

  STATUS:
    v1.0 — 2026-04-20 — viết mới cho v7.8 cycle-based architecture
    v1.1 — 2026-05-17 — +Compilable Architecture, +Compiled/Fresh, +2-tầng, version sync
    v1.2 — 2026-05-23 — Concept Cascade: +Simulation-Engine, +Satiation types, +PFC Budget, version updates
    Gộp từ: Novelty.md v1.0-old + Novelty-Loop.md (backup: _backup/Drive-v75-era/)
    Aligned: Core v7.8, Inter-Body-Mechanism v1.0, prediction-delta terminology
```
