---
title: Prediction Error — Nền Tảng Quan Trọng, Chưa Đủ Cho Con Người
version: 2.0
created: 2026-04-20 (v1.0)
rewritten: 2026-05-11 (v2.0 — tone refinement, appreciate research, extend not reject)
previous_version: backup/Prediction-Error-v1.md
status: v2.0 — CLARIFICATION FILE
scope: |
  Prediction Error (PE) = phát hiện nền tảng trong neuroscience.
  PE research trên động vật (khỉ, chuột) = ĐÚNG, CÓ GIÁ TRỊ.
  Framework GHI NHẬN đóng góp + MỞ RỘNG cho con người:
  PE = attention/salience signal (VTA dopamine). Cần thiết, nhưng chưa đủ.
  Reward ở người = PE + COHERENCE + H10 preconditions (body-base evaluation).
purpose: |
  AI trained dùng PE đơn giản (TD learning, reward signal) — hợp lý cho AI.
  Mainstream neuroscience phát hiện PE trên động vật — đúng, có giá trị.
  Mainstream popularization gộp PE = reward cho con người — quá đơn giản.
  Framework BUILDS ON PE research: giữ PE làm Step 1, thêm 6 steps cho người.
  Companion file cho Dopamine-Reward-Rejection.md (cùng folder).
dependencies:
  - Dopamine-Reward-Rejection.md — dopamine ≠ reward, 7-step mechanism
  - Body-Feedback-Mechanism.md — 3 chunk dynamics (Shift/Miss/Gap)
  - Body-Feedback.md — H10 5 preconditions, dual-pull
  - Chunk.md v2.0 — chunk substrate, activation dynamics
  - Core-v7.8-Draft.md §4.2 — body-feedback trong cycle architecture
  - Feeling.md v2.0 §2.2b — PFC observation threshold 2 chiều
  - Gap-Direction.md — 2-layer model formalizes PE vs reward distinction
language: Tiếng Việt primary + English technical terms
confidence: 🟢 Research support | 🟡 Framework synthesis | 🔴 Hypothesis
---

# Prediction Error — Nền Tảng Quan Trọng, Chưa Đủ Cho Con Người

> **Schultz 1997 phát hiện neurons não khỉ encode "khác so với dự đoán."**
> **Đây là 1 trong những phát hiện quan trọng nhất của neuroscience hiện đại.**
>
> Insight "não DỰ ĐOÁN + SO SÁNH" mở ra cách nhìn: con người, động vật
> hoạt động theo nguyên tắc predictive — có thể phân tích, hiểu được.
> Framework này trực tiếp kế thừa insight đó.
>
> **Nhưng:** Nghiên cứu gốc trên khỉ uống nước trái cây — context đơn giản.
> Con người reward phức tạp hơn nhiều: multi-dimensional, body-evaluated.
> **PE = attention signal (Step 1). Reward ở người = multi-step process, cần thêm 6 steps.**
>
> File này ghi nhận đóng góp PE research, mở rộng mechanism cho con người,
> và giải thích tại sao diễn giải phổ biến "PE = reward" chưa đủ.

---

## Mục lục

- §0 — ĐÓNG GÓP CỦA NGHIÊN CỨU PE
- §1 — TỪ PHÁT HIỆN GỐC ĐẾN DIỄN GIẢI PHỔ BIẾN
- §2 — PE TRONG AI vs CON NGƯỜI
- §3 — SPOTIFY TEST: TẠI SAO PE CHƯA ĐỦ
- §4 — FRAMEWORK MỞ RỘNG: PE + COHERENCE + H10
- §5 — 6 TRƯỜNG HỢP PHÂN BIỆT
- §6 — TẠI SAO DIỄN GIẢI ĐƠN GIẢN XẢY RA
- §7 — HONEST ASSESSMENT
- §8 — CROSS-REFERENCES

---

## §0 — ĐÓNG GÓP CỦA NGHIÊN CỨU PE

