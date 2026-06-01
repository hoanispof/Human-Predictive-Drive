# Drill: Compile-Sleep — Offline Maintenance System

> **Session**: 2026-06-01
> **Trigger**: Drill-Compile-Architecture §11 Q5 — Sleep ở đâu trong architecture?
> **Prerequisite**: Đọc 10-Compile-Architecture.md trước
> **Primary source**: Learning-Cycle.md §4 (6+1 sleep mechanisms chi tiết)
> **Status**: DRILL (phân tích sâu, chưa propagate vào framework files)

---

## MỤC LỤC

- §0 — THESIS: Sleep ≠ Exposure Source
- §1 — SLEEP STAGES: NREM vs REM
- §2 — 6 SLEEP MECHANISMS: Phân Loại Exposure vs Optimization
- §3 — SLEEP × COMPILE ARCHITECTURE INTERACTION
- §4 — SLEEP DEPRIVATION = ARCHITECTURE DEGRADATION
- §5 — WAKING REST: Partial Alternative, NOT Replacement
- §6 — OPEN QUESTIONS
- §7 — IMPLICATIONS CHO FRAMEWORK
- §8 — CROSS-REFERENCES + CITATIONS

---

## §0 — THESIS: Sleep ≠ Exposure Source

```
⭐⭐ CORE THESIS:

  Compile Architecture (10-Compile-Architecture.md):
    Engine A (Hebbian) + Modulator B (Entity-Valence) + Source C (3 channels)
    + Modulator D (PFC) → compile chunks khi THỨC.

  Sleep = Component S: OFFLINE MAINTENANCE SYSTEM.

  Sleep KHÔNG ĐƠN THUẦN là "exposure source" thứ 4.
  Sleep có 6 mechanisms — chỉ ~1.5 là exposure-based.
  4.5 mechanisms còn lại = OPTIMIZATION, không tạo exposure mới.


  TẠI SAO PHÂN BIỆT QUAN TRỌNG:

  Nếu sleep = chỉ là exposure source:
    → Sleep = thêm C3 (automatic internal exposure)
    → Giá trị duy nhất = "lặp lại patterns"
    → Mất ngủ = chỉ "ít repetition hơn"

  THỰC TẾ: sleep là NHIỀU HƠN exposure:
    → Sleep PRUNE (SHY — cắt liên kết yếu)
    → Sleep TRANSFER (Active Consolidation — hippocampus → cortex)
    → Sleep DECOUPLE (Emotional Decoupling — bóc emotional tag)
    → Sleep ABSTRACT (Gist Extraction — trừu tượng hoá)
    → Sleep LINK (Creative Linking — tạo liên kết xa)
    → Sleep REPLAY (Hippocampal Replay — lặp compressed)

    KHÔNG mechanism nào trên đây = "chỉ exposure."
    Hầu hết = OPTIMIZATION trên compiled chunks HIỆN CÓ.


  ANALOGY:

    Engine A (Hebbian) = XÂY nhà (khi thức).
    Sleep = BẢO TRÌ nhà (khi ngủ):
      Dọn dẹp phế liệu (SHY)
      Chuyển đồ từ kho tạm sang kho chính (Active Consolidation)
      Sơn lại (Emotional Decoupling)
      Rút gọn bản vẽ phức → bản vẽ đơn giản (Gist Extraction)
      Kết nối phòng mới với phòng cũ (Creative Linking)
      Chạy thử hệ thống (Replay)

    BẢO TRÌ ≠ XÂY MỚI. Nhưng KHÔNG bảo trì → nhà HỎNG.


  VỊ TRÍ TRONG ARCHITECTURE:

    ┌─────────────────────────────────────────┐
    │  WAKING (thức)                           │
    │                                         │
    │  Engine A ← Sources (C1+C2+C3)          │
    │           ← Modulator B (Entity-Valence)│
    │           ← Modulator D (PFC)           │
    │           → Compiled Chunks              │
    └─────────────────┬───────────────────────┘
                      │
                      ▼
    ┌─────────────────────────────────────────┐
    │  SLEEP (ngủ) — Component S               │
    │                                         │
    │  Compiled Chunks → 6 mechanisms:         │
    │    S1: SHY (prune)                       │
    │    S2: Replay (re-expose)                │
    │    S3: Active Consolidation (transfer)   │
    │    S4: Creative Linking (new links)      │
    │    S5: Emotional Decoupling (strip tag)  │
    │    S6: Gist Extraction (abstract)        │
    │  → Optimized Chunks                      │
    └─────────────────┬───────────────────────┘
                      │
                      ▼
    ┌─────────────────────────────────────────┐
    │  NEXT WAKING                             │
    │                                         │
    │  Optimized Chunks = starting material    │
    │  cho Engine A tiếp tục compile           │
    │  PFC catecholamine RESTORED              │
    │  Cortisol effects PARTIALLY cleared      │
    └─────────────────────────────────────────┘

  = CYCLE: Waking (build) → Sleep (maintain) → Waking (build on maintained)
  = Learning-Cycle.md H8: "Learning là chu kỳ, không phải event."


  🟡 Sleep as Component S in compile architecture: framework synthesis (session 2026-06-01)
  🟢 Multi-mechanism sleep model: Learning-Cycle.md §4 (6 mechanisms established)
  🟢 Sleep ≠ single function: Diekelmann & Born 2010
```

---

## §1 — SLEEP STAGES: NREM vs REM

