---
title: Drive — Observation Parameter (Integration)
version: 1.1
created: 2026-04-20
updated: 2026-05-17
status: OBSERVATION PARAMETER v1.1
scope: |
  INTEGRATION FILE: Drive = tên gọi cho energy + direction emergent từ
  chunk dynamics + body-feedback. File này KHÔNG thêm mechanism mới —
  TÍCH HỢP tất cả observation parameters (Novelty, Threat, Status,...) 
  để giải thích: "Tại sao hành động NÀY tại thời điểm NÀY?"
  PFC participation spectrum, drive conflict, signal strength model.
  v1.1 KEY CHANGES:
    ⑪ +Architecture B: drive = emergent từ general-purpose reward system
    ⑫ +Compiled/Fresh (F1/F2): compiled drive (Mode 1-2) vs fresh drive (Mode 3-6)
    ⑬ +Domain=Arbiter: drive direction CAN BE WRONG
    ⑭ Version refs synced (VP v2.0, BFM v2.0, Feeling v3.0)
    ⑮ +Cross-refs: Inter-Body-Mechanism.md v1.0, Body-Feedback-Label.md v2.0
purpose: |
  Novelty.md + Threat.md = mechanism RIÊNG LẺ.
  File này = HOW chúng COMBINE → action tại mỗi thời điểm.
  Core v7.8 §8 list observation parameters. File này giải thích interaction.
position: |
  Core-Deep-Dive/Observation/ — INTEGRATION file, đọc SAU Novelty + Threat.
dependencies:
  - Core-v7.8-Draft.md — cycle architecture, §8 observation parameters
  - Observation/Novelty.md v1.0 — PULL toward opportunity
  - Observation/Threat.md v1.0 — PUSH away from harm
  - Body-Feedback-Mechanism.md v2.0 — Shift/Miss/Gap, dual-pull
  - Chunk.md v2.0 — chunk substrate, compilation
  - Cortisol-Baseline.md v2.0 — amplifier dynamics
  - Feeling.md v3.0 — PFC observation interface
  - Imagine-Final-Evaluation.md — 2 trục × 4 góc
  - Anchor-Schema.md — Trust binding, sync point
  - Inter-Body-Mechanism.md v1.0 — Architecture B, Compiled/Fresh, Domain=Arbiter
  - Body-Feedback-Label.md v2.0 — vocabulary reference
sources_backup: |
  Rewrite từ: Drive.md v1.1 (2,733L)
  Backup: _backup/Drive-v75-era/
language: Tiếng Việt primary + English technical terms
confidence: 🟢 Research support | 🟡 Framework synthesis | 🔴 Hypothesis
---

# Drive — Observation Parameter (Integration)

> CEO quyết định layoff 200 người (PFC ~85%, cortisol cao, moral dissonance).
> 2 giờ sau, về nhà chơi với con (PFC ~5%, auto, vui vẻ).
>
> Cùng người. Cùng não. KHÁC drives → KHÁC mode hoàn toàn.
>
> "Drive" không phải 1 module bật/tắt — mà là TÊN GỌI cho
> energy + direction ĐANG emergent tại thời điểm quan sát.
>
> File này giải thích: tại sao cùng người mà KHÁC hành vi,
> PFC tham gia THẾ NÀO, và khi drives xung đột thì SAO.

---

## Mục lục

- §0 — DRIVE LÀ OBSERVATION PARAMETER
- §1 — VÔ THỨC = ENGINE, PFC = OBSERVER-ORCHESTRATOR
- §2 — PFC PARTICIPATION SPECTRUM: 6 MODES
- §3 — DRIVE CONFLICT: 4 TYPES + RESOLUTION
- §4 — PULL vs PUSH: TẠI SAO QUAN TRỌNG
- §5 — HONEST ASSESSMENT
- §6 — CROSS-REFERENCES

---

## §0 — DRIVE LÀ OBSERVATION PARAMETER

