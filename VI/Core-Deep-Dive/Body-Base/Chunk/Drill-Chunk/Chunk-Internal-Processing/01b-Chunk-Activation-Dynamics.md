---
title: 01b — Chunk Activation Dynamics (Core Mechanism)
created: 2026-04-17 (N+7 session — plan adjustment)
status: DRILLED v1.0
scope: CORE — Probabilistic activation, competitive re-linking, trigger surface
purpose: |
  Formalize 3 core chunk mechanisms that underlie ALL chunk operations:
  ① Activation probability distribution (how chunks fire)
  ② Competitive re-linking (how chunks change)
  ③ Trigger surface (why some chunks fire more than others)
  These mechanisms are FOUNDATIONAL — used by F1, F3, F4, and all downstream.
  Emerged from user insight during N+7 session. Plan adjusted to include.
parent: 00-Internal-Mechanism-Overview.md (cross-cutting, not specific to 1 thread)
dependencies:
  - 01-Chunk-Connection-Logical.md (4-type connection taxonomy)
  - 03-Chain-Anchor-Decay.md (anchor = retrieval path, decay)
  - Schema/Chunk.md (current DRAFT — this file extends significantly)
  - F1 NT1 (gradient, strength-weighted)
  - F1 NT7 (body-state-at-compile, 3 update paths)
  - Neural-Processing-Flow.md (hardware substrate)
plan_note: |
  File thêm vào F4 do plan adjustment (domain real > plan).
  User insight identified gap: probability mechanism chưa formalize.
  Content = CHUNK CORE, cross-cutting. Target for Chunk.md v2.0 rewrite after 99-Master.
language: Tiếng Việt primary + English technical
---

# 01b — Chunk Activation Dynamics

> **File này formalize 3 cơ chế CORE** mà chunk system vận hành.
> Không thuộc riêng thread nào — cross-cutting cho toàn bộ framework.
> Emerged từ user insight: "chunk không bị xóa, chỉ có thể suy thoái,
> hoặc bị override, hoặc trigger lại chunk sau đó tạo pattern link mới."

---

## §1 — Tại sao file này cần thiết

```
FRAMEWORK HIỆN TẠI ĐÃ CÓ:
  ✅ Chunks không bị xóa (Chunk.md §2, F1 NT1)
  ✅ Reconsolidation window (Chunk.md §2, Nader 2000)
  ✅ 3 update paths (F1 NT7: re-associate / novelty hijack / therapy)
  ✅ 4 compile mechanisms (F1 NT2)
  ✅ Spreading activation (Collins & Loftus 1975)
  ✅ 4 connection types (F4 01)
  ✅ Anchor = retrieval path (F4 03)

FRAMEWORK CHƯA FORMALIZE:
  ❌ HOW activation distributes across multiple links (probability)
  ❌ HOW new links COMPETE with old links (mechanism)
  ❌ WHY some chunks have higher random trigger rates (trigger surface)
  ❌ HOW probability shifts over time (dynamics)

  → Thiếu phần này = thiếu cơ chế VẬN HÀNH cơ bản nhất
  → = Biết chunks connect (01), biết chunks decay (03)
  → = Nhưng CHƯA biết: khi trigger → activation đi ĐÂU, bao NHIÊU, tại SAO
```

---

## §2 — Activation Probability Distribution

### §2.1 — Core mechanism

```
🟡 FRAMEWORK SYNTHESIS from established neuroscience:

KHI CHUNK X ĐƯỢC TRIGGER (bởi PFC hold hoặc sensory input):

  ① Chunk X fires → neurons trong pattern X activate
  ② Spreading activation propagates OUTWARD theo TẤT CẢ links
  ③ Mỗi link có STRENGTH khác nhau (Hebbian: dùng nhiều = mạnh)
  ④ Activation PHÂN BỔ theo strength:

  ┌─────────────────────────────────────────────────────────────┐
  │                                                             │
  │  Chunk X fires                                              │
  │     │                                                       │
  │     ├── 40% activation → Chunk A (link mạnh: nhiều lần,     │
  │     │                              gần đây, multi-modal)    │
  │     ├── 25% activation → Chunk B (link trung bình)          │
  │     ├── 15% activation → Chunk C (link trung bình)          │
  │     ├── 10% activation → Chunk D (link yếu: cũ, ít dùng)   │
  │     ├──  5% activation → Chunk E (link rất yếu)             │
  │     └──  5% activation → scattered (noise, sub-threshold)   │
  │                                                             │
  │  → Chunk A: most likely to fire (highest activation)        │
  │  → Chunk D-E: unlikely to fire (below threshold usually)    │
  │  → = PROBABILITY distribution, not binary on/off            │
  │                                                             │
  └─────────────────────────────────────────────────────────────┘

  ⭐ KHÔNG PHẢI BINARY (fire / not fire):
  → Mỗi connected chunk nhận MỘT LƯỢNG activation
  → Chunk nào nhận ĐỦ activation (vượt threshold) → fires
  → Chunk nào nhận KHÔNG ĐỦ → partial activation (có thể contribute to H5
    multi-weak-signal convergence nhưng không fire riêng lẻ)

  → = "Khi nghĩ về X, hầu hết tôi nghĩ đến A"
  → = Không phải X→A là link DUY NHẤT
  → = Mà X→A là link MẠNH NHẤT → most probable activation

  🟢 EVIDENCE BASE:
  → Spreading activation = probability-weighted (Collins & Loftus 1975)
  → Neural activation follows graded response (not all-or-nothing at network level)
  → Priming studies: stronger associations → faster/more probable activation
    (🟢 Meyer & Schvaneveldt 1971, 🟢 Neely 1977)
  → Response competition in naming tasks (🟢 Luce 1986 choice theory)
```

