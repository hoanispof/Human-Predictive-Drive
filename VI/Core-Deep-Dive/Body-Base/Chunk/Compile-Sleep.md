---
title: Compile-Sleep — Sleep Maintenance (Offline System)
version: 1.0
created: 2026-06-01
status: v1.0
scope: |
  Sleep = Sleep Maintenance trong Compile Architecture.
  6 mechanisms: ~1.5 exposure-based, ~4.5 optimization-based.
  Sleep ≠ "chỉ là exposure source." Sleep = OFFLINE MAINTENANCE SYSTEM.
  Phân loại từng mechanism: IS exposure / NOT exposure / PARTIAL.
  Sleep × Architecture interaction (Compile Engine, Entity-Valence Bias, Exposure Channels, PFC Modulation).
  Sleep deprivation = architecture degradation (PFC degrades FIRST).
  Waking rest = complement (~30%), NOT replacement.
  ~40 research citations, 6+1 mechanisms.
purpose: |
  Chunk.md v2.3 §2.1 ④ "Sleep consolidation" = 3 dòng summary (Walker 2017).
  File này = CHI TIẾT: 6 mechanisms, exposure classification, architecture interaction.
  Learning-Cycle.md §4 đã formalize 6+1 mechanisms riêng lẻ.
  File này THÊM: exposure vs optimization classification + vị trí trong Compile Architecture.
parent: Chunk.md v2.3 (§2.1 ④ sleep consolidation = summary → file này = chi tiết)
related: |
  Compile-Taxonomy.md v3.0 — 3 Compile Types (Sleep Maintenance = offline maintenance)
  Learning-Cycle.md §4 — 6+1 sleep mechanisms (primary research source)
  PFC-Operations.md v1.3 §8.3 — PFC budget recharges via sleep
  Cortisol-Baseline.md v2.2 — Sleep = PRIMARY cortisol recovery
  Background-Pattern.md v2.0 §3 — Gist Extraction → Background-Pattern formation
  Body-Base.md v3.3 §2 — Compilable Architecture (+ Sleep Maintenance)
  Reward-Signal-Architecture.md v2.1 — Evaluative vs Direct-State vulnerability
dependencies:
  - Chunk.md v2.3 — §2.1 ④ sleep, §2.2 compile_rate formula
  - Compile-Taxonomy.md v3.0 — 3 Compile Types + architecture context
  - PFC-Operations.md v1.3 — Hold/Suppress, PFC budget
  - Entity-Valence-Dynamics.md v1.1 — Structural/Current valence
  - Body-Base.md v3.3 — Compilable Architecture
  - Cortisol-Baseline.md v2.2 — Cortisol × sleep interaction
  - Background-Pattern.md v2.0 — Gist extraction → Background-Pattern
  - Simulation-Engine.md v1.1 — PFC offline during sleep
  - Reward-Signal-Architecture.md v2.1 — Reward vulnerability under deprivation
language: Tiếng Việt primary + English technical terms
confidence: 🟢 Research support | 🟡 Framework synthesis | 🔴 Hypothesis
sources: |
  Learning-Cycle.md §4 (6+1 mechanisms) — secondary research source
---

# Compile-Sleep — Sleep Maintenance (Offline System)

> **Sleep KHÔNG ĐƠN THUẦN là "exposure source" thứ 4.**
>
> Sleep có 6 mechanisms — chỉ ~1.5 exposure-based, ~4.5 optimization.
> Phần lớn sleep = OPTIMIZATION trên compiled chunks HIỆN CÓ.
>
> Compile Engine (Hebbian) = XÂY nhà (khi thức).
> Sleep = BẢO TRÌ nhà (khi ngủ):
>   Dọn phế liệu (SHY). Chuyển kho tạm → kho chính (Active Consolidation).
>   Sơn lại (Emotional Decoupling). Rút gọn bản vẽ (Gist Extraction).
>   Kết nối phòng mới với phòng cũ (Creative Linking).
>   Chạy thử hệ thống (Replay).
>
> BẢO TRÌ ≠ XÂY MỚI. Nhưng KHÔNG bảo trì → nhà HỎNG.

---

## MỤC LỤC

- §0 — Vị Trí Trong Framework
- §1 — Core Thesis: Sleep ≠ Exposure Source
- §2 — Sleep Stages: SWS vs REM
- §3 — 6 Mechanisms: Exposure vs Optimization
- §4 — Sleep × Compile Architecture
- §5 — Sleep Deprivation = Architecture Degradation
- §6 — Waking Rest: Complement, Not Replacement
- §7 — Honest Assessment
- §8 — Open Questions
- §9 — Cross-References

---

## §0 — Vị Trí Trong Framework

```
⭐ FILE NÀY MỞ RỘNG CHUNK.MD §2.1 ④ "SLEEP CONSOLIDATION":

  Chunk.md §2.1 ④: 3 dòng — "Hippocampus REPLAY → strengthen hoặc prune.
  Sleep consolidation (Walker 2017). Sáng mai rõ hơn = vô thức ĐÃ xử lý."

  3 dòng đó = summary. File này = chi tiết:
    6 mechanisms riêng biệt (không chỉ "replay")
    Phân loại exposure vs optimization
    Vị trí Sleep Maintenance trong Compile Architecture
    Tương tác với Compile Engine, Entity-Valence Bias, Exposure Channels, PFC Modulation
    Sleep deprivation = architecture degradation model


  VỊ TRÍ TRONG COMPILE ARCHITECTURE:

    Compile Architecture (Compile-Taxonomy.md):
      Compile Engine (Hebbian) + Entity-Valence Bias + Exposure Channels (External+Deliberate+Spontaneous)
      + PFC Modulation → compile chunks khi THỨC.

    Sleep Maintenance (file này):
      Sleep = OFFLINE MAINTENANCE SYSTEM.
      Tương tác với Compile Engine, Entity-Valence Bias, Exposure Channels, PFC Modulation nhưng ĐỘC LẬP — chạy khi THỨC tắt.


  VỊ TRÍ TRONG FILE HIERARCHY:

    Chunk.md §2.1 ④ (summary 3 dòng)
      → [file này] (chi tiết 6 mechanisms + architecture interaction)
      → Learning-Cycle.md §4 (research source gốc cho 6+1 mechanisms)

    Body-Base.md §2 (Compilable Architecture)
      → [file này] (Sleep Maintenance = offline maintenance)

    Đọc Chunk.md §2 trước → đọc file này → đọc Compile-Taxonomy.md.


  READING GUIDE:

    §1-§2: thesis + sleep stages — bối cảnh
    §3: 6 mechanisms — NỘI DUNG CHÍNH (exposure vs optimization classification)
    §4: architecture interaction — tương tác với compile system khi thức
    §5-§6: deprivation + waking rest — consequences + alternatives
    §7-§9: assessment + questions + references
```

---

## §1 — Core Thesis: Sleep ≠ Exposure Source