```
⭐ REFRAME V7.8:

  Core v7.5 (cũ): 3 drives (Novelty/Status/Protect) = L3 operators
  Core v7.8 (mới): Drive = observation parameter — tên gọi cho energy+direction
                    emergent từ chunk dynamics + body-feedback

  Drive KHÔNG PHẢI:
    ✗ "Quyết định → hành động" (sai thứ tự)
      → Thực tế: body-need → drive → action → rồi MỚI "biết" đã quyết định
    ✗ "Ý thức điều khiển hành vi" (dualism)
      → Thực tế: vô thức = engine chính (~95% quyết định)
    ✗ "Cần động lực mới hành động" (motivation theory đơn giản)
      → Thực tế: drives chạy LIÊN TỤC, "thiếu động lực" = drives CONFLICT
    ✗ "1 drive tại 1 thời điểm" (single-channel model)
      → Thực tế: NHIỀU drives ĐỒNG THỜI → action = emergent output

  Drive LÀ:
    ○ Continuous — KHÔNG BAO GIỜ tắt (kể cả ngủ: REM processing)
    ○ Multi-channel — nhiều patterns chạy SONG SONG
    ○ Predictive — dự đoán + hành động trước (not reactive)
    ○ Body-grounded — MỌI drive BẮT ĐẦU từ body-feedback
    ○ Emergent — action = OUTPUT, không phải INPUT


⭐ ARCHITECTURE B → DRIVE EMERGENT (Inter-Body-Mechanism.md §1.2):

  ARCHITECTURE A (côn trùng, động vật đơn giản):
    Hardwired circuits: food→eat, predator→flee, mate→approach.
    Không cần "drive" — stimulus→response CỐ ĐỊNH.
    Không có PFC → không có deliberation → không có conflict.

  ARCHITECTURE B (humans):
    Hardwired: CHỈ reward MECHANISM + compilation + social + PFC.
    Content: LEARN from environment → compile → body-need.
    → KHÔNG CÓ "drive module" hardwired cho specific behaviors.
    → Drive = EMERGENT OUTPUT từ general-purpose system:
      body-need aggregate + chunk dynamics + prediction + PFC orchestration
      → energy + direction xuất hiện → = "drive"

  → Drive là TÊN GỌI cho energy+direction emergent từ Architecture B.
  → Architecture A KHÔNG CẦN khái niệm "drive" (stimulus→response đủ).
  → Architecture B CẦN khái niệm "drive" vì output KHÔNG predetermined.

  🟡 Architecture A/B = framework synthesis (Inter-Body-Mechanism.md §1.2).
     Underlying neuroscience (general-purpose reward, Hebbian) = 🟢.


DRIVE TRONG CYCLE (Core v7.8 §1):

  Domain → Body-Input → Unconscious(Chunks) → Feeling → PFC → Body-Output → Domain

  "Drive" = observation point cho TOÀN BỘ cycle:
  → Body-Input tạo body-feedback signals
  → Chunks process: match patterns, detect gaps, predict outcomes
  → Multiple body-feedback signals fire ĐỒNG THỜI
  → Tổng hợp → energy + direction EMERGE → action
  → = "Drive" = tên gọi cho energy + direction đó

  Giá trị quan sát:
    → Predict: "người này drive bởi novelty" → xu hướng hành vi
    → Communicate: "anh ấy threat-driven" → mô tả trạng thái
    → Diagnose: "thiếu drive" → boredom territory
    → NHƯNG: can thiệp ở mechanism level, KHÔNG ở observation level

  ⚠️ DOMAIN = ARBITER — drive direction CAN BE WRONG:
    → Drive mạnh ≠ drive ĐÚNG.
    → Body-need fires → PFC creates direction → NHƯNG PFC = Lawyer
      (Inter-Body-Mechanism.md §7): narrative phục vụ body-need,
      KHÔNG nhất thiết phù hợp domain reality.
    → Ví dụ: novelty drive kéo vào conspiracy theories = mạnh nhưng SAI hướng.
    → Ví dụ: threat drive kéo khỏi opportunity tốt = mạnh nhưng SAI hướng.
    → Domain feedback = ARBITER duy nhất kiểm tra drive direction.
    → "Cảm thấy đúng" ≠ "Đúng" — cần domain verify.
    🟡 Domain=Arbiter = framework principle (Inter-Body-Mechanism.md §9)


VỊ TRÍ FILE NÀY:

  ┌─────────────────────────────────────────────────────────┐
  │ OBSERVATION PARAMETERS (riêng lẻ):                       │
  │   Novelty.md  — PULL toward opportunity                  │
  │   Threat.md   — PUSH away from harm                      │
  │   (Status, Connection, Meaning,... — Core v7.8 §8)      │
  └────────────────────────┬────────────────────────────────┘
                           │
                           ▼
  ┌─────────────────────────────────────────────────────────┐
  │ INTEGRATION (file NÀY):                                  │
  │   HOW parameters combine → action tại mỗi thời điểm     │
  │   PFC participation spectrum                              │
  │   Drive conflict + resolution                             │
  └─────────────────────────────────────────────────────────┘
```

---

## §1 — VÔ THỨC = ENGINE, PFC = OBSERVER-ORCHESTRATOR