### §2.2 — Link strength determinants

```
LINK STRENGTH = f(7 factors):

  ① REPETITION COUNT:
     → Bao nhiêu lần X và A fire cùng nhau
     → 🟢 Hebbian learning (Hebb 1949): "fire together, wire together"
     → More repetitions → stronger link → higher activation probability

  ② RECENCY:
     → Lần cuối X→A fire là bao lâu trước
     → Recent use → temporarily BOOSTED (🟢 recency effect)
     → Long unused → WEAKENED (but not deleted)
     → = Ebbinghaus decay applied to LINK STRENGTH (F4 03 §4.1)

  ③ EMOTIONAL WEIGHT AT COMPILE:
     → Link compiled under emotional peak → EXTRA STRONG
     → Amygdala tagging → accelerated Hebbian binding
     → = F1 NT2 channel 2: emotional peak compile
     → 1 lần trauma CÓ THỂ tạo link mạnh hơn 100 lần repetition neutral

  ④ MULTI-MODAL RICHNESS:
     → Link spanning nhiều modalities → more neurons involved → stronger
     → Visual + auditory + somatic + emotional → maximally strong
     → = F1 NT2 channel 3: multi-modal compile

  ⑤ CONTEXT MATCH:
     → Current context similar to compile context → link BOOSTED
     → 🟢 Context-dependent memory (Godden & Baddeley 1975)
     → = In school → school-compiled links boosted
     → = Context = temporary probability modifier

  ⑥ EMOTIONAL STATE MATCH:
     → Current emotional state similar to compile state → link BOOSTED
     → 🟢 Mood-congruent memory (Bower 1981)
     → = Đang sợ → fear-compiled links boosted → "thấy nguy hiểm khắp nơi"
     → = Emotional state = temporary probability modifier (bias)

  ⑦ ANCHOR STRENGTH:
     → Active anchor (verbal label, ritual, context) → link MAINTAINED
     → Weak/no anchor → link gradually DECAYS (F4 03 §4)
     → = Anchor = retrieval path maintenance mechanism


⭐ FACTORS INTERACT MULTIPLICATIVELY (not additively):

  → High repetition + high emotion + multi-modal + anchored
    = EXTREMELY strong link (nearly permanent)
    = Ví dụ: tên mẹ, địa chỉ nhà, skill lái xe

  → Low repetition + no emotion + single modal + no anchor
    = EXTREMELY weak link (rapid decay)
    = Ví dụ: số điện thoại nghe 1 lần rồi quên

  → High emotion + low repetition + no anchor
    = STRONG initially but DECAYING (trauma without processing)
    = Chunk tồn tại lâu dài, link cụ thể dần yếu nhưng rất chậm
```

### §2.3 — Probability is DYNAMIC (not static)

