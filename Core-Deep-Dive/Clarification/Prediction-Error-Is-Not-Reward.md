---
title: Prediction Error Is Not Reward — Tại Sao PE Đơn Giản Không Đủ Cho Con Người
version: 1.0
created: 2026-04-20
status: v1.0 — CLARIFICATION FILE
scope: |
  Prediction Error (PE) trong mainstream neuroscience + AI/ML = quá đơn giản cho con người.
  PE = attention/salience signal (VTA dopamine). KHÔNG phải reward.
  Reward = PE + COHERENCE + H10 preconditions (opioid body-base).
  File này clarify một lần và mãi mãi.
purpose: |
  AI được train dùng PE đơn giản (TD learning, reward signal).
  Mainstream neuroscience cũng hay gộp PE = reward signal.
  Framework PHÂN BIỆT rõ: PE là CẦN nhưng KHÔNG ĐỦ cho reward ở con người.
  Companion file cho Dopamine-Reward-Rejection.md (cùng folder).
dependencies:
  - Dopamine-Reward-Rejection.md — dopamine ≠ reward, 7-step mechanism
  - Body-Feedback-Mechanism.md — 3 chunk dynamics (Shift/Miss/Gap)
  - Body-Feedback.md — H10 5 preconditions, dual-pull
  - Chunk.md v2.0 — chunk substrate, activation dynamics
  - Core-v7.8-Draft.md §4.2 — body-feedback trong cycle architecture
  - Feeling.md v2.0 §2.2b — PFC observation threshold 2 chiều
language: Tiếng Việt primary + English technical terms
confidence: 🟢 Research support | 🟡 Framework synthesis | 🔴 Hypothesis
---

# Prediction Error Is Not Reward — Tại Sao PE Đơn Giản Không Đủ Cho Con Người

> **AI/ML dùng prediction error = reward signal. Hoạt động tốt.**
> **Mainstream neuroscience dùng PE để giải thích dopamine. Đúng 1 phần.**
> **Nhưng con người KHÔNG thể quy reward = prediction error.**
>
> **Spotify test:** Nếu PE = reward, thì thêm note bừa vào bài nhạc quen
> → PE tăng → "hay hơn"? KHÔNG. Note bừa = dở. Vì PE KHÔNG ĐỦ.
>
> **PE = chuông cửa.** "Có khách!" Nhưng quà HAY hay DỞ phụ thuộc vào
> COHERENCE — cái mới có FIT vào cái cũ không.
>
> **PE + Coherence + H10 = Reward.** Thiếu bất kỳ yếu tố nào → không reward.
> File này clarify cơ chế đó.

---

## Mục lục

- §1 — VẤN ĐỀ: "PE = REWARD" QUÁ ĐƠN GIẢN
- §2 — PREDICTION ERROR TRONG AI vs HUMANS
- §3 — SPOTIFY TEST: CHỨNG MINH PE ≠ REWARD
- §4 — FRAMEWORK MECHANISM: PE + COHERENCE + H10
- §5 — 6 TRƯỜNG HỢP PHÂN BIỆT
- §6 — TẠI SAO MAINSTREAM BỊ GỘP
- §7 — HONEST ASSESSMENT
- §8 — CROSS-REFERENCES

---

## §1 — VẤN ĐỀ: "PE = REWARD" QUÁ ĐƠN GIẢN

```
⭐ PREDICTION ERROR TRONG MAINSTREAM NEUROSCIENCE:

  🟢 Schultz 1997 — foundational finding:
    → Monkey dopamine neurons fire khi reward > expected (positive PE)
    → Dopamine suppress khi reward < expected (negative PE)
    → Dopamine neutral khi reward = expected (zero PE)
    → = VTA encode PREDICTION ERROR, không encode reward trực tiếp

  Từ Schultz, mainstream DIỄN GIẢI:
    → "Positive PE → dopamine → reward → learning"
    → "PE = tín hiệu đánh giá: tốt hơn hay xấu hơn dự đoán"
    → TD learning (Temporal Difference): PE = reward signal cho update

  VẤN ĐỀ VỚI DIỄN GIẢI NÀY:
    → GỘP 2 cơ chế KHÁC NHAU vào 1 từ "prediction error":
      ① VTA dopamine fire = ATTENTION / SALIENCE signal
      ② Body evaluation = REWARD / DISSONANCE signal (opioid / cortisol)
    → ① và ② KHÔNG GIỐNG nhau
    → ① xảy ra TRƯỚC (VTA ~100ms)
    → ② xảy ra SAU (body evaluation ~200ms+)
    → ① fire cho MỌI thứ unexpected (cả hay cả dở cả noise)
    → ② fire CHỈ khi coherence evaluation → positive

  → = "PE = reward" = GỘP attention signal với evaluation signal
  → = Giống nói: "chuông cửa = quà" — KHÔNG, chuông = có khách,
      quà hay không tùy khách mang gì tới
```