```
⭐ TẠI SAO VÔ THỨC LÀ ENGINE CHÍNH?

  4 lý do vô thức THẮNG PFC trong MỌI cuộc đua:

  ① CAPACITY: ~95% bandwidth não
    → Vô thức: hàng TRIỆU signals/giây
    → PFC: ~4±1 items đồng thời (Cowan 2001)
    → = PFC là spotlight NHỎ trên sân khấu KHỔNG LỒ

  ② SPEED: milliseconds vs seconds
    → Compiled chunks fire trong ms
    → PFC: 200ms+ deliberation
    → = Vô thức ĐÃ HÀNH ĐỘNG trước khi PFC kịp "suy nghĩ"

  ③ EFFICIENCY: energy thấp
    → Compiled schemas = auto = energy thấp
    → PFC deliberation = glucose intensive (~2% mass, ~20% energy)
    → = Não TIẾT KIỆM bằng cách dùng vô thức TỐI ĐA

  ④ EVOLUTION: 500 triệu năm vs ~2 triệu năm
    → Vô thức: MỌI động vật có (500M năm tinh chỉnh)
    → PFC: hoàn chỉnh chỉ ở humans (~2M năm)
    → = PFC BUILD ON TOP OF vô thức, không THAY THẾ

  → KẾT LUẬN:
    → Vô thức = DEFAULT mode → chạy MỌI LÚC
    → PFC = EXCEPTION mode → chạy KHI CẦN
    → PHẦN LỚN cuộc sống = vô thức ổn → PFC nghỉ
    → PFC tham gia khi: dissonance mới, novelty lớn, threat mới,
      drives conflict, Imagine-Final threatened


⭐ SIGNAL STRENGTH MODEL (thay cho Layer Priority):

  V7.5 cũ: L0 > L1 > L2 > L3 (fixed priority)
  V7.8 mới: Signal MẠNH NHẤT thắng (no fixed hierarchy)

  → L0 signals HAPPEN TO BE loudest (evolutionary design cho survival)
  → Nhưng: KHÔNG phải luôn luôn. Context quyết định:
    → Bình thường: đói (strong) override tò mò (weak) → tìm ăn
    → Nhưng: Einstein nhịn đói để imagine (PFC override body-input)
    → Nhưng: Anne Frank được giấu (nhiều reward chains > tử hình threat)
    → = Valence chain CÓ THỂ override signal strength
      (Valence-Propagation.md §5③)

  → PFC CÓ THỂ override (Mode 6, §2) — nhưng LUÔN CÓ COST
  → Kéo dài override → repair debt → body eventually thắng

  ⭐ COMPILED/FRESH = TRỤC THẬT (Inter-Body-Mechanism.md §3):

    Vô thức vs PFC THỰC CHẤT là COMPILED vs FRESH spectrum:

    COMPILED DRIVE (F1 — automatic, cost ≈ 0):
      → Chunks đã compile → body-feedback direct → action EMERGE
      → Vô thức auto → Mode 1-2 (§2)
      → Ví dụ: lái xe đường quen (compiled route chunks fire → auto)
      → Ví dụ: chef thấy nguyên liệu → "biết ngay" cần làm gì
      → = Phần lớn cuộc sống (~70-80%) = compiled drive

    FRESH DRIVE (F2 — PFC draft, cost > 0):
      → Tình huống MỚI / mâu thuẫn → chunks không match → PFC phải draft
      → PFC deliberate → Mode 3-6 (§2)
      → Ví dụ: ngày đầu đi làm → mọi thứ mới → PFC liên tục draft
      → Ví dụ: conflict giữa novelty vs threat → PFC arbitrate
      → = Tình huống mới + khó = fresh drive territory

    TRANSITION F2→F1 (Learning):
      → Fresh drive lặp lại + resolve → chunks compile → compiled drive
      → = "Ngày đầu đi làm" (fresh) → "tháng thứ 6" (compiled)
      → Kahneman System 1 (compiled) / System 2 (fresh) tương đương
      → Chi tiết: Inter-Body-Mechanism.md §3.3

    → INSIGHT: Mode 3 (Spinning) vs Mode 4 (Resolve) = CÙNG fresh territory
      → KHÁC ở chunk availability, KHÔNG phải activation level

  🟢 Unconscious processing dominance = neuroscience consensus
  🟢 PFC capacity limits = Cowan 2001 (4±1)
  🟢 PFC energy cost = Raichle 2006
  🟢 Evolutionary timeline = comparative neuroscience
  🟡 Compiled/Fresh drive distinction = framework synthesis (consistent with Kahneman)


⭐ TẠI MỌI THỜI ĐIỂM, NHIỀU SIGNALS CÙNG LÚC:

  ┌────────────────────────────────────────────────────────┐
  │  Body-input signals:  channels nào thiếu? bao nhiêu?   │
  │  Chunk patterns:      match gì? gaps? conflicts?        │
  │  Body-feedback:       reward hay dissonance? mức nào?   │
  │  Imagine-Final:       action nào serve hướng dài hạn?   │
  │                                                        │
  │  → Tổng hợp → SIGNAL MẠNH NHẤT THẮNG                  │
  │  → = energy + direction EMERGE → action                │
  └────────────────────────────────────────────────────────┘

  Hầu hết thời gian: signals HÒA → action SMOOTH:
    → Body OK + chunks compiled match context + no dissonance
    → = PFC KHÔNG CẦN → Mode 1-2 (§2)
    → = "Cuộc sống bình thường"

  Khi signals CONFLICT hoặc THIẾU:
    → Body urgent + chunks không match + dissonance cao
    → = PFC được gọi → Mode 3-6 (§2)
    → = "Tình huống khó" — cần PFC participate
```

