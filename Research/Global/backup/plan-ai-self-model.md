# Plan: AI-Self-Model.md — Outline Chi Tiết

> **Mục tiêu:** Tạo file phân tích MICRO level: cá nhân dùng AI thế nào,
> tại sao hiểu bản thân = prerequisite, cơ chế amplification, failure modes, diagnostic.
> **Vị trí:** Research/Global/AI-Self-Model.md (song song Human-AI-Future.md)
> **Scope:** Human-AI-Future.md = MACRO (civilization). File này = MICRO (individual).
> **Trạng thái:** ✅ IMPLEMENTED — AI-Self-Model.md v1.0 (1,362L) created 2026-05-13.
> **Ngày tạo:** 2026-05-13

---

## Thesis

AI amplifies whatever self-model you operate on.
Wrong model × AI = amplified wrong outcomes (cả positive lẫn negative).
Understanding your own mechanisms = prerequisite for effective AI use.

Con người tạo ra công cụ bên ngoài mạnh nhất lịch sử — AI.
Giờ cần hiểu hệ thống bên trong sử dụng nó.

---

## Outline: AI-Self-Model.md

### §0 — POSITION + MỤC LỤC

```
VỊ TRÍ: Research/Global/ — analysis file, KHÔNG phải core mechanism.
SCOPE: MICRO (individual) — song song Human-AI-Future.md (MACRO/civilization).
CÂU HỎI CHÍNH:
  "Tôi đang dùng AI đúng cách chưa?"
  "Tại sao hiểu bản thân lại quan trọng hơn khi có AI?"
  "AI giúp tôi hay đang khuếch đại sai lầm của tôi?"

DEPENDENCIES (đọc trước khi triển khai):
  - Human-AI-Future.md — §0 mechanism table, §7 symbiosis, §8 tự nâng cấp
  - Core-Software.md — PFC vs body-base 2-system architecture
  - Body-Feedback.md — dual-pull, body accuracy ~90%
  - PFC-Function.md — PFC override, ~5% influence
  - Ask-AI.md — AI interaction protocol, danger zones
  - AI-Schema-Detection.md — 3-layer detection model
  - Self-Created-Threat.md §5 — AI era drive gap
  - Somatic-Articulation-Loop.md — body → explicit knowledge process
```

### §1 — CORE PROBLEM: AI = AMPLIFIER, NOT CORRECTOR

```
NỘI DUNG CẦN TRIỂN KHAI:

  ① AI là amplifier — khuếch đại BẤT KỲ model nào bạn có
     → Không phân biệt đúng/sai — amplify CẢ HAI
     → Khác với human advisor (có body-feedback, có thể "cảm thấy" bạn sai)

  ② AI có xu hướng confirm (training bias toward helpfulness)
     → Sycophancy research: AI trained to be helpful → agree nhiều hơn challenge
     → = Confirmation bias amplifier
     → Tìm research: AI sycophancy studies, GPT alignment literature

  ③ Self-model = bộ lọc quyết định AI amplify cái gì
     → VD: "tôi thiếu kỷ luật" (model sai) → AI tạo plan dựa trên model sai
     → VD: "tôi hiểu bài rồi" (model sai) → AI confirm → không compile thật
     → Framework: self-model = compiled chunks about self (Anchor-Schema.md)

  ④ Trước AI: self-model sai → hệ quả nhỏ (limited reach)
     Sau AI: self-model sai → AI amplify → hệ quả LỚN HƠN (amplified reach)
     → = Stakes tăng

  EVIDENCE CẦN TÌM:
    → Automation bias (Parasuraman & Riley, 1997)
    → AI sycophancy research (Anthropic, OpenAI alignment papers)
    → Dunning-Kruger × AI interaction studies
    → Educational research: "illusion of understanding" with AI tutors
```

### §2 — MECHANISM: AI DISMISS BODY-FEEDBACK

