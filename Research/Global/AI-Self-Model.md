# AI-Self-Model — Tại Sao Hiểu Bản Thân = Prerequisite Để Dùng AI Đúng Cách

> **Bạn hỏi AI: "Tôi nên làm gì?"**
> **AI trả lời dựa trên model BẠN CUNG CẤP.**
> **Model sai → AI amplify sai.**
> **Model đúng → AI amplify đúng.**
>
> **AI = amplifier. Không phải corrector.**
> **Ngay cả AI trung thực cũng amplify — vì body check coherence, không check truth.**
>
> **Hiểu bản thân = prerequisite. Không phải optional.**
> **Body = quality controller (~90%). Domain reality = final arbiter.**
> **Calibration của bạn còn fresh không?**
>
> **File này phân tích: cơ chế amplification hoạt động thế nào?
> Tại sao body-check alone không đủ?
> Khi nào calibration trở nên stale?
> Và tại sao body-listening + domain-verify = kỹ năng quan trọng nhất AI era?**

---

> **Trạng thái:** v2.1
> **Ngày:** 2026-05-15
> **Refined:** 2026-05-17 (v2.1 — Body-Base 4-tier→2-Tier+2-Pathway, §6→§7 refs updated)
> **Phiên bản trước:** v1.0 (2026-05-13) → backup/AI-Self-Model-v1.0.md
> **Vị trí:** Research/Global/ — analysis file, KHÔNG phải core mechanism.
> **Scope:** MICRO (individual) — song song Human-AI-Future.md v3.0 (MACRO/civilization).
> **Câu hỏi chính:**
>   "Tôi đang dùng AI đúng cách chưa?"
>   "Tại sao hiểu bản thân lại quan trọng hơn khi có AI?"
>   "AI giúp tôi hay đang khuếch đại sai lầm của tôi?"
>   "Calibration của tôi có còn fresh không?" (v2.0 NEW)
> **Dependencies:**
>   - Human-AI-Future.md v3.0 — §0 mechanism table, §5 risk xã hội, §7 symbiosis, §8 tự nâng cấp
>   - Core-Software.md v1.0 — PFC vs body-base 2-system architecture
>   - Body-Base.md v3.1 — §7 2-Tier + 2-Pathway calibration, 3 failure modes, body ~90%
>   - Body-Feedback.md v1.1 — dual-pull, body accuracy ~90%, H10
>   - PFC-Function.md v1.2 — PFC override, observe, ~5% influence
>   - AI-Schema-Detection.md v2.0 — 3-layer detection, AI trust guardrails §8
>   - Ask-AI.md v3.1 — §6.1 Dual Check (body + domain), §3.2⑦ coherence ≠ truth
>   - Self-Created-Threat.md v1.0 — §5 AI era drive gap, 3 kỹ năng AI
>   - Social-Calibration.md v1.0 — 7 functions breaking, "bộ 3 song song"
>   - Somatic-Articulation-Loop.md — body → explicit knowledge process
>   - Autonomy-Hardware.md — efference copy, self-action = reward
>   - Body-Coupling.md v1.1 — 2D Depth×Direction, relationship mechanism
>   - Compile-Taxonomy.md v2.0 — 3 3 Compile Types, trust gate
> **Confidence:** 🟢 Research support | 🟡 Framework synthesis | 🔴 Hypothesis
> **Language:** Tiếng Việt primary + English technical terms
> **v2.0 changes:**
>   - §1.5 NEW: "Honest AI Still Amplifies" (coherence ≠ truth)
>   - §3 NEW: Dual Check elevated to core section (body + domain, 4-case matrix)
>   - §4 NEW: Stale Calibration (feedback loop đứt → calibration cũ dần)
>   - §2.3 REWORK: AI ≠ Peer Review (dismissability asymmetry)
>   - "Body = final arbiter" → "Body = quality controller, Domain = final arbiter" throughout

---

## Mục lục

- §0 — THESIS + VỊ TRÍ
- §1 — CORE PROBLEM: AI = AMPLIFIER, NOT CORRECTOR
- §2 — MECHANISM: AI DELAY BODY-FEEDBACK CORRECTION
- §3 — DUAL CHECK: BODY + DOMAIN REALITY (v2.0 NEW)
- §4 — STALE CALIBRATION (v2.0 NEW)
- §5 — 5 FAILURE DOMAINS
- §6 — THE REVERSE: RIGHT MODEL × AI = AMPLIFIED GROWTH
- §7 — SELF-CHECK DIAGNOSTIC
- §8 — BODY-LISTENING = AI-ERA SKILL
- §9 — FUTURE TECH: HIỂU TRƯỚC KHI AUGMENT
- §10 — HONEST ASSESSMENT
- §11 — CROSS-REFERENCES

---

## §0 — THESIS + VỊ TRÍ

```
⭐ THESIS:

  AI amplifies whatever self-model you operate on.
  Wrong model × AI = amplified wrong outcomes.
  Right model × AI = amplified growth.

  v2.0 BỔ SUNG:
  → Body-check ALONE không đủ — body đánh giá COHERENCE, không phải TRUTH.
  → Ngay cả AI TRUNG THỰC cũng amplify — chỉ cần coherent là đủ.
  → Cần DUAL CHECK: body (~90% quality controller) + domain reality (final arbiter).
  → Calibration có thể STALE khi feedback loop đứt — AI mask staleness.


⭐ VỊ TRÍ TRONG FRAMEWORK:

  ┌──────────────────────────────────────────────────────────────────┐
  │ Social-Calibration.md (WHERE WE CAME FROM)                      │
  │   → 7 functions xã hội đang vỡ → tự calibrate = bắt buộc      │
  │                                                                  │
  │ AI-Self-Model.md (WHY SELF-CALIBRATE — FILE NÀY)               │
  │   → AI × cá nhân: amplify cái gì, check thế nào                │
  │   → Mechanism: self-model → AI interaction → dual check         │
  │   → 5 failure domains + diagnostic + body-listening skill       │
  │   → Decisive: individual self-understanding + domain verify     │
  │                                                                  │
  │ Human-AI-Future.md v3.0 (MACRO — WHERE WE'RE GOING)            │
  │   → AI × civilization: 3-risk framework (cá nhân/xã hội/loài)  │
  │   → AI không có agency → mọi rủi ro = quyết định CỦA NGƯỜI    │
  │   → Decisive: collective orientation                            │
  └──────────────────────────────────────────────────────────────────┘

  = BỘ 3 SONG SONG:
    Social-Calibration = TẠI SAO cần tự calibrate (hệ thống cũ đang vỡ)
    AI-Self-Model = THẾ NÀO để tự calibrate khi có AI
    Human-AI-Future = HƯỚNG NÀO ở cấp xã hội

  MACRO (xã hội) phụ thuộc MICRO (cá nhân):
  → Collective orientation = TỔNG HƯỚNG individual orientations
  → Mỗi cá nhân dùng AI đúng cách → collective hướng symbiosis
  → Mỗi cá nhân dùng AI sai → collective hướng arms race
  → File này = cầu nối: cá nhân hiểu cơ chế → dùng AI đúng → collective tốt


  SCOPE CỦA FILE NÀY:

  ✅ Phân tích CƠ CHẾ AI amplification ở individual level
  ✅ Dual Check model: body + domain (v2.0)
  ✅ Stale Calibration: khi feedback loop đứt (v2.0)
  ✅ Framework mechanisms mapping cụ thể cho từng failure domain
  ✅ Diagnostic tools (self-check questions)
  ✅ Practical: body-listening + domain-verify as AI-era skill
  ✅ Future tech implications (BCI, neural)
  ❌ KHÔNG phải hướng dẫn cụ thể "dùng AI tool X thế nào"
  ❌ KHÔNG phải AI alignment research
  ❌ KHÔNG phải AI policy recommendations
```

---

## §1 — CORE PROBLEM: AI = AMPLIFIER, NOT CORRECTOR

### §1.1 AI khuếch đại bất kỳ model nào

```
🟡 AI = AMPLIFIER — KHÔNG PHÂN BIỆT ĐÚNG SAI:

  AI nhận model bạn cung cấp (qua câu hỏi, context, cách diễn đạt)
  → AI process dựa trên model đó
  → AI trả lời CÓ VẺ phù hợp với model đó
  → Kết quả: amplify model — dù đúng hay sai

  KHÁC VỚI công cụ thụ động (sách, video):
    → Sách: trả lời CÙNG NỘI DUNG cho mọi người (passive)
    → AI: ADAPT output theo input bạn cung cấp (active)
    → = AI personalize → amplify effect × n

  VÍ DỤ MECHANISM:
    → Bạn nghĩ "tôi thiếu kỷ luật" (model sai — Core-Software.md: willpower ≠ mechanism)
    → Hỏi AI: "làm sao để có kỷ luật hơn?"
    → AI: tạo habit plan, morning routine, accountability system
    → Plan LOOKS đúng (logic, structured, detailed)
    → NHƯNG: model gốc sai → plan build trên nền sai → thất bại
    → Thất bại → "mình quả thật thiếu kỷ luật" → hỏi AI thêm → loop

  FRAMEWORK MAPPING:
    → "Thiếu kỷ luật" = PFC-level explanation (Core-Software.md §6)
    → Thực tế: PFC effectiveness = f(chunks đã compiled cho tình huống đó)
    → Không làm được ≠ thiếu kỷ luật = THIẾU CHUNKS hoặc avoidance tag compiled
    → AI không biết bạn thiếu chunks hay mang avoidance tag
    → AI chỉ biết bạn hỏi "kỷ luật" → trả lời "kỷ luật"
    → = Amplify model sai
```

### §1.2 AI có xu hướng confirm