```
⭐ CRITICAL INSIGHT: Distribution shifts over time

PROBABILITY DISTRIBUTION THAY ĐỔI LIÊN TỤC:

  T=0 (just after trauma event):
    Chunk [chó] fires →
      85% → [cắn, đau, sợ] (just compiled, emotional peak, multi-modal)
      10% → [lông, mềm] (neutral associations from before)
       5% → [scattered noise]

  T=1 year (avoidance, no new experience):
    Chunk [chó] fires →
      70% → [cắn, đau, sợ] (slightly decayed but no competition)
      15% → [lông, mềm] (relatively stronger now)
      15% → [scattered + new weak associations]

  T=2 years (after exposure therapy + positive dog experiences):
    Chunk [chó] fires →
      30% → [cắn, đau, sợ] (old links still exist but relatively weaker)
      45% → [vuốt ve, ấm, an toàn] (NEW links, recent, repeated, multi-modal)
      15% → [lông, mềm] (neutral, stable)
      10% → [scattered]

  → OLD LINKS NEVER DELETED — chỉ TƯƠNG ĐỐI yếu hơn
  → NEW LINKS GROW → chiếm ngày càng nhiều probability share
  → = PROBABILITY SHIFT, not replacement
  → = Cơ chế nền tảng của: learning, therapy, adaptation, growth
```

---

## §3 — Competitive Re-linking

### §3.1 — Competition mechanism

```
🟡 FRAMEWORK SYNTHESIS — how new links COMPETE with old links:

KHÔNG PHẢI "XÓA LINK CŨ, THAY LINK MỚI":
  → Neural substrate KHÔNG có mechanism "unwire on demand"
  → Chunk.md §2: "Không ai xóa được chunk"
  → F1 NT1: chunks only strengthen/weaken, never delete

MÀ LÀ "LINK MỚI CẠNH TRANH VỚI LINK CŨ":

  MECHANISM:

  ① NEW LINK FORMATION:
     Chunk X encounters new context/experience
     → New association X→F forms (via any of 4 compile mechanisms)
     → F = new chunk linked to X
     → Link X→F starts WEAK (new, few repetitions)

  ② STRENGTHENING:
     X→F repeated in new context → link strengthens
     → Each repetition → Hebbian: X→F connection GROWS
     → Multi-modal experience → X→F DEEPENS

  ③ RELATIVE WEAKENING OF OLD:
     Old link X→A not being used as often (if context changed)
     → X→A link DECAYS (Ebbinghaus, no rehearsal)
     → ⚠️ X→A does NOT decay because X→F exists
     → X→A decays because X→A is NOT BEING USED
     → = Independent decay, not caused by competition
     
     BUT: there IS direct competition:
     → When X fires → finite activation to distribute
     → X→F takes activation share → X→A gets LESS
     → = Lateral inhibition at network level
     → 🟢 Lateral inhibition (Hartline 1949, applied to cognitive networks)
     → 🟢 Retrieval-induced forgetting (Anderson et al. 1994):
       retrieving X→F actually SUPPRESSES X→A temporarily

  ④ PROBABILITY CROSSOVER:
     At some point: P(X→F) > P(X→A)
     → New pathway DOMINATES body signal
     → Old pathway still fires but MINORITY signal
     → PFC experience: "bình thường / tích cực" (dominant) với "hơi sợ" (minority)
     → = "Vẫn hơi sợ chó nhưng không panic nữa"

  ⑤ STABILIZATION:
     New pathway continues strengthening → old pathway continues weakening
     → Eventually: old pathway fires so weakly → mostly sub-threshold
     → But NEVER fully gone → stress/fatigue/context can REACTIVATE
     → = "Tái phát khi mệt" = PFC weakened → old pathway temporarily wins
     → 🟢 Stress-induced relapse (Sinha 2001): stress reactivates old patterns
```

### §3.2 — Reconsolidation window as competition enabler

```
🟢 ESTABLISHED — Nader et al. 2000:

RECONSOLIDATION = key mechanism for re-linking:

  ① Chunk X recalled (or triggered)
  ② Existing links become TEMPORARILY LABILE (~4-6 hours)
  ③ During this window: NEW associations can be INTEGRATED
  ④ Chunk re-consolidates WITH new associations
  ⑤ = Old links MODIFIED (not deleted) + new links ADDED

WHY THIS MATTERS FOR COMPETITIVE RE-LINKING:

  Without reconsolidation:
    → New links form separately
    → Old links remain unchanged
    → Competition is purely at activation level (probability)
    → = Slow, gradual probability shift

  With reconsolidation:
    → Trigger old chunk → WINDOW OPENS
    → In window: provide NEW experience/context
    → Old links + new links RE-COMPILE TOGETHER
    → = Old links can be MODIFIED (not just competed against)
    → = Faster, more effective probability shift

  ⭐ THIS IS WHY EXPOSURE THERAPY WORKS:

  Step 1: Trigger fear chunk (e.g., show spider) → reconsolidation window opens
  Step 2: In window: safe experience (spider doesn't harm) → new safety link forms
  Step 3: Fear chunk re-consolidates WITH safety association integrated
  Step 4: Next trigger: old fear + new safety BOTH fire → safety gradually wins
  
  → 🟢 Reconsolidation-based therapy (Schiller et al. 2010):
    extinction during reconsolidation window prevents fear return
  → 🟢 More effective than extinction without reconsolidation trigger

  ⚠️ CRITICAL WARNING (from Chunk.md):
  "Recall MÀ KHÔNG modify → chunk STRENGTHEN → TỆ HƠN"
  → Trigger old chunk WITHOUT new positive experience
  → = Rehearsal of old links → old links STRENGTHEN
  → = Re-traumatization, not therapy
  → = Rumination = repeated recall without modification → worsens
  → 🟢 Rumination worsens depression (Nolen-Hoeksema 2000)
```

