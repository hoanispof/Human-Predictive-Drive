---
title: Neural-Architecture — Bản Đồ Sinh Lý Neural cho Framework
version: 1.2
created: 2026-04-19
refined: 2026-06-04 (v1.2 — +§7 Bilateral Architecture: horizontal Left↔Right connectivity, corpus callosum, lateralization, "unity = emergent from harmony" principle. Sections renumbered: old §7-§10 → §8-§11)
previous: 2026-05-23 (v1.1 — Concept Cascade: +Simulation-Engine, +Entity-Access, +modality mapping refinement)
status: v1.2 REFERENCE FILE
scope: |
  Physical map của neural systems: PFC, Cortical Modality Areas,
  Subcortical Structures, Peripheral Neural Systems.
  WHAT connects WHERE. WHO does WHAT. PFC reach LIMITS.
  v1.2: +Bilateral Architecture (Left↔Right), corpus callosum integration layer.
  Functional map cho framework — không phải neuroscience textbook.
purpose: |
  Nền tảng sinh lý cho Core-v7.8-Draft.md.
  Thay thế "Unconscious" box mờ bằng liệt kê CỤ THỂ.
  Mỗi claim = verifiable, specific brain area, citable research.
  Mainstream researcher có thể trực tiếp: công nhận / phản đối / tinh chỉnh.
principle: |
  Chỉ liệt kê những gì research ĐÃ CÔNG BỐ.
  Không bịa vùng não không tồn tại.
  Thẳng thắn về những gì CHƯA RÕ.
  Map domain real về neural — kết quả thực tế chỉ có một.
related: |
  Neural-Processing-Flow.md — signal pathways chi tiết (sensor → cortex)
  Modality-Analysis.md — modality encoding analysis
  Chunk.md v2.0 — chunk mechanism chạy trên neural substrate
  Core-v7.8-Draft.md — kiến trúc tổng thể dùng file này làm physical map
language: Tiếng Việt primary + English technical terms
confidence: 🟢 Research support | 🟡 Framework synthesis | 🔴 Hypothesis
---

# Neural-Architecture — Bản Đồ Sinh Lý Neural cho Framework

> **Framework nói "chunks compile", "PFC observe", "body-feedback fire".**
> Nhưng xảy ra Ở ĐÂU trong cơ thể? Vùng não NÀO? Con đường NÀO?
>
> File này: bản đồ SINH LÝ — map framework concepts lên physical neural systems.
>
> **Không dùng "Unconscious" như 1 box mờ.**
> Thay vào đó: liệt kê CỤ THỂ từng vùng, từng function, từng connection.
> Mainstream researcher có thể nhìn vào từng dòng và verify/challenge.
>
> **4 phân vùng** (theo PFC accessibility — gradient, không binary):
>   A. PFC — observe, hold, imagine, orchestrate
>   B. Cortical Modality Areas — processing chuyên biệt, PFC có thể bias
>   C. Subcortical Structures — deep brain, PFC reach hạn chế
>   D. Peripheral Neural Systems — outside brain, PFC gần không reach

---

## Mục lục

- §0 — TẠI SAO FILE NÀY
- §1 — TỔNG QUAN: 4 PHÂN VÙNG
- §2 — A: PFC (Prefrontal Cortex)
- §3 — B: CORTICAL MODALITY AREAS
- §4 — C: SUBCORTICAL STRUCTURES
- §5 — D: PERIPHERAL NEURAL SYSTEMS
- §6 — CONNECTIVITY MAP
- §7 — BILATERAL ARCHITECTURE: Left ↔ Right (v1.2)
- §8 — CHUNK COMPILATION ACROSS A/B/C/D
- §9 — IMPLICATIONS CHO FRAMEWORK
- §10 — HONEST ASSESSMENT
- §11 — CROSS-REFERENCES

---

## §0 — TẠI SAO FILE NÀY

```
VẤN ĐỀ VỚI "UNCONSCIOUS":

  Framework trước dùng "Unconscious" = tất cả non-PFC processing.
  = Gộp visual cortex + amygdala + ruột + tim + brainstem vào 1 từ.
  = Che giấu: mỗi phần hoạt động KHÁC NHAU, function RIÊNG.

  Mainstream CŨNG mơ hồ:
    "Unconscious processing" = catch-all
    "Subconscious" = mơ hồ hơn nữa
    Không ai define rõ boundary

  NHƯNG neuroscience ĐÃ MAP khá rõ từng vùng:
    → Vùng nào ở đâu (anatomy — 🟢 established)
    → Vùng nào connect vùng nào (tractography — 🟢 Human Connectome Project)
    → Vùng nào làm gì (fMRI, lesion studies — 🟢 extensive literature)
    → = KHÔNG CẦN che giấu bằng 1 từ chung

  FILE NÀY:
    → Liệt kê CỤ THỂ từng phần neural system
    → Map framework concepts (chunks, PFC observe, body-feedback) lên physical areas
    → Thẳng thắn về PFC reach limits
    → Cho phép mainstream verify từng claim
```

---

## §1 — TỔNG QUAN: 4 PHÂN VÙNG

```
🟡 4 PHÂN VÙNG THEO PFC ACCESSIBILITY (gradient, không binary):

  ┌─────────────────────────────────────────────────────────────┐
  │ A. PFC (Prefrontal Cortex)                                   │
  │    = Observe + Hold + Imagine + Orchestrate                  │
  │    = Framework: "conscious processing"                       │
  │    Sub-regions: dlPFC, vlPFC, OFC, vmPFC, mPFC, ACC*         │
  ├─────────────────────────────────────────────────────────────┤
  │ B. CORTICAL MODALITY AREAS                                   │
  │    = Processing chuyên biệt theo modality                    │
  │    = PFC CÓ THỂ bias, gate attention, training               │
  │    Areas: Visual, Auditory, Language, Somatosensory,         │
  │           Motor, Insula, Parietal, Temporal, Cerebellum*     │
  ├─────────────────────────────────────────────────────────────┤
  │ C. SUBCORTICAL STRUCTURES                                    │
  │    = Deep brain structures                                   │
  │    = PFC reach HẠN CHẾ (some direct, some indirect)          │
  │    Areas: Amygdala, Hippocampus, Thalamus, Hypothalamus,     │
  │           Basal Ganglia, Brainstem nuclei (VTA, LC, Raphe,   │
  │           PAG, NTS)                                          │
  ├─────────────────────────────────────────────────────────────┤
  │ D. PERIPHERAL NEURAL SYSTEMS                                 │
  │    = Outside brain, trong cơ thể                             │
  │    = PFC GẦN KHÔNG reach trực tiếp                           │
  │    Systems: ENS (gut), Spinal cord, ANS (sympathetic +       │
  │             parasympathetic), Cardiac plexus                 │
  └─────────────────────────────────────────────────────────────┘

  ⚠️ 4 PHÂN VÙNG = GRADIENT, KHÔNG BINARY:
    → PFC reach GIẢM DẦN từ A → B → C → D
    → Không có boundary sạch sẽ giữa các vùng
    → ACC: overlap A/C (PFC hay limbic? — debated)
    → Cerebellum: overlap B/C (cortical-like processing, subcortical location)
    → Insula: overlap B/C (cortical nhưng deep function)
```