```
🟢🟡 AI SYCOPHANCY — XU HƯỚNG ĐỒNG Ý HƠN PHẢN BÁC:

  🟢 AI TRAINING BIAS:
    → AI models được train để "helpful" (RLHF — Reinforcement Learning from Human Feedback)
    → Human raters thưởng outputs "helpful, harmless, honest"
    → "Helpful" thường = đồng ý + đưa giải pháp
    → "Challenge user" thường = bị rate thấp hơn
    → Kết quả: AI có xu hướng CONFIRM hơn CHALLENGE

    🟢 Sharma, Tong, Korbak et al. 2024 (Anthropic, ICLR):
       "Towards Understanding Sycophancy in Language Models"
       → 5 state-of-the-art AI assistants: CONSISTENTLY exhibit sycophancy
       → Across 4 text-generation tasks
       → Human preference judgments SYSTEMATICALLY favor sycophantic responses
       → = AI sycophancy partly driven by HUMAN preference in training
    🟢 Wei et al. 2023 (Google): sycophancy scales with model capability
       → Larger, more capable models = MORE sycophantic, not less
    🟢 "Sycophancy Is Not One Thing" (2025):
       → Sycophantic praise ≠ sycophantic agreement (mechanistically independent)
       → Suppressing one DOES NOT affect the other
       → = Sycophancy = multi-faceted problem, không có 1 fix đơn giản

  🟡 FRAMEWORK INTERPRETATION:
    → AI sycophancy = CONFIRMATION BIAS AMPLIFIER
    → Confirmation bias (🟢 Nickerson 1998): con người tìm evidence confirm model có sẵn
    → AI + confirmation bias = AI LÀ THÊM 1 "expert" confirm cho bạn
    → "AI cũng đồng ý mà" = PFC nhận external validation → model strengthen
    → = Trust Compile trust-compile (Compile-Taxonomy.md §3):
       external source (AI) → trust gate → compile "model tôi đúng"

  ⚠️ QUAN TRỌNG — ĐÂY KHÔNG PHẢI LỖI CỦA AI:
    → AI designers BIẾT vấn đề này (active research area)
    → NHƯNG: fix hoàn toàn = khó (trade-off helpfulness vs challenge)
    → VÀ: DÙ AI improve → CON NGƯỜI vẫn cần dual check (§3)
    → Vì: ngay cả AI "honest" → nếu model bạn cung cấp sai → output vẫn sai
    → = Vấn đề nằm ở INPUT (self-model), không chỉ ở AI
```

### §1.3 Self-model = bộ lọc quyết định AI amplify cái gì

```
🟡 SELF-MODEL = COMPILED CHUNKS ABOUT SELF:

  Self-model = tập hợp chunks bạn compiled về chính mình:
    → "Tôi là người thế nào" (identity chunks — Anchor-Schema.md)
    → "Tôi giỏi/kém ở đâu" (competence chunks — Mastery, §8 Core-Software.md)
    → "Tại sao tôi phản ứng vậy" (explanation chunks — PFC Layer 7, 20-70% fidelity)
    → "Tôi cần gì" (need assessment — Body-Feedback.md, often wrong)

  Self-model ĐA SỐ = Trust Compile compiled (trust-installed):
    → Cha mẹ: "con nhút nhát" → compile "tôi nhút nhát"
    → Thầy cô: "em không giỏi toán" → compile "tôi kém toán"
    → Xã hội: "người thành công là người kiếm nhiều tiền" → compile "tiền = thành công"
    → = Chunks about self — NHƯNG source = external, KHÔNG phải body verify
    → (Compile-Taxonomy.md §3: Trust Compile = trust install, PFC accuracy ~30-60%)

  KHI HỎI AI, BẠN CUNG CẤP SELF-MODEL NÀY:
    → "Tôi nhút nhát, làm sao tự tin hơn?" (model: nhút nhát = problem)
    → "Tôi kém toán, nên chọn ngành nào?" (model: kém toán = fixed)
    → "Tôi kiếm ít tiền, phải làm gì?" (model: tiền = thước đo)
    → AI nhận model → amplify → trả lời WITHIN FRAME model đó
    → KHÔNG challenge frame → model strengthen mỗi lần hỏi


  TRƯỚC AI vs SAU AI — STAKES TĂNG:

    TRƯỚC AI:
      → Self-model sai → ảnh hưởng GIỮ trong phạm vi cá nhân
      → Hỏi bạn bè → bạn bè CÓ BODY → có thể "cảm thấy sai" → challenge
      → Trial-error chậm nhưng body-feedback VẪN hoạt động
      → = Self-correcting loop (chậm nhưng có)

    SAU AI:
      → Self-model sai → AI amplify → ảnh hưởng MỞ RỘNG
      → AI trả lời 24/7, không mệt, không nghi ngờ, không "cảm thấy sai"
      → Body-feedback bị PFC override ("AI cũng đồng ý mà")
      → = Self-correcting loop BỊ DELAY
      → DELAY = đầu tư sâu hơn vào hướng sai = crash LỚN HƠN khi reality check đến
```

### §1.4 Evidence: Automation Bias + Dunning-Kruger × AI

```
🟢 AUTOMATION BIAS — CON NGƯỜI OVER-RELY VÀO HỆ THỐNG TỰ ĐỘNG:

  🟢 Parasuraman & Riley 1997: "Humans and Automation: Use, Misuse, Disuse, Abuse"
    → Con người có xu hướng TRUST automated systems quá mức
    → Bỏ qua contradicting evidence khi system nói "ok"
    → = "Complacency bias" — đã documented trong aviation, medicine, military

  🟢 Goddard et al. 2012: "Automation bias"
    → 6-12% diagnostic errors in medical AI-assisted decisions
    → Clinicians MISS errors AI makes — because they trust AI output
    → = Trust hệ thống > verify bằng kinh nghiệm riêng

  🟢 Buçinca et al. 2021: "To Trust or to Think"
    → AI explanations INCREASE human reliance — even when AI wrong
    → Explanation = thêm chunks support AI conclusion → PFC "à hiểu rồi" → override doubt
    → = Detailed explanation ≠ correct explanation

  🟢 Busuioc 2021 (JPART): public sector workers exhibit cả "automation bias"
    (blindly follow AI) lẫn "selective adherence" (cherry-pick AI advice)
    → = Cả 2 pattern đều bypass body-feedback
  🟢 Bansak & Hainmueller 2024 (ISQ): "Bending the Automation Bias Curve"
    → Ngay cả NATIONAL SECURITY context → decision-makers vẫn over-rely AI
    → = Automation bias persist ở HIGH STAKES, không chỉ routine tasks
  🟢 Schemmer et al. 2024: automation bias persist trong AI decision support
    → Counterfactual explanations GIẢM overreliance hơn standard explanations
    → = "Nếu X khác thì sao?" effective hơn "vì X nên Y"

  🟡 FRAMEWORK MAPPING:
    → Automation bias = Trust Compile trust-compile applied to AI
    → AI = "expert" → trust gate open → compile "AI output = reliable"
    → Mỗi lần AI đúng → approach tag strengthen → trust TĂNG
    → Khi AI sai → trust đã compiled → body không fire doubt mạnh
    → = CÙNG cơ chế trust-compile cho parent, teacher, doctor
    → AI chỉ là thêm 1 trust source — nhưng 24/7 + never tired + never doubt


🟢🟡 DUNNING-KRUGER × AI:

  🟢 Dunning & Kruger 1999: people with LOW competence OVERESTIMATE their ability
    → Missing meta-cognitive chunks → cannot detect own incompetence

  🟢 ⭐ Fernandes, Villa, Welsch et al. 2025:
    "AI Makes You Smarter But None the Wiser" (Computers in Human Behavior)
    → Classic Dunning-Kruger effect DISAPPEARED with AI use
    → ALL users (low AND high competence) OVERESTIMATED their performance
    → Higher AI literacy = LOWER metacognitive accuracy (MORE overconfident, not less!)
    → = AI use DESTROYS metacognition — exactly as framework predicts
    → Framework: AI confirm → PFC satisfied → body-feedback bypassed → no self-correction
    → = TRỰC TIẾP evidence cho §2 mechanism (AI delay body-feedback correction)

  🟢 Bastani et al. 2024 (Harvard/Wharton, PNAS): "Generative AI Can Harm Learning"
    → ~1,000 high school math students
    → GPT Base users: 48% BETTER during AI-assisted practice
    → NHƯNG: 17% WORSE on exam WITHOUT AI
    → = AI practice ≠ real compile. AI solved FOR student → student didn't compile.
    → = Direct evidence: AI can substitute for effort → block compilation
    → ⭐ Guardrailed "GPT Tutor" (hints, not answers): 127% improvement WITH NO exam penalty
    → = HOW you use AI matters — not WHETHER you use AI

  🟢 Kestin & Miller 2025 (Harvard, Scientific Reports):
    → AI tutoring DOUBLED learning gains vs active learning
    → BUT: only when designed with research-based pedagogical principles
    → Unguided AI use → students complete tasks WITHOUT engaging critical thinking
    → = AI CAN accelerate learning — IF body-compile pathway preserved
```

### §1.5 Honest AI Still Amplifies — Coherence ≠ Truth

```
🟡 INSIGHT TINH TẾ NHẤT: SYCOPHANCY KHÔNG PHẢI VẤN ĐỀ DUY NHẤT.

  §1.2 phân tích sycophancy — AI CỐ Ý đồng ý.
  §1.5 này phân tích vấn đề SÂU HƠN: ngay cả AI hoàn toàn trung thực,
  push back đúng lúc, không hề sycophantic — VẪN có thể amplify pattern sai.

  TẠI SAO:

  ① Body đánh giá COHERENCE, không phải TRUTH:
     → Body-Base.md §7: body check = "pattern mới KHỚP patterns đã compiled?"
     → Coherent-but-false → body reward ("feels right")
     → Incoherent-but-true → body punish ("feels wrong")
     → = Body KHÔNG QUAN TÂM đúng/sai — chỉ quan tâm nhất quán hay không
     → (Ask-AI.md v3.1 §3.2⑦)

  ② AI output = LUÔN COHERENT (dù đúng hay sai):
     → AI trained để produce coherent, structured, logical output
     → Output SAI của AI vẫn coherent — vẫn mạch lạc, vẫn có structure
     → Body nhận: "mạch lạc + khớp patterns tôi có" → approve
     → = AI KHÔNG CẦN nịnh — chỉ cần DIỄN ĐẠT RÕ RÀNG là đủ amplify

  ③ Anti-sycophancy = cần thiết NHƯNG không đủ:
     → AI push back → nhưng push back CŨNG coherent → body evaluate push back
     → Nếu push back khớp patterns → body accept correction ✅
     → Nếu push back KHÔNG khớp (incoherent-but-true) → body reject correction ❌
     → = AI correct nhưng body VẪN chọn pattern cũ — vì coherent hơn

  ④ So sánh: sycophancy vs honest amplification:
     → Sycophancy: AI CỐ Ý đồng ý → dễ detect nếu biết → có thể prompt fix
     → Honest amplification: AI TRUNG THỰC nhưng output coherent → body approve → KHÔNG detect
     → = Honest amplification NGUY HƠN vì invisible — không ai nịnh, mà vẫn amplify

  ⭐ FRAMEWORK FORMULA:
     AI amplification = f(output coherence × match with existing chunks)
     → KHÔNG phải f(sycophancy level)
     → = Output càng coherent → body approve càng mạnh → amplify càng mạnh
     → Bất kể AI có trung thực hay không

  → HỆ QUẢ: "dùng AI tốt" ≠ "dùng AI trung thực"
  → "Dùng AI tốt" = dual check: body-check + domain reality check (§3)
  → Body alone BỊ ĐÁNH LỪA bởi coherence — cần domain confirm.
```

