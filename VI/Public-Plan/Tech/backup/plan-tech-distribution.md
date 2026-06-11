# Plan: Tech Expert Distribution — Phân Phối Framework Tới Chuyên Gia Công Nghệ

> **Mục tiêu:** Đưa framework tới nhóm tech expert quan tâm neuro/psych — nhóm DUY NHẤT có khả năng verify cross-domain toàn bộ.
> **Nguyên tắc:** Stress-test deployment, không phải marketing. Framework sống hay chết bằng evidence, không bằng quảng bá.
> **Logic cốt lõi:** Nếu tech verify → propagation TỰ NHIÊN. Nếu tech reject → không propagation = framework cần sửa. CẢ HAI = outcome tốt.
> **Trạng thái:** DRAFT v0.1
> **Ngày tạo:** 2026-05-25
> **Bổ sung cho:** plan-public.md (plan gốc, general strategy)

---

## §0 — TẠI SAO TECH EXPERT LÊN ĐẦU TIÊN

### 0.1 — Vấn Đề Silo Của Domain Expert

```
Framework = CROSS-DOMAIN (~170 files, ~300,000 dòng)
  ├── Neuroscience: dopamine, cortisol, opioid, VTA, PFC, amygdala
  ├── Psychology: behavior, empathy, motivation, 2-system architecture
  ├── Education: compile types, direction > level, per-age development
  ├── AI: amplification, schema detection, human-AI future
  └── Philosophy: epistemological position, falsifiability

DOMAIN EXPERT BỊ SILO:
  Neuroscientist → verify ~20-30% (biological claims) → phần còn lại = "ngoài domain tôi"
  Psychologist   → verify ~20-30% (behavioral claims) → phần còn lại = "tôi không rõ"
  Educator       → verify ~15% (learning claims) → phần còn lại = "quá technical"
  Philosopher    → verify ~10% (logic, falsifiability) → phần còn lại = "cần data"

  → KHÔNG AI verify được >50% framework bằng chuyên môn riêng.
  → Framework TOÀN BỘ = cấu trúc cross-domain → cần người ĐỌC TOÀN BỘ.

TECH EXPERT + AI:
  → Đọc TOÀN BỘ (quen đọc documentation lớn, architecture diagrams)
  → Claim neuro → hỏi AI + check citation → flag nếu không khớp
  → Claim psych → hỏi AI + cross-ref evidence → flag nếu mâu thuẫn
  → Cross-domain logic → TỰ kiểm tra consistency
  → KẾT QUẢ: verify ~60-70% (logic + citation-check + cross-domain coherence)
  → Phần 30% còn lại = empirical depth → ROUTE tới domain expert cụ thể
```

### 0.2 — 6 Lý Do Tech Expert = Nhóm Mạnh Nhất

```
① ĐỌC CROSS-DOMAIN:
  → Quen đọc system architecture, multi-component systems
  → Framework dùng ngôn ngữ architecture: "compile", "chunk", "cycle",
    "pipeline", "body-base", "prediction-delta"
  → = ĐỌC TỰ NHIÊN hơn bất kỳ nhóm chuyên gia nào khác

② DÙNG AI STRESS-TEST:
  → Feed claim vào AI → "Evidence nào ủng hộ? Phản bác?"
  → Cross-reference citation → "Paper này có nói đúng điều framework claim?"
  → Tìm edge cases → "Nếu mechanism X đúng thì case Y phải đúng — Y có đúng?"
  → = Verification NHANH và BAO QUÁT hơn đọc thủ công

③ TRIAGE AGENT:
  → Tech đọc toàn bộ → extract claim cụ thể
  → Route: "r/neuroscience, cụ thể claim này về VTA — có đúng không?"
  → Domain expert nhận CÂU HỎI CỤ THỂ thay vì đọc 300,000 dòng
  → = Hiệu quả hơn tác giả tự post từng community

④ BUILD VERIFICATION INFRASTRUCTURE:
  → Knowledge graph / visualization
  → Cross-reference checker (claim A ở file X ↔ claim B ở file Y)
  → Citation validator
  → Prediction generator → danh sách testable predictions
  → = Công cụ mà CHỈ tech mới tạo được

⑤ ĐÔNG ĐẢO + CÓ REACH:
  → HN ~500K daily, r/programming ~7M, r/MachineLearning ~3.5M
  → Tech bloggers, newsletter writers, podcasters
  → Nếu verify → propagation nhanh + có chất lượng
  → Nếu reject → cũng nhanh → tiết kiệm thời gian

⑥ AI ERA = PAIN POINT TRỰC TIẾP:
  → Framework nói về AI amplify model sai → đúng vấn đề họ ĐANG SỐNG
  → "Why knowing ≠ doing" → mọi programmer đều trải nghiệm
  → "Compile" architecture → ngôn ngữ CỦA HỌ
  → = Engagement TỰ NHIÊN, không cần convince "tại sao quan trọng"
```

### 0.3 — Logic Tự Nhiên: Verify → Propagate, Reject → Stop

```
  ┌──────────────────────────────────────────────────────────────┐
  │ FRAMEWORK ĐÚNG (phần lớn):                                   │
  │   → Tech verify logic + cross-ref → "coherent, citations hold"│
  │   → Tech route claims → domain expert confirm → confidence ↑  │
  │   → Tech TỰ viết blog/tweet/video → propagation TỰ NHIÊN    │
  │   → = Không cần tác giả push — evidence push                  │
  ├──────────────────────────────────────────────────────────────┤
  │ FRAMEWORK SAI (phần lớn):                                     │
  │   → Tech tìm contradictions → "claim X mâu thuẫn với data Y" │
  │   → Post phân tích → cộng đồng đồng ý → KHÔNG propagation   │
  │   → Tác giả biết SAI Ở ĐÂU → sửa hoặc rút                  │
  │   → = TỐT. Biết sai sớm = tiết kiệm thời gian mọi người    │
  ├──────────────────────────────────────────────────────────────┤
  │ FRAMEWORK ĐÚNG MỘT PHẦN:                                     │
  │   → Tech verify phần A → "đúng" → propagate phần A           │
  │   → Tech reject phần B → "sai" → KHÔNG propagate phần B      │
  │   → = Outcome CHÍNH XÁC NHẤT. Tốt hơn "all or nothing."     │
  └──────────────────────────────────────────────────────────────┘

  KEY INSIGHT:
    → Tác giả KHÔNG CẦN convince. Chỉ cần EXPOSE.
    → Framework tự sống hoặc tự chết bằng evidence.
    → Đây KHÔNG phải marketing plan. Đây là stress-test deployment.
    → Mọi outcome (verify/reject/partial) = đều có giá trị.
```