```
🟢 2 LOẠI SLEEP CHÍNH — KHÁC NEUROCHEMISTRY, KHÁC FUNCTION:


  NREM (Non-REM), đặc biệt SWS (Slow Wave Sleep, stage N3):
    EEG: slow oscillations (< 1 Hz) + spindles (~12-16 Hz) + sharp-wave ripples
    Chemistry: low acetylcholine, low norepinephrine
    Dominant NỬA ĐẦU đêm
    Functions: S1 SHY, S2 Replay, S3 Active Consolidation, S6 Gist Extraction

  REM (Rapid Eye Movement):
    EEG: similar to waking (desynchronized)
    Chemistry: HIGH acetylcholine, LOW norepinephrine, theta rhythms
    Muscles: paralyzed (atonia)
    Dominant NỬA SAU đêm
    Functions: S4 Creative Linking, S5 Emotional Decoupling

  Cycle: ~4-6 NREM/REM cycles per đêm, mỗi cycle ~90 phút.


  TẠI SAO 2 STAGES TỒN TẠI (evolutionary argument):

    Nếu sleep chỉ có 1 function → 1 stage đủ.
    2 stages = 2 SETS of distinct mechanisms:
      SWS = strengthen + transfer + prune (declarative memory dominant)
      REM = creative link + emotional calibrate (procedural + emotional dominant)

    → Stage-specific disruption causes SPECIFIC deficits:
      SWS disruption → memory impairment
      REM disruption → emotional dysregulation
    → = 2 independent maintenance systems sharing sleep time.


  ┌──────────┬────────────────────┬──────────────────────┐
  │ Stage    │ SWS (NREM deep)    │ REM                  │
  ├──────────┼────────────────────┼──────────────────────┤
  │ When     │ Nửa đầu đêm       │ Nửa sau đêm          │
  │ EEG      │ Slow oscillations  │ Desynchronized       │
  │ NE       │ Low                │ Very low             │
  │ ACh      │ Low                │ High                 │
  │ Muscles  │ Relaxed            │ Paralyzed            │
  │ Dreams   │ Rare, abstract     │ Vivid, narrative     │
  │ Key mech │ S1, S2, S3, S6    │ S4, S5               │
  │ Primary  │ Declarative memory │ Emotional + creative │
  └──────────┴────────────────────┴──────────────────────┘


  🟢 Sleep architecture: Walker 2017, Diekelmann & Born 2010
  🟢 SWS dominant early, REM dominant late: established polysomnography
  🟢 Stage-specific deficits: Gais et al. 2000, Wagner et al. 2001
```

---

## §2 — 6 SLEEP MECHANISMS: Phân Loại Exposure vs Optimization

```
⭐ PHÂN LOẠI MỖI MECHANISM:

  ┌────┬─────────────────────┬─────────────┬──────────────────────────┐
  │ #  │ Mechanism           │ Exposure?   │ Primary function         │
  ├────┼─────────────────────┼─────────────┼──────────────────────────┤
  │ S1 │ SHY Homeostasis     │ ❌ NOT      │ Prune weak, preserve     │
  │    │                     │             │ strong (signal/noise)    │
  ├────┼─────────────────────┼─────────────┼──────────────────────────┤
  │ S2 │ Hippocampal Replay  │ ✅ YES      │ Re-fire sequences        │
  │    │                     │ (internal)  │ (internal exposure)      │
  ├────┼─────────────────────┼─────────────┼──────────────────────────┤
  │ S3 │ Active Consolidation│ ❌ NOT      │ Transfer hippocampus     │
  │    │                     │             │ → cortex (relocate)      │
  ├────┼─────────────────────┼─────────────┼──────────────────────────┤
  │ S4 │ REM Creative Linking│ 🟡 PARTIAL  │ New remote associations  │
  │    │                     │ (new links) │ (cross-domain connect)   │
  ├────┼─────────────────────┼─────────────┼──────────────────────────┤
  │ S5 │ Emotional Decoupling│ ❌ NOT      │ Strip emotional charge   │
  │    │                     │             │ (preserve content)       │
  ├────┼─────────────────────┼─────────────┼──────────────────────────┤
  │ S6 │ Gist Extraction     │ 🟡 PARTIAL  │ Abstract pattern from    │
  │    │                     │ (abstract)  │ specific (generalize)    │
  └────┴─────────────────────┴─────────────┴──────────────────────────┘

  EXPOSURE COUNT: 1 full (S2) + 2 partial (S4, S6) = ~1.5 exposure-based.
  OPTIMIZATION: 3 full (S1, S3, S5) + 2 partial (S4, S6) = ~4.5 optimization.
  → MAJORITY of sleep = OPTIMIZATION, not exposure.
```

### §2.1 — S1: Synaptic Homeostasis Hypothesis (SHY) — NOT exposure

```
🟢 S1 = GLOBAL SYNAPTIC DOWNSCALING:

  Research: Tononi & Cirelli 2003, 2014 "Sleep and the price of plasticity"

  CƠ CHẾ:
    Khi thức: synapses NET-POTENTIATE (Hebbian → Engine A tăng connections)
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

    Engine A (Hebbian) khi thức → tạo NHIỀU connections (cả strong + weak)
    S1 (SHY) khi ngủ → prune weak → giữ strong
    = Quality control SAU compile.
    = KHÔNG tạo compile mới — tối ưu compile CŨ.

    Analogy: viết bài xong → ĐỌC LẠI → XÓA câu thừa.
    Xóa câu thừa ≠ viết câu mới.


  🟢 Tononi & Cirelli 2003, 2014
  🟢 Maret 2011, Yang 2014 (dendritic spine evidence)
  🟢 Gilestro 2009 (cross-species drosophila)
  🟡 SHY = not exposure classification: framework synthesis
```

### §2.2 — S2: Hippocampal Replay — IS exposure (internal)

```
🟢 S2 = PATTERN RE-FIRE COMPRESSED:

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
    → Spindle-ripple coupling coordinates replay × cortex transfer (S3)


  TẠI SAO IS EXPOSURE:

    Replay = neurons FIRE TOGETHER → Hebbian → STRENGTHEN
    = ENGINE A operating on REPLAYED patterns
    = Internal exposure (Source C3 variant during sleep)
    = "Exposure" theo đúng định nghĩa: pattern được activate → Hebbian

    NHƯNG: replay ≠ new exposure.
    Replay = RE-expose ĐÃ HỌC.
    Không tạo patterns MỚI — chỉ STRENGTHEN patterns CŨ.


  TRONG COMPILE ARCHITECTURE:

    S2 = DẠNG exposure DUY NHẤT trong sleep system.
    S2 feed vào Engine A (Hebbian) → strengthen existing compiled chunks.
    = C3 sleep variant: automatic internal exposure, PFC offline.

    Khác C3 khi thức:
      C3 thức: spontaneous fire, random context, PFC CÓ THỂ influence
      S2 ngủ: SYSTEMATIC replay, compressed, PFC OFFLINE, hippocampus-driven

    → S2 = "industrial-strength C3" — organized, fast, efficient.


  🟢 Wilson & McNaughton 1994
  🟢 Lee & Wilson 2002
  🟢 O'Neill et al. 2010
  🟢 Staresina et al. 2015 (spindle-ripple coupling)
  🟡 S2 = C3 sleep variant: framework synthesis
```

