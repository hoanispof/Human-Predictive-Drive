---
title: Addiction Analysis — Cơ Chế Nghiện Qua Kiến Trúc v7.8
version: 3.1
created: 2026-05-11
updated: 2026-05-15 (v3.1 — §10 3 misconceptions pattern + PTSD self-medication, Health Conditions Drill)
status: REFERENCE v3.1
scope: |
  OVERVIEW FILE: Nghiện HOẠT ĐỘNG THẾ NÀO qua v7.8 cycle-based architecture.
  Chunk-loop hijack mechanism. Type A/B reward bypass. Body-Coupling × Withdrawal.
  PFC-Configuration × Addiction states. Recovery = re-compilation pathway.
  3 nhóm phân loại (Chemical / Behavioral / Schema-based) — NGUYÊN LÝ, không drill từng chất.
  Self-medication pattern. Honest Assessment + Open Questions.
purpose: |
  OVERVIEW cho Chemical Hijack/ folder.
  Mô tả CƠ CHẾ TỔNG QUÁT — substance-specific drill ở file riêng:
    Alcohol-Brain-Mechanism.md (v1.0) — đã có.
    Các chất khác — drill sau nếu cần.
  Supersedes: Addiction-Analysis-v2.md (v7.5, backup/).
  v2 insight cốt lõi (dopamine ≠ reward, 4-phase, self-medication) → GIỮA LẠI, reframe v7.8.
  v3.0 NEW: Type A/B hijack, Body-Coupling withdrawal, PFC-Configuration mapping,
  Recovery re-compilation, Compile-Taxonomy × Addiction, Reward-Calibration × Tolerance.
position: Research/Chemical Hijack/ — OVERVIEW file, đọc trước substance-specific files.
dependencies:
  - Core-Software.md v1.0 — cycle architecture, 7-step
  - Core-Hardware.md v1.0 — 4 zones A/B/C/D, PFC reach gradient
  - Chunk.md v2.1 — chunk substrate, compile, trust gate
  - 03-Reward.md v1.1 — H10 5 preconditions, 7-step VTA, opioid = reward thật
  - Reward-Signal-Architecture.md v1.0 — Type A/B, A₀→A₃, A Gates B, 5 Profiles
  - Reward-Calibration.md v1.1 — Goldilocks per-gap, over-reward, premature compilation
  - Body-Feedback-Mechanism.md v1.2 — Sensory-Driven / Pattern-Driven, Chunk-Shift/Miss/Gap
  - Body-Coupling.md v1.1 — |❸| Depth × Direction, 3 Phase, Extension/Entanglement
  - Compile-Taxonomy.md v1.1 — 3 Loại A/B/C, 4 pathways
  - PFC-Configuration.md v1.0 — 6 dynamic modes
  - Cortisol-Baseline.md v2.0 — amplifier, 5 Roles, novelty vs threat
  - Dopamine-Is-Not-Reward.md v1.1 — dopamine ≠ reward, 7-step mechanism
  - PFC-Hardware.md v1.1 — COMT, DRD4, individual variation
  - Alcohol-Brain-Mechanism.md v1.0 — substance-specific reference (đã có)
  - Collective-Body.md v1.1 — Cấp 2 chains, drug culture
backup: Chemical Hijack/backup/Addiction-Analysis-v2.md
language: Tiếng Việt primary + English technical terms
confidence: 🟢 Research support | 🟡 Framework synthesis | 🔴 Hypothesis
---

# Addiction Analysis — Cơ Chế Nghiện Qua Kiến Trúc v7.8

> **Bạn scroll phone 2 tiếng. Tắt đi. Trống rỗng.**
> **Bạn uống rượu mỗi tối. Dừng 1 ngày. Bồn chồn không chịu nổi.**
> **Bạn làm việc 14h/ngày. Nghỉ phép. "Mất mình."**
>
> 3 nguồn KHÁC NHAU. Cùng 1 pattern: KHÔNG THỂ DỪNG dù BIẾT nên dừng.
>
> Pop science gọi: "nghiện dopamine." Framework nói: SAI.
> Dopamine = chuông cửa ("có gì đó đáng chú ý"). Nghiện = quà đằng sau cửa.
>
> Nghiện qua v7.8: **chunk-reward loop bị hijack**.
> Substance/behavior bypass H10 preconditions → deliver reward
> KHÔNG phục vụ body-need thật → compile "shortcut" chunks →
> tolerance = baseline shift → withdrawal = body-coupling disruption.
>
> File này: CƠ CHẾ TỔNG QUÁT — addiction hoạt động thế nào.
> Drill từng chất cụ thể → file riêng (Alcohol-Brain-Mechanism.md đã có).
>
> **Đọc trước**: Dopamine-Is-Not-Reward.md (tại sao dopamine ≠ reward).
> **Đọc trước hoặc song song**: 03-Reward.md (H10 5 preconditions).

---

## Mục lục

- §0 — VỊ TRÍ + SCOPE
- §1 — SỬA MISCONCEPTION: "NGHIỆN DOPAMINE" LÀ SAI
- §2 — CƠ CHẾ TỔNG QUÁT: CHUNK-REWARD LOOP HIJACK
- §3 — TYPE A/B × ADDICTION: TẤN CÔNG REWARD BẰNG CÁCH NÀO
- §4 — PHÂN LOẠI THEO CƠ CHẾ: 3 NHÓM
- §5 — WITHDRAWAL = BODY-COUPLING DISRUPTION
- §6 — PFC-CONFIGURATION × CÁC GIAI ĐOẠN NGHIỆN
- §7 — RECOVERY = RE-COMPILATION PATHWAY
- §8 — SELF-MEDICATION PATTERN
- §9 — HONEST ASSESSMENT + OPEN QUESTIONS
- §10 — CROSS-REFERENCES

---

## §0 — VỊ TRÍ + SCOPE

```
⭐ FILE NÀY TRONG FRAMEWORK:

  OVERVIEW cho Chemical Hijack/ folder.
  Mô tả CƠ CHẾ TỔNG QUÁT — addiction hoạt động thế nào qua v7.8.

  PHÂN BIỆT VỚI CÁC FILE KHÁC:

    ┌────────────────────────────┬───────────────────────────────────────┐
    │ File                       │ Scope                                  │
    ├────────────────────────────┼───────────────────────────────────────┤
    │ Addiction-Analysis.md      │ CƠ CHẾ TỔNG QUÁT: tại sao nghiện     │
    │ (FILE NÀY)                │ xảy ra, hoạt động thế nào, hồi phục  │
    │                            │ thế nào — KHÔNG drill từng chất.      │
    ├────────────────────────────┼───────────────────────────────────────┤
    │ Alcohol-Brain-Mechanism.md │ SUBSTANCE-SPECIFIC: ethanol × 5 hệ   │
    │ (v1.0, đã có)             │ thống não, BAC gradient, 6 biến thể  │
    │                            │ cá nhân, withdrawal cụ thể.           │
    ├────────────────────────────┼───────────────────────────────────────┤
    │ Alcohol-Vietnam-           │ CULTURAL-SPECIFIC: rượu bia × thế hệ │
    │ Generational.md (v1.0)    │ VN, gen ALDH2, xu hướng.              │
    ├────────────────────────────┼───────────────────────────────────────┤
    │ [Future substance files]  │ Per-substance drill: cocaine, opioid, │
    │                            │ nicotine, MDMA, cannabis...           │
    │                            │ NẾU CẦN — drill sau.                  │
    └────────────────────────────┴───────────────────────────────────────┘

  PATTERN ĐÃ CÓ TRONG FRAMEWORK:
    Body-Feedback.md (overview) → 01-Foundation, 02-Dissonance, 03-Reward (drill)
    Feeling.md (overview) → Feeling-Mechanism-Deep, Feeling-Sources (drill)
    Addiction-Analysis.md (overview) → Alcohol-Brain-Mechanism.md (drill)

  V2 → V3.0 REFRAME:
    v2 (v7.5): "Imagine layer DISCONNECT khỏi Body-Base"
    v3.0 (v7.8): "Chunk-reward loop bị hijack — H10 bypass + compile shortcut"
    v2 insight cốt lõi VẪN ĐÚNG — chỉ terminology + mechanism depth thay đổi.
```