---

## §2 — PFC PARTICIPATION SPECTRUM: 6 MODES

```
⭐ PFC = PHỔ LIÊN TỤC, KHÔNG PHẢI ON/OFF

  PFC participation = spectrum từ 0% → 95%
  Framework DISCRETE hóa thành 6 MODES cho communication.

  2 TRỤC:
    Trục 1: PFC ACTIVATION — "PFC bận CỠ NÀO?"
    Trục 2: PFC EFFECTIVENESS — "PFC bận có ÍCH không?"

  ⚠️ INSIGHT QUAN TRỌNG:
    Activation CAO ≠ Effectiveness CAO
    Mode 3 (Spinning): PFC 30-50% nhưng KHÔNG hiệu quả (thiếu chunks)
    Mode 4 (Resolve): PFC 20-40% nhưng RẤT hiệu quả (đủ chunks)
    → "Bận hơn" ≠ "giỏi hơn" — CHUNKS quyết định chất lượng PFC


2-TRỤC DIAGRAM:

  PFC EFFECTIVENESS ▲
  (chunks quality)   │
                     │
    HIGH ────────────┤── [MODE 4: RESOLVE] ──── [MODE 5: STRATEGIC] ──
    (chunks đủ,      │    PFC 20-40%              PFC 60-80%
     relevant)       │    scan → match → act      hold → optimize
                     │                                     │
                     │                            [MODE 6: OVERRIDE]
                     │                              PFC 80-95%
                     │                              against body-base
                     │                              ⚠️ cost CỰC CAO
                     │
    LOW ─────────────┤── [MODE 3: SPINNING]
    (chunks thiếu,   │    PFC 30-50%
     sai tầng)       │    try → fail → try → fail
                     │
    N/A ─────────────┤── [MODE 1: ABSENT] ─── [MODE 2: MONITOR]
    (không cần PFC)  │    PFC 0-5%              PFC 5-15%
                     │    auto hoàn toàn         scan background
                     │
                     └──────────────────────────────────────────►
                          0%     20%     40%     60%     80%    95%
                                    PFC ACTIVATION (% bandwidth)

  ⚠️ 6 modes = VÙNG label trên spectrum liên tục, không phải 6 ô cố định.


═══════════════════════════════════════════════════════
MODE 1: ABSENT (PFC ~0-5%)
═══════════════════════════════════════════════════════

  Vô thức auto hoàn toàn. PFC "đèn tắt."
  Điều kiện: context an toàn + chunks compiled + no dissonance

  Ví dụ: chơi với con, đi bộ đường quen, phản xạ lái xe
  = ~60-70% thời gian thức. "Bình thường", "tự nhiên."

  🟢 Automatic behavior dominance = neuroscience consensus


═══════════════════════════════════════════════════════
MODE 2: MONITOR (PFC ~5-15%)
═══════════════════════════════════════════════════════

  PFC quan sát, KHÔNG can thiệp. "Camera an ninh."
  Vô thức vẫn chạy ~90%. PFC scan: "có gì bất thường?"
  Nếu detect dissonance → TĂNG lên Mode 3+.

  Ví dụ: lái xe đường quen, bạn rủ chơi (PFC: "có rảnh?→OK")

  🟢 Background monitoring = attention research (Posner 1980)


═══════════════════════════════════════════════════════
MODE 3: SPINNING (PFC ~30-50%, chunks THIẾU)
═══════════════════════════════════════════════════════

  ⭐ MODE KHÓ CHỊU NHẤT — PFC active nhưng KHÔNG hiệu quả.
  "Biết có vấn đề, không biết cách fix."

  Cơ chế:
    → PFC scan chunks → chỉ TÌM THẤY giải pháp CÙNG TẦNG
    → Thử A → fail → A' → fail → A'' → fail
    → Giải pháp ĐÚNG = KHÁC TẦNG — nhưng chunk cho tầng đó KHÔNG CÓ

  Ví dụ: xem TV chán
    → PFC: đổi kênh? scroll TikTok? ăn vặt? → CẢ 3 = cùng tầng (passive)
    → Giải pháp đúng: ra ngoài, vận động, gặp bạn (KHÁC TẦNG: active)
    → Nhưng chunk "đi dạo" có thể: không tồn tại / yếu / bị suppress

  Tại sao khó chịu nhất:
    → PFC active = energy cost CAO (glucose intensive)
    → Nhưng: no resolution = reward 0
    → = Chi phí CAO + phần thưởng KHÔNG → WORST experience

  ⚠️ PFC% cao hơn Mode 4 — vì CƯỠNG ÉP tìm kiếm, không phải vì giỏi hơn.

  🟡 Spinning mechanism = framework analysis
  🟢 PFC energy cost without reward = frustration research


═══════════════════════════════════════════════════════
MODE 4: RESOLVE (PFC ~20-40%, chunks ĐỦ)
═══════════════════════════════════════════════════════

  PFC active VÀ hiệu quả. "Biết vấn đề VÀ biết cách fix."
  Scan → match → act → resolve → PFC giảm.

  Ví dụ: bác sĩ gặp triệu chứng quen → chunks match → chẩn đoán → done
  = "Expertise" = Mode 4 ở domain cụ thể

  ⚠️ PFC% THẤP HƠN Mode 3 vì chunks đủ → scan nhanh → done.
  → = Chunks quyết định spinning vs resolve, KHÔNG PHẢI "cố gắng"

  🟢 Expertise = pattern recognition (Chase & Simon 1973)


═══════════════════════════════════════════════════════
MODE 5: STRATEGIC (PFC ~60-80%, chunks NHIỀU + META)
═══════════════════════════════════════════════════════

  PFC CÓ giải pháp → nhưng HOLD.
  Meta-observe: "giải pháp tức thời có TỐI ƯU dài hạn?"

  = Mode 4 + META-COGNITIVE layer:
    → PFC evaluate PFC: "tôi đang nghĩ đúng chưa?"
    → Metacognition (Flavell 1979)

  6 cách thêm data khi hold:
    → Đọc/nghiên cứu, hỏi người kinh nghiệm, ngủ (REM consolidation),
      release → DMN (đi dạo, tắm → vô thức process),
      observe thêm, imagine simulate scenarios

  Ví dụ: CEO hold trước investment decision → "cần thêm data"

  🟢 Metacognition = Flavell 1979
  🟡 Mode 5 as distinct from Mode 4 = framework distinction


═══════════════════════════════════════════════════════
MODE 6: OVERRIDE (PFC ~80-95%)
═══════════════════════════════════════════════════════

  PFC CHỐNG LẠI body-feedback signal. Đắt nhất, hiếm nhất.

  → Nhịn đói để finish deadline
  → Tough love (override empathy cho long-term good)
  → Ở lại vùng nguy hiểm vì duty

  ⚠️ LUÔN CÓ COST (body protest):
    → Cost ∝ cường độ body drive × thời gian override
    → Override nhẹ, ngắn → cost nhỏ, recover nhanh
    → Override mạnh, dài → burnout, trauma
    → = "Override hàng ngày" = đường đến burnout

  🟢 Executive function override = Miller & Cohen 2001


TÓM TẮT:

  ┌────────┬──────────┬──────────────┬──────────────────────────┐
  │ Mode   │ PFC %    │ Effectiveness│ Khi nào                  │
  ├────────┼──────────┼──────────────┼──────────────────────────┤
  │ 1 Abs. │  0-5%    │ N/A          │ Auto, safe, compiled     │
  │ 2 Mon. │  5-15%   │ N/A          │ Scan, ready to activate  │
  │ 3 Spin │ 30-50%   │ LOW          │ Dissonance + no chunks   │
  │ 4 Res. │ 20-40%   │ HIGH         │ Dissonance + chunks đủ  │
  │ 5 Str. │ 60-80%   │ HIGH + META  │ Complex, need optimize   │
  │ 6 Ovr. │ 80-95%   │ HIGH but COST│ Against body, last resort│
  └────────┴──────────┴──────────────┴──────────────────────────┘

  → PHẦN LỚN cuộc sống: Mode 1-2 (~70-80% thời gian)
  → Mode 3 vs 4 = CÙNG tình huống, KHÁC chunks → KHÁC mode → KHÁC output
  → = Chunks = BIẾN SỐ QUYẾT ĐỊNH
```

