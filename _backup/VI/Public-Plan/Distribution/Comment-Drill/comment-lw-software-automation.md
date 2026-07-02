# COMMENT — Why Software Automation Is Hard

> **Ref:** post-lw-software-automation.md (bài gốc)
> **Ref:** drill-lw-software-automation.md (phân tích)
> **URL:** https://www.lesswrong.com/posts/KzXptMbuDsYLrppss/why-software-automation-is-hard
> **Status:** Phase 4 BUILD done — Draft v2 ready for review

---

## §1 — SYNTHESIS (Phase 3)

```
  ⭐ Phase 3 — FILLED (2026-06-07)


  ════════════════════════════════════════════════════════
  ĐIỂM MẠNH NHẤT CHO COMMENT: GAP D + GAP B (kết hợp)
  ════════════════════════════════════════════════════════

  CHỌN GAP D (assumptions without body-check) LÀM CORE:
    → Novel reframe mà bài post chưa có: "unchecked" not "bad"
    → Trực tiếp address fn5 — author's own "even in principle" question
    → Testable prediction mà LW audience tự verify được
    → Mechanism cụ thể: gut feeling = compiled baseline + mismatch detection

  CHỌN GAP B (failure to compile) LÀM SUPPORT:
    → Kết nối tự nhiên: tại sao delegation → mất body-check?
    → Reconcile fn6 (skill stays + fog happens) = satisfying cho reader
    → Cung cấp ACTIONABLE insight (choose to solve SOME manually)

  KHÔNG DÙNG GAP A, C (lý do):
    → A (unknown knowns mechanism): quá rộng, cần nhiều chữ
    → C (multi-modal vs text): author đã gần đúng, ít novel


  ════════════════════════════════════════════════════════
  TẠI SAO KẾT HỢP D + B THAY VÌ CHỈ 1?
  ════════════════════════════════════════════════════════

    D alone: "experienced devs have gut feeling, AI doesn't" → đúng
      nhưng reader hỏi: "so what? that's obvious"
    B alone: "delegation = failure to compile" → interesting reframe
      nhưng thiếu mechanism giải thích WHY that matters
    D + B combined: "expertise builds through doing → creates
      internal baseline → when assumptions violate baseline →
      gut feeling fires → AI has no equivalent signal"
      → = COMPLETE CAUSAL CHAIN: doing → patterns → baseline →
        mismatch detection → gut feeling
      → Reader: "ah, THAT'S why!"

    Constraint: ~150-200 words → phải rất tight


  ════════════════════════════════════════════════════════
  ACKNOWLEDGE POINT (cụ thể)
  ════════════════════════════════════════════════════════

  TARGET: Footnote 5 — assumption trade-off
    → "they have learned to make usually correct assumptions...
       but I don't think they have a way, even in principle, to
       distinguish right from wrong assumptions reliably"
    → = Author's sharpest observation, LÀ NỀN cho framework add

  ACKNOWLEDGE CÂU: Framing assumption-making as a fundamental
    trade-off rather than a fixable bug is spot on.
    → Cụ thể (footnote 5 insight, not general praise)
    → Tôn trọng (author's analysis = starting point)
    → Ngắn gọn (1 câu)


  ════════════════════════════════════════════════════════
  MAINSTREAM LANGUAGE (dịch từ plan-content-engagement §6.2)
  ════════════════════════════════════════════════════════

  ┌─────────────────────┬──────────────────────────────────┐
  │ FRAMEWORK TERM      │ COMMENT LANGUAGE                  │
  ├─────────────────────┼──────────────────────────────────┤
  │ compiled behavior   │ automatic patterns / learned      │
  │                     │ patterns built through doing      │
  ├─────────────────────┼──────────────────────────────────┤
  │ body-feedback       │ gut feeling / that physical sense │
  │                     │ that something's off              │
  ├─────────────────────┼──────────────────────────────────┤
  │ prediction-delta    │ your brain flags a mismatch       │
  │                     │ between what it expects and what  │
  │                     │ it sees                           │
  ├─────────────────────┼──────────────────────────────────┤
  │ Experience Compile  │ learning from direct experience / │
  │                     │ learning by doing                 │
  ├─────────────────────┼──────────────────────────────────┤
  │ PFC vs body-base    │ conscious reasoning vs the        │
  │                     │ automatic system that runs in the │
  │                     │ background                        │
  ├─────────────────────┼──────────────────────────────────┤
  │ Precondition-2      │ compiled baseline / years of      │
  │ (Chunk-Substrate)   │ hands-on pattern building         │
  ├─────────────────────┼──────────────────────────────────┤
  │ Background-Pattern  │ accumulated experience that runs  │
  │                     │ in the background without you     │
  │                     │ noticing                          │
  ├─────────────────────┼──────────────────────────────────┤
  │ "failure to compile"│ failure to build new automatic    │
  │                     │ patterns / expertise doesn't form │
  │                     │ from reading — it forms from doing│
  └─────────────────────┴──────────────────────────────────┘

  ⚠️ KHÔNG dùng trong comment:
    prediction-delta, compiled behavior, body-base, PFC,
    chunk, compile, Background-Pattern, Hebbian, VTA


  ════════════════════════════════════════════════════════
  PREDICTION + FALSIFICATION
  ════════════════════════════════════════════════════════

  PREDICTION (mainstream language):
    "If this is right, we'd expect a specific pattern: as context
    windows grow, agents should get much better at matching known
    patterns in a codebase, but their rate of catching violations
    of UNWRITTEN norms — the things experienced devs flag on gut
    feeling — should plateau. The gap would be most visible in
    edge cases where the code technically works but an experienced
    developer would say 'this doesn't feel right.'"

  FALSIFICATION (mainstream language):
    "If scaling context windows closes BOTH gaps equally — known
    patterns AND unwritten norms — then the missing piece isn't
    architectural but informational, and my framing is wrong."

  → Testable by LW audience (many use coding agents daily)
  → Specific: known patterns vs unwritten norms = measurable split
  → Honest: explicitly states what would prove framing wrong


  ════════════════════════════════════════════════════════
  CÂU MỜI THẢO LUẬN
  ════════════════════════════════════════════════════════

  OPTION A (experience-focused):
    "Curious whether this matches your experience — do you find
    yourself catching different types of issues than your agents?"

  OPTION B (prediction-focused):
    "I'd be interested to hear if anyone has data on whether
    fine-tuned models actually close this gap or just the
    pattern-matching one."

  CHỌN: Option A — vì:
    → Nối trực tiếp với author's own experience (fn1: 15 năm)
    → Invites personal observation → easy to engage
    → Không yêu cầu data → lower barrier to respond
    → Author ĐÃ nói "happy to hear thoughts" → receptive


  ════════════════════════════════════════════════════════
  QUALITY GATE: ĐÁNG COMMENT KHÔNG?
  ════════════════════════════════════════════════════════

    ✅ Framework giải thích mechanism gap mạnh (D = Very Strong)
    ✅ Reframe novel: "unchecked" not "bad"
    ✅ Prediction testable + falsifiable
    ✅ Audience = LW tech-rationalist = mechanism reasoning = high value
    ✅ Author receptive ("happy to hear thoughts")
    ✅ NOT ép framework — builds on author's own observations
    ✅ Reader không biết framework → vẫn thấy hay

    → ✅ PASS QUALITY GATE — proceed to Phase 4 BUILD
```