### §2.3 — S3: Active Systems Consolidation — NOT exposure

```
🟢 S3 = HIPPOCAMPUS → CORTEX TRANSFER:

  Research: Born & Wilhelm 2012, Diekelmann & Born 2010

  CƠ CHẾ:
    New memories start HIPPOCAMPUS-DEPENDENT (cần hippocampus để recall)
    → Qua sleep (SWS): memories TRANSFER to NEOCORTEX-DEPENDENT
    → Hippocampus "teach" cortex via spindle-ripple coupling
    → Cortex build OWN representation, independent of hippocampus
    → Weeks to months cho full transfer (complex memories)

  DISTINCT FROM REPLAY (S2):
    S2 (Replay) = firing event (neurons fire)
    S3 (Consolidation) = long-term TRANSFER that replay enables
    S2 = necessary substrate. S3 = the RESULT.
    → S2 WITHIN S3, nhưng S3 ≠ S2.

  EVIDENCE:
    Squire 1992: hippocampal damage → anterograde amnesia (mới)
                                    but spares old memories (đã consolidate)
    Takashima 2006: fMRI shows decreasing hippocampal + increasing cortical
    Rasch & Born 2013: sleep-dependent nature confirmed


  TẠI SAO NOT EXPOSURE:

    S3 = RELOCATE, không phải STRENGTHEN.
    Pattern di chuyển từ hippocampus → cortex.
    = Architectural reorganization, not re-activation for Hebbian.

    Analogy: chuyển file từ USB (tạm) sang ổ cứng (vĩnh viễn).
    Chuyển file ≠ viết file mới.
    File content KHÔNG đổi — location đổi.


  TRONG COMPILE ARCHITECTURE:

    S3 tương tác với Engine A INDIRECTLY:
    → S2 (replay) → Hebbian strengthen (Engine A)
    → S3 USES replay output để transfer location
    → After S3: chunk accessible WITHOUT hippocampus
    → = "Permanent installation" — từ RAM (hippocampus) sang ROM (cortex)

    IMPLICATION:
    Khi thức: mới học = hippocampus-dependent = FRAGILE
    Sau sleep S3: cortex-dependent = STABLE
    → "Sáng mai nhớ rõ hơn" = S3 đã transfer thành công
    → "Simple things take one night, complex things take weeks"
        = complex → nhiều S3 cycles để full transfer


  🟢 Born & Wilhelm 2012
  🟢 Squire 1992 (hippocampal amnesia)
  🟢 Takashima 2006 (fMRI evidence)
  🟢 Rasch & Born 2013 (review)
  🟡 S3 = not exposure (relocation): framework synthesis
```

### §2.4 — S4: REM Creative Linking — PARTIAL exposure

```
🟢 S4 = REMOTE ASSOCIATIONS MỚI:

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
    = TECHNICALLY Engine A operating on novel combinations

    NHƯNG mechanism KHÁC typical exposure:
    ① Random activation (not intentional exposure)
    ② Weak gating (not normal associative gating)
    ③ Only SOME combinations strengthen (match schema = survive)
    ④ No external input, no PFC direction
    → = "Exploration" hơn là "exposure"

    = PARTIALLY exposure: Engine A involved, nhưng MECHANISM khác.
    → New links = new compiled connections.
    → Nhưng creation process = unique to REM, not replicable khi thức.


  TRONG COMPILE ARCHITECTURE:

    S4 = dạng compile DUY NHẤT trong sleep tạo connections MỚI.
    (S2 chỉ strengthen connections CŨ.)

    S4 tương tác với Source C3:
    → S4 trong REM tạo new links
    → Sáng hôm sau: new links CÓ THỂ fire tự động (C3)
    → "Eureka khi thức dậy" = S4 output fire lần đầu khi conscious

    Chunk-Search-Advanced §2: "Aha = link mới between old chunks"
    → S4 = 1 trong các mechanisms tạo aha.
    → Incubation (§5 waking rest) = mechanism khác cho aha.


  🟢 Cai et al. 2009
  🟢 Wagner et al. 2004
  🟢 Stickgold 1999
  🟡 S4 = partial exposure (novel mechanism): framework synthesis
```

### §2.5 — S5: Emotional Decoupling — NOT exposure

```
🟢 S5 = BÓC EMOTIONAL TAG, GIỮ CONTENT:

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
    Folk wisdom "ngủ 1 giấc sáng ra khác" → research confirmation


  TẠI SAO NOT EXPOSURE:

    S5 KHÔNG fire pattern for Hebbian strengthening.
    S5 MODIFY existing compiled chunk:
      Strip emotional tag ← chunk remains
      = EDITING, not CREATING.

    Analogy: chỉnh color temperature của ảnh.
    Ảnh (content) KHÔNG đổi. Color (emotional tag) đổi.
    Chỉnh ảnh ≠ chụp ảnh mới.


  TRONG COMPILE ARCHITECTURE:

    S5 tương tác với MODULATOR B (Entity-Valence):
    → Emotional tag = part of valence profile
    → S5 reduce emotional intensity → Entity-Valence UPDATE
    → Sáng hôm sau: event vẫn có valence, nhưng INTENSITY giảm

    → = "Sáng mai thấy thoải mái hơn" =
      S5 đã decouple emotional charge
      + PFC restored (catecholamine)
      + Cortisol effects partially cleared

    FAILURE MODE (critical):
    Chronic REM disruption (insomnia, alcohol, PTSD):
    → S5 fails → emotional tags ACCUMULATE
    → Every day adds emotional charge WITHOUT decoupling
    → = Burnout, emotional exhaustion, PTSD escalation
    → Cortisol-Baseline.md: "phá nhanh, xây chậm"


  CONNECTION TO TRAUMA THERAPY:
    EMDR (Eye Movement Desensitization and Reprocessing):
    → Hypothesized to partially simulate S5 mechanism while awake
    → Bilateral stimulation may mimic REM-related processing
    → 🟡 Mechanism debated but clinical efficacy established

    Exposure therapy (Foa & Kozak 1986):
    → Different mechanism: create NEW exposure (D → B indirect)
    → S5 = STRIP old emotional tag (sleep-specific, no new exposure)
    → Both reduce emotional reactivity, but via DIFFERENT paths


  🟢 Walker 2017
  🟢 van der Helm et al. 2011
  🟢 Walker 2005 (sleep deprivation → amygdala)
  🟢 Germain 2013 (PTSD × REM)
  🟡 S5 × Modulator B interaction: framework synthesis
  🟡 EMDR × S5 analogy: hypothesized (Stickgold 2002)
```

