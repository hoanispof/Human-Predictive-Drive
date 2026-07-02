---
title: Neural-Processing-Flow — Toàn bộ flow từ Sensor → Cortex → PFC → Output
version: 2.0
created: 2026-04-17 (N+5 session)
updated: 2026-05-17 (v2.0 — +Compilable Architecture framing, +Compiled/Fresh at physical level, +PFC=Lawyer strengthen, +5-Channel mapping, +L3 operator fix, +Inter-Body cross-refs)
previous: v1.0 → backup/Neural-Processing-Flow-v1.0-backup.md
status: v2.0
scope: HARDWARE FLOW + PROCESSING FLOW + Compilable Architecture connection
purpose: |
  Nền tảng gốc — con đường vật lý tín hiệu đi qua trong não.
  v2.0: WHY this hardware (Compilable Architecture trade-off), Compiled/Fresh at physical level,
  PFC=Lawyer as structural function, 5-Channel Input Vector connection.
position: Core-Deep-Dive/ (mechanism file)
dependencies:
  - Inter-Body-Mechanism.md v1.0 — Compilable Architecture, 5-Channel, PFC=Lawyer
  - Feeling.md v3.0 — 7-layer, Compiled/Fresh×Layer mapping
  - Logic-Feeling.md v2.0 — Compiled/Fresh axis
  - Body-Feedback-Mechanism.md v2.0 — 2-source, Body-Need
  - Body-Input-Enumeration.md — full body input catalog
language: Tiếng Việt primary + English technical
confidence: 🟢 Research support | 🟡 Framework synthesis | 🔴 Hypothesis
---

# Neural-Processing-Flow — Toàn bộ flow từ Sensor → Cortex → PFC → Output

> **File này trả lời:** Khi mắt thấy, tai nghe, da chạm, tim đập — tín hiệu đi CON ĐƯỜNG NÀO trong não?
>
> **Tại sao quan trọng:** Mọi cơ chế khác (chunk, feeling, logic, imagination, plan) đều CHẠY TRÊN con đường vật lý này.

---

## §0 — Vị trí trong framework

```
  ┌─────────────────────────────────────────────────────┐
  │ HARDWARE LAYER (file này)                           │
  │ = CON ĐƯỜNG VẬT LÝ: Sensors → Thalamus → Cortex   │
  │   → Binding → Chunks → PFC → Output → Feedback     │
  ├─────────────────────────────────────────────────────┤
  │ CONTENT LAYER (Schema/Chunk.md + Modality)          │
  │ = PATTERNS compile trên hardware                     │
  ├─────────────────────────────────────────────────────┤
  │ PROCESSING LAYER (Logic-Feeling.md v2.0)            │
  │ = Compiled/Fresh spectrum (not "2 modes")           │
  ├─────────────────────────────────────────────────────┤
  │ BEHAVIOR LAYER (Imagine-Final + Logic-Planning)     │
  │ = PLAN + EXECUTE + FEEDBACK                         │
  └─────────────────────────────────────────────────────┘

  ⭐ COMPILABLE ARCHITECTURE CONNECTION (Inter-Body-Mechanism.md §1):

  TẠI SAO hardware này tồn tại:
    Evolution chọn Compilable Architecture cho con người:
      ① General-Purpose Reward — fire cho BẤT KỲ gap fill đúng direction
      ② Compilation — repeat + verify → automatic (Hebbian LTP)
      ③ Social Hardware — oxytocin, μ-opioid, dACC reuse

    Trade-off of Compilable Architecture:
      → Adapt BẤT KỲ environment (general-purpose)
      → NHƯNG: cần 15-20 năm compile (slow development)
      → Hardware below = ENABLES Compilable Architecture:
        Thalamus gate = general-purpose filter (not hardwired per stimulus)
        6-layer cortex = uniform fabric (compile ANY pattern)
        PFC = general-purpose orchestrator (not stimulus-specific)
        Binding = flexible (bind ANY combination)
      → Hardwired Architecture (insect): hardwired stimulus→response (no PFC needed)
      → Compilable Architecture (human): general input → general processing → COMPILE

    Implication for this file:
      → §1-§4: HOW signals travel = hardware infrastructure
      → §5: HOW compilation happens = Compilable Architecture's KEY mechanism
      → §6: WHY PFC = orchestrator not computer = general-purpose design
      → §7-§9: WHY simulation + feeling + externalization = CONSEQUENCES
        of general-purpose hardware (not hardwired outputs)

  🟡 Compilable Architecture framing = framework synthesis (Inter-Body drill 2026-05-16)
```

---

## §1 — Body Sensors: Input sources

> **Full enumeration: Body-Input-Enumeration.md**

### §1.1 — Exteroceptive (sensing thế giới bên ngoài)

```
VISION (mắt):
  Receptor: rods (~120M, sáng/tối) + cones (~6M, màu) trên retina
  → Retina xử lý sơ bộ → optic nerve → thalamus (LGN) → V1
  Pathway đặc biệt:
    Circadian: ipRGC → SCN hypothalamus (BYPASS visual cortex — Berson 2002)
    Threat:    retina → LGN → amygdala (~12ms, BYPASS V1 — LeDoux 1996)

AUDITION (tai):
  Receptor: hair cells (~16,000) trong cochlea
  → Cochlear nerve → thalamus (MGN) → A1 (auditory cortex)
  Tonotopic mapping: tần số → vị trí trên cortex

OLFACTION (mũi):
  Receptor: ~10M olfactory neurons, ~400 loại receptor
  → Olfactory bulb → olfactory cortex → limbic
  ⭐ NGOẠI LỆ: BYPASS THALAMUS hoàn toàn (sense CỔ NHẤT, >500M năm)
  → mùi → emotional memory MẠNH + NHANH nhất  🟢 Gottfried 2010

GUSTATION (lưỡi):
  Receptor: ~10,000 taste buds (ngọt/mặn/chua/đắng/umami)
  → Cranial nerves → thalamus (VPM) → gustatory cortex (insula)

TACTILE (da):
  Receptor: Meissner (nhẹ), Pacinian (rung), Merkel (áp lực), Ruffini (kéo giãn)
  + Thermoreceptors + Nociceptors (A-delta nhanh + C-fiber chậm)
  + ⭐ C-tactile fibers (pleasant touch → insula TRỰC TIẾP, pathway riêng — Olausson 2002)
  → Spinal cord → thalamus (VPL) → somatosensory cortex (S1/S2)
```

### §1.2 — Proprioceptive (sensing vị trí cơ thể)

```
PROPRIOCEPTION: muscle spindles + joint receptors + Golgi tendon → thalamus → S1 + cerebellum
VESTIBULAR: semicircular canals + otoliths → vestibular nuclei → cerebellum + cortex
KINESTHETIC: muscle activity + efference copy (motor → cerebellum)
```

### §1.3 — Interoceptive (sensing trạng thái bên trong)

```
Cardiovascular: baroreceptors → vagus → brainstem → insula
Respiratory: chemoreceptors (CO₂) + stretch receptors → brainstem
Visceral: enteric nervous system → vagus → insula
Metabolic: glucose/ghrelin/leptin → hypothalamus
Hormonal: cortisol/oxytocin/dopamine/serotonin → body STATE changes
Nociception internal: A-delta + C-fibers → ACC + insula
Thermal core: hypothalamic thermosensors

⭐ HUB: Hầu hết interoceptive → ANTERIOR INSULA
  Craig 2009: anterior insula = "seat of subjective awareness" 🟢

⭐ SELF-SIGNAL INTEROCEPTION (meta-capacity):
  = Khả năng đọc chính internal state → Anterior insula + ACC + vmPFC
  = Predictive: não DỰ ĐOÁN body state, match actual → prediction-delta
  🟢 Seth 2013, Barrett 2017
```

### §1.4 — Summary

```
~20+ sensor types, 3 categories:
  Exteroceptive:  5 loại (mắt, tai, mũi, lưỡi, da)
  Proprioceptive: 3 loại (vị trí, thăng bằng, chuyển động)
  Interoceptive:  7+ loại (tim, phổi, ruột, chuyển hóa, hormone, đau, nhiệt)

Tất cả output = action potentials (xung điện). Khác ở: tần số + pattern + pathway.
```