---

## §2 — DRAFT COMMENT (Phase 4)

### Draft v1

```
  Your framing of assumption-making as a fundamental trade-off rather
  than a fixable bug is the sharpest point in this post. I think there's
  a specific mechanism underneath it worth naming.

  When an experienced developer has spent years hands-on with a codebase,
  they've built up thousands of automatic patterns — not just knowledge
  they can articulate, but a kind of background model that runs without
  conscious effort. When an assumption violates that background model,
  the brain flags a mismatch: that pre-verbal "something's off" feeling
  before you can explain why. This is what lets experienced devs catch
  wrong assumptions — not better reasoning, but a mismatch-detection
  system built from direct experience.

  Coding agents don't have this. They can match patterns statistically
  — often impressively well — but when an assumption happens to violate
  an unwritten norm of the codebase, there's no internal signal that
  fires. The assumptions aren't "bad"; they're unchecked.

  This also connects to your point about cognitive decline (footnote 6).
  When developers delegate problem-solving, they're not losing existing
  skills — those persist. But they stop building NEW automatic patterns,
  because those only form through direct experience, not from reading an
  agent's explanation. Over time, the background model doesn't keep up
  with how the codebase evolves. The "brain fog" you describe is what it
  feels like when your conscious mind has to handle everything that the
  automatic system would normally catch in the background.

  If this framing is right, it predicts something specific: as context
  windows scale up, agents should get dramatically better at matching
  documented patterns, but their rate of catching violations of unwritten
  norms — the things experienced devs flag on gut feeling — should
  plateau. If scaling context closes both gaps equally, this framing
  is wrong.

  Curious whether this matches your experience — do you notice yourself
  catching fundamentally different types of issues than your agents do?
```