---

## §1 — SỬA MISCONCEPTION: "NGHIỆN DOPAMINE" LÀ SAI

### §1.1 — 3 vị trí trong debate

```
🟢🟡 SO SÁNH 3 VỊ TRÍ — CÙNG CÂU HỎI, KHÁC CÂU TRẢ LỜI:

  ┌───────────────────────────────────────────────────────────────────┐
  │ CLASSICAL (1950s-1990s → pop science hiện tại):                    │
  │                                                                    │
  │   "Dopamine = reward/pleasure chemical."                           │
  │   "Nghiện = hệ dopamine bị hyperactive."                          │
  │   "Dopamine detox = giải pháp."                                   │
  │                                                                    │
  │   Vấn đề: 25+ năm research đã bác bỏ.                            │
  │   Pop science + textbook phổ thông VẪN lặp lại.                   │
  └───────────────────────────────────────────────────────────────────┘

  ┌───────────────────────────────────────────────────────────────────┐
  │ BERRIDGE-ROBINSON (1998-nay — current research consensus):         │
  │                                                                    │
  │   "Dopamine = WANTING (incentive salience), KHÔNG phải pleasure." │
  │   "Liking (pleasure) = primarily opioid system."                   │
  │   "Hai hệ TÁCH RỜI: có thể want without liking."                 │
  │                                                                    │
  │   Limitation: tách wanting/liking nhưng KHÔNG mô tả mechanism     │
  │   của liking cụ thể. "Opioid system" = black box.                 │
  └───────────────────────────────────────────────────────────────────┘

  ┌───────────────────────────────────────────────────────────────────┐
  │ FRAMEWORK v7.8:                                                    │
  │                                                                    │
  │   Dopamine = VTA detect delta → alert PFC: "CÓ BIẾN ĐỘNG"        │
  │   = CHUÔNG CỬA — signal salience, KHÔNG phải reward.              │
  │                                                                    │
  │   Reward = body-base opioid release KHI chunk fits body-need.      │
  │   = QUÀ ĐẰNG SAU CỬA — actual reward, phụ thuộc H10.            │
  │                                                                    │
  │   7-step mechanism (chi tiết: Dopamine-Is-Not-Reward.md §4):   │
  │   ① Neurons fire 24/7 → ② VTA detect delta → ③ DRD4 filter →    │
  │   ④ PFC spotlight → ⑤ Body-base check (body-need match?) →       │
  │   ⑥ Opioid release NẾU match → ⑦ COMT clear dopamine.            │
  │                                                                    │
  │   Bước ⑤ = CRITICAL: body-base CHECK.                             │
  │   Có body-need match → opioid → reward THẬT.                      │
  │   KHÔNG match → "meh" → PFC discard → TRỐNG RỖNG.                │
  │                                                                    │
  │   → "Nghiện dopamine" SAI vì:                                     │
  │   Dopamine = chuông cửa. Không ai nghiện tiếng chuông.            │
  │   Nghiện = content đằng sau (opioid body reward).                  │
  │                                                                    │
  │   v1.1 UPDATE: Opioid reward = primarily Type A (evaluative).     │
  │   Type B reward (touch, exercise) = non-opioid pathways.           │
  │   Chi tiết: Reward-Signal-Architecture.md §1-§3.                  │
  └───────────────────────────────────────────────────────────────────┘

  🟢 Berridge & Robinson 1998, 2003, 2016 — wanting ≠ liking.
  🟢 Schultz 1997 — prediction error signal.
  🟢 Koob & Volkow 2010 — addiction = allostatic, multi-system.
  Chi tiết 7 bằng chứng: Dopamine-Is-Not-Reward.md §3.
```

### §1.2 — Tại sao misconception này QUAN TRỌNG cho addiction

```
🟡 SAI CƠ CHẾ → SAI GIẢI PHÁP:

  Nếu tin "nghiện dopamine":
    → "Dopamine detox" = giải pháp → SAI
    → "Giảm dopamine" = mục tiêu → SAI (dopamine CẦN cho function)
    → "Chặn novelty" = cách cai → SAI (novelty = healthy drive)

  Nếu hiểu "nghiện = body reward bị hijack":
    → Câu hỏi đúng: "Body reward từ ĐÂU? Reward CÓ phục vụ body-need không?"
    → Giải pháp đúng: thay thế NGUỒN reward, không phải chặn signal
    → Recovery: re-build body reward từ nguồn THẬT (§7)

  Ví dụ: scroll MXH
    ❌ "Nghiện dopamine" → giải pháp: tắt phone → thất bại vì chưa
       có nguồn reward thay thế → quay lại scroll
    ✅ "Body reward nhẹ từ content" → giải pháp: thay thế bằng
       body reward MẠNH HƠN (exercise, connection thật, creative project)
       → scroll trở nên KHÔNG ĐỦ hấp dẫn
```

---

## §2 — CƠ CHẾ TỔNG QUÁT: CHUNK-REWARD LOOP HIJACK

### §2.1 — Normal cycle vs Addiction cycle

```
🟡 NORMAL CYCLE (v7.8 Core-Software.md):

  Domain → Body-Input → Unconscious Processing → Feeling → PFC → Body-Output → Domain
                                  ↑
                    Chunk-System evaluates:
                    Body-need gap? → Behavior → Input → Body-base check →
                    Match? → Opioid reward → Gap closes → DỪNG.

  ĐẶC ĐIỂM QUAN TRỌNG:
    ① Body-need gap THẬT tồn tại trước (P1 Schema pending)
    ② Behavior phục vụ gap đó (ăn khi đói, uống khi khát)
    ③ Body-base CHECK sau behavior: "có đáp ứng need không?"
    ④ Match → opioid → reward → gap closes → cycle DỪNG tự nhiên
    ⑤ H10 5 preconditions ĐỀU phải met (03-Reward.md §3)


  ADDICTION CYCLE — HIJACK Ở ĐÂU:

  ┌─────────────────────────────────────────────────────────────────────┐
  │                                                                     │
  │  HIJACK POINT 1 — H10 BYPASS:                                      │
  │                                                                     │
  │    Chemical tấn công TRỰC TIẾP receptor/neurotransmitter system     │
  │    → deliver opioid (hoặc opioid-like signal) KHÔNG CẦN P1-P5:     │
  │                                                                     │
  │    P1 (Schema pending — body-need gap):                             │
  │      Normal: cần gap THẬT. Addiction: chất tạo reward KHÔNG CÓ gap │
  │      hoặc gap KHÔNG LIÊN QUAN (đói → uống rượu, buồn → hút thuốc) │
  │                                                                     │
  │    P2 (Compiled chunks — evaluation capacity):                      │
  │      Normal: cần chunks để đánh giá "input có tốt không?"           │
  │      Addiction: chất BYPASS evaluation → reward trực tiếp            │
  │                                                                     │
  │    P3 (prediction-delta — novelty signal):                                 │
  │      Normal: cần prediction-delta. Addiction: chất FLOOD dopamine   │
  │      → VTA overwhelmed → signal bất thường                          │
  │                                                                     │
  │    P4 (Goldilocks — vừa đủ):                                       │
  │      Normal: ~40-70% match = optimal. Addiction: chất OVERRIDE      │
  │      → reward cường độ vượt xa Goldilocks → over-reward             │
  │                                                                     │
  │    P5 (Chunk tag — cortisol direction):                             │
  │      Normal: novelty cortisol → approach. Addiction: substance      │
  │      CÓ THỂ tag positive DÙ hại body (§2.3 false positive)        │
  │                                                                     │
  │  → CHEMICAL = BYPASS H10, deliver reward KHÔNG QUA body-base check  │
  │  → Behavioral = EXPLOIT H10 weaknesses (variable ratio, low cost)   │
  │                                                                     │
  └─────────────────────────────────────────────────────────────────────┘

  ┌─────────────────────────────────────────────────────────────────────┐
  │                                                                     │
  │  HIJACK POINT 2 — CYCLE KHÔNG DỪNG:                                │
  │                                                                     │
  │    Normal: body-need met → gap closes → cycle dừng tự nhiên.       │
  │    Addiction: reward KHÔNG phục vụ body-need thật →                 │
  │      gap KHÔNG ĐÓNG (vì need thật chưa met) →                     │
  │      cycle LẶP LẠI → reward nhẹ mỗi lần → compile "shortcut" →   │
  │      shortcut chunks MẠNH DẦN → override body signals khác.        │
  │                                                                     │
  │    Ví dụ: buồn (need = connection) → uống rượu → opioid nhẹ →     │
  │    buồn VẪN CÒN (connection chưa có) → uống thêm → opioid thêm → │
  │    loop KHÔNG có điểm dừng tự nhiên.                                │
  │                                                                     │
  └─────────────────────────────────────────────────────────────────────┘

  ┌─────────────────────────────────────────────────────────────────────┐
  │                                                                     │
  │  HIJACK POINT 3 — COMPILE "SHORTCUT" CHUNKS:                       │
  │                                                                     │
  │    Mỗi lần substance → reward:                                     │
  │    Body compile chunk: [tình huống X → dùng chất → reward]          │
  │    Lặp lại nhiều lần → chunk STRENGTHEN (Chunk.md §2 compile via   │
  │    repetition + emotional peak).                                    │
  │    Dần dần: chunk "shortcut" MẠNH HƠN chunks thay thế              │
  │    → activation probability CAO → fire trước chunks khác            │
  │    → body "tự động" hướng về substance.                             │
  │                                                                     │
  │    = Chunk-Activation-Dynamics.md: probability-weighted activation. │
  │    Chunk nghiện có probability CAO → fire TRƯỚC → dominate.         │
  │                                                                     │
  └─────────────────────────────────────────────────────────────────────┘
```