---

## §1 — AUDIENCE MAP: AI TRONG TỆP TECH QUAN TÂM NEURO/PSYCH?

### 1.1 — 5 Subtypes (từ gần → xa)

```
  ┌──────────────────────────────────────────────────────────────────┐
  │ SUBTYPE             │ ĐẶC ĐIỂM                │ ƯU TIÊN        │
  ├──────────────────────────────────────────────────────────────────┤
  │ ① Rationalist       │ LessWrong, SSC, EA       │ ⭐⭐⭐ CAO NHẤT │
  │   (đã quan tâm      │ Đã đọc cog-sci,          │ Đọc sâu,       │
  │    cognitive         │ Bayesian, predictive      │ cross-domain,   │
  │    science)          │ processing. Quen          │ stress-test     │
  │                      │ unified models.           │ KỸ NHẤT        │
  ├──────────────────────────────────────────────────────────────────┤
  │ ② AI/ML Engineer    │ Prediction error =        │ ⭐⭐⭐ CAO NHẤT │
  │   (hiểu             │ core of their work.       │ Hiểu PE,        │
  │    prediction        │ "Human brain vs AI"       │ body-first =    │
  │    error)            │ = topic họ quan tâm.      │ insight MỚI     │
  ├──────────────────────────────────────────────────────────────────┤
  │ ③ Quantified Self   │ Self-tracking, biometrics, │ ⭐⭐ CAO       │
  │   / Biohacker       │ body data. Body-first     │ Body-feedback   │
  │                      │ architecture = ĐÚNG       │ = ngôn ngữ     │
  │                      │ trải nghiệm CỦA HỌ.     │ CỦA HỌ        │
  ├──────────────────────────────────────────────────────────────────┤
  │ ④ Software          │ "Compile", "cache",       │ ⭐⭐ CAO       │
  │   Engineer           │ "pipeline" = ngôn ngữ    │ Analogy tự     │
  │   (general)          │ hàng ngày. Architecture   │ nhiên, dễ      │
  │                      │ thinking tự nhiên.        │ engage          │
  ├──────────────────────────────────────────────────────────────────┤
  │ ⑤ Neurotech /       │ BCI, neural interface.    │ ⭐ TB          │
  │   BCI Community      │ "Hiểu hệ thống TRƯỚC    │ Nhỏ nhưng      │
  │                      │ KHI can thiệp" = trực    │ chất lượng     │
  │                      │ tiếp relevant.            │ rất cao        │
  └──────────────────────────────────────────────────────────────────┘
```

### 1.2 — Audience KHÔNG Target (dù là tech)

```
  ✗ Productivity / self-help tech community
    → Risk: take framework → làm app "dopamine tracker" → SAI mechanism → damage
  ✗ Startup/growth hacker community
    → Risk: dùng framework → "exploit body-reward" → ĐẢO NGƯỢC mục đích
  ✗ Mass programmer community (r/programming general)
    → Risk: đọc title → không đọc sâu → oversimplify → "dopamine tip" level
  ✗ "Tech bro" self-optimization
    → Risk: "biohack dopamine" → đúng cái mà framework PHẢN BÁC
```

---

## §2 — TOPIC STRATEGY: 6 Entry Points, 1 Convergence

> **Nguyên tắc:** Mỗi topic = 1 CỬA VÀO framework từ 1 góc.
> Tất cả cửa dẫn tới CÙNG 1 TÒA NHÀ (GitHub repo).
> Người đến từ cửa nào cũng gặp nhau BÊN TRONG.

### Overview: 6 Topics

```
  ┌────────────────────────────────────────────────────────────────────┐
  │  #  │ TOPIC                          │ HOOK CHO TECH              │
  ├────────────────────────────────────────────────────────────────────┤
  │  T1 │ Dopamine ≠ Reward              │ "Mô hình bạn biết là sai" │
  │  T2 │ Human OS: 2-System Architecture│ "Hệ điều hành cơ thể"     │
  │  T3 │ Compile Pipeline               │ "Cách brain compile code"  │
  │  T4 │ AI Amplifies Wrong Models      │ "AI × self-model = danger" │
  │  T5 │ Prediction Error Is Not Enough  │ "PE thiếu gì cho humans?" │
  │  T6 │ The Full Architecture          │ "170 files, unified model" │
  └────────────────────────────────────────────────────────────────────┘

  THỨ TỰ POST:
    T1 hoặc T2 TRƯỚC (hook mạnh nhất, self-contained nhất)
    → T3, T4, T5 (bổ sung, tạo depth)
    → T6 (overview, CHỈ KHI T1-T5 đã có traction)

  MỖI TOPIC = 1 FILE DRAFT riêng tại Public-Plan/tech-posts/
```

### T1 — Dopamine ≠ Reward: "Mô Hình Bạn Đang Dùng Là Sai"

```
CORE CLAIM:
  Dopamine = salience alert ("something relevant changed")
  Reward = opioid system + 5 preconditions
  Dopamine tracks CHANGE, not pleasure.

TẠI SAO TECH AUDIENCE CARE:
  → AI recommendation systems optimize cho dopamine-like signals
  → Nếu dopamine ≠ reward → đang optimize SAI metric
  → "Your engagement metric measures attention capture, not user satisfaction"
  → = Trực tiếp relevant cho ML engineers building recommendation systems

EVIDENCE (self-contained):
  → L-DOPA: tăng dopamine, KHÔNG tăng mood (Liggins 2012)
  → Optogenetics: bật VTA → wanting UP, liking UNCHANGED (Berridge lab)
  → Nicotine: chặn opioid → mất reward DÙ dopamine còn fire (Bhatt 2010)
  → Parkinson's agonist: 6-7% gambling compulsive, KHÔNG pleasure từ thuốc

FALSIFICATION TEST:
  → "Nếu bạn có thể chỉ ra 1 'pure dopamine' drug tạo pleasure
     mà KHÔNG kích hoạt opioid system → framework sai ở đây."
  → "Nếu TikTok random algo vẫn cuốn bằng targeted algo → dopamine alone đủ."

SOURCE: Clarification/Dopamine-Is-Not-Reward.md + 01-Dopamine-Not-Reward.md (draft có sẵn)

PLATFORMS:
  → HN, LessWrong, r/slatestarcodex, r/MachineLearning, r/cogsci
  → Medium (Towards Data Science hoặc The Spike)
```

### T2 — Human OS: 2-System Architecture

