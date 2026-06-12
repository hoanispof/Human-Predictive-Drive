# Future Topic Ideas — Extracted from plan-tech-distribution.md

> **Source:** plan-tech-distribution.md §2 — Topics T3, T4, T5
> **Extracted:** 2026-06-04 (trước khi backup plan-tech-distribution.md)
> **Mục đích:** Lưu lại 3 topic ideas chưa triển khai, dùng cho future blog/post planning.
> **Trạng thái:** REFERENCE — chưa có blog/post nào cho các topics này.

---

## T3 — Compile Pipeline: Cách Brain "Compile" Kinh Nghiệm

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

---

## T4 — AI Amplifies Your Wrong Self-Model

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

---

## T5 — Prediction Error Is Necessary But Insufficient

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