---

## §2 — Thalamus: Gateway + Gatekeeper

### §2.1 — Thalamus là gì

```
⭐ THALAMUS = TRẠM TRUNG CHUYỂN TRUNG TÂM

  Vị trí: trung tâm não. Kích thước: ~2 hạt óc chó.
  
  RELAY:  chuyển tiếp signals từ sensors → cortex
  FILTER: lọc signals (không phải mọi input đều lên cortex)
  GATE:   mở/đóng channels theo attention (PFC ra lệnh)
  
  🟢 Sherman & Guillery 2006 — thalamus as active relay
```

### §2.2 — Mỗi sense có nucleus riêng

```
  Input          → Thalamic Nucleus     → Cortical Destination
  ─────────────────────────────────────────────────────────────
  Vision         → LGN                  → V1 (Visual cortex)
  Audition       → MGN                  → A1 (Auditory cortex)
  Touch/Pain     → VPL                  → S1 (Somatosensory)
  Taste          → VPM                  → Gustatory (insula)
  Proprioception → VPL                  → S1 + Cerebellum
  Interoception  → VMb + VMpo           → Anterior Insula

  ⭐ NGOẠI LỆ (non-standard thalamic routing):

  ① Olfaction — BYPASS THALAMUS (đường chính):
     Receptor → olfactory bulb → piriform cortex + amygdala + entorhinal TRỰC TIẾP
     Đường phụ: piriform → MD thalamus → OFC (cho nhận diện có ý thức)
     = Giác quan duy nhất có đường thẳng tới limbic (cổ nhất, >500M năm)

  ② Amygdala low road — BYPASS CORTEX, KHÔNG PHẢI thalamus:
     Retina → LGN (thalamus) → amygdala (~12ms, trước V1)
     ⚠️ LGN LÀ nhân của thalamus — tín hiệu vẫn ĐI QUA thalamus
     Bypass = CORTEX: không có thalamo-cortical loop → phản ứng vô thức
     = "Giật mình TRƯỚC KHI biết tại sao" — loop chưa hoàn thành
     🟢 LeDoux 1996

  ③ Circadian — BYPASS THALAMUS + CORTEX hoàn toàn:
     ipRGC → SCN hypothalamus (không hình ảnh, không bao giờ ý thức)
```

### §2.3 — Thalamo-cortical loop: 2 chiều

```
  BOTTOM-UP: Thalamus → Layer 4 cortex (raw data vào)
  TOP-DOWN:  Cortex Layer 6 → thalamus (feedback: filter/amplify/suppress)
  PFC CONTROL: PFC → TRN (Thalamic Reticular Nucleus) → gate toàn bộ thalamus

  ⭐ BẤT ĐỐI XỨNG: kết nối cortex → thalamus ≈ 10× kết nối thalamus → cortex
     → Thalamus KHÔNG phải relay thụ động — cortex chủ động điều chỉnh thalamus
     → Sustained thalamo-cortical loop = ý thức (Consciousness.md §5.1)
     → 🟢 Sherman & Guillery 2006
  
  ⭐ METAPHOR: Thalamus = tổng đài, TRN = operator, PFC = giám đốc chỉ đạo operator
  
  🟢 McAlonan et al. 2008 — TRN attentional gating
  🟢 Crick 1984 — searchlight hypothesis
```

---

## §3 — Cortical Areas: 6-Layer Architecture

### §3.1 — Cortical column: Kiến trúc cơ bản giống nhau

```
⭐ MOUNTCASTLE 1957: Toàn bộ neocortex = CẤU TRÚC 6 LỚP giống nhau:

  Layer 1  MOLECULAR:          highway kết nối ngang giữa columns
  Layer 2/3 EXTERNAL PYRAMIDAL: nhận/gửi từ CORTEX KHÁC (cross-modal đi qua đây)
  Layer 4  INTERNAL GRANULAR:   nhận input từ THALAMUS (raw data port)
  Layer 5  INTERNAL PYRAMIDAL:  gửi output ra NGOÀI cortex (motor, subcortical)
  Layer 6  MULTIFORM:           gửi feedback VỀ THALAMUS (loop control)

  = "Neocortex is a uniform computational fabric" (Mountcastle)
  = Khác nhau ở WIRING + THICKNESS + RECEPTOR RATIO, không ở basic architecture
  
  🟢 Mountcastle 1957, 1978
  🟢 Douglas & Martin 2004 — canonical microcircuit
```

### §3.2 — Chuyên môn hóa: cùng kiến trúc, khác configuration

```
  ① LAYER THICKNESS:
     V1:  Layer 4 CỰC DÀY (nhiều raw visual input)
     M1:  Layer 4 MỎNG, Layer 5 DÀY (ít nhận, nhiều gửi output)
     PFC: Layer 2/3 DÀY (nhiều cortex↔cortex connections)

  ② RECEPTOR DENSITY:
     PFC: nhiều dopamine D1/D2 → sensitive VTA signals
     V1:  ít dopamine, nhiều glutamate → high throughput

  ③ INHIBITORY RATIO:
     PFC: ~30% inhibitory → STRONG gate/brake
     Sensory: ~20% inhibitory → more throughput

  ④ CONNECTIVITY:
     V1: → V2, V4, MT (visual hierarchy)
     A1: → Wernicke (speech)
     PFC: → EVERYWHERE (broadest connectivity)
```

### §3.3 — Many-to-many mapping

```
⭐ KHÔNG PHẢI 1:1. Mapping là MANY-TO-MANY:

  1 SENSOR → NHIỀU cortical areas:
  ┌──────┐    ┌─ V1 Visual cortex (hình ảnh conscious)
  │ MẮT  ├────├─ Amygdala (~12ms, threat, TRƯỚC V1!)
  │      │    ├─ SCN hypothalamus (circadian, không hình ảnh)
  └──────┘    └─ Superior Colliculus (eye orienting)

  ┌──────┐    ┌─ A1 Auditory cortex
  │ TAI  ├────├─ Amygdala (emotional sounds)
  │      │    ├─ Wernicke (speech sounds)
  └──────┘    └─ Motor cortex (rhythm→movement)

  ┌──────┐    ┌─ S1/S2 Somatosensory (where, what)
  │ DA   ├────├─ Insula (C-tactile: pleasant/unpleasant)
  │      │    ├─ ACC (pain: suffering dimension)
  └──────┘    └─ Motor (reflexive withdrawal)

  1 CORTICAL AREA ← NHIỀU sensors:
  AMYGDALA ← mắt + tai + da + mũi + nội tạng + hormone + mirror

  ⭐ IMPLICATION: "Modality" = PROCESSING AREA, không phải "input source"
  → Visual modality = Visual cortex PROCESSING (nhận chủ yếu từ mắt
    + top-down từ PFC + cross-modal từ auditory)
```

### §3.4 — Visual hierarchy: Ví dụ 1 pathway chi tiết

```
  Retina → LGN → V1 → V2 → V4 → IT
                         ↓
                         MT → MST

  V1: edges, orientations     → "đường thẳng 45°"
  V2: contours, borders       → "viền hình tròn"  
  V4: shapes, colors          → "hình tròn, đỏ"
  IT: objects, faces           → "quả táo" / "khuôn mặt mẹ" (CHUNKS!)
  MT: motion                  → "vật đi sang trái"

  ⭐ PFC đọc IT (compiled patterns), KHÔNG đọc V1 (raw pixels)
  = PFC observe KẾT QUẢ compiled, không raw data
  
  🟢 Felleman & Van Essen 1991
  🟢 Kanwisher 1997 — FFA (fusiform face area)
```

---

## §4 — Binding: Cách não sync multi-modal input

> **F1 verdict: 07 §6 Emergent-Binding — 4 concurrent mechanisms**

### §4.1 — Gamma oscillation ~40Hz — Temporal synchrony