```
CORE CLAIM:
  Body-base (compiled behavior) = ~95% driver.
  PFC (conscious thinking) = ~5% influence, mostly OBSERVER.
  "Knowing ≠ doing" = 2 SEPARATE systems, not willpower failure.

TẠI SAO TECH AUDIENCE CARE:
  → Mọi programmer biết: "tôi BIẾT phải refactor, nhưng vẫn copy-paste"
  → Mọi dev biết: "tôi BIẾT nên test, nhưng vẫn ship without tests"
  → Framework giải thích: PFC (biết) ≠ body-base (làm). 2 systems KHÁC NHAU.
  → "Your conscious mind is a monitoring process, not the main thread."

EVIDENCE:
  → Libet 1983: brain activity ~500ms TRƯỚC conscious decision
  → Kornhuber & Deecke 1965: Bereitschaftspotential (readiness potential)
  → Soon et al. 2008: fMRI predict decision 7-10s TRƯỚC subject aware
  → Damasio somatic marker: body evaluates TRƯỚC PFC
  → Dual process theory (Kahneman): System 1/2 nhưng framework đi sâu hơn

TECH ANALOGY:
  → Body-base = compiled binary (fast, no source visible, hard to change)
  → PFC = debugger/profiler (can OBSERVE, limited ability to CHANGE)
  → "Knowing" = debugger sees the bug
  → "Doing" = recompiling the binary (requires specific conditions, not just seeing)
  → = Tại sao reading about productivity ≠ being productive

FALSIFICATION TEST:
  → "Show a case where PFC alone (pure conscious decision, no body involvement)
     produces sustained behavior change without body-base recompilation."
  → "If willpower is unlimited → meditation practitioners should never relapse.
     But 90%+ do within first year. Why?"

SOURCE: Core-Software.md, PFC/PFC-Operations.md, Ask-AI.md §3

PLATFORMS:
  → HN, r/slatestarcodex, r/programming, LessWrong
  → Medium (Better Programming, Towards Data Science)
```

### T3 — Compile Pipeline: Cách Brain "Compile" Kinh Nghiệm

```
CORE CLAIM:
  Kinh nghiệm = "chunks" → compile thành body-level patterns.
  3 compile types:
    Type A (Experience Compile): tự trải nghiệm → compile MẠNH, khó break
    Type B (Expertise Compile): lặp lại + feedback → compile CHÍNH XÁC
    Type C (Trust Compile): nghe + tin → compile NHANH, dễ sai, dễ sụp

TẠI SAO TECH AUDIENCE CARE:
  → "Type C = Stack Overflow copy-paste. Works until edge case."
  → "Type B = deliberate practice. Slow but solid."
  → "Type A = burned by production incident. Never forget."
  → = Giải thích tại sao junior dev đọc docs nhưng không debug được
  → = Giải thích tại sao "10 years experience" ≠ "10 years of learning"

TECH ANALOGY:
  → Type A = learned from segfault → compiled into muscle memory
  → Type B = code review + iteration → compiled into design intuition
  → Type C = read tutorial → fragile knowledge, breaks under pressure
  → Decompile = unlearning (expensive, requires specific conditions)
  → = Tại sao "just read the docs" KHÔNG WORK cho complex systems

EVIDENCE:
  → Procedural vs declarative memory (Squire 1992)
  → Expertise research (Ericsson 1993): deliberate practice ≠ repetition
  → Fear conditioning: 1 event → lifelong avoidance (amygdala compile)
  → Cognitive load theory (Sweller 1988): why reading ≠ understanding

FALSIFICATION TEST:
  → "If all compile types are equal → reading a textbook should produce
     same skill level as 1000 hours of practice. It doesn't."
  → "If Trust Compile is as durable as Experience Compile → learned beliefs
     should never change when authority changes. But they do (cults, ideologies)."

SOURCE: Body-Base/Chunk.md, Compile-Taxonomy.md

PLATFORMS:
  → HN, r/programming, r/ExperiencedDevs, r/slatestarcodex, LessWrong
  → Medium (Better Programming)
```

### T4 — AI Amplifies Your Wrong Self-Model

```
CORE CLAIM:
  AI = amplifier. Amplifies WHATEVER model you have about yourself.
  Wrong model + AI confirm → body-feedback (your gut feeling) gets dismissed
  → domain feedback (reality) gets DELAYED → correction is LARGER and more painful.

TẠI SAO TECH AUDIENCE CARE:
  → Họ DÙNG AI hàng ngày. Đây là TRẢI NGHIỆM CỦA HỌ.
  → "Ever asked ChatGPT to validate your architecture decision
     and felt great — until production broke?"
  → = AI confirmed your model → you ignored warning signs → reality hit harder
  → Brain-computer interfaces, neural implants coming →
     "Understand the system BEFORE augmenting it"

REAL-WORLD CASES (all tech-relevant):
  → Coding: "AI says my code is correct" → skip testing → bug in production
  → Career: "AI confirms my career plan" → ignore gut feeling "something's off"
     → 2 years later: skills obsolete
  → Learning: "AI explains clearly, I understand" → don't practice →
     can't solve problems independently
  → Architecture: "AI validates my design" → skip peer review →
     scalability issues at 10x load

FRAMEWORK MECHANISM:
  → Body-feedback = quality controller (gut feeling: "something's off")
  → Domain feedback = final arbiter (reality: "it broke")
  → AI sits BETWEEN body-feedback and domain feedback
  → Wrong model + AI → body-feedback dismissed → domain feedback DELAYED
  → = Correction is MORE PAINFUL because you went FURTHER in wrong direction

FALSIFICATION TEST:
  → "If AI doesn't amplify wrong models → AI-assisted decisions should have
     LOWER error rates than solo decisions. But automation bias research
     (Parasuraman & Riley 1997) shows INCREASED errors in some conditions."
  → "If this mechanism is wrong → 'AI-validated' code should have fewer bugs
     than peer-reviewed code. Test it."

SOURCE: Research/Global/AI-Self-Model.md, Ask-AI.md §6.1

PLATFORMS:
  → HN (STRONGEST fit — directly about AI), r/MachineLearning, r/artificial
  → r/slatestarcodex, LessWrong/Alignment Forum
  → Twitter/X AI accounts
```

### T5 — Prediction Error Is Necessary But Insufficient