---

## §2 — A: PFC (Prefrontal Cortex)

```
🟢 PFC = VÙNG VỎ NÃO PHÍA TRƯỚC (frontal lobe, anterior)

  SUB-REGIONS + FUNCTIONS:

  ┌──────────┬──────────────────────────────────────────────────────┐
  │ Sub-region│ Primary function                                     │
  ├──────────┼──────────────────────────────────────────────────────┤
  │ dlPFC    │ Working memory, planning, cognitive control           │
  │          │ = Framework: "Hold ~4±1 slots", Type 4 linking       │
  │          │ 🟢 Fuster 1973, Goldman-Rakic 1995                    │
  ├──────────┼──────────────────────────────────────────────────────┤
  │ vlPFC    │ Response inhibition, rule maintenance                 │
  │          │ = Framework: "inhibit compiled response khi cần"     │
  │          │ 🟢 Aron et al. 2004                                   │
  ├──────────┼──────────────────────────────────────────────────────┤
  │ OFC      │ Value computation, reward expectation, flexibility    │
  │          │ = Framework: valence evaluation at PFC level          │
  │          │ 🟢 Rolls 2000, Padoa-Schioppa 2011                    │
  ├──────────┼──────────────────────────────────────────────────────┤
  │ vmPFC    │ Emotion regulation, self-referential, somatic marker  │
  │          │ = Framework: BRIDGE body signals → conscious access   │
  │          │ = Direct connection to amygdala (uncinate fasciculus) │
  │          │ 🟢 Damasio 1994, Ghashghaei 2007                      │
  ├──────────┼──────────────────────────────────────────────────────┤
  │ mPFC     │ Self-referential thought, social cognition, DMN hub   │
  │          │ = Part of Default Mode Network                       │
  │          │ = Framework: self-assessment chunks, identity schemas │
  │          │ 🟢 Raichle 2001, Buckner 2008                         │
  ├──────────┼──────────────────────────────────────────────────────┤
  │ ACC*     │ Conflict monitoring, error detection, effort          │
  │          │ = Framework: "body vote" smooth vs resistance signal  │
  │          │ * Debated: PFC hay limbic? Functional overlap cả hai │
  │          │ 🟢 Botvinick et al. 2004                              │
  └──────────┴──────────────────────────────────────────────────────┘

  PFC HARDWARE PROPERTIES:
    → Online from BIRTH (🟢 Huttenlocher 1979, Doria 2010, Kouider 2013)
    → Newborn PFC = hardware present, CHUNKS MISSING (PFC-From-Prenatal reframe)
    → Layer 2/3 DÀY nhất → broadest cortex-cortex connectivity
    → WM capacity: ~4±1 items (🟢 Cowan 2001)
    → COMT gene: Val/Val = fast clear, Met/Met = slow clear
    → DRD4 gene: ảnh hưởng VTA-PFC attention sensitivity
    → ~30% inhibitory neurons → strong gate/brake function

  PFC TRONG FRAMEWORK:
    → OBSERVE: đọc integrated output từ B+C qua feeling bridge
    → HOLD: giữ chunks active trong WM (~4±1)
    → TYPE 4 LINKING: deliberate chaining ("thinking") — Chunk.md §3
    → IMAGINATION: combine chunks → simulate chưa xảy ra
    → DOMAIN-CHECK: verify body-smooth vs reality (Domain-Checked vs Self-Referencing)
    → ORCHESTRATE: hold goals → bias B areas via top-down
    → GATE: control thalamus qua TRN → chọn sensory channels
    → INHIBIT: suppress compiled responses ("đừng nói vậy")

  PFC LIMITATIONS:
    → Phải NHẬN feeling từ body — không feel trực tiếp
    → Không compile chunks tự động — B+C compile, PFC observe
    → Không override body-base khi signal quá mạnh
    → Processing CHẬM hơn subcortical pathways (~200ms vs ~12ms amygdala)
    → OFFLINE khi: say rượu (GABA), ngủ sâu (NREM),
      NE α1 flood (acute threat), severe cortisol overload

  PFC OFFLINE — EVIDENCE:
    🟢 Say rượu: VẪN nói (Broca), VẪN đi (motor), VẪN đánh nhau (amygdala)
       → KHÔNG nhớ hôm sau = hippocampal encoding failure
       → = B+C+D CHẠY BÌNH THƯỜNG không cần PFC
    🟢 Sleepwalking: PFC offline (NREM) → VẪN đi lại, mở cửa, nấu ăn
    🟢 Split-brain: tay trái (right hemisphere) grab → left PFC confabulate lý do
       → 🟢 Sperry, Gazzaniga 1960s
    🟢 Blindsight: V1 hỏng → BÁO "không thấy" → VẪN dodge objects
       → 🟢 Weiskrantz 1986
```

---

## §3 — B: CORTICAL MODALITY AREAS