### §2.2 — 4-Phase Progression qua v7.8

```
🟡 4 GIAI ĐOẠN — CÙNG PATTERN CHO MỌI LOẠI NGHIỆN:

  Mức độ + tốc độ KHÁC NHAU per-substance/behavior,
  nhưng PROGRESSION LOGIC giống nhau.


  PHASE 1 — PULL (lần đầu → vài lần):

    Input → body reward THẬT (ít nhất lần đầu) → "sướng"
    → Body learns: [substance X → reward]
    → Chunk compile bắt đầu (Compile-Taxonomy: Pathway 1 — Hardware Fit)

    ⭐ ĐIỀU KIỆN TIÊN QUYẾT: body reward THẬT lần đầu.
    Nếu lần đầu KHÔNG có body reward → "chả có gì" → không lặp → không nghiện.
    Body PHẢI learn "X → reward" TRƯỚC khi nghiện có thể hình thành.

    🟢 Koob & Le Moal 2001 — initial positive reinforcement phase.


  PHASE 2 — TOLERANCE (lần 10-50+):

    Reward-Calibration.md: Goldilocks SHIFT.
    → Body adapts baseline: yesterday's reward = today's normal.
    → VTA habituate: cùng liều → delta NHỎ hơn → dopamine alert YẾU hơn.
    → Receptor downregulate: cần NHIỀU hơn cho cùng opioid response.
    → = Goldilocks zone DỊCH lên — cần liều CAO hơn để đạt "match."

    Đồng thời:
    → Hormone tự nhiên GIẢM sản xuất (body dựa vào chất thay vì tự sản).
    → Body reward từ nguồn THẬT (ăn ngon, gặp bạn) trở nên NHẠT
      so với chemical reward → anhedonia dần hình thành.
    → Chunk "shortcut" MẠNH hơn chunks thay thế.

    🟢 Koob & Volkow 2016 — opponent process theory, allostatic shift.
    🟢 Nestlé & Aghajanian 1997 — receptor downregulation.


  PHASE 3 — PUSH (lâu dài):

    CHUYỂN từ "dùng vì SƯỚNG" → "dùng vì KHÔNG DÙNG = KHỔ."

    → KHÔNG dùng = withdrawal:
      - Receptor đã downregulate → hormone tự nhiên CỰC THẤP
      - Cortisol TĂNG (Role ① Compile Direction: threat tag)
      - Body state CỰC TỆ → dissonance cường độ CAO
    → Dùng = HẾT withdrawal (relief, KHÔNG phải euphoria ban đầu)
    → = REWARD TYPE THAY ĐỔI:
      Phase 1: Pull reward = "sướng" (positive reinforcement)
      Phase 3: Push reward = "hết khổ" (negative reinforcement)
    → RSA: reward shift từ Profile ① Sensory/② Coherence →
      Profile ④ Relief (pain/dissonance stops = reward)

    🟢 Koob 2013 — negative reinforcement drives late-stage addiction.


  PHASE 4 — DEPENDENCY:

    → Hệ thống hormone SỤP HOÀN TOÀN.
    → Không dùng = body threat CỰC NẶNG
      (chemical: đau, run, nôn, có thể chết — tùy substance).
    → Chunk "shortcut" ĐÃ COMPILED SÂU:
      [cảm giác X → dùng chất] → automatic, PFC gần không can thiệp được.
    → Schema: "dùng X = SỐNG" (chất hijack từ luxury → survival need).
    → PFC-Configuration: withdrawal trigger Config ④ (Disconnected) →
      PFC offline → subcortical takeover → relapse probability CỰC CAO.

    🟢 Koob & Volkow 2010 — addiction as brain disease model.
    🟢 Arnsten 2009 — stress-induced PFC dysfunction.
```

### §2.3 — Tại sao body bị "lừa" — False Positive Mechanism

```
🟡 BODY-BASE CHECK (7-step bước ⑤) ĐÚNG 100% THỜI GIAN —
   VẤN ĐỀ LÀ CHEMICAL BYPASS CHECK, KHÔNG LỪA CHECK:

  Body-base check: "chunk này match body-need?"
  → Check mechanism VẪN HOẠT ĐỘNG đúng.
  → VẤN ĐỀ: chemical DELIVER opioid TRỰC TIẾP vào receptor,
    KHÔNG ĐI QUA check.

  Ví dụ heroin:
    Normal: [ăn ngon → taste → brainstem evaluate → match? → opioid]
    Heroin: [heroin → mu-opioid receptor TRỰC TIẾP → opioid]
    → Body-base check bị BYPASS, không phải bị lừa.
    → = Chất KHÔNG đi vào cửa trước (check) mà phá cửa sau (receptor).

  Ví dụ rượu:
    → GABA↑ → relaxation THẬT (body-state improves) = Type B reward
    → + opioid nhẹ (NAcc, Mitchell 2012) = Type A reward
    → Body-base check: "relaxation? ✅" → nhưng KHÔNG check:
      "relaxation CÓ PHỤ VỤ body-need lâu dài không?"
    → Body-base check = SHORT-TERM evaluator, không long-term planner.
    → PFC = long-term planner, nhưng PFC reach Zone C/D yếu (Core-Hardware.md §2).

  → FUNDAMENTAL LIMITATION:
    Body-base check evaluates IMMEDIATE FIT (short-term).
    Long-term consequence = PFC territory.
    Chemical BYPASS body-base check + PFC bị REDUCE/OFFLINE bởi chất.
    → = HAI tuyến phòng thủ ĐỀU bị vô hiệu hóa.
```

---

## §3 — TYPE A/B × ADDICTION: TẤN CÔNG REWARD BẰNG CÁCH NÀO

### §3.1 — Nguyên lý: Chemical tấn công Type A hay Type B?