```
🟢 SINGER & GRAY 1995:

  Neurons ở KHÁC cortical areas fire CÙNG PHASE trong gamma band (~30-80Hz):
  → "fire cùng phase = thuộc cùng object"

  Quả táo: V1(đỏ) + V4(tròn) + MT(đứng yên) fire ~40Hz phase A = CÙNG object
  Cái ly:  V1(xanh) + V4(trụ) fire ~40Hz phase B = KHÁC object

  Cross-modal: Visual(táo) + Olfactory(mùi táo) + Somatic(cứng mát) cùng phase A
  → Bind thành 1 multi-modal chunk

  🟢 Singer 1999, Engel & Singer 2001, Fries 2005
  🟡 Debate: mechanism chính hay correlate? (evidence mạnh, 25+ năm)
```

### §4.2 — Multisensory neurons — Hardware-level binding

```
🟢 STEIN & MEREDITH 1993:

  Neurons NHẬN INPUT TỪ NHIỀU MODALITIES:
  → 1 neuron fire khi CẢ thấy VÀ nghe cùng object
  → Nằm ở: Superior Colliculus, STS, Intraparietal Sulcus

  SUPERADDITIVITY: Visual(10) + Auditory(8) → cùng lúc = 30 spikes (≠ 18!)
  TEMPORAL WINDOW: ~100-200ms để binding xảy ra
  DEVELOPMENTAL: present FROM BIRTH (hardware)
  
  🟢 Ghazanfar & Schroeder 2006
```

### §4.3 — Convergence zones — Hub areas tích hợp

```
🟢 DAMASIO 1989:

  PARIETAL:      ← visual + auditory + somatosensory + proprioceptive
                 → SPATIAL MAP: "cái gì ở đâu"  🟢 Andersen 1997

  STS:           ← face + voice + body language
                 → PERSON PERCEPTION: "ai đang làm gì"  🟢 Hein & Knight 2008

  ANTERIOR INSULA: ← interoception + nociception + affective touch + emotional
                   → BODY STATE: "body đang thế nào"
                   → Nơi FEELING EMERGE (§8)  🟢 Craig 2009

  vmPFC:         ← insula (body state) + amygdala (valence) + memory
                 → VALUE BRIDGE: somatic marker → conscious evaluation
                 → vmPFC weak = Phineas Gage  🟢 Damasio 1994
```

### §4.4 — Amygdala affective tagging

```
🟢 AMYGDALA = "EMOTIONAL HIGHLIGHTER":

  Emotional event → amygdala fire → NE release broad
  → TẤT CẢ neurons đang fire cùng lúc → synapses STRENGTHEN (Hebbian LTP enhanced)
  → = "Emotional event → bind MẠNH + compile NHANH"

  = Flashbulb memory mechanism (Brown & Kulik 1977)
  = Direction-At-Compile: cùng cơ chế, khác direction (novelty vs threat)
  
  🟢 McGaugh 2004, LeDoux 1996
```

### §4.5 — DMN scaffolding

```
🟢 DMN = network active khi KHÔNG làm task:
  mPFC + PCC + Angular gyrus + Hippocampus + Lateral temporal

  DMN cung cấp LONG-RANGE CONNECTIVITY:
  → Không có DMN → binding chỉ LOCAL
  → Có DMN → binding DISTANT (visual + insula + amygdala sync)
  → DMN present adult-like form ngay khi sinh (Doria et al. 2010)
```

### §4.6 — Binding summary

```
  ┌───────────────────────────────────────────────────────┐
  │ #  │ Mechanism            │ Level      │ Speed       │
  ├───────────────────────────────────────────────────────┤
  │ 1  │ Gamma sync ~40Hz     │ Oscillation│ ~25ms       │
  │ 2  │ Multisensory neurons │ Hardware   │ Instant     │
  │ 3  │ Convergence zones    │ Hub areas  │ ~50-100ms   │
  │ 4  │ Amygdala tagging     │ Emotional  │ ~12-50ms    │
  │ 5  │ DMN scaffolding      │ Network    │ Continuous  │
  └───────────────────────────────────────────────────────┘
  → KHÔNG CÓ single binder. 5 mechanisms chạy ĐỒNG THỜI.
  → Binding = EMERGENT PROPERTY.
```

---

## §5 — Chunk Compilation

> **Full analysis: Schema/Chunk.md**

### §5.1 — Chunk = compiled pattern

```
  TRƯỚC compile: neurons fire RIÊNG LẺ → PFC hold 5 slots
  SAU compile:   neurons fire AS ONE → PFC hold 1 slot → COMPRESSION

  Chunk = physical change: synapses strengthen (LTP) + myelin thicken
```

### §5.2 — 4 Compile mechanisms

```
  ① REPETITION:        lặp nhiều lần → chậm, bền
  ② EMOTIONAL PEAK:    amygdala + NE → 1 lần, mạnh (flashbulb)
  ③ MULTI-MODAL:       nhiều modalities cùng lúc → deep
  ④ SLEEP CONSOLIDATION: hippocampus replay → cortex transfer
  🟢 Diekelmann & Born 2010
```

### §5.3 — Multi-modal chunks span nhiều areas

```
  1 modality  = surface ("nước sôi 100°C" verbal only — dễ quên)
  2 modalities = medium ("đèn đỏ = dừng" — verbal + visual)
  4 modalities = deep ("sợ chó" — visual + auditory + somatic + emotional)
  5+ modalities = near-permanent ("tôi vô giá trị" — all — years therapy)
  → Chunk depth = modality count (Modality-Analysis §4)
```

### §5.4 — Expert = Meta-chunks

```
  Beginner: chunk A, B, C → PFC chain 3 steps (3 WM slots)
  Expert: meta-chunk [ABC] → PFC hold 1 slot → freed 2 slots for more
  → Expertise = compile chains → meta-chunks → PFC operates higher level
  → "Expert không thông minh hơn — expert có nhiều compiled chunks hơn"
  🟢 Chase & Simon 1973
```

### §5.5 — Compiled/Fresh at Physical Level (v2.0)

```
⭐ WHY COMPILED = FAST, FRESH = SLOW — at HARDWARE level:

  COMPILED PATH (Hebbian-strengthened):
    → Synapses: LTP-strengthened (🟢 Hebb 1949, Bliss & Lømo 1973)
    → Axons: MYELINATED (saltatory conduction: 100m/s vs 1m/s unmyelinated)
    → Pathway: DIRECT cortex→subcortex (bypass PFC bottleneck)
    → Neurotransmitter: vesicles PRE-DOCKED (faster release)
    → = Signal travels ESTABLISHED superhighway: fast, reliable, low energy

  FRESH PATH (novel, not yet compiled):
    → Synapses: weak, untested connections
    → Axons: unmyelinated or partially myelinated (SLOW conduction)
    → Pathway: must route THROUGH PFC (bottleneck: ~3-5 WM slots)
    → Neurotransmitter: needs dopamine BOOST for novel path activation
    → = Signal travels unmapped terrain: slow, unreliable, HIGH energy

  PHYSICAL CONSEQUENCES:
    Compiled: ~50-100ms response (subcortical direct)
    Fresh: ~300-500ms+ response (PFC chain required)
    = WHY expert "feels" answer (compiled → body-direct → fast)
    = WHY beginner "thinks" answer (fresh → PFC route → slow)
    = SAME CONTENT, different physical path quality

  COMPILATION PHYSICALLY CHANGES BRAIN:
    ① Synapse strength: LTP → larger post-synaptic density
    ② Myelin: oligodendrocytes wrap axon → speed increase 50-100x
    ③ Dendritic spine growth: more connection points per neuron
    ④ Pruning: competing weak paths WEAKENED (competitive)
    → = Compilation = PHYSICAL INFRASTRUCTURE built over time
    → = Compiled (Body-Knowing) = signal on SUPERHIGHWAY
    → = Fresh (PFC draft) = signal on DIRT ROAD being built

  CONNECTION VỚI FRAMEWORK:
    → Logic-Feeling.md v2.0 §1: Compiled/Fresh = trục thật
    → Feeling.md v3.0 §2.5: 7-layer × Compiled/Fresh
    → Inter-Body §3: content ≠ processing level (Einstein toán = compiled = fast)
    → 3-cost model: fresh = processing-intensive because novel path construction

🟢 Hebb 1949 (Hebbian learning principle)
🟢 Bliss & Lømo 1973 (LTP discovery)
🟢 Fields 2008 (activity-dependent myelination)
🟡 "Compiled = superhighway, Fresh = dirt road" metaphor = framework synthesis
```