```
🟢 CORTICAL AREAS CHUYÊN XỬ LÝ TỪNG LOẠI THÔNG TIN:

  Cùng 6-layer architecture (🟢 Mountcastle 1957),
  khác ở wiring + layer thickness + receptor density.
  PFC CÓ THỂ interact qua Layer 2/3 connections + TRN gating.
  TÁCH BIỆT khỏi PFC (🟢 Fedorenko et al. 2024 — dissociable networks).


  ┌─────────────────────────────────────────────────────────────────┐
  │ VISUAL CORTEX (V1-V5, IT, FFA)                                  │
  │   Location: Occipital lobe                                      │
  │   Function: hình ảnh, pattern, faces, spatial, motion            │
  │   Hierarchy: V1(edges) → V2(contours) → V4(shapes) → IT(objects)│
  │   PFC reads IT (compiled patterns), KHÔNG đọc V1 (raw pixels)  │
  │   Framework: chunks visual compile ở đây                        │
  │   PFC bias: "tìm mặt người" → FFA amplify                      │
  │   🟢 Hubel & Wiesel 1959 (Nobel), Kanwisher 1997 (FFA)          │
  ├─────────────────────────────────────────────────────────────────┤
  │ AUDITORY CORTEX (A1, Heschl's gyrus)                             │
  │   Location: Temporal lobe (superior temporal gyrus)              │
  │   Function: âm thanh, giọng nói, rhythm, pitch, music           │
  │   Tonotopic mapping: tần số → vị trí trên cortex                │
  │   Framework: chunks auditory compile ở đây                      │
  │   🟢 Hickok & Poeppel 2007 (dual stream model)                   │
  ├─────────────────────────────────────────────────────────────────┤
  │ LANGUAGE AREAS (Broca + Wernicke + Arcuate fasciculus)           │
  │   Broca (frontal): sản xuất ngôn ngữ + sequential processing    │
  │   Wernicke (temporal): hiểu ngôn ngữ                             │
  │   Arcuate fasciculus: white matter tract nối Broca ↔ Wernicke    │
  │   ⭐ TÁCH BIỆT khỏi PFC reasoning (🟢 Fedorenko et al. 2024):   │
  │     Language network = "natural kind" — dissociable từ           │
  │     Multiple Demand network (PFC reasoning)                      │
  │     → Hỏng language: không nói, VẪN reasoning ✓                 │
  │     → Hỏng MD: không reasoning, VẪN nói ✓                       │
  │   Say rượu VẪN nói = language areas chạy không cần PFC           │
  │   Framework: communication modality, label system, sequential    │
  │   🟢 Fedorenko, Ivanova & Regev 2024 (Nature Reviews Neuroscience)│
  ├─────────────────────────────────────────────────────────────────┤
  │ SOMATOSENSORY CORTEX (S1, S2)                                    │
  │   Location: Parietal lobe (postcentral gyrus)                    │
  │   Function: touch, pressure, proprioception, body position       │
  │   Somatotopic mapping (homunculus): body → cortex position       │
  │   Framework: body-knowledge chunks compile ở đây                 │
  │   🟢 Penfield & Boldrey 1937                                      │
  ├─────────────────────────────────────────────────────────────────┤
  │ MOTOR CORTEX (M1) + PREMOTOR + SUPPLEMENTARY MOTOR              │
  │   Location: Frontal lobe (precentral gyrus)                      │
  │   Function: voluntary movement execution                        │
  │   PFC hold intention → premotor plan → M1 execute → spinal cord │
  │   Framework: motor chunks auto-execute (PFC hold "viết con chó")│
  │   🟢 Penfield 1950, Rizzolatti & Luppino 2001                    │
  ├─────────────────────────────────────────────────────────────────┤
  │ CEREBELLUM ⭐                                                     │
  │   Location: posterior fossa (dưới occipital)                     │
  │   Function: KHÔNG CHỈ motor — CŨNG cognitive + emotional         │
  │     Motor: timing, coordination, skill refinement                │
  │     Cognitive: Crus I, II — social mentalizing, language          │
  │     Emotional: lobule IX — affective processing                  │
  │     Prediction: generates predictions, compares to actual         │
  │   Framework: chunk timing, skill compilation, prediction engine  │
  │   🟢 Schmahmann 1998 (cerebellar cognitive affective syndrome)    │
  │   🟢 2024 meta-analysis: 1,000+ fMRI, 44,500 participants        │
  ├─────────────────────────────────────────────────────────────────┤
  │ INSULA (anterior + posterior) ⭐                                  │
  │   Location: deep trong lateral sulcus                            │
  │   Posterior: raw interoceptive signals arrive                     │
  │   Mid: re-representation                                         │
  │   Anterior: INTEGRATION HUB — all subjective feelings            │
  │   Von Economo neurons: rapid interhemispheric communication      │
  │   Framework: self-signal interoception KEYSTONE (§4.2.3.9)       │
  │   Craig propose: anterior insula = neural correlate of awareness │
  │   🟢 Craig 2002, 2009 (Nature Reviews Neuroscience)               │
  ├─────────────────────────────────────────────────────────────────┤
  │ PARIETAL CORTEX (posterior parietal, angular gyrus)               │
  │   Function: spatial processing, attention, multisensory          │
  │   Angular gyrus: semantic integration, mathematical cognition    │
  │   Part of DMN (angular gyrus)                                    │
  │   Framework: cross-modal binding, spatial chunks                 │
  │   🟢 Colby & Goldberg 1999                                        │
  ├─────────────────────────────────────────────────────────────────┤
  │ TEMPORAL CORTEX (IT, MTG, STS)                                   │
  │   IT: object recognition, face recognition                      │
  │   MTG: semantic memory, word meaning                             │
  │   STS: social perception, biological motion                     │
  │   Part of DMN (MTG)                                              │
  │   Framework: object chunks, social perception chunks             │
  │   🟢 Martin 2007                                                   │
  └─────────────────────────────────────────────────────────────────┘

  MODALITY BALANCE = development level của các areas này:
    → Người visual dominant = V1-IT developed mạnh
    → Người somatic dominant = insula developed mạnh
    → = Brain-wide HARDWARE property
    → Ảnh hưởng: hướng chunk compile, chất lượng chunk
    → PFC KHÔNG quyết định modality balance — PFC dùng OUTPUT
```

---

## §4 — C: SUBCORTICAL STRUCTURES