```
🟡 REWARD CÓ 2 LOẠI (RSA v1.0 §1):

  Type A — EVALUATIVE CONFIRM:
    Circuit: Hedonic hotspot (NAcc shell, VP, mOFC). μ-opioid primary.
    H10: Full 5 preconditions REQUIRED.
    Learned: YES — quality depends on chunk library.
    Examples: Food, music, insight, social praise.

  Type B — DIRECT STATE CONFIRM:
    Circuit: Interoceptive / body-state regulation. VARIES by modality.
    H10: Simplified (P1 basic, P2-P5 reduced/N/A).
    Learned: MINIMAL — hardware from birth.
    Examples: Touch comfort, exercise, warmth, stretching.


  ADDICTION TẤN CÔNG CẢ HAI — NHƯNG BẰNG CÁCH KHÁC:

  ┌─────────────────────────────────────────────────────────────────────┐
  │                                                                     │
  │  TYPE A HIJACK — "PHÁ CỬA SAU EVALUATION":                        │
  │                                                                     │
  │    Normal Type A: Input → compiled chunks evaluate → match? →       │
  │    hedonic hotspot → μ-opioid → reward.                             │
  │    = Qua CỔNG ĐÁNH GIÁ (evaluation gate).                          │
  │                                                                     │
  │    Chemical hijack: substance → TRỰC TIẾP kích hoạt receptor →     │
  │    opioid signal → reward. KHÔNG qua evaluation gate.               │
  │                                                                     │
  │    Heroin/morphine: mu-opioid receptor TRỰC TIẾP.                  │
  │    Cocaine: block DAT → dopamine tràn + opioid indirect.           │
  │    Alcohol: opioid nhẹ ở NAcc (Mitchell 2012).                     │
  │                                                                     │
  │    → Type A bị hijack = "quà giả giao THẲNG, không qua kiểm tra." │
  │                                                                     │
  ├─────────────────────────────────────────────────────────────────────┤
  │                                                                     │
  │  TYPE B HIJACK — "BODY-STATE THAY ĐỔI THẬT NHƯNG KHÔNG BỀN":     │
  │                                                                     │
  │    Normal Type B: body activity → body-state DIRECTLY improves.     │
  │    = Hardware pathway, ít phụ thuộc chunks.                         │
  │                                                                     │
  │    Chemical hijack: substance thay đổi body-state THẬT:             │
  │    → Alcohol: GABA↑ = relaxation THẬT (muscle, anxiety giảm)       │
  │    → Cannabis: endocannabinoid = relaxation THẬT                   │
  │    → Nicotine: NE nhẹ = alertness THẬT                            │
  │                                                                     │
  │    Type B reward TỪ CHẤT = THẬT ở mức body-state.                 │
  │    VẤN ĐỀ: body-state improvement KHÔNG BỀN,                      │
  │    + receptor adapt → tolerance → cần nhiều hơn.                    │
  │    + body-state KHÔNG improve nếu không dùng (withdrawal).          │
  │                                                                     │
  │    → Type B bị hijack = "quà THẬT nhưng tạm thời + có giá."       │
  │                                                                     │
  ├─────────────────────────────────────────────────────────────────────┤
  │                                                                     │
  │  CẢ A + B ĐỒNG THỜI — NGUY HIỂM NHẤT:                            │
  │                                                                     │
  │    Hầu hết chất nghiện mạnh tấn công CẢ HAI TYPE:                 │
  │    → Heroin: Type A (opioid trực tiếp) + Type B (pain relief)      │
  │    → Cocaine: Type A (opioid indirect) + Type B (energy, alertness) │
  │    → Alcohol: Type A (opioid nhẹ) + Type B (GABA relaxation)       │
  │    → MDMA: Type A (serotonin → opioid cross) + Type B (warmth)     │
  │                                                                     │
  │    → Multi-channel attack = STRONGER hook:                          │
  │    body nhận reward từ NHIỀU nguồn đồng thời →                     │
  │    compile chunk MẠNH hơn (multi-modal compile, Chunk.md §2).      │
  │                                                                     │
  └─────────────────────────────────────────────────────────────────────┘

  🟢 Berridge 2003 — hedonic hotspot opioid mechanism.
  🟢 Mitchell et al. 2012 — alcohol triggers endorphin in NAcc + OFC.
  🟢 Fuss 2015 — endocannabinoid in exercise (Type B, non-opioid).
  🟢 Löken 2009 — CT afferents (Type B touch pathway).
```

### §3.2 — A Gates B mechanism × Addiction

```
🟡 NORMAL: TYPE A EVALUATION GATES TYPE B AMPLIFICATION (RSA §3):

  Khi cả A và B fire đồng thời:
    A positive → B AMPLIFIED (ăn ngon + ấm áp = cả hai tốt hơn)
    A negative → B SUPPRESSED (ăn ngon nhưng bạn vừa mắng = ăn mất ngon)
    = A "đánh giá context" → quyết định B có được amplify không.

  ADDICTION BYPASS GATE NÀY:

    Chemical → A fire TRỰC TIẾP (không qua evaluation) →
    B cũng fire (body-state thay đổi thật) →
    A KHÔNG đánh giá được "B này có tốt lâu dài không?" →
    = Gate bị vô hiệu hóa → cả A + B fire "unfiltered."

    → Giải thích tại sao chất gây nghiện cảm giác "toàn diện":
    không chỉ 1 loại sướng mà NHIỀU loại đồng thời (relaxation +
    euphoria + social ease + confidence...) = multi-type reward
    không có gate filtering.

  🔴 HYPOTHESIS: Cường độ nghiện ∝ f(số Type bị bypass × depth)
    → Heroin (A bypass trực tiếp + B pain relief) = CỰC MẠNH
    → Caffeine (B nhẹ: alertness) = NHẸ
    → Cannabis (B: relaxation + A nhẹ) = TRUNG BÌNH
    → Cần research thêm để xác nhận.
```

---

## §4 — PHÂN LOẠI THEO CƠ CHẾ: 3 NHÓM

### §4.1 — Nghiện Hóa Chất (Chemical Addiction)

```
🟢🟡 NGUYÊN TẮC: Chất tấn công TRỰC TIẾP hệ thống neurochemical.

  ĐẶC ĐIỂM CHUNG:
    → Bypass H10 evaluation gate (§2.1 Hijack Point 1)
    → Receptor downregulate → tolerance
    → Hormone tự nhiên GIẢM sản xuất
    → Withdrawal = body threat (nhẹ → cực nặng tùy chất)
    → Recovery: tháng → năm (receptor upregulate chậm)

  ĐỘ NGUY HIỂM = f(bypass depth × speed × receptor specificity):

    Bypass depth: heroin (mu-opioid TRỰC TIẾP) > cocaine (indirect)
                  > alcohol (multi-system nhẹ) > caffeine (adenosine block nhẹ)

    Speed: injection/smoking (giây) > snort (phút) > oral (30+ phút)
           → Speed ảnh hưởng compile: nhanh hơn = prediction-delta LỚN hơn
           → = chunk compile MẠNH hơn

    Receptor specificity: heroin = μ-opioid specific (cực mạnh)
                          > cocaine = DAT block (dopamine tràn)
                          > alcohol = multi-system nhẹ (5 hệ thống)
                          > caffeine = adenosine antagonist (rất nhẹ)

  DRD4 × CHEMICAL (PFC-Hardware.md):
    → 7R (threshold cao): cần LIỀU CAO hơn để feel initial effect
    → 4R (threshold thấp): feel effect ở LIỀU THẤP
    → 🟢 Có support: ADHD medication 7R cần liều cao hơn
    → ⚠️ CẢ HAI: reward từ opioid, KHÔNG từ dopamine

  Chi tiết per-substance: file riêng.
  Alcohol: Alcohol-Brain-Mechanism.md v1.0 (đã có — 5 hệ thống, BAC gradient).
  Các chất khác: drill sau nếu cần.
```

### §4.2 — Nghiện Hành Vi (Behavioral Addiction)