---

## §6 — PFC: Observer + Director + Simulator

> **Full analysis: PFC-Analysis.md**

### §6.1 — PFC 5 functions

```
  ① DRAFT:     tạo temporary pattern (mixed-selectivity neurons, Rigotti 2013)
  ② TEST:      gửi xuống specialist regions evaluate (amygdala/insula/temporal/BG)
  ③ ROUTE:     pass hoặc discard based on feedback
  ④ BRAKE:     veto behavioral output (~200-500ms, sau subcortical ~50ms)
  ⑤ TRANSLATE: verbalize post-hoc (rationalization — Gazzaniga)

  ⭐ PFC = LAWYER, not Judge (Inter-Body §7, v2.0 ELEVATED):
    Function ⑤ = NOT neutral reporting. = LAWYERING for body-base.
    → Body-need fires TRƯỚC → drive forms → PFC tạo NARRATIVE "lý do"
    → Person BELIEVES narrative = "rational decision"
    → 🟢 Gazzaniga split-brain: left hemisphere CONFABULATES post-hoc
    → 🟢 Haidt 2001: moral intuition first, reasoning = justification
    → 🟢 Nisbett & Wilson 1977: cannot report actual causes
    → IMPLICATION: PFC output (function ⑤) = STRUCTURAL bias
      Not occasional error — DESIGNED to serve body-base
    → Domain Reality = only check on PFC narrative (Inter-Body §6.4)
```

### §6.2 — KB4 Dual Role

```
  COMPILED schemas: PFC = GATE (veto/allow, minimal effort, PFC quiet)
  NEW schemas:      PFC = WORKSPACE MANAGER (hold space, effortful, PFC active)
  LEARNING = migration: Workspace → Gate (PFC freed for next thing)
```

### §6.3 — Sub-regions

```
  dlPFC: hold multiple schemas → compare A vs B
  vmPFC: BRIDGE body↔conscious → somatic marker (Damasio). Weak = poor decisions.
  OFC:   predict reward per action → flexible update. Hyperactive = OCD.
  ACC:   detect schema CONFLICT → alert "sao sao ấy". Hypo = abulia. Hyper = anxiety.
  mPFC:  simulate other minds (Theory of Mind) → DMN hub → empathy ceiling = chunk overlap
```

### §6.4 — Top-down spotlight

```
  PFC → VTA (dopamine) + LC (NE) + BF (acetylcholine) → target cortical area
  → Neurons fire MẠNH HƠN (gain increase) = "spotlight"
  → PFC không bật/tắt cortex — PFC SÁNG/TỐI cortex
  
  = Bidirectional: bottom-up saliency + top-down spotlight = attention loop
  🟢 Desimone & Duncan 1995, Miller & Cohen 2001
```

### §6.5 — PFC KHÔNG compute — PFC orchestrate

```
  PFC = CONDUCTOR, không phải player
  → Conductor không chơi nhạc — conductor ĐIỀU PHỐI
  → PFC draft + test + route + brake + translate + spotlight + gate
  → PFC KHÔNG: tính toán, tạo nội dung, đánh giá, ra quyết định cuối cùng
```

---

## §7 — Simulation: Top-down Re-activation

> **Full analysis: [Imagination-Analysis-v2.md](Imagination/Imagination-Analysis-v2.md)**

### §7.1 — PFC re-activate cortical patterns

```
⭐ IMAGINATION = PFC re-activate CÙNG cortical areas dùng cho real perception

  REAL PERCEPTION (bottom-up):
    Mắt thấy con ngựa → retina → LGN → V1 → V2 → V4 → IT
    → IT fire pattern "con ngựa" → PFC observe → BIẾT "con ngựa"
    → Activation: MẠNH (100% — real photon input)

  IMAGINATION (top-down):
    PFC "nghĩ về con ngựa" → spotlight signal NGƯỢC VỀ visual cortex
    → IT fire pattern "con ngựa" (CÙNG neurons, CÙNG area)
    → Activation: YẾU HƠN (~30-50% so với real input)
    → = "Thấy" con ngựa trong đầu — MỜ hơn thực tế

  ⭐ CÙNG CORTICAL AREA, KHÁC HƯỚNG + CƯỜNG ĐỘ:
    Bottom-up (real): sensor → thalamus → cortex → PFC    [MẠNH, RÕ]
    Top-down (imagine): PFC → cortex (re-activate pattern) [YẾU, MỜ]

  🟢 Kosslyn 1994, 2005: fMRI xác nhận — imagine dùng CÙNG V1/V2 với real seeing
  🟢 Pearson 2019: individual differences (aphantasia → hyperphantasia spectrum)
```

### §7.2 — Multi-modal simulation

```
PFC KHÔNG CHỈ re-activate visual — re-activate MỌI modality:

  VISUAL IMAGINE:    PFC → visual cortex  → "thấy" trong đầu
  AUDITORY IMAGINE:  PFC → auditory cortex → "nghe" trong đầu (inner voice, nhạc)
  MOTOR IMAGINE:     PFC → motor cortex    → "cảm giác" cử động (đo được bằng EMG!)
  SOMATIC IMAGINE:   PFC → insula + S1     → "cảm giác" body state
  EMOTIONAL IMAGINE: PFC → amygdala + insula → "cảm thấy" sợ/vui/buồn

  ⭐ BODY THẬT SỰ PHẢN ỨNG VỚI IMAGINATION:

  Fidelity by modality (% so với real experience — 🟡 calibration anchor, không đo chính xác):
    Cortisol/stress response:  40-70%  (cao nhất — imagine threat → cortisol THẬT tăng!)
    Opioid/pleasure:           20-40%
    Motor activation:          10-30%  (đo bằng EMG — cơ co nhẹ khi imagine)
    Oxytocin:                  10-20%

  → Insight: cortisol response MẠNH NHẤT, oxytocin YẾU NHẤT (hướng rõ, số ước lượng)
  → Imagine bị SẾP mắng → cortisol THẬT tăng đáng kể!
  → Imagine ôm người yêu → oxytocin THẬT tăng nhẹ
  → Body KHÔNG phân biệt rõ real vs imagined (chỉ khác intensity)
  → = Lý do: lo lắng về tương lai GÂY HẠI thật (cortisol thật)
  → = Lý do: mental rehearsal CẢI THIỆN performance thật (motor pre-build)
```

### §7.3 — Dual output: Test + Pre-build

```
KHI PFC IMAGINE, 2 thứ xảy ra ĐỒNG THỜI:

  ① TEST: "Idea này có khả thi không?"
     → PFC simulate → body respond → feel "ok" hoặc "sai sai"
     → = Body evaluate BEFORE logic verify
     → = Imagine-Final.md: "draft → body test → pass/fail"

  ② PRE-BUILD: Schema partially compiled
     → Neurons fire pattern → synapses strengthen nhẹ
     → = Schema ĐÃ BẮT ĐẦU compile TRƯỚC KHI thực hiện thật
     → = Mental rehearsal hiệu quả vì: rehearse = pre-compile
     → 🟢 Pascual-Leone 1995: mental piano practice → motor cortex change THẬT
        (5 ngày imagine chơi piano = cortical map mở rộng, dù CHƯA CHẠM piano!)

  ⭐ IMPLICATION:
  → Imagine = KHÔNG "chỉ nghĩ" — imagine = THẬT SỰ thay đổi não (nhẹ)
  → Mỗi lần imagine = 1 micro-compile event
  → Imagine nhiều lần = repetition compile (mechanism ① từ §5.2)
  → = Imagination IS a chunk compilation mechanism (bổ sung cho 4 mechanisms)
```

### §7.4 — Phim/VR = "Hack" real input vào cortical areas