```
CORE CLAIM:
  Prediction error (PE) = fundamental mechanism (Schultz 1997).
  Framework ENDORSES PE.
  BUT: PE alone = attention shift. NOT reward.
  Human reward requires PE + body-base evaluation + 5 preconditions (H10).

TẠI SAO TECH AUDIENCE CARE:
  → ML engineers KNOW prediction error (it's core of reinforcement learning)
  → "In RL, prediction error drives learning. In humans, it's necessary but
     not sufficient. Here's what else is needed."
  → = Bridge BETWEEN their expertise AND human mechanism
  → = "Your RL model is missing 5 modules"

EVIDENCE:
  → Schultz 1997: PE = dopamine signal for "something changed"
  → Framework adds: PE fires for NEGATIVE changes too (not just reward)
  → Berridge: wanting (PE-driven) ≠ liking (body-evaluation-driven)
  → H10: 5 preconditions for reward — same stimulus, different body-state,
     different outcome → PE alone CANNOT explain this

TECH ANALOGY:
  → PE = interrupt signal in CPU → "something needs attention"
  → But interrupt ≠ "good thing happened"
  → CPU still needs to EVALUATE what triggered the interrupt
  → Body-base evaluation = the evaluation subroutine PE triggers
  → = "You've been modeling human reward with just the interrupt handler"

FALSIFICATION TEST:
  → "If PE alone is sufficient for reward → every surprising stimulus
     should be rewarding. But unexpected loud noise = PE + aversion.
     PE fires, reward does NOT."
  → "If PE alone drives learning → all prediction errors should produce
     equal learning. But fear conditioning (1 trial) vs skill acquisition
     (1000+ trials) = same PE, wildly different compile rates."

SOURCE: Clarification/Prediction-Error-Is-Not-Reward.md

PLATFORMS:
  → r/MachineLearning, r/reinforcementlearning, LessWrong
  → HN (for RL/AI audience)
  → Medium (Towards Data Science, Towards AI)
```

### T6 — The Full Architecture: "170 Files, 1 Unified Model"

```
CORE CLAIM:
  Framework connects ~300,000 lines of analysis into 1 consistent
  body-first architecture. Covers: neuroscience, psychology, behavior,
  education, AI, love, addiction, OCD, religion, climate cognition.
  CC0 license. Inviting falsification.

TẠI SAO TECH AUDIENCE CARE:
  → "Someone wrote 170+ files of system documentation for the human body-brain"
  → = Quen đọc large codebases, architecture docs
  → Challenge: "Is this architecture internally consistent?"
  → = THÁCH THỨC tech audience stress-test

KHI NÀO POST T6:
  → CHỈ SAU KHI T1-T5 đã có traction
  → T6 = "If individual claims interested you, here's the full picture"
  → T6 KHÔNG phải entry point — T6 là DESTINATION

FORMAT:
  → Architectural overview (2-3 diagrams)
  → File map + reading order
  → "Here are 20 positions where this diverges from mainstream"
  → "Here's how to stress-test it with AI"
  → Link: GitHub repo

SOURCE: README.md, Core-Software.md, Core-Hardware.md

PLATFORMS:
  → HN (essay-style post), r/slatestarcodex (long-form), LessWrong
```

---

## §3 — PLATFORM MAP: Ở Đâu, Post Gì, Cách Nào

### 3.1 — Platform Priority Matrix

```
  ╔═══════════════════════════════════════════════════════════════════╗
  ║ TIER S — POST ĐẦU TIÊN (nhỏ, chất lượng cao, stress-test kỹ)  ║
  ╠═══════════════════════════════════════════════════════════════════╣
  ║                                                                   ║
  ║ ① LessWrong / Alignment Forum                                    ║
  ║   Size: ~50K active                                               ║
  ║   Audience: rationalist, Bayesian, cognitive science, AI safety   ║
  ║   Quen: unified models, predictive processing, embodied cognition ║
  ║   Fit: T1-T6 TẤT CẢ — audience đọc sâu nhất, challenge KỸ nhất  ║
  ║   Format: long-form essay (3000-8000 words ok)                    ║
  ║   Risk: thấp (nhỏ, không viral quá nhanh)                        ║
  ║   Tại sao ĐẦU TIÊN: stress-test TỐT NHẤT trước khi mở rộng      ║
  ║                                                                   ║
  ║ ② r/slatestarcodex (~129K)                                       ║
  ║   Audience: intellectual long-form, cross-domain thinking         ║
  ║   Fit: T1, T2, T4, T6                                            ║
  ║   Format: long-form (2000-5000 words)                             ║
  ║   Risk: thấp-trung (có thể reach HN nếu cross-post)              ║
  ║                                                                   ║
  ╠═══════════════════════════════════════════════════════════════════╣
  ║ TIER A — POST SAU KHI TIER S ĐÃ STRESS-TEST (vừa, reach tốt)  ║
  ╠═══════════════════════════════════════════════════════════════════╣
  ║                                                                   ║
  ║ ③ Hacker News (~500K daily)                                       ║
  ║   Audience: tech-intellectual, engineering mindset                 ║
  ║   Fit: T1, T2, T4 (single essay-style link)                      ║
  ║   Format: link tới blog post / Medium article                     ║
  ║   Risk: TRUNG (có thể frontpage → 300K views → kiểm soát khó)    ║
  ║   ⚠️ Post SAU KHI Tier S đã refine content                       ║
  ║   ⚠️ KHÔNG "Show HN" (đó là cho products)                        ║
  ║                                                                   ║
  ║ ④ r/MachineLearning (~3.5M)                                      ║
  ║   Audience: ML/AI engineers, researchers                          ║
  ║   Fit: T5 (PE reframe), T4 (AI amplify), T1 (dopamine = RL link) ║
  ║   Format: [D] Discussion tag, academic but accessible             ║
  ║   Risk: trung (audience kỹ tính, nhưng lớn)                      ║
  ║                                                                   ║
  ║ ⑤ r/cogsci (~129K)                                               ║
  ║   Audience: cognitive science (CROSS-OVER tech + neuro + psych)   ║
  ║   Fit: T1, T2, T5 — BRIDGE platform giữa tech và domain expert   ║
  ║   Format: academic tone, cite studies                              ║
  ║   Risk: thấp (nhỏ, academic)                                     ║
  ║   Giá trị: NẾU cogsci engage → domain experts thấy → credibility ║
  ║                                                                   ║
  ╠═══════════════════════════════════════════════════════════════════╣
  ║ TIER B — MỞ RỘNG (lớn, diverse, sau khi có traction)            ║
  ╠═══════════════════════════════════════════════════════════════════╣
  ║                                                                   ║
  ║ ⑥ r/QuantifiedSelf                                               ║
  ║   Fit: T2, T3 (body-feedback, self-tracking)                      ║
  ║                                                                   ║
  ║ ⑦ r/artificial (~1.3M)                                           ║
  ║   Fit: T4, T5 (AI × human)                                       ║
  ║                                                                   ║
  ║ ⑧ r/neuroscience (~500K+)                                        ║
  ║   Fit: T1, T5 (domain expert verification — ROUTE từ tech)       ║
  ║   ⚠️ Post CÂU HỎI CỤ THỂ, không phải full framework             ║
  ║                                                                   ║
  ║ ⑨ Twitter/X                                                       ║
  ║   Format: thread 5-10 tweets, link tới full post                  ║
  ║   Target: #NeuroTwitter, #AIethics, #CogSci                      ║
  ║   ⚠️ Build presence trước (§3.3)                                  ║
  ║                                                                   ║
  ║ ⑩ Medium — curated publications                                   ║
  ║   → Towards Data Science (T5, T4)                                 ║
  ║   → The Spike (T1)                                                ║
  ║   → Better Programming (T2, T3)                                   ║
  ║   ⚠️ Submit vào publication, KHÔNG self-publish                   ║
  ║                                                                   ║
  ║ ⑪ Dev.to                                                          ║
  ║   Fit: T2, T3 (programming analogies)                             ║
  ║   Format: accessible, shorter                                     ║
  ║                                                                   ║
  ║ ⑫ LinkedIn                                                        ║
  ║   Fit: T4 (AI amplify — professional relevance)                   ║
  ║   Format: short post + link                                       ║
  ║                                                                   ║
  ╚═══════════════════════════════════════════════════════════════════╝
```