### §2.6 — S6: Gist Extraction — PARTIAL exposure

```
🟢 S6 = TRỪU TƯỢNG HOÁ, BỎ CHI TIẾT:

  Research: Payne et al. 2009, Stickgold 2013, Tamminen 2010

  CƠ CHẾ:
    S2 (Replay) re-fires sequences nhiều lần
    → Shared features ACROSS SIMILAR experiences = REINFORCED
    → Unique surface details of EACH experience = NOT reinforced
    → Relative contrast → GIST dominant in later recall
    → = Abstract pattern emerges, specific details fade

  EVIDENCE:
    Payne 2009: sleep increases false memory for gist-consistent items
      (DRM paradigm — EVIDENCE that gist is being extracted)
    Stickgold 2013: sleep abstracts "rules" from examples
    Tamminen 2010: sleep necessary for integrating new words into semantic network
    Lutz 2017: gist extraction scales with sleep duration


  TẠI SAO PARTIAL EXPOSURE:

    CÓ exposure element:
    → S6 relies on S2 (replay) as substrate
    → Shared features fire TOGETHER across replays → Hebbian strengthen → gist
    → = Engine A operating on ABSTRACTED patterns

    NHƯNG:
    → Primary function = EXTRACT (generalize), not STRENGTHEN specific
    → TRADE-OFF: gist preserved, detail LOST
    → = Net effect: DIFFERENT kind of compile (abstract, not specific)

    Analogy: đọc 100 bài báo → tóm tắt 1 paragraph.
    Tóm tắt = new content (gist). Nhưng 100 bài = LOST.
    = Creation BY destruction. New (gist) replaces old (details).


  TRONG COMPILE ARCHITECTURE:

    S6 tương tác với BACKGROUND-PATTERN formation:
    → Background-Pattern.md: "sleep gist extraction abstracts thousands of
       repeated events into single pattern"
    → S6 = MECHANISM tạo Background-Pattern
    → Background-Pattern = accumulated gist over YEARS of S6 cycles

    S6 → Background-Pattern → Source C3:
    → S6 create gist → gist becomes part of Background-Pattern
    → Background-Pattern fires continuously (C3)
    → C3 → Engine A → reinforce gist further → snowball

    = Tại sao "người lạc quan" MỌI THỨ đều thấy tốt:
      Years of positive experiences
      → S6 extract positive gist
      → Background-Pattern = positive-dominant
      → C3 fire positive → bias ALL new exposure
      → = Self-reinforcing via S6 → C3 → Engine A loop


  🟢 Payne et al. 2009
  🟢 Stickgold 2013
  🟢 Tamminen 2010
  🟢 Lutz 2017
  🟡 S6 → Background-Pattern formation link: framework synthesis
```

### §2.7 — S7: Dreaming as Simulation — DEBATED (excluded from core)

```
🟡 S7 = THREAT SIMULATION THEORY (DEBATED):

  Research: Revonsuo 2000, Nielsen & Levin 2007
  Status: 🟡 Debated — KHÔNG đủ tin cậy để đưa vào architecture chính

  Claim: REM dreams = simulations of threat/life-relevant scenarios.
  Evidence for: dreams bias negative (Schredl 2010), cross-cultural consistency
  Evidence against: many dreams mundane/positive/bizarre, random-activation viable

  FRAMEWORK POSITION:
    → Include for completeness nhưng KHÔNG rely on.
    → S7 nếu đúng = thêm 1 mechanism vào Component S.
    → S7 nếu sai = 6 mechanisms còn lại vẫn đủ.
    → Đợi future research trước khi formalize.

  🟡 Revonsuo 2000
  🟡 Not included in core architecture (insufficient evidence)
```

### §2.8 — Summary: 6 mechanisms × compile architecture role

```
⭐ TỔNG HỢP:

  ┌────┬──────────────────┬───────────┬─────────────────┬──────────────────────┐
  │ #  │ Mechanism         │ Stage     │ Exposure?       │ Architecture role    │
  ├────┼──────────────────┼───────────┼─────────────────┼──────────────────────┤
  │ S1 │ SHY              │ SWS       │ ❌ NOT          │ Quality control      │
  │    │                  │           │                 │ (prune weak)         │
  ├────┼──────────────────┼───────────┼─────────────────┼──────────────────────┤
  │ S2 │ Replay           │ SWS       │ ✅ YES          │ Strengthen existing  │
  │    │                  │           │ (internal,      │ (Engine A offline)   │
  │    │                  │           │  compressed)    │                      │
  ├────┼──────────────────┼───────────┼─────────────────┼──────────────────────┤
  │ S3 │ Active Consol.   │ SWS       │ ❌ NOT          │ Relocate             │
  │    │                  │           │                 │ (RAM → ROM)          │
  ├────┼──────────────────┼───────────┼─────────────────┼──────────────────────┤
  │ S4 │ Creative Link    │ REM       │ 🟡 PARTIAL      │ Create new links     │
  │    │                  │           │ (novel combos)  │ (exploration)        │
  ├────┼──────────────────┼───────────┼─────────────────┼──────────────────────┤
  │ S5 │ Emot. Decoupling │ REM       │ ❌ NOT          │ Calibrate valence    │
  │    │                  │           │                 │ (strip emotional tag)│
  ├────┼──────────────────┼───────────┼─────────────────┼──────────────────────┤
  │ S6 │ Gist Extraction  │ SWS+REM   │ 🟡 PARTIAL      │ Abstract + generalize│
  │    │                  │           │ (new abstract)  │ (→ Background-Pattern│
  └────┴──────────────────┴───────────┴─────────────────┴──────────────────────┘

  ~1.5 exposure-based. ~4.5 optimization-based.
  → MAJORITY of sleep = optimization of EXISTING compile.
  → Sleep ≠ "just more repetition."
```