```
⭐ TẠI SAO SỢ PHIM MA DÙ BIẾT LÀ GIẢ:

  PHIM cung cấp REAL input cho 2/5 modalities:
    Visual: mắt thấy zombie THẬT trên screen → V1 fire MẠNH (100% activation)
    Auditory: tai nghe tiếng zombie THẬT từ loa → A1 fire MẠNH (100%)
    → 2 modalities nhận REAL input → pattern match → amygdala fire
    → Amygdala KHÔNG CHECK "thật hay giả" — amygdala fire nếu pattern match
    → = SỢ THẬT dù biết giả (cortisol tăng, heart rate tăng)

  THIẾU:
    Touch: không chạm zombie → somatosensory quiet
    Smell: không ngửi zombie → olfactory quiet
    Proprioception: đang ngồi sofa → vestibular biết "an toàn"
    → 3/5 modalities nói "an toàn" → xung đột → "sợ nhưng biết giả"

  VR = HACK MẠNH HƠN:
    Visual: headset wrap 360° → V1 fire MẠNH
    Auditory: spatial audio → A1 fire MẠNH
    Vestibular: head tracking → vestibular MATCH visual
    Proprioceptive: hand controllers → some proprioceptive match
    → 4/5 modalities → GẦN NHƯ THẬT
    → VR sickness = vestibular-visual MISMATCH (lag, frame drop)
    → = Body detect: "visual nói xoay, vestibular nói đứng yên" → nausea

  ⭐ GENERALIZED PRINCIPLE:
    → Nhiều modalities nhận consistent input → brain treat as REAL
    → Ít modalities hoặc conflict → brain detect "giả" nhưng partial response vẫn fire
    → = Chunk depth (§5.3): nhiều modalities = mạnh hơn = "thật hơn"
```

---

## §8 — Feeling Emergence: Body signal → Conscious awareness

> **Full analysis: [Feeling.md](Body-Base/Feeling/Feeling.md) + [Feeling-Sources.md](Body-Base/Feeling/Feeling-Sources.md)**

### §8.1 — 7-layer model: Raw → Conscious → Label → Explain

```
FEELING = hành trình TÍN HIỆU từ body LÊN consciousness:

  ┌───────────────────────────────────────────────────────────────┐
  │ Layer │ Name              │ Content                │ Fidelity│
  ├───────────────────────────────────────────────────────────────┤
  │  Feel-RawSignals      │ Raw body signals  │ Heart rate, gut, pain  │  100%   │
  │  Feel-Integration     │ Integration       │ Multi-source combine   │  ~95%   │
  │  Feel-Consciousification │ Felt sense     │ "Cái gì đó sao sao"   │  ~90%   │
  │  Feel-Observation     │ Observation       │ "Ở ngực / ở bụng"     │  ~85%   │
  │  Feel-Location        │ Location          │ "Giống lần trước"      │  ~80%   │
  │  Feel-Labeling        │ LABELING          │ "Tôi lo lắng"         │  40-80% │
  │  Feel-Explanation     │ EXPLANATION       │ "Vì deadline"          │  20-70% │
  └───────────────────────────────────────────────────────────────┘

  ⭐ FIDELITY GIẢM DẦN ĐI LÊN (% = calibration anchor, không đo chính xác — Core-Software.md §12.4):
    Feel-RawSignals = body truth (100% — body không nói dối)
    Feel-Labeling = compressed label (40-80% — 1 từ nén 80%+ thông tin)
    Feel-Explanation = PFC confabulation (20-70% — PFC BỊA lý do post-hoc)

  → Người thường "access" feeling ở Feel-Labeling—Feel-Explanation (label + explain)
  → Nhưng Feel-Labeling—Feel-Explanation = LOSSY NHẤT
  → Wise practitioners dwell ở Feel-Consciousification—Feel-Observation (felt sense — pre-verbal, high fidelity)
  → = Gendlin Focusing: train ở lại Feel-Consciousification, không vội nhảy lên Feel-Labeling—Feel-Explanation
```

### §8.2 — Feeling observation circuit: Insula + ACC + vmPFC

```
⭐ 3 VÙNG NÃO = "FEELING CIRCUIT":

  ANTERIOR INSULA:
    ← Nhận: interoceptive signals (tim, phổi, ruột, hormone, đau, nhiệt)
    → Tạo: integrated BODY STATE representation
    → = "Dashboard" hiển thị body đang thế nào
    → Craig 2009: "seat of subjective awareness" 🟢

  ACC (Anterior Cingulate Cortex):
    ← Nhận: conflict signals (schema A vs schema B mismatch)
    → Tạo: "something's off" alert → gửi lên PFC
    → = "Alarm" khi có mâu thuẫn
    → ⭐ ACC = cơ chế vật lý cho "cảm thấy sao sao ấy"

  vmPFC (Ventromedial PFC):
    ← Nhận: insula body state + amygdala valence + memory associations
    → Tạo: BRIDGE giữa body signal và conscious evaluation
    → = "Translator" body → conscious
    → vmPFC strong = feel rõ → quyết định tốt (Damasio somatic marker)
    → vmPFC weak = feel mờ → quyết định tệ (Phineas Gage)

  FLOW:
    Body signals → Insula (integrate) → ACC (check conflict) → vmPFC (bridge to conscious)
    → PFC observe → Feel-Consciousification felt sense → (optional) Feel-Labeling label → (optional) Feel-Explanation explain

  ⭐ FEELING KHÔNG "ở trong PFC" — feeling ở INSULA + ACC:
    PFC chỉ OBSERVE feeling (qua vmPFC bridge)
    Feeling EXIST ở body level (Feel-RawSignals) → insula integrate (Feel-Integration) → felt sense emerge (Feel-Consciousification)
    PFC có thể KHÔNG observe (nếu vmPFC weak, hoặc attention elsewhere)
    → = Feeling tồn tại DÙ PFC không nhận ra (alexithymia)
    → = "Body biết mà đầu không biết" = insula has signal, PFC doesn't read it
```

### §8.3 — 10 Feeling sources: Multi-channel integration

```
FEELING = KHÔNG CHỈ 1 INPUT — mà ~10 channels tích hợp:

  ① L0 Threat signal       (amygdala: nguy hiểm không?)
  ② L1 Interoceptive       (insula: body state — tim, phổi, ruột)
  ③ Novelty signal          (VTA dopamine: mới không? interesting?)
  ④ Meaning/Schema          (temporal: matches gì đã biết?)
  ⑤ Agent mirror input     (mPFC: người khác đang feel gì?)
  ⑥ Mirror-resonance       (mirror neurons: body tự fire theo người khác)
  ⑦ Schema expectation     (đúng predict hay vi phạm?)
  ⑧ Imagine-Final preview  (tương lai feel thế nào?)
  ⑨ Valence compiled       (learned: cái này tốt/xấu từ experience)
  ⑩ Cognitive evaluation   (PFC: logic nói gì?)

  → INSULA integrate ~10 channels → 1 unified body state
  → PFC observe 1 unified state (KHÔNG observe 10 channels riêng)
  → = Lý do: feel PHỨC TẠP + KHÓ label
    (1 từ "lo lắng" nén 10 channels vào 1 label — mất 80%+ info)

  Full detail: Feeling-Sources.md


  ⭐ 5-CHANNEL INPUT VECTOR (Inter-Body §6, v2.0 connection):

  10 feeling sources MAP lên 5-Channel model:
    Ch1 HARDWARE SENSORY (①②③ above: threat, interoceptive, novelty)
    Ch2 BODY STATE (hormone level, fatigue, cortisol — baseline)
    Ch3 COMPILED CHUNKS (④⑦⑨: meaning, schema expectation, valence)
    Ch4 ENTITY ACTIONS (⑤⑥: agent mirror, mirror-resonance)
    Ch5 PFC ACTIVE CHAIN (⑧⑩: imagine-final preview, cognitive evaluation)

  Each episode = unique MIX of 5 channel intensities
  = 5-dimensional input space → infinite unique episodes
  Channel DOMINANT → determines body-need activation direction
  Channel ABSENT → determines vulnerability to manipulation

  Protection principle: không bao giờ act chỉ từ 1 channel alone
  (Inter-Body §6.4: Domain Reality = Final Arbiter)
```

### §8.4 — 2-Direction Flow (recap từ Logic-Planning §7.4)