### §3.3 — 3 re-linking strategies (F1 NT7, extended)

```
F1 NT7 committed 3 update paths. §3 extends with probability mechanism:

STRATEGY 1 — RE-ASSOCIATE (gradual probability shift):
  = Use chunk in positive contexts REPEATEDLY → build new links → shift probability
  
  Mechanism:
    Chunk [chó] + positive experience [vuốt ve, an toàn] → new link forms
    Repeat nhiều lần → new link strengthens → probability shifts
    Old link [chó → sợ] → relatively weaker (not rehearsed + competition)
    
  Speed: SLOW (months-years)
  Depth: MODERATE (new links compete but old links intact)
  Risk: LOW (no direct trigger of old trauma)
  Best for: mild associations, preference changes, habit modification

  → = "Sống tích cực ở context mới" (user's formulation)
  → Each positive experience = one more link pulling probability toward positive
  → Accumulation over time → significant shift


STRATEGY 2 — NOVELTY HIJACK (context-driven probability jump):
  = Novelty-drive context pulls chunk into NEW PURPOSE → rapid re-linking
  
  Mechanism:
    Strong novelty/curiosity → chunk activated IN novelty context
    Dopamine + opioid (novelty rewards) → new link compiles FAST
    = Emotional peak mechanism BUT with positive valence
    → Can match trauma link strength (both use emotional peak compile)
    
  Speed: FAST (when conditions align)
  Depth: DEEP (emotional peak = strong new link)
  Risk: MODERATE (requires right conditions, cannot force)
  Best for: strong associations, redirecting obsessive patterns

  → Example: "ghét toán" chunk → game development interest activates
  → Math chunks re-linked to [game, fun, creative] via novelty
  → Old link [toán → boring/threatening] → relatively weaker


STRATEGY 3 — THERAPY-ASSISTED (reconsolidation-based):
  = Professional trigger + reconsolidation window + guided re-linking
  
  Mechanism:
    Therapist deliberately triggers old chunk (controlled recall)
    → Reconsolidation window opens
    → In window: guided positive/neutral re-processing
    → Chunk re-consolidates WITH new associations
    → = Most direct, most effective for deep trauma

  Specific methods:
    EMDR: bilateral stimulation during recall → reduces emotional intensity
      → 🟢 Shapiro 2001, multiple RCTs
    Somatic Experiencing: body-level processing of trauma chunks
      → 🟡 Levine 1997, growing evidence
    Cognitive Processing Therapy: PFC-level re-framing during window
      → 🟢 Resick et al. 2017
    Exposure + Response Prevention: trigger → no catastrophe → safety link
      → 🟢 Foa & Kozak 1986, gold standard for anxiety

  Speed: MODERATE (weeks-months of sessions)
  Depth: DEEPEST (direct modification of old links)
  Risk: HIGHEST (requires professional — wrong execution = re-traumatize)
  Best for: Level 3-4 trauma (F1 NT7), deep pathological associations

  ⚠️ ALL 3 strategies use SAME underlying mechanism:
  → Build new links → shift activation probability → old links relatively weaker
  → Differ in: speed, depth, risk, required conditions
```

---

## §4 — Trigger Surface

### §4.1 — What is trigger surface

```
🟡 FRAMEWORK CONCEPT — "trigger surface" = attack surface for chunk activation:

DEFINITION:
  Trigger surface = TOTAL NUMBER OF ENTRY POINTS that can activate a chunk.
  
  Entry point = any neuron/pattern that is part of the chunk's network
  AND shared with other active chunks or environmental inputs.

  → More entry points = higher probability of RANDOM activation
  → Fewer entry points = lower probability of random activation
  → = "Bao nhiều cửa vào chunk này?"

ANALOGY:
  Small house (1 door, 2 windows) = few entry points → rarely enters uninvited
  Large building (20 doors, 100 windows) = many entry points → frequently enters
  
  Similarly:
  Simple chunk (1 modality, 1 context) = small trigger surface
  Complex chunk (multi-modal, multi-context, emotional) = LARGE trigger surface
```