```
🟢 DEEP BRAIN STRUCTURES — PFC reach HẠN CHẾ (gradient):

  ┌─────────────────────────────────────────────────────────────────┐
  │ AMYGDALA                                                         │
  │   Location: medial temporal lobe (bilateral)                     │
  │   Function: threat/reward tagging, fear conditioning, emotional  │
  │     salience evaluation                                         │
  │   Timeline: fire 12ms (subcortical visual pathway) — TRƯỚC PFC   │
  │   PFC reach: vmPFC → amygdala DIRECT (uncinate fasciculus)       │
  │     → PFC CÓ THỂ modulate amygdala SAU khi nó đã fire           │
  │     → PFC KHÔNG THỂ ngăn amygdala fire lần đầu                  │
  │     → Extinction learning: vmPFC gradually recalibrate amygdala  │
  │   Framework: threat detection, emotional peak compile, Precondition-5 tag │
  │   🟢 LeDoux 1996, Phelps et al. 2004, Ghashghaei et al. 2007    │
  ├─────────────────────────────────────────────────────────────────┤
  │ HIPPOCAMPUS                                                      │
  │   Location: medial temporal lobe                                 │
  │   Function: memory encoding, spatial navigation, consolidation   │
  │   Role: temporary storage → replay during sleep → cortical chunks│
  │   Alcohol → block hippocampal LTP → blackout (encoding failure)  │
  │     = Short-term memory INTACT, long-term transfer BLOCKED       │
  │   Framework: chunk compile gateway, sleep consolidation mechanism│
  │   🟢 Scoville & Milner 1957 (patient HM), White 2003 (blackout)  │
  │   🟢 Zorumski et al. 2014                                         │
  ├─────────────────────────────────────────────────────────────────┤
  │ THALAMUS                                                         │
  │   Location: central brain (diencephalon)                         │
  │   Function: GATEWAY — relay + filter sensory → cortex             │
  │   TRN (Thalamic Reticular Nucleus): PFC CAN gate via TRN         │
  │   Each sense has own nucleus (LGN visual, MGN auditory,...)       │
  │   Exception: olfaction BYPASSES thalamus entirely                 │
  │   Framework: attention gating mechanism                          │
  │   🟢 Sherman & Guillery 2006, McAlonan et al. 2008               │
  ├─────────────────────────────────────────────────────────────────┤
  │ HYPOTHALAMUS                                                      │
  │   Location: below thalamus                                       │
  │   Function: hormone regulation, homeostasis, circadian (SCN),     │
  │     hunger, thirst, temperature, HPA axis (CRH → ACTH → cortisol)│
  │   PFC reach: indirect via cortical → hypothalamic pathways        │
  │   Framework: cortisol baseline regulation, L1 body-input control  │
  │   🟢 Sapolsky 2004                                                 │
  ├─────────────────────────────────────────────────────────────────┤
  │ BASAL GANGLIA (Striatum: caudate + putamen + NAc)                │
  │   Location: deep in cerebral hemispheres                         │
  │   Function: habit formation, implicit learning, reward processing│
  │   Architecture: parallel cortico-BG-thalamo-cortical LOOPS        │
  │     → Associative loop: PFC ↔ caudate (flexible, goal-directed)  │
  │     → Sensorimotor loop: premotor ↔ putamen (habitual, automatic)│
  │     → Limbic loop: OFC/ACC ↔ NAc (reward/motivation)             │
  │   Habit = shift từ associative → sensorimotor loop               │
  │   Framework: chunk compilation pathway, habit = compiled chunks   │
  │   🟢 Yin & Knowlton 2006, 2025 Trends in Neurosciences           │
  ├─────────────────────────────────────────────────────────────────┤
  │ BRAINSTEM NUCLEI                                                  │
  │                                                                   │
  │   VTA (Ventral Tegmental Area):                                  │
  │     → Dopamine source → prediction-delta signals                  │
  │     → Fires on: positive prediction-delta (input > expected)                    │
  │     → Framework: delta rule, Body-Feedback-Precondition Precondition-3 Delta-Gate VTA threshold │
  │     → 🟢 Schultz 1997 (prediction error)                          │
  │                                                                   │
  │   LC (Locus Coeruleus):                                          │
  │     → Norepinephrine source → arousal, attention, alertness       │
  │     → HIGH NE → α1 receptors → PFC DISCONNECT (circuit breaker)  │
  │     → Framework: NE acute freeze (§9.1 Cortisol-Baseline)        │
  │     → 🟢 Arnsten 2009, 2015                                       │
  │                                                                   │
  │   Raphe Nuclei:                                                   │
  │     → Serotonin source → mood baseline, gut function              │
  │     → 95% serotonin produced IN GUT                               │
  │     → Framework: mood stability, status baseline                  │
  │                                                                   │
  │   PAG (Periaqueductal Gray):                                     │
  │     → Pain modulation, defensive behavior, fight/flight/freeze   │
  │     → PFC HAS direct connections to PAG                           │
  │     → Framework: pain gate, survival responses                   │
  │                                                                   │
  │   NTS (Nucleus of Solitary Tract):                               │
  │     → Visceral sensory relay: taste, cardiovascular, respiratory  │
  │     → Vagus nerve arrives here                                    │
  │     → PFC HAS direct connections to NTS                           │
  │     → Framework: body-input relay to brain                       │
  │                                                                   │
  │   🟢 PFC → brainstem: direct reciprocal connections to PAG + NTS  │
  └─────────────────────────────────────────────────────────────────┘

  DEFAULT MODE NETWORK (DMN) — cross-cuts A+B+C:
    Core areas: mPFC (A) + PCC/precuneus (B) + angular gyrus (B) + MTG (B)
    Active during: rest, self-referential thought, autobiographical memory,
      future planning, social cognition
    mPFC = DMN hub → sends info to PCC directionally
    Framework: self-assessment, imagination, identity schemas
    🟢 Raichle et al. 2001, Buckner et al. 2008
    🟢 2024 Nature Neuroscience: DMN architecture mapped through
      cytoarchitecture, wiring, and signal flow
```

---

## §5 — D: PERIPHERAL NEURAL SYSTEMS

```
🟢 NEURAL SYSTEMS NGOÀI NÃO — PFC GẦN KHÔNG REACH TRỰC TIẾP:

  ┌─────────────────────────────────────────────────────────────────┐
  │ ENTERIC NERVOUS SYSTEM (ENS — "Second Brain")                   │
  │   Location: wall of GI tract (esophagus → rectum)               │
  │   Neurons: ~100-500 million (more than spinal cord)              │
  │   Function: digestion, peristalsis, local immune, microbiome     │
  │     signaling, serotonin production (95% of body's serotonin)   │
  │   Gut-brain axis: vagus nerve (80% AFFERENT — gut → brain)       │
  │   PFC reach: KHÔNG trực tiếp. PFC → hypothalamus/brainstem →    │
  │     vagus → ENS (minimum 2 synaptic relays)                      │
  │   Framework: ăn đồ mới → gut calibrate RIÊNG → PFC không biết   │
  │   🟢 Gershon 1998, Mayer 2016, Cryan & Dinan                     │
  ├─────────────────────────────────────────────────────────────────┤
  │ SPINAL CORD                                                      │
  │   Function: motor reflexes (rút tay ~50ms, TRƯỚC PFC),           │
  │     pain pathways (A-delta fast + C-fiber slow),                  │
  │     motor neuron → muscle execution                              │
  │   PFC reach: indirect (PFC → premotor → M1 → spinal)             │
  │   Framework: L0 reflex circuit breaker, pain pathways             │
  ├─────────────────────────────────────────────────────────────────┤
  │ AUTONOMIC NERVOUS SYSTEM (ANS)                                   │
  │   Sympathetic: fight-or-flight (accelerate)                      │
  │   Parasympathetic: rest-and-digest (brake)                       │
  │   Vagus nerve: primary parasympathetic (gut, heart, lungs)       │
  │   PFC reach: KHÔNG direct control                                │
  │     → PFC stress → sympathetic activate (indirect via HPA)       │
  │     → PFC calm (via breathing — voluntary bridge) → parasympathetic│
  │     → Breathing = UNIQUE: voluntary + involuntary bridge          │
  │   Framework: body-feedback signals, homeostasis                  │
  │   🟢 Porges polyvagal theory, Thayer neurovisceral integration   │
  ├─────────────────────────────────────────────────────────────────┤
  │ CARDIAC NEURAL SYSTEM                                            │
  │   Location: intrinsic cardiac ganglia                            │
  │   Neurons: ~40,000 (small but functional network)                │
  │   Function: local heart rhythm regulation                        │
  │   PFC reach: KHÔNG direct                                        │
  │   Framework: cardiovascular interoception (L1 body-input)         │
  └─────────────────────────────────────────────────────────────────┘
```

