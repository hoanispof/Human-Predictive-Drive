# Core-Hardware — Physical Architecture (Hardware Map)

> **Trạng thái:** v1.1 — 1 trong 2 bản đồ Core v8.0
> **Ngày:** 2026-05-25 (v1.1 — Core-Interface.md → backup, 3→2 bản đồ, Ask-AI.md = dynamic interface)
> **v1.0:** 2026-05-10
> **Bản đồ này:** HARDWARE MAP — CÁI GÌ Ở ĐÂU (physical architecture)
> **Bản đồ khác:** Core-Software.md (CHẠY THẾ NÀO)
> **Tương tác:** Ask-AI.md (AI generate dynamic interface per user)
> **Supersedes:** Core-v7.8-Draft.md v0.2 §1.2 + §6.3 (tách thành 3 file)
> **Nguyên tắc:**
> - 4 zones A/B/C/D theo PFC accessibility gradient
> - Mỗi claim verifiable bằng fMRI, lesion studies, tractography
> - Physical map — KHÔNG mô tả mechanism (→ Core-Software.md)
> - KHÔNG mô tả observer experience (→ Ask-AI.md: AI generate dynamic interface per user)
> **Tiền đề đọc:** Không cần — file này self-contained
> **Đọc sâu hơn:** Neural-Architecture.md v1.0 (chi tiết từng vùng não)
> **Confidence:** 🟢 Research support | 🟡 Framework synthesis | 🔴 Hypothesis
> **Language:** Tiếng Việt primary + English technical terms

---

## Mục lục

- §0 — BA BẢN ĐỒ + FILE NÀY MÔ TẢ GÌ
- §1 — HARDWARE MAP — PHYSICAL ARCHITECTURE
- §2 — PFC REACH GRADIENT
- §3 — TIMING HIERARCHY
- §4 — RECEPTOR SYSTEM OVERVIEW
- §5 — HARDWARE PROFILE — INDIVIDUAL SPECS
- §6 — HARDWARE SETS RANGE, CHUNKS CHOOSE POSITION
- §7 — CROSS-REFERENCES

---

## §0 — BA BẢN ĐỒ + FILE NÀY MÔ TẢ GÌ

### §0.1 Ba bản đồ Core v8.0

Framework mô tả body-brain system từ 2 góc nhìn, mỗi góc = 1 bản đồ:

| # | Bản đồ | Góc nhìn | Đối tượng | File |
|---|---|---|---|---|
| 1 | **Hardware Map** | **CÁI GÌ ở ĐÂU** | **Neuroscience researcher** | **File này** |
| 2 | Software Map | CHẠY THẾ NÀO | Framework researcher | Core-Software.md |

2 bản đồ mô tả CÙNG hệ thống. Khác góc nhìn. Đọc độc lập được.
Giống máy tính: sơ đồ mạch (Hardware) / code architecture (Software).
Tương tác với framework: Ask-AI.md — AI đọc framework, adapt theo mức hiểu của từng người.

### §0.2 File này mô tả gì

Bản đồ VẬT LÝ: CÁI GÌ ở ĐÂU, nối với gì, specs cá nhân.
Cho chuyên gia muốn VERIFY framework bằng fMRI, lesion studies, tractography.

File này KHÔNG mô tả:
- Mechanism (CÁI GÌ CHẠY thế nào) → Core-Software.md
- Observer experience (TƯƠNG TÁC) → Ask-AI.md (AI generate dynamic interface per user)

---

## §1 — HARDWARE MAP — PHYSICAL ARCHITECTURE

