# DRILL — Why Software Automation Is Hard

> **Ref:** post-lw-software-automation.md (bài gốc)
> **Ref:** comment-lw-software-automation.md (output)
> **Status:** Phase 1 CAPTURE done → chờ Phase 2 DRILL

---

## §1 — ĐÁNH GIÁ SƠ BỘ

```
  TOPIC:       Software automation bottlenecks tại enterprise scale
  AUDIENCE:    LW tech-rationalist, nhiều software engineers
  TONE:        Analytical, measured, acknowledges uncertainty
  ĐỘ DÀI:     ~2500 words + footnotes
  AUTHOR BG:   15 năm programmer, dùng Copilot + Claude Code professionally

  PHÙ HỢP FRAMEWORK:  CAO
    → Author mô tả WHAT (bottlenecks) nhưng thiếu WHY (mechanism)
    → Framework giải thích WHY ở mức mechanistic
    → Multiple mapping points rõ ràng

  RỦI RO:  THẤP
    → Author không phải cognitive science expert
    → Framework contribution rõ ràng novel
    → Bổ sung, không sửa = natural fit
```

---

## §2 — BÀI POST NÓI GÌ? (Drill Question ①)

```
  ⭐ Phase 2 — FILLED (2026-06-07)

  TÁCH RIÊNG:

  CLAIMS (author assert as true):

    C1. Context = bottleneck LỚN NHẤT cho software automation
        → Cả context window SIZE lẫn cách FILL context

    C2. Humans có "vast amounts of context" — chỉ 1 phần nhỏ active cho mỗi task
        → "It just automatically appears in our brains when we need it"
        → Đôi khi human KHÔNG BIẾT mình đang dùng context nào ("unknown knowns")

    C3. Words are not a great representation — human context gần embedding vectors hơn
        → "Words don't come with integrated dimensions of importance,
           recency, risk, interrelations"

    C4. Expert KHÔNG THỂ viết hết knowledge ra text
        → "many millions of words, still wouldn't capture everything"
        → "would not be expressed in a way that the LLM would understand"

    C5. Agents rely on assumptions = FUNDAMENTAL TRADE-OFF, không phải bug cần fix
        → "Them jumping to conclusions is a feature, not a bug"
        → Nhưng "don't have a way, even in principle, to distinguish right
           from wrong assumptions" (footnote 5)

    C6. Tech debt tích lũy khi dùng low-context agents
        → "isolated patches rather than clean, wholesome solutions"
        → Nhiều agent instances = nhiều contributor không hiểu code = quality giảm

    C7. Cognitive decline xảy ra khi delegate quá nhiều
        → "People can solve hard problems without understanding them"
        → "It now takes a lot of agency to understand things"

    C8. Coordination bottlenecks KHÔNG THỂ bypass bằng tăng tốc 1 phần
        → "You can't just accelerate isolated aspects by 10x"
        → Amdahl's Law (Stephen McAleese comment)

    C9. Diminishing returns — tốc độ KHÔNG tự chuyển thành giá trị
        → "not at all clear that 5x faster → anything close to 5x ARR"


  EVIDENCE (data, examples, citations):

    E1. Author experience: 15 năm lập trình, dùng Copilot + Claude Code professionally
        → = First-person industry observation (not formal study)

    E2. Footnote 3 — specific examples of intangible knowledge:
        → Dangerous modules ("the 3 times somebody tried that, it always
           spectacularly failed")
        → Conflict with other teams having strong views
        → Non-functional requirements absorbed organically

    E3. Footnote 4 — "theory of the code" concept:
        → Humans build constantly growing model of code+product+org
        → Know users, bug severity, outage impact, future plans, time pressure
        → "Very particular glasses through which human sees their work"

    E4. Footnote 5 — observation about LLM assumptions:
        → Prompts are vague nhưng LLM usually infers correctly
        → "learned to make usually correct assumptions with incomplete info"
        → But can't distinguish right from wrong assumptions reliably

    E5. Footnote 6 — cognitive decline personal experience:
        → "Brain fog when suddenly have to work without coding agent"
        → "drug of just typing the problem into a chat box"
        → Metaphor, no mechanism

    E6. Comments evidence:
        → AnthonyC (179pts): fine-tune on codebase → tacit knowledge in weights
        → core (20pts): "proves too much" challenge — replacing dev team ALSO hard
        → Dagon (50pts): fractal nature — meta-meta-tasks also need automation
        → McAleese (20pts): Amdahl's Law formal framing


  OPINIONS (author's judgment/impression):

    O1. "Gets less and less true the larger an organization is"
        → Qualified impression, not data-backed

    O2. Speed KHÔNG essential cho hầu hết companies
        → "quality of strategic insight is likely more important than speed"
        → Judgment call

    O3. Startups CÓ THỂ figure it out better than established orgs
        → "these better-prepared startups may outcompete"
        → Plausible but speculative

    O4. Cognitive decline is "very concerning"
        → Personal assessment of risk

    O5. "Betting the minds of millions of engineers" on continued AI progress
        → Framing choice — dramatic but not evidence

    O6. Bull Case might work but author is skeptical
        → "I would expect these to not have that much of an immediate advantage"


  ASSUMPTIONS (taken for granted, not argued):

    A1. ⭐ Tacit knowledge LÀ GÌ → được mô tả nhưng KHÔNG giải thích
        → "Unknown knowns" — WHY knowledge becomes tacit? Không có mechanism
        → "It just automatically appears" — HOW? Không giải thích

    A2. ⭐ Cognitive decline HAPPENS → được mô tả nhưng mechanism chỉ là metaphor
        → "Drug of typing" (fn6) — metaphor, không phải mechanism
        → WHY delegation erodes skill? Không giải thích beyond observation

    A3. ⭐ Words poorly represent — OBSERVED nhưng WHY không giải thích
        → "Human context is closer to embedding vectors" — observation
        → TẠI SAO brain representation ≠ text representation? Không address

    A4. ⭐ Human CAN distinguish right/wrong assumptions, AI CAN'T → WHY?
        → Footnote 5: "I don't think they have a way even in principle"
        → Nhưng MECHANISM cho human ability này = không explain
        → "Gut feeling" được ngụ ý nhưng không named/explained

    A5. Non-functional requirements absorbed "organically" by humans
        → HOW "organic absorption" works? Không giải thích

    A6. "Theory of the code" grows constantly in humans
        → HOW? Through what mechanism? Không giải thích


  AUTHOR ACKNOWLEDGES LIMITATIONS?

    ✅ YES — author acknowledges extensively:
      → "I'm sure none of the thoughts in this post are totally original"
      → Bull Case section = genuine counterargument engagement
      → "None of the challenges are insurmountable"
      → "I'm not meaning to imply much about alignment/existential risk"
      → Tone = analytical, measured, invites disagreement
      → "Happy to hear thoughts on where you think I'm off"

    ⚠️ KEY OBSERVATION:
      → Author rất honest về LIMITATIONS CỦA CLAIMS (bounded scope)
      → Nhưng KHÔNG aware rằng mình describe WHAT without explaining WHY
      → 4 assumptions A1-A4 = 4 gaps chính
      → Author GIAO ĐÚNG nơi framework có thể BỔ SUNG (not contradict)


  TÓM TẮT PATTERN:

    Author = EXCELLENT observer — mô tả PHENOMENA chính xác:
      → "Unknown knowns" (A1)
      → Cognitive decline (A2)
      → Words vs brain representation (A3)
      → Assumption reliability gap (A4)

    Author = DOES NOT explain mechanisms:
      → Dừng ở WHAT level, thiếu WHY level
      → Dùng metaphor thay mechanism (fn6: "drug", "brain fog")
      → Dùng comparison thay explanation ("closer to embedding vectors")

    → = FRAMEWORK OPPORTUNITY: bổ sung WHY cho WHAT author đã mô tả
    → Fit tự nhiên: "building on your observations, here's a possible mechanism"
    → Risk THẤP: author đã invite disagreement, tone analytical
```