### §4.2 — Trigger surface determinants

```
TRIGGER SURFACE SIZE = f(4 factors):

  ① NUMBER OF MODALITIES in chunk:
     → Visual + auditory + somatic + motor + emotional = 5 "cửa vào"
     → Each modality = independent entry point
     → Any matching sensory input in ANY modality → can trigger
     → Multi-modal chunks = LARGE trigger surface

  ② NUMBER OF ASSOCIATED CHUNKS:
     → Chunk connected to 3 other chunks = 3 entry points via Type 1 contamination
     → Chunk connected to 50 other chunks = 50 entry points
     → Well-connected chunks = LARGE trigger surface
     → = "Hub" chunks (central to many schemas) fire more often

  ③ EMOTIONAL INTENSITY at compile:
     → Emotional peak → amygdala tags → BROAD activation during compile
     → Many cortical areas activated simultaneously
     → = More neurons involved = more potential pattern matches with future inputs
     → = Trauma chunks have DISPROPORTIONATELY large trigger surfaces
     → = Expertise chunks ALSO have large trigger surfaces (for same reason: deep compile)

  ④ GENERALITY vs SPECIFICITY of pattern:
     → Very specific pattern (one face, one voice) = FEW matching inputs
     → Very general pattern (any dog, any loud noise) = MANY matching inputs
     → Fear generalization: initially fear SPECIFIC dog → generalizes to ALL dogs
     → 🟢 Fear generalization (Lissek et al. 2008): overgeneralization in anxiety
     → = General patterns = larger trigger surface than specific patterns
```

### §4.3 — Trauma: large trigger surface explained

```
⭐ WHY TRAUMA IS UNIQUELY PERSISTENT (trigger surface analysis):

TRAUMA COMPILE CREATES MAXIMUM TRIGGER SURFACE:

  ① MULTI-MODAL: visual + auditory + somatic + olfactory + emotional
     → Bị chó cắn: thấy chó (visual), nghe sủa (auditory), cảm giác đau (somatic),
       mùi (olfactory), sợ (emotional)
     → = 5+ independent entry points

  ② EMOTIONAL PEAK: amygdala fires maximally → BROAD cortical activation
     → Many neurons recruited during compile → many potential pattern matches
     → = Entry points expanded beyond the original 5 modalities
     → = Anything VAGUELY similar can trigger

  ③ GENERALIZATION: fear extends from specific → general
     → Initially: fear THIS dog (specific)
     → Generalizes: fear ALL dogs, dog sounds, dog shapes, dog-like things
     → 🟢 Stimulus generalization (Pavlov, extensively replicated)
     → = Trigger surface EXPANDS over time after trauma

  ④ MANY ASSOCIATED CHUNKS compiled simultaneously:
     → During trauma: ENTIRE SCENE compiled as interconnected chunks
     → Person, place, time, smell, sound, body state, emotional state
     → = Many chunks created → many cross-links → many entry points
     → = "Ngửi mùi tương tự → toàn bộ trauma scene fires"

  RESULT:
    Trauma multi-chunk = DOZENS of entry points
    → Random daily input → HIGH probability of matching at least 1 entry point
    → = "Lờ mờ sợ cái gì đó mặc dù không biết rõ" (user's formulation)
    → PFC doesn't know WHICH entry point triggered
    → Body just feels: fear/tension/alert
    → = H5 multi-weak-signal in THREAT direction


⭐ CRITICAL PARALLEL — EXPERTISE HAS SAME MECHANISM:

  Expert in domain X:
    → Thousands of chunks compiled over years
    → Multi-modal (seen, done, felt, discussed, read)
    → Deep emotional engagement (passion, curiosity, flow)
    → Many cross-linked chunks
    → = LARGE trigger surface for domain-relevant inputs

  → Expert walks into room → MANY domain-relevant chunks fire weakly
  → = H5 multi-weak-signal convergence → "gut feeling" about situation
  → = Klein 1998 firefighter: large trigger surface → many chunks fire → accurate intuition

  → TRAUMA VÀ EXPERTISE = CÙNG CƠ CHẾ, KHÁC HƯỚNG:
    Trauma: large trigger surface + threat direction → fear/avoidance
    Expertise: large trigger surface + novelty direction → insight/competence
    → = F1 NT7 confirmed: novelty vs threat DIRECTION matters, not mechanism
```

### §4.4 — Trigger surface reduction (natural + therapeutic)