```
🟡 BẢN ĐỒ VẬT LÝ — "CÁI GÌ Ở ĐÂU, NỐI VỚI GÌ":

  PFC ở trên cùng — vì mọi người đều quan sát bằng PFC.
  Domain bao bên ngoài — body tồn tại TRONG domain.
  Gradient từ trên xuống: PFC reach GIẢM DẦN.

  ┌─ DOMAIN (môi trường thực — tồn tại khách quan, domain KHÔNG nói dối) ──────┐
  │                                                                              │
  │  ┌─ BODY (neural systems — physical architecture) ─────────────────────┐   │
  │  │                                                                      │   │
  │  │  ┌─ A: PFC ── observer + orchestrator ──────────────────────────┐   │   │
  │  │  │  dlPFC ── working memory (~4±1 slots), planning, control      │   │   │
  │  │  │  vlPFC ── response inhibition, rule maintenance               │   │   │
  │  │  │  OFC ── value computation, reward expectation                 │   │   │
  │  │  │  vmPFC ── emotion regulation, amygdala bridge (uncinate)      │   │   │
  │  │  │  mPFC ── self-referential, social cognition, DMN hub          │   │   │
  │  │  │  ACC* ── conflict monitoring (*PFC/limbic overlap)            │   │   │
  │  │  │  Online from birth (PFC-From-Prenatal). ⏱ ~200-500ms (SLOWEST)             │   │   │
  │  │  └─────────────────────────┬────────────────────────────────────┘   │   │
  │  │     Layer 2/3 connections — PFC reach: STRONG                       │   │
  │  │  ┌─────────────────────────┴────────────────────────────────────┐   │   │
  │  │  │  B: CORTICAL MODALITY ── PFC trainable ────────────────────   │   │   │
  │  │  │  Visual (V1→IT, FFA)  Auditory (A1)  Language (Broca+W)       │   │   │
  │  │  │    ⭐ Language dissociable from PFC (Fedorenko 2024)           │   │   │
  │  │  │  Somatosensory (S1/S2)  Motor (M1+premotor)                   │   │   │
  │  │  │  Cerebellum (motor+cognitive+prediction)                       │   │   │
  │  │  │  Insula (⭐ anterior = interoception integration, Craig 2002)  │   │   │
  │  │  │  Parietal (spatial, cross-modal)  Temporal (objects, social)    │   │   │
  │  │  │  ⏱ ~150-200ms cortical processing                             │   │   │
  │  │  └─────────────────────────┬────────────────────────────────────┘   │   │
  │  │     thalamocortical + BG loops — PFC reach: VARIABLE                │   │
  │  │  ┌─────────────────────────┴────────────────────────────────────┐   │   │
  │  │  │  C: SUBCORTICAL ── PFC reach limited ────────────────────     │   │   │
  │  │  │  Amygdala ── threat/reward ── vmPFC direct (uncinate)         │   │   │
  │  │  │  Hippocampus ── encoding gateway ── sleep replay → cortex     │   │   │
  │  │  │  Thalamus + TRN ── sensory gateway ── PFC can gate            │   │   │
  │  │  │  Hypothalamus ── HPA axis, homeostasis ── PFC indirect        │   │   │
  │  │  │  Basal Ganglia ── habit loops (associative → sensorimotor)    │   │   │
  │  │  │  Brainstem: VTA (dopamine), LC (NE, α1→PFC offline),         │   │   │
  │  │  │    Raphe (serotonin), PAG (pain/defense), NTS (visceral)      │   │   │
  │  │  │  DMN cross-cuts: mPFC(A) + PCC + angular + MTG               │   │   │
  │  │  │  ⏱ ~12ms amygdala (subcortical shortcut)                      │   │   │
  │  │  └─────────────────────────┬────────────────────────────────────┘   │   │
  │  │     vagus (80% afferent), spinal paths — PFC reach: WEAK           │   │
  │  │  ┌─────────────────────────┴────────────────────────────────────┐   │   │
  │  │  │  D: PERIPHERAL ── outside brain, PFC reach ≈ 0 ────────────  │   │   │
  │  │  │  ENS "second brain" (~100-500M neurons, 95% serotonin)        │   │   │
  │  │  │  Spinal cord (reflex, pain: A-delta + C-fiber)                │   │   │
  │  │  │  ANS (sympathetic / parasympathetic)                           │   │   │
  │  │  │    Breathing = UNIQUE voluntary-involuntary bridge             │   │   │
  │  │  │  Cardiac plexus (~40K neurons)                                 │   │   │
  │  │  │  ⏱ ~50ms spinal reflex (FASTEST — before brain)               │   │   │
  │  │  └──────────────────────────────────────────────────────────────┘   │   │
  │  │                                                                      │   │
  │  └──────────────────────────────────────────────────────────────────────┘   │
  │                                                                              │
  └──────────────────────────────────────────────────────────────────────────────┘
```

---

## §2 — PFC REACH GRADIENT