---

## §3 — GAP NÀO TỒN TẠI? (Drill Question ②)

```
  ⭐ Phase 2 — FILLED (2026-06-07)

  ════════════════════════════════════════════════════════
  GAP A — WHY TACIT KNOWLEDGE IS TACIT
  ════════════════════════════════════════════════════════

    AUTHOR NÓI GÌ:
      → "Unknown knowns that they never explicitly thought about" (main)
      → "It just automatically appears in our brains" (main)
      → "Human does not even consciously notice they're relying on
         some piece of context" (main)
      → "Much of their knowledge may be unknown knowns" (main)
      → Footnote 3: intangible things — dangerous modules, team conflicts,
        implicit constraints → "you don't necessarily think about deliberately,
        but they still steer your behavior in meaningful ways"
      → Footnote 4: "constantly growing theory of the code, of the product,
        and of the organization as a whole"

    AUTHOR CÓ ADDRESS MECHANISM KHÔNG?
      → ❌ KHÔNG. Author MÔ TẢ phenomena xuất sắc:
        - Knowledge tự appear (WHAT)
        - Knowledge invisible to knower (WHAT)
        - Knowledge steer behavior without awareness (WHAT)
        - Knowledge = "unknown knowns" (LABEL)
      → Nhưng WHY: tại sao knowledge trở thành invisible? = KHÔNG address
      → HOW: cơ chế nào khiến knowledge "tự appear"? = KHÔNG address
      → WHY: tại sao không thể "viết hết ra text"? = KHÔNG address

    GAP THẬT HAY GIẢ?
      → ✅ GAP THẬT — verified qua 3 tests:
        ① Author dùng METAPHOR thay mechanism: "just appears",
           "unknown knowns" (Rumsfeld term, not mechanism)
        ② Author dùng COMPARISON thay explanation: "closer to
           embedding vectors" (what it's LIKE, not HOW it works)
        ③ LW comments CŨNG không address WHY:
           AnthonyC (179pts) gợi ý fine-tuning = solution
           nhưng KHÔNG giải thích WHY knowledge tacit ban đầu
      → Author KHÔNG cần giải thích (bài = industry observation, not cogsci)
      → Gap = legitimate EXTENSION, not correction

    FRAMEWORK EXPLANATION STRENGTH: ⭐ STRONG
      → Background-Pattern.md §1.1: accumulated chunk-network invisible to PFC
      → Background-Pattern.md §5: 7 reasons PFC cannot observe:
        ① Habituation — VTA không fire cho constant
        ② Quá phân tán — không có boundary
        ③ Gist đã abstract — detail gốc đã fade
        ④ Được label thành identity — "tôi vốn vậy"
        ⑤ Compound — fire cùng event khác
        ⑥ Compiled suppress absorb vào baseline
        ⑦ PFC budget finite — giảm tool để detect
      → Chunk.md §8.1: vô thức = ~95% processing
      → Compile-Taxonomy.md §4.1: Experience Compile = direct exposure,
        ~90% behavior = automatic compiled patterns
      → Chunk.md §1.1: NO SOURCE TAG — PFC cannot trace back origin


  ════════════════════════════════════════════════════════
  GAP B — WHY COGNITIVE DECLINE HAPPENS WITH DELEGATION
  ════════════════════════════════════════════════════════

    AUTHOR NÓI GÌ:
      → "People can solve hard problems without understanding them" (main)
      → "It now takes a lot of agency to understand things, because
         you don't have to anymore" (main)
      → "Some have reported brain fog when suddenly working without
         a coding agent. I've experienced this as well." (main)
      → Footnote 6: "once you're high on the drug of just typing
         the problem into a chat box and hope for it to magically
         get solved, it's very hard to go back to the old world
         of expending serious cognitive effort for 8 hours a day"
      → "The software world is currently betting the minds of
         millions of engineers on continued progress" (main)

    AUTHOR CÓ ADDRESS MECHANISM KHÔNG?
      → ❌ KHÔNG — author dùng METAPHOR:
        - "Drug" (fn6) — addiction analogy, not mechanism
        - "Brain fog" — phenomenological description
        - "Lost the skill" — observed outcome, not HOW skill is lost
      → Author acknowledge "I don't necessarily think that the skill
        itself degrades that quickly" (fn6) — nhận ra skill ≠ lost
      → Nhưng KHÔNG explain: nếu skill không mất, TẠI SAO fog?

    GAP THẬT HAY GIẢ?
      → ✅ GAP THẬT — verified:
        ① Author chỉ ra đúng cả 2 HIỆN TƯỢNG (delegation → decline + skill
           không mất ngay) nhưng thiếu mechanism NỐI 2 hiện tượng
        ② LW comments không address WHY:
           Không có comment nào giải thích mechanism of decline
        ③ Author's own note "I find this very concerning" =
           still at observation level, seeking explanation

    FRAMEWORK EXPLANATION STRENGTH: ⭐⭐ VERY STRONG
      → Compile-Taxonomy.md §4.1: Experience Compile = DIRECT EXPOSURE
        → Hebbian → compiled chunk
        → ~90% behavior = experience-compiled patterns
        → You only compile through DOING, not watching/reading
      → Delegation = REMOVE experience loop:
        1. AI solves problem → dev reads explanation → "yeah makes sense"
        2. Dev's body NOT exposed to problem-solving process
        3. No neural firing of problem-specific patterns
        4. No Hebbian strengthening → no new chunks compiled
        5. Existing chunks DON'T decay quickly (substrate level)
        6. But NEW chunks aren't forming → gap widens over time
      → "Brain fog" explained:
        → Chunk.md §9.1: Expert = database LỚN → PFC holds META-CHUNKS
          (each slot = much more info). Beginner = database NHỎ → PFC
          holds small chunks → overloaded
        → Without new compiled patterns → PFC must hold EVERYTHING fresh
        → PFC budget = finite (PFC-Operations §9) → exhaustion → "fog"
      → ⭐ REFRAME: không phải "cognitive decline" mà là
        "FAILURE TO COMPILE NEW CHUNKS"
        → Skill cũ vẫn còn (author đúng). Skill MỚI không form.
        → = Architecture prediction, not metaphor

    ⚠️ NUANCE QUAN TRỌNG:
      → Author fn6 note "skill doesn't degrade that quickly"
      → Framework ĐỒNG Ý: compiled chunks resist decay (Chunk §5.4)
      → Framework ADD: problem = NOT compilation, not LOSS of compilation
      → = Complementary, not contradictory


  ════════════════════════════════════════════════════════
  GAP C — WHY WRITTEN LANGUAGE POORLY REPRESENTS EXPERTISE
  ════════════════════════════════════════════════════════

    AUTHOR NÓI GÌ:
      → "Human context is closer to embedding vectors" (main)
      → "Words don't come with integrated dimensions of importance,
         recency, risk, interrelations" (main)
      → "The word count explodes the more nuance you want to
         represent in your context" (main)
      → "An experienced human worker can just write down everything
         they know... I don't think that's feasible" (main)
      → "Would not be expressed in a way that the LLM would
         understand/interpret in the same way" (main)

    AUTHOR CÓ ADDRESS MECHANISM KHÔNG?
      → ⚠️ PARTIALLY — author dùng COMPARISON:
        - "Closer to embedding vectors" — comparison ĐÚNG nhưng
          không giải thích TẠI SAO brain ≠ text
        - "Words don't come with integrated dimensions" —
          observes what words LACK, not WHY brain HAS it
      → Better than A1/A2 nhưng vẫn dừng ở observation level

    GAP THẬT HAY GIẢ?
      → ✅ GAP THẬT nhưng NHỎ HƠN A và B:
        ① Author's "embedding vectors" comparison = correct direction
        ② Author identifies WHAT is missing (dimensions, nuance)
        ③ Gap = WHY brain has multi-dimensional representation
           nhưng text doesn't → mechanism level chưa explain
      → = Weaker gap — framework bổ sung mechanism cho observation
        author đã gần đúng

    FRAMEWORK EXPLANATION STRENGTH: 🟡 MODERATE-STRONG
      → Chunk.md §1.2: chunks = MULTI-MODAL from birth
        (visual + auditory + somatic + emotional fire AS ONE)
      → Chunk.md §6: Labels = retrieval PATHS, not chunk CONTENT
        → Words point to chunks but DON'T carry multi-modal richness
        → "Moderate Whorfian" (§6.2): labels shape ACCESS, not content
      → Body-base processes ~95% in PARALLEL, multi-modal
      → PFC can only hold ~4±1 items SEQUENTIALLY (Cowan 2001)
      → Text = PFC-level output (sequential, single-modal, explicit)
      → Expert knowledge = body-base compiled (parallel, multi-modal)
      → Context limitation = ARCHITECTURAL, not just quantity:
        even infinite tokens ≠ multi-modal compiled body-base
      → ⚠️ Nhưng: author's "embedding vectors" comparison
        suggests awareness of this — framework REFINES, not discovers


  ════════════════════════════════════════════════════════
  GAP D — WHY HUMANS CAN "SMELL" WRONG ASSUMPTIONS BUT AI CAN'T
  ════════════════════════════════════════════════════════

    AUTHOR NÓI GÌ:
      → "They have learned to make usually correct assumptions
         when working with highly incomplete information" (fn5)
      → "But this comes at the cost of sometimes making wrong
         assumptions without questioning them" (fn5)
      → "I don't think they have a way, even in principle, to
         distinguish right from wrong assumptions reliably" (fn5)
      → "A lot of time can be wasted on such cases" (main)
      → "This is a fundamental trade-off with no perfect solution" (main)
      → "Developers often complain about coding agents just assuming
         things" (main)

    AUTHOR CÓ ADDRESS MECHANISM KHÔNG?
      → ❌ KHÔNG — author identifies the PHENOMENON perfectly:
        - Agents MUST assume (otherwise too slow)
        - Agents CAN'T distinguish right from wrong assumptions
        - Humans somehow CAN (implicit — "developers complain")
      → Nhưng KHÔNG explain:
        - WHY humans can distinguish (mechanism?)
        - WHAT mechanism allows "even in principle" distinction?
        - HOW experienced dev "smells" wrong assumption?

    GAP THẬT HAY GIẢ?
      → ✅ GAP THẬT — verified:
        ① Author explicitly says "even in principle" = seeking mechanism
        ② No comments address the HOW of human assumption-checking
        ③ Author frames as "fundamental trade-off" = resigned, no solution
           → Framework offers a WHY that reframes the trade-off

    FRAMEWORK EXPLANATION STRENGTH: ⭐⭐ VERY STRONG
      → Body-Feedback-Precondition.md §1.1: 5 preconditions AND-gate:
        Precondition-2: CHUNK-SUBSTRATE — need compiled chunks to decode
        Precondition-3: DELTA-GATE — VTA detect change > threshold
      → HUMAN DEVELOPER WITH EXPERIENCE:
        1. Years of codebase work → compiled baseline (Background-Pattern)
        2. Encounter assumption → body checks against compiled baseline
        3. Assumption VIOLATES baseline → VTA fires (prediction error)
        4. Body-feedback signal: "something's off" (pre-verbal)
        5. Multi-Weak-Signal-Convergence (Chunk §8.5) → "gut feeling"
        6. Dev investigates → finds wrong assumption
      → AI AGENT:
        1. No body → no compiled baseline for THIS codebase
        2. Makes assumption → no body-check possible
        3. No VTA, no prediction-delta, no "something's off"
        4. Must either ask (slow) or proceed (risk wrong)
        5. Cannot distinguish right from wrong assumptions
           BECAUSE THERE IS NO BODY-FEEDBACK SIGNAL TO FIRE
      → ⭐ REFRAME: Not "agents make BAD assumptions"
        but "agents make assumptions WITHOUT BODY-CHECK"
        → Human ability = not "better reasoning" but "compiled baseline
          generates prediction-delta when assumption violates pattern"
        → This is ARCHITECTURAL, not quality improvement
      → 🟢 Schultz 1997: VTA prediction error signals
      → 🟢 Damasio 1994: somatic marker hypothesis
      → 🟢 Klein 1998: expert intuition = pattern recognition


  ════════════════════════════════════════════════════════
  TỔNG HỢP — 4 GAPS RANKED
  ════════════════════════════════════════════════════════

    ┌────┬──────────────────────────────┬─────────────┬──────────────┐
    │ #  │ GAP                          │ FRAMEWORK   │ COMMENT      │
    │    │                              │ STRENGTH    │ POTENTIAL    │
    ├────┼──────────────────────────────┼─────────────┼──────────────┤
    │ A  │ WHY tacit knowledge is tacit │ ⭐ STRONG    │ HIGH         │
    │    │ ("unknown knowns" mechanism) │             │ (core topic) │
    ├────┼──────────────────────────────┼─────────────┼──────────────┤
    │ B  │ WHY delegation → decline     │ ⭐⭐ V.STRONG │ HIGH         │
    │    │ (failure to compile)         │             │ (reframe)    │
    ├────┼──────────────────────────────┼─────────────┼──────────────┤
    │ C  │ WHY words ≠ brain           │ 🟡 MOD-STR   │ MEDIUM       │
    │    │ (multi-modal vs sequential)  │             │ (author      │
    │    │                              │             │  already     │
    │    │                              │             │  close)      │
    ├────┼──────────────────────────────┼─────────────┼──────────────┤
    │ D  │ WHY humans "smell" wrong     │ ⭐⭐ V.STRONG │ HIGHEST      │
    │    │ assumptions (body-check)     │             │ (novel       │
    │    │                              │             │  reframe +   │
    │    │                              │             │  testable)   │
    └────┴──────────────────────────────┴─────────────┴──────────────┘

    ⭐ TOP CANDIDATES cho comment: GAP D + GAP B
      → D: novel reframe ("assumptions without body-check"),
           testable prediction, trực tiếp address fn5 concern
      → B: powerful reframe ("failure to compile, not decline"),
           directly explains fn6 "brain fog", matches author's own
           observation that "skill doesn't degrade that quickly"
      → A: strong nhưng rộng (khó fit trong 100-200 word comment)
      → C: author đã gần đúng → framework chỉ refine, ít novel

  ⚠️ VERIFIED — KHÔNG GAP GIẢ:
    → Tất cả 4 gaps = phenomena author MÔ TẢ CHÍNH XÁC, thiếu MECHANISM
    → Tất cả 4 = framework BỔ SUNG, không CONTRADICTS
    → Tất cả 4 = author sẽ RECOGNIZE gap nếu được chỉ ra
      (vì author đã gần chạm vào, đặc biệt fn5 và fn6)
```