```
TRIGGER SURFACE CAN SHRINK OVER TIME:

  NATURAL REDUCTION ("sống tích cực ở context mới"):
    → Move to new environment → old context entry points less matched
    → New positive chunks accumulate → compete for activation (§3)
    → Generalization NARROWS with safe experiences
      (🟢 Discriminative learning: safe experiences narrow fear generalization)
    → Some entry points DECAY (Ebbinghaus — unused retrieval paths weaken)
    → = Trigger surface gradually SHRINKS
    → = "Giảm dần theo thời gian sống tích cực" (user's formulation, confirmed)

  THERAPEUTIC REDUCTION:
    → Exposure therapy: systematic safe experience at each entry point
    → Each exposure: entry point → safe → new safety link → competition
    → Over time: each entry point has competing safe link
    → = Trigger surface remains same SIZE but OUTCOME changes at each point
    → = Not fewer doors, but each door now leads to safe room alongside scary room

  ⚠️ TRIGGER SURFACE NEVER REACHES ZERO:
    → Some entry points too deep (body-level, emotional peak compiled)
    → Complete elimination NOT possible (chunk not deletable)
    → Goal is SUFFICIENT probability shift, not elimination
    → = "Vẫn hơi khó chịu nhưng handle được" = success
    → = "Hoàn toàn quên" = unrealistic expectation
```

---

## §5 — Unified Model

### §5.1 — 3 mechanisms interact

```
⭐ 3 MECHANISMS FORM A UNIFIED SYSTEM:

  ┌──────────────────────────────────────────────────────────────┐
  │                                                              │
  │  TRIGGER SURFACE (§4)                                        │
  │  = How OFTEN chunk gets activated                            │
  │  = f(modalities, connections, emotional weight, generality)  │
  │       │                                                      │
  │       ↓                                                      │
  │  ACTIVATION PROBABILITY (§2)                                 │
  │  = WHERE activation goes when chunk fires                    │
  │  = f(link strength: repetition, recency, emotion, context)  │
  │       │                                                      │
  │       ↓                                                      │
  │  COMPETITIVE RE-LINKING (§3)                                 │
  │  = How probability distribution CHANGES over time            │
  │  = f(new experiences, reconsolidation, anchor management)    │
  │                                                              │
  │  → Together: explains learning, therapy, adaptation, growth  │
  │  → Same mechanism for ALL chunk operations                   │
  │  → Trauma and expertise = same mechanism, different direction │
  └──────────────────────────────────────────────────────────────┘

EXAMPLE — Full lifecycle:

  Event: Bị chó cắn lúc 5 tuổi

  COMPILE:
    → Emotional peak → large trigger surface (many entry points)
    → Strong links: [chó] → [đau, sợ, chạy] (dominant pathway)
    → Probability: 85% threat, 10% neutral, 5% noise

  YEARS 5-10 (avoidance):
    → No new dog experience → no new links
    → Old links decay slightly (Ebbinghaus) but slowly (emotional peak = durable)
    → Trigger surface: still large (generalized to dog sounds, images, similar animals)
    → Random triggers: frequent → "sợ chó" identity consolidated
    → Probability: 75% threat, 15% neutral, 10% scattered

  YEARS 10-15 (gradual positive exposure):
    → Friend has gentle dog → positive experiences begin
    → New links: [chó] → [hiền, an toàn, vui] (initially weak)
    → Reconsolidation: each positive encounter → window → new link integrates
    → Probability shifting: 50% threat, 30% positive, 20% other

  YEAR 20 (resolved):
    → Many positive dog experiences accumulated
    → Trigger surface: still exists but each entry point has competing safe link
    → Probability: 20% old threat (still there), 55% positive, 25% other
    → PFC: "à, hồi nhỏ mình sợ chó, giờ ok rồi, cẩn thận thôi"
    → Body: mostly calm, slight alertness (old link fires weakly)
    → = FUNCTIONAL RESOLUTION (not deletion)
```

### §5.2 — Applications across framework