```
⭐⭐ CORE THESIS:

  Sleep KHÔNG ĐƠN THUẦN là "exposure source" thứ 4.

  Nếu sleep = chỉ là exposure source:
    → Sleep = thêm Spontaneous (automatic internal exposure)
    → Giá trị duy nhất = "lặp lại patterns"
    → Mất ngủ = chỉ "ít repetition hơn"

  THỰC TẾ: sleep có 6 mechanisms — chỉ ~1.5 exposure-based:
    → Sleep PRUNE (SHY — cắt liên kết yếu)
    → Sleep REPLAY (Hippocampal Replay — lặp compressed)
    → Sleep TRANSFER (Active Consolidation — hippocampus → cortex)
    → Sleep LINK (Creative Linking — tạo liên kết xa)
    → Sleep DECOUPLE (Emotional Decoupling — bóc emotional tag)
    → Sleep ABSTRACT (Gist Extraction — trừu tượng hoá)

  Hầu hết = OPTIMIZATION trên compiled chunks HIỆN CÓ.
  KHÔNG phải "thêm exposure mới."


  VỊ TRÍ TRONG ARCHITECTURE — SLEEP MAINTENANCE:

    ┌─────────────────────────────────────────┐
    │  WAKING (thức)                           │
    │                                         │
    │  Compile Engine ← Exposure (External+Deliberate+Spontaneous)         │
    │           ← Entity-Valence Bias│
    │           ← PFC Modulation           │
    │           → Compiled Chunks              │
    └─────────────────┬───────────────────────┘
                      │
                      ▼
    ┌─────────────────────────────────────────┐
    │  SLEEP (ngủ) — Sleep Maintenance               │
    │                                         │
    │  Compiled Chunks → 6 mechanisms:         │
    │    ① SHY (prune)                          │
    │    ② Replay (re-expose)                  │
    │    ③ Active Consolidation (transfer)     │
    │    ④ Creative Linking (new links)        │
    │    ⑤ Emotional Decoupling (strip tag)    │
    │    ⑥ Gist Extraction (abstract)          │
    │  → Optimized Chunks                      │
    └─────────────────┬───────────────────────┘
                      │
                      ▼
    ┌─────────────────────────────────────────┐
    │  NEXT WAKING                             │
    │                                         │
    │  Optimized Chunks = starting material    │
    │  cho Compile Engine tiếp tục compile           │
    │  PFC catecholamine RESTORED              │
    │  Cortisol effects PARTIALLY cleared      │
    └─────────────────────────────────────────┘

  = CYCLE: Waking (build) → Sleep (maintain) → Waking (build on maintained)
  = Learning-Cycle.md H8: "Learning là chu kỳ, không phải event."


  TẠI SAO PHÂN BIỆT QUAN TRỌNG:

    "Sleep = exposure source" → mất ngủ = "ít repetition hơn"
    "Sleep = maintenance system" → mất ngủ = "KHÔNG prune, KHÔNG transfer,
      KHÔNG decouple, KHÔNG abstract, KHÔNG link + ít replay"
    → Hệ quả KHÁC NHAU. Model khác → prediction khác → intervention khác.

    Mất ngủ THỰC TẾ: PFC degrade + emotional reactivity + memory fragile
    + creativity down + noise accumulate = CONSISTENT với 6-mechanism model.
    KHÔNG consistent với "chỉ ít repetition."


  🟡 Sleep as Sleep Maintenance in compile architecture: framework synthesis
  🟢 Multi-mechanism sleep model: Diekelmann & Born 2010
  🟢 Sleep ≠ single function: established sleep neuroscience
```

---

## §2 — Sleep Stages: SWS vs REM

```
🟢 2 LOẠI SLEEP CHÍNH — KHÁC NEUROCHEMISTRY, KHÁC FUNCTION:


  NREM (Non-REM), đặc biệt SWS (Slow Wave Sleep, stage N3):
    EEG: slow oscillations (< 1 Hz) + spindles (~12-16 Hz) + sharp-wave ripples
    Chemistry: low acetylcholine, low norepinephrine
    Dominant NỬA ĐẦU đêm
    Functions: SHY, Replay, Active Consolidation, Gist Extraction

  REM (Rapid Eye Movement):
    EEG: desynchronized (similar to waking)
    Chemistry: HIGH acetylcholine, LOW norepinephrine, theta rhythms
    Muscles: paralyzed (atonia)
    Dominant NỬA SAU đêm
    Functions: Creative Linking, Emotional Decoupling


  Cycle: ~4-6 NREM/REM cycles per đêm, mỗi cycle ~90 phút.


  TẠI SAO 2 STAGES TỒN TẠI:

    Nếu sleep chỉ có 1 function → 1 stage đủ.
    2 stages = 2 SETS of distinct mechanisms:
      SWS = strengthen + transfer + prune (declarative memory dominant)
      REM = creative link + emotional calibrate (procedural + emotional dominant)

    Stage-specific disruption → SPECIFIC deficits:
      SWS disruption → memory impairment
      REM disruption → emotional dysregulation
    = 2 independent maintenance systems sharing sleep time.


  ┌────────────┬────────────────────┬──────────────────────┐
  │ Stage      │ SWS (NREM deep)    │ REM                  │
  ├────────────┼────────────────────┼──────────────────────┤
  │ When       │ Nửa đầu đêm       │ Nửa sau đêm          │
  │ EEG        │ Slow oscillations  │ Desynchronized       │
  │ NE         │ Low                │ Very low             │
  │ ACh        │ Low                │ High                 │
  │ Muscles    │ Relaxed            │ Paralyzed            │
  │ Dreams     │ Rare, abstract     │ Vivid, narrative     │
  │ Mechanisms │ SHY, Replay,      │ Creative Linking,    │
  │            │ Consolidation,    │ Emotional            │
  │            │ Gist Extraction   │ Decoupling           │
  │ Primary    │ Declarative memory │ Emotional + creative │
  └────────────┴────────────────────┴──────────────────────┘


  🟢 Sleep architecture: Walker 2017, Diekelmann & Born 2010
  🟢 SWS dominant early, REM dominant late: established polysomnography
  🟢 Stage-specific deficits: Gais et al. 2000, Wagner et al. 2001
```

---

## §3 — 6 Mechanisms: Exposure vs Optimization

```
⭐ PHÂN LOẠI MỖI MECHANISM — EXPOSURE HAY OPTIMIZATION:

  ┌────┬─────────────────────┬─────────────┬──────────────────────────┐
  │ #  │ Mechanism           │ Exposure?   │ Primary function         │
  ├────┼─────────────────────┼─────────────┼──────────────────────────┤
  │  1 │ SHY Homeostasis     │ ❌ NOT      │ Prune weak, preserve     │
  │    │                     │             │ strong (signal/noise)    │
  ├────┼─────────────────────┼─────────────┼──────────────────────────┤
  │  2 │ Hippocampal Replay  │ ✅ YES      │ Re-fire sequences        │
  │    │                     │ (internal)  │ (internal exposure)      │
  ├────┼─────────────────────┼─────────────┼──────────────────────────┤
  │  3 │ Active Consolidation│ ❌ NOT      │ Transfer hippocampus     │
  │    │                     │             │ → cortex (relocate)      │
  ├────┼─────────────────────┼─────────────┼──────────────────────────┤
  │  4 │ REM Creative Linking│ 🟡 PARTIAL  │ New remote associations  │
  │    │                     │ (new links) │ (cross-domain connect)   │
  ├────┼─────────────────────┼─────────────┼──────────────────────────┤
  │  5 │ Emotional Decoupling│ ❌ NOT      │ Strip emotional charge   │
  │    │                     │             │ (preserve content)       │
  ├────┼─────────────────────┼─────────────┼──────────────────────────┤
  │  6 │ Gist Extraction     │ 🟡 PARTIAL  │ Abstract pattern from    │
  │    │                     │ (abstract)  │ specific (generalize)    │
  └────┴─────────────────────┴─────────────┴──────────────────────────┘

  EXPOSURE COUNT: 1 full (Replay) + 2 partial (Creative Linking, Gist) = ~1.5 exposure-based.
  OPTIMIZATION: 3 full (SHY, Consolidation, Decoupling) + 2 partial (Creative Linking, Gist) = ~4.5 optimization.
  → MAJORITY of sleep = OPTIMIZATION, not exposure.

  "~1.5 / ~4.5" = ước lượng vì Creative Linking và Gist Extraction là PARTIAL — ranh giới
  exposure/optimization không binary. Điểm cốt lõi: phần lớn sleep
  KHÔNG tạo exposure mới mà TỐI ƯU compile hiện có.

  🟡 Exposure vs optimization classification: framework synthesis
  🟢 6 mechanisms individually: established (citations per section below)
```