---

## §4 — FRAMEWORK MAP VÀO ĐÂU? (Drill Question ③)

```
  ⭐ Phase 2 — FILLED (2026-06-07)


  ════════════════════════════════════════════════════════
  GAP A ↔ COMPILED BEHAVIOR INVISIBLE TO PFC
  ════════════════════════════════════════════════════════

    FILES:
      Background-Pattern.md v2.0 §1.1, §5 (primary)
      Chunk.md v3.0 §1.3, §8.1, §8.5
      Compile-Taxonomy.md v3.0 §4.1

    MECHANISM (chi tiết):

      ① COMPILATION = EXPERIENCE → HEBBIAN → AUTOMATIC PATTERN
        → Compile-Taxonomy §1.1: TẤT CẢ compile = Exposure → Hebbian
        → 1 Engine duy nhất. Experience Compile = direct exposure, ~90% behavior
        → Developer debug 1000 lần → neurons fire together → wire together
        → Pattern [code structure → likely bug location] compiled
        → Sau compile: fires WITHOUT PFC involvement

      ② COMPILED PATTERNS = INVISIBLE TO PFC (7 reasons)
        → Background-Pattern §5:
          Reason ①: Habituation — VTA không fire cho CONSTANT baseline
            → Developer "biết" codebase = constant → VTA silent → PFC no alert
            → = Author's "unknown knowns" — knowledge IS there but PFC not alerted
          Reason ②: Quá phân tán — pattern linked to thousands of chunks
            → 10 năm làm 1 codebase → pattern linked to EVERY sub-system
            → PFC cannot "see" boundary → cannot articulate
          Reason ③: Gist đã abstract — chi tiết gốc đã fade qua sleep
            → Thousands of debugging sessions → gist [pattern X → bug Y] remains
            → Detail FADE: which ticket, which day, which version → GONE
            → = Author fn3: "you don't necessarily think about deliberately"
          Reason ④: Labeled as identity — PFC says "I just know the code"
            → "Theory of the code" (fn4) = PFC LABEL cho Background-Pattern
            → Label STOPS INQUIRY: "I know this codebase" = done searching

      ③ "UNKNOWN KNOWNS" = BACKGROUND-PATTERN QUADRANT
        → Background-Pattern §2.2: Low Depth × High Link Density quadrant
          = INVISIBLE BUT PERVASIVE
        → Each debugging event = Low depth per event
        → 10 years × daily = HIGH link density across all chunks
        → PFC cannot target (no single memory to recall)
        → = EXACTLY what author describes: "passively there, informing
          actions and decisions"

      ④ TRANSFER KHÁC VÌ COMPILATION = PERSONAL
        → Chunk §1.1: NO SOURCE TAG — PFC cannot trace chunk origin
        → Compilation = YOUR body, YOUR experience, YOUR specific codebase
        → Written knowledge = PFC-level labels pointing to chunks
        → But labels ≠ chunks themselves (Chunk §6.1: label = retrieval path)
        → = Author: "human would have to write many millions of words,
          still wouldn't capture everything"

    EVIDENCE:
      🟢 Habituation: Thompson & Spencer 1966
      🟢 Expert intuition = pattern recognition: Klein 1998
      🟢 Spreading activation: Collins & Loftus 1975
      🟢 Gist extraction in sleep: Payne 2009, Stickgold 2013
      🟢 Expert chunking: Chase & Simon 1973
      🟡 Background-Pattern 2D model: framework synthesis
      🟡 7 reasons PFC invisible: framework synthesis

    FIT QUALITY: ⭐ STRONG
      → Framework explains BOTH "unknown knowns" AND "why transfer fails"
      → Framework explains WHY author's fn3 examples work the way they do
      → NOT ép: author's observations = independent confirmation of mechanism


  ════════════════════════════════════════════════════════
  GAP B ↔ FAILURE TO COMPILE (NOT "DECLINE")
  ════════════════════════════════════════════════════════

    FILES:
      Compile-Taxonomy.md v3.0 §1.1, §4.1 (primary)
      PFC-Operations.md v1.3 §2, §9 (PFC budget)
      Chunk.md v3.0 §9.1 (expert vs beginner)

    MECHANISM (chi tiết):

      ① EXPERIENCE COMPILE = ONLY WAY TO BUILD EXPERT PATTERNS
        → Compile-Taxonomy §4.1: Experience Compile = Compile Engine +
          minimal modulators (direct exposure)
        → "Thuần engine" — body trải nghiệm → body tự wire → chunk forms
        → Developer solving bug DIRECTLY: neurons fire specific pattern
          → Hebbian strengthen → compiled chunk [bug pattern → fix approach]
        → ~90% behavior = Experience compiled patterns firing automatically
        → 🟢 Ericsson 1993: deliberate practice, 🟢 Chase & Simon 1973

      ② DELEGATION = REMOVING THE EXPERIENCE LOOP
        → AI solves → dev reads explanation → "yeah makes sense" → commit
        → Dev's body DID NOT FIRE problem-solving neurons
        → No co-firing → no Hebbian strengthening → no new chunk compiled
        → = NOT "skill loss" but "skill NON-ACQUISITION"
        → Author's fn6 ĐÚNG: "skill itself doesn't degrade that quickly"
        → Framework AGREES: compiled chunks resist decay (Chunk §5.4)
        → Problem = NEW chunks aren't forming → gap between codebase
          evolution and developer's compiled patterns WIDENS over time

      ③ "BRAIN FOG" = PFC OVERLOAD WITHOUT COMPILED SUPPORT
        → Chunk §9.1: Expert = PFC holds META-CHUNKS (each slot = vast info)
        → Without compiled meta-chunks → PFC holds SMALL chunks → overloaded
        → PFC-Operations §9: PFC budget = finite SHARED resource
        → Without compiled patterns doing automatic processing →
          PFC must handle EVERYTHING as fresh → budget exhausts → "fog"
        → = NOT mysterious "decline" but predictable ARCHITECTURE outcome

      ④ DOWNSTREAM: NO COMPILED BASELINE → NO BODY-FEEDBACK
        → Body-Feedback-Precondition §3.1: Precondition-2 = CHUNK-SUBSTRATE
        → Without compiled chunks → cannot form gap about domain
        → Cannot generate prediction-delta → no "something's off"
        → = Developer who delegated for 2 years → reviews code →
          CANNOT "smell" that something's wrong → vì baseline CHƯA compile
        → Links directly to Gap D

    EVIDENCE:
      🟢 Hebbian learning: Hebb 1949
      🟢 Deliberate practice = expertise: Ericsson et al. 1993
      🟢 Expert chunking 50,000+: Chase & Simon 1973
      🟢 Working memory ~4±1: Cowan 2001
      🟢 PFC top-down amplification: Miller & Cohen 2001
      🟡 "Failure to compile" reframe: framework synthesis
      🟡 PFC budget = finite shared: framework synthesis (from established components)

    FIT QUALITY: ⭐⭐ VERY STRONG
      → Framework PREDICTS author's exact observations:
        - Skill doesn't decay quickly ✓ (compiled chunks resistant)
        - "Brain fog" when working without AI ✓ (PFC overload)
        - Easy to delegate ✓ (delegation = zero body-cost)
      → REFRAME adds value: "failure to compile" is ACTIONABLE
        (you can choose to manually solve SOME problems to maintain compilation)
      → Author would likely find reframe ILLUMINATING because it
        reconciles fn6's two observations (skill stays + fog happens)


  ════════════════════════════════════════════════════════
  GAP C ↔ MULTI-MODAL BODY-BASE vs SEQUENTIAL PFC OUTPUT
  ════════════════════════════════════════════════════════

    FILES:
      Chunk.md v3.0 §1.2, §6.1-§6.2 (primary)
      Body-Base.md v4.0 §1
      Core-Software.md v3.0 §1.2

    MECHANISM (chi tiết):

      ① CHUNKS = MULTI-MODAL FROM BIRTH
        → Chunk §1.2: chunk "mẹ" = mặt + giọng + ôm + ấm → fire as ONE
        → Developer's codebase knowledge = visual (code structure) +
          motor (typing patterns) + emotional (frustration at bugs) +
          temporal (sequence of changes) + social (team discussions)
        → ALL bound in single chunk via Hebbian co-firing
        → 🟢 Distributed representations: Rumelhart & McClelland 1986

      ② LABELS ≠ CHUNK CONTENT
        → Chunk §6.1: Label = retrieval PATH to chunk, NOT content
        → "Moderate Whorfian" (§6.2): words shape ACCESS, not content
        → Writing knowledge down = extracting LABELS + PFC-level description
        → But multi-modal body-level compiled patterns CANNOT be captured
        → = Author: "Words are not a great representation"
        → Framework adds WHY: because words are labels (single-modal,
          sequential) pointing to chunks (multi-modal, parallel)

      ③ ARCHITECTURE GAP: PFC ~4±1 SEQUENTIAL vs BODY-BASE PARALLEL
        → Compile-Taxonomy §2 ①: PFC ~4±1 slots = physics limit
        → Body-base: compiled patterns fire in PARALLEL (no slot limit)
        → Text = PFC output channel = sequential, slot-limited
        → Body-base expertise = parallel, multi-modal, unlimited patterns
        → Even infinite context window = still TEXT (sequential, single-modal)
        → = Limitation is ARCHITECTURAL (body-base vs PFC), not quantitative

    EVIDENCE:
      🟢 Multi-modal binding: Stein & Meredith 1993
      🟢 Working memory ~4±1: Cowan 2001
      🟢 Expert chunking: Chase & Simon 1973
      🟢 Distributed representations: Rumelhart & McClelland 1986
      🟡 Architectural limitation framing: framework synthesis

    FIT QUALITY: 🟡 MODERATE-STRONG
      → Framework EXPLAINS author's observation ("embedding vectors")
      → Author already CLOSE to this insight → framework REFINES, not discovers
      → ⚠️ RISK: author might feel "I already said this" since
        "embedding vectors" comparison already implies multi-dimensionality
      → BEST USE: support point for Gap D argument, not standalone


  ════════════════════════════════════════════════════════
  GAP D ↔ BODY-FEEDBACK PRECONDITIONS (ASSUMPTIONS WITHOUT BODY-CHECK)
  ════════════════════════════════════════════════════════

    FILES:
      Body-Feedback-Precondition.md v1.0 §1, §3, §4 (primary)
      Chunk.md v3.0 §8.4, §8.5
      Background-Pattern.md v2.0 §7

    MECHANISM (chi tiết):

      ① BODY-FEEDBACK = 5 PRECONDITIONS AND-GATE
        → Body-Feedback-Precondition §1.1: signal fires WHEN AND ONLY WHEN
          all 5 preconditions simultaneously met
        → KEY preconditions cho Gap D:
          Precondition-2 (CHUNK-SUBSTRATE): need compiled chunks to decode
          Precondition-3 (DELTA-GATE): VTA detect change > threshold

      ② EXPERIENCED DEVELOPER = ALL PRECONDITIONS MET
        → Precondition-2 MET: years of experience → rich compiled chunks
          for this codebase → can DECODE any input
        → Precondition-1 MET: active problem = directed gap
        → Precondition-3 MET: assumption VIOLATES compiled baseline →
          VTA fires prediction error → dopamine alert
        → Body-feedback signal: "something's off" (pre-verbal)
        → Chunk §8.5: Multi-Weak-Signal-Convergence gradient:
          ① Body Signal → ② Emotion → ③ Gut Feeling → ④ Intuition
          → Expert developer operates at ③-④: many compiled chunks
          fire simultaneously → convergence → accurate "gut feeling"
        → Developer: "Wait, that assumption doesn't feel right..." →
          investigates → finds wrong assumption

      ③ AI AGENT = PRECONDITION-2 STRUCTURALLY FAILS
        → Agent has NO compiled baseline for THIS specific codebase
        → Agent processes text tokens → statistical patterns → generates response
        → No body → no Hebbian compilation → no chunk-substrate
        → Precondition-2 fail → Precondition-1 cannot form domain-specific gap
        → Precondition-3 impossible: no baseline → no delta to detect
        → Agent makes assumption → NO body-feedback signal fires
        → Agent CANNOT distinguish right from wrong assumption
          BECAUSE THE ARCHITECTURE FOR DISTINCTION DOESN'T EXIST
        → = Author fn5: "I don't think they have a way, even in
          principle" → CORRECT — the way IS body-feedback,
          which requires body + compiled baseline

      ④ REFRAME: NOT "BAD" ASSUMPTIONS BUT "UNCHECKED" ASSUMPTIONS
        → Agent's assumptions are often STATISTICALLY CORRECT
          (trained on vast data → good pattern matching)
        → But when assumption HAPPENS TO BE WRONG → no signal
        → Human developer's assumptions are also often wrong
          → BUT body-feedback signals CATCH some of them
        → Difference = NOT reasoning quality but CHECKING mechanism
        → = Author's "fundamental trade-off" reframed:
          Not "accuracy vs speed" but "has body-check vs doesn't"

      ⑤ CONNECTS TO ANTHONYC COMMENT (179pts):
        → AnthonyC suggests: fine-tune on codebase → knowledge in weights
        → Framework prediction: fine-tuning improves pattern MATCHING
          (better statistical model of codebase) but NOT body-level
          EVALUATION (no prediction-delta mechanism)
        → Fine-tuned model: better at "what usually happens here"
        → Still no: "something feels wrong about this"
        → = Functional improvement, but architecturally DIFFERENT
          from human compiled baseline + body-feedback

    EVIDENCE:
      🟢 VTA prediction error: Schultz 1997
      🟢 Somatic marker hypothesis: Damasio 1994
      🟢 Expert intuition = pattern recognition: Klein 1998
      🟢 Expert chunk patterns: Chi et al. 1981
      🟢 Hedonic adaptation (habituation): Cabanac 1971
      🟡 5 Preconditions AND-gate: framework synthesis
      🟡 "Assumptions without body-check": framework reframe

    FIT QUALITY: ⭐⭐ VERY STRONG — BEST CANDIDATE FOR COMMENT
      → Directly addresses author's fn5 "even in principle" question
      → Provides MECHANISM where author sees only observation
      → Reframe is NOVEL: "unchecked" not "bad" = new angle
      → Testable: predicts fine-tuning improves matching but not catching
      → Connects to highest-voted comment (AnthonyC, 179pts)
      → Audience = LW tech-rationalist → mechanism argument = high value


  ════════════════════════════════════════════════════════
  TỔNG HỢP — MAPPING QUALITY RANKED
  ════════════════════════════════════════════════════════

    ┌────┬─────────────────┬────────────────┬──────────────────────────┐
    │ #  │ MAPPING         │ FIT QUALITY    │ ĐẶC ĐIỂM                │
    ├────┼─────────────────┼────────────────┼──────────────────────────┤
    │ D  │ Body-feedback   │ ⭐⭐ VERY STRONG │ Novel reframe, testable, │
    │    │ preconditions   │                │ addresses fn5 directly   │
    ├────┼─────────────────┼────────────────┼──────────────────────────┤
    │ B  │ Failure to      │ ⭐⭐ VERY STRONG │ Reconciles fn6, predicts │
    │    │ compile         │                │ author's exact obs       │
    ├────┼─────────────────┼────────────────┼──────────────────────────┤
    │ A  │ Background-     │ ⭐ STRONG       │ Explains "unknown knowns"│
    │    │ Pattern         │                │ mechanism, but broad     │
    ├────┼─────────────────┼────────────────┼──────────────────────────┤
    │ C  │ Multi-modal vs  │ 🟡 MOD-STRONG  │ Author already close,    │
    │    │ sequential      │                │ framework refines only   │
    └────┴─────────────────┴────────────────┴──────────────────────────┘

  ⚠️ KHÔNG CÓ ÉP:
    → Tất cả 4 mappings = framework BỔ SUNG mechanism cho observation
    → Không mapping nào CONTRADICTS author
    → Gap C = weakest fit (author already close) → có thể drop nếu comment quá dài
    → Gap D + B = strongest combination cho 1 comment
```