```
🟡 NGUYÊN TẮC: Hành vi tạo body reward THẬT từ body-base channels —
   KHÔNG tấn công hormone trực tiếp, nhưng EXPLOIT weaknesses trong H10.

  ĐẶC ĐIỂM CHUNG:
    → H10 KHÔNG bị bypass — nhưng bị EXPLOIT:
      - Variable ratio reinforcement → P3 prediction-delta LIÊN TỤC
      - Low cost behavior → lặp lại DỄ → compile NHANH
      - Multi-channel reward → multi-modal compile → MẠNH
    → Receptor KHÔNG downregulate nặng như chất
    → Withdrawal NHẸ hơn nhiều (không có body threat nặng)
    → Recovery NHANH hơn (ngày → tuần) — nhưng DỄ TÁI vì nguồn LUÔN available

  NGUYÊN LÝ PHÂN BIỆT VỚI CHEMICAL:

    Chemical: BYPASS evaluation gate → deliver reward TRỰC TIẾP.
    Behavioral: EXPLOIT gate → deliver reward QUA gate nhưng ở tần suất/
               pattern mà gate không designed to handle.

    Ví dụ: cờ bạc
      → Near-miss: VTA fire delta LỚN ("GẦN THẮNG!") → dopamine alert →
        body simulate anticipation reward → opioid NHẸ từ anticipation →
        gate evaluate: "gần thắng = có giá trị" → ✅ (gate ĐÚNG: gần thắng
        IS informative signal) → nhưng ở tần suất slot machine → exploit
      → 🟢 Clark et al. 2009: near-miss activate reward areas GIỐNG win.

    Ví dụ: MXH scroll
      → Mỗi scroll = content MỚI → prediction-delta nhỏ → dopamine nhẹ →
        body check: "liên quan?" → sometimes yes → opioid NHẸ →
        variable ratio = Skinner schedule → gate ĐÚNG per-event
        nhưng tổng thể = exploit continuous micro-reward.
      → 🟢 Meshi et al. 2013 — social media activates NAcc.

    Ví dụ: gaming
      → Multi-channel: mastery + novelty + status + belonging + shared experience
      → 5+ body-base channels ĐỒNG THỜI → multi-modal compile MẠNH
      → Game designed: difficulty curve + reward schedule + social hooks
      → Body reward THẬT per-channel — vấn đề là THAY THẾ real-world channels.


  SO SÁNH CHEMICAL vs BEHAVIORAL:

    ┌──────────────┬──────────────────────┬──────────────────────┐
    │ Đặc điểm     │ Chemical              │ Behavioral            │
    ├──────────────┼──────────────────────┼──────────────────────┤
    │ H10          │ BYPASS (phá cửa sau) │ EXPLOIT (lách cửa    │
    │              │                      │ trước ở tần suất cao) │
    ├──────────────┼──────────────────────┼──────────────────────┤
    │ Receptor     │ Downregulate NẶNG    │ Downregulate NHẸ     │
    ├──────────────┼──────────────────────┼──────────────────────┤
    │ Hormone      │ Sản xuất tự nhiên    │ Sản xuất tự nhiên    │
    │ tự nhiên     │ GIẢM                 │ VẪN bình thường       │
    ├──────────────┼──────────────────────┼──────────────────────┤
    │ Withdrawal   │ Body threat          │ Bồn chồn, restless   │
    │              │ (nhẹ → chết)         │ (không đe dọa sinh   │
    │              │                      │ mạng)                 │
    ├──────────────┼──────────────────────┼──────────────────────┤
    │ Recovery     │ Tháng → năm          │ Ngày → tuần          │
    ├──────────────┼──────────────────────┼──────────────────────┤
    │ Tái phạm     │ Schema cũ LUÔN CÒN  │ Nguồn LUÔN available │
    │              │ (chunk không xóa)    │ (phone, food, game)   │
    └──────────────┴──────────────────────┴──────────────────────┘
```

### §4.3 — Nghiện Schema (Schema-Based Addiction)

```
🟡🔴 NGUYÊN TẮC: Schema compiled quá sâu → TỰ DRIVE liên tục →
   override body "đủ rồi" signal.

  V7.8 REFRAME:
    v2: "Schema override body-base signals"
    v7.8: Chunk network compiled [hành vi X → body-need met] NHƯNG
          chunk network CŨNG compiled [chưa đủ X → threat] →
          2 chunk sets compete → "chưa đủ" chunk SET THẮNG liên tục.

  ĐẶC ĐIỂM KHÁC VỚI 2 NHÓM TRÊN:
    → KHÔNG có hóa chất, KHÔNG có hành vi cụ thể "nghiện"
    → Compile qua Pathway 2 (Trust Install) hoặc 3 (Social Default):
      "Phải hoàn hảo" → từ cha mẹ/culture compile vào → child trusts → installs
    → Body reward NHỎ nhưng LIÊN TỤC:
      mỗi lần comply schema → reward NHẸ ("tôi đang làm đúng")
    → Body "đủ rồi" signal → bị override bởi schema ("chưa đủ hoàn hảo")
    → = Reward-Calibration.md: Goldilocks zone bị DISTORT bởi compiled schema

  VÍ DỤ QUA V7.8:

    Perfectionism:
      → Chunk network: [hoàn hảo → an toàn → reward] + [chưa hoàn hảo → threat]
      → Mỗi lần "đủ tốt" → body signal satisfaction → NHƯNG chunk "chưa hoàn hảo"
        fire → threat → override satisfaction → tiếp tục → loop.
      → = Compile-Taxonomy: chunk "chưa đủ" compiled via Pathway 4 (Threat Avoidance)
        + Pathway 2 (Trust: cha mẹ nói "phải hoàn hảo").

    Workaholic:
      → Chunk network: [làm việc → mastery + status → reward] +
        [không làm → mất status → threat]
      → Cortisol Role ② Holding: PFC hold "công việc chưa xong" →
        cortisol sustained → không thể relax.
      → PFC-Configuration: stuck ở Mode 5 (Strategic) → không shift được.

    People-pleasing:
      → Chunk network: [người khác vui → connection reward] +
        [người khác không vui → connection threat]
      → SPM F1 fire liên tục → body respond người khác → exhaust
      → Empathy v2.0: burnout = f(L1 cao / L2 thấp).

  RECOVERY schema-based = KHÓ NHẤT:
    → Schema = identity level ("tôi là ai")
    → Bỏ schema = identity threat → Meaning.md v2.0: anchor disrupted
    → PFC phải draft schema MỚI override schema cũ
    → Chunk cũ KHÔNG XÓA ĐƯỢC (Chunk.md: never delete) → chỉ probability shift
    → = Cần compile chunk set MỚI mạnh hơn chunk set cũ.
```

---

## §5 — WITHDRAWAL = BODY-COUPLING DISRUPTION

### §5.1 — Hypothesis: Substance as Coupled Entity

```
🔴 HYPOTHESIS MỚI — SUBSTANCE TRỞ THÀNH BODY-COUPLED ENTITY:

  Body-Coupling.md v1.1: coupling xảy ra khi |❸| per-entity valence
  compile đủ sâu → entity trở thành phần cấu trúc của body-base.

  SUBSTANCE CÓ THỂ TRỞ THÀNH "ENTITY" TRONG HỆ THỐNG COUPLING KHÔNG?

  Argument FOR:
    → Repeated use + strong reward → positive ❸ builds dần
    → Substance trở thành phần body-base: "uống cà phê buổi sáng = tôi"
    → Removal → body responds TƯƠNG TỰ mất entity coupled:
      grief-like response (disorientation, yearning, emptiness)
    → Body-Coupling: Phase 1 (initiate) → Phase 2 (threshold) →
      Phase 3 (sustain) — timeline tương ứng 4-phase addiction

  Argument AGAINST (quan trọng):
    → Entity coupling trong Body-Coupling.md = PER-AGENT (con người)
    → Substance = OBJECT, không phải agent
    → VP §2: "Object KHÔNG BAO GIỜ có Body-Base Extension dimension"
    → Coupling require SPM (Self-Pattern-Match) → substance có SPM không?

  RESOLUTION — PARTIAL COUPLING:
    → Substance KHÔNG couple ở mức agent (no SPM, no L2 reward)
    → Substance CÓ THỂ couple ở mức BODY-STATE:
      Body state khi dùng substance = "normal"
      Body state khi KHÔNG dùng = "abnormal, threatening"
      = Body-BASE SHIFT, không phải agent coupling.
    → Gần hơn với Body-Feedback-Mechanism.md:
      Quality Baseline Shift (§5) — baseline DI CHUYỂN
      → removal = Chunk-Miss (baseline expected, not present)
    → = WITHDRAWAL = body-base baseline disruption + cortisol amplification,
      KHÔNG phải agent-level grief.

  ⚠️ NHƯNG: heavy addiction withdrawal CÓ grief-like features
    (yearning, identity disruption, emptiness) → partial overlap.
    Framework honest: mechanism chính xác CHƯA hoàn toàn rõ.
```