```
🟢 PFC REACH — GRADIENT, KHÔNG BINARY:

  PFC "reach" = mức độ PFC có thể influence activity ở vùng đó.
  Quyết định bởi physical connectivity: axon pathways + synaptic relays.

  A → B: STRONG
    → Layer 2/3 direct connections (top-down bias)
    → PFC hold chunk → cortical area activate + run
    → TRN (thalamic reticular nucleus) = attention gate PFC can control
    → Example: PFC hold "viết chữ" → motor cortex execute
    → 🟢 Miller & Cohen 2001 — top-down control mechanism

  A → C: VARIABLE
    → vmPFC → amygdala DIRECT via uncinate fasciculus — emotion regulation
    → PFC → Basal Ganglia (indirect cortico-striatal loops) — habit influence
    → PFC → PAG/NTS (limited, multi-relay) — pain modulation, autonomic
    → NHƯNG: PFC KHÔNG direct access hippocampus encoding process
    → NHƯNG: PFC KHÔNG direct control VTA dopamine firing
    → 🟢 Ghashghaei et al. 2007 — prefrontal-amygdala connectivity

  A → D: WEAK
    → Minimum 2 synaptic relays (PFC → brainstem → peripheral)
    → PFC gần KHÔNG reach: ENS (ruột), cardiac plexus, spinal reflex
    → UNIQUE EXCEPTION: Breathing
      → Voluntary: hold breath, deep breath (motor cortex → diaphragm)
      → Involuntary: brainstem controls (sleep, reflex, CO2 response)
      → = ONLY zone D system PFC can directly influence
    → 🟢 Del Negro et al. 2018 — respiratory rhythm generation

  ⭐ IMPLICATIONS:
    → PFC = observer + orchestrator → nhưng orchestra CHỈ mạnh ở zone A+B
    → Zone C: PFC influence via INDIRECT pathways only
    → Zone D: PFC gần bất lực (trừ breathing)
    → "Ý chí" = PFC hold → bias zone B → hope for cascade tới C, D
    → = Tại sao "control yourself" fundamentally limited — PFC physical reach limited
    → Chi tiết mechanism: Core-Software.md §6.1-§6.2
```

---

## §3 — TIMING HIERARCHY

```
🟢 TIMING — PFC LUÔN BIẾT SAU CÙNG:

  ┌──────┬──────────┬───────────────────────────────────────────────────┐
  │ Zone │ Timing   │ Cái gì xảy ra                                     │
  ├──────┼──────────┼───────────────────────────────────────────────────┤
  │ D    │ ~50ms    │ Spinal reflex (FASTEST — trước brain)             │
  │ C    │ ~12ms    │ Amygdala subcortical shortcut (thalamus→amygdala) │
  │ B    │ ~150ms   │ Cortical processing (visual, auditory, motor)     │
  │ A    │ ~200ms+  │ PFC deliberate (SLOWEST — observer arrives LAST)  │
  └──────┴──────────┴───────────────────────────────────────────────────┘

  EVOLUTIONARY LOGIC:
    → D fastest: tay rụt lại TRƯỚC khi biết nóng (survival reflex)
    → C fast: amygdala fire TRƯỚC PFC aware (threat detection)
    → B medium: cortical integration → recognize object/pattern
    → A slowest: PFC evaluate + plan → only AFTER body đã xử lý xong

  IMPLICATIONS:
    → Body process TRƯỚC → PFC LUÔN biết SAU CÙNG
    → Feeling "tôi quyết định" thực ra = PFC observe decision ĐÃ HÌNH THÀNH
    → 🟢 Libet 1983: readiness potential 300ms TRƯỚC conscious will
    → = Timing hierarchy supports "PFC = observer, not controller"

  CROSS-REFERENCE:
    → NE α1 FREEZE (Cortisol-Baseline.md §9.1):
      Threat → NE flood → PFC OFFLINE (ms) — design feature, NOT malfunction
      Tắt PFC (slow) → nhường subcortical (fast) cho survival
    → Chi tiết mechanism: Core-Software.md §4.3
```

---

## §4 — RECEPTOR SYSTEM OVERVIEW