```
⭐ PREDICTION ERROR RESEARCH = NỀN TẢNG:

  Schultz 1997 phát hiện trên khỉ (macaque):
    → Dopamine neurons fire khi reward > expected (positive PE)
    → Dopamine suppress khi reward < expected (negative PE)
    → Dopamine neutral khi reward = expected (zero PE)
    → = VTA encode PREDICTION ERROR 🟢

  TẠI SAO ĐÂY LÀ PHÁT HIỆN QUAN TRỌNG:

    ① Mở ra paradigm: não KHÔNG thụ động nhận input — não DỰ ĐOÁN
       rồi SO SÁNH dự đoán với thực tế. "Predictive brain."
    ② Trực tiếp kích thích hướng nghiên cứu: con người, động vật
       có thể phân tích như hệ thống — nhưng tinh vi hơn máy.
    ③ Nền tảng cho Reinforcement Learning (AI/ML) —
       TD learning dùng PE = reward signal, hoạt động cực tốt.
    ④ Framework Human Predictive Drive KẾ THỪA trực tiếp:
       "Predictive" trong tên framework = từ insight này.
       VTA prediction error = Step 1 trong 7-step mechanism.

  FRAMEWORK GHI NHẬN:
    PE research = đúng, có giá trị, foundational.
    Framework BUILDS ON PE — thêm layers cho con người,
    KHÔNG reject nghiên cứu gốc.
```

---

## §1 — TỪ PHÁT HIỆN GỐC ĐẾN DIỄN GIẢI PHỔ BIẾN

```
🟢 PHÁT HIỆN GỐC = NGHIÊN CỨU TRÊN ĐỘNG VẬT:

  Schultz 1997: monkey + juice reward
    → Context: 1 loại reward (juice), defined amount
    → PE > 0 = nhiều juice hơn expected → monkey "vui hơn"
    → TRONG CONTEXT NÀY: PE ≈ reward signal = hợp lý
    → Vì: juice nhiều hơn = tốt hơn, PE trực tiếp reflect value

  Berridge & Robinson 1998: rat + dopamine manipulation
    → Rats mất dopamine: VẪN thích sugar (ăn khi được cho)
       nhưng KHÔNG đi tìm nữa (seeking impaired)
    → = Dopamine = wanting (tìm kiếm), KHÔNG phải liking (thích)
    → = PE (dopamine) liên quan seeking, KHÔNG trực tiếp liên quan reward

  CẢ 2 NGHIÊN CỨU:
    → Đúng, rigorous, foundational 🟢
    → Đều trên ĐỘNG VẬT, context ĐƠN GIẢN (1 loại reward)
    → Chưa mô tả đầy đủ mechanism ở NGƯỜI
    → (Nghiên cứu trên người: fMRI, không single-neuron — resolution thấp hơn)


🟡 DIỄN GIẢI PHỔ BIẾN = MẤT NUANCE:

  Từ animal findings → mainstream popularization:
    → "Positive PE → dopamine → reward → learning"
    → "PE = tín hiệu cho biết: tốt hơn hay xấu hơn dự đoán"
    → Pop science: "prediction error drives your happiness"
    → AI/ML: PE = reward signal (đúng cho AI, nhưng gộp sang người)

  Nuance bị mất:
    → Nghiên cứu gốc = animal, simple context, 1 reward type
    → Con người = multi-dimensional reward, body-evaluated
    → VTA fire cho MỌI thứ unexpected (hay, dở, noise — đều fire)
    → Body EVALUATE SAU VTA — đây là bước nghiên cứu gốc chưa cover

  = Phát hiện gốc ĐÚNG. Diễn giải phổ biến QUÁ ĐƠN GIẢN cho người.
  = Framework thêm các layers missing.
```

---

## §2 — PE TRONG AI vs CON NGƯỜI