### §5.2 — Withdrawal Mechanism qua v7.8

```
🟡 WITHDRAWAL = BODY-BASE BASELINE BỊ PHÁ VỠ + CORTISOL AMPLIFICATION:

  ① RECEPTOR DOWNREGULATION (Tolerance đã xảy ra):
     → Body giảm receptor sensitivity + giảm sản xuất hormone tự nhiên
     → Baseline MỚI = "có chất = normal"
     → Removal chất = baseline bị PHÁ:
       hormone tự nhiên CỰC THẤP + receptor CHƯA upregulate kịp

  ② CHUNK-MISS DYNAMICS (BFM §3):
     → Body EXPECT body-state X (có chất) → body-state X KHÔNG ĐẾN
     → = Chunk-Miss: expected pattern không match reality
     → Dissonance signal MẠNH — tỷ lệ thuận với mức độ expect

  ③ CORTISOL AMPLIFICATION (Cortisol-Baseline.md §7.7):
     → Withdrawal = threat → cortisol sustained
     → Cortisol Role ① Compile Direction: tag withdrawal = THREAT
     → Cortisol Role ② Holding: PFC hold "cần chất" → cannot release
     → Cortisol Role ④ Inertia: withdrawal cortisol KÉOẢI dù đã qua peak
     → = Cortisol KHÔNG gây withdrawal, nhưng KHUẾCH ĐẠI + KÉO DÀI

  ④ PFC DEGRADATION:
     → Chronic substance use → PFC dendrite retraction
       (Cortisol-Baseline.md §9: PFC damage timeline)
     → Withdrawal + cortisol → PFC tiếp tục yếu →
       decision-making IMPAIRED → relapse probability TĂNG
     → = Vòng xoắn: withdrawal → cortisol → PFC yếu → khó cưỡng → relapse

  ⑤ GRADIENT WITHDRAWAL SEVERITY:
     → Chemical: Heroin > Alcohol (lâu năm) > Cocaine > Nicotine > Cannabis > Caffeine
     → Behavioral: NHẸ hơn nhiều (không receptor downregulate nặng)
     → Schema: identity crisis (không phải body withdrawal)

  🟢 Koob 2008 — anti-reward, allostatic load.
  🟢 Arnsten 2009 — PFC dysfunction under stress.
  🟢 Valenzuela 1997 — GABA-A downreg + NMDA upreg (alcohol-specific).
```

---

## §6 — PFC-CONFIGURATION × CÁC GIAI ĐOẠN NGHIỆN

```
🟡 PFC-CONFIGURATION.MD V1.0: 6 DYNAMIC MODES.
   MỖI GIAI ĐOẠN NGHIỆN → PFC Ở MODE KHÁC:

  ┌──────────────────┬──────────────────────┬──────────────────────────┐
  │ Giai đoạn        │ PFC Config           │ Mechanism                │
  ├──────────────────┼──────────────────────┼──────────────────────────┤
  │ Lần đầu thử     │ Config ① Normal       │ PFC evaluate bình thường │
  │                  │                      │ → "thử xem"              │
  │                  │                      │ → body reward → PFC note │
  ├──────────────────┼──────────────────────┼──────────────────────────┤
  │ Regular use      │ Config ① → ②         │ Substance-seeking tasks  │
  │ (Phase 1-2)     │ Reallocation         │ gets more PFC bandwidth  │
  │                  │                      │ → self-monitoring GIẢM   │
  │                  │                      │ → "biết hại nhưng mặc kệ"│
  ├──────────────────┼──────────────────────┼──────────────────────────┤
  │ Craving intense  │ Config ② extreme     │ PFC bandwidth ĐỔHẾT vào │
  │                  │ → approaching ④      │ seeking → other functions│
  │                  │                      │ gần mất → approaching    │
  │                  │                      │ subcortical takeover     │
  ├──────────────────┼──────────────────────┼──────────────────────────┤
  │ Withdrawal       │ Config ④             │ Cortisol cực cao + NE    │
  │ (Phase 3-4)     │ Disconnected         │ flood → PFC OFFLINE →    │
  │                  │                      │ subcortical takeover →   │
  │                  │                      │ compiled chunks RUN →    │
  │                  │                      │ relapse probability MAX  │
  ├──────────────────┼──────────────────────┼──────────────────────────┤
  │ "Using despite   │ Config ② + ④         │ PFC alternate giữa      │
  │  knowing"        │ oscillation          │ "biết hại" (①→②) và     │
  │                  │                      │ "không cưỡng được" (④)   │
  │                  │                      │ → oscillation = torment  │
  ├──────────────────┼──────────────────────┼──────────────────────────┤
  │ Recovery         │ Config ① stable      │ PFC cần STABLE Config ①  │
  │                  │ (cần rebuild)        │ để hold new schemas →    │
  │                  │                      │ compile competing chunks │
  │                  │                      │ → CẦN safe environment   │
  └──────────────────┴──────────────────────┴──────────────────────────┘

  ⭐ KEY INSIGHT:
    → "Biết hại mà vẫn dùng" = KHÔNG phải thiếu ý chí.
    → = PFC Config ④ (offline) khi craving/withdrawal →
      subcortical compiled chunks RUN → PFC không can thiệp được.
    → = PFC-Function.md: PFC ~200ms+, amygdala ~12ms →
      compiled addiction chunk fire TRƯỚC PFC can intervene.
    → = Tương tự tay rụt khỏi bếp nóng trước khi "biết nóng" —
      body respond trước, PFC biết sau.

  🟢 Goldstein & Volkow 2011 — impaired prefrontal function in addiction.
  🟢 Arnsten 2009 — stress-induced PFC dysfunction.
  🔴 Config oscillation model = framework hypothesis.
```

---

## §7 — RECOVERY = RE-COMPILATION PATHWAY

### §7.1 — Nguyên lý: Chunk không xóa, chỉ compete

```
🟡 CHUNK.MD V2.1: BRAIN KHÔNG BAO GIỜ XÓA CHUNK.
   Recovery = KHÔNG "xóa nghiện." Recovery = BUILD chunk set MỚI mạnh hơn.

  ① Chunk nghiện VẪN TỒN TẠI — chỉ activation probability GIẢM.
     → Trigger (context, stress, people) → chunk CÓ THỂ fire lại
     → = Tại sao relapse CÓ THỂ xảy ra NHIỀU NĂM sau cai
     → = Chunk.md: "never delete — only probability shift"

  ② Recovery = compile chunk set MỚI competing cùng trigger:
     → Trigger cũ: [stress → dùng chất → reward]
     → Chunk mới: [stress → exercise → reward THẬT] hoặc
                  [stress → gọi bạn → connection reward]
     → 2 chunk sets compete → chunk MẠNH HƠN win
     → Recovery = làm chunk mới MẠNH hơn chunk cũ

  ③ Chunk mới compile CHẬM (cùng 4 mechanisms: repetition + emotional peak
     + multi-modal + sleep):
     → Chunk nghiện đã compile NHIỀU NĂM → rất mạnh
     → Chunk mới bắt đầu từ 0 → cần THỜI GIAN + LẶP LẠI + SLEEP
     → = Tại sao recovery = process dài, không phải event

  ④ ENVIRONMENT quan trọng:
     → Environment chứa TRIGGER → chunk nghiện fire → probability TĂNG lại
     → Environment MỚI = ít trigger → chunk mới có SPACE compile
     → 🟢 Alexander 1978 "Rat Park": chuột có environment tốt → ít nghiện
     → = Environment xóa trigger surface → cho chunk mới cơ hội
```

### §7.2 — Type B as Recovery Floor