---

## §6 — CONNECTIVITY MAP

```
🟡 AI CONNECT TỚI AI — GRADIENT, KHÔNG BINARY:

  PFC (A) → CORTICAL (B): STRONG, direct
    → Layer 2/3 connections (broadest connectivity)
    → Top-down bias: PFC hold → modality areas amplify/suppress
    → TRN gate: PFC → thalamus → control sensory input
    → = Framework: PFC bias spreading activation trong B

  PFC (A) → SUBCORTICAL (C): VARIABLE
    → vmPFC → Amygdala: DIRECT (uncinate fasciculus) 🟢
    → PFC → Striatum: DIRECT (cortico-BG loops) 🟢
    → PFC → Thalamus: DIRECT (via TRN) 🟢
    → PFC → PAG, NTS: DIRECT reciprocal 🟢
    → PFC → Hypothalamus: MODERATE (cortical pathways)
    → = Framework: PFC CÓ THỂ modulate C, nhưng C fire TRƯỚC PFC

  PFC (A) → PERIPHERAL (D): WEAK/INDIRECT
    → PFC → ENS: minimum 2 synaptic relays (PFC → brainstem → vagus → ENS)
    → PFC → Spinal: indirect (PFC → premotor → M1 → spinal)
    → PFC → ANS: indirect (via HPA, voluntary breathing = exception)
    → = Framework: PFC gần không influence D trực tiếp

  CORTICAL (B) → SUBCORTICAL (C): MODERATE
    → B → Thalamus: bidirectional (thalamocortical loop)
    → B → Amygdala: some direct (visual → amygdala subcortical)
    → B → Basal Ganglia: cortico-BG loops
    → B → Hippocampus: memory encoding
    → B → Cerebellum: corticopontocerebellar pathway

  SUBCORTICAL (C) → PERIPHERAL (D): DIRECT
    → Brainstem → Spinal cord: motor commands
    → Brainstem → ANS: sympathetic/parasympathetic
    → Brainstem → ENS: vagus nerve
    → Hypothalamus → Endocrine: hormone release

  BODY-INPUT → ALL LEVELS:
    → Sensors → Thalamus (C) → Cortex (B) → PFC (A) : standard path
    → Sensors → Amygdala (C) : shortcut (12ms, bypasses B+A)
    → Sensors → ENS (D) : local processing without brain
    → Sensors → Spinal cord (D) : reflex without brain
    → = Body-input reaches EVERYWHERE, PFC is LAST to know


  ⭐ KEY INSIGHT: TIMING HIERARCHY

    D: Spinal reflex         ~50ms (FASTEST — before brain)
    C: Amygdala threat       ~12ms from retina (subcortical shortcut)
    C: Brainstem response    ~100ms
    B: Cortical processing   ~150-200ms
    A: PFC awareness         ~200-500ms (SLOWEST — last to know)

    → PFC is ALWAYS the last to know
    → Body (D) + subcortical (C) + cortical (B) all process BEFORE PFC
    → PFC "decides" = often confirming what B+C already started
    → = Framework: body compute FIRST → feeling emerge → PFC observe LAST
```

---

## §7 — BILATERAL ARCHITECTURE: Left ↔ Right (v1.2)

```
🟢 NÃO = BILATERAL: MỌI VÙNG A/B/C/D ĐỀU CÓ TRÁI + PHẢI

  §1-§6 mô tả connectivity VERTICAL (PFC reach depth: A→B→C→D).
  Section này: connectivity HORIZONTAL (Left ↔ Right).
  2 chiều ORTHOGONAL — cả 2 đều cần cho bản đồ đầy đủ.


  MỌI ZONE ĐỀU CÓ 2:

    Zone A (PFC):  Left dlPFC + Right dlPFC, Left vmPFC + Right vmPFC, ...
    Zone B:        Left V1 + Right V1, Left Broca + Right homologue, ...
    Zone C:        Left amygdala + Right amygdala, Left hippocampus + Right, ...
    Zone D:        Peripheral = ĐỐI XỨNG (left/right body → left/right pathways)

  Ngoại lệ quan trọng — MIDLINE structures:
    → Brainstem nuclei (VTA, LC, Raphe, PAG) = MIDLINE → không chia trái phải rõ
    → Hypothalamus = phần lớn MIDLINE
    → Cerebellum = bilateral nhưng CROSS-CONNECTED (left cerebellum ↔ right cortex)
    → = Subcortical midline structures = cơ sở cho SHARED arousal + motivation
      (giải thích tại sao split-brain vẫn đồng bộ emotional tone)
```

```
🟢 CORPUS CALLOSUM = INTEGRATION LAYER:

  Cấu trúc: ~200 triệu axon nối vùng homologous trái ↔ phải
  = White matter tract LỚN NHẤT trong brain
  = Cho phép 2 bán cầu TÍCH HỢP processing output

  WHAT IT CONNECTS (anterior → posterior):
    Genu (anterior)     : PFC ↔ PFC (prefrontal connections)
    Body (central)      : Motor ↔ Motor, Somatosensory ↔ Somatosensory
    Splenium (posterior) : Visual ↔ Visual, Parietal ↔ Parietal
    → = MỌI zone A + B đều có cross-hemisphere connection qua corpus callosum

  WHAT IT DOES:
    → Tích hợp 2 processing styles thành 1 output giàu hơn
    → Left hemisphere: sequential, analytic, verbal encoding
    → Right hemisphere: simultaneous, holistic, spatial encoding
    → = 2 LENS nhìn cùng 1 vấn đề, KHÔNG PHẢI 2 worker làm 2 việc khác
    → Corpus callosum = layer cho phép 2 lens HỢP NHẤT
    → VD: Nhận diện bạn cũ: Right detect gestalt khuôn mặt (spatial) +
      Left gắn tên + context (verbal) → corpus callosum tích hợp →
      "À Minh, học cùng cấp 3!" = output giàu hơn 1 bên riêng lẻ

  Các commissure khác (nhỏ hơn):
    → Anterior commissure: nối temporal lobes (olfactory, some emotional)
    → Hippocampal commissure: nối 2 hippocampi
    → Posterior commissure: nối midbrain areas
    → Trong callosotomy: đôi khi giữ lại, đôi khi cắt kèm — tùy ca

  SPEED: transmission ~10-30ms → integration gần như đồng thời

  🟢 Witelson 1989 (corpus callosum anatomy)
  🟢 Human Connectome Project (tractography mapping)
  🟢 Aboitiz et al. 1992 (fiber composition + regional variation)
```