### 3.2 — Topic × Platform Matrix

```
  ┌──────────┬──────────┬──────────┬──────────┬──────────┬──────────┐
  │          │ T1       │ T2       │ T3       │ T4       │ T5       │
  │          │ Dopamine │ Human OS │ Compile  │ AI×Model │ PE       │
  ├──────────┼──────────┼──────────┼──────────┼──────────┼──────────┤
  │ LessWrong│ ⭐⭐⭐  │ ⭐⭐⭐  │ ⭐⭐    │ ⭐⭐⭐  │ ⭐⭐⭐  │
  │ SSC      │ ⭐⭐⭐  │ ⭐⭐⭐  │ ⭐⭐    │ ⭐⭐⭐  │ ⭐⭐    │
  │ HN       │ ⭐⭐⭐  │ ⭐⭐⭐  │ ⭐⭐    │ ⭐⭐⭐  │ ⭐⭐    │
  │ r/ML     │ ⭐       │ ⭐       │ ⭐       │ ⭐⭐⭐  │ ⭐⭐⭐  │
  │ r/cogsci │ ⭐⭐⭐  │ ⭐⭐⭐  │ ⭐⭐    │ ⭐⭐    │ ⭐⭐⭐  │
  │ QS       │ ⭐       │ ⭐⭐⭐  │ ⭐⭐    │ ⭐       │ ⭐       │
  │ Medium   │ ⭐⭐⭐  │ ⭐⭐    │ ⭐⭐⭐  │ ⭐⭐⭐  │ ⭐⭐    │
  │ Dev.to   │ ⭐       │ ⭐⭐⭐  │ ⭐⭐⭐  │ ⭐⭐    │ ⭐       │
  │ LinkedIn │ ⭐       │ ⭐⭐    │ ⭐       │ ⭐⭐⭐  │ ⭐       │
  │ Twitter  │ ⭐⭐    │ ⭐⭐    │ ⭐       │ ⭐⭐⭐  │ ⭐⭐    │
  └──────────┴──────────┴──────────┴──────────┴──────────┴──────────┘

  ĐỌC: ⭐⭐⭐ = perfect fit, ⭐⭐ = good fit, ⭐ = post được nhưng không optimal
```

### 3.3 — Platform-Specific Rules

```
LESSWRONG:
  → Tag: [Epistemic status: hypothesis, inviting falsification]
  → Dùng LaTeX nếu cần
  → Crosspost tới Alignment Forum nếu AI-relevant
  → Community expectation: acknowledge uncertainty, steelman counterarguments
  → ⚠️ Nếu viết bad epistemics → bị downvote NHANH → mất credibility

HACKER NEWS:
  → Submit LINK (tới blog post / Medium), không text post
  → Title: factual, không clickbait (HN sẽ edit clickbait title)
  → Respond comments NHANH trong 2h đầu (HN algorithm boost)
  → ⚠️ KHÔNG post weekend (traffic thấp)
  → ⚠️ KHÔNG post multiple links trong 1 tuần (spam flag)

r/MACHINELEARNING:
  → Tag: [D] Discussion
  → Dùng technical language (PE, reward signal, RL terminology)
  → Connect tới existing ML concepts (reward shaping, curiosity-driven exploration)
  → ⚠️ Low-effort posts bị delete — cần substantial content

TWITTER/X:
  → Build presence 2-4 tuần TRƯỚC khi share framework
  → Step 1: Follow neuro/AI researchers
  → Step 2: Reply có giá trị (không "great post!", mà thêm insight)
  → Step 3: Share 1 insight (T1 hoặc T4) → gauge
  → Step 4: Thread + link tới full post
  → ⚠️ Cold posting = 0 engagement. PHẢI build presence trước.

MEDIUM:
  → SUBMIT vào curated publication, KHÔNG self-publish
  → Nếu bị reject → refine + try publication khác
  → Self-publish = mất curation filter = audience không pre-selected
```

---

## §4 — CONVERGENCE ARCHITECTURE: Mọi Con Đường Dẫn Tới GitHub

### 4.1 — Hub-and-Spoke Model

```
                    ┌─────────────┐
         ┌─────────│   GITHUB    │──────────┐
         │         │   (HUB)     │          │
         │         └──────┬──────┘          │
         │                │                 │
    ┌────┴─────┐   ┌──────┴──────┐   ┌─────┴────┐
    │ LessWrong│   │ Hacker News │   │ r/ML     │
    │ (T1,T2)  │   │ (T1,T4)    │   │ (T4,T5)  │
    └──────────┘   └─────────────┘   └──────────┘
         │                │                 │
    ┌────┴─────┐   ┌──────┴──────┐   ┌─────┴────┐
    │ SSC      │   │ Medium      │   │ Twitter  │
    │ (T2,T6)  │   │ (T1,T3)    │   │ (T4)     │
    └──────────┘   └─────────────┘   └──────────┘

  MỌI POST ĐỀU KẾT THÚC VỚI:
    "Full framework (170+ files, CC0, inviting falsification):
     [GitHub link]"
    "Discussion hub: [GitHub Discussions link]"
    "What would falsify this? We want to know."
```

### 4.2 — Tại Sao GitHub Là Hub (Không Phải Discord/Forum Riêng)