---

## §3 — DRIVE CONFLICT: 4 TYPES + RESOLUTION

```
⭐ TẠI SAO CONFLICT QUAN TRỌNG?

  Con người "phức tạp" vì drives THƯỜNG XUNG ĐỘT.
  Nhiều signals CÙNG LÚC + khác hướng = conflict → hành vi "khó hiểu"
  Hiểu conflict types → giải thích PHẦN LỚN hành vi "irrational"


═══════════════════════════════════════════════════════
TYPE 1: SIGNAL STRENGTH (survival override)
═══════════════════════════════════════════════════════

  Khi body-input signal CỰC MẠNH → override MỌI THỨ khác.
  → Vô thức AUTO, PFC không tham gia.

  Cơ chế cụ thể: NE flood → α1 receptors → PFC DISCONNECT
    → PFC literally bị cắt kết nối → KHÔNG THỂ negotiate
    → Không phải "PFC chọn nhường" — mà body TẮT PFC (Arnsten 2009)

  Ví dụ:
    → Thiếu oxy → thở, bất kể đang làm gì
    → Rất đói → dừng mọi thứ → tìm ăn
    → Hổ → quên status → CHẠY

  🟢 α1 receptor → PFC offline = Arnsten 2009, LeDoux 1996


═══════════════════════════════════════════════════════
TYPE 2: NOVELTY vs THREAT (pull vs push)
═══════════════════════════════════════════════════════

  Khi Novelty (PULL) vs Threat (PUSH) ở CÙNG target.

  → Novelty > Threat → EXPLORE (approach thắng)
  → Threat > Novelty → STAY (avoid thắng)
  → Ngang nhau → FROZEN → PFC phải arbitrate

  Ví dụ: muốn chuyển nghề
    → Novelty: "ngành mới, exciting, growth"
    → Threat: "mất thu nhập, gia đình phản đối, failure risk"
    → Resolution tùy chunks:
      → CÓ chunks (network, savings, skills): Mode 4 → chuyển
      → THIẾU chunks: Mode 3 → spinning "muốn mà không dám"
      → META chunks: Mode 5 → "chuẩn bị 6 tháng trước"

  🟢 Approach-avoidance conflict = Lewin 1935, Miller 1944


═══════════════════════════════════════════════════════
TYPE 3: BODY-FEEDBACK vs PFC (override territory)
═══════════════════════════════════════════════════════

  Body muốn X NGAY, PFC nói KHÔNG.
  = PFC dùng Imagine-Final XA để override body-feedback GẦN.
  = Mode 6 — luôn có cost.

  Ví dụ:
    → Ngủ (body) vs Deadline (PFC) → thức → cost: repair debt
    → Empathy (body) vs Strategy (PFC) → không giúp → cost: guilt
    → Fear (body) vs Duty (PFC) → ở lại → cost: trauma risk

  → Cost ∝ cường độ × thời gian. Kéo dài = burnout.

  🟢 PFC override = executive function (Miller & Cohen 2001)


═══════════════════════════════════════════════════════
TYPE 4: INTRA-OBSERVATION (cùng mức, khác hướng)
═══════════════════════════════════════════════════════

  Khi 2 observation patterns cùng signal strength, KHÁC direction.
  → Phức tạp NHẤT — không có auto priority → PFC dùng Imagine-Final tiebreaker.

  Ví dụ: Nói thẳng vs Giữ hòa khí
    → Integrity: "nên nói thẳng"
    → Status: "nói thẳng → mất lòng"
    → PFC arbitrate: Imagine-Final "respected leader" → chọn nói thẳng
    → HOẶC: Imagine-Final "harmonious relationship" → chọn giữ hòa

  Ví dụ (VN context): Bố mẹ vs Career
    → Schema empathy: "thương bố mẹ, muốn vui lòng"
    → Schema growth: "muốn phát triển, thử thách"
    → CÙNG mạnh, CÙNG "đúng" → PFC arbitrate dựa trên Imagine-Final
    → KHÔNG CÓ đáp án đúng duy nhất — framework GIẢI THÍCH, không khuyên

  🟡 Intra-observation conflict = framework classification
  🟢 Multiple social motives = Fiske 2004


═══════════════════════════════════════════════════════
RESOLUTION RULES — 5 rules theo thứ tự
═══════════════════════════════════════════════════════

  1. EMERGENCY → signal mạnh nhất AUTO THẮNG (không cần PFC)

  2. NON-EMERGENCY → PFC arbitrate dựa trên IMAGINE-FINAL
     → Imagine-Final rõ → resolution nhanh (Mode 4)
     → Imagine-Final không rõ → spinning (Mode 3) hoặc deliberate (Mode 5)

  3. CÙNG MỨC → cường độ + Imagine-Final relevance quyết định
     → Ngang nhau → FROZEN → cần thêm thông tin/thời gian

  4. PFC OVERRIDE → possible nhưng COSTLY
     → Dùng tiết kiệm — "override hàng ngày" = burnout path

  5. NO RESOLUTION NGAY → 3 options:
     a) FROZEN → cần thêm chunks, data, thời gian
     b) STRATEGIC ACCEPT → chấp nhận dissonance tạm (tiết kiệm PFC)
     c) RELEASE → DMN → để vô thức process → possible eureka

  ⚠️ CONFLICT CÓ THỂ LÀ TỐT:
    → Conflict BUỘC PFC participate → evaluate → grow
    → Resolve → chunks MỚI compiled → mode upgrade
    → = "Khó khăn" = opportunity (nếu resolve)
    → = "Khó khăn" = damage (nếu KHÔNG resolve + kéo dài)
```