```
🟢 LATERALIZATION = FUNCTION-SPECIFIC, KHÔNG PHẢI "LOẠI NGƯỜI":

  Một số CHỨC NĂNG lateralized (1 bên dominant):

    Left dominant:                       Right dominant:
    ┌──────────────────────────┐         ┌──────────────────────────┐
    │ Language production       │         │ Spatial processing       │
    │ (Broca — 95% right-hand) │         │ Face recognition (FFA)   │
    │ Language comprehension    │         │ Prosody (ngữ điệu,      │
    │ (Wernicke)               │         │   sắc thái giọng nói)   │
    │ Sequential processing    │         │ Holistic/gestalt         │
    │ Fine motor (dominant     │         │   perception             │
    │   hand)                  │         │ Music perception         │
    │ Arithmetic calculation   │         │   (non-trained)          │
    │ Logical grammar parsing  │         │ Emotional expression     │
    │                          │         │   (face, voice)          │
    └──────────────────────────┘         └──────────────────────────┘

  ⚠️ "LEFT-BRAIN PERSON" vs "RIGHT-BRAIN PERSON" = POP SCIENCE SAI:
    → Nielsen et al. 2013 (n=1,011, fMRI resting state):
      KHÔNG tìm thấy người nào "ưu tiên" 1 bán cầu tổng thể
    → Lateralization = per-FUNCTION, KHÔNG phải per-PERSON
    → Cả 2 bán cầu THAM GIA hầu hết tasks, chỉ khác contribution
    → VD ngôn ngữ: Left parse grammar, Right detect irony + context + metaphor
    → Đọc câu đùa: LEFT parse cú pháp, RIGHT detect irony → CẢ HAI cần

  "DOMINANT" ≠ "EXCLUSIVE":
    → Left dominant cho language ≠ right không tham gia
    → Right dominant cho spatial ≠ left không tham gia
    → Mỗi bên CONTRIBUTE khác nhau cho cùng task
    → Corpus callosum tích hợp 2 contributions → output phong phú hơn

  🟢 Broca 1861 (language lateralization)
  🟢 Kimura 1961 (dichotic listening — auditory lateralization)
  🟢 Nielsen et al. 2013 PLOS ONE (no whole-brain dominance)
```

```
🟢 SPLIT-BRAIN: PHƠI BÀY BILATERAL ARCHITECTURE

  Callosotomy (cắt corpus callosum): phẫu thuật cho động kinh nặng
  Số bệnh nhân được nghiên cứu kỹ: <12 trên toàn cầu
  → CẮT integration layer → 2 bán cầu MẤT kết nối cortical
  → Subcortical (C) + peripheral (D) VẪN NỐI (nằm dưới đường cắt)

  KEY FINDINGS (Sperry 1981 Nobel, Gazzaniga 1978/2000/2005):

    ① 2 bán cầu xử lý RIÊNG BIỆT
       → Mỗi bên có data riêng, preferences riêng, response riêng
       → VD: right hemisphere muốn "automobile racer",
         left hemisphere muốn "draftsman" — cùng 1 bệnh nhân

    ② Left PFC "Interpreter" CONFABULATE narrative
       → Left hemisphere (có ngôn ngữ) luôn tạo causal story
       → Dù KHÔNG CÓ access tới lý do thật (ở right hemisphere)
       → KHÔNG BAO GIỜ nói "tôi không biết"
       → VD kinh điển: chân gà + cảnh tuyết → "cần xẻng dọn chuồng gà"

    ③ Bệnh nhân hàng ngày GẦN NHƯ BÌNH THƯỜNG — vì:
       a) Subcortical midline unity (shared arousal, motivation, emotional tone)
       b) Cross-cueing: đồng bộ GIÁN TIẾP qua body-input
          (right hemisphere cử động tay trái → left hemisphere THẤY qua mắt
          → đồng bộ bằng observation thay vì neural pathway)
       c) Pre-surgery compiled chunks = shared (compile trước khi cắt → cả 2 bên có)
       d) Interpreter maintain narrative "tôi là 1 người" liên tục

    ④ Alien Hand Syndrome (hiếm):
       → 2 tay làm ngược nhau (1 tay cài nút, 1 tay cởi nút)
       → = 2 processing systems LỘ RA khi integration bị cắt
       → Bệnh nhân KHÔNG nói "có 2 tôi" — nói "tay trái nó nghịch"
       → = Interpreter maintain unity narrative bằng mọi giá

  FRAMEWORK VALIDATION:
    → PFC = Lawyer: STRENGTHENED (Interpreter = literal demonstration)
    → Chunks no source tag: CONFIRMED (Left PFC không biết source từ right hemisphere)
    → Body first, PFC after: CONFIRMED (action trước, narrative sau)
    → Compiled ~95%: SUPPORTED (daily function preserved dù mất integration)

  🟢 Sperry 1981 (Nobel Prize — split-brain research)
  🟢 Gazzaniga 1978 (initial Interpreter observations)
  🟢 Gazzaniga 2000, 2005 (Interpreter theory refined)
```