### §3.1 — Synaptic Homeostasis Hypothesis (SHY) — NOT exposure

```
🟢 SHY = GLOBAL SYNAPTIC DOWNSCALING:

  Research: Tononi & Cirelli 2003, 2014 "Sleep and the price of plasticity"

  CƠ CHẾ:
    Khi thức: synapses NET-POTENTIATE (Hebbian → Compile Engine tăng connections)
    → Metabolically UNSUSTAINABLE — nếu chỉ tăng → brain bão hoà
    → Sleep (SWS): ALL synapses weaken PROPORTIONALLY
    → Result: total network strength → baseline, RELATIVE strengths PRESERVED

  CONSEQUENCE:
    Synapses fire THƯỜNG XUYÊN → still RELATIVELY strong → PRESERVED
    Synapses fire HIẾM → relatively weaker → may fall below threshold → PRUNED
    = "Pruning is not deletion — it's competitive preservation"

  EVIDENCE:
    Slow oscillation amplitude decreases across night (progressive downscaling)
    GluA1 AMPA receptors decrease after sleep (molecular evidence)
    Dendritic spine turnover: waking ADD, sleep PRUNE (Maret 2011, Yang 2014)
    Cross-species: fly brain shows similar downscaling (Gilestro 2009)


  TẠI SAO NOT EXPOSURE:

    SHY KHÔNG fire specific patterns.
    SHY KHÔNG re-activate learned content.
    SHY = GLOBAL process — ALL synapses affected.
    = Không có "tiếp xúc với pattern" → không phải exposure.

    SHY = SIGNAL-TO-NOISE OPTIMIZER:
      Loại bỏ noise (weak random connections)
      Giữ signal (strong repeated patterns)
      → Sáng hôm sau: "thấy rõ hơn" = noise GIẢM, signal tương đối TĂNG


  TRONG COMPILE ARCHITECTURE:

    Compile Engine (Hebbian) khi thức → tạo NHIỀU connections (cả strong + weak)
    SHY khi ngủ → prune weak → giữ strong
    = Quality control SAU compile. KHÔNG tạo compile mới.

    Analogy: viết bài xong → đọc lại → xóa câu thừa.
    Xóa câu thừa ≠ viết câu mới.


  🟢 Tononi & Cirelli 2003, 2014
  🟢 Maret 2011, Yang 2014 (dendritic spine evidence)
  🟢 Gilestro 2009 (cross-species drosophila)
  🟡 SHY = not exposure classification: framework synthesis
```

### §3.2 — Hippocampal Replay — IS exposure (internal)

```
🟢 REPLAY = PATTERN RE-FIRE COMPRESSED:

  Research: Wilson & McNaughton 1994 (seminal), O'Neill et al. 2010

  CƠ CHẾ:
    Khi thức: hippocampal cells fire A→B→C→D (experience sequence)
    Khi ngủ (SWS): cells RE-FIRE A→B→C→D at 10-20x compressed speed
    → Trong sharp-wave ripples (SWRs: ~100-250 Hz bursts, ~50-100ms)
    → Mỗi replay = 1 Hebbian strengthening event
    → 1 đêm = NHIỀU replays = NHIỀU Hebbian events

  EVIDENCE:
    Wilson & McNaughton 1994: rat hippocampus replay matches daytime navigation
    Lee & Wilson 2002: replay can be FORWARD or REVERSE
    O'Neill 2010: disrupting ripples → memory consolidation IMPAIRED
    Human analog: fMRI replay during rest (Tambini 2010, Schuck 2019)

  COMPRESSED SPEED:
    10-20x = 1 đêm replay lượng learning bằng VÀI NGÀY repetition
    Different plasticity rules at compressed speed (Staresina 2015)
    Spindle-ripple coupling coordinates replay × cortex transfer (Active Consolidation)


  TẠI SAO IS EXPOSURE:

    Replay = neurons FIRE TOGETHER → Hebbian → STRENGTHEN
    = COMPILE ENGINE operating on REPLAYED patterns
    = Internal exposure (Spontaneous variant during sleep)

    NHƯNG: replay ≠ NEW exposure.
    Replay = RE-expose ĐÃ HỌC. Không tạo patterns MỚI — chỉ STRENGTHEN cũ.


  TRONG COMPILE ARCHITECTURE:

    Replay = dạng exposure DUY NHẤT đầy đủ trong sleep system.
    Replay feed vào Compile Engine (Hebbian) → strengthen existing compiled chunks.
    = Spontaneous sleep variant: automatic internal exposure, PFC offline.

    Khác Exposure-Spontaneous khi thức:

    ┌──────────────────┬──────────────────────┬────────────────────┐
    │                  │ Spontaneous (thức)   │ Replay (ngủ)       │
    ├──────────────────┼──────────────────────┼────────────────────┤
    │ Trigger          │ Context, random      │ Hippocampus-driven │
    │ Speed            │ Normal              │ 10-20x compressed  │
    │ Organization     │ Unstructured        │ Systematic (SWRs)  │
    │ PFC influence    │ Possible (partial)   │ None (offline)     │
    │ External input   │ Possible (External)  │ None (blocked)     │
    │ Efficiency       │ Low                 │ High               │
    └──────────────────┴──────────────────────┴────────────────────┘

    → Replay = "industrial-grade Spontaneous" — same principle, different execution.


  🟢 Wilson & McNaughton 1994
  🟢 Lee & Wilson 2002
  🟢 O'Neill et al. 2010
  🟢 Staresina et al. 2015 (spindle-ripple coupling)
  🟡 Replay = Spontaneous sleep variant: framework synthesis
```

### §3.3 — Active Systems Consolidation — NOT exposure

```
🟢 ACTIVE CONSOLIDATION = HIPPOCAMPUS → CORTEX TRANSFER:

  Research: Born & Wilhelm 2012, Diekelmann & Born 2010

  CƠ CHẾ:
    New memories start HIPPOCAMPUS-DEPENDENT (cần hippocampus để recall)
    → Qua sleep (SWS): memories TRANSFER to NEOCORTEX-DEPENDENT
    → Hippocampus "teach" cortex via spindle-ripple coupling
    → Cortex build OWN representation, independent of hippocampus
    → Weeks to months cho full transfer (complex memories)

  DISTINCT FROM REPLAY:
    Replay = firing event (neurons fire)
    Active Consolidation = long-term TRANSFER that replay enables
    Replay = necessary SUBSTRATE. Consolidation = the RESULT.
    → Replay WITHIN Consolidation, nhưng Consolidation ≠ Replay.

  EVIDENCE:
    Squire 1992: hippocampal damage → anterograde amnesia (mới)
                                    but spares old memories (đã consolidate)
    Takashima 2006: fMRI shows decreasing hippocampal + increasing cortical
    Rasch & Born 2013: sleep-dependent nature confirmed


  TẠI SAO NOT EXPOSURE:

    Active Consolidation = RELOCATE, không phải STRENGTHEN.
    Pattern di chuyển từ hippocampus → cortex.
    = Architectural reorganization, not re-activation for Hebbian.

    Analogy: chuyển file từ USB (tạm) sang ổ cứng (vĩnh viễn).
    Chuyển file ≠ viết file mới. File content KHÔNG đổi — location đổi.


  TRONG COMPILE ARCHITECTURE:

    Active Consolidation tương tác với Compile Engine INDIRECTLY:
    → Replay → Hebbian strengthen (Compile Engine)
    → Consolidation USES replay output để transfer location
    → After Consolidation: chunk accessible WITHOUT hippocampus
    → = "Permanent installation" — từ RAM (hippocampus) sang ROM (cortex)

    IMPLICATION:
      Khi thức: mới học = hippocampus-dependent = FRAGILE
      Sau sleep Consolidation: cortex-dependent = STABLE
      → "Sáng mai nhớ rõ hơn" = Consolidation đã transfer thành công
      → "Simple things take one night, complex things take weeks"
        = complex → nhiều Consolidation cycles để full transfer


  🟢 Born & Wilhelm 2012
  🟢 Squire 1992 (hippocampal amnesia)
  🟢 Takashima 2006 (fMRI evidence)
  🟢 Rasch & Born 2013 (review)
  🟡 Active Consolidation = not exposure (relocation): framework synthesis
```