### Draft v2 (refined — changes noted)

```
  CHANGES FROM V1:
    ① "reading an agent's explanation" → "reviewing an agent's solution"
       (more precise — devs review solutions, not explanations)
    ② Tightened Gap B paragraph (~15 words shorter)
    ③ "what it feels like when..." → simpler phrasing
    ④ Slightly smoother D→B transition
    ⑤ "not better reasoning" → rephrased to avoid implying agents
       DO have better reasoning
    ⑥ Lines wrapped at ~72 chars (LW editor overflow fix — single \n
       → space in rendered markdown; blank lines = paragraph break)
    ⑦ Gap B sentences (3 × single-\n) merged into one paragraph
       (LW renders them as one para anyway; now explicit + wrapped)

  ─────────────── DRAFT V2 ───────────────

Your framing of assumption-making as a fundamental trade-off rather
than a fixable bug is the sharpest point in this post. I think
there's a specific mechanism underneath it worth naming.

When an experienced developer has spent years hands-on with a
codebase, they've built thousands of automatic patterns — not just
knowledge they can articulate, but a background model that runs
without conscious effort. When an assumption violates that model,
the brain flags a mismatch: that pre-verbal "something's off"
feeling before you can explain why. Experienced devs catch wrong
assumptions not through superior reasoning, but through a
mismatch-detection system built from years of direct problem-solving.

Coding agents don't have this. They match patterns statistically —
often impressively well — but when an assumption violates an
unwritten norm of the codebase, there's no internal signal that
fires. The assumptions aren't "bad"; they're unchecked.

This connects to your cognitive decline point (footnote 6). When
developers delegate, they're not losing existing skills — those
persist. But new automatic patterns only form through hands-on
problem-solving, not from reviewing an agent's solution. So over
time, the developer's background model stops growing while the
codebase keeps evolving — and the widening gap means more and more
decisions fall to conscious effort instead of automatic
pattern-matching. That's the "brain fog": not skill loss, but your
conscious mind picking up work that the automatic system was never
built to handle.

If this framing is right, it predicts something testable: as
context windows scale, agents should get dramatically better at
matching documented patterns, but plateau on catching violations of
unwritten norms — the stuff experienced devs flag on gut feeling.
If scaling context closes both gaps equally, this framing is wrong.

Curious whether this matches your experience — do you notice
yourself catching fundamentally different types of issues than your
agents do?

  ─────────────── END DRAFT V2 ───────────────

  WORD COUNT: ~270 words (down from ~300)
  STRUCTURE:  Acknowledge(1) + Gap D(2 para) + Gap B(1 para)
              + Prediction(1 para) + Invite(1 sentence)
```