```
SAME 3 MECHANISMS EXPLAIN:

  LEARNING:
    → New knowledge = new links to existing chunks → probability shift
    → Practice = strengthen new links → dominant pathway changes
    → Expertise = accumulated probability shifts across thousands of chunks

  THERAPY:
    → Trauma = strong old links + large trigger surface
    → Recovery = build competing new links → probability shift → trigger surface managed
    → 3 strategies (§3.3) = 3 speeds of the same mechanism

  HABIT CHANGE:
    → Old habit = dominant pathway (high probability, automatic)
    → New habit = must build competing pathway strong enough to dominate
    → "21 days to form habit" = approximately when new pathway crosses old
    → Stress → old pathway temporarily regains dominance → "relapse"
    → 🟢 Habit relapse under stress (Wood & Neal 2007)

  CREATIVITY:
    → Cross-domain chunks = unusual links (low probability)
    → Creative insight = low-probability link fires (Type 2 aha)
    → Diverse experience = more low-probability links available
    → = "Creativity = accessing low-probability pathways"

  IDENTITY / SELF:
    → Self-related chunks have LARGEST trigger surface (compiled across ALL experience)
    → "Tôi là người X" = dominant pathway from self-chunk to X-chunks
    → Identity change = competitive re-linking of self-chunk associations
    → = SLOW (self = most connected, most reinforced chunk network)

  CULTURAL CHANGE:
    → Shared chunks in community = shared probability distributions
    → Cultural shift = community-level competitive re-linking
    → Takes GENERATIONS (many individuals must shift)
    → = F3 cultural transmission applied to probability model
```

---

## §6 — Honest Assessment

```
═══════════════════════════════════════
🟢 WELL-GROUNDED (individual components)
═══════════════════════════════════════

  Spreading activation (probability-weighted):    Collins & Loftus 1975
  Hebbian learning:                                Hebb 1949
  Memory reconsolidation:                          Nader et al. 2000
  Extinction learning (new, not erasure):          Bouton 2004
  Retrieval-induced forgetting:                    Anderson et al. 1994
  Context-dependent memory:                        Godden & Baddeley 1975
  Mood-congruent memory:                           Bower 1981
  Fear generalization:                             Lissek et al. 2008
  Exposure therapy efficacy:                       Foa & Kozak 1986
  Reconsolidation-based intervention:              Schiller et al. 2010
  Stress-induced relapse:                          Sinha 2001
  Expert recognition:                              Klein 1998
  Priming probability:                             Meyer & Schvaneveldt 1971, Neely 1977
  Lateral inhibition:                              Hartline 1949
  Rumination → worse outcomes:                     Nolen-Hoeksema 2000
  EMDR:                                            Shapiro 2001
  Habit relapse:                                   Wood & Neal 2007
  Stimulus generalization:                         Pavlov, replicated extensively


═══════════════════════════════════════
🟡 FRAMEWORK SYNTHESIS (novel integration)
═══════════════════════════════════════

  Activation PROBABILITY DISTRIBUTION model:       Novel formalization of established components
  Competitive re-linking as unified mechanism:     Novel integration — components established
  Trigger surface concept:                          Novel concept name, mechanism established
  Trauma = expertise same mechanism diff direction: Novel insight, consistent with NT7
  7-factor link strength model:                    Framework formalization
  3 strategies as speed variants of same mechanism: Extends F1 NT7 with mechanism


═══════════════════════════════════════
🔴 SPECULATIVE
═══════════════════════════════════════

  Specific probability percentages:                Illustrative, not measured
  Trigger surface SIZE quantification:             Concept valid, numbers speculative
  Probability crossover timeline:                  Approximate, highly individual
  Identity change as competitive re-linking:       Plausible extension, not tested
  "21 days" habit crossover:                       Folk wisdom, actual timing varies
```

---

## §7 — Falsifiable Predictions

```
P-01b-1: Items with STRONGER competing associations should show MORE
          retrieval-induced forgetting of original associations.
          → 🟢 Already established: Anderson et al. 1994 + subsequent work

P-01b-2: Trauma memories with MORE modalities involved should show HIGHER
          frequency of involuntary recall (intrusions) than single-modality trauma.
          → Testable: compare intrusion rates by number of modalities
          → 🟡 Consistent with PTSD literature (multi-sensory flashbacks)

P-01b-3: Extinction training conducted DURING reconsolidation window should
          produce MORE durable fear reduction than extinction without trigger.
          → 🟢 Already established: Schiller et al. 2010

P-01b-4: Probability of old pathway reactivation should INCREASE under stress,
          fatigue, or cognitive load (PFC weakened → old dominant pathway returns).
          → 🟢 Established: stress-induced relapse (Sinha 2001, Wood & Neal 2007)

P-01b-5: Expert intuition accuracy should correlate with DOMAIN-SPECIFIC trigger
          surface size (measurable via association fluency tests in domain).
          → 🟡 Novel prediction, testable via expertise + association tasks

P-01b-6: Therapeutic exposure at MULTIPLE entry points should produce faster
          symptom reduction than exposure at single entry point.
          → 🟡 Consistent with systematic desensitization hierarchy approach
          → Testable: compare single-stimulus vs multi-stimulus exposure protocols
```