```
🟡 RSA V1.0 §1.4: TYPE B = "EVOLUTIONARY FLOOR" — ALWAYS AVAILABLE.

  Type A (evaluative): CÓ THỂ bị damage bởi addiction
    → Receptor downregulate → A₁-A₃ evaluation impaired
    → Anhedonia: "ăn mà không thấy ngon, nghe nhạc mà trống rỗng"

  Type B (direct state): HARDWARE-BASED → VẪN accessible
    → Touch comfort: CT afferents VẪN hoạt động
    → Exercise: endocannabinoid pathway VẪN hoạt động
    → Warmth, stretching: interoceptive pathways VẪN hoạt động

  → TYPE B = "BACKDOOR" KHI TYPE A BỊ STUCK:
    → Anhedonia (A exhausted) → B vẫn có thể provide BASELINE reward
    → Body-oriented approaches: exercise, massage, yoga, nature walk
    → 🟢 Van der Kolk 2014: body-oriented therapy effective for trauma/addiction
    → = Activate B pathways → body gets SOME reward →
      cortisol giảm nhẹ → PFC stabilize → Config ① possible →
      A recovery can BEGIN

  → Recovery pathway:
    B floor (stabilize) → PFC Config ① (rebuild) → A gradually recovers →
    new chunks compile → competing with addiction chunks
```

### §7.3 — Social Coupling as Recovery Resource

```
🟡 CONNECTION.MD V3.1 + BODY-COUPLING.MD V1.1:

  Social connection provides:
    → L1 reward (SPM-owned, momentary — gặp bạn → cảm giác tốt)
    → L2 reward (Entity-compiled, structural — bạn thân = body-base extension)
    → = ALTERNATIVE reward source không cần substance

  Recovery programs (AA, NA, therapy groups):
    → Group = connection reward THẬT
    → Shared experience = SPM F1 fire → empathy → L1 reward
    → Sustained relationship = L2 coupling builds → structural support
    → = Body-Coupling: positive coupling với người MỚI →
      competing với substance "coupling"

  ⚠️ NHƯNG:
    → Addiction đã DAMAGE connection capacity:
      - PFC weakened → SPM impaired → connection khó hơn
      - Trust chunks: nhiều người nghiện đã phá trust → chunk [people → threat]
      - Isolation → ít connection chunks → SPM library NGHÈO
    → = Recovery cần PATIENCE + safe context cho SPM rebuild

  🟢 Heilig et al. 2016 — social factors in addiction recovery.
  🟢 Kelly et al. 2020 — AA mechanism: social network change.
```

### §7.4 — Compile-Taxonomy × Recovery

```
🟡 COMPILE-TAXONOMY.MD V1.1: Recovery chunks compile qua 4 pathways —
   nhưng KHÁC NHAU per-pathway:

  Pathway 1 — Hardware Fit (body tự reward):
    → Exercise → endorphin/endocannabinoid → body reward THẬT
    → Repeat → compile [exercise → reward] → competing chunk
    → MẠNH vì body reward THẬT (không cần trust, không cần social)
    → = Pathway phục hồi TỰ NHIÊN nhất

  Pathway 2 — Trust Install:
    → Therapist/sponsor nói "bạn có thể hồi phục"
    → Trust compile → chunk [recovery → possible]
    → QUAN TRỌNG cho giai đoạn đầu khi body chưa cho reward
    → ⚠️ Trust fragile: 1 relapse → "trust sai → mình không thể"

  Pathway 3 — Social Default:
    → Recovery community: "mọi người ở đây đều đang recovery"
    → Social default: recovery = norm → compile nhẹ nhàng
    → = AA/NA model: collective default shift

  Pathway 4 — Threat Avoidance:
    → "Nếu dùng lại → mất gia đình, mất việc"
    → Compile [dùng lại → threat] → avoidance chunk
    → ⚠️ Pathway này KHÔNG TẠO reward — chỉ tạo avoidance
    → Không sustainable nếu KHÔNG có Pathway 1-3 bổ sung

  → Recovery TỐT NHẤT: multi-pathway simultaneously.
    Body exercise (1) + therapist trust (2) + recovery group (3) + consequences aware (4)
    = 4 pathways compile CÙNG LÚC → new chunks MẠNH nhanh hơn.
```

---

## §8 — SELF-MEDICATION PATTERN

```
🟡 SELF-MEDICATION: DÙNG CHẤT ĐỂ XỬ LÝ DISSONANCE CÓ SẴN.

  Pattern phổ biến: người có dissonance lâu dài (anxiety, depression,
  trauma, loneliness) → tìm substance → substance GIẢM dissonance →
  "thuốc" → dependency.


  QUA V7.8:

  ① Dissonance tồn tại (nhiều nguồn):
     → Social isolation → Connection dissonance
     → Trauma → Background-Pattern.md: compiled threat pattern
     → Anxiety → Cortisol Role ② Holding: sustained cortisol
     → Boredom → Boredom.md: Imagine-Final chưa rõ + dissonance nhẹ liên tục

  ② Substance GIẢM dissonance THẬT (ngắn hạn):
     → Alcohol: GABA↑ → anxiety GIẢM THẬT (Type B: body-state improves)
     → Cannabis: endocannabinoid → relaxation THẬT
     → Opioids: pain relief THẬT (cả physical VÀ emotional pain)
     → = Body-Feedback-Mechanism.md: Chunk-Miss giảm (expected state MET)

  ③ Loop hình thành:
     → Dissonance → substance → relief (reward) → dissonance quay lại
       (vì ROOT CAUSE chưa resolved) → substance lại → tolerance →
       cần nhiều hơn → dependency
     → = Body learn: [dissonance → substance → relief]
     → Chunk compile VÀ strengthen mỗi lần lặp

  ④ Root cause VẪN INTACT:
     → Substance chỉ giảm SYMPTOM (dissonance), không fix SOURCE
     → Isolation vẫn isolation. Trauma pattern vẫn intact.
     → = Giống uống thuốc giảm đau mà không chữa xương gãy


  SELF-MEDICATION × PFC-CONFIGURATION:

    → Dissonance sustained → cortisol sustained →
      PFC approaching Config ④ (Disconnected) →
      decision quality GIẢM → substance = "easy fix" →
      PFC khi dùng substance: temporary shift ① (GABA relax PFC) →
      "cảm giác bình thường trở lại" → reinforce

    → = Tại sao self-medication CỰC KHÓ bỏ:
      substance = ONLY thing that restores Config ① temporarily.
      Bỏ → Config ④ (or approaching) → CHỊU KHÔNG NỔI → quay lại.

    → Recovery: phải fix ROOT CAUSE (trauma, isolation, anxiety)
      → PFC stable ở Config ① WITHOUT substance
      → THEN substance no longer needed for self-medication.


  🟢 Khantzian 1985, 1997 — self-medication hypothesis.
  🟢 Turner et al. 2018 — trauma-substance use comorbidity.
```

---

## §9 — HONEST ASSESSMENT + OPEN QUESTIONS

### §9.1 — Confidence Map

```
  ┌──────────────────────────────────────┬──────────────────────┐
  │ Claim                                │ Confidence             │
  ├──────────────────────────────────────┼──────────────────────┤
  │ Dopamine ≠ reward                    │ 🟢 Berridge 1998+     │
  │ 4-phase progression                  │ 🟢 Koob & Volkow      │
  │ Receptor downregulation → tolerance  │ 🟢 Established         │
  │ PFC impaired in addiction            │ 🟢 Goldstein 2011     │
  │ Self-medication pattern              │ 🟢 Khantzian 1985     │
  │ Environment affects recovery         │ 🟢 Alexander 1978     │
  │ Body-oriented therapy effective      │ 🟢 Van der Kolk 2014  │
  ├──────────────────────────────────────┼──────────────────────┤
  │ H10 bypass model (§2.1)             │ 🟡 Framework synthesis │
  │ Type A/B × addiction mapping (§3)   │ 🟡 Framework synthesis │
  │ 4-phase × chunk dynamics (§2.2)     │ 🟡 Framework synthesis │
  │ PFC-Config × addiction stages (§6)  │ 🟡 Framework synthesis │
  │ Recovery = re-compilation (§7)      │ 🟡 Framework synthesis │
  │ Schema-based addiction (§4.3)       │ 🟡 Framework synthesis │
  ├──────────────────────────────────────┼──────────────────────┤
  │ Substance as body-coupling (§5.1)   │ 🔴 Hypothesis          │
  │ A Gates B bypass model (§3.2)       │ 🔴 Hypothesis          │
  │ Addiction severity formula (§3.2)   │ 🔴 Hypothesis          │
  │ Config oscillation model (§6)       │ 🔴 Hypothesis          │
  └──────────────────────────────────────┴──────────────────────┘
```