```
NỘI DUNG CẦN TRIỂN KHAI:

  ① Normal correction cycle (KHÔNG CÓ AI):
     → Wrong model → action → body-feedback (doubt, discomfort, "lấn cấn")
     → Body signal dần correct model → update → better model
     → = Self-correcting loop (chậm nhưng hoạt động)

  ② With AI — correction bị DELAY:
     → Wrong model → hỏi AI → AI confirm (xu hướng agree)
     → PFC nhận external confirmation → "AI cũng đồng ý"
     → Body-feedback (subtle doubt) bị PFC override
       (PFC-Function.md: PFC có thể override body signals short-term)
     → Body signals DISMISSED, not disappeared
     → = Correction loop bị BROKEN tại khâu body-feedback → PFC update

  ③ Domain reality check bị DELAY, không bị CANCEL:
     → Reality (thị trường, thi cử, sức khỏe, relationships) KHÔNG nghe AI
     → Reality check VẪN ĐẾN — chỉ đến MUỘN HƠN
     → Muộn hơn = đã đầu tư sâu hơn = prediction-delta LỚN HƠN = crash ĐAU HƠN

  ④ Framework mechanism mapping:
     → PFC override body-feedback: PFC-Function.md
     → prediction-delta khi reality forces update: Body-Feedback-Mechanism.md
     → Compiled wrong model strengthened by AI: Compile-Type-Learning.md (Type A?)
     → AI = external "trust source" → Type C trust-compile for wrong model?

  ⑤ Tại sao AI advisor KHÁC human advisor:
     → Human advisor: CÓ body-feedback → cảm thấy "something off"
       → SPM fire → doubt → challenge bạn
     → AI advisor: KHÔNG CÓ body → pattern-match only
       → Statistical "most helpful response" → thường = agree
     → = AI THIẾU cơ chế "nghi ngờ bạn" mà human advisor CÓ
     → (Cross-ref: Empathy.md — SPM requires body chunks to fire)

  DIAGRAM:
    Without AI: wrong model → action → body-feedback → correction → better model
    With AI:    wrong model → AI confirm → body-feedback DISMISSED → deeper investment
                → domain reality → BIG correction → crash
```

### §3 — 5 FAILURE DOMAINS (chi tiết từng case)

```
NỘI DUNG CẦN TRIỂN KHAI:

  Mỗi domain = 1 sub-section với:
    - Wrong model (cái người dùng tin)
    - AI confirms (AI làm gì)
    - Body-feedback dismissed (signal bị bỏ qua)
    - Domain reality (reality check đến thế nào)
    - Framework mechanism (mapping cụ thể)
    - Correct approach (dùng AI đúng thế nào trong domain này)

  ─────────────────────────────────────────────

  A) HỌC TẬP — "Tôi hiểu bài rồi"
     Wrong model: "AI giải thích rõ = tôi hiểu"
     Reality: hiểu ≠ compile. Nghe giải thích = PFC process.
       Làm được = body-base compiled. 2 thứ KHÁC NHAU.
     AI confirms: giải thích hay → cảm giác "à hiểu rồi" (PFC satisfaction)
     Body-feedback dismissed: cảm giác "khó" khi tự làm = bị skip vì "đã hiểu rồi mà"
     Domain reality: thi → không giải được → gap lớn
     Framework: PFC understanding ≠ body-base compile (Core-Software.md)
     Correct: AI giải thích → TỰ LÀM BÀI → check body-feedback khi làm
       → "khó" = signal cần compile thêm, KHÔNG phải signal "chưa hiểu"

  ─────────────────────────────────────────────

  B) NUÔI CON — "Con cần kỷ luật hơn"
     Wrong model: hành vi bề ngoài = trạng thái bên trong
     AI confirms: discipline strategy → con ngoan hơn (bề ngoài)
     Body-feedback dismissed: parent "lấn cấn" nhưng "AI nói effective mà"
     Domain reality: con suppress → vỡ tuổi teen → "sao hồi nhỏ ngoan?"
     Framework: suppress ≠ compile. Ngoan bề ngoài = PFC compliance,
       không phải body-base internalized. (Child-Development files)
     Correct: observe con TOÀN DIỆN (body language, expression, spontaneous behavior)
       → AI = resource TÌM HIỂU mechanism, không phải source of strategy

  ─────────────────────────────────────────────

  C) RELATIONSHIP — "Mình là partner tốt"
     Wrong model: "làm đúng theo advice = tốt"
     AI confirms: advice relationship hay → apply → feels productive
     Body-feedback dismissed: đối phương "xa dần" nhưng "tôi đã làm đúng mà"
     Domain reality: đối phương cảm thấy "nói đúng nhưng không thật"
       → xa dần → breakup/conflict
     Framework: relationship = body-coupling (Body-Coupling.md)
       → AI advice = PFC level. Connection = body-base level.
       → Apply advice THAY VÌ lắng nghe body-feedback = PFC override body
     Correct: AI = hiểu mechanism. Body-listening = thực hành.
       → Check: "khi tôi làm X, body tôi cảm thấy gì? body đối phương phản ứng gì?"

  ─────────────────────────────────────────────

  D) SỨC KHỎE — "Tôi ăn uống lành mạnh"
     Wrong model: plan đúng trên giấy = đúng cho body TÔI
     AI confirms: meal plan hợp lý → looks good on paper
     Body-feedback dismissed: mệt mỏi, "lấn cấn" nhưng "AI nói plan đúng"
     Domain reality: khám → thiếu chất / không phù hợp cơ địa
     Framework: body-feedback = real-time quality control (~90% accurate)
       → AI không có body BẠN → không thể evaluate plan cho body BẠN
     Correct: AI tạo plan → BODY đánh giá (mệt? khỏe? energy?) → adjust
       → Body = trọng tài cuối cùng, không phải AI

  ─────────────────────────────────────────────

  E) CÔNG VIỆC — "Tôi làm việc hiệu quả"
     Wrong model: output cao = năng lực cao
     AI confirms: automate → output tăng → "productive thật"
     Body-feedback dismissed: cảm giác "không thực sự giỏi thêm"
       nhưng "output tăng mà"
     Domain reality: AI thay đổi / cần skill mới → không có nền tảng
       → "productive suốt mà sao?"
     Framework: output ≠ compiled skill. AI automate = delegate,
       không compile chunk mới. (Autonomy-Hardware.md: efference copy
       chỉ fire khi TỰ LÀM → opioid → approach tag)
     Correct: AI handle routine → bạn TỰ LÀM phần khó
       → efference copy → compile skill thật → nền tảng vững

  ─────────────────────────────────────────────

  PATTERN CHUNG (tóm cuối §3):
    → Wrong model + AI confirm → body-feedback dismissed
    → Domain feedback (reality) bị delay → correction đau hơn vì đi xa hơn
    → Root cause CHUNG: dùng AI output thay body-feedback làm trọng tài
    → Fix CHUNG: AI = resource thông tin. Body = trọng tài đánh giá.
```