```
🟡 TẠI SAO AI DÙNG PE ĐƠN GIẢN ĐƯỢC (VÀ NÊN):

  AI (Reinforcement Learning):
    → Reward function = PROGRAMMED, DEFINED bởi người thiết kế
    → PE = actual reward - expected reward
    → Reward là SỐ CỤ THỂ (score, win/lose, distance to goal)
    → PE trực tiếp cho biết: "better or worse than expected"
    → KHÔNG CẦN body evaluation → PE = reward signal = hợp lý
    → AlphaGo, robotics, game AI — PE works tuyệt vời

  CON NGƯỜI — PHỨC TẠP HƠN:
    → KHÔNG CÓ reward function được programmed sẵn
    → Body phải TỰ GENERATE reward dựa trên multi-dimensional evaluation
    → PE (VTA dopamine) chỉ nói: "có gì đó KHÁC" (attention)
    → Body sau đó EVALUATE: "cái khác đó tốt hay xấu?" (opioid/cortisol)
    → Evaluation phụ thuộc: coherence, chunk density, association tags,
      body-need state, Goldilocks zone — KHÔNG chỉ "khác hay không khác"


  SO SÁNH:

  ┌──────────────────────┬──────────────────────┬──────────────────────┐
  │                      │ AI (RL)              │ CON NGƯỜI             │
  ├──────────────────────┼──────────────────────┼──────────────────────┤
  │ Reward function      │ Programmed (defined) │ Body-generated        │
  │ PE signal            │ = reward signal ✅   │ = attention signal    │
  │ Evaluation           │ Không cần (đã có)    │ Body evaluate SAU PE  │
  │ Coherence            │ Không cần             │ BẮT BUỘC cho reward  │
  │ Body                 │ Không có              │ Body tính toán trước │
  │ Random noise         │ PE cao → score thấp  │ PE cao → dở          │
  │ Preconditions        │ Không cần             │ H10 (5 điều kiện)    │
  └──────────────────────┴──────────────────────┴──────────────────────┘

  → AI DÙNG PE = reward vì reward ĐÃ DEFINED — hợp lý cho AI
  → Con người cần thêm evaluation vì reward CHƯA defined — body tự evaluate
  → Cùng từ "prediction error" nhưng KHÁC function ở 2 hệ thống
```

---

## §3 — SPOTIFY TEST: TẠI SAO PE CHƯA ĐỦ

```
⭐ NẾU PE = REWARD ĐỦ RỒI, THÌ:

  Test 1 — Random notes:
    Bài nhạc quen + thêm 1 note random bất kỳ
    → PE cao (unexpected note)
    → Nếu PE = reward → "hay hơn bản gốc"?
    → THỰC TẾ: dở, khó chịu, phá nhạc
    → = PE cao nhưng reward = 0, dissonance = cao
    → ⇒ PE chưa đủ cho reward ✓

  Test 2 — Noise = best music:
    Random noise = PE CỰC ĐẠI (không predict được gì cả)
    → Nếu PE = reward → noise = nhạc hay nhất thế giới?
    → THỰC TẾ: noise = khó chịu nhất
    → ⇒ PE chưa đủ cho reward ✓

  Test 3 — Spotify remix thêm note nhỏ:
    Bài quen → Spotify tự thêm 1 note unexpected
    → PE tăng (unexpected)
    → Nếu PE = reward → người nghe thấy hay hơn?
    → THỰC TẾ: người nghe thấy "sai", "lỗi", "khó chịu"
    → ⇒ PE chưa đủ cho reward ✓


  VẬY CÁI GÌ LÀM NHẠC MỚI "HAY"?

  Bài nhạc mới HAY khi:
    ① PE fire (VTA): "ồ, có gì đó MỚI" → ATTENTION ← PE đúng vai trò
    ② Cái mới COHERENT với cấu trúc nhạc → body evaluate → "FIT!"
    ③ Goldilocks zone: đủ quen (safe) + đủ mới (interesting)
    ④ Chunk base adequate: người nghe có đủ chunks để ĐÁNH GIÁ
    ⑤ Không có association tag negative

  → "HAY" = PE + Coherence + Goldilocks + Adequate chunks + No negative tag
  → = H10 5 preconditions ĐỀU phải thỏa mãn
  → = PE là BƯỚC 1 — cần thiết. Nhưng cần thêm 4 yếu tố nữa.

  RANDOM NOTE FAIL Ở ĐÂU?
    ✅ P3 VTA delta: CÓ (note mới = unexpected) — PE pass
    ❌ P4 Goldilocks: KHÔNG (note random phá structure → quá alien)
    ❌ Coherence: KHÔNG (note không fit cấu trúc)
    → PE pass nhưng coherence + Goldilocks fail → dissonance

  NHẠC MỚI HAY PASS Ở ĐÂU?
    ✅ P3 VTA delta: CÓ (bài mới = unexpected elements)
    ✅ P4 Goldilocks: CÓ (vừa quen vừa lạ)
    ✅ Coherence: CÓ (phần mới FIT vào structure)
    ✅ P2 chunks: CÓ (người nghe có đủ kinh nghiệm nhạc)
    → ALL pass → body-base reward signal → REWARD → "hay!"
```