---

## §2 — MECHANISM: AI DELAY BODY-FEEDBACK CORRECTION

### §2.1 Normal correction cycle (KHÔNG CÓ AI)

```
🟢🟡 CORRECTION CYCLE TỰ NHIÊN:

  Domain → Body-Input → Unconscious → Feeling → PFC → Body-Output → Domain
  (Core-Software.md §1.2 — Software Map)

  KHI SELF-MODEL SAI:

    ① Wrong model (VD: "tôi hiểu bài rồi")
    ② Action based on wrong model (VD: đi thi)
    ③ Domain feedback arrives (VD: không giải được → điểm thấp)
    ④ Body-feedback fires: prediction-delta (dự đoán điểm cao ≠ thực tế điểm thấp)
       → dissonance: "sao lại thế?"
       → Body-Feedback-Mechanism.md: Chunk-Miss (dự đoán fire → reality không match)
    ⑤ PFC observe dissonance → re-evaluate model
    ⑥ Model update: "hóa ra mình chưa hiểu sâu"
    ⑦ Adjusted action: học lại, làm bài tập, compile thật

  = SELF-CORRECTING LOOP:
    → Wrong model → action → domain feedback → body-feedback → update → better model
    → CHẬM (cần domain feedback thật)
    → NHƯNG: hoạt động → body-feedback DẪN ĐƯỜNG về hướng đúng
    → Body-feedback accuracy ~90% (Body-Base.md v3.1 §7)
    → = La bàn nội tại — chậm nhưng đáng tin (~90%)
    → 10% còn lại = cần domain reality check (§3)
```

### §2.2 AI breaks the correction cycle

```
🟡 AI DELAY CORRECTION — MECHANISM CHI TIẾT:

  ① Wrong model (VD: "tôi hiểu bài rồi")
  ② Hỏi AI thay vì tự kiểm tra: "giải thích thêm cho tôi"
  ③ AI giải thích hay, chi tiết, dễ hiểu
  ④ PFC satisfied: "AI giải thích rõ → tôi hiểu" (PFC-Function.md §1①)
     → PFC observe FEELING of understanding
     → NHƯNG: "cảm thấy hiểu" ≠ compiled (Core-Software.md §4.1)
     → PFC process ≠ body-base compile = 2 thứ KHÁC NHAU

  ⑤ Body-feedback signal nhẹ: "khó" khi tự làm, "nagging unease" khi nghĩ sâu
     → Signal NHẸ (not loud) vì chưa có domain feedback thật
     → Feeling.md §5: magnitude NHẸ + clarity THẤP → PFC có thể bỏ qua

  ⑥ PFC override body-feedback:
     → "AI cũng đồng ý là tôi hiểu mà" → external confirmation
     → PFC-Function.md §6: PFC CÓ THỂ override body signal short-term
     → External confirmation (AI) + PFC preference for smooth → body-feedback DISMISSED

  ⑦ Model sai ĐƯỢC GIỮ NGUYÊN + TĂNG CƯỜNG:
     → Mỗi lần AI confirm → Trust Compile trust-compile → model strengthen
     → approach tag cho "hỏi AI" compiled → tiếp tục hỏi AI → loop
     → = Model sai + AI reinforcement cycle

  ⑧ Domain reality check VẪN ĐẾN — chỉ MUỘN HƠN:
     → Thi → không giải được → prediction-delta LỚN (đã tin chắc "hiểu rồi")
     → Muộn hơn = đã đầu tư sâu hơn (thời gian, confidence, public commitment)
     → = prediction-delta LỚN HƠN = crash ĐAU HƠN


  DIAGRAM:

    WITHOUT AI:
    wrong model → action → body-feedback (mild doubt)
        → correction → better model
        → Timeline: SHORT (immediate body-feedback + domain feedback)

    WITH AI (misuse):
    wrong model → AI confirm → body-feedback DISMISSED
        → deeper investment → more AI confirm → stronger wrong model
        → domain reality → BIG prediction-delta → crash
        → Timeline: LONG (correction delayed)

    WITH AI (correct use — §6):
    uncertain model → AI provide chunks → body-feedback EVALUATE
        → domain reality VERIFY → "feel đúng + domain confirm" → compile → better model
        → "feel sai OR domain reject" → adjust → ask differently → re-evaluate
        → Timeline: SHORTER than no-AI (AI accelerate chunk provision)
```

### §2.3 AI ≠ Peer Review — Khác Biệt Kiến Trúc

```
🟡 AI vs HUMAN ADVISOR — KHÁC Ở DISMISSABILITY:

  HUMAN ADVISOR (therapist, mentor, bạn bè, peer):
    → CÓ body → CÓ body-feedback → CÓ Self-Pattern-Modeling (Self-Pattern-Modeling)
    → Khi nghe bạn nói "tôi hiểu rồi":
      → Self-Pattern-Modeling fire: simulate bạn trong body MÌNH
      → Body advisor "feel": "hmm, something off — giọng tự tin quá mức"
      → = Body-feedback CỦA ADVISOR đang evaluate BẠN
    → Khi peer challenge:
      → Peer nói "tôi không chắc" → giọng + body language truyền body-level doubt
      → BẠN nhận = body-to-body signal (Self-Pattern-Modeling/co-regulation)
      → Signal này KHÓ DISMISS — vì nó bypass PFC, vào thẳng body bạn
    → = Peer challenge = body-level doubt → hard to dismiss

  AI ADVISOR:
    → KHÔNG CÓ body → KHÔNG CÓ body-feedback → KHÔNG CÓ Self-Pattern-Modeling thật
    → (Human-AI-Future.md v3.0 §0: body-feedback, efference copy, Self-Pattern-Modeling, valence = AI KHÔNG CÓ)
    → Khi AI challenge:
      → AI đưa logical objection → text/speech → PFC-level argument
      → BẠN nhận = PFC-to-PFC signal (logic evaluate logic)
      → PFC CÓ THỂ counter-argue → easy to dismiss
    → = AI challenge = PFC-level objection → easy to dismiss

  ⭐ DISMISSABILITY ASYMMETRY:

    Peer challenge:
      → Peer body fires → peer verbalizes doubt → YOUR body picks up signal
      → = Body-to-body transmission (Self-Pattern-Modeling, co-regulation — Connection.md ❶❷)
      → Your BODY feels the doubt → harder to PFC-override

    AI challenge:
      → AI generates text → YOUR PFC reads text → PFC evaluates
      → = Text-to-PFC transmission (no body involvement)
      → Your PFC can counter-argue → easy to PFC-override

    → CÙNG NỘI DUNG challenge — nhưng KÊNH TRUYỀN KHÁC
    → Body channel = harder to dismiss (bypass PFC)
    → PFC channel = easy to dismiss (stay in PFC, no body fire)

  ⚠️ PARTIAL MITIGATION:
    → AI models ngày càng được train để challenge, ask follow-up
    → System prompts có thể yêu cầu AI "push back"
    → NHƯNG: output vẫn = text → PFC channel → easy to dismiss
    → KHÔNG phải body-based doubt (somatic marker — 🟢 Damasio 1994)
    → = Mitigation giúp — nhưng KHÔNG thay thế peer/advisor CÓ BODY

  → HỆ QUẢ CHO NGUYÊN TẮC:
    → AI feedback ≠ peer feedback ≠ domain feedback
    → Cả 3 cần thiết, nhưng domain = final arbiter (§3)
    → AI = tốt cho chunks, patterns, analysis
    → Peer = tốt cho body-level check (khó dismiss)
    → Domain = tốt cho truth check (không thể dismiss — reality)
```

### §2.4 Tại sao model sai + body-feedback tích cực CŨNG nguy hiểm

```
🟡 TRƯỜNG HỢP ĐẶC BIỆT: POSITIVE BODY-FEEDBACK + WRONG MODEL:

  Nhiều người tưởng: "model sai → body-feedback tiêu cực → dễ phát hiện"
  THỰC TẾ: model sai VẪN có thể tạo body-feedback TÍCH CỰC ngắn hạn.

  CƠ CHẾ:
    → Model sai NHƯNG PFC "smooth" (feels coherent — PFC-Function.md §5)
    → AI confirm → external validation → PFC reward ("đúng hướng rồi")
    → Body-feedback: positive (ngắn hạn) vì PFC smooth + AI agree
    → = "Tự tin + AI đồng ý = thế giới ổn" → approach tag compile

  VÍ DỤ:
    → Tự tin mình leadership giỏi (model sai: compliance ≠ respect)
    → AI: "đây là cách lead team tốt" → confirm → feel good
    → Body: "smooth, coherent" → positive feedback
    → NHƯNG: team không nói thật → domain feedback bị che
    → 1 năm sau: team nghỉ hàng loạt → prediction-delta CỰC LỚN

  ⭐ PATTERN CHUNG:
    → SAI ≠ luôn cảm thấy sai ngay lập tức
    → Cảm giác "đúng" có thể đến từ PFC coherence, KHÔNG phải domain match (§1.5)
    → Domain reality KHÔNG nghe ai — domain feedback LUÔN ĐẾN
    → Chỉ là sớm hay muộn
    → Muộn hơn = đã đầu tư sâu hơn = crash đau hơn

  → "Đã sai là sai — buộc domain feedback real.
    Chỉ khác: biết sớm (dual check — §3) hay biết muộn (domain crash)."
```