---

## §3 — SLEEP × COMPILE ARCHITECTURE INTERACTION

```
⭐ SLEEP TƯƠNG TÁC VỚI TỪNG COMPONENT:
```

### §3.1 — Sleep × Engine A (Hebbian)

```
🟡 SLEEP ENHANCES ENGINE A QUA REPLAY:

  S2 (Replay) = Engine A hoạt động OFFLINE:
    Replayed patterns → Hebbian strengthen → same mechanism as waking
    Nhưng: COMPRESSED speed (10-20x) = efficient
    Nhưng: NO external input = chỉ strengthen ĐÃ HỌC
    Nhưng: SYSTEMATIC (hippocampus-driven, not random)

  Net effect: Engine A gets "bonus exposure cycles" during sleep.
  = Tại sao "sáng hôm sau nhớ rõ hơn" = more Hebbian cycles occurred.

  S1 (SHY) IMPROVES Engine A efficiency:
    Prune weak connections → next day Engine A runs on CLEANER network
    → Signal-to-noise ratio BETTER → compile quality HIGHER next day
    → = "Fresh start" effect — not new knowledge, but cleaner processing.

  S6 (Gist) creates NEW inputs for Engine A:
    Gist = abstract pattern = new compiled chunk
    → Tomorrow's Engine A can build ON TOP of abstracted knowledge
    → = Expertise Compile: each night compresses → pyramidal stacking


  🟡 Sleep enhances Engine A via 3 mechanisms: framework synthesis
  🟢 Replay = Hebbian during sleep: Wilson & McNaughton 1994
  🟢 SHY improves SNR: Tononi & Cirelli 2014
```

### §3.2 — Sleep × Modulator B (Entity-Valence)

```
🟡 SLEEP CALIBRATES MODULATOR B:

  S5 (Emotional Decoupling) directly affects Entity-Valence:
    → Reduce emotional INTENSITY of entity associations
    → Entity-Valence profile: content preserved, peak valence reduced
    → Sáng hôm sau: entity vẫn có valence, nhưng less REACTIVE

  MECHANISM:
    Khi thức: encounter entity → emotional peak → Engine A compile
    Khi ngủ: S5 strip emotional peak → same entity, lower intensity
    → Next encounter: entity triggers LESS extreme response
    → = Modulator B CALIBRATED: not removed, but TUNED

  VÍ DỤ:
    Cãi nhau với bạn tối qua → emotional peak: angry + hurt
    S5 during REM: amygdala reactivate WITHOUT noradrenaline
    → Emotional tag REDUCED
    → Sáng hôm sau: still remember argument, but feel "less angry"
    → = Entity-Valence [bạn] updated: anger REDUCED, content PRESERVED

  S6 (Gist) also affects Modulator B indirectly:
    → Abstract PATTERNS from entity interactions
    → Long-term: entity structural valence built from gist of MANY interactions
    → = Entity-Compiled.md: 40→200 giờ formation time
      = MANY S6 cycles abstracting entity gist over months


  🟡 S5 calibrates Modulator B: framework synthesis
  🟢 Emotional decoupling: van der Helm 2011
  🟢 Amygdala reactivity reduced after sleep: Walker 2005
```

### §3.3 — Sleep × Sources C (independent of)

```
🟡 SLEEP = INDEPENDENT OF SOURCE CHANNELS:

  Khi ngủ:
    C1 (External) = BLOCKED (thalamic gating, sensory input suppressed)
    C2 (PFC deliberate) = OFFLINE (PFC minimal activity, no deliberate thought)
    C3 (Spontaneous chunk fire) = ACTIVE but in DIFFERENT mode (S2 replay)

  → Sleep operates INDEPENDENT of normal C1/C2/C3 channels.
  → Sleep has its OWN internal activation system (hippocampus-driven replay).
  → = Tại sao sleep = SEPARATE component S, không phải variant của C.


  S2 ≈ C3 VARIANT nhưng KHÁC:

    ┌──────────────────┬──────────────────────┬────────────────────┐
    │                  │ C3 (thức)            │ S2 (ngủ)           │
    ├──────────────────┼──────────────────────┼────────────────────┤
    │ Trigger          │ Context, random      │ Hippocampus-driven │
    │ Speed            │ Normal              │ 10-20x compressed  │
    │ Organization     │ Unstructured        │ Systematic (SWRs)  │
    │ PFC influence    │ Possible (partial)   │ None (offline)     │
    │ External input   │ Possible (C1 mix)    │ None (blocked)     │
    │ Duration         │ Intermittent        │ Sustained (SWS)    │
    │ Efficiency       │ Low                 │ High               │
    └──────────────────┴──────────────────────┴────────────────────┘

    → S2 = "industrial-grade C3" — same principle, different execution.


  🟡 Sleep independent of C1/C2/C3: framework synthesis
  🟢 Thalamic gating during sleep: established polysomnography
  🟢 PFC reduced activity during SWS: established neuroimaging
```

### §3.4 — Sleep × Modulator D (PFC OFFLINE)