```
① TECH AUDIENCE Ở ĐÓ SẴN:
  → Mọi dev có GitHub account
  → Không cần sign up platform mới → friction = 0
  → GitHub Discussions = forum built-in, free

② TRANSPARENT:
  → Mọi file visible, mọi thay đổi có history
  → Stars = proxy cho interest (visible social proof)
  → Issues = public record of challenges + responses
  → = KHÔNG giấu gì → trust

③ FORKABLE:
  → Ai muốn modify → fork → experiment
  → AI muốn verify → clone → chạy analysis
  → = Framework SỐNG bằng community, không phải tác giả

④ PERSISTENT:
  → Reddit post → chìm sau 48h
  → HN post → chìm sau 24h
  → GitHub repo → CÒN MÃI → mọi link trỏ tới ĐÂY
  → = Central reference point lâu dài

⑤ DOMAIN EXPERT CÓ THỂ TÌM:
  → Tech route claim cụ thể → domain expert mở GitHub → ĐỌC CỤ THỂ
  → Không cần đọc toàn bộ → chỉ đọc file được chỉ định
  → Issues tagged [needs-neuro-review] → domain expert biết đọc gì
```

### 4.3 — GitHub Setup TRƯỚC KHI Post

```
TRƯỚC KHI POST BẤT KỲ ĐÂU, setup GitHub:

① ENABLE DISCUSSIONS:
  Categories:
    → 📢 Announcements (tác giả only)
    → 💡 General (thảo luận chung)
    → 🔬 Verification (claim-specific threads)
    → ❌ Falsification (challenges + responses)
    → 🤔 Questions (hỏi về mechanism)

② ISSUE LABELS:
  → [claim: neuroscience] — biological claims cần verify
  → [claim: psychology] — behavioral claims cần verify
  → [claim: education] — learning claims cần verify
  → [claim: cross-domain] — cross-domain consistency
  → [status: needs review] — chưa ai verify
  → [status: verified] — đã có evidence confirm
  → [status: challenged] — có counterevidence
  → [status: updated] — framework đã cập nhật theo feedback

③ CREATE VERIFICATION GUIDE:
  → File: VERIFY.md (hoặc section trong README)
  → "How to stress-test this framework with AI"
  → Step 1: Clone repo
  → Step 2: Open AI (Claude Opus recommended)
  → Step 3: Drop entire folder
  → Step 4: Ask AI to check specific claims
  → Step 5: Report findings in GitHub Discussions
  → = HƯỚNG DẪN CỤ THỂ cho tech audience

④ CREATE CLAIMS LIST:
  → File: CLAIMS.md
  → Danh sách TẤT CẢ falsifiable claims
  → Mỗi claim: source file, evidence, falsification test
  → = Checklist cho verification
  → Tech audience THÍCH checklists → engagement ↑

⑤ STAR/FORK STRATEGY:
  → Stars = social proof cho next platform
  → "Framework đã có X stars on GitHub" = credibility signal
  → KHÔNG kêu gọi star — nếu tốt, tự star
  → Forks = people ĐANG verify/modify → activity signal
```

### 4.4 — Cross-Platform Linking

```
MỖI POST ĐỀU CÓ:

  HEADER (đầu bài):
    "This is 1 of 6 entry points into the Human Predictive Drive framework.
     Each post covers 1 mechanism. Full framework: [GitHub link]"

  FOOTER (cuối bài):
    "Full framework: 170+ files, 300,000+ lines, CC0 license.
     GitHub: [link]
     Discussion: [GitHub Discussions link]
     Verification guide: [VERIFY.md link]
     Claims checklist: [CLAIMS.md link]
     
     This is a hypothesis inviting falsification.
     What would break this? We want to know."

  CROSS-LINK (giữa các topics):
    T1 post: "Related: why prediction error alone isn't enough [link T5]"
    T4 post: "Background: the 2-system architecture [link T2]"
    → Người đọc 1 topic → thấy related → click → đọc thêm → GitHub
```

---

## §5 — POST EXECUTION: Cách Viết, Cách Post, Cách Respond

### 5.1 — Post Template (cho mọi platform)

```
STRUCTURE CHO MỌI BÀI (thứ tự quan trọng):

  ① PROBLEM (1-2 câu):
     "Current mainstream model X has limitation Y."
     → Hook: tạo cognitive dissonance nhẹ
     → VD: "You've heard 'dopamine = reward.' 30 years of neuroscience
            says otherwise."

  ② MECHANISM (3-5 paragraphs):
     "Here's what the research actually shows + what we propose."
     → Body chính: evidence + framework interpretation
     → PHẢI cite specific studies (author, year)
     → Tech-friendly: dùng analogy nếu phù hợp

  ③ EVIDENCE (bullets):
     3-5 key findings + citations
     → Mỗi bullet = 1 study, 1 finding, 1 sentence
     → = Scannable cho người đọc nhanh

  ④ FALSIFICATION (1 paragraph):
     "Here's how to prove this wrong."
     → Cụ thể, testable
     → = Credibility signal — không sợ bị challenge

  ⑤ HONEST LIMITATIONS (1-2 câu):
     "Here's what we DON'T know."
     → VD: "Chunk substrate is our biggest blackbox — what IS a chunk physically?"

  ⑥ CALL TO VERIFY (cuối):
     "Full framework (CC0, open): [link]
      What doesn't fit? Where does this break?"
     → = Mời engage, không mời agree
```

### 5.2 — Posting Cadence

```
⚠️ KHÔNG POST TẤT CẢ CÙNG LÚC.

TUẦN 1-2: Tier S (LessWrong + SSC)
  → Post T1 hoặc T2 → 1 platform
  → Đợi 3-5 ngày → đọc feedback
  → Refine → post cùng topic platform còn lại
  → Thu thập challenges → cập nhật draft

TUẦN 3-4: Tier A (HN + r/ML + r/cogsci)
  → Post topic ĐÃ REFINE từ Tier S
  → Adapt format cho platform
  → Đợi 1 tuần giữa mỗi platform
  → ⚠️ KHÔNG post >1 sub cùng ngày (spam detection)

TUẦN 5+: Tier B + topics còn lại
  → Mở rộng platforms
  → Post topics mới (T3, T4, T5)
  → Cross-link giữa topics

SAU 2 THÁNG: T6 (full architecture)
  → CHỈ KHI T1-T5 đã có traction
  → T6 = "If you found individual pieces interesting,
          here's the full picture"

RULE OF THUMB:
  → 1 post / tuần maximum (across all platforms)
  → Đợi feedback trước khi post tiếp
  → Nếu post bị ignore → refine, KHÔNG spam lại
  → Nếu post có traction → respond comments → THEN post tiếp
```