```
🟢🟡 17 RECEPTOR CATEGORIES — BODY-DOMAIN INTERFACE:

  Receptors = cửa ngõ body nhận input từ domain.
  3 taxonomy chuẩn neuroscience:

  EXTEROCEPTION — sensing external world (5):
    ① Vision     — retina, V1→IT pathway, FFA (faces)
    ② Audition   — cochlea, A1, voice processing
    ③ Olfaction   — ~400 receptor types, DIRECT limbic (bypass thalamus)
    ④ Gustation   — 5+1 basic tastes, chemo-receptors tongue/palate
    ⑤ Tactile     — mechanoreceptors + CT affective touch fibers

  PROPRIOCEPTION — sensing body position (3):
    ⑥ Proprioception — muscle spindles + joint receptors
    ⑦ Vestibular     — inner ear semicircular canals + otoliths
    ⑧ Kinesthetic    — muscle dynamics, exertion, fatigue sensing

  INTEROCEPTION — sensing internal state (9):
    ⑨ Thermoreception   — hypothalamic, ~37°C set point
    ⑩ Nociception       — A-delta (fast sharp) + C-fiber (slow dull)
    ⑪ Respiratory       — CO2 chemoreception, vagal afferents
    ⑫ Cardiovascular    — baroreceptors, HR, HRV, vagal tone
    ⑬ Visceral          — ENS (~100-500M neurons), gut-brain axis
    ⑭ Metabolic         — glucose, hydration, ghrelin/leptin
    ⑮ Hormonal-sensed   — cortisol, testosterone, oxytocin (downstream effects)
    ⑯ Sleep/Circadian   — SCN master clock, melatonin, REM/NREM
    ⑰ Self-signal interoception (META, KEYSTONE) ⭐

  ⭐ SELF-SIGNAL INTEROCEPTION = KEYSTONE:
    → Body's capacity to READ own internal state
    → Hub: anterior insula (zone B, Craig 2002, 2009) + ACC
    → WITHOUT this: other inputs fire but body "cannot hear itself"
    → Explains alexithymia (~10% population, 🟢 Bird & Cook 2013)
    → Developmental foundation: caregiver mirroring → child learns self-reading

  HARDWARE PATHWAYS:
    → Exteroception: receptor → thalamus (zone C) → cortical area (zone B)
    → Exception: olfaction → DIRECT limbic (zone C, bypass thalamus)
    → Interoception: vagus (80% afferent) + spinal → insula (zone B)
    → Nociception: dual pathway (A-delta fast via zone C, C-fiber slow)

  CHI TIẾT: Body-Input-Enumeration.md (8-field schema mỗi input)
  MECHANISM (delta rule, baseline adaptation): Core-Software.md §3
```

---

## §5 — HARDWARE PROFILE — INDIVIDUAL SPECS

```
🟢🟡 HARDWARE SPECS CÁ NHÂN — THAY ĐỔI CHẬM:

  Mỗi người có hardware profile khác nhau.
  Hardware = RANGE. Chunks chọn VỊ TRÍ trong range (§6).
  Thay đổi rất chậm (genetic + epigenetic + structural development).

  ── PFC PARAMETERS ──

    WM CAPACITY: ~4±1 slots (🟢 Cowan 2001)
      → Beginner: slot = small chunk → ít info
      → Expert: slot = meta-chunk → CỰC NHIỀU info
      → = "Cùng 4 slots, khác SIZE mỗi slot"

    PFC-CLEAR-SPEED: COMT gene
      → Val/Val: clear dopamine nhanh → WM refresh nhanh → good for switch
      → Met/Met: clear chậm → WM hold lâu → good for sustained attention
      → 🟢 Egan et al. 2001 — COMT-WM relationship

    PFC-ATTENTION: DRD4 gene
      → 7R: longer receptor → novelty seeking tendency higher
      → 4R: shorter receptor → attention stability higher
      → 🟢 Swanson et al. 2007

    PFC ONLINE FROM BIRTH (🟢 PFC-From-Prenatal):
      → 5 empirical pillars:
        Huttenlocher 1979: synaptic density at birth
        Doria 2010: functional networks at term
        Kouider 2013: frontal signatures at 5 months
        Grossmann 2009: fNIRS early PFC activity
        Hodel 2018: rapid plasticity
      → OLD claim: "PFC offline until X age"
      → CORRECTED: "PFC hardware online from birth, development = CHUNKS MISSING"

    PFC CONNECTIVITY LIMITS:
      → PFC connections chủ yếu tới cortical areas (zone B)
      → LIMITED direct connections tới brainstem, ENS, amygdala
      → PFC CÓ THỂ: fire pattern ở zone B qua top-down bias
      → PFC KHÔNG THỂ: force fire ở zone D (ENS) hay trực tiếp zone C (VTA)
      → PFC orchestrate scope = f(physical connectivity)
      → 🟢 Measurable via fMRI, tractography — individual variation lớn

    PFC-INFERENCE LADDER (Chunk.md §8.4):
      L0: Reflex (no PFC involvement)
      L1: Orienting (PFC receives alert from body)
      L2: Pattern-match (PFC recognizes compiled pattern)
      L3: Deliberate comparison (Type 4 PFC chain)
      L4: Coordinated execution (multi-step PFC plan)
      → EVENT property, not AGE property

  ── BODY-WIDE PARAMETERS ──

    MOOD-STABILITY: MAO-A gene
      → Toàn não, không riêng PFC
      → Affects monoamine metabolism (serotonin, dopamine, NE)
      → 🟢 Caspi et al. 2002 — interaction with early adversity

    RECEPTOR VARIANTS:
      → OXTR: oxytocin receptor sensitivity (social bonding range)
      → TAS2R: bitter taste receptor (taste sensitivity range)
      → CT-fiber density: affective touch sensitivity
      → = Individual variation → different body-input sensitivity profiles

    MODALITY BALANCE:
      → Visual / auditory / somatic / motor / emotional processing mix
      → Property of TOÀN BỘ brain, không riêng PFC hay Unconscious
      → Ảnh hưởng: cách chunks compile (multi-modal richness)
        và cách PFC observe (modality nào dominant)
      → 🟡 Mainstream chưa define rõ boundary PFC vs unconscious cho modality
      → Framework position: modality = brain-wide hardware property

  CHI TIẾT PFC FUNCTIONS: PFC-Function.md v1.1 (24 functions, sub-region mapping)
  CHI TIẾT PFC MODES: PFC-Configuration.md v1.0 (6 dynamic configuration modes)
```