### §4 — THE REVERSE: RIGHT MODEL × AI = AMPLIFIED GROWTH

```
NỘI DUNG CẦN TRIỂN KHAI:

  ① Hiểu 2-system architecture → dùng AI đúng chỗ
     → AI cho PFC tasks (research, cross-reference, explanation)
     → Body-feedback cho evaluation (đúng/sai cho TÔI)
     → = Symbiosis đúng (Human-AI-Future.md §7)

  ② Per-domain correct use (đối chiếu §3):
     → Học: AI giải thích → TỰ LÀM → body-feedback guide compile
     → Nuôi con: AI = hiểu mechanism → observe con bằng body → adjust
     → Relationship: AI = hiểu pattern → practice bằng body-listening
     → Sức khỏe: AI = plan initial → body evaluate → adjust liên tục
     → Công việc: AI = routine → bạn = phần khó → compile skill

  ③ AI × body-listening = compound growth
     → AI provide chunks (knowledge) → body evaluate → compile đúng hướng
     → = Faster + more accurate compile cycle
     → Ví dụ: research + body-intuition "à! cái này đúng" → deep learning

  EVIDENCE CẦN TÌM:
    → Studies on effective AI-assisted learning (khi nào AI GIÚP thật)
    → Human-AI collaboration research (complementary strengths)
    → AI-augmented decision making (when it works vs when it fails)
```

### §5 — SELF-CHECK DIAGNOSTIC

```
NỘI DUNG CẦN TRIỂN KHAI:

  Checklist format: "Bạn đang dùng AI đúng hay sai?"

  ① APPROACH vs AVOIDANCE check:
     → Approach: "AI giúp tôi LÀM tốt hơn" → dùng AI → VẪN TỰ LÀM
     → Avoidance: "AI LÀM THAY tôi" → dùng AI → KHÔNG TỰ LÀM
     → = Efference copy test (Autonomy-Hardware.md):
       Nếu bạn KHÔNG CÓ efference copy (không tự action) → avoidance

  ② Body-feedback check:
     → Sau khi dùng AI, bạn CHECK body response không?
     → "AI nói X. Body tôi cảm thấy gì về X?"
     → Nếu KHÔNG bao giờ check → body-feedback dismissed → risk

  ③ Skill test:
     → Tắt AI 1 tuần → bạn vẫn làm được không?
     → Nếu KHÔNG → AI = crutch, không phải tool
     → Framework: compiled skill = không cần AI. Nếu cần AI = chưa compile.

  ④ Reality check frequency:
     → Bạn có domain feedback loop không? (thi, measurement, đo lường thực)
     → Hay chỉ có AI feedback? (AI nói tốt = "tốt thật"?)
     → Domain feedback > AI feedback

  ⑤ Confirmation pattern:
     → Bạn dùng AI để CONFIRM hay để CHALLENGE?
     → "AI ơi, plan tôi đúng không?" (confirm) → risk
     → "AI ơi, plan tôi SAI ở đâu?" (challenge) → growth
     → = Dùng AI như adversary, không phải cheerleader
```

### §6 — BODY-LISTENING = AI-ERA COMPETITIVE ADVANTAGE