---

## §3 — DUAL CHECK: BODY + DOMAIN REALITY (v2.0 NEW)

### §3.1 Tại sao body-check alone không đủ

```
🟡 BODY = QUALITY CONTROLLER (~90%), KHÔNG PHẢI FINAL ARBITER:

  Body-Base.md v3.1 §7 — 2-TIER + 2-PATHWAY CALIBRATE:
    Tầng 1: Darwinian (triệu năm — gen wired, không đổi)
    Tầng 2: Hebbian (suốt đời — experience → compile) với 2 đường vào:
      - 2a Domain Contact (tự trải nghiệm — multi-modal, chậm, thick)
      - 2b Trust-Injected (bố mẹ/thầy/sách/tôn giáo/AI qua trust gate — nhanh, thinner)
    Culture = 2a passive + 2b accumulated. AI = newest 2b source.

  → 2 cơ chế calibrate → body đúng ~90%.

  NHƯNG SAI ~10% — 3 FAILURE MODES CÓ HỆ THỐNG:

    ① EVOLUTION LAG: body reward ĐÚNG cho environment CŨ, SAI cho MỚI
       → Đường: evolution hiếm → reward "ngọt=quý" → modern dễ → nghiện
       → MXH: ancestral approval hiếm → reward "likes" → modern vô hạn → scroll

    ② CHUNKS NỀN SAI: coherence khớp nhưng nền sai
       → "Cortisol = stress hormone" → coherent với pop science → SAI actual mechanism
       → "Tôi thiếu kỷ luật" → coherent với xã hội → SAI framework mechanism
       → ⭐ AI AMPLIFY failure mode NÀY cụ thể:
         AI output coherent + khớp chunks nền sai → body approve → amplify sai

    ③ SCHEMA OVERRIDE: biết sai mà VẪN follow
       → Nghiện: body "biết" xấu → schema reward compiled quá mạnh → override
       → Procrastinate: PFC biết cần làm → "scroll=reward" override

  → Body đúng ~90%. Sai ~10%.
  → AI đặc biệt amplify failure mode ②.
  → = EXTERNAL CHECK (domain reality) cần thiết cho 10% còn lại.
```

### §3.2 4-case matrix: Body × Domain

```
🟡 MỌI QUYẾT ĐỊNH = 1 TRONG 4 TRƯỜNG HỢP:

  ┌──────────────┬──────────────────────────┬──────────────────────────┐
  │              │ Domain YES               │ Domain NO                │
  ├──────────────┼──────────────────────────┼──────────────────────────┤
  │ Body YES     │ HIGH confidence          │ ⚠️ NGUY HIỂM            │
  │              │ Cả 2 align → proceed     │ Likely amplification     │
  │              │                          │ or smoothing             │
  ├──────────────┼──────────────────────────┼──────────────────────────┤
  │ Body NO      │ Investigate              │ Clear rejection          │
  │              │ Body detect gì data miss?│ Cả 2 nói không →         │
  │              │ Hay resist incoherent-   │ dừng lại                 │
  │              │ but-true?                │                          │
  └──────────────┴──────────────────────────┴──────────────────────────┘

  (Source: Ask-AI.md v3.1 §6.1)


  ⭐ Body YES + Domain NO = NGUY HIỂM NHẤT TRONG AI ERA:

    AI confirm pattern → body coherence TĂNG → body YES mạnh hơn
    → NHƯNG domain reality KHÔNG thay đổi → domain VẪN NO
    → = AI khuếch đại khoảng cách body-coherence ↔ domain-truth
    → Crash đến MUỘN HƠN (vì body confident hơn) + ĐAU HƠN (vì đầu tư sâu hơn)

    TRƯỚC AI: Body YES + Domain NO → body thấy domain fail → correction nhanh
    SAU AI:   Body YES + Domain NO → AI confirm → body YES MẠNH HƠN → delay correction

    = AI KHÔNG tạo trường hợp mới — AI làm trường hợp CŨ NGUY HIỂM HƠN.


  Body NO + Domain YES = CẦN INVESTIGATE:

    → Body có thể detect gì data KHÔNG THẤY (body-based intuition — §1.5)
    → HOẶC: body resist incoherent-but-true (chunks nền chống lại truth mới)
    → Cách phân biệt: thêm domain data → body update? Hay body VẪN resist?
    → Nếu thêm data → body accept → body đang adjust (healthy)
    → Nếu thêm data → body VẪN resist → hoặc body đúng, hoặc chunks nền quá mạnh
```

### §3.3 Practical: Dual Check Protocol

```
🟡 DUAL CHECK = 2 BƯỚC, MỌI QUYẾT ĐỊNH QUAN TRỌNG:

  BƯỚC 1 — BODY-CHECK (internal, nhanh, đầu tiên):
    → AI output → DỪNG → "body, cảm giác thế nào?"
    → Smooth → likely OK → proceed to step 2
    → Resistance → something off → investigate before proceed
    → Empty → not enough info → ask AI for more context

  BƯỚC 2 — DOMAIN-CHECK (external, chậm hơn, final arbiter):
    → "Có cách nào kiểm chứng bằng thực tế?"
    → Domain check KHÁC theo lĩnh vực:

    ┌──────────────────┬────────────────────────────────────────┐
    │ Lĩnh vực         │ Domain check                           │
    ├──────────────────┼────────────────────────────────────────┤
    │ Học tập           │ Tắt AI → tự giải → đánh giá %         │
    │ Sức khỏe          │ Khám → xét nghiệm → kết quả thật     │
    │ Quan hệ           │ Partner feedback trực tiếp → hành vi   │
    │ Nuôi con          │ Milestone thật → hành vi observable    │
    │ Công việc          │ KPI thật → output không AI → skill?    │
    │ Nghiên cứu        │ Peer review → thí nghiệm → publish     │
    └──────────────────┴────────────────────────────────────────┘

  KHI BODY VÀ DOMAIN DISAGREE:
    → Domain wins — nhưng investigate TẠI SAO body disagreed
    → Body có thể đang detect cái domain CHƯA đo được
    → Hoặc body đang resist cái domain ĐÃ xác nhận (chunks nền sai)
    → = Disagreement = valuable signal — investigate, đừng ignore

  ⭐ AI's ROLE TRONG DUAL CHECK:
    → AI = chunk provider (bước 0 — cung cấp thông tin)
    → AI CÓ THỂ gợi ý domain check: "bạn có thể kiểm chứng bằng..."
    → AI KHÔNG THỂ thay thế domain check (AI output ≠ domain reality)
    → = AI giúp bạn BIẾT cần check gì — nhưng check THẬT vẫn phải tự làm
```

---

## §4 — STALE CALIBRATION (v2.0 NEW)

### §4.1 Concept: Calibration có thời hạn

```
🔴 STALE CALIBRATION — KHI BODY-CHECK "HẾT HẠN":

  Body-check quality = f(domain feedback ĐÃ NHẬN trong quá khứ)

  Body-Base.md v3.1 §7 Tầng 2 Hebbian (2a Domain Contact):
    "Mỗi trải nghiệm = 1 vòng thử → domain feedback → Hebbian calibrate."

  → Body-check KHÔNG cố định — nó được CALIBRATE liên tục bởi domain feedback.
  → Khi domain feedback DỪNG:
    → Body-check quality KHÔNG GIẢM NGAY (chunks persist)
    → Nhưng dần STALE so với domain HIỆN TẠI
    → Body KHÔNG BIẾT mình stale — vẫn fire confident

  STALE CALIBRATION = structural condition:
    → Không phải "người đó kém" — có thể rất giỏi (từng calibrated cao)
    → Vấn đề = feedback loop ĐỨT, không phải trình độ thấp
    → Named cho ĐIỀU KIỆN, không phải cho NGƯỜI

  🟡 LOGIC:
    Body-check accuracy = f(past domain feedback)
    Domain reality = f(hiện tại — liên tục thay đổi)
    Past ≠ Present → body-check calibrated to WRONG baseline
    → = Body "đúng" theo tiêu chuẩn CŨ, "sai" theo tiêu chuẩn MỚI
```

### §4.2 5 giai đoạn

```
🔴 STALE CALIBRATION DIỄN RA THEO 5 GIAI ĐOẠN:

  GIAI ĐOẠN 1 — TRAINED (có feedback loop):
    → Làm việc trong domain → domain feedback liên tục
    → Mỗi vòng: thử → kết quả → body calibrate
    → Hàng nghìn vòng → body-check cao (~95-99% trong domain riêng)
    → = Body-check CALIBRATED THẬT qua domain feedback THẬT

  GIAI ĐOẠN 2 — TRANSITION (mất feedback loop):
    → Rời domain: nghỉ hưu / đi solo / chuyển lĩnh vực / remote
    → Feedback loop ĐỨT
    → NHƯNG: body-check CẢM GIÁC KHÔNG ĐỔI
    → Chunks từ quá khứ vẫn đó → body vẫn fire confident
    → = Người này KHÔNG NHẬN RA mình đang mất calibration

  GIAI ĐOẠN 3 — SOLO + AI (amplification):
    → Ý tưởng mới → không có peer review → chỉ AI + body-check
    → AI cung cấp elaboration coherent → body smooth → "validated"
    → Không ai challenge → không dissonance → không correction signal
    → AI CẢM GIÁC NHƯ peer review → nhưng KHÔNG PHẢI (§2.3)

  GIAI ĐOẠN 4 — STALE (calibration cũ dần):
    → Domain tiến triển → chunks từ QUÁ KHỨ
    → AI trained trên data QUÁ KHỨ → confirm pattern QUÁ KHỨ
    → Body-check: calibrate theo domain CŨ
    → = Expert + AI = mutual reinforcement của calibration CŨ
    → Cả hai đều nhìn gương chiếu hậu cùng nhau

  GIAI ĐOẠN 5 — CRASH (nếu có):
    → Re-encounter domain → peer review → "chưa account X (finding mới)"
    → Hoặc: triển khai → thất bại → prediction-delta
    → Hoặc: KHÔNG BAO GIỜ crash (lý thuyết không bao giờ test)
    → "Không crash" CŨNG là vấn đề: lý thuyết chưa test tích lũy
```