---

## §3 — QUALITY CHECK (Phase 4)

```
  ⭐ QUALITY CHECK — Draft v1 (2026-06-07)

  CONTENT:
    ✅ Cho giá trị, không quảng cáo
       → Mechanism explanation = value. Không link, không mention framework.
    ✅ Bổ sung, không sửa
       → "I think there's a specific mechanism underneath it worth naming"
       → = Building on, not correcting
    ✅ Không mention "framework" hay "my research"
       → Zero framework references. Zero self-promotion.
    ✅ Reader không biết framework → vẫn thấy comment hay
       → Comment đọc như cognitive science insight, standalone

  LANGUAGE:
    ✅ Ngôn ngữ mainstream, không jargon
       → "automatic patterns", "background model", "gut feeling",
         "mismatch-detection system", "unwritten norms"
    ✅ Không dùng: prediction-delta, compiled behavior, body-base, PFC
       → Zero framework terms
    ✅ Dùng mainstream equivalents naturally
       → "brain flags a mismatch" (= prediction-delta)
       → "automatic patterns built from direct experience" (= compiled)
       → "conscious mind has to handle everything" (= PFC overload)

  STRUCTURE:
    ✅ ① ACKNOWLEDGE (1 câu)
       → "Your framing of assumption-making as a fundamental trade-off
          rather than a fixable bug is the sharpest point in this post."
       → Cụ thể (assumption trade-off), không nịnh (analytical praise)
    ✅ ② PHÂN TÍCH GAP — phần CHÍNH (3 paragraphs)
       → Para 1: mechanism of gut feeling (Gap D core)
       → Para 2: why agents lack it ("unchecked" reframe)
       → Para 3: cognitive decline explained (Gap B support)
    ✅ ③ DỰ ĐOÁN MỞ RỘNG (1 paragraph)
       → Specific: documented patterns vs unwritten norms
       → Falsification: "if scaling context closes both gaps equally"
    ✅ ④ MỜI THẢO LUẬN (1 câu)
       → "Curious whether this matches your experience"

  PLATFORM FIT:
    ✅ Tone phù hợp LessWrong — analytical, mechanism-focused, falsifiable
    ⚠️ Độ dài ~300 words — TRÊN target 100-200
       → NHƯNG: LW comments thường dài hơn YouTube/Reddit
       → Top comments bài này: AnthonyC ~200 words, author reply ~250 words
       → ~300 words = acceptable for LW analytical comment
       → CÂN NHẮC: v2 có thể trim đoạn Gap B nếu cần ngắn hơn
    ✅ Prediction có falsification condition
       → "If scaling context closes both gaps equally, this framing is wrong"

  RESPECT:
    ✅ Author đọc sẽ feel respected
       → "sharpest point in this post" = genuine appreciation
       → "This also connects to your point about cognitive decline"
       → = Linking TO author's insights, not over them
    ✅ Không imply author thiếu kiến thức
       → "a specific mechanism underneath it" = deeper layer, not correction
       → Author = industry observer, framework = different discipline
    ✅ Frame bổ sung
       → "I think there's a mechanism worth naming" = offering angle

  ────────────────────────────────────────
  OVERALL ASSESSMENT:
    ✅ 11/12 checks pass
    ⚠️ 1 concern: LENGTH (~300 words vs 100-200 target)

  OPTIONS:
    A. Keep ~300 words (LW-appropriate, analytical depth = valued)
    B. Trim Gap B paragraph → ~200 words (tighter, loses fn6 connection)
    C. Split: Core comment ~200 words + reply-to-self with Gap B detail
```

---

## §4 — POST STATUS (Phase 5)

```
  NGÀY POST:
  LINK COMMENT:

  ENGAGEMENT:
    24h:
    48h:
    1 tuần:

  REPLIES THÚ VỊ:
    →

  BÀI HỌC RÚT RA:
    →
```