### §3.4 — REM Creative Linking — PARTIAL exposure

```
🟢 CREATIVE LINKING = REMOTE ASSOCIATIONS MỚI:

  Research: Cai et al. 2009, Wagner et al. 2004

  CƠ CHẾ:
    REM features: HIGH acetylcholine + LOW norepinephrine + theta oscillations
    → "Associative gating" WEAKENED:
      Khi thức: strong associations dominate (focused thinking)
      Khi REM: weak associations CAN fire (unfocused, cross-domain)
    → Concepts từ DIFFERENT DOMAINS fire together
    → Weak novel combinations that MATCH schemas → strengthened
    → Result: sáng hôm sau = new creative links available

  EVIDENCE:
    Cai 2009: Remote Associates Test (RAT) improvement after REM
      (not just quiet rest or NREM — REM SPECIFICALLY)
    Wagner 2004: Number Reduction Task — sleep doubles hidden pattern discovery
      (8% → 23% find hidden shortcut)
    Cross-species: REM present in all mammals + birds → evolutionary conserved
    Stickgold 1999: sleep improves emotionally salient recall, REM specifically


  TẠI SAO PARTIAL EXPOSURE:

    CÓ exposure element: concepts FIRE TOGETHER → Hebbian → new link
    = TECHNICALLY Compile Engine operating on novel combinations

    NHƯNG mechanism KHÁC typical exposure:
    ① Random activation (not intentional exposure)
    ② Weak gating (not normal associative gating)
    ③ Only SOME combinations strengthen (match schema = survive)
    ④ No external input, no PFC direction
    → = "Exploration" hơn là "exposure"

    = PARTIALLY exposure: Compile Engine involved, nhưng MECHANISM khác.


  TRONG COMPILE ARCHITECTURE:

    Creative Linking = dạng compile DUY NHẤT trong sleep tạo connections MỚI.
    (Replay chỉ strengthen connections CŨ.)

    Creative Linking tương tác với Exposure-Spontaneous:
    → Creative Linking trong REM tạo new links
    → Sáng hôm sau: new links CÓ THỂ fire tự động (Spontaneous)
    → "Eureka khi thức dậy" = Creative Linking output fire lần đầu khi conscious


  🟢 Cai et al. 2009
  🟢 Wagner et al. 2004
  🟢 Stickgold 1999
  🟡 Creative Linking = partial exposure (novel mechanism): framework synthesis
```

### §3.5 — Emotional Decoupling — NOT exposure

```
🟢 EMOTIONAL DECOUPLING = BÓC EMOTIONAL TAG, GIỮ CONTENT:

  Research: Walker 2017, van der Helm et al. 2011

  CƠ CHẾ:
    REM: LOW noradrenaline + HIGH amygdala reactivation
    → Amygdala "fires WITHOUT stress chemistry"
    → Repeated REM cycles → decouple amygdala response from memory retrieval
    → CONTENT preserved (you remember the event)
    → EMOTIONAL TAG reduced (it feels "less intense")

  = "Sleep on it" = emotional charge GIẢM, knowledge GIỮ.

  EVIDENCE:
    van der Helm 2011: REM reduces amygdala reactivity to emotional stimuli
    Walker 2005: sleep-deprived → heightened amygdala reactivity
    Germain 2013: disrupted REM correlates with PTSD emotional memory problems


  TẠI SAO NOT EXPOSURE:

    Decoupling KHÔNG fire pattern for Hebbian strengthening.
    Decoupling MODIFY existing compiled chunk:
      Strip emotional tag ← chunk remains
      = EDITING, not CREATING.

    Analogy: chỉnh color temperature của ảnh.
    Ảnh (content) KHÔNG đổi. Color (emotional tag) đổi.
    Chỉnh ảnh ≠ chụp ảnh mới.


  TRONG COMPILE ARCHITECTURE:

    Emotional Decoupling tương tác với Entity-Valence:
    → Emotional tag = part of valence profile
    → Decoupling reduce emotional intensity → Entity-Valence UPDATE
    → Sáng hôm sau: event vẫn có valence, nhưng INTENSITY giảm

    FAILURE MODE:
      Chronic REM disruption (insomnia, alcohol, PTSD):
      → Decoupling fails → emotional tags ACCUMULATE
      → Every day adds emotional charge WITHOUT decoupling
      → = Burnout, emotional exhaustion, PTSD escalation
      → Cortisol-Baseline.md v2.2: "phá nhanh, xây chậm"

    CONNECTION TO TRAUMA THERAPY:
      EMDR: hypothesized to partially simulate Decoupling mechanism while awake
      → Bilateral stimulation may mimic REM-related processing
      → 🟡 Mechanism debated but clinical efficacy established (Stickgold 2002)

      Exposure therapy (Foa & Kozak 1986):
      → Different mechanism: create NEW exposure (PFC Modulation → Entity-Valence Bias indirect)
      → Decoupling = STRIP old emotional tag (sleep-specific, no new exposure)
      → Both reduce emotional reactivity, but via DIFFERENT paths


  🟢 Walker 2017
  🟢 van der Helm et al. 2011
  🟢 Walker 2005 (sleep deprivation → amygdala)
  🟢 Germain 2013 (PTSD × REM)
  🟡 Emotional Decoupling × Entity-Valence Bias interaction: framework synthesis
  🟡 EMDR × Emotional Decoupling analogy: hypothesized (Stickgold 2002)
```

### §3.6 — Gist Extraction — PARTIAL exposure

```
🟢 GIST EXTRACTION = TRỪU TƯỢNG HOÁ, BỎ CHI TIẾT:

  Research: Payne et al. 2009, Stickgold 2013, Tamminen 2010

  CƠ CHẾ:
    Replay re-fires sequences nhiều lần
    → Shared features ACROSS SIMILAR experiences = REINFORCED
    → Unique surface details of EACH experience = NOT reinforced
    → Relative contrast → GIST dominant in later recall
    → = Abstract pattern emerges, specific details fade

  EVIDENCE:
    Payne 2009: sleep increases false memory for gist-consistent items
      (DRM paradigm — evidence that gist is being extracted)
    Stickgold 2013: sleep abstracts "rules" from examples
    Tamminen 2010: sleep necessary for integrating new words into semantic network
    Lutz 2017: gist extraction scales with sleep duration


  TẠI SAO PARTIAL EXPOSURE:

    CÓ exposure element:
    → Gist Extraction relies on Replay as substrate
    → Shared features fire TOGETHER across replays → Hebbian → gist
    → = Compile Engine operating on ABSTRACTED patterns

    NHƯNG:
    → Primary function = EXTRACT (generalize), not STRENGTHEN specific
    → TRADE-OFF: gist preserved, detail LOST
    → = Net effect: DIFFERENT kind of compile (abstract, not specific)

    Analogy: đọc 100 bài báo → tóm tắt 1 paragraph.
    Tóm tắt = new content (gist). Nhưng 100 bài = LOST.
    = Creation BY destruction. New (gist) replaces old (details).


  TRONG COMPILE ARCHITECTURE:

    Gist Extraction tương tác với BACKGROUND-PATTERN formation:
    → Background-Pattern.md v2.0 §3: sleep gist extraction abstracts
      repeated events into single pattern
    → Gist Extraction = PRIMARY MECHANISM tạo Background-Pattern
    → Background-Pattern = accumulated gist over YEARS of Gist Extraction cycles

    Gist Extraction → Background-Pattern → Exposure-Spontaneous:
    → Gist Extraction create gist → gist becomes part of Background-Pattern
    → Background-Pattern fires continuously (Spontaneous)
    → Spontaneous → Compile Engine → reinforce gist further → snowball

    = Tại sao "người lạc quan" MỌI THỨ đều thấy tốt:
      Years of positive experiences
      → Gist Extraction extract positive gist
      → Background-Pattern = positive-dominant
      → Spontaneous fire positive → bias ALL new exposure
      → = Self-reinforcing via Gist Extraction → Spontaneous → Compile Engine loop


  🟢 Payne et al. 2009
  🟢 Stickgold 2013
  🟢 Tamminen 2010
  🟢 Lutz 2017
  🟡 Gist Extraction → Background-Pattern formation link: framework synthesis
```