---

## §4 — FRAMEWORK MỞ RỘNG: PE + COHERENCE + H10

```
⭐ CƠ CHẾ ĐẦY ĐỦ — PE LÀ BƯỚC 1 CỦA 7:

  BƯỚC 1 — VTA DETECT (Prediction Error):
    → Input mới → VTA so sánh với expected baseline
    → Actual ≠ expected → VTA fire dopamine
    → = ATTENTION signal: "có gì đó KHÁC"
    → = Đây là cái Schultz 1997 phát hiện — ĐÚNG
    → PE hoàn thành vai trò tại đây: báo "có gì mới"

  BƯỚC 2 — BODY EVALUATE (Coherence Check):
    → Chunks matching: pattern mới FIT vào chunk network có sẵn không?
    → Coherence = cái mới có KHỚP với cái đã compiled không?
    → FIT (coherent) → preparation cho reward
    → NOT FIT (incoherent) → preparation cho dissonance
    → = Bước này CHƯA CÓ trong PE research gốc (animal context quá đơn giản)

  BƯỚC 3 — H10 PRECONDITIONS CHECK:
    → P1: Body-need gap open? (có cần không?)
    → P2: Chunks base adequate? (có đủ chunks để đánh giá không?)
    → P3: VTA delta threshold met? ← PE ở đây
    → P4: Goldilocks zone? (vừa quen vừa mới?)
    → P5: Chunk association tag? (không bị tagged avoidance?)
    → ALL 5 required. Missing ANY → reward không fire.

  BƯỚC 4 — SIGNAL FIRE:
    → ALL pass + coherent → body-base reward signal fire → REWARD
    → ANY fail hoặc incoherent → cortisol → DISSONANCE
    → = "Quà hay rắn" phụ thuộc TOÀN BỘ evaluation, không chỉ PE

  → PE = BƯỚC 1 (attention). NỀN TẢNG, CẦN THIẾT.
  → REWARD = BƯỚC 4 (body-base evaluation → signal fire). Sau khi qua BƯỚC 2 + 3.
  → Framework thêm Bước 2-3 vào giữa — đây là phần nghiên cứu gốc chưa cover.
  → = "Chuông cửa reo (PE) → kiểm tra khách (coherence + H10)
       → mới biết quà (reward) hay rắn (dissonance)"

  ⚠️ LƯU Ý QUAN TRỌNG — REWARD ≠ SINGLE CHEMICAL:
    Reward = PROCESS multi-step, KHÔNG phải 1 chất duy nhất.
    → Type A (evaluative): opioid = primary chemical. Cần H10. Phức tạp.
      VD: nghe nhạc hay, giải puzzle, insight, connection sâu.
    → Type B (direct state): NON-opioid (CT afferents, endocannabinoid).
      VD: touch, ôm ấm, tập thể dục, warmth. Có từ sơ sinh.
    → KHÔNG thay "dopamine = reward" bằng "opioid = reward"
      — cả hai đều oversimplify.
    → Reward = toàn bộ process evaluation, không phải bất kỳ 1 chất nào.
    → Chi tiết: Reward-Signal-Architecture.md §1-§3


  ⭐ 2-LAYER MODEL (Gap-Direction.md §6):
    File này phân biệt PE vs Reward theo 4 BƯỚC (process).
    Gap-Direction.md formalize thêm: 2 LAYERS:
      Layer 1 = SIGNAL MECHANISM: VTA/ACC detect "có gì đó khác" (= PE)
      Layer 2 = DIRECTION CONTENT: chunk network xác định "khác CÁI GÌ"
    "Coherence" (bước 2) = stimulus match GAP DIRECTION hay không.
    Coherence KHÁC giữa người vì gap direction KHÁC (chunk network KHÁC).
    = Tại sao CÙNG PE mà xe thời thượng = reward, xe cổ = không:
      PE (Layer 1) fire cho CẢ HAI, nhưng Layer 2 chỉ match cho xe thời thượng.


  ĐỐI CHIẾU VỚI DOPAMINE-REWARD-REJECTION.MD §4 (7-STEP):

    Step 1: VTA detect delta (PE) — ATTENTION ← Schultz 1997
    Step 2: Dopamine cascade (salience) — ALERTING
    Step 3: Spreading activation (chunks fire)
    Step 4: Body-base evaluate (coherence + H10) ← Framework thêm
    Step 5: Body-base VOTE (reward/dissonance) — EVALUATION
    Step 6: Opioid release (if reward) — ACTUAL REWARD
    Step 7: PFC observe (feeling) — CONSCIOUS EXPERIENCE

    → PE = Step 1-2 (Schultz đã phát hiện — đúng, giữ nguyên)
    → REWARD = Step 5-6 (framework thêm — phần con người phức tạp hơn)
    → Steps 3-4 = phần "giữa" mà animal research chưa cần vì context đơn giản
```