```
🟡🟢 SLEEP RESTORES MODULATOR D:

  Khi ngủ: PFC = OFFLINE.
    → Modulator D KHÔNG hoạt động
    → No Hold, no Suppress
    → = "PFC rest mode"

  NHƯNG: sleep RESTORES PFC function cho ngày hôm sau:

  ① Catecholamine restoration:
     PFC-Operations.md §8.3: "Budget recharges via sleep = catecholamine restoration"
     → Dopamine + Norepinephrine pools REFILL during sleep
     → Sáng hôm sau: PFC ĐẦY catecholamine = OPTIMAL performance

  ② Cortisol effects CLEAR:
     Cortisol-Baseline.md: sustained cortisol → gene expression → neural wear
     → Sleep = recovery window → cortisol effects PARTIALLY cleared
     → "Sáng: catecholamine ĐẦY + cortisol effects ÍT = PFC optimal"
     → "Tối: catecholamine CẠN + cortisol effects NHIỀU = PFC yếu"

  ③ Synaptic efficiency restored (S1 SHY):
     → PFC synapses also downscaled → more efficient processing
     → = PFC "refreshed" — same hardware, cleaner connections


  IMPLICATION:
    Sleep deprivation → Modulator D degrades FIRST:
    → PFC = most metabolically expensive brain region
    → PFC = most sensitive to catecholamine depletion
    → = Tại sao mất ngủ → impulsive, emotional, poor judgment
    → = Modulator D (PFC) OFFLINE → Modulator B (Entity-Valence) UNCHECKED
    → = Chi tiết: §4 (Sleep Deprivation).


  🟢 Catecholamine restoration during sleep: Arnsten 2009
  🟢 PFC sensitivity to sleep deprivation: Yoo et al. 2007
  🟡 PFC degrades first under sleep deprivation: framework synthesis
```

---

## §4 — SLEEP DEPRIVATION = ARCHITECTURE DEGRADATION

```
⭐⭐ MẤT NGỦ = TẤT CẢ 6 MECHANISMS BỊ DISRUPT ĐỒNG THỜI:


  ┌──────────────────────────────────────────────────────────────────┐
  │ MECHANISM DISRUPTED   │ CONSEQUENCE                              │
  ├───────────────────────┼──────────────────────────────────────────┤
  │ S1 SHY absent         │ Synapses không prune → noise TÍCH LŨY    │
  │                       │ → Signal-to-noise ratio GIẢM              │
  │                       │ → Next day learning IMPAIRED              │
  ├───────────────────────┼──────────────────────────────────────────┤
  │ S2 Replay absent      │ Patterns không strengthen → FRAGILE      │
  │                       │ → Memory WORSE than pre-sleep             │
  │                       │ → What was learned → not consolidated     │
  ├───────────────────────┼──────────────────────────────────────────┤
  │ S3 Consolidation miss │ Hippocampus → cortex transfer STALLED    │
  │                       │ → Knowledge stuck in "temporary storage" │
  │                       │ → Hippocampus FULL → new learning blocked│
  ├───────────────────────┼──────────────────────────────────────────┤
  │ S4 Creative Link miss │ No remote associations formed             │
  │                       │ → No "eureka moments" next day           │
  │                       │ → Problem-solving capacity REDUCED        │
  ├───────────────────────┼──────────────────────────────────────────┤
  │ S5 Decoupling miss    │ Emotional tags NOT stripped               │
  │                       │ → Emotions ACCUMULATE day-over-day       │
  │                       │ → Reactivity INCREASES                   │
  │                       │ → Trajectory: burnout, PTSD escalation   │
  ├───────────────────────┼──────────────────────────────────────────┤
  │ S6 Gist absent        │ No abstraction → details overwhelm      │
  │                       │ → Can't see "big picture"                │
  │                       │ → Background-Pattern formation slowed    │
  └───────────────────────┴──────────────────────────────────────────┘


  ĐẶC BIỆT: PFC DEGRADES FIRST:

    PFC-Function.md: "PFC capacity GIẢM bởi: sleep deprivation"
    PFC-Operations.md §8.3: catecholamine pools CẠN
    → Modulator D = FIRST CASUALTY of sleep deprivation

    Khi Modulator D fails:
    → Entity-Valence (Modulator B) goes UNCHECKED
    → Emotional reactivity TĂNG (no PFC suppress)
    → Impulsive decisions (no PFC hold alternatives)
    → "Mệt → dễ cáu → không muốn gặp ai → quyết định tệ"

    = ARCHITECTURE COLLAPSE ORDER:
      1st: Modulator D (PFC) → depleted catecholamine
      2nd: S1-S6 maintenance missed → chunks degrade
      3rd: Engine A still runs nhưng trên DIRTY network
      4th: Modulator B unchecked → emotional amplification
      → = Compound degradation


  CORTISOL INTERACTION (Cortisol-Baseline.md):

    Sleep deprivation → cortisol baseline DRIFT UP
    → Cortisol = gene expression effects → neural wear
    → "Phá nhanh, xây chậm":
      Cortisol elevation: hours to days
      Recovery: weeks to months
    → = Sleep debt COMPOUNDS: mỗi đêm mất ngủ = damage > 1 đêm recover

    Chronic sleep deprivation → cortisol chronically elevated
    → All 6 S mechanisms degraded + cortisol damage
    → = Double hit: no maintenance + active damage


  REWARD VULNERABILITY:

    Reward-Signal-Architecture.md:
    → Sleep deprivation degrades Evaluative Reward FIRST
      (complex, compilation-dependent, VTA habituation stacks)
    → Direct-State Reward PERSISTS as "hedonic floor"
      (hardware-based, CT afferents, simple comfort)

    → Mất ngủ: "chỉ muốn ăn ngon, nằm thoải mái"
      = Evaluative reward GONE, Direct-State still accessible
    → = Tại sao sleep-deprived people → comfort food, simple pleasures
    → = Modulator D down → complex reward UNAVAILABLE


  🟢 Sleep deprivation → memory impairment: Walker & Stickgold 2004
  🟢 Sleep deprivation → amygdala hyperactivity: Yoo et al. 2007
  🟢 Sleep deprivation → PFC impairment: Killgore 2010
  🟢 Cortisol × sleep deprivation: Leproult & Van Cauter 2010
  🟢 Arnsten 2009 (catecholamine inverted-U)
  🟡 Architecture collapse order model: framework synthesis
  🟡 Evaluative vs Direct-State vulnerability: framework synthesis
```

---

## §5 — WAKING REST: Partial Alternative, NOT Replacement