### 5.3 — Responding to Challenges

```
KHI AI CHALLENGE:

  ① AGREE + CITE:
     "Good point. Here's the evidence: [citation]"
     → KHÔNG defensive. Welcome challenge = credibility.

  ② HONEST:
     "We don't know. That's a genuine gap."
     → Ghi lại gap → cập nhật framework → credit người challenge.

  ③ COUNTERARGUMENT:
     "The evidence suggests otherwise: [3 studies]"
     → Luôn evidence, KHÔNG opinion.

  ④ UPDATE:
     Nếu bị falsify → CẬP NHẬT framework → note:
     "Updated based on [username]'s challenge. See commit [hash]."
     → = Framework là living document → trust ↑

KHI AI HỎI "BẠN LÀ AI?":

  → "Independent researcher. Game developer by background.
     Framework is CC0 — test the claims, not the credentials.
     Here's the evidence: [links]"
  → Redirect tới evidence, không discuss authority.

KHI AI KHEN:

  → "Thanks — but we need MORE challenge, not less.
     Here's what we're LEAST confident about: [gaps].
     Can you find holes in those?"
  → = Redirect positive engagement tới VERIFICATION
```

---

## §6 — HIỆU ỨNG LAN TRUYỀN: Verify → Propagate (Tự Nhiên)

### 6.1 — Propagation Mechanism (Nếu Framework Đúng)

```
GIAI ĐOẠN 1 — EXPOSURE (tuần 1-4):
  → Post T1-T5 tại Tier S + A
  → Tech audience đọc → "interesting, let me check"
  → Clone repo → dùng AI verify → "logic seems consistent"
  → Star repo → share với đồng nghiệp
  → = SEED planted

GIAI ĐOẠN 2 — VERIFICATION (tuần 4-12):
  → Tech extract specific claims → route tới domain experts
  → "Hey r/neuroscience, cụ thể: does VTA fire as salience signal?"
  → Domain experts respond → confirm/deny CỤ THỂ
  → Tech aggregate: "5/7 neuro claims confirmed, 2 debated"
  → GitHub Discussions = central record of verification
  → = EVIDENCE accumulates

GIAI ĐOẠN 3 — PROPAGATION (tháng 3-6):
  → Tech bloggers viết: "I stress-tested this framework with AI. Here's what I found."
  → Newsletter writers cover: "A unified model of human behavior — open source"
  → YouTubers (tech-oriented): explain framework for THEIR audience
  → = COMMUNITY tự propagate — tác giả KHÔNG CẦN push

GIAI ĐOẠN 4 — CROSS-DOMAIN (tháng 6+):
  → Teachers thấy qua tech blogs → test education mechanisms
  → Parents thấy qua newsletters → test child-development claims
  → Therapists thấy qua academic discussions → test behavioral predictions
  → = Framework tới domain practitioners QUA tech community

  KEY: Tác giả KHÔNG CẦN post ở mass community.
       Tech community = BRIDGE tự nhiên.
       Nếu framework đúng → bridge tự hình thành.
       Nếu framework sai → bridge KHÔNG hình thành = tốt.
```

### 6.2 — Anti-Propagation (Nếu Framework Sai)

```
NẾU FRAMEWORK SAI (phần lớn):
  → Tech tìm contradictions → post phân tích
  → "Framework claims X, but data shows Y" → upvote
  → Không ai share → không ai propagate → ĐÚNG behavior
  → Tác giả biết sai → sửa hoặc rút → TIẾN BỘ

NẾU FRAMEWORK SAI MỘT PHẦN:
  → Phần đúng → được share (T1 đúng → T1 propagate)
  → Phần sai → bị challenge → KHÔNG propagate → tác giả sửa
  → = Natural selection at topic level

KEY INSIGHT (từ bạn):
  "Nếu họ chửi nhiều thì ai mà lan truyền được."
  → ĐÚNG. Propagation = EMERGENT từ quality.
  → Không cần marketing strategy.
  → Chỉ cần EXPOSURE + HONEST FRAMING.
  → Quality tự sàng lọc.
```

---

## §7 — RISK MANAGEMENT

### 7.1 — Risks Specific to Tech-First Strategy

```
① PREMATURE TOOL-BUILDING:
  Risk: tech build app dựa trên mechanism CHƯA verified
  → "Dopamine Tracker" dựa trên framework → nếu framework sai → tool sai
  Phòng: README + VERIFY.md nói rõ "hypothesis, not established science"
  → "Build experiments, not products. Verify first."

② "TECH BRO SCIENCE" LABEL:
  Risk: domain experts thấy framework adopted by tech → dismiss
  Phòng:
  → Post r/cogsci song song (Tier A) → bridge
  → Frame as "inviting domain expert review"
  → Tech community output = "claims for domain expert to check"
    → KHÔNG "verified by programmers"
  → GitHub Issues tagged [needs-neuro-review] → show đang TÌM domain expert

③ VIRAL TRƯỚC KHI READY:
  Risk: HN frontpage → 300K views → oversimplify → damage
  Phòng:
  → Tier S trước (nhỏ, stress-test)
  → Tier A SAU KHI Tier S refine
  → Nếu viral xảy ra → respond bình tĩnh, redirect tới VERIFY.md
  → "Excited about interest. Here's the verification guide.
     We NEED challenges, not adoption."

④ ECHO CHAMBER:
  Risk: tech audience all agree → confirmation bias → không ai challenge
  Phòng:
  → Mỗi post KẾT THÚC bằng "What breaks this?"
  → Actively seek STRONGEST counterarguments
  → Post ở r/neuroscience (Tier B) → domain expert challenge
  → THANH challenges, KHÔNG thank agreements

⑤ AI-MEDIATED DUNNING-KRUGER:
  Risk: tech dùng AI verify → AI nói "consistent" → tech nghĩ "verified"
  → Nhưng: AI check logic, KHÔNG check empirical truth
  → Logically consistent framework CÓ THỂ empirically wrong (Freudian psychology)
  Phòng:
  → VERIFY.md phân biệt rõ:
    "AI can check: logical consistency, citation accuracy, cross-reference"
    "AI CANNOT check: whether cited studies are replicable,
     whether methodology is sound, whether interpretation is correct"
  → = Hướng dẫn tech audience giới hạn của AI verification
```

### 7.2 — Success vs Failure Signals