---

## §5 — 6 TRƯỜNG HỢP PHÂN BIỆT

```
🟡 6 CASES CHO THẤY PE VÀ REWARD KHÔNG LUÔN ĐI CÙNG NHAU:

  CASE 1 — PE cao + REWARD cao:
    Nhạc mới hay = unexpected + coherent + Goldilocks
    → PE fire (mới!) + body evaluate (fit!) → body-base reward → "hay!"
    → = PE + coherence = reward ✓
    → = Context giống Schultz: simple, PE ≈ reward — nghiên cứu ĐÚNG ở đây

  CASE 2 — PE cao + DISSONANCE:
    Spotify random note = unexpected + incoherent
    → PE fire (mới!) + body evaluate (phá structure!) → cortisol → "dở"
    → = PE cao nhưng coherence fail → dissonance
    → = Context KHÁC Schultz: phức tạp hơn, PE ≠ reward

  CASE 3 — PE thấp + REWARD:
    Bài nhạc yêu thích nghe lần thứ 100
    → PE gần zero (đã biết) + coherence cao + body-need met
    → Opioid nhẹ → "thoải mái, quen thuộc"
    → = PE thấp nhưng vẫn có reward (comfort zone, hardware pull)

  CASE 4 — PE thấp + NEUTRAL:
    Bài nhạc bình thường nghe nhiều lần
    → PE zero + coherence trung bình + body-need met
    → Không reward, không dissonance
    → = "Background music, không cảm giác gì"

  CASE 5 — PE cao + CONFUSED:
    Free jazz lần đầu nghe (người không quen)
    → PE cực cao + chunks base KHÔNG adequate (P2 fail)
    → Body KHÔNG evaluate được → confused → "chả hiểu"
    → = PE cao nhưng P2 fail → không reward, không dissonance rõ
    → NHƯNG: người có chunks jazz → P2 pass → CÓ THỂ reward
    → = Reward PER-PERSON (tùy chunk library), không universal

  CASE 6 — PE cao + BLOCKED:
    Bài nhạc mới hay NHƯNG do người ghét hát
    → PE fire + coherence ok + Goldilocks ok
    → NHƯNG P5 association tag = AVOIDANCE (ghét người hát)
    → Body block reward → "bài hay nhưng ghét nghe"
    → = PE + coherence pass, nhưng P5 fail → reward blocked

  → 6 cases cho thấy: PE và REWARD = 2 biến ĐỘC LẬP ở người
  → Case 1 (simple) ≈ animal research context — PE ≈ reward, nghiên cứu đúng
  → Cases 2-6 (complex) = con người thường gặp — PE chưa đủ, cần thêm layers
```