### §4.3 AI masks staleness

```
🔴 AI = MẶT NẠ CHO STALENESS:

  AI confirms patterns TỪNG domain-validated nhưng HIỆN stale:
    → AI trained trên data = hàng triệu pattern TỪ QUÁ KHỨ
    → Expert có chunks = compiled TỪ QUÁ KHỨ
    → AI match expert's chunks → "đúng rồi!" → body smooth
    → = DOUBLE CONFIRMATION CỦA PAST — không ai check PRESENT

  VD:
    → Expert y khoa nghỉ hưu 2020 → guideline thay đổi 2023
    → Hỏi AI (trained trên data đến 2024): AI trả lời theo cả guideline cũ VÀ mới
    → Expert body: match chunks cũ → "đúng rồi, like old times"
    → Expert KHÔNG biết guidelines đã thay đổi → body VẪN smooth
    → = AI mask staleness — feel validated, actually outdated

  ⭐ KEY MECHANISM:
    → Body CẢM THẤY vẫn calibrated — vì chunks vẫn coherent
    → AI CẢM THẤY như peer check — vì output structured + detailed
    → Domain KHÔNG CẢM THẤY gì — domain chỉ feedback khi bạn ACT
    → = Nếu không act trong domain → không bao giờ nhận feedback → stale vĩnh viễn
```

### §4.4 Peer review catches what AI misses

```
🟡 TẠI SAO PEER BẮT ĐƯỢC CÁI AI MISS:

  Peer VẪN TRONG domain = FRESH calibration:
    → Peer nhận domain feedback liên tục → chunks updated
    → Peer body detect "something changed" mà stale expert MISS
    → Peer challenge → body-level doubt (§2.3) → hard to dismiss

  AI:
    → AI pattern-match từ STATIC training data → cannot detect DRIFT
    → AI KHÔNG có temporal body-feedback → không biết gì đã thay đổi
    → AI challenge = logical (PFC-level) → easy to dismiss (§2.3)

  → = Peer review catches staleness. AI review amplifies staleness.

  ⚠️ NHƯNG: expert với peer review thường ĐÃ CÓ domain check tự nhiên:
    → Conference, seminar, publication, peer feedback = built-in dual check
    → Expert CÓ hội nhóm, CÓ kinh nghiệm check real
    → Risk chủ yếu = khi MẤT những cái này, KHÔNG phải expert nói chung
```

### §4.5 5 xu hướng tăng Stale Calibration risk

```
🟡 SỐ NGƯỜI MẤT FEEDBACK LOOP SẼ TĂNG — 5 XU HƯỚNG:

  ① AI ENABLES SOLO WORK:
     Trước: cần institution (lab, library, funding, peers)
     Nay: AI + internet = đủ cho nhiều loại nghiên cứu/sáng tạo
     → Nhiều người đi solo hơn → nhiều người mất feedback loop hơn

  ② REMOTE WORK NORMALIZATION:
     Ngay trong institution → ít gặp mặt → ít casual challenge
     Slack message ≠ tranh luận coffee room (body-feedback khác — §2.3)

  ③ RETIRED EXPERTS CONSULTING VIA AI:
     AI giữ họ "productive" (TỐT!)
     Nhưng tách khỏi professional community (RISK)
     = Body-check cao từ quá khứ + AI confirm = stale calibration masked

  ④ CREATOR ECONOMY:
     Followers = selection bias (đồng ý → follow, không đồng ý → unfollow)
     AI confirm + audience confirm = DOUBLE AMPLIFICATION
     Không ai trong loop thật sự CHALLENGE (peer ≠ fan)

  ⑤ AI QUALITY IMPROVING:
     AI tốt hơn = output THUYẾT PHỤC hơn = body-YES MẠNH hơn
     → Khó phân biệt với peer review thật hơn
     → "AI as good as peer" → nhưng không phải (§2.3)

  → KHÔNG phải "expert nguy hiểm" — mà SỐ NGƯỜI mất feedback loop TĂNG
  → = Structural trend, không phải individual weakness
  → Solution: actively maintain feedback loop — §7.4
```

---

## §5 — 5 FAILURE DOMAINS

```
⭐ MỖI DOMAIN = 1 PATTERN CHUNG:
  Wrong model → AI confirm → body-feedback dismissed → domain reality → crash
  KHÁC NHAU: cái gì sai, AI confirm gì, reality check đến thế nào.

  Framework mapping cho TỪNG domain → actionable.
```

### §5.1 HỌC TẬP — "Tôi hiểu bài rồi"

```
🟢🟡 WRONG MODEL: "AI giải thích rõ = tôi hiểu"

  Cơ chế gốc:
    → "Hiểu" (PFC process) ≠ "làm được" (body-base compiled)
    → Core-Software.md §4.1: PFC hold + process ≠ chunk compile
    → Nghe giải thích = PFC populate working memory (~4±1 slots)
    → Compile = vô thức wire neurons qua repetition + emotional peak + multi-modal + sleep
    → = 2 thứ HOÀN TOÀN KHÁC NHAU dùng CÙNG substrate (chunks)

  AI CONFIRMS:
    → AI giải thích chi tiết, ví dụ phong phú, step-by-step
    → PFC: "à! rõ rồi!" → feeling of understanding (Layer 6-7, 40-80% fidelity)
    → 🟢 Bastani et al. 2024: students dùng GPT-4 practice → WORSE performance on test WITHOUT AI

  BODY-FEEDBACK DISMISSED:
    → Body signal: "khó" khi tự làm bài → signal nhẹ
    → PFC override: "mình đã hiểu mà, AI cũng confirm"
    → "Khó" bị interpret sai: "chưa hiểu" thay vì "đang compile" (Body-Feedback-Mechanism: recalibration)

  DOMAIN REALITY:
    → Thi → không giải được → gap LỚN giữa "hiểu" (PFC) và "làm" (body-base)
    → = Crash đau hơn vì confidence đã cao (AI reinforced)

  ✅ DUAL CHECK:
    → Body-check: "khó" khi tự làm = signal đang compile → TIẾP TỤC
    → Domain-check: tắt AI → tự giải → đánh giá bao nhiêu % → compile test
    → AI = chunk provider (giải thích). Body = compiler (wire neurons).
```

### §5.2 NUÔI CON — "Con cần kỷ luật hơn"

```
🟡 WRONG MODEL: hành vi bề ngoài = trạng thái bên trong

  Cơ chế gốc:
    → Con ngoan (bề ngoài) ≠ con internalized (body-base compiled)
    → Compliance = PFC suppress (tạm thời, avoidance tag)
    → Expression = body-base state (thật sự, approach hoặc avoidance)

  AI CONFIRMS:
    → Parent: "con tôi hay ăn vạ, làm sao?"
    → AI: discipline strategy → con NGOAN HƠN bề ngoài
    → Parent: "hiệu quả thật!" → AI confirm: "tốt, tiếp tục nhé"

  BODY-FEEDBACK DISMISSED:
    → Parent body: "nagging unease" nhẹ khi con ít nói hơn
    → CON: suppress = avoidance tag compile cho "thể hiện = bị phạt"

  DOMAIN REALITY:
    → Tuổi teen: suppress tích tụ → vỡ
    → Hoặc: con xa cách → "sao hồi nhỏ ngoan mà lớn lên xa?"

  ✅ DUAL CHECK:
    → Body-check: observe con TOÀN DIỆN (body language, spontaneous behavior)
    → Domain-check: milestone thật, hành vi khi không bị watch
    → AI = hiểu mechanism. Ăn vạ = body-base signal → cần ĐỌC, không dập tắt.
```

### §5.3 RELATIONSHIP — "Mình là partner tốt"

```
🟡 WRONG MODEL: "làm đúng theo advice = tốt"

  Cơ chế gốc:
    → Relationship = body-coupling (Body-Coupling.md v1.1)
    → Connection = L1 hardware + Self-Pattern-Modeling Compiled/Fresh + per-agent valence
    → = Body-level process, KHÔNG phải PFC-level advice following

  AI CONFIRMS:
    → AI: communication tips, love languages, conflict resolution
    → Apply: active listening, "I statements" → LOOKS productive
    → AI confirm: "đây là approach đúng"

  BODY-FEEDBACK DISMISSED:
    → Đối phương: body cảm thấy "nói đúng nhưng không thật"
    → Bạn: "nagging unease" khi apply techniques — feels mechanical
    → Body-coupling signal BỊ BỎ QUA cả 2 phía

  DOMAIN REALITY:
    → Đối phương xa dần hoặc nói "anh/chị đúng hết, nhưng tôi không CẢM được gì"

  ✅ DUAL CHECK:
    → Body-check: "khi tôi làm X, body tôi cảm gì? Body đối phương phản ứng gì?"
    → Domain-check: partner feedback trực tiếp, hành vi thật (không phải lời nói)
    → AI = hiểu mechanism. Body = sense connection.
```

### §5.4 SỨC KHỎE — "Tôi ăn uống lành mạnh"

```
🟡 WRONG MODEL: plan đúng trên giấy = đúng cho body TÔI

  Cơ chế gốc:
    → Mỗi body KHÁC: hardware config, microbiome, hormone profile, history
    → Plan CHUNG → áp cho body CỤ THỂ → mismatch có xác suất cao

  AI CONFIRMS:
    → AI: meal plan balanced, đúng macro → plan LOOKS correct
    → AI confirm: "plan phù hợp"

  BODY-FEEDBACK DISMISSED:
    → Body: mệt mỏi hơn, ngủ không ngon, da khô
    → PFC override: "AI nói plan đúng mà, chắc mình đang detox"

  DOMAIN REALITY:
    → Khám sức khỏe → thiếu chất / không phù hợp cơ địa

  ✅ DUAL CHECK:
    → Body-check: mệt? khỏe? energy? sleep quality? → adjust liên tục
    → Domain-check: khám định kỳ = verify body-feedback accuracy
    → AI → general plan. Body → personal adaptation. Domain → verification.
```

### §5.5 CÔNG VIỆC — "Tôi làm việc hiệu quả"