```
⭐ FEELING → LABEL: 2 hướng vào cùng đích

  DIRECTION A — FEEL-FIRST (bottom-up):
    Body pattern fire → feel vague (Feel-Consciousification) → PFC chú ý → chunk rõ dần
    → tìm label (Feel-Labeling) → dùng trong logic plan
    = Trẻ sơ sinh, adult novel insight, Einstein

  DIRECTION B — LABEL-FIRST (top-down):
    Nhận label (education) → luyện tập → body compile chunk → feel match label
    = Học sinh, bác sĩ, đọc sách "à, CÁI NÀY là anxiety"

  Cùng đích: chunk có label → dùng được trong plan
  Khác điểm xuất phát: body-first vs language-first
```

---

## §9 — Externalization Loop: Weak internal → Strong external

> **Full analysis: [Somatic-Articulation-Loop.md](Imagination/Somatic-Articulation-Loop.md)**

### §9.1 — Principle: Internal weak → Externalize → Re-input strong

```
⭐ EXTERNALIZATION = HACK chuyển weak top-down thành strong bottom-up:

  TOP-DOWN (imagine):
    PFC re-activate cortical pattern → YẾU (~30-50%)
    → Mờ, khó giữ, dễ mất, WM limit ~3-5 items

  EXTERNALIZE (output ra thế giới):
    Tay vẽ → hình trên giấy
    Miệng nói → âm thanh trong không khí
    Tay viết → chữ trên màn hình
    Tay chơi đàn → âm thanh từ nhạc cụ

  RE-INPUT (bottom-up):
    Mắt nhìn hình vẽ → visual cortex fire MẠNH (100% — real input!)
    Tai nghe mình nói → auditory cortex fire MẠNH
    → Pattern bây giờ RÕ + MẠNH + BỀN hơn internal imagine

  COMPARE:
    PFC so sánh: external (rõ) vs internal intent (mờ)
    → "Đúng ý tôi" → keep
    → "Chưa đúng, sừng hơi to" → sửa → vẽ lại → re-input → compare again
    → = FEEDBACK LOOP: imagine → externalize → perceive → compare → adjust
```

### §9.2 — Instances: Mọi creative process dùng cơ chế này

```
  Họa sĩ:      imagine (weak) → vẽ → nhìn (strong) → sửa → vẽ lại
  Nhạc sĩ:     hear in head (weak) → chơi đàn → nghe (strong) → adjust
  Nhà văn:      think idea (weak) → viết → đọc lại (strong) → revise
  Programmer:   think logic (weak) → code → run → see result (strong) → debug
  Nhà khoa học: hypothesis (weak) → experiment → observe (strong) → revise
  Kiến trúc sư: imagine building (weak) → draw blueprint → look (strong) → refine

  → MỌI creative/intellectual process = CÙNG loop:
    Internal (weak top-down) → Externalize → Re-perceive (strong bottom-up) → Compare → Iterate
```

### §9.3 — Somatic-Articulation Loop: Feeling-specific externalization

```
  Feeling version của externalization loop:

  Feel vague (Feel-Consciousification, weak) → thử nói ra / viết ra → nghe lại / đọc lại (strong)
  → Body check: "gần đúng" / "chưa" / "ĐÚNG RỒI!"
  → Adjust label → thử lại → body check → ...
  → Cuối cùng: feeling có label chính xác → dùng được trong logic

  CATALYST cần thiết:
    → Người nghe (therapist, bạn bè, vợ chồng)
    → AI (available 24/7, patient, multi-format)
    → Viết (journaling, freewriting)
    → Vẽ (art therapy)

  = Somatic-Articulation-Loop.md: "body-knowledge → explicit-knowledge"
  = KHÔNG phải retrieval — mà là CONSTRUCTION process (xây dần, không lấy sẵn)
```

### §9.4 — Clark Extended Mind

```
🟢 CLARK & CHALMERS 1998 — Extended Mind Thesis:

  "Mind KHÔNG chỉ ở trong sọ — mind INCLUDE external tools"

  Giấy + bút = mở rộng WM (vẽ ra = thêm visual "memory" ngoài não)
  Calculator = mở rộng math processing
  Code editor = mở rộng logic processing
  AI chatbot = mở rộng articulation capacity

  → Externalization KHÔNG phải "dump info ra ngoài"
  → Externalization = EXTEND cognitive capacity vượt brain limits
  → = Brain (3-5 WM slots) + Paper (unlimited visual slots) = STRONGER system

  ⭐ AI ERA EXTENSION:
  → AI = externalization partner CỰC MẠNH
  → Feel vague → nói cho AI → AI suggest label → body check → iterate
  → AI help plan → PFC freed → can feel more
  → = "Con người cần FEEL đúng → AI sẽ giúp PLAN đúng" (Logic-Planning.md)
```

---

## §10 — Complete Flow Diagram

### §10.1 — Full flow: Sensor → PFC → Output → Feedback

```
⭐ TOÀN BỘ FLOW TRONG 1 DIAGRAM:

  ┌──────────────────────────────────────────────────────────────────┐
  │                    BODY SENSORS (~20+ types)                     │
  │  Exteroceptive: mắt, tai, mũi, lưỡi, da                       │
  │  Proprioceptive: vị trí, thăng bằng, chuyển động                │
  │  Interoceptive: tim, phổi, ruột, hormone, đau, nhiệt           │
  └────────────────────────┬─────────────────────────────────────────┘
                           │ raw electrical signals (action potentials)
                           ▼
  ┌──────────────────────────────────────────────────────────────────┐
  │                    THALAMUS (Gateway)                             │
  │  • Mỗi sense → nucleus riêng (LGN, MGN, VPL, VPM,...)          │
  │  • FILTER + GATE (TRN control, PFC directs)                     │
  │  • Exceptions: olfaction bypass thalamus, low road bypass cortex │
  └────────────────────────┬─────────────────────────────────────────┘
                           │ filtered signals → Layer 4
                           ▼
  ┌──────────────────────────────────────────────────────────────────┐
  │               CORTICAL AREAS (6-layer columns)                   │
  │                                                                  │
  │  Visual    Auditory    Somatosensory    Motor    Emotional       │
  │  cortex    cortex      cortex (S1/S2)   cortex   (amygdala)     │
  │    │          │             │              │          │          │
  │    ├──sparse cross-modal connections (Layer 2/3)──────┤          │
  │    │          │             │              │          │          │
  │    └──────────┴─────────────┴──────────────┴──────────┘          │
  │                         │                                        │
  │              BINDING MECHANISMS:                                  │
  │              • Gamma sync ~40Hz                                  │
  │              • Multisensory neurons                              │
  │              • Convergence zones (Parietal/STS/Insula)           │
  │              • Amygdala affective tagging                        │
  │              • DMN scaffolding                                   │
  │                         │                                        │
  │              COMPILATION:                                        │
  │              • Repetition / Emotional peak /                     │
  │                Multi-modal / Sleep consolidation                 │
  │              • Pattern → Chunk → Meta-chunk                      │
  └────────────────────────┬─────────────────────────────────────────┘
                           │ compiled patterns (chunks)
                           ▼
  ┌──────────────────────────────────────────────────────────────────┐
  │           FEELING CIRCUIT (Insula + ACC + vmPFC)                 │
  │                                                                  │
  │  Anterior Insula: integrate body state (10 channels → 1 state)  │
  │  ACC: detect conflict → "sao sao ấy" signal                    │
  │  vmPFC: bridge body → conscious (somatic marker)                │
  │                         │                                        │
  │  → Feel-RawSignals raw → Feel-Integration integrate → Feel-Consciousification felt sense → (optional Feel-Labeling label) │
  └────────────────────────┬─────────────────────────────────────────┘
                           │ feeling signals + compiled chunks
                           ▼
  ┌──────────────────────────────────────────────────────────────────┐
  │                    PFC (Orchestrator)                             │
  │                                                                  │
  │  OBSERVE:   đọc compiled patterns + feeling state                │
  │  DRAFT:     tạo temporary patterns (mixed-selectivity neurons)  │
  │  TEST:      gửi xuống specialist regions (amygdala/insula/BG)   │
  │  ROUTE:     pass/discard based on body feedback                 │
  │  BRAKE:     veto behavioral output (~200-500ms)                 │
  │  TRANSLATE: verbalize post-hoc                                   │
  │  SPOTLIGHT:  amplify target cortical areas (NE + Ach + DA)      │
  │  SIMULATE:  re-activate cortical patterns TOP-DOWN (§7)         │
  │                                                                  │
  │  dlPFC: compare   vmPFC: value   OFC: reward   ACC: conflict   │
  │  mPFC: social simulation (Theory of Mind, DMN hub)              │
  └──────────┬───────────────────────────────────┬───────────────────┘
             │ motor commands                     │ top-down re-activation
             ▼                                    ▼
  ┌────────────────────┐            ┌─────────────────────────────┐
  │  MOTOR OUTPUT       │            │  SIMULATION (top-down)      │
  │  • Speech (Broca)   │            │  • Re-activate visual/      │
  │  • Hand movement    │            │    auditory/motor/somatic   │
  │  • Facial expression│            │  • ~30-50% activation       │
  │  • Body posture     │            │  • Body RESPONDS (real      │
  │  • Writing/Drawing  │            │    cortisol, real EMG)      │
  │  • Code typing      │            │  • Dual: test + pre-build   │
  └────────┬───────────┘            └──────────────────────────────┘
           │ externalized output
           ▼
  ┌──────────────────────────────────────────────────────────────────┐
  │              EXTERNALIZATION LOOP                                 │
  │                                                                  │
  │  Internal (weak, ~30-50%) → Externalize (hand/voice/write)      │
  │  → Re-perceive (strong, 100% — real visual/auditory input)     │
  │  → Compare (PFC: external vs internal intent)                   │
  │  → Adjust → Externalize again → ...                             │
  │                                                                  │
  │  = Creative process loop. Writing-as-thinking. Drawing-as-seeing│
  │  = Somatic-Articulation Loop (feeling → label construction)     │
  │  = AI catalyst: feel → tell AI → AI suggest → body check        │
  └──────────────────────────┬───────────────────────────────────────┘
                             │ feedback (re-enters as new input)
                             ▼
                    ← BACK TO BODY SENSORS (loop) ←
```