```
  ┌────────────────────────────────────────────────────────────────┐
  │ TÍN HIỆU THÀNH CÔNG (framework likely correct)               │
  ├────────────────────────────────────────────────────────────────┤
  │ → GitHub stars tăng đều (không burst rồi dừng)                │
  │ → Discussions active: verification threads có content          │
  │ → Tech bloggers viết detailed analysis (không chỉ summary)   │
  │ → Domain experts BẮT ĐẦU engage (comment, issue, paper)      │
  │ → Specific claims verified bởi domain expert                  │
  │ → Forks with meaningful modifications (not just stars)        │
  │ → People APPLY framework → report "matches my observation"    │
  ├────────────────────────────────────────────────────────────────┤
  │ TÍN HIỆU THẤT BẠI (framework likely wrong / needs major fix) │
  ├────────────────────────────────────────────────────────────────┤
  │ → Tier S ignore hoàn toàn (0 engagement)                     │
  │ → Multiple specific falsifications chưa trả lời được         │
  │ → Domain experts dismiss: "fundamentally misunderstands X"    │
  │ → Stars ≠ engagement (star nhưng không ai discuss)            │
  │ → Verification attempts all find problems                     │
  ├────────────────────────────────────────────────────────────────┤
  │ TÍN HIỆU TRUNG LẬP (framework partially right)              │
  ├────────────────────────────────────────────────────────────────┤
  │ → Some topics verify, some challenged                         │
  │ → = BÌNH THƯỜNG. Update + credit + re-post.                  │
  │ → Outcome tốt thứ 2 (sau verify toàn bộ)                    │
  └────────────────────────────────────────────────────────────────┘
```

---

## §8 — TIMELINE

```
  ┌──────────────────────────────────────────────────────────────────┐
  │ PHASE    │ THỜI GIAN    │ NỘI DUNG                              │
  ├──────────────────────────────────────────────────────────────────┤
  │ PREP     │ 1-2 tuần     │ GitHub setup (Discussions, Issues,     │
  │          │              │ VERIFY.md, CLAIMS.md). Viết T1+T2     │
  │          │              │ draft. Core files dịch EN (nếu chưa). │
  ├──────────────────────────────────────────────────────────────────┤
  │ TIER S   │ tuần 1-2     │ Post T1 hoặc T2 tại LessWrong.       │
  │          │              │ Đợi 3-5 ngày. Gauge. Refine.          │
  │          │              │ Post cùng topic tại r/slatestarcodex. │
  ├──────────────────────────────────────────────────────────────────┤
  │ TIER A   │ tuần 3-6     │ Refine T1/T2 từ Tier S feedback.      │
  │          │              │ Post HN + r/cogsci + r/ML.            │
  │          │              │ 1 post/tuần max. Respond comments.    │
  ├──────────────────────────────────────────────────────────────────┤
  │ EXPAND   │ tuần 7-12    │ Post T3, T4, T5 tại Tier S → A → B.  │
  │          │              │ Cross-link topics. Medium submissions. │
  │          │              │ Twitter presence building.             │
  ├──────────────────────────────────────────────────────────────────┤
  │ FULL     │ tháng 3-4    │ T6 (full architecture) nếu traction.  │
  │          │              │ Route claims → domain experts.         │
  │          │              │ Aggregate verification status.         │
  ├──────────────────────────────────────────────────────────────────┤
  │ SUSTAIN  │ tháng 4+     │ Respond challenges. Update framework.  │
  │          │              │ Credit falsifiers. Support community.  │
  │          │              │ EXIT khi community tự duy trì.        │
  └──────────────────────────────────────────────────────────────────┘

  ⚠️ Timeline = ước lượng. Thực tế phụ thuộc:
    → Tốc độ dịch EN (nếu cần)
    → Feedback từ Tier S (có thể cần refine nhiều)
    → Viral events (không kiểm soát được)
```

---

## §9 — PRE-REQUISITES: Cần Gì TRƯỚC KHI Bắt Đầu

```
PHẢI CÓ:
  □ Core files dịch tiếng Anh (ít nhất: README, Core-Software, Ask-AI,
    + 4 Clarification files, + Body-Base, Body-Feedback)
  □ GitHub Discussions enabled
  □ VERIFY.md created (hướng dẫn stress-test với AI)
  □ CLAIMS.md created (danh sách falsifiable claims)
  □ ORCID iD registered
  □ T1 + T2 post drafts written + reviewed
  □ Anticipated challenges + responses prepared (per topic)

NÊN CÓ:
  □ Zenodo DOI (academic credibility)
  □ Summary paper draft (entry point cho domain experts)
  □ bioRxiv/PsyArXiv preprint submitted
  □ 1-2 diagrams (cycle architecture, observation parameters)

KHÔNG CẦN TRƯỚC KHI BẮT ĐẦU TIER S:
  □ Toàn bộ framework dịch EN (core files đủ)
  □ Summary paper hoàn chỉnh (draft đủ)
  □ Twitter presence (xây sau)
  □ Medium publications (submit sau)
```

---

## §10 — RELATION TO PLAN-PUBLIC.MD

```
Plan này BỔ SUNG cho plan-public.md, KHÔNG thay thế.

plan-public.md:
  → General strategy (mọi audience)
  → Phase 0-4 tổng quát
  → §WHY (nền tảng chiến lược — vẫn đúng)
  → Framing rules (W.4) — ÁP DỤNG cho plan này

plan-tech-distribution.md (FILE NÀY):
  → CHUYÊN SÂU cho tech audience
  → Tại sao tech ĐẦU TIÊN (silo problem, cross-domain capability)
  → 6 topics cụ thể + platform mapping
  → Convergence architecture (GitHub hub)
  → Execution details (cadence, response protocol)

THỨ TỰ THỰC HIỆN:
  1. plan-tech-distribution.md (file này) — tech audience TRƯỚC
  2. plan-public.md Phase 2-3 — domain experts SAU (via tech routing)
  3. plan-public.md §3.8 — community propagation SAU (via natural selection)

NGUYÊN TẮC TỪ plan-public.md VẪN ÁP DỤNG:
  → W.4: KHÔNG self-help, KHÔNG marketing
  → W.5: Stakes cụ thể per topic
  → §3.1: Tác giả vs cộng đồng roles
  → §3.9: Verification → Trust → Exit
```

---

> **Plan v0.1 — sẽ refine dần.**
> Bước tiếp:
>   1. Tạo folder Public-Plan/tech-posts/ cho drafts per-topic
>   2. Viết T1 + T2 drafts (adapt từ 01-Dopamine-Not-Reward.md có sẵn)
>   3. Setup GitHub (Discussions, VERIFY.md, CLAIMS.md)
>   4. Dịch core files sang EN (prerequisite)