---

## §5 — DỰ ĐOÁN GÌ? (Drill Question ④)

```
  ⭐ Phase 2 — FILLED (2026-06-07)


  ════════════════════════════════════════════════════════
  PREDICTION 1 — COMPILATION GAP: DELEGATION → DETECTABLE INTUITION DEFICIT
  ════════════════════════════════════════════════════════

    IF compilation-requires-experience is correct:

    PREDICTION:
      Developers who heavily delegate problem-solving to AI for 2-3 years
      will show MEASURABLY LOWER "anomaly detection" in novel situations
      compared to developers who solved equivalent problems manually.

    SPECIFIC TEST:
      → Present both groups with a codebase containing a SUBTLE
        architectural issue (not a pattern in training data)
      → Measure: time to first "something seems wrong" signal
      → AI-heavy group: slower to detect (lack compiled baseline)
      → Manual group: faster gut-level detection (compiled patterns fire)
      → Difference should be LARGEST for anomalies NOT in documentation
        (i.e., things that require body-level "smell")

    FALSIFICATION:
      → If AI-heavy juniors detect anomalies at EQUIVALENT rates
        after same years → compilation model WRONG or INSUFFICIENT
      → Specifically: if delegation + reading AI explanations =
        sufficient for building anomaly-detection intuition,
        then Experience Compile is NOT required (observation alone
        could suffice)

    CONFIDENCE: 🟡 Framework prediction — testable but not yet tested
    LW RELEVANCE: HIGH — directly connects to author's "cognitive decline"
      concern with a specific, measurable prediction


  ════════════════════════════════════════════════════════
  PREDICTION 2 — CONTEXT WINDOW ≠ BODY-FEEDBACK
  ════════════════════════════════════════════════════════

    IF tacit-knowledge-is-compiled (body-level, not text-level):

    PREDICTION:
      Even with 10-100M token context windows + full codebase history,
      agents will STILL miss a specific CLASS of errors: violations
      of implicit constraints that experienced devs catch via
      "something's off" feeling.

    SPECIFIC TEST:
      → Characterize errors caught by senior devs during code review
      → Separate into 2 categories:
        (a) Pattern-matchable: documented constraints, style violations,
            known anti-patterns → agent SHOULD catch these
        (b) Body-feedback-dependent: violations of unwritten norms,
            "this technically works but feels wrong", subtle architectural
            mismatch → agent SHOULD MISS these disproportionately
      → If model correct: agents improve dramatically on (a) with
        more context but plateau on (b) regardless of context size

    FALSIFICATION:
      → If massive context windows close the gap on BOTH categories
        equally → body-feedback distinction is WRONG
      → If agents catch (b)-type errors at senior dev rates with
        enough context → "something's off" is text-recoverable
        after all, and body-feedback model overstates body requirement

    CONFIDENCE: 🟡 Framework prediction — strongest of the 3
    LW RELEVANCE: VERY HIGH — directly testable by audience members
      who use coding agents daily. Author himself could verify from
      his experience with Copilot + Claude Code.


  ════════════════════════════════════════════════════════
  PREDICTION 3 — FINE-TUNING ≠ COMPILATION
  (Responds to AnthonyC comment, 179pts)
  ════════════════════════════════════════════════════════

    IF body-feedback model is correct:

    PREDICTION:
      Fine-tuning a model on a specific codebase (AnthonyC's suggestion)
      will improve pattern-MATCHING accuracy but NOT anomaly-CATCHING
      rate for implicit constraint violations.

    SPECIFIC TEST:
      → Fine-tune model on codebase X with full history
      → Test on 2 types of issues:
        (a) Pattern-matching: "based on this codebase's history,
            what's the likely approach here?" → IMPROVE with fine-tuning
        (b) Anomaly-catching: "does this new code violate unwritten
            norms of this codebase?" → NO SIGNIFICANT IMPROVEMENT
      → Fine-tuning = better statistical model (weights ≈ patterns)
      → But weights ≠ body-feedback signal architecture
      → = Better "what usually happens" but not better
        "something feels wrong about this"

    FALSIFICATION:
      → If fine-tuned models catch anomalies at rates comparable
        to experienced devs → body-feedback distinction WRONG
      → Specifically: if weights can functionally replicate
        "something's off" signal → then body is NOT architecturally
        necessary, and FUNCTIONAL EQUIVALENCE without body suffices

    CONFIDENCE: 🟡 Framework prediction — most debatable
    LW RELEVANCE: HIGH — directly responds to top comment,
      makes falsifiable claim about an approach many people endorse

    ⚠️ HONEST NOTE: This is the prediction MOST LIKELY TO BE WRONG.
      Functional equivalence is a serious counter-argument.
      Fine-tuning may achieve "good enough" anomaly detection
      through purely statistical means. Framework predicts it
      won't FULLY replicate body-feedback, but "fully" is a
      high bar — "mostly" might be sufficient for practical purposes.


  ════════════════════════════════════════════════════════
  PREDICTIONS SUMMARY — CHO COMMENT
  ════════════════════════════════════════════════════════

    STRONGEST for comment: Prediction 2 (context window ≠ body-feedback)
      → Most testable by audience
      → Connects to author's main argument (context = biggest issue)
      → Makes specific, falsifiable claim about a measurable difference

    SUPPORT: Prediction 1 (compilation gap)
      → Adds depth to "cognitive decline" discussion
      → But harder to test (longitudinal, confounding variables)

    USE CAREFULLY: Prediction 3 (fine-tuning ≠ compilation)
      → High engagement potential (responds to top comment)
      → But also highest risk of being wrong
      → Best as "interesting to test" not "I predict this is true"
```