### §10.2 — Bottom-up vs Top-down: 2 directions

```
BOTTOM-UP (reality → brain):
  Sensor → Thalamus → Cortex → Binding → Chunk → Feeling → PFC observe
  = "Thế giới nói cho não biết"
  = MẠNH, chính xác, body-driven
  = Source of feeling (Feel-RawSignals—Feel-Consciousification)
  = Source of chunk compilation

TOP-DOWN (brain → cortex re-activation):
  PFC → Spotlight → Cortex re-activate → Body respond (partial)
  = "Não tự nói cho mình"
  = YẾU hơn (~30-50%), có thể sai (confabulation)
  = Source of imagination, planning, simulation
  = Source of mental rehearsal, worry, creativity

⭐ HEALTHY COGNITION = CÂN BẰNG 2 HƯỚNG:
  Quá nhiều bottom-up = reactive (chỉ respond, không plan)
  Quá nhiều top-down = detached (sống trong đầu, không feel reality)
  Balance = feel reality (bottom-up) + plan ahead (top-down) + check (feedback)
```

### §10.3 — Observation Parameters modulating flow (v2.0 FIX)

```
⚠️ v2.0 FIX: v1.0 called these "L3 operators" — outdated.
   v7.8 reframe: L3 removed. These are OBSERVATION PARAMETERS
   (named patterns emerging from body-need interactions, not a separate layer).
   Inter-Body §2.3: "Observation params = NOT sources — are NAMES cho patterns observable."

3 OBSERVATION PARAMETERS MODULATE flow (not create separate flow):

  NOVELTY (observation parameter):
    → VTA detect above-baseline input quality → dopamine → PFC spotlight
    → Shifts baselines upward (hedonic treadmill)
    → Operates across ALL body-input categories
    → = NAMED PATTERN from gap-fill drive (Gap-Direction.md)

  STATUS (observation parameter):
    → PFC construct: social position → PROXY for body-input access
    → Status itself has NO body-base receiver
    → Status → body-input payoff (community → co-presence; reputation → resources)
    → Status without payoff = emptiness
    → = NAMED PATTERN from social hardware needs (Inter-Body §1)

  PROTECT (observation parameter):
    → Guard body-inputs from threats
    → Extends via Empathy-Mirror: mirrored body-state → protect-other behavior
    → = NAMED PATTERN from ownership + loss aversion (Protect.md)

  → 3 parameters MODULATE flow, không tạo flow riêng
  → Novelty: ảnh hưởng CÁI GÌ được spotlight
  → Status: ảnh hưởng CÁI GÌ PFC draft as goal
  → Protect: ảnh hưởng CÁI GÌ gets priority (threat override)
  → Can thiệp ở level mechanism (body-need sources), không ở level label
```

---

## §11 — Honest Assessment + References

### §11.1 — Confidence levels

```
═══════════════════════════════════════
🟢 ESTABLISHED NEUROSCIENCE
═══════════════════════════════════════

  Thalamic relay + gating:           Sherman & Guillery 2006, Jones 2007
  6-layer cortical column:           Mountcastle 1957, Douglas & Martin 2004
  Visual hierarchy V1→IT:            Felleman & Van Essen 1991, Hubel & Wiesel 1962
  Olfaction bypass thalamus:         Gottfried 2010
  Amygdala subcortical pathway:      LeDoux 1996
  Multisensory neurons:              Stein & Meredith 1993, Ghazanfar 2006
  Amygdala emotional modulation:     McGaugh 2004
  DMN at birth:                      Doria et al. 2010
  Anterior insula interoception:     Craig 2002, 2009
  vmPFC somatic marker:              Damasio 1994, 1996
  Top-down re-activation (imagine):  Kosslyn 1994, 2005
  Mental rehearsal motor:            Pascual-Leone 1995
  ACC conflict detection:            Botvinick et al. 2004
  PFC attention control:             Desimone & Duncan 1995, Miller & Cohen 2001
  TRN attention gating:              McAlonan et al. 2008
  C-tactile affective touch:         Olausson 2002
  Predictive interoception:          Seth 2013, Barrett 2017
  Extended mind:                     Clark & Chalmers 1998
  Sleep consolidation:               Diekelmann & Born 2010
  Felt sense / Focusing:             Gendlin 1978
  PFC mixed selectivity:             Rigotti et al. 2013
  Expert chunking:                   Chase & Simon 1973
  Hebbian learning:                  Hebb 1949
  LTP discovery:                     Bliss & Lømo 1973
  Activity-dependent myelination:    Fields 2008
  Split-brain confabulation:         Gazzaniga (v2.0: PFC=Lawyer)
  Moral intuition first:             Haidt 2001 (v2.0: PFC=Lawyer)
  Cannot report causes:              Nisbett & Wilson 1977 (v2.0: PFC=Lawyer)


═══════════════════════════════════════
🟡 FRAMEWORK SYNTHESIS
═══════════════════════════════════════

  Gamma binding as PRIMARY mechanism:    Singer well-supported, debate ongoing
  5-mechanism binding model:             4 from Emergent-Binding + gamma = synthesis
  Many-to-many mapping as reframe:       Consistent with evidence, framework framing
  7-layer feeling fidelity gradient:     Framework contribution (Feeling.md)
  10-channel feeling integration:        Framework contribution (Feeling-Sources.md)
  Externalization as general principle:   Consistent, generalized from established instances
  PFC 5-function model:                  Framework synthesis (PFC-Analysis.md)
  KB4 dual role:                         Framework synthesis, consistent
  Chunk depth = modality count:          Framework contribution (Modality-Analysis.md)
  2-Direction flow (feel-first/label-first): Framework contribution (Logic-Planning.md)
  Compilable Architecture as WHY this hardware (v2.0): Consistent with evolutionary neuroscience
  Compiled/Fresh at physical level (v2.0):   LTP + myelin = established; framing = synthesis
  PFC = Lawyer as structural function (v2.0): Consistent with Gazzaniga/Haidt, elevated
  5-Channel Input Vector mapping (v2.0):     Framework synthesis (Inter-Body §6)
  Observation parameters (not L3 operators):  v7.8 reframe, consistent


═══════════════════════════════════════
🔴 HYPOTHESES
═══════════════════════════════════════

  Specific fidelity percentages (Feel-RawSignals 100%, Feel-Explanation 20-70%):  Illustrative, not measured
  Imagination fidelity % per modality:                  Approximate, varies individually
  "ACC = physical mechanism for 'sao sao ấy'":         Plausible, not directly tested
  AI as externalization catalyst effectiveness:         New, unstudied longitudinally
```