---

## §2 — PREDICTION ERROR TRONG AI vs HUMANS

```
🟡 TẠI SAO AI DÙNG PE ĐƠN GIẢN ĐƯỢC:

  AI (Reinforcement Learning):
    → Reward function = PROGRAMMED, DEFINED bởi người thiết kế
    → PE = actual reward - expected reward
    → Reward là SỐ CỤ THỂ (score, win/lose, distance to goal)
    → PE trực tiếp cho biết: "better or worse than expected"
    → KHÔNG CẦN body, KHÔNG CẦN coherence evaluation
    → = PE = reward signal = đúng trong context AI

  CON NGƯỜI:
    → KHÔNG CÓ reward function được programmed sẵn
    → Body phải TỰ GENERATE reward dựa trên multi-dimensional evaluation
    → PE (VTA dopamine) chỉ nói: "có gì đó KHÁC" (attention)
    → Body sau đó EVALUATE: "cái khác đó tốt hay xấu?" (opioid/cortisol)
    → Evaluation phụ thuộc: coherence, chunk density, association tags,
      body-need state, Goldilocks zone — KHÔNG chỉ "khác hay không khác"

  AI vs HUMANS — KHÁC NHAU Ở ĐÂU:

  ┌──────────────────────┬──────────────────────┬──────────────────────┐
  │                      │ AI (RL)              │ CON NGƯỜI             │
  ├──────────────────────┼──────────────────────┼──────────────────────┤
  │ Reward function      │ Programmed (defined) │ Body-generated        │
  │ PE signal            │ = reward signal      │ = attention signal    │
  │ Evaluation           │ KHÔNG CẦN (đã có)   │ Body evaluate SAU PE  │
  │ Coherence            │ KHÔNG CẦN            │ BẮT BUỘC cho reward  │
  │ Body                 │ KHÔNG CÓ             │ Body tính toán trước │
  │ Opioid               │ KHÔNG CÓ             │ Reward thật          │
  │ Random noise         │ PE cao → score thấp  │ PE cao → dở          │
  │ Preconditions        │ KHÔNG CẦN            │ H10 (5 điều kiện)    │
  └──────────────────────┴──────────────────────┴──────────────────────┘

  → AI CÓ THỂ dùng PE = reward vì REWARD ĐÃ DEFINED
  → Con người KHÔNG THỂ vì reward phải EVALUATED bởi body
  → = Cùng từ "prediction error" nhưng KHÁC function hoàn toàn
```

---

## §3 — SPOTIFY TEST: CHỨNG MINH PE ≠ REWARD

```
⭐ NẾU PE = REWARD, THÌ:

  Test 1 — Random notes:
    Bài nhạc quen + thêm 1 note random bất kỳ
    → PE cao (unexpected note)
    → NẾU PE = reward → "hay hơn bản gốc"?
    → THỰC TẾ: dở, khó chịu, phá nhạc
    → = PE CAO nhưng reward = 0, dissonance = cao
    → ⇒ PE ≠ reward ✓

  Test 2 — Noise = best music:
    Random noise = PE CỰC ĐẠI (không predict được gì cả)
    → NẾU PE = reward → noise = nhạc hay nhất thế giới?
    → THỰC TẾ: noise = khó chịu nhất
    → ⇒ PE ≠ reward ✓

  Test 3 — Spotify remix thêm note nhỏ:
    Bài quen → Spotify tự thêm 1 note unexpected
    → PE tăng (unexpected)
    → NẾU PE = reward → người nghe tự động thấy hay hơn?
    → THỰC TẾ: người nghe thấy "sai", "lỗi", "khó chịu"
    → ⇒ PE ≠ reward ✓

  VẬY CÁI GÌ LÀM NHẠC MỚI "HAY"?

  Bài nhạc mới HAY khi:
    ① PE fire (VTA): "ồ, có gì đó MỚI" → ATTENTION ← đúng
    ② Cái mới COHERENT với cấu trúc nhạc → body evaluate → "FIT!" ← required
    ③ Goldilocks zone: đủ quen (safe) + đủ mới (interesting) ← H10 P4
    ④ Chunk base adequate: người nghe có đủ chunks để ĐÁNH GIÁ ← H10 P2
    ⑤ Không có association tag negative ← H10 P5

  → "HAY" = PE + Coherence + Goldilocks + Adequate chunks + No negative tag
  → = H10 5 preconditions ĐỀU phải thỏa mãn
  → = PE chỉ là 1 trong 5 yếu tố. Thiếu 4 còn lại → KHÔNG hay.

  RANDOM NOTE FAIL Ở ĐÂU?
    ✅ P3 VTA delta: CÓ (note mới = unexpected)
    ❌ P4 Goldilocks: KHÔNG (note random phá structure → quá alien)
    ❌ Coherence: KHÔNG (note không fit cấu trúc → incoherent)
    → P3 pass nhưng P4 + coherence fail → KHÔNG reward → dissonance

  NHẠC MỚI HAY PASS Ở ĐÂU?
    ✅ P3 VTA delta: CÓ (bài mới = unexpected elements)
    ✅ P4 Goldilocks: CÓ (vừa quen vừa lạ)
    ✅ Coherence: CÓ (phần mới FIT vào structure → body: "coherent!")
    ✅ P2 chunks: CÓ (người nghe có đủ kinh nghiệm nhạc)
    → ALL pass → opioid → REWARD → "hay!"
```