---

## §4 — PULL vs PUSH: TẠI SAO QUAN TRỌNG

```
⭐ CỐT LÕI: CÙNG HÀNH VI → KHÁC DRIVE → KHÁC SUSTAINABILITY

  PULL drives (novelty, connection, experience):
    → "Muốn làm" → enjoy process → sustainable
    → Body-feedback: reward per step → chunks compile positive
    → Satisfaction: CÓ THỂ fire → natural endpoint

  PUSH drive (threat):
    → "Phải làm" → endure process → tốn cortisol → not sustainable
    → Body-feedback: relief khi threat tạm hết (≠ reward)
    → Satisfaction: KHÓ fire → no natural endpoint
    → = "Tránh threat ≠ body-need fulfilled"

  SO SÁNH:

    ┌────────────────┬────────────────┬────────────────┐
    │                │ PULL drives    │ PUSH drive     │
    ├────────────────┼────────────────┼────────────────┤
    │ Direction      │ TOWARD reward  │ AWAY FROM harm │
    │ Feeling        │ "Muốn"        │ "Phải"         │
    │ Process feel   │ Enjoy          │ Stress         │
    │ Endpoint       │ Rõ (đủ)       │ KHÔNG RÕ       │
    │ Satisfaction   │ Fire ✅        │ Khó fire ❌    │
    │ Sustainability │ Cao            │ THẤP           │
    │ Schema compile │ Positive       │ Negative       │
    │ Body cost      │ Thấp          │ CAO            │
    │ When healthy   │ Default        │ Emergency      │
    │ When dominant  │ Flow territory │ BURNOUT        │
    └────────────────┴────────────────┴────────────────┘


⭐ THREAT-DRIVE DOMINANCE TRONG MODERN LIFE:

  Hầu hết hoạt động hiện đại bị threat-drive HIJACK:

    ĐI LÀM:
      Lý tưởng: novelty + connection drive → enjoy
      Thực tế: "mất việc → mất tiền → khổ" → threat → endure

    HỌC HÀNH:
      Lý tưởng: novelty drive → tò mò → learn vì thích
      Thực tế: "thi trượt → bố mẹ mắng → tương lai tệ" → threat → học cho qua

    MỐI QUAN HỆ:
      Lý tưởng: connection drive → gần vì ấm áp
      Thực tế: "chia tay → cô đơn" → threat → giữ vì sợ

  → Pattern: cùng hành vi → khác drive → khác output + sustainability
  → KHÔNG phải hoạt động sai → mà DRIVE sai
  → Threat-Drive được THIẾT KẾ cho emergency (ngắn hạn)
  → Xã hội biến nó thành DEFAULT (dài hạn) = BURNOUT


⭐ CHUYỂN TỪ PUSH → PULL:

  CÂU HỎI MỞ (Threat-Drive-Analysis.md §14):
    → Threat CÓ THỂ chuyển thành pull không?
    → "Phải học" → dần dần → "muốn học"?
    → CÓ THỂ: nếu trong quá trình "phải" → tình cờ ENJOY → schema mới
    → NHƯNG: cortisol QUÁ CAO → PFC offline → KHÔNG thể discover enjoy
    → = PARADOX: threat-drive CẢN CHÍNH VIỆC chuyển sang pull-drive
    → = Tại sao giảm threat TRƯỚC, rồi mới build novelty path

  🟡 Pull vs push sustainability = framework analysis
  🟢 Threat designed for emergency (stress physiology)
  🟡 Modern threat-drive dominance = derived, consistent with epidemiology
```