### §3.7 — Dreaming as Simulation — DEBATED (excluded from core)

```
🟡 THREAT SIMULATION THEORY (DEBATED):

  Research: Revonsuo 2000, Nielsen & Levin 2007
  Status: 🟡 Debated — KHÔNG đủ tin cậy để đưa vào architecture chính

  Claim: REM dreams = simulations of threat/life-relevant scenarios.
  Evidence for: dreams bias negative (Schredl 2010), cross-cultural consistency
  Evidence against: many dreams mundane/positive/bizarre, random-activation viable

  FRAMEWORK POSITION:
    → Ghi nhận cho completeness nhưng KHÔNG rely on.
    → Dreaming nếu đúng = thêm 1 mechanism vào Sleep Maintenance.
    → Dreaming nếu sai = 6 mechanisms còn lại vẫn đủ.
    → Đợi future research trước khi formalize.

  🟡 Revonsuo 2000
  🟡 Not included in core architecture (insufficient evidence)
```

### §3.8 — Summary table: 6 mechanisms × architecture role

```
⭐ TỔNG HỢP:

  ┌────┬──────────────────────┬───────────┬─────────────────┬──────────────────────────┐
  │ #  │ Mechanism             │ Stage     │ Exposure?       │ Architecture role        │
  ├────┼──────────────────────┼───────────┼─────────────────┼──────────────────────────┤
  │  1 │ SHY Homeostasis       │ SWS       │ ❌ NOT          │ Quality control          │
  │    │                       │           │                 │ (prune weak)             │
  ├────┼──────────────────────┼───────────┼─────────────────┼──────────────────────────┤
  │  2 │ Hippocampal Replay    │ SWS       │ ✅ YES          │ Strengthen existing      │
  │    │                       │           │ (internal,      │ (Compile Engine offline)  │
  │    │                       │           │  compressed)    │                          │
  ├────┼──────────────────────┼───────────┼─────────────────┼──────────────────────────┤
  │  3 │ Active Consolidation  │ SWS       │ ❌ NOT          │ Relocate                 │
  │    │                       │           │                 │ (RAM → ROM)              │
  ├────┼──────────────────────┼───────────┼─────────────────┼──────────────────────────┤
  │  4 │ Creative Linking      │ REM       │ 🟡 PARTIAL      │ Create new links         │
  │    │                       │           │ (novel combos)  │ (exploration)            │
  ├────┼──────────────────────┼───────────┼─────────────────┼──────────────────────────┤
  │  5 │ Emotional Decoupling  │ REM       │ ❌ NOT          │ Calibrate valence        │
  │    │                       │           │                 │ (strip emotional tag)    │
  ├────┼──────────────────────┼───────────┼─────────────────┼──────────────────────────┤
  │  6 │ Gist Extraction       │ SWS+REM   │ 🟡 PARTIAL      │ Abstract + generalize    │
  │    │                       │           │ (new abstract)  │ (→ Background-Pattern)   │
  └────┴──────────────────────┴───────────┴─────────────────┴──────────────────────────┘

  ~1.5 exposure-based. ~4.5 optimization-based.
  → MAJORITY of sleep = optimization of EXISTING compile.
  → Sleep ≠ "just more repetition."


  TẠI SAO MULTI-MECHANISM LÀ FRAMING ĐÚNG (Learning-Cycle.md §4.9):

    Single-mechanism view ("sleep consolidates memory") KHÔNG giải thích:
    ① Tại sao 2 sleep stages tồn tại (SWS vs REM distinct chemistry)
    ② Tại sao disruption CỤ THỂ gây deficit CỤ THỂ
    ③ Tại sao evolution duy trì ~1/3 lifespan trong sleep nếu chỉ 1 function
    ④ Tại sao "sáng hôm sau" = pleasant + thoải mái + thấy liên kết mới
       = 3 distinct improvements cùng lúc

    Multi-mechanism view giải thích cả 4.
```

---

## §4 — Sleep × Compile Architecture

```
⭐ SLEEP TƯƠNG TÁC VỚI TỪNG COMPONENT CỦA COMPILE ARCHITECTURE:

  Sleep Maintenance (sleep) KHÔNG hoạt động ĐỘC LẬP.
  Sleep ENHANCES, CALIBRATES, hoặc RESTORES từng component.
```

### §4.1 — Sleep × Compile Engine (Hebbian)

```
🟡 SLEEP ENHANCES COMPILE ENGINE QUA 3 ĐƯỜNG:

  ① Replay = Compile Engine hoạt động OFFLINE:
     Replayed patterns → Hebbian strengthen → same mechanism as waking
     NHƯNG: COMPRESSED speed (10-20x) = efficient
     NHƯNG: NO external input = chỉ strengthen ĐÃ HỌC
     NHƯNG: SYSTEMATIC (hippocampus-driven, not random)

     Net effect: Compile Engine gets "bonus exposure cycles" during sleep.
     = Tại sao "sáng hôm sau nhớ rõ hơn" = more Hebbian cycles occurred.

  ② SHY IMPROVES Compile Engine efficiency:
     Prune weak connections → next day Compile Engine runs on CLEANER network
     → Signal-to-noise ratio BETTER → compile quality HIGHER next day
     → = "Fresh start" effect — not new knowledge, but cleaner processing.

  ③ Gist Extraction creates NEW inputs for Compile Engine:
     Gist = abstract pattern = new compiled chunk
     → Tomorrow's Compile Engine can build ON TOP of abstracted knowledge
     → = Expertise Compile: each night compresses → pyramidal stacking


  🟡 Sleep enhances Compile Engine via 3 mechanisms: framework synthesis
  🟢 Replay = Hebbian during sleep: Wilson & McNaughton 1994
  🟢 SHY improves signal-to-noise ratio: Tononi & Cirelli 2014
```

### §4.2 — Sleep × Entity-Valence Bias

```
🟡 SLEEP CALIBRATES ENTITY-VALENCE BIAS:

  Emotional Decoupling directly affects Entity-Valence:
  → Reduce emotional INTENSITY of entity associations
  → Entity-Valence profile: content preserved, peak valence reduced
  → Sáng hôm sau: entity vẫn có valence, nhưng less REACTIVE

  MECHANISM:
    Khi thức: encounter entity → emotional peak → Compile Engine compile
    Khi ngủ: Decoupling strip emotional peak → same entity, lower intensity
    → Next encounter: entity triggers LESS extreme response
    → = Entity-Valence Bias CALIBRATED: not removed, but TUNED

  VÍ DỤ:
    Cãi nhau với bạn tối qua → emotional peak: angry + hurt
    Decoupling during REM: amygdala reactivate WITHOUT noradrenaline
    → Emotional tag REDUCED
    → Sáng hôm sau: still remember argument, but feel "less angry"
    → = Entity-Valence [bạn] updated: anger REDUCED, content PRESERVED

  Gist Extraction also affects Entity-Valence Bias indirectly:
  → Abstract PATTERNS from entity interactions
  → Long-term: entity structural valence built from gist of MANY interactions
  → = Entity-Compiled.md: 40→200 giờ formation time
    = MANY Gist Extraction cycles abstracting entity gist over months


  🟡 Emotional Decoupling calibrates Entity-Valence Bias: framework synthesis
  🟢 Emotional decoupling: van der Helm 2011
  🟢 Amygdala reactivity reduced after sleep: Walker 2005
```