---

## §4 — FRAMEWORK MECHANISM: PE + COHERENCE + H10

```
⭐ CƠ CHẾ ĐẦY ĐỦ — KHÔNG CHỈ PE:

  BƯỚC 1 — VTA DETECT (Prediction Error):
    → Input mới arrive → VTA so sánh với expected baseline
    → Actual ≠ expected → VTA fire dopamine
    → = ATTENTION signal: "có gì đó KHÁC"
    → = Chuông cửa reo: "có khách đến"
    → KHÔNG cho biết khách mang quà hay mang rắn

  BƯỚC 2 — BODY EVALUATE (Coherence Check):
    → Chunks matching: pattern mới FIT vào chunk network có sẵn không?
    → Coherence = cái mới có KHỚP với cái đã compiled không?
    → FIT (coherent) → preparation cho reward
    → NOT FIT (incoherent) → preparation cho dissonance

  BƯỚC 3 — H10 PRECONDITIONS CHECK:
    → P1: Body-need gap open? (có cần không?)
    → P2: Chunks base adequate? (có đủ chunks để đánh giá không?)
    → P3: VTA delta threshold met? (PE đủ lớn không?) ← PE ở đây
    → P4: Goldilocks zone (vừa quen vừa mới)? (vừa quen vừa mới?)
    → P5: Chunk association tag? (không bị tagged avoidance?)
    → ALL 5 required. Missing ANY → signal absent hoặc wrong.

  BƯỚC 4 — SIGNAL FIRE:
    → ALL pass + coherent → opioid body-base → REWARD
    → ANY fail hoặc incoherent → cortisol → DISSONANCE
    → = Quà hay hay dở phụ thuộc TOÀN BỘ evaluation, KHÔNG chỉ PE

  → PE = BƯỚC 1 (attention). KHÔNG phải kết luận.
  → REWARD = BƯỚC 4 (opioid). Sau khi qua BƯỚC 2 + 3.
  → = "Chuông cửa reo (PE) → kiểm tra khách (coherence + H10) → mới biết quà (reward) hay rắn (dissonance)"

  ⭐ 2-LAYER MODEL (Gap-Direction.md §6):
    File này phân biệt PE vs Reward theo 4 BƯỚC (process).
    Gap-Direction.md formalize thêm: 2 LAYERS phân biệt:
      Layer 1 = SIGNAL MECHANISM: VTA/ACC detect "có gì đó khác" (= PE, bước 1)
      Layer 2 = DIRECTION CONTENT: chunk network xác định "khác CÁI GÌ cụ thể"
    "Coherence" (bước 2) = stimulus match GAP DIRECTION hay không.
    Coherence KHÁC giữa người vì gap direction KHÁC (chunk network KHÁC).
    = Tại sao CÙng PE mà xe thời thượng = reward, xe cổ = không:
      PE (Layer 1) fire cho CẢ HAI, nhưng Layer 2 chỉ match cho xe thời thượng.
    Chi tiết: Gap-Direction.md (gap direction + 4 properties + unified Tier 1-4)


  ĐỐI CHIẾU VỚI DOPAMINE-REWARD-REJECTION.MD §4 (7-STEP):

    Step 1: VTA detect delta (PE) — ATTENTION
    Step 2: Dopamine cascade (salience) — ALERTING
    Step 3: Spreading activation (chunks fire)
    Step 4: Body-base evaluate (coherence + H10)
    Step 5: Body-base VOTE (reward/dissonance) — EVALUATION
    Step 6: Opioid release (if reward) — ACTUAL REWARD
    Step 7: PFC observe (feeling) — CONSCIOUS EXPERIENCE

    → PE = Step 1-2 (dopamine, salience)
    → REWARD = Step 5-6 (body vote, opioid)
    → Steps 3-4 QUYẾT ĐỊNH hướng: reward hay dissonance
    → = PE fire ở Step 1, reward fire ở Step 6 — KHÁC nhau 4 bước
```