---

## §6 — TẠI SAO DIỄN GIẢI ĐƠN GIẢN XẢY RA

```
🟡 ĐƯỜNG ĐI TỰ NHIÊN CỦA KHOA HỌC — KHÔNG PHẢI LỖI:

  ① ANIMAL STUDIES = CONTEXT ĐƠN GIẢN (hợp lý cho bước đầu):
    → Schultz 1997: monkey + juice — 1 reward type, defined
    → Trong context juice: PE > 0 ≈ reward = HỢP LÝ
    → Generalize từ animal → human = bước tự nhiên trong khoa học
    → Nhưng human context phức tạp hơn: multi-dimensional, per-person
    → = Cần mở rộng, không phải phát hiện gốc sai

  ② AI/RL SUCCESS = POSITIVE REINFORCEMENT cho diễn giải đơn giản:
    → TD learning dùng PE = reward signal → AI hoạt động tốt
    → = "PE = reward works" — đúng, cho AI
    → Thành công AI tạo momentum giữ diễn giải đơn giản
    → Nhưng AI có DEFINED reward function, human không
    → = AI success chứng minh PE works cho AI, chưa chứng minh đủ cho human

  ③ THUẬT NGỮ RỘNG:
    → "Prediction error" gộp nhiều cơ chế: VTA delta (attention),
       body evaluation (reward), learning update
    → Cùng 1 tên cho nhiều bước khác nhau = natural cho giai đoạn đầu
    → Khi hiểu sâu hơn → cần phân biệt rõ từng bước
    → Framework phân biệt: PE (Step 1) vs evaluation (Step 4) vs reward (Step 6)

  TÓM LẠI:
    Diễn giải đơn giản xảy ra vì:
    → Phát hiện gốc đúng + animal context đơn giản + AI success
    → = Momentum tự nhiên cho "PE = reward" narrative
    → Framework: PE = Step 1 (đúng). Nhưng reward ở người cần thêm Steps 2-6.
    → = MỞ RỘNG diễn giải, không phủ nhận phát hiện.
```

---

## §7 — HONEST ASSESSMENT