---

## §6 — FRAMEWORK CÓ THỂ SAI Ở ĐÂU? (Drill Question ⑤)

```
  ⭐ Phase 2 — FILLED (2026-06-07)


  ════════════════════════════════════════════════════════
  WEAKNESS 1 — FUNCTIONAL EQUIVALENCE (STRONGEST COUNTER)
  ════════════════════════════════════════════════════════

    CHALLENGE:
      Framework claims body-feedback (biological) is ESSENTIAL for
      expert-level evaluation. But AI could develop FUNCTIONAL
      EQUIVALENT without biological body.

    DETAIL:
      → AI attention/weighting mechanisms MIGHT replicate
        "something's off" signal through purely statistical means
      → If AI's internal confidence calibration achieves SAME
        practical effect as human body-feedback → framework's
        body-requirement claim is TOO STRONG
      → This is principled, not just empirical: if the FUNCTION
        is what matters (detecting anomalies), not the SUBSTRATE
        (biological body), then body is unnecessary

    FRAMEWORK POSITION:
      → Framework predicts functional equivalence is INCOMPLETE:
        body-feedback integrates multi-modal compiled experience
        in ways that statistical pattern-matching cannot fully replicate
      → But "cannot fully" ≠ "cannot at all"
      → If 90% functional equivalence is achievable → framework's
        practical relevance is limited even if theoretically correct

    HONEST ASSESSMENT: This is the MOST SERIOUS weakness.
      Framework might be TECHNICALLY correct (body-feedback is distinct)
      but PRACTICALLY irrelevant (AI achieves close enough results).

    HOW TO HANDLE IN COMMENT:
      → Acknowledge explicitly: "This is an empirical question"
      → Frame prediction as testable, not as certain
      → If proven wrong → framework learns something valuable


  ════════════════════════════════════════════════════════
  WEAKNESS 2 — FINE-TUNING AS COMPILATION ANALOG
  ════════════════════════════════════════════════════════

    CHALLENGE:
      AnthonyC (179pts — LW community endorsed):
      "Fine-tune on codebase → tacit knowledge in weights"
      → If weights ≈ functional chunks → fine-tuning ≈ compilation
      → Challenges claim that compilation must be personal/embodied

    DETAIL:
      → Weights trained on codebase DO capture statistical patterns
      → These patterns ARE "knowledge" in a meaningful sense
      → If fine-tuned model catches anomalies experienced devs catch
        → then "knowledge in weights" IS sufficient
      → Framework would need to explain WHY weights ≠ compiled chunks
        at a level beyond "different substrate"

    FRAMEWORK POSITION:
      → Weights = pattern-statistical (trained on text)
      → Compiled chunks = multi-modal body-calibrated (trained on doing)
      → KEY DIFFERENCE: compiled chunks generate body-FEEDBACK signals
        when violated. Weights generate probability distributions.
      → Probability distribution CAN flag low-probability outputs
      → But: body-feedback is EVALUATIVE (this feels wrong)
        vs statistical (this is unlikely) → different signal types
      → Question is: does the DIFFERENCE between these matter in practice?

    HONEST ASSESSMENT: Genuinely uncertain.
      Fine-tuning MIGHT be "good enough" for most practical purposes.
      Framework predicts residual gap, but gap might be small.


  ════════════════════════════════════════════════════════
  WEAKNESS 3 — SCALE MIGHT OVERCOME ARCHITECTURE
  ════════════════════════════════════════════════════════

    CHALLENGE:
      Author's Bull Case: enough context + continual learning might
      solve ALL the problems listed, including "unknown knowns."
      → If 100M token windows + company knowledge base + agent memory
        effectively replicate "theory of the code" → architecture
        argument weakens

    DETAIL:
      → Massive context could substitute for body-level knowledge
        IF enough information is made explicit
      → Companies that systematically document everything might
        create context sufficient for agents
      → Author himself notes this: "once coding agents get continual
        learning, they may be able to persist such things on their own"
      → If true → the PRACTICAL bottleneck is documentation quality,
        not architectural limitation

    FRAMEWORK POSITION:
      → Framework predicts this approach hits a CEILING:
        some knowledge CANNOT be made explicit (Background-Pattern
        §5: PFC invisible → cannot articulate → cannot document)
      → But ceiling might be high enough for practical purposes
      → 95% of "unknown knowns" might be documentable with effort
      → The last 5% might matter most (edge cases, critical bugs)
        or might not matter at all (good enough for shipping)

    HONEST ASSESSMENT: Framework predicts ceiling exists.
      But whether ceiling matters depends on domain and use case.
      For safety-critical code: ceiling matters. For CRUD apps: maybe not.


  ════════════════════════════════════════════════════════
  WEAKNESS 4 — FRAMEWORK = HUMAN COGNITION MODEL, NOT AI MODEL
  ════════════════════════════════════════════════════════

    CHALLENGE:
      Framework describes HUMAN cognitive architecture.
      Applying it to explain AI LIMITATIONS is an INFERENCE,
      not a direct finding.

    DETAIL:
      → Framework is built to explain human body-brain system
      → Saying "AI can't do X because AI lacks body" is
        framework-centric reasoning
      → AI might achieve X through COMPLETELY DIFFERENT mechanism
        that framework doesn't model
      → Absence of body-feedback in AI ≠ absence of anomaly detection
        in AI. Different architecture might find different paths.

    FRAMEWORK POSITION:
      → Framework predicts WHAT specifically AI will miss (body-check)
      → If AI finds different path to same result → framework claim
        about body-requirement is falsified
      → But framework's DESCRIPTION of what "unknown knowns" are
        and HOW they work in humans remains valid regardless

    HONEST ASSESSMENT: This weakness limits framework's PREDICTIVE power
      about AI, not its DESCRIPTIVE power about humans.
      Comment should focus on "here's what's happening in human experts"
      (descriptive, strong) not "AI can never do this" (predictive, weak).


  ════════════════════════════════════════════════════════
  SUMMARY — HONEST POSITION FOR COMMENT
  ════════════════════════════════════════════════════════

    STRONG CLAIMS (safe for comment):
      → Human expertise involves compiled body-level patterns
        invisible to conscious reflection = well-supported
      → Delegation removes the experience loop that builds these
        patterns = logically follows from compilation model
      → The "something's off" signal in experienced devs is
        architecturally grounded, not magical = specific mechanism

    QUALIFIED CLAIMS (frame as "interesting to test"):
      → AI cannot replicate body-feedback through statistical means
        = testable prediction, may be wrong
      → Fine-tuning ≠ compilation = strongest version may be too
        strong, weaker version ("fine-tuning is incomplete") more
        defensible

    AVOID IN COMMENT:
      → "AI will NEVER..." = too strong, framework doesn't support
      → "Body is ESSENTIAL..." = may be wrong (functional equivalence)
      → "This is proven..." = framework is synthesis, not established

    TONE:
      → "Here's a possible mechanism that would explain what
        you're observing, and here's how we could test it"
      → NOT: "Here's why AI can't do X"
```

---

> **Phase hiện tại: 2 DRILL — DONE (2026-06-07)**
> **Phase tiếp: 3 SYNTHESIZE → chọn 1-2 điểm mạnh nhất → mainstream language → comment**
> **Top candidates: Gap D (body-check) + Gap B (failure to compile)**