---

## §5 — 6 TRƯỜNG HỢP PHÂN BIỆT

```
🟡 6 CASES CHO THẤY PE VÀ REWARD = KHÁC NHAU:

  CASE 1 — PE cao, REWARD cao:
    Nhạc mới hay = unexpected + coherent + Goldilocks
    → PE fire (mới!) + body evaluate (fit!) → opioid → "hay!"
    → = PE + coherence = reward ✓

  CASE 2 — PE cao, DISSONANCE:
    Spotify random note = unexpected + incoherent
    → PE fire (mới!) + body evaluate (phá structure!) → cortisol → "dở"
    → = PE cao nhưng coherence fail → dissonance ✗

  CASE 3 — PE thấp, REWARD:
    Bài nhạc yêu thích nghe lần thứ 100
    → PE gần zero (đã biết) + coherence cao + body-need met
    → Opioid nhẹ → "thoải mái, quen thuộc"
    → = PE thấp nhưng vẫn có reward (comfort zone, hardware pull) ✓

  CASE 4 — PE thấp, NEUTRAL:
    Bài nhạc bình thường nghe nhiều lần
    → PE zero + coherence trung bình + body-need met
    → Không reward, không dissonance
    → = "Background music, không cảm giác gì"

  CASE 5 — PE cao, CONFUSED:
    Free jazz lần đầu nghe (người không quen)
    → PE cực cao + chunks base KHÔNG adequate (P2 fail)
    → Body KHÔNG evaluate được → confused → "chả hiểu"
    → = PE cao nhưng P2 fail → không reward, không dissonance rõ
    → NHƯNG: người có chunks jazz → P2 pass → CÓ THỂ reward

  CASE 6 — PE cao, BLOCKED:
    Bài nhạc mới hay NHƯNG do người ghét hát
    → PE fire + coherence ok + Goldilocks ok
    → NHƯNG P5 chunk association tag = AVOIDANCE (ghét người hát)
    → Body block reward → "bài hay nhưng ghét nghe"
    → = PE + coherence pass, nhưng P5 fail → reward blocked

  → 6 cases chứng minh: PE và REWARD = 2 biến SỐ ĐỘC LẬP
  → PE có thể cao/thấp VÀ reward có thể cao/thấp/blocked/confused
  → = PE KHÔNG quyết định reward. Coherence + H10 quyết định.
```

---

## §6 — TẠI SAO MAINSTREAM BỊ GỘP

```
🟡 3 LÝ DO MAINSTREAM GỘP PE = REWARD:

  ① ANIMAL STUDIES = SIMPLIFIED CONTEXT:
    → Schultz 1997 dùng monkey + juice reward
    → Trong context juice: PE > 0 ≈ reward (juice nhiều hơn = tốt hơn)
    → = PE ≈ reward TRONG CONTEXT ĐƠN GIẢN (1 reward type, defined)
    → NHƯNG human reward = multi-dimensional, KHÔNG 1 loại
    → = Generalize từ juice monkey → toàn bộ human experience = quá đơn giản

  ② AI/RL SUCCESS = CONFIRMATION BIAS:
    → TD learning dùng PE = reward signal → AI hoạt động tốt
    → = "PE = reward works trong AI" → assume "PE = reward cho human"
    → NHƯNG AI có DEFINED reward function, human KHÔNG
    → = Success trong AI KHÔNG chứng minh mechanism giống cho human
    → = AlphaGo dùng PE thắng cờ vây ≠ PE giải thích tại sao con người thấy nhạc hay

  ③ THUẬT NGỮ MƠ HỒ:
    → "Prediction error" = quá rộng
    → Gộp: VTA delta (attention) + body evaluation (reward) + learning update
    → = 3 cơ chế khác nhau, cùng 1 tên
    → = Giống gọi "điện" = đèn + TV + tủ lạnh — "điện" đúng nhưng quá gộp

  FRAMEWORK PHÂN BIỆT:
    → VTA delta = PE signal = ATTENTION (dopamine)
    → Body evaluation = COHERENCE check = EVALUATION (multi-system)
    → Opioid release = REWARD thật = REWARD (opioid body-base)
    → Learning update = chunk re-linking = LEARNING (Hebbian LTP)
    → = 4 cơ chế RIÊNG BIỆT, KHÔNG nên gộp thành 1 từ "PE"
```