```
🟡 FRAMEWORK PRINCIPLE: "THỐNG NHẤT" = EMERGENT, KHÔNG PHẢI STRUCTURAL

  Brain = NHIỀU HỆ THỐNG ĐỘC LẬP chạy song song:
    → Vùng khác nhau (visual, auditory, motor, amygdala, insula, ...)
    → Bán cầu khác nhau (left processing ≠ right processing)
    → Chunks cục bộ (local connections trong từng vùng)
    → Schemas cross-modal (multi-region, có thể conflict ở level tổng thể)

  "TÔI LÀ 1 NGƯỜI THỐNG NHẤT":
    → KHÔNG PHẢI structural fact (não KHÔNG phải 1 khối đồng nhất)
    → MÀ LÀ emergent state khi systems HÀI HÒA
    → Hài hòa: no dissonance signal → PFC idle → "tôi ổn"
    → Conflict: dissonance signal → PFC pulled in → narrative → action
    → = "Thống nhất" = TRẠNG THÁI, không phải CẤU TRÚC

  Split-brain CONFIRMS:
    → Cắt integration layer → 2 bán cầu lộ ra là independent
    → NHƯNG Interpreter VẪN maintain "tôi là 1" bằng confabulation
    → = "Unity" = narrative construct của Interpreter, không phải report of structural fact

  NORMAL BRAIN — CÙNG CƠ CHẾ, ÍT DRAMATIC HƠN:
    → Internal conflicts VẪN xảy ra ở não bình thường:
      Compiled body-base vs fresh PFC intent
      Multiple drives competing (Novelty vs Threat vs Boredom)
      Social schema vs body-need (muốn học giỏi vs không có gap)
    → "Muốn dậy sớm mà sáng muốn ngủ" = 2 subsystems conflict,
      Interpreter confabulate "tôi lười" (= "tay trái nó nghịch" version nhẹ)
    → = Split-brain alien hand = phiên bản CỰC ĐOAN
      của kiến trúc vốn đã parallel ở mọi người

  TẠI SAO FRAMEWORK HEMISPHERE-AGNOSTIC:
    → Framework operate ở level MECHANISM (chunk, compile, PFC observe, body-feedback)
    → Mechanisms ĐÚNG regardless of hemisphere:
      Hebbian compile ở left = Hebbian compile ở right = cùng mechanism
      PFC observe ở left = PFC observe ở right = cùng function
      Body-feedback fire ở left amygdala = fire ở right = cùng mechanism
    → Lateralization = TOPOLOGY detail, không thay đổi mechanism claims
    → = Framework mô tả ENGINE, section này mô tả ENGINE chạy trên bilateral HARDWARE
    → Khi cần topology detail → đọc section này + mainstream neuroscience literature

  🟡 "Unity = emergent from harmony" = framework synthesis
     Consistent with: Tononi 2004 IIT, Baars 1988 GWT
     Extended by: split-brain evidence + internal conflict observations
  🟢 Split-brain evidence = direct test (Gazzaniga, Sperry)
  🟢 Internal conflicts = universal human experience
```

---

## §8 — CHUNK COMPILATION ACROSS A/B/C/D

```
🟡 CHUNKS COMPILE Ở MỌI VÙNG — nhưng mechanism + PFC involvement KHÁC:

  CORTICAL CHUNKS (B areas) — PFC CAN TRAIN:
    → Visual chunks: V1→IT pattern recognition
    → Auditory chunks: A1 → speech patterns
    → Motor chunks: M1+cerebellum → skill compilation
    → Language chunks: Broca+Wernicke → grammar, vocabulary
    → PFC CÓ THỂ: hold + repeat + bias → accelerate compilation
    → VD: PFC hold "tập đàn" → motor cortex compile skill chunks

  SUBCORTICAL CHUNKS (C areas) — PFC INDIRECT:
    → Amygdala: fear conditioning (1 trial, emotional peak)
    → Hippocampus: episodic encoding → sleep replay → cortical
    → Basal ganglia: habit compilation (associative → sensorimotor)
    → PFC INDIRECT: PFC không force fire ở đây
      nhưng PFC thay đổi MÔI TRƯỜNG → body-input thay đổi → C recalibrate
    → VD: PFC chuyển tới môi trường an toàn → qua thời gian →
      amygdala recalibrate (vmPFC extinction pathway)

  PERIPHERAL CHUNKS (D areas) — PFC NEAR-ZERO:
    → ENS: gut calibrate khi ăn đồ mới → microbiome adjust
    → Spinal: reflex patterns (withdraw, posture)
    → ANS: autonomic calibration
    → PFC influence: gần zero trực tiếp
    → Body-input compile TRỰC TIẾP ở đây
    → VD: ăn đồ ăn lạ liên tục → gut neurons calibrate → PFC không biết

  PROPAGATION ACROSS LEVELS:
    → Cortical chunks (B) CÓ THỂ propagate → subcortical (C) qua thời gian
    → Repeated positive cortical processing → vmPFC → amygdala recalibrate
    → = Therapy mechanism: PFC create safe context (B) →
      repeated exposure → amygdala (C) gradually shift
    → Timeline: weeks to months (NOT instant)
    → = "PFC không chữa amygdala — PFC tạo CONTEXT cho amygdala tự recalibrate"
```

---

## §9 — IMPLICATIONS CHO FRAMEWORK

```
🟡 4 PHÂN VÙNG THAY THẾ "UNCONSCIOUS" BOX TRONG CORE:

  CŨ (Core v7.5, v7.8 draft):
    "PFC vs Unconscious" — 2 boxes, 1 box mờ

  MỚI:
    A (PFC) / B (Cortical Modality) / C (Subcortical) / D (Peripheral)
    — 4 vùng cụ thể, từng function rõ ràng

  FRAMEWORK MAPPING:

    "Chunk compile" → xảy ra ở B + C + D (PFC observe, không compile)
    "Body-feedback" → fire ở C (amygdala, brainstem) + B (insula, ACC)
    "Feeling" → integrate ở B (anterior insula) → PFC observe
    "PFC hold" → xảy ra ở A (dlPFC working memory)
    "PFC orchestrate" → A → B (top-down bias) + A → C (vmPFC-amygdala, TRN)
    "Cortisol amplifier" → xuyên suốt A+B+C+D (HPA axis = C, effects = everywhere)
    "Delta rule" → VTA (C) fire → signal tới B+A
    "Motor execute" → A hold → B (motor cortex) → D (spinal) → muscle
    "Self-signal interoception" → B (anterior insula) đọc D (body) qua C (brainstem/vagus)

  HARDWARE PROFILE:
    → Modality Balance = B area development (brain-wide, không thuộc A hay C)
    → PFC params = A properties (WM capacity, COMT, DRD4)
    → Receptor variants = D properties (OXTR, TAS2R, CT-fiber density)
    → Hardware set RANGE → chunks (compiled across B+C+D) chọn VỊ TRÍ trong range
```

---

## §10 — HONEST ASSESSMENT