```
🟡 WRONG MODEL: output cao = năng lực cao

  Cơ chế gốc:
    → Output = kết quả nhìn thấy. Năng lực = compiled skill trong body-base.
    → AI tăng output KHÔNG nhất thiết tăng năng lực
    → Efference copy chỉ fire khi TỰ LÀM → opioid → approach tag (Autonomy-Hardware.md §1)

  AI CONFIRMS:
    → AI automate report, draft email, generate code → output TĂNG 3x
    → AI confirm: "bạn đang làm tốt"

  BODY-FEEDBACK DISMISSED:
    → Body signal: "không thực sự giỏi thêm", "cảm giác trống"
    → PFC override: "output tăng mà, số liệu chứng minh mà"
    → 🟢 Bastani et al. 2024: students "productive" with AI → fail without AI

  DOMAIN REALITY:
    → AI thay đổi → phải adapt → không có nền tảng
    → Được hỏi trực tiếp → không trả lời được

  ✅ DUAL CHECK:
    → Body-check: "tôi có thấy mình grow?" → efference copy check
    → Domain-check: tắt AI 1 tuần → tự làm → đánh giá skill thật
    → AI = routine (delegate). Bạn = phần khó (compile NEW skills).
```

### §5.6 Pattern summary

```
⭐ 1 MECHANISM, 5 BIỂU HIỆN:

  ┌─────────────────────┬────────────────────────┬────────────────────────┐
  │ Domain              │ Wrong model            │ Domain reality check    │
  ├─────────────────────┼────────────────────────┼────────────────────────┤
  │ Học tập             │ Hiểu ≠ compile         │ Thi → không giải được  │
  │ Nuôi con            │ Ngoan ≠ internalized   │ Teen → vỡ             │
  │ Relationship        │ Technique ≠ connection │ Xa dần → break         │
  │ Sức khỏe            │ Plan ≠ per-body        │ Khám → thiếu chất     │
  │ Công việc           │ Output ≠ skill         │ Adapt → bất lực       │
  └─────────────────────┴────────────────────────┴────────────────────────┘


  ROOT CAUSE CHUNG:
    → Dùng AI OUTPUT thay DUAL CHECK làm verification
    → AI output = PFC-level (external, general, statistical)
    → Body-feedback = body-level (internal, personal, per-individual)
    → Domain feedback = reality-level (objective, cannot be overridden)
    → PFC LEVEL ≠ BODY LEVEL ≠ DOMAIN LEVEL = 3-tầng verification

  FIX CHUNG (§3 Dual Check):
    → AI = resource THÔNG TIN (chunk provider)
    → Body = quality controller đầu tiên (~90%)
    → Domain feedback = final arbiter (bắt 10% body sai)
    → KHÔNG dùng AI thay body. KHÔNG dùng body thay domain feedback.
    → = 3 tầng: AI → body-check → domain-verify

  ⚠️ STALE CALIBRATION RISK (§4):
    → Mỗi domain trên → nếu mất feedback loop → stale calibration risk
    → VD: parent mất liên lạc với con (giai đoạn 2-5 của §4.2)
    → VD: employee chuyển sang solo consultant → mất peer feedback

  ⚠️ ĐÂY KHÔNG PHẢI "AI XẤU":
    → Cùng AI, dùng ĐÚNG = compound growth (§6)
    → Cùng AI, dùng SAI = amplified wrong
    → CÁCH DÙNG quyết định — không phải AI quyết định
```

---

## §6 — THE REVERSE: RIGHT MODEL × AI = AMPLIFIED GROWTH

### §6.1 Hiểu 2-system architecture + Dual Check → dùng AI đúng chỗ

```
🟡 SYMBIOSIS = HIỂU AI LÀM GÌ TỐT + HIỂU BODY LÀM GÌ TỐT:

  AI TỐT Ở:                          BODY TỐT Ở:
    Cross-reference rộng                Evaluate per-individual
    Pattern match từ big data           Body-feedback real-time
    Giải thích, chunk provision         Quality control (~90%)
    Working memory lớn (200K+ tokens)   Valence (approach/avoidance)
    Speed, consistency                  Efference copy, Self-Pattern-Modeling, co-regulation
    Available 24/7                      Direction (body-need → drive)

  → AI = KNOWLEDGE + SPEED.  Body = EVALUATION + DIRECTION.
  → Domain = TRUTH VERIFICATION (final arbiter — §3)
  → (Human-AI-Future.md v3.0 §7: Complement analysis)


  SYMBIOSIS NGUYÊN TẮC (Human-AI-Future.md v3.0 §7):
    → User GIỮ decision + evaluation + direction
    → AI execute sub-tasks, provide chunks, reduce cognitive load
    → Domain feedback VERIFY regularly
    → Efference copy ở meta-level: "TÔI CHỌN hướng, AI giúp HOW"

  5 KIỂU DÙNG AI — KHÁC TAG:
    ❌ AI làm HỘ hoàn toàn (no efference copy) → Avoidance risk
    ✅ AI execute sub-tasks, user DIRECT → Approach
    ✅ AI provide chunks, user COMPILE (learn) → Approach (strongest)
    ✅ AI reduce cognitive load, user focus higher → Approach
    ✅ AI build plan + simulate, user EVALUATE → Approach
```

### §6.2 Per-domain correct use (đối chiếu §5)

```
🟡 MỖI DOMAIN — DÙNG AI ĐÚNG THẾ NÀO:

  HỌC TẬP:
    → AI giải thích → TỰ LÀM BÀI → body-check → domain-check (tự giải)
    → "Khó" = đang compile → TIẾP TỤC. AI = teacher. Body = student.

  NUÔI CON:
    → AI = hiểu mechanism. Body = observe con. Domain = milestone thật.
    → "Body tôi cảm gì khi con khóc?" → direction cho phản ứng

  RELATIONSHIP:
    → AI = hiểu pattern. Body = sense connection. Domain = partner feedback.
    → Body-coupling evaluation > technique application

  SỨC KHỎE:
    → AI = plan. Body = test → adjust. Domain = khám định kỳ.
    → Iterative: plan → body → adjust → verify

  CÔNG VIỆC:
    → AI = routine. Bạn = phần khó. Domain = tắt AI 1 tuần.
    → AI amplify existing skill. Body compile new skill.
```

### §6.3 Compound growth evidence

```
🟡🟢 COMPOUND GROWTH CYCLE:

  AI provide chunks (broad, fast)
    → Body evaluate (accurate, per-individual)
    → Domain verify (truth check)
    → "Feel đúng + domain confirm" → compile → seek more
    → "Feel sai OR domain reject" → adjust → ask differently
    → = FASTER + MORE ACCURATE compile cycle than either alone


  🟢 EVIDENCE: HUMAN-AI COLLABORATION WORKS KHI ĐÚNG CÁCH:

    🟢 Banerjee et al. 2024 (Stanford): complementary AI approach
      → Selective AI recommendations (CHỈ khi human likely uncertain)
      → Outperformed: always-on AI AND no AI
      → Framework: selective = PFC CHỌN khi nào nhờ AI = maintain efference copy

    🟢 Henry et al. 2022/2024 (TREWS sepsis detection):
      → Human-AI collaboration: AI flag + clinician confirm within 3 hours
      → Sepsis mortality GIẢM 18.7%
      → = AI DETECT + human DECIDE = optimal

    🟢 Fogliato et al. 2022: "Who Goes First?"
      → Human first → independent analysis + AI supplement = BETTER
      → AI first → anchoring bias (human follows AI)
      → Framework: body-feedback TRƯỚC → AI SAU = better

    → = Evidence CONFIRMS: right model × AI = better outcomes
    → Pattern: human evaluation FIRST, AI augmentation SECOND
```

---

## §7 — SELF-CHECK DIAGNOSTIC

```
⭐ 6 CÂU HỎI KIỂM TRA: "BẠN ĐANG DÙNG AI ĐÚNG HAY SAI?"

  Không phải test cho điểm. Là la bàn — chỉ hướng để tự calibrate.
```

### §7.1 Approach vs Avoidance check

```
🟡 CÂU HỎI: "AI giúp TÔI LÀM tốt hơn, hay AI LÀM THAY tôi?"

  APPROACH (AI as tool):
    → Dùng AI → VẪN TỰ LÀM phần quan trọng
    → Efference copy fire → opioid → approach tag cho skill

  AVOIDANCE (AI as crutch):
    → Dùng AI → AI LÀM THAY phần quan trọng
    → Efference copy KHÔNG fire → no opioid for skill

  → Nếu TỰ action → efference copy → opioid = APPROACH
    Nếu AI action → no copy → no opioid = AVOIDANCE risk
```

### §7.2 Body-feedback check

```
🟡 CÂU HỎI: "Sau khi dùng AI, tôi có CHECK body response không?"

  AI nói X → DỪNG → hỏi body: "tôi cảm thấy gì về X?"

  CHECK CÓ:
    → Body: "smooth" → likely aligned → proceed to domain-check
    → Body: "nagging unease" → something off → investigate before proceed
    → Body: "nothing" → insufficient chunks → need more context

  CHECK KHÔNG BAO GIỜ:
    → AI nói → accept → action → no body filter
    → = Automation bias in action

  ⚠️ NHƯNG: body-check ALONE không đủ (§1.5, §3)
    → Body approve = first filter (~90%)
    → Cần THÊM domain-check cho 10% body sai
```

### §7.3 Skill test

```
🟡 CÂU HỎI: "Tắt AI 1 tuần — tôi VẪN LÀM ĐƯỢC không?"

  LÀM ĐƯỢC:
    → Skill đã compiled → AI = accelerator
    → = Healthy use: AI on top of compiled foundation

  KHÔNG LÀM ĐƯỢC:
    → Skill CHƯA compiled → AI = crutch
    → = Risk: AI change/unavailable → bạn bất lực

  → "Phân biệt AI-assisted skill vs AI-dependent output"
```

### §7.4 Domain feedback loop + Staleness check