---

## §6 — HARDWARE SETS RANGE, CHUNKS CHOOSE POSITION

```
🟡 KEY PRINCIPLE — HARDWARE ≠ DESTINY:

  Hardware = RANGE of possible positions.
  Chunks (tích lũy qua trải nghiệm) = ACTUAL POSITION within range.

  VÍ DỤ:
    WM capacity ~4±1 → beginner: 4 small items | expert: 4 meta-chunks
    COMT Val/Val → fast clear → nhưng chỉ hữu ích khi chunks cho task switching đã compiled
    DRD4 7R → novelty seeking tendency → nhưng direction nào phụ thuộc environmental exposure

  = KHÔNG PHẢI "PFC mạnh/yếu"
  = MÀ "chunks compiled bao nhiêu cho tình huống đó"

  Hardware khác nhau → optimal environment khác nhau → chunks compile khác nhau.
  CÙNG hardware + KHÁC environment → KHÁC outcomes hoàn toàn.
  KHÁC hardware + CÙNG environment → KHÁC adaptation strategies.

  FRAMEWORK POSITION:
    → Individual variation = hardware × environment × time
    → Talent = early compile advantage (environment happens to match hardware)
    → Not fixed destiny — chunks continue to compile throughout life
    → Critical periods: some hardware windows close
      (phoneme discrimination ~7-10yr, attachment style ~1-3yr)

  CHI TIẾT MECHANISM: Core-Software.md §4.1 (compile rate, 3 Compile Types)
```

---

## §7 — CROSS-REFERENCES

### §7.1 Bản đồ khác + Tương tác

```
  Core-Software.md   — CHẠY THẾ NÀO: cycle mechanism, chunk dynamics, body-feedback
  Ask-AI.md v3.1     — TƯƠNG TÁC: AI generate dynamic interface per user (protocol + navigation)
```

### §7.2 Mapping Hardware ↔ Software

```
  Core-Software.md §1.3: mapping table (Software function → Hardware location)
  = "Body-Input ở Receptors→D+C+B, PFC observe ở A, Cortisol amplifier ở C→xuyên"
```

### §7.3 Hardware deep-dive files

```
  Neural-Architecture.md v1.0      — chi tiết từng vùng não, 4 zones A/B/C/D expanded
  Body-Input-Enumeration.md        — 17 body-inputs, 8-field schema mỗi input
  Cortisol-Baseline.md v2.0        — HPA axis (zone C), NE mechanism, 7 modes
  PFC-Function.md v1.1             — 24 PFC functions, sub-region mapping
  PFC-Configuration.md v1.0        — 6 dynamic modes, survival matrix
```

### §7.4 Superseded content

```
  Core-v7.8-Draft.md v0.2 §1.2     → replaced by this file §1 (Hardware Map diagram)
  Core-v7.8-Draft.md v0.2 §6.3     → replaced by this file §5 (Hardware Profile)
  Backup: _backup/Core-v7.8-Draft-pre-3maps.md
```

---

## Closing note

**Core-Hardware v1.1** — 1 trong 2 bản đồ Core v7.8.

Bản đồ phần cứng: CÁI GÌ ở ĐÂU, nối với gì, specs cá nhân.
Ngắn nhất trong 2 file — intentionally brief.
Chuyên gia có thể verify từng vùng não bằng fMRI, lesion studies, tractography.

Muốn biết CHẠY THẾ NÀO → Core-Software.md.
Muốn TƯƠNG TÁC với framework → Ask-AI.md (AI generate dynamic interface per user).

> *Core-Hardware — "4 zones A/B/C/D. PFC reach gradient: A→B strong, A→C variable,
> A→D weak. Timing: D fastest (50ms) → A slowest (200ms+). 17 receptor categories.
> Hardware sets RANGE, chunks choose POSITION. Hardware ≠ destiny.
> PFC hardware online from birth — development = chunks missing."*