---

## §8 — Cross-References

```
WITHIN F4:
  → 01-Chunk-Connection-Logical.md (4 connection types — each creates links with different strength)
  → 02-Feeling-Intuition-Gradient.md (H5 — multi-weak-signal = sub-threshold activations from §2)
  → 03-Chain-Anchor-Decay.md (anchor = retrieval path → link strength maintenance per §2.2⑦)
  → 04-Right-Wrong-Vague.md (to drill — vague detection = competing signals, probability undetermined)
  → 05-Insight-Tacit-Upgrade.md (to drill — insight = low-probability path fires, §5.2 creativity)

WITHIN CHUNK-ANALYSIS:
  → F1 NT1: gradient (strength-weighted) = §2 probability model substrate
  → F1 NT2: 4 compile mechanisms = §2.2 link strength factors ①-④
  → F1 NT7: 3 update paths = §3.3 strategies (extended with mechanism)
  → F3 00-External-Mechanism.md: external install = link creation via Direction B

CORE FRAMEWORK:
  → Schema/Chunk.md (DRAFT — this file EXTENDS significantly, target for v2.0 rewrite)
  → Schema/Chunk-Search-Advanced.md §1 (resonance = probability-weighted search)
  → Schema/Schema.md §2 (cross-contamination = Type 1 + probability)
  → Somatic-Articulation-Loop.md §2 (implicit→explicit = accessing low-probability knowledge)
  → Feeling/ folder (7-layer model: body signal = aggregate of activated probabilities)

ACADEMIC REFERENCES:
  🟢 Anderson et al. 1994 — Retrieval-induced forgetting
  🟢 Bouton 2004 — Context and extinction
  🟢 Bower 1981 — Mood-congruent memory
  🟢 Collins & Loftus 1975 — Spreading activation
  🟢 Foa & Kozak 1986 — Emotional processing theory / exposure therapy
  🟢 Godden & Baddeley 1975 — Context-dependent memory
  🟢 Hartline 1949 — Lateral inhibition
  🟢 Hebb 1949 — Hebbian learning
  🟢 Klein 1998 — Recognition-primed decision making
  🟢 Lissek et al. 2008 — Fear generalization in anxiety
  🟢 Meyer & Schvaneveldt 1971 — Priming
  🟢 Nader et al. 2000 — Memory reconsolidation
  🟢 Neely 1977 — Semantic priming
  🟢 Nolen-Hoeksema 2000 — Rumination and depression
  🟢 Schiller et al. 2010 — Reconsolidation-based extinction
  🟢 Shapiro 2001 — EMDR
  🟢 Sinha 2001 — Stress-induced relapse
  🟢 Wood & Neal 2007 — Habits under stress
  🟡 Levine 1997 — Somatic Experiencing
  🟢 Resick et al. 2017 — Cognitive Processing Therapy
```

---

## §9 — Status

```
✅ DRILLED v1.0 (N+7, 2026-04-17 — plan adjustment)

  3 CORE MECHANISMS FORMALIZED:
    ① Activation Probability Distribution (§2)
    ② Competitive Re-linking (§3)
    ③ Trigger Surface (§4)

  FRAMEWORK CONTRIBUTIONS:
    ① Activation is PROBABILITY-WEIGHTED, not binary (§2.1)
    ② 7-factor link strength model (§2.2)
    ③ Probability is DYNAMIC, shifts over time (§2.3)
    ④ Competition mechanism: new links vs old links (§3.1)
    ⑤ Reconsolidation window as competition enabler (§3.2)
    ⑥ 3 strategies = 3 speeds of same mechanism (§3.3)
    ⑦ Trigger surface concept formalized (§4.1)
    ⑧ 4-factor trigger surface model (§4.2)
    ⑨ Trauma = expertise = same mechanism, diff direction (§4.3)
    ⑩ Unified model: 3 mechanisms interact (§5.1)

  FALSIFIABLE PREDICTIONS: P-01b-1 through P-01b-6

  ORIGIN: User insight during N+7 session. Plan adjusted from 6→7 files.
  
  TARGET: Chunk.md v2.0 rewrite after 99-Master-Synthesis will incorporate
  this file as CORE mechanism chapter.

  Line count: ~850L
```

---

> **01b-Chunk-Activation-Dynamics.md — End of file.**
>
> 3 core chunk mechanisms formalized: probability distribution,
> competitive re-linking, trigger surface.
> Trauma = expertise = same mechanism, different direction.
> "Domain real không theo chúng ta" — plan adjusted to capture core insight.
>
> Phiên bản: v1.0, 2026-04-17.