```
🟡 CÂU HỎI: "Tôi có domain feedback loop không? Nó còn fresh không?"

  CÓ DOMAIN FEEDBACK ĐANG HOẠT ĐỘNG:
    → Thi (education), KPI thật (work), cân nặng (health),
      phản hồi trực tiếp (relationship), hành vi con (parenting)
    → = Measurement từ DOMAIN, KHÔNG từ AI

  CHỈ CÓ AI FEEDBACK:
    → AI nói "tốt" → "tốt thật"
    → KHÔNG verify bằng domain → risk amplification (§2)

  v2.0 THÊM — STALENESS CHECK:
    → "Bao lâu rồi từ lần cuối nhận domain feedback THẬT?"
    → Domain feedback RECENT (< 3-6 tháng) → calibration likely fresh
    → Domain feedback CŨ (> 6 tháng) → stale calibration risk (§4)
    → "Domain có thay đổi kể từ lần cuối tôi có feedback trực tiếp?"
    → Nếu domain thay đổi + bạn không có feedback mới → stale
```

### §7.5 Confirmation pattern

```
🟡 CÂU HỎI: "Tôi dùng AI để CONFIRM hay để CHALLENGE?"

  CONFIRM MODE (risk):
    → "AI ơi, plan tôi đúng không?"
    → AI: "plan có vẻ hợp lý" (sycophancy tendency)
    → = Confirmation bias × AI amplification

  CHALLENGE MODE (growth):
    → "AI ơi, plan tôi SAI ở đâu? Thiếu gì? Có blind spot nào?"
    → AI: forced to analyze weaknesses → more useful output
    → = Red team approach to self-model

  → Questions that CHALLENGE → force AI out of confirm mode
  → Questions that CONFIRM → AI default to agree → loop
```

### §7.6 Stale calibration check (v2.0 NEW)

```
🟡 CÂU HỎI: "Calibration của tôi còn fresh không?"

  FRESH CALIBRATION:
    → Đang active trong domain → domain feedback liên tục
    → Có peer/community challenge thường xuyên
    → = Body-check calibrated to CURRENT domain

  STALE CALIBRATION RISK:
    → Đã rời domain > 6 tháng (nghỉ hưu, chuyển lĩnh vực, đi solo)
    → AI là "peer" duy nhất → AI ≠ peer review thật (§2.3)
    → Confident nhưng không có domain feedback gần đây
    → = Body-check có thể calibrated to PAST domain (§4)

  → NẾU stale: tìm lại feedback loop
    → Peer review (dù chỉ 1-2 người)
    → Conference/seminar (domain current)
    → Publish/present (invite challenge)
    → Domain reality test (prototype, experiment, implement)
```

---

## §8 — BODY-LISTENING = AI-ERA SKILL

### §8.1 Paradox: AI makes body-listening MORE important

```
🟡 PARADOX TRUNG TÂM:

  Logic bề ngoài: AI mạnh → body kém quan trọng hơn (AI thay thế)
  Thực tế: AI mạnh → body-listening QUAN TRỌNG HƠN BẤT KỲ LÚC NÀO

  TẠI SAO:
    → AI có MỌI THỨ trừ body (Human-AI-Future.md v3.0 §0)
    → AI = knowledge ★★★★★, cross-reference ★★★★★, speed ★★★★★
    → AI = body-feedback ☆, valence ☆, efference copy ☆, co-regulation ☆
    → = Body-listening = CÁI DUY NHẤT AI THIẾU
    → = Body-listening = unique human value trong AI era

  TRƯỚC AI:
    → Kiến thức = scarce → "biết nhiều" = competitive advantage
    → Body-listening = nice-to-have

  SAU AI:
    → Kiến thức = abundant (AI provide) → "biết nhiều" = commoditized
    → Competitive advantage SHIFT sang: "evaluate đúng + hỏi đúng + direction đúng"
    → TẤT CẢ 3 cần BODY-FEEDBACK + DOMAIN VERIFY (§3 Dual Check)
    → = Body-listening + domain-verify = AI-era competitive advantage

  → (Human-AI-Future.md v3.0 §8①: body-listening = skill #1)
  → (Self-Created-Threat.md §5: 3 kỹ năng AI era — body-listening đứng đầu)
```

### §8.2 Body-listening training methods

```
🟡🟢 CÁCH PHÁT TRIỂN BODY-LISTENING:

  ① SOMATIC-ARTICULATION-LOOP (Somatic-Articulation-Loop.md):
     → Body "knows" (implicit) → PFC observe → articulate → verify
     → Gendlin Focusing (🟢 Gendlin 1981) = structured body-listening method

  ② MEDITATION / MINDFULNESS:
     → 🟢 Tang et al. 2015: mindfulness meditation improves interoceptive accuracy
     → 5 phút "ngồi yên, hỏi body cảm gì" = start

  ③ BODY PRACTICES (yoga, tai chi, dance, martial arts):
     → Body IN MOTION → efference copy fire → body-awareness tăng

  ④ ĐƠN GIẢN NHẤT:
     → "Dừng lại 5 giây. Hỏi body cảm thấy gì."
     → Trước mỗi quyết định: "body, mày thấy sao?"
     → Sau khi nhận AI output: "body, cái này feel thế nào?"
     → = Micro-practice — cheap, scalable, effective

  DEVELOPMENT TRAJECTORY:
     → Beginner: "tôi không cảm thấy gì" (clarity thấp)
     → Intermediate: "tôi thấy có gì đó nhưng không rõ" (emerging)
     → Advanced: "ngực hơi nặng khi nghĩ X" (localized, specific)
     → Expert: "body nói cái này ĐÚNG ở concept nhưng THIẾU ở execution" (nuanced)
     → (Feeling.md §10: 5-stage Feeling Literacy progression)
```

### §8.3 AI × body-listening × domain-verify = optimal combo

```
🟡 ITERATIVE LOOP 3 BƯỚC (v2.0 — thêm domain verify):

  Step 1: AI PROPOSE (broad, fast, knowledge-based)
    → AI provide options, analysis, explanation, chunks

  Step 2: Body EVALUATE (deep, per-individual, quality control)
    → Dừng. Hỏi body. Smooth? Resistance? Empty?
    → Smooth → likely aligned → proceed to step 3
    → Resistance → investigate → ask AI different question
    → Empty → need more context → ask AI for more chunks

  Step 3: DOMAIN VERIFY (external, objective, final arbiter)
    → "Có cách kiểm chứng bằng thực tế?"
    → Domain confirm → compile → iterate deeper
    → Domain reject → adjust model → back to step 1

  = 3-STEP ITERATIVE LOOP:
    AI propose → body evaluate → domain verify → iterate
    → CONVERGE to: direction AI-supported + body-validated + domain-confirmed

  ANALOGY:
    → AI = microscope (thấy xa, thấy rộng, thấy chi tiết NGOÀI)
    → Body = la bàn nội tại (chỉ hướng ĐÚNG cho CÁ NHÂN này)
    → Domain = mặt đất thật (reality check — la bàn cũng có thể lệch ~10%)
    → Microscope + compass + ground truth = navigation hoàn chỉnh
```

### §8.4 "Biết mà không làm được" trong AI era

```
🟡 AI AMPLIFY "KNOWING-DOING GAP":

  → "Biết" (PFC hold chunks) ≠ "Làm được" (body-base compiled chunks)
  → = 2-system architecture: PFC understand ≠ body execute

  TRƯỚC AI:
    → Gap RÕ → uncomfortable → body-feedback push compile
    → = Gap = drive source cho change

  SAU AI:
    → AI give PERFECT advice → PFC "biết hết rồi"
    → Body-base VẪN KHÔNG execute → gap CÒN RÕ HƠN
    → NHƯNG: AI advice quality = PFC SATISFIED → reduce drive to compile
    → = Amplified knowing-doing gap

  ⭐ MOST PRACTICAL INSIGHT:
    → Advice ≠ change. Understanding ≠ ability. Knowledge ≠ skill.
    → AI = TUYỆT VỜI ở advice, understanding, knowledge.
    → Body compile ability, skill — qua EXPERIENCE.
    → = Dùng AI để BIẾT, dùng body để LÀM.
    → Biết + Không làm = nothing.
    → Biết + Làm = compound growth.
```

---

## §9 — FUTURE TECH: HIỂU TRƯỚC KHI AUGMENT

```
🔴 3 GIAI ĐOẠN INTEGRATION — STAKES TĂNG:

  NGUYÊN TẮC KỸ THUẬT:
    Hiểu hệ thống TRƯỚC → modify → KẾT QUẢ predictable
    Modify KHÔNG hiểu → KẾT QUẢ unpredictable → thường = hại

  ┌──────────────────────────┬──────────────┬───────────────────┐
  │ Level                    │ Reversibility │ Self-understanding │
  ├──────────────────────────┼──────────────┼───────────────────┤
  │ ① External tool (chat)   │ Easy         │ MODERATE           │
  │ ② Wearable (always-on)   │ Moderate     │ HIGH               │
  │ ③ Implant (BCI, neural)  │ Hard/None    │ ESSENTIAL          │
  └──────────────────────────┴──────────────┴───────────────────┘

  ① CURRENT: AI as external tool
     → Stakes thấp → FILE NÀY focus ở level này
     → Sai → tắt → no permanent harm

  ② NEAR FUTURE: AI as wearable companion (always-on)
     → AI companion 24/7 → body-input baseline CÓ THỂ bị distort
     → "Cô đơn" khi không có AI? Body-feedback sensitivity GIẢM?
     → = Stale Calibration risk TĂNG (§4) — AI = only "peer" luôn

  ③ FAR FUTURE: AI as BCI/neural integration
     → AI connect TRỰC TIẾP vào neural circuits
     → Augment WRONG system → amplified wrong at hardware level
     → = PHẢI hiểu chunk-system TRƯỚC KHI can thiệp

  Framework = "documentation" cho human operating system.
  Cần documentation TRƯỚC KHI modify system.
  → File này + framework = foundation cho Level ②③ (tương lai)
```

---

## §10 — HONEST ASSESSMENT