```
🟡🟢 WAKING REST CÓ 1 SỐ OVERLAP VỚI SLEEP, NHƯNG KHÔNG THAY THẾ:

  Learning-Cycle.md §5:
    "Sleep is one path for refinement. Waking rest is another.
     Different hardware, different neurochemistry, different strengths."


  WAKING REST MECHANISMS:

  ① DMN activation (Raichle et al. 2001):
     PFC release → Default Mode Network activate
     → Mind-wandering + autobiographical memory + future simulation
     → Some integration of disparate information
     → = Partial S3 (consolidation) + partial S4 (creative links)

  ② Incubation effect (Sio & Ormerod 2009 meta-analysis):
     Pause on problem → solution emerges "spontaneously"
     → DMN + subconscious processing continues in background
     → = Partial S4 (creative linking while awake)

  ③ Walking boosts creativity (Oppezzo & Schwartz 2014):
     Divergent thinking +~60% vs sitting
     → Rhythmic gait + low cognitive load + sensory input
     → = Partial S4 + C1 exposure (novel environment)

  ④ Meditation (Tang et al. 2015):
     Reduces DMN hyperactivity, enhances PFC-DMN coupling
     → Less rumination (negative C3 reduced)
     → Background integration without wandering interference
     → = Partial S5 (emotional regulation) + partial S3 (integration)


  WAKING REST vs SLEEP — COMPARISON:

  ┌──────────────────────┬───────────────────┬──────────────────────┐
  │ Mechanism            │ Waking Rest       │ Sleep                │
  ├──────────────────────┼───────────────────┼──────────────────────┤
  │ S1 SHY (prune)       │ ❌ NOT available  │ ✅ Full              │
  │ S2 Replay (Hebbian)  │ 🟡 Partial (DMN)  │ ✅ Full (SWR)        │
  │ S3 Consolidation     │ 🟡 Partial (slow)  │ ✅ Full (fast)       │
  │ S4 Creative linking  │ 🟡 Partial         │ ✅ Full (REM)        │
  │ S5 Emot. decoupling  │ 🟡 Very partial    │ ✅ Full (REM NE↓)    │
  │ S6 Gist extraction   │ 🟡 Partial          │ ✅ Full              │
  │ PFC restoration      │ ❌ NOT (PFC ON)    │ ✅ Full (catechol.)  │
  │ Cortisol recovery    │ ❌ NOT             │ ✅ Partial           │
  └──────────────────────┴───────────────────┴──────────────────────┘


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
  → Full night sleep = IRREPLACEABLE for complete Component S function.


  🟢 DMN: Raichle et al. 2001
  🟢 Incubation: Sio & Ormerod 2009
  🟢 Walking: Oppezzo & Schwartz 2014
  🟢 Meditation: Tang et al. 2015
  🟡 Waking rest as partial sleep: framework synthesis
```

---

## §6 — OPEN QUESTIONS

```
🔴 CÁC CÂU HỎI CHƯA CÓ ĐÁP ÁN:


  Q1: SLEEP MECHANISMS — SEQUENTIAL HAY CONCURRENT?

     Trong 1 đêm: S1-S6 chạy lần lượt hay song song?
     Evidence gợi ý: SWS mechanisms (S1,S2,S3,S6) mostly sequential with overlap
     REM mechanisms (S4,S5) concurrent within REM episode
     But: cross-cycle interactions chưa rõ
     → Ảnh hưởng gì nếu SWS bị cắt (rượu → suppress SWS)?
     → Ảnh hưởng gì nếu REM bị cắt (antidepressants → suppress REM)?

     🟢 Alcohol suppresses SWS: Ebrahim et al. 2013
     🟢 SSRIs suppress REM: Wilson & Argyropoulos 2005
     🔴 Cross-mechanism interaction during night: needs more research


  Q2: NAPPING — MECHANISM NÀO ACTIVE?

     20-min nap: mainly S1 (SHY partial) + S2 (replay partial)
     90-min nap: 1 full NREM/REM cycle → S1+S2+S3+S4+S5+S6 (all partial)
     → Napping research supports memory improvement (Mednick et al. 2003)
     → But: napping ≠ full night (fewer cycles, less accumulation)
     → How much of Component S does a nap provide? % estimate?

     🟢 Napping benefits: Mednick et al. 2003
     🔴 Quantitative nap vs full night: needs measurement


  Q3: AGE-RELATED SLEEP ARCHITECTURE CHANGES:

     Children: MORE SWS → more S1/S2/S3/S6 → faster consolidation
     Elderly: LESS SWS + LESS REM → S1-S6 ALL reduced
     → = Age-related compile quality decline PARTIALLY explained by sleep?
     → Elderly "learn slower" = Engine A same nhưng Component S degraded?

     🟢 Sleep architecture changes with age: Ohayon et al. 2004
     🔴 S mechanism degradation → compile quality: needs analysis


  Q4: INDIVIDUAL VARIATION IN SLEEP MECHANISMS:

     Genetic: DEC2 mutation → "short sleepers" (6h sufficient)
     → Do short sleepers have MORE EFFICIENT S mechanisms?
     → Or do they simply SKIP some mechanisms?
     → Implications cho compile quality long-term?

     🟢 DEC2 mutation: He et al. 2009
     🔴 Short sleep → compile quality: unknown


  Q5: S5 EMOTIONAL DECOUPLING × TRAUMA:

     PTSD: REM disrupted → S5 fails → trauma emotional tag PERSISTS
     Nightmares = S5 ATTEMPTING but FAILING decoupling
     → Can S5 be artificially enhanced? (Pharmacological? Technological?)
     → Prazosin (α1 blocker) reduces nightmares → possibly enhances S5?

     🟢 PTSD × REM disruption: Germain 2013
     🟢 Prazosin for nightmares: Raskind et al. 2003
     🔴 Enhancing S5 artificially: experimental


  Q6: SLEEP × MODULATOR B CALIBRATION SPEED:

     S5 strips emotional tag PER NIGHT.
     Nhưng: Entity-Valence structural = accumulated over YEARS.
     → S5 chỉ strip CURRENT emotional peak, KHÔNG strip structural valence?
     → Bao nhiêu S5 cycles để shift structural valence measurably?
     → = Tại sao "chia tay lâu rồi mà vẫn buồn" — S5 works on current,
       nhưng structural valence = deep, slow, needs MANY S5 cycles?

     🔴 S5 current vs structural effect: needs analysis


  Q7: COMPILE_RATE FORMULA × SLEEP:

     Current formula: f(exposure × saliency × contingency × peak_valence × multi_modal_richness)
     → Sleep thêm exposure (S2) + modify peak_valence (S5) + modify richness? (S4)
     → Should sleep be an ADDITIONAL parameter in formula?
     → Or: sleep = maintenance of existing parameters, not new parameter?

     🟡 Sleep as parameter vs maintenance: framework decision needed
```