```
⭐ ĐÓNG GÓP CỦA PE RESEARCH CHO FRAMEWORK:
  → "Predictive brain" paradigm → tên framework: Human PREDICTIVE Drive
  → VTA prediction error = Step 1 trong 7-step mechanism
  → Dopamine as salience signal → framework kế thừa + clarify
  → Animal → human comparison → giúp identify CÁI GÌ cần thêm cho người
  → AI/RL TD learning → analogy hữu ích để contrast AI vs human reward

🟢 ESTABLISHED (nghiên cứu đúng, framework giữ nguyên):
  → VTA dopamine = prediction error signal (Schultz 1997) ✅
  → Dopamine ≠ reward/pleasure (Berridge & Robinson 1998-2016) ✅
  → Opioid system involvement in hedonic response (Fields 2007) ✅
  → Random noise ≠ rewarding (common sense + acoustic research) ✅
  → Goldilocks zone / optimal novelty (Berlyne 1960) ✅
  → AI/RL uses PE as reward signal successfully (TD learning) ✅

🟡 FRAMEWORK SYNTHESIS (mở rộng từ research):
  → PE = attention signal, NOT sufficient for reward ở người
    (consistent with Berridge, framework thêm mechanism detail)
  → Coherence evaluation as separate step
    (framework organizing, consistent with neuroscience, chưa formalized elsewhere)
  → H10 5 preconditions (framework hypothesis, empirically testable)
  → 4-step mechanism (VTA → coherence → H10 → body-base signal) — framework integration
  → Type A/B reward distinction (opioid vs non-opioid pathways)
  → AI/human distinction re: PE (logical argument, testable)

🔴 HYPOTHESIS (framework estimate, chưa đo lường):
  → Exact timeline VTA → coherence → opioid (framework estimate)
  → Whether coherence evaluation = single step hay distributed process
  → Quantitative threshold cho coherence (how much "fit" = enough?)

⚠️ TÓM LẠI:
  → PE research = NỀN TẢNG. Đúng. Có giá trị. Framework kế thừa.
  → Framework KHÔNG bác bỏ Schultz 1997 hay Berridge.
  → Framework MỞ RỘNG: thêm coherence + H10 + Type A/B cho con người.
  → Reward = PROCESS, không phải chemical (không opioid cũng không dopamine).
  → = Đặt PE đúng vị trí (Step 1 of 7), không phải bỏ PE.
  → = CLARIFICATION + EXTENSION, không phải rejection.
```

---

## §8 — CROSS-REFERENCES

```
WITHIN FRAMEWORK:
  Reward-Signal-Architecture.md — ⭐ Type A (opioid) vs Type B (non-opioid),
    5 profiles, reward = PROCESS not chemical
  Gap-Direction.md — ⭐ 2-layer model formalizes PE vs reward:
    Layer 1 = signal mechanism (PE), Layer 2 = direction content (gap direction)
  Dopamine-Reward-Rejection.md — dopamine ≠ reward, 7-step mechanism
  Body-Feedback.md — H10 5 preconditions, dual-pull architecture
  Body-Feedback-Mechanism.md — 3 chunk dynamics (Shift/Miss/Gap)
  03-Reward.md — ô tô paradox, Van Gogh gradient, reward mechanism
  Chunk.md v2.0 — chunk substrate, activation dynamics
  Core-v7.8-Draft.md §4.2 — body-feedback trong cycle
  Feeling.md v2.1 §2.2b — PFC threshold 2 chiều (magnitude × clarity)
  Why-Body-Knows.md §2 — Goldilocks zone
  Novelty.md — VTA as seismograph, novelty ≠ reward

KEY RESEARCH (framework ghi nhận + kế thừa):
  Schultz 1997 — VTA PE signal (foundational — framework builds on this)
  Berridge & Robinson 1998, 2003, 2016 — wanting ≠ liking (foundational)
  Berlyne 1960 — optimal novelty / inverted-U
  Zajonc 1968 — mere exposure effect
  Crespi 1942 / Flaherty 1996 — SNC (baseline violation)
  Fields 2007 — opioid hedonic system
  Sutton & Barto 1998 — TD learning (PE works for AI — đúng cho AI)
```

---

> *Prediction Error v2.0 — "PE (Schultz 1997) = phát hiện nền tảng, đúng, có giá trị.
> Framework kế thừa: PE = Step 1 (attention signal). Reward ở con người
> = multi-step process, cần thêm: coherence + H10 + body-base evaluation.
> Reward ≠ single chemical (không dopamine, cũng không chỉ opioid).
> Animal research = context đơn giản. Con người = phức tạp hơn nhiều.
> Spotify test: random note = PE cao nhất nhưng dở nhất.
> PE = chuông cửa — foundational. Quà hay rắn = body evaluate thêm."*