---

## §7 — HONEST ASSESSMENT

```
🟢 ESTABLISHED:
  → VTA dopamine = prediction error signal (Schultz 1997) ✅
  → Dopamine ≠ reward/pleasure (Berridge & Robinson 1998-2016) ✅
  → Opioid system involvement in hedonic response (Fields 2007) ✅
  → Random noise ≠ rewarding (common sense + acoustic research) ✅
  → Goldilocks zone / optimal novelty (Berlyne 1960) ✅
  → AI/RL uses PE as reward signal (TD learning established) ✅

🟡 FRAMEWORK SYNTHESIS:
  → PE = attention signal, NOT reward signal (consistent with Berridge,
    framework adds mechanism detail)
  → Coherence evaluation as separate step (framework organizing,
    consistent with neuroscience but not formalized elsewhere)
  → H10 5 preconditions (framework hypothesis, empirically testable)
  → 4-step mechanism (VTA → coherence → H10 → opioid) — framework integration
  → AI/human distinction re: PE (logical argument, not empirically tested)

🔴 HYPOTHESIS:
  → Exact timeline VTA → coherence → opioid (framework estimate, not measured)
  → Whether coherence evaluation is a SINGLE step or distributed process
  → Quantitative threshold cho coherence (how much "fit" = enough?)

⚠️ IMPORTANT:
  → Framework KHÔNG bác bỏ Schultz 1997. PE IS real.
  → Framework KHÔNG bác bỏ PE trong AI/RL. PE works cho AI.
  → Framework CHỈ nói: PE ĐƠN THUẦN ≠ reward ở CON NGƯỜI.
  → = CLARIFICATION, không rejection.
  → = Đặt PE đúng vị trí (Step 1 of 7), không phải bỏ PE.
```

---

## §8 — CROSS-REFERENCES

```
WITHIN FRAMEWORK:
  Gap-Direction.md — ⭐ 2-layer model formalizes PE vs reward distinction:
    Layer 1 = signal mechanism (PE), Layer 2 = direction content (gap direction)
  Dopamine-Reward-Rejection.md — dopamine ≠ reward, 7-step mechanism
  Body-Feedback.md — H10 5 preconditions, dual-pull architecture
  Body-Feedback-Mechanism.md — 3 chunk dynamics (Shift/Miss/Gap)
  03-Reward.md — ô tô paradox, Van Gogh gradient, reward mechanism
  Chunk.md v2.0 — chunk substrate, activation dynamics
  Core-v7.8-Draft.md §4.2 — body-feedback trong cycle
  Feeling.md v2.0 §2.2b — PFC threshold 2 chiều (magnitude × clarity)
  Why-Body-Knows.md §2 — Goldilocks zone (needs update with this insight)
  Novelty.md — VTA as seismograph, novelty ≠ reward

KEY RESEARCH:
  Schultz 1997 — VTA PE signal (foundational, KHÔNG bác bỏ)
  Berridge & Robinson 1998, 2003, 2016 — wanting ≠ liking (foundational)
  Berlyne 1960 — optimal novelty / inverted-U
  Zajonc 1968 — mere exposure effect
  Crespi 1942 / Flaherty 1996 — SNC (baseline violation)
  Fields 2007 — opioid hedonic system
  Sutton & Barto 1998 — TD learning (AI/RL PE as reward)
```

---

> *Prediction Error Is Not Reward — "PE (VTA dopamine) = attention signal: có gì đó KHÁC.
> Reward = PE + Coherence + H10 preconditions → opioid body-base.
> AI dùng PE = reward vì reward đã DEFINED. Con người không có defined reward function —
> body phải EVALUATE. Spotify test: random note = PE cao nhất nhưng dở nhất.
> PE = chuông cửa. Quà hay rắn phụ thuộc coherence evaluation."*