### §4.3 — Sleep × Exposure Channels

```
🟡 SLEEP = INDEPENDENT OF NORMAL SOURCE CHANNELS:

  Khi ngủ:
    Exposure-External = BLOCKED (thalamic gating, sensory input suppressed)
    Exposure-Deliberate = OFFLINE (PFC minimal activity, no deliberate thought)
    Exposure-Spontaneous = ACTIVE but in DIFFERENT mode (Replay)

  → Sleep operates INDEPENDENT of normal External/Deliberate/Spontaneous channels.
  → Sleep has its OWN internal activation system (hippocampus-driven replay).
  → = Tại sao sleep = SEPARATE Sleep Maintenance, không phải variant của Exposure.


  Replay ≈ Spontaneous VARIANT nhưng KHÁC:
    Replay = organized, compressed, systematic, PFC offline
    Spontaneous thức = unstructured, normal speed, PFC possible
    → Replay = "industrial-grade Spontaneous" — same principle, different execution.

  Creative Linking tương tác với Spontaneous NGÀY HÔM SAU:
    Creative Linking tạo new links trong REM
    → Sáng hôm sau: new links CÓ THỂ fire tự động (Spontaneous)
    → "Eureka khi thức dậy" = Creative Linking output fire lần đầu khi conscious


  🟡 Sleep independent of External/Deliberate/Spontaneous: framework synthesis
  🟢 Thalamic gating during sleep: established polysomnography
  🟢 PFC reduced activity during SWS: established neuroimaging
```

### §4.4 — Sleep × PFC Modulation

```
🟡🟢 SLEEP RESTORES PFC MODULATION:

  Khi ngủ: PFC = OFFLINE.
  → PFC Modulation KHÔNG hoạt động
  → No Hold, no Suppress = "PFC rest mode"

  NHƯNG: sleep RESTORES PFC function cho ngày hôm sau:

  ① Catecholamine restoration:
     PFC-Operations.md v1.3: PFC budget recharges via sleep
     → Dopamine + Norepinephrine pools REFILL during sleep
     → Sáng hôm sau: PFC ĐẦY catecholamine = OPTIMAL performance

  ② Cortisol effects CLEAR:
     Cortisol-Baseline.md v2.2: sustained cortisol → gene expression → neural wear
     → Sleep = recovery window → cortisol effects PARTIALLY cleared
     → "Sáng: catecholamine ĐẦY + cortisol effects ÍT = PFC optimal"
     → "Tối: catecholamine CẠN + cortisol effects NHIỀU = PFC yếu"

  ③ Synaptic efficiency restored (SHY):
     → PFC synapses also downscaled → more efficient processing
     → = PFC "refreshed" — same hardware, cleaner connections


  IMPLICATION:
    Sleep deprivation → PFC Modulation degrades FIRST:
    → PFC = most metabolically expensive brain region
    → PFC = most sensitive to catecholamine depletion
    → = Tại sao mất ngủ → impulsive, emotional, poor judgment
    → = PFC Modulation OFFLINE → Entity-Valence Bias UNCHECKED
    → = Chi tiết: §5 (Sleep Deprivation).


  🟢 Catecholamine restoration during sleep: Arnsten 2009
  🟢 PFC sensitivity to sleep deprivation: Yoo et al. 2007
  🟡 PFC degrades first under sleep deprivation: framework synthesis
```

---

## §5 — Sleep Deprivation = Architecture Degradation

```
⭐⭐ MẤT NGỦ = TẤT CẢ 6 MECHANISMS BỊ DISRUPT ĐỒNG THỜI:


  ┌───────────────────────┬──────────────────────────────────────────┐
  │ MECHANISM DISRUPTED   │ CONSEQUENCE                              │
  ├───────────────────────┼──────────────────────────────────────────┤
  │ SHY absent            │ Synapses không prune → noise TÍCH LŨY    │
  │                       │ → Signal-to-noise ratio GIẢM              │
  │                       │ → Next day learning IMPAIRED              │
  ├───────────────────────┼──────────────────────────────────────────┤
  │ Replay absent         │ Patterns không strengthen → FRAGILE      │
  │                       │ → Memory WORSE than pre-sleep             │
  │                       │ → What was learned → not consolidated     │
  ├───────────────────────┼──────────────────────────────────────────┤
  │ Consolidation miss    │ Hippocampus → cortex transfer STALLED    │
  │                       │ → Knowledge stuck in "temporary storage" │
  │                       │ → Hippocampus FULL → new learning blocked│
  ├───────────────────────┼──────────────────────────────────────────┤
  │ Creative Linking miss │ No remote associations formed             │
  │                       │ → No "eureka moments" next day           │
  │                       │ → Problem-solving capacity REDUCED        │
  ├───────────────────────┼──────────────────────────────────────────┤
  │ Decoupling miss       │ Emotional tags NOT stripped               │
  │                       │ → Emotions ACCUMULATE day-over-day       │
  │                       │ → Reactivity INCREASES                   │
  │                       │ → Trajectory: burnout, PTSD escalation   │
  ├───────────────────────┼──────────────────────────────────────────┤
  │ Gist absent           │ No abstraction → details overwhelm      │
  │                       │ → Can't see "big picture"                │
  │                       │ → Background-Pattern formation slowed    │
  └───────────────────────┴──────────────────────────────────────────┘


  ARCHITECTURE COLLAPSE ORDER:

    1st: PFC Modulation → depleted catecholamine
         → PFC = most expensive, most sensitive
    2nd: all 6 mechanisms missed → chunks degrade
    3rd: Compile Engine still runs nhưng trên DIRTY network
    4th: Entity-Valence Bias unchecked → emotional amplification
    → = Compound degradation

    "Mệt → dễ cáu → không muốn gặp ai → quyết định tệ"
    = PFC down → Entity-Valence unchecked → emotional reactivity ↑
      → social avoidance → poor judgment


  CORTISOL INTERACTION (Cortisol-Baseline.md v2.2):

    Sleep deprivation → cortisol baseline DRIFT UP
    → Cortisol = gene expression effects → neural wear
    → "Phá nhanh, xây chậm":
      Cortisol elevation: hours to days
      Recovery: weeks to months
    → = Sleep debt COMPOUNDS: mỗi đêm mất ngủ = damage > 1 đêm recover

    Chronic sleep deprivation → cortisol chronically elevated
    → All 6 Sleep mechanisms degraded + cortisol damage
    → = Double hit: no maintenance + active damage


  REWARD VULNERABILITY (Reward-Signal-Architecture.md v2.1):

    Sleep deprivation degrades Evaluative Reward FIRST
      (complex, compilation-dependent, VTA habituation stacks)
    Direct-State Reward PERSISTS as "hedonic floor"
      (hardware-based, CT afferents, simple comfort)

    → Mất ngủ: "chỉ muốn ăn ngon, nằm thoải mái"
      = Evaluative reward GONE, Direct-State still accessible
    → = Tại sao sleep-deprived people → comfort food, simple pleasures


  🟢 Sleep deprivation → memory impairment: Walker & Stickgold 2004
  🟢 Sleep deprivation → amygdala hyperactivity: Yoo et al. 2007
  🟢 Sleep deprivation → PFC impairment: Killgore 2010
  🟢 Cortisol × sleep deprivation: Leproult & Van Cauter 2010
  🟢 Arnsten 2009 (catecholamine inverted-U)
  🟡 Architecture collapse order model: framework synthesis
  🟡 Evaluative vs Direct-State vulnerability: framework synthesis
```

---