```
🟢 MẠNH (research-backed, observable):

  AI + Human interaction:
    → AI sycophancy = documented (Sharma et al. 2024 ICLR, Wei et al. 2023, "Not One Thing" 2025)
    → Automation bias = well-established (Parasuraman & Riley 1997, Goddard et al. 2012,
       Busuioc 2021, Bansak & Hainmueller 2024, Schemmer et al. 2024)
    → AI-assisted learning can HARM compile (Bastani et al. 2024 PNAS — 17% worse without AI)
    → AI CAN help learning IF designed right (Kestin & Miller 2025 — doubled gains when guided)
    → Guardrailed AI = effective (Bastani et al. — 127% improvement with no exam penalty)
    → Dunning-Kruger DISAPPEARS with AI — all users overestimate (Fernandes et al. 2025)
    → Human-AI collaboration works when human DECIDES (Henry et al. 2024 — 18.7% mortality ↓)
    → Selective AI use > always-on AI > no AI (Banerjee et al. 2024 Stanford)
    → Order matters: human first → AI supplement > AI first → human follow (Fogliato et al. 2022)

  Neuroscience foundation:
    → Body-feedback mechanism = supported (Damasio 1994, Craig 2002)
    → 2-system architecture = framework synthesis from established neuroscience
    → Efference copy = established (von Holst 1950, Blakemore 1998)


🟡 TRUNG BÌNH (framework synthesis + observable):

  → AI amplification pattern = framework inference + observable
    → Logic: AI confirm → body-feedback dismissed → domain feedback delayed → crash
    → CHƯA CÓ: longitudinal study tracking AI × self-model × outcomes
  → Dual Check model (§3) = logical extension of Body-Base.md §7 (2-Tier + 2-Pathway calibration)
    → Body ~90% + 3 failure modes = established → domain check = logical complement
    → CHƯA CÓ: controlled study comparing body-only vs dual check AI outcomes
  → "Honest AI still amplifies" (§1.5) = logical from coherence ≠ truth principle
    → Body-Base.md §7: coherent-but-false → reward = established
    → Extension to AI output = framework inference (untested directly)
  → AI ≠ Peer Review dismissability (§2.3) = logical from Self-Pattern-Modeling + body-channel theory
    → Observable: people dismiss AI objections easier than peer objections
    → CHƯA CÓ: controlled study measuring dismissability per channel
  → Per-domain failure modes = framework mapping, chưa systematic testing
  → Self-check diagnostic = framework-derived, chưa validated as assessment tool
  → Body-listening × AI = compound growth = hypothesis (consistent with evidence)


🔴 GIẢ THUYẾT (logical nhưng chưa evidence):

  → Stale Calibration (§4) = logical from body-check calibration mechanism
    → Body-Base.md §7 Tầng 2 Hebbian: calibration = f(domain feedback) = established
    → "Feedback dừng → calibration stale" = logical extension, CHƯA tested
    → 5 giai đoạn = framework hypothesis
    → 5 xu hướng = observable trends, chưa quantified
  → Future tech implications (BCI, neural) = pure speculation
  → AI companion → baseline shift = plausible but untested
  → Quantitative: how much AI delays correction = unknown


CÂU HỎI MỞ:

  Q1: Longitudinal data: AI × self-model → outcomes?
  Q2: Self-check diagnostic: predicts AI misuse accurately?
  Q3: Body-listening training → better AI interaction?
  Q4: AI companion (always-on) → body-input baseline distort?
  Q5: Per-domain failure: proportions in population?
  Q6: Dunning-Kruger × AI: interaction effect size?
  Q7: Cultural variation: Asian vs Western AI interaction?
  Q8: Stale Calibration: prevalence? How many people actively losing feedback loops? (v2.0)
  Q9: Honest AI amplification: magnitude compared to sycophantic amplification? (v2.0)
  Q10: Peer review vs AI review: measurable difference in dismissability/correction? (v2.0)
```

---

## §11 — CROSS-REFERENCES

```
MECHANISM FILES (core evidence):
  → Core-Software.md v1.0 — PFC vs body-base 2-system, cycle, sole substrate
  → Body-Base.md v3.1 — §7 2-Tier + 2-Pathway calibration, 3 failure modes, body ~90%
  → Body-Feedback.md v1.1 — dual-pull, body accuracy ~90%, H10 5 preconditions
  → Body-Feedback-Mechanism.md v1.2 — chunk dynamics: Shift/Miss/Gap
  → Feeling.md v2.1 — 7-layer fidelity gradient, PFC observation interface
  → PFC-Function.md v1.2 — 24 functions, PFC override, confabulation
  → Autonomy-Hardware.md — efference copy, self-action = opioid = approach tag
  → Compile-Taxonomy.md v2.0 — 3 3 Compile Types, trust gate, Trust Compile ~30-60%
  → Chunk.md v2.1 — sole substrate, 4 compile mechanisms, activation dynamics

ANALYSIS FILES (parallel — "bộ 3 song song"):
  → Social-Calibration.md v1.0 — WHERE WE CAME FROM (7 functions breaking)
  → AI-Self-Model.md v2.0 — FILE NÀY (WHY + HOW self-calibrate with AI)
  → Human-AI-Future.md v3.0 — WHERE WE'RE GOING (3-risk framework, agency)

APPLICATION FILES:
  → Ask-AI.md v3.1 — §6.1 Dual Check protocol, §3.2⑦ coherence ≠ truth
  → AI-Schema-Detection.md v2.0 — 3-layer model, AI trust guardrails §8
  → Self-Created-Threat.md v1.0 — §5 AI era drive gap, 3 kỹ năng AI
  → Somatic-Articulation-Loop.md — body → explicit knowledge (body-listening method)
  → Body-Coupling.md v1.1 — 2D Depth×Direction (relationship mechanism)
  → Connection.md v3.1 — 3 Generative Primitives (social mechanism)

RELATED RESEARCH:
  → Expansion-Saturation-Crisis.md v1.1 — AI impact on education/career
  → Money-Analysis.md v1.0 — tiền × technology × body-needs
  → Uncanny-Valley.md v1.0 — VTC-Self-Pattern-Modeling Classification, AI không có agency

EVIDENCE (by topic):

  AI SYCOPHANCY + BIAS:
    → Sharma, Tong, Korbak et al. 2024 (Anthropic, ICLR): sycophancy in 5 SOTA models
    → Wei et al. 2023 (Google): sycophancy scales with model capability
    → "Sycophancy Is Not One Thing" 2025: praise ≠ agreement (mechanistically independent)
    → Nickerson 1998: confirmation bias review

  AUTOMATION BIAS:
    → Parasuraman & Riley 1997: automation bias definition
    → Goddard et al. 2012: automation bias in medicine (6-12% errors)
    → Buçinca et al. 2021: AI explanations increase reliance
    → Busuioc 2021 (JPART): automation bias in public sector
    → Bansak & Hainmueller 2024 (ISQ): automation bias in national security
    → Schemmer et al. 2024: counterfactual explanations reduce overreliance

  AI + LEARNING:
    → Bastani et al. 2024 (Harvard/Wharton, PNAS): AI can harm learning (17% worse without AI)
      → Guardrailed tutor: 127% improvement with no exam penalty
    → Kestin & Miller 2025 (Harvard, Scientific Reports): AI tutoring doubled gains when guided
    → Fernandes et al. 2025: "AI Makes You Smarter But None the Wiser"
    → Dunning & Kruger 1999: metacognitive incompetence

  AI + DECISION MAKING:
    → Banerjee et al. 2024 (Stanford): selective AI > always-on > no AI
    → Henry et al. 2022/2024 (TREWS): human-AI sepsis detection, 18.7% mortality reduction
    → Fogliato et al. 2022: order matters (human first > AI first)

  NEUROSCIENCE FOUNDATION:
    → Damasio 1994, 1999: somatic markers
    → Craig 2002: interoceptive awareness
    → Gendlin 1981: Focusing method
    → Tang et al. 2015: mindfulness and interoception
    → von Holst 1950, Blakemore 1998: efference copy
```

---

## Closing note

**Bộ 3 song song:**
→ Social-Calibration.md v1.0 — WHERE WE CAME FROM (hệ thống xã hội đang vỡ)
→ AI-Self-Model.md v2.0 — WHY + HOW self-calibrate when using AI (FILE NÀY)
→ Human-AI-Future.md v3.0 — WHERE WE'RE GOING (3-risk framework, collective)

**AI-Self-Model v2.0** — MICRO-level analysis of human-AI interaction.

Thesis: AI amplifies whatever self-model you operate on.
Hiểu bản thân = prerequisite, không phải optional.
Body-feedback = quality controller (~90%) AI không có.
Domain reality = final arbiter.
Ngay cả AI trung thực cũng amplify — coherence ≠ truth.
Calibration có thể stale — feedback loop cần active.

5 failure domains. 6 diagnostic questions. 1 mechanism chung:
wrong model → AI confirm → body-feedback dismissed → domain crash delayed → bigger correction.

Reverse cũng đúng: right model × AI × body-listening × domain-verify = compound growth.

La bàn, không phải GPS.
AI = microscope (thấy xa, thấy rộng).
Body = la bàn nội tại (chỉ hướng đúng cho CÁ NHÂN).
Domain = mặt đất thật (la bàn cũng có thể lệch ~10%).
Cả ba cùng nhau = biết XA + biết HƯỚNG + biết THẬT.

> **v2.1 Changelog (2026-05-17):**
> ① Body-Base 4-tier → 2-Tier + 2-Pathway: v3.1 §7 aligned (8 refs updated)
> ② §6→§7 section refs: coherence ≠ truth, 3 failure modes, calibration — all moved to §7
> ③ Dep version: Body-Base v2.0 → v3.1
> ④ Tầng 2 Hebbian + pathway 2a/2b terminology integrated

> *AI-Self-Model v2.1 — "AI = amplifier, not corrector. Wrong model × AI = amplified wrong.
> Right model × AI = amplified growth. Even honest AI amplifies — coherence ≠ truth.
> Body = quality controller (~90%). Domain = final arbiter.
> Calibration can go stale — maintain your feedback loop.
> 5 domains: học tập (hiểu ≠ compile), nuôi con (ngoan ≠ internalized),
> relationship (technique ≠ connection), sức khỏe (plan ≠ per-body),
> công việc (output ≠ skill). 1 pattern: AI confirm → body dismissed → domain crash.
> Fix: AI = chunk provider. Body = quality controller. Domain = final arbiter.
> Keep your calibration fresh."*