```
🟢 ESTABLISHED (high confidence):
  → PFC sub-regions and functions (decades of lesion + fMRI research)
  → Cortical 6-layer architecture (Mountcastle 1957)
  → vmPFC-amygdala direct connection (Ghashghaei 2007)
  → Language ≠ reasoning (Fedorenko 2024)
  → Hippocampal encoding failure = blackout (White 2003, Zorumski 2014)
  → Cerebellum cognitive + emotional (Schmahmann 1998, 2024 meta-analysis)
  → NE α1 PFC disconnect (Arnsten 2009)
  → PFC → ENS: minimum 2 relays, no direct connection
  → Craig anterior insula interoception (2002, 2009)
  → Human Connectome Project connectivity data (NIH, 1,200 participants)
  → Bilateral brain organization (anatomy — established since 19th century) (v1.2)
  → Corpus callosum structure + function (Witelson 1989, Aboitiz 1992, HCP) (v1.2)
  → Function-specific lateralization, NOT person-specific (Broca 1861+, extensive) (v1.2)
  → No "whole-brain dominance" per person (Nielsen et al. 2013, n=1,011) (v1.2)
  → Split-brain findings (Sperry Nobel 1981, Gazzaniga 1978/2000/2005) (v1.2)
  → Cross-cueing in split-brain patients (documented extensively) (v1.2)
  → Subcortical midline structures unaffected by callosotomy (v1.2)

🟡 FRAMEWORK SYNTHESIS (medium confidence):
  → 4-zone classification (A/B/C/D) = novel organizing framework
  → "PFC accessibility gradient" = novel framing, components established
  → Chunk compilation across zones = novel integration, mechanisms established
  → "PFC tạo context cho C recalibrate" = novel framing, consistent with
    extinction learning literature
  → Modality Balance as hardware property = novel positioning
  → DMN cross-cutting A+B = established areas, novel integration
  → "Unity = emergent from harmony, not structural" = novel framing, (v1.2)
    consistent with split-brain evidence + IIT/GWT consciousness theories
  → Framework hemisphere-agnostic = deliberate abstraction choice (v1.2)
    (mechanisms correct regardless of hemisphere)
  → Normal internal conflicts ≈ split-brain alien hand (same mechanism, (v1.2)
    different intensity) = novel framing, logically consistent

🔴 NEEDS MORE RESEARCH:
  → Exact PFC influence on cerebellum cognitive functions
  → Whether ENS "chunks" are mechanistically same as cortical chunks
  → Precise boundary ACC: PFC or limbic? (ongoing debate)
  → How much PFC can influence hypothalamic regulation
  → Individual variation in PFC-subcortical connectivity strength
  → Whether "chunk" concept applies uniformly across A/B/C/D
    or needs refinement per zone
  → Whether each hemisphere develops meaningfully different chunk libraries (v1.2)
    in intact brains (beyond lateralized function differences)
  → How hemisphere-specific processing styles interact with COMT/DRD4 (v1.2)
    hardware profiles (PFC-Hardware.md)
```

---

## §11 — CROSS-REFERENCES

```
WITHIN FRAMEWORK:
  Neural-Processing-Flow.md — signal pathway detail (sensor → cortex → PFC)
  Modality-Analysis.md — modality encoding analysis
  Chunk.md v2.3 — chunk mechanism on this substrate
  Feeling.md v2.0 — feeling = PFC observation (maps to A reading B+C)
  Body-Feedback.md — body signals (maps to C+B generating, A observing)
  Cortisol-Baseline.md v2.0 — cortisol mechanism across A+B+C+D
  Core-v7.8-Draft.md — kiến trúc tổng thể uses this as physical map
  Agent-Mechanism.md v2.1 — agent function (maps to A+B social areas)
  Empathy.md v4.0 — Self-Pattern-Modeling function (maps to A+B, reading C signals)

BILATERAL ARCHITECTURE (v1.2):
  PFC-Function.md v1.2 §6 — Confabulation + Gazzaniga evidence → §7 extends
  Feeling.md v3.0 §3.4 — PFC = Lawyer structural bias → §7 split-brain proof
  Logic-Feeling.md v4.0 §2.3 — PFC = Lawyer applies to both labels → §7 mechanism
  Drive.md — drive conflict subsystem-based; §7 adds hemisphere conflict (split-brain only)
  Simulation-Engine.md v1.0 — "1 engine" = midline substrate → §7 clarifies bilateral hardware
  Compile-Taxonomy.md v3.0 — "1 engine = Hebbian" = mechanism-level → §7: hemisphere-agnostic

NEW CONCEPT MAPPING (28-session Drill):
  Simulation-Engine.md v1.0 — Zone A: PFC simulation = interoception × simulation × Self-Pattern-Modeling
    → PFC (dlPFC, vmPFC) + hippocampus + default mode network
    → = Simulation-Engine neural substrate identified
  Entity-Access.md v1.2 — Zone A+C: entity-access gradient maps to:
    → Amygdala (C): per-entity valence tagging
    → Hippocampus (C): per-entity memory consolidation
    → PFC (A): per-entity access assessment
    → = Entity-Access = distributed A+C network per-entity
  Entity-Compiled.md v1.0 — Zone A+B+C: hub-and-spoke per-entity:
    → Amygdala hub + hippocampal spokes + PFC executive access
    → Dunbar ~150 = capacity constraint of this network

KEY RESEARCH (by area):
  PFC: Fuster 1973, Goldman-Rakic 1995, Damasio 1994, Arnsten 2009
  Language: Fedorenko et al. 2024 (Nature Reviews Neuroscience)
  Visual: Hubel & Wiesel 1959, Kanwisher 1997
  Amygdala: LeDoux 1996, Phelps 2004, Ghashghaei 2007
  Hippocampus: Scoville & Milner 1957, White 2003
  Cerebellum: Schmahmann 1998, 2024 meta-analysis
  Insula: Craig 2002, 2009
  Basal Ganglia: Yin & Knowlton 2006
  DMN: Raichle 2001, Buckner 2008
  Connectivity: Human Connectome Project (NIH)
  ENS: Gershon 1998, Mayer 2016
  ANS: Porges polyvagal, Thayer neurovisceral
  Cortex: Mountcastle 1957
  Thalamus: Sherman & Guillery 2006
  Bilateral/Split-brain: Sperry 1981 (Nobel), Gazzaniga 1978/2000/2005 (v1.2)
  Corpus callosum: Witelson 1989, Aboitiz et al. 1992 (v1.2)
  Lateralization: Broca 1861, Kimura 1961, Nielsen et al. 2013 PLOS ONE (v1.2)
```

---

> **Neural-Architecture.md v1.2**
>
> Physical map: A (PFC) / B (Cortical Modality) / C (Subcortical) / D (Peripheral).
> PFC accessibility = gradient, không binary.
> Chunks compile across ALL zones — PFC involvement varies.
> PFC = last to know (timing hierarchy: D→C→B→A).
> Simulation-Engine = Zone A (PFC + hippocampus + DMN).
> Entity-Access/Entity-Compiled = Zone A+C distributed network.
> **Bilateral Architecture: Left ↔ Right = horizontal dimension, orthogonal to A→D vertical.**
> **Corpus callosum = integration layer. "Unity" = emergent from harmony, NOT structural.**
> "Unconscious" replaced by specific, verifiable, challengeable claims.
>
> Phiên bản: v1.2, 2026-06-04.
> v1.2: +§7 Bilateral Architecture (corpus callosum, lateralization, split-brain, unity=emergent).
> v1.1: +Simulation-Engine mapping, +Entity-Access/Entity-Compiled mapping.