## §6 — Waking Rest: Complement, Not Replacement

```
🟡🟢 WAKING REST CÓ OVERLAP VỚI SLEEP, NHƯNG KHÔNG THAY THẾ:

  Learning-Cycle.md §5:
    "Sleep is one path for refinement. Waking rest is another.
     Different hardware, different neurochemistry, different strengths."


  WAKING REST MECHANISMS:

  ① DMN activation (Raichle et al. 2001):
     PFC release → Default Mode Network activate
     → Mind-wandering + autobiographical memory + future simulation
     → Some integration of disparate information
     → = Partial Consolidation + partial Creative Linking

  ② Incubation effect (Sio & Ormerod 2009 meta-analysis):
     Pause on problem → solution emerges "spontaneously"
     → DMN + subconscious processing continues in background
     → = Partial Creative Linking (while awake)

  ③ Walking boosts creativity (Oppezzo & Schwartz 2014):
     Divergent thinking +~60% vs sitting
     → Rhythmic gait + low cognitive load + sensory input
     → = Partial Creative Linking + External exposure (novel environment)

  ④ Meditation (Tang et al. 2015):
     Reduces DMN hyperactivity, enhances PFC-DMN coupling
     → Less rumination (negative Spontaneous reduced)
     → Background integration without wandering interference
     → = Partial Decoupling (emotional regulation) + partial Consolidation (integration)


  WAKING REST vs SLEEP — COMPARISON:

  ┌────────────────────────┬───────────────────┬────────────────────────────┐
  │ Mechanism              │ Waking Rest       │ Sleep                      │
  ├────────────────────────┼───────────────────┼────────────────────────────┤
  │ SHY (prune)            │ ❌ NOT available  │ ✅ Full                    │
  │ Replay (Hebbian)       │ 🟡 Partial (DMN)  │ ✅ Full (SWR)              │
  │ Consolidation          │ 🟡 Partial (slow)  │ ✅ Full (fast)             │
  │ Creative Linking       │ 🟡 Partial         │ ✅ Full (REM)              │
  │ Emotional Decoupling   │ 🟡 Very partial    │ ✅ Full (REM NE↓)          │
  │ Gist Extraction        │ 🟡 Partial          │ ✅ Full                    │
  │ PFC restoration        │ ❌ NOT (PFC ON)    │ ✅ Full (catecholamine)    │
  │ Cortisol recovery      │ ❌ NOT             │ ✅ Partial                 │
  └────────────────────────┴───────────────────┴────────────────────────────┘


  ⭐ KEY INSIGHT:

  Waking rest CAN do ~30% of what sleep does:
    → Some replay (DMN), some creative links (incubation), some emotional regulation
    → USEFUL for mid-day breaks between learning sessions

  Waking rest CANNOT do ~70%:
    → NO SHY (prune) → noise accumulates
    → NO full REM mechanisms → emotional tags stay, creative links limited
    → NO PFC restoration → catecholamine still depleting
    → NO cortisol recovery → wear continues

  → Waking rest = COMPLEMENT, not substitute.
  → Nap (20-90 min) = INTERMEDIATE — some SWS but limited REM.
  → Full night sleep = IRREPLACEABLE for complete Sleep Maintenance function.

  "~30% / ~70%" = ước lượng minh hoạ, KHÔNG phải đo lường chính xác.
  Điểm cốt lõi: waking rest KHÔNG thể thay thế sleep cho phần lớn mechanisms.


  🟢 DMN: Raichle et al. 2001
  🟢 Incubation: Sio & Ormerod 2009
  🟢 Walking: Oppezzo & Schwartz 2014
  🟢 Meditation: Tang et al. 2015
  🟢 Napping benefits: Mednick et al. 2003
  🟡 Waking rest as partial sleep (~30%): framework synthesis
```

---

## §7 — Honest Assessment

```
🟢 ESTABLISHED (strong research support):

  INDIVIDUAL MECHANISMS:
    SHY: Tononi & Cirelli 2003, 2014 (molecular + cross-species evidence)
    Replay: Wilson & McNaughton 1994 (seminal, replicated extensively)
    Active Consolidation: Born & Wilhelm 2012 (hippocampus → cortex transfer)
    Creative Linking: Cai 2009, Wagner 2004 (REM-specific creative improvement)
    Emotional Decoupling: Walker 2017, van der Helm 2011 (amygdala reactivity)
    Gist Extraction: Payne 2009, Stickgold 2013 (DRM paradigm evidence)

  SLEEP ARCHITECTURE:
    2 stages (SWS vs REM) with distinct functions: established polysomnography
    Stage-specific disruption → specific deficits: Gais 2000, Wagner 2001
    Sleep deprivation → PFC impairment: Yoo 2007, Killgore 2010
    Sleep deprivation → amygdala hyperactivity: Yoo 2007
    Cortisol × sleep: Leproult & Van Cauter 2010

  WAKING REST:
    DMN: Raichle 2001, Incubation: Sio & Ormerod 2009
    Walking: Oppezzo & Schwartz 2014, Meditation: Tang 2015


🟡 FRAMEWORK SYNTHESIS (logic consistent, dựa trên established):

  Sleep Maintenance model:
    Sleep as separate component in Compile Architecture.
    Components individually established. Positioning = synthesis.

  Exposure vs Optimization classification:
    Novel classification. "Is this mechanism exposure?" = novel question.
    TESTABLE: if classification correct, disrupting Replay (exposure) should impair
    memory differently from disrupting SHY (optimization).

  "~1.5 exposure / ~4.5 optimization" count:
    Approximate. Creative Linking and Gist Extraction = PARTIAL → exact boundary subjective.
    Core insight (majority = optimization) robust regardless of exact count.

  Architecture collapse order (PFC first):
    Consistent with established PFC sensitivity to sleep deprivation.
    Specific sequential model = novel synthesis.

  Gist Extraction → Background-Pattern formation link:
    Consistent with Background-Pattern.md §3 + gist extraction research.
    Specific mechanism chain = novel framework claim.

  Waking rest ~30% overlap:
    Approximate. Based on mechanism-by-mechanism comparison.
    Individual overlaps established. Aggregate estimate = synthesis.


🔴 NEEDS MORE RESEARCH:

  Quantitative mechanism interaction: 6 mechanisms sequential hay concurrent trong 1 đêm?
  Napping: mechanism nào active ở 20-min vs 90-min nap?
  Age-related sleep architecture → compile quality decline?
  DEC2 short sleepers: efficient mechanisms hay skip?
  Emotional Decoupling current vs structural Entity-Valence effect: bao nhiêu cycles?
  Sleep as compile_rate parameter hay maintenance?
  Cross-cultural variation in sleep practices × compile quality
```

---

## §8 — Open Questions