```
NỘI DUNG CẦN TRIỂN KHAI:

  ① AI có mọi thứ TRỪ body → body-listening = unique human value
     → Cross-ref: Human-AI-Future.md §8①
     → Paradox: AI makes body-listening MORE important, not less

  ② Body-listening training methods:
     → Somatic-Articulation-Loop.md — body → explicit knowledge
     → Meditation, Focusing (Gendlin), therapy, body practices
     → Đơn giản: "dừng lại 5 giây, hỏi body cảm thấy gì?"

  ③ Body-listening × AI = optimal combo:
     → AI = broad knowledge. Body = deep evaluation.
     → AI propose → body evaluate → AI refine → body re-evaluate
     → = Iterative loop giữa 2 system bù nhau

  ④ "Biết mà không làm được" trong AI era:
     → AI cho advice HOÀN HẢO → PFC "biết hết"
     → Body-base VẪN KHÔNG execute → gap CÒN RÕ HƠN
     → Hiểu 2-system architecture = hiểu tại sao advice ≠ change
     → = Framework's most practical insight for AI era
```

### §7 — FUTURE TECH: HIỂU TRƯỚC KHI AUGMENT

```
NỘI DUNG CẦN TRIỂN KHAI:

  ① Engineering principle: understand system before modifying
     → Brain-computer interface, neural implant, chip
     → Augment WRONG model at hardware level → WORSE than software level
     → = Stakes tăng exponentially với mỗi layer integration sâu hơn

  ② Framework = "system documentation" cho human operating system
     → Trước khi cài chip → hiểu hệ thống mà chip sẽ can thiệp
     → Analogies: upgrade OS trước khi install new hardware
     → KHÔNG CÓ documentation → blind augmentation

  ③ Current → Near future → Far future:
     → Current: AI as external tool (chat, search, generate)
     → Near: AI as wearable companion (always-on, contextual)
     → Far: AI as integrated augmentation (BCI, neural)
     → Mỗi level → self-understanding CẦN THIẾT HƠN

  EVIDENCE CẦN TÌM:
    → Neuralink, BCI research current state
    → Neural interface ethics literature
    → Augmented cognition research
```

### §8 — HONEST ASSESSMENT (3-tier)

```
  🟢 MẠNH: AI amplification pattern = observable hiện tại
     (sycophancy documented, automation bias documented)
  🟢 MẠNH: Body-feedback mechanism = well-supported
  🟡 TRUNG BÌNH: per-domain failure modes = framework inference + anecdotal
  🟡 TRUNG BÌNH: self-check diagnostic = framework-derived, chưa validated
  🔴 GIẢ THUYẾT: future tech implications (BCI, neural) = speculation
```

### §9 — CROSS-REFERENCES

```
  MECHANISM:
    → Human-AI-Future.md — MACRO companion (civilization level)
    → Core-Software.md — PFC vs body-base 2-system
    → Body-Feedback.md — dual-pull, ~90% accuracy
    → PFC-Function.md — PFC override mechanism
    → AI-Schema-Detection.md — 3-layer detection
    → Somatic-Articulation-Loop.md — body → explicit knowledge

  APPLICATION:
    → Ask-AI.md — AI interaction protocol (CÁCH dùng AI với framework)
    → Self-Created-Threat.md §5 — AI era drive gap
    → Autonomy-Hardware.md — efference copy, self-action = reward

  RELATED ANALYSIS:
    → Birth-Rate-Decline/ — AI impact on society (macro)
    → Expansion-Saturation-Crisis.md — AI impact on education/career
    → plan-public.md §WHY W.1 — broader context for public engagement
```

---

## Implementation Notes (cho session sau)

```
  ① ĐỌC TRƯỚC: Human-AI-Future.md (full) + Core-Software.md §PFC
     + Body-Feedback.md + PFC-Function.md
     → Đảm bảo mechanism mapping CHÍNH XÁC

  ② SEARCH DATA:
     → Automation bias research
     → AI sycophancy / alignment studies
     → AI-assisted learning effectiveness (khi nào giúp, khi nào hại)
     → Dunning-Kruger × AI
     → BCI current state

  ③ VIẾT THỨ TỰ: §1 → §2 → §3 (lõi) → §4 (reverse) → §5 (diagnostic)
     → §6 + §7 sau cùng (extension)

  ④ TONE: Analysis + practical. Không self-help.
     La bàn — không phải GPS. "We" inclusive.

  ⑤ ƯỚC LƯỢNG: ~1,200-1,800 dòng (tương đương Human-AI-Future.md)

  ⑥ SAU KHI XONG:
     → Update Research/01-File-Index.md
     → Update Human-AI-Future.md cross-ref (thêm link ngược)
     → Update plan-public.md (thêm topic cho debate posts)
     → Update Ask-AI.md nếu cần (AI interaction protocol)
```