---

## §5 — HONEST ASSESSMENT

```
  TOÀN FILE — ĐÁNH GIÁ TRUNG THỰC:

  🟢 VERIFIED (neuroscience / established research):
    ┌────────────────────────────────────────────────────────────┐
    │ Unconscious processing dominance (Dijksterhuis, Bargh)    │
    │ PFC capacity limits — 4±1 (Cowan 2001)                    │
    │ PFC energy cost (Raichle 2006)                             │
    │ Evolutionary timeline PFC vs subcortical                   │
    │ NE → α1 → PFC disconnect (Arnsten 2009)                   │
    │ Pattern recognition = expertise (Chase & Simon 1973)       │
    │ Approach-avoidance conflict (Lewin 1935, Miller 1944)      │
    │ Executive function override (Miller & Cohen 2001)          │
    │ Metacognition (Flavell 1979)                               │
    │ Predictive processing (Clark 2013, Friston)                │
    │ Parallel processing (multiple circuits simultaneously)     │
    │ Automatic behavior = established                           │
    │ Background monitoring (Posner 1980)                        │
    └────────────────────────────────────────────────────────────┘

  🟡 FRAMEWORK SYNTHESIS (consistent logic, derived from 🟢):
    ┌────────────────────────────────────────────────────────────┐
    │ Drive = observation parameter (not operator)               │
    │ Signal strength model (vs fixed layer priority)            │
    │ 6 PFC modes on 2-axis spectrum                             │
    │ Mode 3 vs 4 differentiated by chunks                       │
    │ 4 conflict types classification                            │
    │ 5 resolution rules                                         │
    │ Pull vs Push sustainability difference                     │
    │ Modern threat-drive dominance                              │
    │ Conflict as growth opportunity                              │
    │ Push→Pull transition paradox                                │
    │ Architecture B → drive emergent (v1.1)                     │
    │ Compiled/Fresh drive (F1/F2) distinction (v1.1)            │
    │ Domain=Arbiter — drive direction can be wrong (v1.1)       │
    └────────────────────────────────────────────────────────────┘

  🔴 HYPOTHESIS (logical but unverified):
    ┌────────────────────────────────────────────────────────────┐
    │ Exact PFC% per mode — approximation                        │
    │ Mode 1-2 = 70-80% of waking time — estimated              │
    │ Optimal pull:push ratio — unknown                          │
    │ Push→Pull transition conditions — unclear                  │
    │ Signal strength vs valence chain priority — case-dependent │
    └────────────────────────────────────────────────────────────┘
```