```
🔴 CÁC CÂU HỎI CHƯA CÓ ĐÁP ÁN:


  Q1: SLEEP MECHANISMS — SEQUENTIAL HAY CONCURRENT?

     Trong 1 đêm: 6 mechanisms chạy lần lượt hay song song?
     Evidence gợi ý: SWSleep mechanisms (SHY, Replay, Consolidation, Gist) mostly sequential with overlap
     REM mechanisms (Creative Linking, Decoupling) concurrent within REM episode
     NHƯNG: cross-cycle interactions chưa rõ
     → Ảnh hưởng: rượu suppress SWS (Ebrahim 2013), SSRIs suppress REM
       (Wilson & Argyropoulos 2005) → stage-specific mechanism loss

     🟢 Alcohol suppresses SWS: Ebrahim et al. 2013
     🟢 SSRIs suppress REM: Wilson & Argyropoulos 2005
     🔴 Cross-mechanism interaction during night: needs more research


  Q2: NAPPING — MECHANISM NÀO ACTIVE?

     20-min nap: mainly SHY (partial) + Replay (partial)
     90-min nap: 1 full NREM/REM cycle → all 6 mechanisms (all partial)
     → Napping research supports memory improvement (Mednick et al. 2003)
     → NHƯNG: napping ≠ full night (fewer cycles, less accumulation)

     🟢 Napping benefits: Mednick et al. 2003
     🔴 Quantitative nap vs full night: needs measurement


  Q3: AGE-RELATED SLEEP ARCHITECTURE CHANGES:

     Children: MORE SWS → more SHY/Replay/Consolidation/Gist → faster consolidation
     Elderly: LESS SWS + LESS REM → all 6 mechanisms ALL reduced
     → = Age-related compile quality decline PARTIALLY explained by sleep?

     🟢 Sleep architecture changes with age: Ohayon et al. 2004
     🔴 Sleep mechanism degradation → compile quality: needs analysis


  Q4: INDIVIDUAL VARIATION IN SLEEP MECHANISMS:

     Genetic: DEC2 mutation → "short sleepers" (6h sufficient)
     → Do short sleepers have MORE EFFICIENT Sleep mechanisms?
     → Or do they simply SKIP some mechanisms?

     🟢 DEC2 mutation: He et al. 2009
     🔴 Short sleep → compile quality: unknown


  Q5: EMOTIONAL DECOUPLING × STRUCTURAL VALENCE:

     Decoupling strips emotional tag PER NIGHT (current valence).
     NHƯNG: Entity-Valence structural = accumulated over YEARS.
     → Decoupling chỉ strip CURRENT emotional peak, KHÔNG strip structural valence?
     → Bao nhiêu Decoupling cycles để shift structural valence measurably?
     → = Tại sao "chia tay lâu rồi mà vẫn buồn" — Decoupling works on current,
       nhưng structural valence = deep, slow, needs MANY Decoupling cycles

     🔴 Emotional Decoupling current vs structural effect: needs analysis


  Q6: COMPILE_RATE FORMULA × SLEEP:

     Current formula: f(exposure × saliency × contingency
                        × peak_valence × multi_modal_richness)
     → Sleep thêm exposure (Replay) + modify peak_valence (Decoupling) + modify richness? (Creative Linking)
     → Should sleep be an ADDITIONAL parameter in formula?
     → Or: sleep = maintenance of existing parameters, not new parameter?

     🟡 Sleep as parameter vs maintenance: framework decision needed


  Q7: DREAMING (Dreaming as Simulation):

     Revonsuo 2000 Threat Simulation Theory — debated.
     Nếu đúng: thêm 1 mechanism vào Sleep Maintenance.
     Nếu sai: 6 mechanisms đủ.
     → Đợi future research.

     🟡 Revonsuo 2000 — insufficient evidence for architecture commitment
```

---

## §9 — Cross-References

### §9.1 — Framework files referenced

```
PRIMARY SOURCE:
  Learning-Cycle.md §4 — 6+1 sleep mechanisms, detailed evidence
  Learning-Cycle.md §5 — waking rest mechanisms

COMPILE ARCHITECTURE:
  Compile-Taxonomy.md v3.0 — 3 Compile Types (file này = Sleep Maintenance)

CORE FILES:
  Chunk.md v2.3 §2.1 ④ — Sleep consolidation (summary → file này = chi tiết)
  Chunk.md v2.3 §2.2 — compile_rate formula (sleep × formula interaction)
  PFC-Operations.md v1.3 — PFC budget recharges via sleep
  Cortisol-Baseline.md v2.2 — Sleep = PRIMARY cortisol recovery
  Background-Pattern.md v2.0 §3 — Gist Extraction → Background-Pattern
  Entity-Valence-Dynamics.md v1.1 — VTA habituation × emotional dynamics
  Reward-Signal-Architecture.md v2.1 — Evaluative vs Direct-State vulnerability
  Simulation-Engine.md v1.1 — PFC offline during sleep
  Body-Base.md v3.3 §2 — Compilable Architecture (+ Sleep Maintenance)
```

### §9.2 — Research citations

```
ESTABLISHED (🟢):

  SLEEP MECHANISMS:
  Tononi & Cirelli 2003, 2014 — SHY (Synaptic Homeostasis Hypothesis)
  Wilson & McNaughton 1994 — Hippocampal replay (seminal)
  Lee & Wilson 2002 — Forward and reverse replay
  O'Neill et al. 2010 — SWR disruption → memory impairment
  Staresina et al. 2015 — Spindle-ripple coupling
  Born & Wilhelm 2012 — Active Systems Consolidation
  Diekelmann & Born 2010 — Sleep and memory consolidation review
  Squire 1992 — Hippocampal amnesia (classical evidence)
  Takashima 2006 — fMRI hippocampus → cortex transfer
  Rasch & Born 2013 — Sleep-dependent consolidation review
  Cai et al. 2009 — REM creative linking (RAT improvement)
  Wagner et al. 2004 — Sleep doubles insight discovery
  Stickgold 1999 — Sleep × emotional memory
  Walker 2017 — Emotional decoupling
  van der Helm et al. 2011 — REM reduces amygdala reactivity
  Walker 2005 — Sleep deprivation → amygdala hyperactivity
  Germain 2013 — PTSD × REM disruption
  Payne et al. 2009 — Gist extraction (DRM paradigm)
  Stickgold 2013 — Sleep abstracts rules
  Tamminen 2010 — Sleep integrates new words into semantic network
  Lutz 2017 — Gist extraction scales with sleep duration

  SLEEP STAGES:
  Gais et al. 2000 — SWS × declarative memory
  Wagner et al. 2001 — REM × emotional memory
  Ohayon et al. 2004 — Age-related sleep architecture changes

  SLEEP DEPRIVATION:
  Yoo et al. 2007 — Sleep deprivation → amygdala hyperactivity
  Killgore 2010 — Sleep deprivation → PFC impairment
  Leproult & Van Cauter 2010 — Cortisol × sleep deprivation
  Walker & Stickgold 2004 — Sleep deprivation → memory
  Arnsten 2009 — Catecholamine inverted-U

  SLEEP DISRUPTION:
  Ebrahim et al. 2013 — Alcohol suppresses SWS
  Wilson & Argyropoulos 2005 — SSRIs suppress REM
  Raskind et al. 2003 — Prazosin for PTSD nightmares

  DENDRITIC EVIDENCE:
  Maret 2011, Yang 2014 — Dendritic spine turnover
  Gilestro 2009 — Drosophila sleep downscaling

  INDIVIDUAL VARIATION:
  He et al. 2009 — DEC2 short sleep mutation

  WAKING REST:
  Raichle et al. 2001 — Default Mode Network
  Sio & Ormerod 2009 — Incubation meta-analysis
  Oppezzo & Schwartz 2014 — Walking × creativity
  Tang et al. 2015 — Meditation neuroscience review
  Mednick et al. 2003 — Napping benefits


FRAMEWORK SYNTHESIS (🟡):
  Sleep as Sleep Maintenance in compile architecture — session 2026-06-01
  6 mechanisms × exposure classification — session 2026-06-01
  Emotional Decoupling calibrates Entity-Valence Bias — session 2026-06-01
  Gist Extraction → Background-Pattern formation link — session 2026-06-01
  Architecture collapse order (PFC first) — session 2026-06-01
  Waking rest = complement not replacement — session 2026-06-01
  Replay = industrial-grade Spontaneous — session 2026-06-01

DEBATED (🟡):
  Revonsuo 2000 — Threat Simulation Theory (dreaming)
  Stickgold 2002 — EMDR × REM analogy
```

---

> **PARENT**: Chunk.md v2.3 §2.1 ④ (summary → file này = chi tiết)
> **COMPANION**: Compile-Taxonomy.md (1 Compile Engine + 3 Modulators + Sleep Maintenance)
> **SOURCE**: Learning-Cycle.md §4 (6+1 mechanisms research source)