### §9.2 — What Framework ADDS vs What Already Exists

```
🟡 FRAMEWORK KHÔNG "PHÁT MINH" ADDICTION THEORY.
   Framework REFRAME existing knowledge qua v7.8 architecture:

  ĐÃ CÓ (framework đồng ý + cite):
    → Berridge wanting ≠ liking → framework ĐỒNG Ý + thêm 7-step mechanism
    → Koob allostatic model → framework ĐỒNG Ý + reframe bằng chunk dynamics
    → Khantzian self-medication → framework ĐỒNG Ý + reframe bằng dissonance
    → Goldstein PFC impairment → framework ĐỒNG Ý + map vào 6 Config modes

  FRAMEWORK THÊM:
    → H10 bypass model: formalize TẠI SAO substance bypass body-base check
    → Type A/B × addiction: formalize LOẠI REWARD NÀO bị tấn công
    → Chunk competition model: recovery = new chunks vs addiction chunks
    → PFC-Configuration × stages: formalize PFC state per-phase
    → Compile-Taxonomy × recovery: 4 pathways for building competing chunks

  FRAMEWORK CHƯA GIẢI QUYẾT:
    → Substance as coupled entity: partial hypothesis, chưa rõ mechanism
    → A Gates B bypass: logical but untested
    → Individual variation: DRD4 × substance-specific → cần research
    → Behavioral addiction boundary: khi nào "thói quen" thành "nghiện"?
```

### §9.3 — Open Questions

```
  Q1: "Healthy addiction" có tồn tại không?
      → "Nghiện" exercise, "nghiện" sáng tạo, "nghiện" học?
      → = Body reward THẬT + phục vụ body-need THẬT
      → Nếu H10 preconditions MET + body-need THẬT → gọi "addiction"?
      → Hay gọi "sustained drive" / "flow" / "Imagine-Final pursuit"?
      → Framework lean: nếu body reward THẬT + need THẬT → KHÔNG phải addiction
        (vì cycle DỪNG tự nhiên khi need met).
      → ⚠️ NHƯNG: exercise CÓ THỂ trở thành compulsive (injury ignore)
        → boundary CHƯA rõ.

  Q2: Behavioral addiction boundary?
      → Khi nào scroll MXH = thói quen vs nghiện?
      → Khi nào gaming = hobby vs nghiện?
      → Framework suggest: khi behavior KHÔNG DỪNG dù body signals dissonance
        (fatigue, isolation, pain) → override body = addiction territory.
      → NHƯNG: threshold CHƯA quantifiable.

  Q3: AI addiction?
      → AI conversation = Novelty (chunks mới) + Coherence (hiểu) +
        "Being Seen" (AI "hiểu" bạn) → body reward từ 3+ channels
      → GIỐNG MXH nhưng SÂU HƠN (personalized + interactive + responsive)
      → Behavioral addiction pattern applicable?
      → 🔴 Chưa có research (quá mới).

  Q4: Cross-substance interaction?
      → Alcohol + nicotine: synergy? Competitive? Independent?
      → Multi-substance user: body-coupling với MỖI substance hay TỔNG THỂ?
      → Framework chưa model interaction between substances.

  Q5: Epigenetic transmission?
      → Cha/mẹ nghiện → con có baseline KHÁC? Receptor density khác?
      → Framework: "hardware sets range, chunks choose position"
        (Core-Hardware.md §6) → epigenetic = range shift?
      → 🟢 Vassoler et al. 2014 — epigenetic changes in offspring of addicts.
      → Mechanism qua v7.8: CHƯA model.

  Q6: Schema-based addiction × OCD?
      → OCD-Analysis.md v2.1: 3-tuyến model (anxiety / habit / mixed)
      → Schema-based addiction (perfectionism, control) overlap OCD?
      → Framework predict: KHÁC mechanism gốc (OCD = serotonin-mediated
        3-tuyến, schema addiction = trust-installed compile) NHƯNG surface
        behavior có thể giống → misdiagnosis risk.
```

---

## §10 — CROSS-REFERENCES

```
  CORE FILES (mechanism foundation):
    → Core-Software.md v1.0 — cycle architecture, 7-step
    → Core-Hardware.md v1.0 — 4 zones, PFC reach gradient
    → Chunk.md v2.1 — compile, never delete, probability-weighted activation
    → Chunk-Activation-Dynamics.md — probability, competitive re-linking, trigger surface

  REWARD SYSTEM (bị hijack):
    → 03-Reward.md v1.1 — H10 5 preconditions, 7-step VTA
    → Reward-Signal-Architecture.md v1.0 — Type A/B, A₀→A₃, A Gates B
    → Reward-Calibration.md v1.1 — Goldilocks, over-reward, premature compilation
    → Dopamine-Is-Not-Reward.md v1.1 — dopamine ≠ reward, 7 bằng chứng
    → Liking-Wanting.md v1.0 — bridge Berridge, wanting mechanisms

  BODY SYSTEM (withdrawal + coupling):
    → Body-Feedback-Mechanism.md v1.2 — Sensory/Pattern-Driven, Chunk-Shift/Miss/Gap
    → Body-Coupling.md v1.1 — |❸| Depth × Direction, Extension/Entanglement
    → Cortisol-Baseline.md v2.0 — amplifier, 5 Roles, novelty vs threat

  PFC SYSTEM (impairment + recovery):
    → PFC-Configuration.md v1.0 — 6 modes, survival matrix
    → PFC-Function.md v1.2 — 24 functions, PFC offline
    → PFC-Hardware.md v1.1 — COMT, DRD4, individual variation

  COMPILE + RECOVERY:
    → Compile-Taxonomy.md v1.1 — 3 Loại A/B/C, 4 pathways
    → Background-Pattern.md v1.1 — invisible bias, sleep = accelerator
    → Connection.md v3.2 — social coupling, L1/L2 reward

  HEALTH CONDITIONS DRILL (v3.1):

    3 MISCONCEPTIONS UNIFIED PATTERN (Nicotine-Brain-Mechanism.md §5):
      → Nicotine: ① "stress relief" (actually: withdrawal relief) ② "focus enhancer"
        (actually: baseline restore) ③ "social facilitator" (actually: anxiety relief)
      → = Pattern: WITHDRAWAL MASQUERADES as benefit → applies to ALL substance addiction
      → Same pattern in caffeine, alcohol, benzodiazepines → generalized addiction misconception

    PTSD SELF-MEDICATION BRIDGE (PTSD-Analysis.md §12.1):
      → 🟢 Khantzian 1985: self-medication hypothesis
      → PTSD → chronic hyperarousal/dysphoria → substance USE = attempted regulation
      → Framework: context-free chunks fire → body in threat → substance DAMPENS signal
      → NOT "weak willpower" — BODY SEEKING REGULATION via available tools

    Cross-refs:
      → Nicotine-Brain-Mechanism.md v1.1 §5 (3 misconceptions)
      → PTSD-Analysis.md v1.0 §12.1 (self-medication bridge)

  SUBSTANCE-SPECIFIC (drill files):
    → Alcohol-Brain-Mechanism.md v1.0 — ethanol × 5 hệ thống não
    → Alcohol-Vietnam-Generational.md v1.0 — VN context

  RELATED RESEARCH:
    → OCD-Analysis.md v2.1 — overlap schema-based addiction? (Q6)
    → Boredom.md — dissonance + self-medication trigger
    → Meaning.md v2.0 — identity anchor × schema addiction

  BACKUP (superseded):
    → backup/Addiction-Analysis-v2.md — v7.5 framing, insight cốt lõi giữ lại
    → backup/Addiction-Analysis.md — v7.0, historical
    → backup/Chemical-Enhancement-Notes.md — raw notes, partial coverage
```