---

## §6 — CROSS-REFERENCES

```
  ← FOUNDATION (đọc trước):
    Core-v7.8-Draft.md §1 — cycle architecture
    Core-v7.8-Draft.md §8 — ALL observation parameters
    Observation/Novelty.md v1.0 — PULL mechanism deep-dive
    Observation/Threat.md v1.0 — PUSH mechanism deep-dive
    Inter-Body-Mechanism.md v1.0 §1.2 — Architecture B (general-purpose → drive emergent)
    Inter-Body-Mechanism.md v1.0 §3 — Compiled/Fresh (F1/F2 processing axis)
    Inter-Body-Mechanism.md v1.0 §7 — PFC=Lawyer (Domain=Arbiter correction)
    PFC-Configuration.md v1.0 — §2 participation modes ORTHOGONAL with config (2026-05-10)

  ← MECHANISM (đọc trước hoặc cùng):
    Body-Feedback-Mechanism.md v2.0 — chunk dynamics → body-feedback
    Chunk.md v2.0 — chunk substrate
    Valence-Propagation.md v2.0 — body evaluation, chain propagation
    Feeling.md v3.0 — PFC observation interface
    Cortisol-Baseline.md v2.0 — amplifier dynamics
    Body-Feedback-Label.md v2.0 — vocabulary reference

  ↔ SONG SONG (cùng Observation/ folder):
    Observation/Empathy.md v3.0 — SPM function → detect drives in others
    Observation/Liking-Wanting.md — wanting overlap drive mechanism
    Observation/AI-Schema-Detection.md — detect drive patterns
    Schema.md v2.0 — schema = observation parameter for chunk patterns

  → DOWNSTREAM:
    Imagine-Final-Evaluation.md — quality Imagine-Final → conflict resolution
    Anchor-Schema.md — Trust as tiebreaker in drive conflict

  → ỨNG DỤNG:
    Domain-Mapping-Drive.md — drive trong education context
    Boredom-Analysis.md — khi drive THIẾU target

  STATUS:
    v1.0 — 2026-04-20 — viết mới cho v7.8 cycle-based architecture
    v1.1 — 2026-05-17 — +Architecture B, +Compiled/Fresh, +Domain=Arbiter, version sync
    Rewrite từ: Drive.md v1.1-old (backup: _backup/Drive-v75-era/)
    Aligned: Core v7.8, Inter-Body-Mechanism v1.0, signal strength model
```