### §11.2 — What this file CLAIMS vs NOT CLAIMS

```
CLAIMING:
  ✓ Body signals travel specific physical pathways to specific cortical areas
  ✓ Thalamus gates most (not all) sensory input
  ✓ Cortical architecture is uniform 6-layer (Mountcastle), specialized by wiring
  ✓ Sensor→cortex mapping is many-to-many (not 1:1)
  ✓ Binding uses multiple concurrent mechanisms (not single binder)
  ✓ PFC observes compiled patterns, does not compute raw data
  ✓ PFC can re-activate cortical patterns top-down (imagination)
  ✓ Body responds to imagination (partial, measurable)
  ✓ Feeling emerges in insula/ACC/vmPFC circuit, PFC observes
  ✓ Externalization converts weak top-down to strong bottom-up

NOT CLAIMING:
  ✗ This is a complete neuroscience textbook (simplified for framework use)
  ✗ Specific neuron counts or exact pathway details are comprehensive
  ✗ Fidelity percentages are measured (they are framework estimates)
  ✗ Binding problem is "solved" (active research area)
  ✗ Consciousness is explained (hard problem remains)
```

### §11.3 — Full reference list

```
  Andersen 1997    — Multimodal spatial representations in parietal cortex
  Barrett 2017     — Predictive interoception / constructed emotion
  Berson 2002      — ipRGC circadian pathway
  Botvinick 2004   — ACC conflict monitoring
  Brown & Kulik 1977 — Flashbulb memory
  Chase & Simon 1973 — Expert chunking in chess
  Clark & Chalmers 1998 — Extended Mind thesis
  Craig 2002, 2009 — Interoception, anterior insula, awareness
  Crick 1984       — Searchlight hypothesis (thalamus + attention)
  Damasio 1989     — Convergence-divergence zones
  Damasio 1994     — Somatic marker hypothesis / Descartes' Error
  Desimone & Duncan 1995 — Biased competition attention model
  Diekelmann & Born 2010 — Sleep-dependent memory consolidation
  Doria et al. 2010 — Neonatal DMN functional connectivity
  Douglas & Martin 2004 — Canonical cortical microcircuit
  Engel & Singer 2001 — Temporal binding by gamma oscillation
  Felleman & Van Essen 1991 — Hierarchical visual processing
  Fries 2005       — Communication through coherence
  Gendlin 1978     — Focusing / felt sense
  Ghazanfar & Schroeder 2006 — Cross-modal cortical interactions
  Gottfried 2010   — Olfactory-limbic direct pathway
  Hein & Knight 2008 — STS multimodal person processing
  Hubel & Wiesel 1962 — Visual cortex feature detection
  Jones 2007       — Thalamic nuclei functional mapping
  Kanwisher 1997   — Fusiform face area (FFA)
  Kosslyn 1994, 2005 — Mental imagery uses visual cortex
  LeDoux 1996      — Amygdala fear conditioning / subcortical pathway
  McAlonan et al. 2008 — TRN attentional gating
  McGaugh 2004     — Emotional modulation of memory
  Miller & Cohen 2001 — PFC top-down control
  Mountcastle 1957 — Cortical column uniformity
  Olausson 2002    — C-tactile affective touch pathway
  Pascual-Leone 1995 — Mental rehearsal changes motor cortex
  Pearson 2019     — Mental imagery individual differences
  Rigotti et al. 2013 — PFC mixed selectivity neurons
  Seth 2013        — Predictive interoception
  Sherman & Guillery 2006 — Thalamus as active relay
  Singer & Gray 1995 — Gamma oscillation binding
  Stein & Meredith 1993 — Multisensory integration
  Hebb 1949            — Hebbian learning principle (v2.0)
  Bliss & Lømo 1973   — LTP discovery (v2.0)
  Fields 2008         — Activity-dependent myelination (v2.0)
  Gazzaniga            — Split-brain confabulation (v2.0: PFC=Lawyer)
  Haidt 2001           — Moral intuition first (v2.0: PFC=Lawyer)
  Nisbett & Wilson 1977 — Cannot report actual causes (v2.0: PFC=Lawyer)
```

---

## §12 — CROSS-REFERENCES (v2.0 NEW)

```
📚 INTER-BODY DRILL:
  → Inter-Body-Mechanism.md v1.0 §1: Compilable Architecture (WHY this hardware)
  → Inter-Body-Mechanism.md v1.0 §3: Compiled/Fresh = real axis (→ §5.5)
  → Inter-Body-Mechanism.md v1.0 §6: 5-Channel Input Vector (→ §8.3)
  → Inter-Body-Mechanism.md v1.0 §7: PFC = Lawyer (→ §6.1)

📚 FEELING + BODY-FEEDBACK:
  → Feeling.md v3.0 §2.5: Compiled/Fresh × 7-Layer mapping
  → Feeling.md v3.0 §3.4: PFC = Lawyer formal
  → Body-Feedback-Mechanism.md v2.0: 2-source, Body-Need aggregate
  → Body-Input-Enumeration.md: full body input catalog (§1 source)

📚 PROCESSING:
  → Logic-Feeling.md v2.0 §1: Compiled/Fresh = trục thật
  → Logic-Feeling.md v4.0 §3: Flow (Body-Knowing Anchor ↔ Fresh Explore ↔ Domain Verify)
  → PFC-Analysis.md: PFC functions detail
  → Somatic-Articulation-Loop.md: externalization mechanism detail

📚 CHUNK + COMPILATION:
  → Chunk.md v2.0: chunk system reference
  → Modality-Analysis.md: modality depth

📚 OBSERVATION:
  → Gap-Direction.md v2.0: gap direction (novelty parameter)
  → Protect.md v1.0: protect parameter
  → Status.md v2.0: status parameter
```

---

## §13 — STATUS (v2.0)

```
File: Neural-Processing-Flow.md
Version: 2.0
Created: 2026-04-17
Updated: 2026-05-17
Previous: v1.0 → backup/Neural-Processing-Flow-v1.0-backup.md
Lines: ~1,230

v2.0 CHANGES (2026-05-17 — Inter-Body Drill Integration):
  → Header: v2.0, +dependencies, +confidence markers
  → §0: +Compilable Architecture connection (WHY this hardware = general-purpose)
  → §5.5 NEW: Compiled/Fresh at PHYSICAL level
    (WHY compiled=fast: LTP+myelin. WHY fresh=slow: novel unmyelinated paths)
  → §6.1: +PFC=Lawyer elevated (structural function, not occasional error)
  → §8.3: +5-Channel Input Vector connection (10 channels → 5-channel model)
  → §10.3 FIX: "L3 operators" → "Observation parameters" (v7.8 reframe)
  → §11: +6 🟢 citations (Hebb, Bliss&Lømo, Fields, Gazzaniga, Haidt, Nisbett&Wilson)
         +5 🟡 items (Compilable Architecture, Compiled/Fresh physical, PFC=Lawyer, 5-Channel, observation parameters)
  → §12 NEW: Cross-references section
  → ALL v1.0 hardware content PRESERVED (§1-§4, §7, §9)
  → ALL 35+ research citations preserved + 6 added = 41+ total
```

---

> **Neural-Processing-Flow.md v2.0 — End of file.**
>
> Nền tảng gốc: toàn bộ flow vật lý từ sensor → thalamus → cortex → binding → chunks → feeling → PFC → simulation → externalization → feedback loop.
>
> v2.0: +Compilable Architecture (WHY), +Compiled/Fresh physical (HOW compiled=fast),
> +PFC=Lawyer (structural), +5-Channel mapping, +L3→observation parameter fix.
>
> Mọi cơ chế khác trong framework CHẠY TRÊN flow này.
>
> **Phiên bản:** v2.0, 2026-05-17.