---

## §7 — IMPLICATIONS CHO FRAMEWORK

```
🟡 NẾU SLEEP ANALYSIS NÀY ĐÚNG:


  ① CHUNK.MD §2.1 ④ SLEEP: EXPAND:

     Current: 1 line "④ SLEEP CONSOLIDATION" + Walker 2017 citation
     → EXPAND: multi-mechanism model (6 mechanisms, not just "consolidation")
     → S2 (replay) = the mechanism closest to current §2.1 ④
     → BUT: S1,S3,S4,S5,S6 = 5 additional mechanisms NOT in Chunk.md
     → = Learning-Cycle.md §4.10 đã recommend this expansion


  ② COMPILE-TAXONOMY.md v3.0: ADD SLEEP SECTION:

     → Sleep as Component S: independent offline maintenance
     → Not "4th compile type" — separate system
     → Table mapping: 6 mechanisms × compile architecture components
     → = Drill-Compile-Architecture §12 propagation item


  ③ BODY-BASE.MD: COMPILABLE ARCHITECTURE UPDATE:

     → Compilable Architecture = Engine A + B + C + D + S
     → S = maintenance system that enables sustainable compile over lifetime
     → Without S: Engine A degrades rapidly (days → cognitive impairment)


  ④ BACKGROUND-PATTERN FORMATION:

     → S6 (Gist Extraction) = PRIMARY mechanism tạo Background-Pattern
     → Currently: Background-Pattern.md §3 mentions "sleep gist extraction"
     → Could enrich: S6 as specific mechanism driving Background-Pattern formation
     → Implications: sleep quality → Background-Pattern quality → C3 quality


  ⑤ CORTISOL-BASELINE CROSS-REF:

     → Already mentions sleep as PRIMARY recovery mechanism
     → Could enrich: link to 6 specific mechanisms
     → S5 specifically: emotional decoupling → cortisol reactivity reduced


  ⑥ NEW CONCEPT: ARCHITECTURE COLLAPSE ORDER:

     Sleep deprivation → PFC first → Entity-Valence unchecked → compound
     → This sequence NOT currently in framework
     → Could add to Cortisol-Baseline or PFC-Operations or new section


  ⑦ WAKING REST POSITIONING:

     → Currently: Learning-Cycle.md §5 covers waking rest well
     → Addition: explicit comparison table (§5 this file)
     → Positioning: complement, NOT replacement


  ⭐ PROPAGATION SEQUENCE (combined with Drill-Compile-Architecture):

    Phase 1: Drill-Compile-Architecture ✅ DONE
    Phase 2: Drill-Compile-Sleep ✅ DONE
    Phase 3: Review cả 2 drill → xác nhận insights
    Phase 4: Compile-Taxonomy.md v3.0 REWRITE
    Phase 5: Chunk.md §2.1 ④ expand + §2.3 "gate" → "amplifier"
    Phase 6: Cross-ref updates (Background-Pattern, Cortisol, PFC-Ops, Body-Base)
```

---

## §8 — CROSS-REFERENCES + CITATIONS

### §8.1 — Framework files referenced

```
PRIMARY SOURCE:
  Learning-Cycle.md §4 (6+1 sleep mechanisms, detailed evidence)
  Learning-Cycle.md §5 (waking rest mechanisms)

COMPILE ARCHITECTURE:
  10-Compile-Architecture.md (Engine A + Modulators + Sources — companion drill)

CORE FILES:
  Chunk.md v2.3 §2.1 ④ — Sleep consolidation (→ NEEDS expansion)
  Chunk.md v2.3 §2.2 — compile_rate formula (sleep × formula interaction)
  PFC-Operations.md v1.3 §8.3 — PFC budget recharges via sleep
  PFC-Function.md v1.2 — Sleep deprivation degrades all 24 PFC functions
  Cortisol-Baseline.md v2.2 — Sleep = PRIMARY cortisol recovery, "phá nhanh xây chậm"
  Background-Pattern.md v2.0 §3 — S6 gist extraction → Background-Pattern formation
  Entity-Valence-Dynamics.md v1.1 §5 — VTA habituation × emotional dynamics
  Body-Feedback-Mechanism.md v2.1 §1.2 — 2 genuine sources
  Reward-Signal-Architecture.md v2.1 — Evaluative vs Direct-State vulnerability
  Simulation-Engine.md v1.1 — Constructive Simulation (PFC offline during sleep)
  Body-Base.md v3.3 §2 — Compilable Architecture (→ add Component S)
```

### §8.2 — Research citations

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
  Walker 2017 — Why We Sleep (emotional decoupling)
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

  WAKING REST:
  Raichle et al. 2001 — Default Mode Network
  Sio & Ormerod 2009 — Incubation meta-analysis
  Oppezzo & Schwartz 2014 — Walking × creativity
  Tang et al. 2015 — Meditation neuroscience review
  Mednick et al. 2003 — Napping benefits

  NAPPING + INDIVIDUAL VARIATION:
  He et al. 2009 — DEC2 short sleep mutation
  Maret 2011, Yang 2014 — Dendritic spine turnover
  Gilestro 2009 — Drosophila sleep downscaling


FRAMEWORK SYNTHESIS (🟡):
  Sleep as Component S in compile architecture — session 2026-06-01
  6 mechanisms × exposure classification — session 2026-06-01
  S5 calibrates Modulator B — session 2026-06-01
  S6 → Background-Pattern formation link — session 2026-06-01
  Architecture collapse order (PFC first) — session 2026-06-01
  Waking rest = complement not replacement — session 2026-06-01
  S2 = industrial-grade C3 — session 2026-06-01

DEBATED (🟡):
  Revonsuo 2000 — Threat Simulation Theory (dreaming)
  Stickgold 2002 — EMDR × REM analogy
```

---

> **COMPANION**: 10-Compile-Architecture.md (Engine A + Modulators + Sources)
> **NEXT**: Review cả 2 drill → xác nhận insights → Compile-Taxonomy.md v3.0 REWRITE
