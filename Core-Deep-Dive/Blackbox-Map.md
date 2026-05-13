# Blackbox-Map — Bản Đồ Vùng Chưa Biết (5-Layer Gap Analysis)

> Framework mô tả body-brain system ở level HÀNH VI.
> Nhưng giữa hành vi và neuron vật lý = NHIỀU TẦNG chưa biết.
>
> Giống máy tính: bạn biết chuột USB và con trỏ trên màn hình.
> Nhưng driver code ở giữa — bạn không viết, không đọc, không kiểm soát.
> Body-brain system cũng vậy.
>
> File này map CHÍNH XÁC chỗ nào framework "jump qua" —
> không phải để nói "framework yếu," mà để trỏ ra:
> ① Ranh giới rõ ràng giữa BIẾT và CHƯA BIẾT
> ② Hướng nghiên cứu cụ thể cho từng vùng chưa biết
> ③ Cơ sở để bất kỳ ai cũng có thể drill sâu hơn
>
> Nếu framework đúng → đây là bản đồ FRONTIER của domain.
> Nếu framework sai ở chỗ nào → tìm ra chỗ đó cũng có giá trị.

---

> **Trạng thái:** v1.0
> **Ngày:** 2026-05-12
> **Vị trí:** Core-Deep-Dive/ (fundamental analysis — ngang hàng Neural-Architecture, Neural-Processing-Flow)
> **Supersedes:** Research/Meta-Impact/Framework-Boundaries.md v2.0 (→ backup/)
>   Nội dung Framework-Boundaries.md v2.0 (1 blackbox + 2 complexity dimensions)
>   được tích hợp vào §4 + §7 file này. Không mất thông tin.
> **Dual purpose:**
>   ① Honest assessment — framework biết gì, không biết gì
>   ② Research roadmap — mỗi gap = hướng nghiên cứu testable
> **Confidence:** 🟢 Research support | 🟡 Framework synthesis | 🔴 Hypothesis
> **Language:** Tiếng Việt primary + English technical terms

---

## Mục lục

- §0 — TẠI SAO FILE NÀY QUAN TRỌNG
- §1 — 5-LAYER MODEL: COMPUTER ANALOGY
- §2 — GAP 1: BODY-INPUT COMPLETENESS (Layer 1)
- §3 — GAP 2: SIGNAL TRANSDUCTION — "DRIVER LAYER" (Layer 1→3)
- §4 — GAP 3: CHUNK SUBSTRATE — FUNDAMENTAL BLACKBOX (Layer 3)
- §5 — GAP 4: INTEGRATION → FEELING → CONSCIOUSNESS (Layer 3→4)
- §6 — GAP 5: HORMONE COMBINATORICS (Cross-cutting)
- §7 — COMPLEXITY DIMENSIONS (Scale + Hardware Variance)
- §8 — FRAMEWORK AS RESEARCH ROADMAP
- §9 — AI AS DYNAMIC DRILL TOOL
- §10 — CROSS-REFERENCES

---

## §0 — TẠI SAO FILE NÀY QUAN TRỌNG

```
Framework mô tả body-brain system ở level HÀNH VI:
  → "Chunk compile qua repetition + emotional peak"
  → "Cortisol = amplifier, không phải stress hormone"
  → "Dopamine = salience signal, không phải reward"
  → "PFC observe, không control"

Những claim này có evidence support (🟢) hoặc synthesis (🟡).
Nhưng ở MỖI claim, framework JUMP QUA một khoảng:

  CLAIM (behavioral)          REALITY (biological)
  ──────────────────          ──────────────────────────
  "chunk compile"         →   neuron nào fire? synapse nào strengthen?
  "cortisol amplifier"    →   GR/MR receptor nào? gene expression nào?
  "VTA fire salience"     →   signal đi con đường nào tới vùng nào?
  "body-feedback reward"  →   opioid receptor subtype nào? ở neuron nào?

Khoảng JUMP này = KHÔNG PHẢI framework sai.
= Framework mô tả ở TẦNG KHÁC — behavioral, không phải molecular.
= Giống kỹ sư phần mềm biết "click chuột → menu hiện"
  nhưng không viết driver code giữa USB signal → OS interrupt → render.

FILE NÀY MAP CHÍNH XÁC 5 khoảng jump đó:
  → Mỗi khoảng = 1 GAP giữa framework và biological reality
  → Mỗi GAP = hướng nghiên cứu cụ thể
  → Mỗi GAP có level nghiêm trọng khác nhau
  → Researcher có thể chọn GAP phù hợp chuyên môn → drill

DUAL PURPOSE:
  ① Cho người đọc: biết framework tin được tới đâu
  ② Cho researcher: biết drill ở đâu sẽ có giá trị nhất
```

---

## §1 — 5-LAYER MODEL: COMPUTER ANALOGY

### §1.1 Analogy

```
🟡 COMPUTER ANALOGY — framework hoạt động ở đâu trong stack:

  MÁY TÍNH                        BODY-BRAIN SYSTEM
  ──────────                       ──────────────────

  Layer 5: USER BEHAVIOR           Layer 5: HUMAN BEHAVIOR
    (click, gõ phím, kéo thả)        (hành động, quyết định, phản ứng)
    = quan sát ĐƯỢC                   = framework MÔ TẢ ĐƯỢC ⭐

  Layer 4: USER INTERFACE           Layer 4: FEELING + PFC OBSERVATION
    (con trỏ, cửa sổ, menu)          (ý thức, cảm nhận, quan sát)
    = thấy ĐƯỢC, mô tả ĐƯỢC          = framework mô tả PATTERN (7-layer)

  Layer 3: SOFTWARE                 Layer 3: CHUNK PROCESSING
    (click handler, render loop)      (compile, fire, associate, install)
    = viết được, debug được           = framework mô tả FUNCTION ⚠️
                                        nhưng KHÔNG BIẾT implementation

  Layer 2: DRIVERS                  Layer 2: SIGNAL TRANSDUCTION
    (USB driver, GPU driver)          (neurotransmitter, receptor binding,
    = ít người đọc, ít người hiểu      ion channel, gene expression)
                                      = framework JUMP QUA ⚠️⚠️

  Layer 1: HARDWARE                 Layer 1: PHYSICAL BODY
    (sensor, chip, mạch điện)         (receptor, neuron, organ, hormone)
    = biết có, biết function          = neuroscience biết PHẦN LỚN
      nhưng không biết HẾT              nhưng chưa biết HẾT

                    ↕                              ↕
  Framework hoạt động                Framework hoạt động
  ở Layer 3-5                        ở Layer 3-5
  (software + UI + behavior)         (chunk + feeling + behavior)

  Layer 1-2 = neuroscience +         Layer 1-2 = molecular biology +
  electrical engineering territory   neuroscience territory
```

### §1.2 Ở đâu framework MẠNH, ở đâu framework JUMP

```
🟡 FRAMEWORK COVERAGE MAP:

  Layer 5 (Behavior):
    ████████████████████ 95%+ coverage
    → Observation parameters, patterns, predictions
    → Framework MẠNH NHẤT ở đây

  Layer 4 (Feeling + PFC):
    ██████████████░░░░░░ ~70% coverage
    → 7-layer fidelity, PFC reach gradient, 6 error modes
    → PATTERN mô tả được, HOW integration = partial

  Layer 3 (Chunk Processing):
    ████████░░░░░░░░░░░░ ~40% coverage
    → FUNCTION mô tả được (compile, fire, link, install)
    → IMPLEMENTATION = BLACKBOX (neuron nào? circuit nào?)

  Layer 2 (Signal Transduction):
    ██░░░░░░░░░░░░░░░░░░ ~10% coverage
    → Framework dùng KẾT QUẢ (cortisol = amplifier)
    → PATHWAY CHÍNH XÁC = framework không mô tả

  Layer 1 (Physical Body):
    ██████████████░░░░░░ ~70% coverage (VIA neuroscience)
    → 17 receptor categories, 4 zones A/B/C/D
    → CHI TIẾT molecular = neuroscience textbook territory
    → DANH SÁCH body-input = có thể CHƯA ĐẦY ĐỦ

  ⭐ Pattern rõ ràng:
    → Framework coverage GIẢM DẦN từ Layer 5 → Layer 2
    → Layer 1 coverage phụ thuộc neuroscience (không phải framework)
    → GAP LỚN NHẤT = Layer 2→3 ("Driver Layer")
```

### §1.3 Tại sao gap KHÔNG phải yếu điểm

```
Framework hoạt động ở behavioral level = BY DESIGN:

  ① Mô tả PATTERN không cần biết implementation
     → Kỹ sư phần mềm viết code KHÔNG CẦN biết transistor
     → Framework mô tả behavior KHÔNG CẦN biết từng synapse
     → Mỗi layer có GIỚI HẠN + GIÁ TRỊ riêng

  ② Behavioral description = TESTABLE mà không cần lab
     → "Chunk compile qua repetition" — observe behavior = verify
     → "Cortisol amplifier" — observe pattern = verify
     → Không cần fMRI để thấy pattern → accessible cho mọi người

  ③ Gaps = RESEARCH OPPORTUNITY, không phải weakness
     → Nếu framework đúng ở behavioral level
     → Thì biological level PHẢI có mechanism khớp
     → Tìm mechanism đó = validate HOẶC falsify framework
     → Cả hai kết quả đều có giá trị

  ⚠️ GAP TRỞ THÀNH NGUY HIỂM khi:
     → Ai đó claim framework giải thích ở level molecular — OVERCLAIM
     → Ai đó dùng framework thay clinical protocol — OVERAPPLICATION
     → Framework = la bàn — cho thấy hướng, KHÔNG dẫn đường cụ thể
```

---

## §2 — GAP 1: BODY-INPUT COMPLETENESS (Layer 1)

### §2.1 Hiện trạng

```
Framework liệt kê 17 body-input categories (Core-Software.md §3.2,
Core-Hardware.md §4) trong 3 taxonomy chuẩn neuroscience:

  EXTEROCEPTION (5): Vision, Audition, Olfaction, Gustation, Tactile
  PROPRIOCEPTION (3): Proprioception, Vestibular, Kinesthetic
  INTEROCEPTION (9): Thermo, Nociception, Respiratory, Cardiovascular,
    Visceral, Metabolic, Hormonal-sensed, Sleep/Circadian,
    Self-signal interoception (META KEYSTONE)

Mỗi category có:
  → Receptor system + neural pathway (🟢 neuroscience established)
  → Evolved baseline range (🟡 framework synthesis)
  → Delta rule evaluation (🟡 framework mechanism)
  → Chi tiết: Neural-Processing-Flow.md §1, Body-Input-Enumeration.md

Framework DÙNG 17 categories này làm nền tảng cho toàn bộ body-feedback.
```

### §2.2 Gap: danh sách có thể CHƯA ĐẦY ĐỦ

```
⚠️ 17 CATEGORIES = DANH SÁCH TỐT NHẤT HIỆN TẠI, KHÔNG PHẢI DANH SÁCH CUỐI CÙNG.

Body-input ở level chi tiết = GẦN NHƯ VÔ TẬN.
Framework không cố enumerate hết — chỉ liệt kê CATEGORIES.
Nhưng chính categories cũng có thể thiếu.

CANDIDATES CHƯA CÓ TRONG DANH SÁCH:

  ① Magnetoreception (🟡 Open question)
     → Cryptochrome proteins trong retina người (Wang et al. 2019, Caltech)
     → Chim, rùa biển, cá hồi = SỬ DỤNG RÕ RÀNG
     → Người = chưa rõ có influence behavior không
     → Nếu có → thêm 1 exteroceptive channel

  ② Microbiome → Brain neural signals (🟢 Active research, chưa đầy đủ)
     → Gut-brain axis tồn tại (🟢 — ⑬ Visceral đã cover PHẦN NÀO)
     → ~95% serotonin sản xuất ở ruột (🟢 Yano et al. 2015)
     → NHƯNG: microbiome composition → specific neural signals
       → specific behavior changes = đang nghiên cứu MẠNH
     → Có thể ⑬ Visceral CHƯA ĐỦ để cover hết microbiome influence

  ③ Pheromone processing (🟡 Tranh luận)
     → Vomeronasal organ tồn tại ở người (vestigial?)
     → Androstadienone, estratetraenol = candidates
     → Có thể influence social behavior mà framework chưa track

  ④ Infrasound sensing (🟡 Một số evidence)
     → Con người có thể sense < 20Hz
     → Gây unease, "feeling of presence" (Vic Tandy 1998)
     → Nếu thật → 1 exteroceptive channel ẩn

  ⑤ Barometric pressure sensing (🟡 Anecdotal + một số research)
     → "Đau xương trước trời mưa" = phổ biến
     → Nociceptors có thể respond to pressure changes
     → Mechanism chưa rõ hoàn toàn

  ⑥ Immune system → Brain signaling (🟢 Established, framework chưa integrate)
     → Cytokines cross BBB → sickness behavior (🟢 Dantzer 2008)
     → ⑮ Hormonal-sensed cover PHẦN NÀO
     → NHƯNG: immune signaling phức tạp hơn "hormonal-sensed"
     → "Ốm → buồn, mệt, withdrawal" = immune signal, không chỉ hormone

⭐ NGUYÊN TẮC: Danh sách body-input = OPEN-ENDED.
   Framework acknowledge: có thể phát hiện thêm channels.
   Mechanism (delta rule, baseline adaptation) = UNIVERSAL —
   áp dụng cho BẤT KỲ body-input nào, kể cả chưa biết.
   Phát hiện input mới → thêm vào → framework vẫn hoạt động.
```

### §2.3 Chiều sâu trong MỖI category

```
Mỗi category framework liệt kê = TỔNG HỢP của rất nhiều sub-systems.

VÍ DỤ — ① VISION:
  Framework nói: "Vision: retina, V1→IT pathway, FFA"
  Thực tế bên trong:
    → Retina: ~120M rods + ~6M cones + ~1.5M ganglion cells
    → Ganglion: ~20+ loại (ON, OFF, ON-OFF, direction-selective,...)
    → ipRGC (intrinsically photosensitive) → circadian, bypass visual
    → Optic nerve → chiasm (partial crossing) → LGN (6 layers!)
    → LGN → V1 → V2, V4, MT, IT — mỗi vùng sub-specialization
    → Koniocellular, Magnocellular, Parvocellular pathways
    → = HÀNG NGHÌN chi tiết framework không (và không cần) mô tả

VÍ DỤ — ⑬ VISCERAL:
  Framework nói: "ENS ~100-500M neurons, gut-brain axis"
  Thực tế bên trong:
    → ENS có 2 plexus (Auerbach + Meissner)
    → ~30 neurotransmitters (serotonin, dopamine, acetylcholine,...)
    → Vagus nerve: ~80% AFFERENT (gut → brain, không chỉ brain → gut)
    → Microbiome: ~38 NGÀN TỶ vi khuẩn → metabolites → neural signals
    → Short-chain fatty acids, tryptophan metabolism,...
    → = TOÀN BỘ "second brain" framework chỉ note, không drill

⭐ NGUYÊN TẮC:
   Framework mô tả ở CATEGORY level. Chi tiết bên trong = vô tận.
   Mỗi category = cửa ngõ dẫn vào toàn bộ sub-domain khoa học.
   Neuroscience / physiology textbook = nơi có chi tiết đó.
   AI có thể chỉ ra chi tiết tế bào khi user hỏi cụ thể (§9).
```

### §2.4 Research direction

```
HƯỚNG NGHIÊN CỨU TỪ GAP 1:

  RD-1.1: Magnetoreception ở người — có influence behavior không?
    → Method: fMRI trong từ trường thay đổi có kiểm soát
    → Predict (nếu framework đúng): nếu magnetoreception active
      → phải có baseline → phải có delta rule → phải có body-feedback
    → Reference: Wang et al. 2019

  RD-1.2: Microbiome → Behavior pathway chi tiết
    → Gut microbiome composition → specific neurotransmitter changes
      → specific behavioral patterns
    → Method: germ-free mice + human microbiome transplant + fMRI
    → Predict: microbiome change → baseline shift → body-feedback

  RD-1.3: Immune → Brain → Behavior mapping
    → Cytokine profiles → specific neural activation → specific behavior
    → Method: controlled inflammation + behavioral + neural measurement
    → Predict: immune signal = body-input → delta rule applies

  RD-1.4: Phát hiện body-input channels MỚI
    → Bất kỳ channel nào chưa biết
    → Predict: nếu là body-input thật → PHẢI có baseline,
      delta rule, adaptation dynamics, body-feedback response
    → = Framework PREDICT property của channel chưa biết
```

---

## §3 — GAP 2: SIGNAL TRANSDUCTION — "DRIVER LAYER" (Layer 1→3)

### §3.1 Gap lớn nhất mà framework CHƯA NÓI RÕ

```
⭐⭐ ĐÂY LÀ GAP LỚN NHẤT FRAMEWORK CHƯA DOCUMENT RÕ RÀNG.

Framework nói:
  "Light → retina → LGN → V1 → chunks"
  "Danger → amygdala → cortisol → body-feedback"
  "Touch → somatosensory → insula → feeling"

Nhưng ở MỖI mũi tên (→) = TOÀN BỘ molecular biology:
  → Ion channel mở/đóng
  → Action potential truyền dọc axon
  → Neurotransmitter release tại synapse
  → Receptor binding ở neuron nhận
  → Second messenger cascade bên trong neuron
  → Gene expression thay đổi
  → Protein synthesis
  → Synaptic remodeling
  → = MỖI "→" = hàng chục bước molecular

COMPUTER ANALOGY:
  Framework mô tả: "user click → menu hiện"
  Giữa "click" và "menu hiện":
    → USB interrupt → OS kernel → driver decode → event queue
    → Window manager → application event handler → DOM update
    → Layout engine → paint → GPU composite → screen refresh
  = Toàn bộ "driver layer" mà user không thấy, không cần biết.

Body-brain system cũng vậy:
  Framework mô tả: "experience → chunk compile"
  Giữa "experience" và "chunk compile":
    → Receptor activation → ion channel → action potential
    → Thalamic relay → cortical processing → neural ensemble activation
    → LTP (Long-Term Potentiation) → protein synthesis
    → Synaptic tag → consolidation → stabilization
    → = Toàn bộ "driver layer" framework không (và không thể) mô tả.
```

### §3.2 Cụ thể: 6 sub-gaps trong Driver Layer

```
🟡 6 SUB-GAPS CỤ THỂ:

  SG-2.1: RECEPTOR → NEURAL SIGNAL
    Framework biết: "receptor nhận input" (⑤ Tactile: mechanoreceptors)
    Không biết chi tiết: mechanoreceptor nào (Meissner? Pacinian?
      Merkel? Ruffini?) → ion channel nào (Na+? K+? Ca2+?)
      → depolarization pattern nào → action potential frequency nào
    = Neuroscience BIẾT phần lớn (🟢), nhưng framework không mô tả.

  SG-2.2: SIGNAL → THALAMUS → CORTEX routing
    Framework biết: "thalamus = gateway" (Neural-Processing-Flow.md §2)
    Không biết chi tiết: tại nucleus nào (LGN/MGN/VPL/...)?
      → neuron nào nhận? → inhibitory/excitatory balance?
      → TRN gating pattern cụ thể thế nào?
    = Neuroscience BIẾT phần lớn (🟢), framework reference nhưng không drill.

  SG-2.3: CORTICAL PROCESSING → "PATTERN" FORMATION ⭐⭐
    Framework biết: "neurons fire together → wire together" (Hebb 1949)
    Không biết chi tiết: neurons NÀO fire together?
      → Trong 6 cortical layers (Mountcastle), ở layer nào?
      → Gamma binding (Singer) synchronize bằng mechanism nào?
      → Khi nào "pattern" trở thành "chunk"? Ngưỡng ở đâu?
    = Neuroscience ĐANG NGHIÊN CỨU (🟡). Đây là frontier.
    = GAP NÀY NỐI THẲNG VÀO §4 (Chunk Substrate Blackbox).

  SG-2.4: NEUROTRANSMITTER → BEHAVIORAL FUNCTION mapping
    Framework biết behavioral function:
      "Dopamine VTA = salience signal" (🟢 Berridge & Robinson 1998)
      "Cortisol = amplifier" (🟡 Framework reframe)
      "Opioid = body-need match reward" (🟢 partial)
    Không biết chi tiết:
      → Dopamine D1 vs D2 vs D3 vs D4 receptor → khác nhau thế nào?
      → Cortisol → GR (glucocorticoid) vs MR (mineralocorticoid)
        → gene expression cascade → protein nào → neuron behavior đổi thế nào?
      → μ-opioid vs κ-opioid vs δ-opioid → khác nhau thế nào ở behavior level?
    = Pharmacology ĐANG NGHIÊN CỨU chi tiết (🟢🟡). Framework dùng kết quả tổng hợp.

  SG-2.5: SYNAPTIC PLASTICITY → "COMPILE" mechanism ⭐
    Framework biết: "compile qua repetition + emotional peak + multi-modal + sleep"
    Không biết chi tiết:
      → LTP (🟢 Bliss & Lømo 1973): cụ thể NMDA receptor → Ca2+ influx
        → CaMKII → AMPA insertion → spine enlargement
      → Consolidation: hippocampus replay → cortical storage (🟢 Walker 2017)
        → cụ thể replay pattern nào? → cortical storage ở neuron nào?
      → Emotional peak compile: NE + cortisol → amygdala tag
        → cụ thể tag bằng mechanism nào? (🟢 McGaugh 2004: partial)
    = Neuroscience BIẾT từng bước riêng lẻ (🟢).
      NHƯNG: connect toàn chuỗi thành "1 experience → 1 chunk" = CHƯA.

  SG-2.6: SLEEP CONSOLIDATION mechanism chi tiết
    Framework biết: "sleep consolidation = critical" (🟢 Walker 2017)
    Không biết chi tiết:
      → Slow-wave sleep: hippocampal sharp-wave ripples → cortical replay
        → cụ thể replay TOÀN BỘ pattern hay SELECTIVE?
      → REM: emotional memory processing — cụ thể mechanism?
      → Gist extraction: HOW brain "tóm tắt" experience qua ngủ?
      → Mỗi đêm: bao nhiêu chunks? thay đổi bao nhiêu connections?
    = Active research area (🟢🟡). Frontier.
```

### §3.3 Tại sao Driver Layer gap QUAN TRỌNG

```
⭐ DRIVER LAYER = NƠI FRAMEWORK VÀ NEUROSCIENCE GẶP NHAU:

  Framework (behavioral level): "chunk compile" "body-feedback" "feeling"
  Neuroscience (molecular level): LTP, receptor, synapse, gene expression
  Driver Layer = VÙNG GIAO NHAU ở giữa

  Nếu framework đúng:
    → PHẢI có molecular pathway khớp từng claim behavioral
    → Pathway đó = testable, measurable, verifiable
    → = VÙNG CÓ GIÁ TRỊ NGHIÊN CỨU CAO NHẤT

  Nếu framework sai ở behavioral level:
    → Driver layer sẽ cho thấy: molecular evidence KHÔNG match prediction
    → = Framework cần sửa hoặc bỏ claim đó

  VÍ DỤ CỤ THỂ:
    Framework claim: "Cortisol = amplifier, KHÔNG phải stress hormone"
    → Driver layer test: cortisol ở moderate level + novel context
      → cortical activation pattern thế nào? = match "amplifier"?
      → hay match "stress response" (HPA → fight/flight only)?
    → Nếu match amplifier → framework validated ở molecular level
    → Nếu match stress only → framework claim cần refine

⚠️ HIỆN TẠI:
   Framework CHƯA nói rõ gap này là gap.
   Neural-Processing-Flow.md mô tả PATHWAY (hardware flow) —
   nhưng chưa explicitly nói: "giữa pathway và chunk = TOÀN BỘ
   molecular biology mà framework không mô tả."
   File này fill gap đó.
```

### §3.4 Research direction

```
HƯỚNG NGHIÊN CỨU TỪ GAP 2:

  RD-2.1: "Experience → Chunk" pathway tracing
    → Specific experience (e.g., learning a new face)
    → Trace: retina → V1 → FFA → hippocampus → consolidation
    → Measure: từ LTP đến behavioral recognition = bao lâu, bao nhiêu synapse?
    → Method: fMRI + EEG + computational modeling
    → Framework predict: compile NHANH nếu multi-modal + emotional peak

  RD-2.2: Cortisol "amplifier" molecular verification
    → Cortisol + novel context → measure cortical excitability
    → Cortisol + threat context → measure cùng cortical regions
    → Framework predict: CÙNG molecular effect (amplify),
      KHÁC direction (approach vs avoidance — determined by chunks, not cortisol)
    → Method: cortisol administration + context manipulation + fMRI

  RD-2.3: Delta rule at molecular level
    → Repeated exposure to same stimulus → measure receptor sensitivity change
    → Framework predict: receptor downregulation = "baseline shift UP" (§3.3 Core-Software)
    → Partially known (🟢 tolerance, habituation) — but connecting to
      framework's delta rule at unified mechanism level = novel

  RD-2.4: Sleep "gist extraction" mechanism
    → Record hippocampal replay during SWS → compare with experience
    → Framework predict: replay selectively strengthens PATTERN-relevant connections
      (not all connections equally) — "gist" = proto-chunk
    → Method: hippocampal recording (animal) + fMRI sleep (human)

  RD-2.5: Compile TYPE A/B/C at molecular level
    → Type A (direct short): LTP + opioid = simple, fast
    → Type B (expertise): LTP + repetition + meta-chunk formation
    → Type C (trust install): social signal → trust gate → compile
    → Framework predict: 3 types = DIFFERENT molecular signatures
    → Method: social learning paradigm + pharmacological manipulation
```

---

## §4 — GAP 3: CHUNK SUBSTRATE — FUNDAMENTAL BLACKBOX (Layer 3)

### §4.1 Blackbox duy nhất mang tính nền tảng

```
⭐⭐⭐ ĐÂY LÀ BLACKBOX CƠ BẢN NHẤT CỦA FRAMEWORK.

  Framework dùng "chunk" làm đơn vị cơ bản.
  Mọi thứ từ feeling, schema, logic, connection đều build trên chunks.

  Framework mô tả chunk ở level BEHAVIORAL:
    → Compile qua repetition + emotional peak + multi-modal + sleep
    → Fire theo probability-weighted spreading activation
    → Link: Type 1-3 auto + Type 4 PFC deliberate
    → Proto-chunk → Compiled → Meta-chunk (gradient, không binary)
    → Never delete — only probability shift

  Framework KHÔNG BIẾT chunk ở level BIOLOGICAL:
    → Chunk tương ứng với cấu trúc neural NÀO?
      (cell assembly? neural ensemble? engram? distributed pattern?)
    → Lưu trữ ở vùng não NÀO? Phân bổ ra sao?
      (hippocampal index? cortical storage? distributed?)
    → Fire theo cơ chế vật lý NÀO?
      (synchronous firing? oscillation coupling? phase-locking?)
    → Compile cụ thể thành CÁI GÌ ở level synapse?
      (Hebbian assembly? synaptic tag-and-capture? structural change?)

  Framework chỉ quan sát chunk ở level hành vi
  (người ta làm gì, cảm thấy gì, phản ứng thế nào)
  — KHÔNG phải level tế bào.
```

### §4.2 D1 Convergence — BB1 + BB2 = Cùng 1 mechanism

```
⭐ PHÁT HIỆN (Drill §26 D1 — Framework-Boundaries.md v2.0):

  Trước (v1.0): framework gọi "2 blackbox":
    BB1 = Chunk substrate (brain biology unknown)
    BB2 = Valence complexity (complex chains unpredictable)

  Drill phát hiện: KHÔNG PHẢI 2 mechanism riêng biệt.

  Ở Cấp 1 (individual brain):
    COMPILE = wire neurons together (structural aspect)
    VALENCE = tag neurons with body-base impact (evaluative aspect)
    = ĐỒNG THỜI, 1 process — KHÔNG TÁCH ĐƯỢC
    → BB1 + BB2 ở Cấp 1 = CÙNG mechanism

  "Valence phức tạp" (BB2 cũ) = TẠI SAO?
    Vì chunk substrate (BB1) hoạt động ở SCALE lớn hơn:
    → Chain DÀI + distributed + nhiều links + trust × nhiều nguồn
    → = BB2 "complexity" PHẦN LỚN nằm ở Cấp 2 (collective), KHÔNG phải Cấp 1

  REFRAME:
    BB1 (chunk substrate)    = 1 FUNDAMENTAL BLACKBOX (giữ nguyên)
    BB2 (valence complexity) = BB1 + scale + variance (→ §7 Complexity Dimensions)
```

### §4.3 Neuroscience candidates cho "chunk"

```
🟢🟡 Neuroscience có NHIỀU candidates — chưa ai CHỐT:

  ① Cell Assembly (Hebb 1949)
     → Nhóm neurons fire đồng bộ = 1 unit
     → 🟢 Foundational concept. Gần nhất với "chunk."
     → Limitation: chưa measure được 1 assembly cụ thể end-to-end

  ② Neural Ensemble / Population Coding
     → Pattern activation DISTRIBUTED across many neurons
     → 🟢 Established (Georgopoulos 1986 — population vector in motor cortex)
     → Consistent: chunk = distributed pattern, not localized

  ③ Engram (Josselyn & Tonegawa 2020)
     → Physical trace of memory in specific neurons
     → 🟢 Nobel Prize work — engram cells identified in mice
     → Most promising: engram ≈ chunk at cellular level?
     → Limitation: mice, short-term, simple memory — human complex chunks?

  ④ Oscillatory Coupling (Buzsáki 2006)
     → Theta-gamma coupling cho working memory
     → Gamma oscillation cho binding (Singer)
     → 🟢 Established in animal models
     → Possibly HOW chunks fire, not WHAT chunks are

  ⑤ Synaptic Tag-and-Capture (Frey & Morris 1997)
     → Weak stimulus creates tag, strong stimulus creates protein
     → Tag captures protein → consolidated memory
     → 🟢 Established mechanism
     → Possibly HOW compile works at single-synapse level

  ⭐ FRAMEWORK POSITION:
    Framework KHÔNG commit cho candidate nào.
    "Chunk" = behavioral unit. Biological implementation = unknown.
    Neuroscience tương lai sẽ giải mã blackbox này.
    Khi đó framework sẽ được kiểm chứng rõ ràng hơn
    — hoặc bị bác bỏ nếu substrate thực tế không khớp.
    Cả hai kết quả đều có giá trị.
```

### §4.4 Research direction

```
HƯỚNG NGHIÊN CỨU TỪ GAP 3:

  RD-3.1: "Chunk" = engram?
    → Framework predict: chunk = multi-modal engram
      (không chỉ 1 vùng não, mà distributed across cortical areas)
    → Method: engram labeling (optogenetics + TRAP) cho complex experience
    → Test: reactivate engram → behavior returns?

  RD-3.2: Chunk "strength" at neural level
    → Framework: chunk strength = gradient (proto → compiled → meta)
    → Predict: stronger chunk = more synapses? more neurons? denser connections?
    → Method: longitudinal imaging của skill acquisition → synaptic changes

  RD-3.3: "Never delete, only probability shift"
    → Framework claim: chunks không bao giờ xóa, chỉ probability giảm
    → Predict: "quên" = retrieval failure, not structural deletion
    → Consistent with reconsolidation (🟢 Nader 2000) nhưng chưa chứng minh UNIVERSAL
    → Method: very old memories + strong cue → reactivation possible?

  RD-3.4: Meta-chunk at neural level
    → Framework: meta-chunk = chunk OF chunks
    → Predict: expert meta-chunk = hierarchical neural pattern
      (lower-level patterns activate → higher-level pattern emerges)
    → Method: expert vs novice fMRI during domain-specific task
    → Partially tested (🟢 Chase & Simon 1973 chess) — neural level untested
```

---

## §5 — GAP 4: INTEGRATION → FEELING → CONSCIOUSNESS (Layer 3→4)

### §5.1 Hiện trạng

```
Framework mô tả feeling qua 7-layer fidelity gradient
(Feeling.md v2.1, Core-Software.md §5):

  L1: Raw body signals              ~100% fidelity
  L2: Integration (insula)          ~95%
  L3: Consciousification            ~90%
  L4: Observation (PFC threshold)   ~85%
  L5: Location                      70-90%
  L6: Labeling                      40-80%  ← CRITICAL LOSS
  L7: Explanation                   20-70%  ← MOST RISKY

  (🟡 % = calibration anchor, không đo chính xác — Core-Software.md §12.4)

Framework biết:
  → Anterior insula = hub tích hợp interoceptive signals (🟢 Craig 2002, 2009)
  → ACC = conflict detection (🟢 Botvinick 2004)
  → vmPFC = somatic marker, emotion regulation (🟢 Damasio 1994)
  → PFC observe KẾT QUẢ compiled, không raw data
  → Body process TRƯỚC → PFC LUÔN biết SAU
  → Temporal order KHÔNG BAO GIỜ đảo ngược (🟢 Libet 1983)
```

### §5.2 Gap: HOW integration → conscious feeling

```
⚠️ FRAMEWORK MÔ TẢ PATTERN, KHÔNG MÔ TẢ MECHANISM:

  SUB-GAP 1: Integration — HOW?
    Framework: "body signals integrate at insula"
    Missing: insula NHẬN signals từ vagus, spinal, hormonal...
      → HOW chúng được MERGE thành 1 unified state?
      → Cơ chế integrate = gì? Summation? Weighted average?
        Phase-locking? Predictive coding?
    → Predictive interoception (🟢 Seth 2013, Barrett 2017)
      = best candidate — brain PREDICTS body state, COMPARES actual
      → prediction error = body-feedback signal
    → NHƯNG: chi tiết computational model = still active research

  SUB-GAP 2: "Consciousification" — HOW?
    Framework: L2→L3 = "trở thành conscious"
    Missing: CHÍNH XÁC thế nào neural activity TRỞ THÀNH
      subjective experience?
    → = HARD PROBLEM OF CONSCIOUSNESS (Chalmers 1995)
    → Framework EXPLICITLY out of scope (Core-Software.md §12.2)
    → Framework mô tả: khi nào, ở đâu, pattern gì — KHÔNG mô tả: tại sao có qualia

  SUB-GAP 3: PFC "observe" — HOW?
    Framework: "PFC observe chunk activations + body signals"
    Missing: PFC NHẬN input từ B+C zones qua axonal connections
      → nhưng HOW "nhận" = "observe"?
      → PFC mixed selectivity (🟢 Rigotti 2013) = encoding complex info
      → NHƯNG: mixed selectivity = mechanism, chưa giải thích "observation"

  ⭐ FRAMEWORK POSITION:
    Feeling.md mô tả PATTERN rõ ràng — trainable, useful.
    HOW integration happens at circuit level = open question.
    Consciousness = explicitly out of scope.
    Framework hữu ích MÀ KHÔNG CẦN giải hard problem —
    giống engineer dùng electricity MÀ KHÔNG CẦN giải quantum mechanics.
```

### §5.3 Research direction

```
HƯỚNG NGHIÊN CỨU TỪ GAP 4:

  RD-4.1: Interoceptive predictive coding verification
    → Framework compatible with Seth 2013 predictive interoception
    → Predict: body-feedback = interoceptive prediction error
    → Method: induce predictable vs unpredictable body state changes
      → measure insula prediction error signal
    → Partially tested (🟢) — connecting to framework's delta rule = novel

  RD-4.2: 7-layer fidelity at neural level
    → Framework: fidelity GIẢM DẦN từ body → PFC
    → Predict: information loss measurable at each neural relay
    → Method: compare body signal (peripheral nerve recording)
      vs insula activation vs PFC activation
    → = Quantify fidelity gradient TRỰC TIẾP

  RD-4.3: L6 Labeling loss mechanism
    → Framework: labeling = CRITICAL loss point (40-80%)
    → Predict: forcing verbal label CHANGES neural activation pattern
      (not just describes it — label ALTERS the experience)
    → Consistent with linguistic relativity (🟢 Lupyan 2012)
    → Method: same stimulus, different label conditions, measure neural change
```

---

## §6 — GAP 5: HORMONE COMBINATORICS (Cross-cutting)

### §6.1 Hiện trạng

```
Framework mô tả từng hormone ở BEHAVIORAL level:

  Cortisol:  amplifier, 7 modes, direction > level
             (Cortisol-Baseline.md v2.0, 15 sections)
  Dopamine:  VTA salience signal, KHÔNG phải reward
             (Dopamine-Reward-Rejection.md, 7 bằng chứng)
  Opioid:    body-need match reward, H10 5 preconditions
             (03-Reward.md, Reward-Signal-Architecture.md)
  Oxytocin:  bonding-related, OXTR sensitivity varies
             (Core-Hardware.md §5)
  Serotonin: stability-related, MAO-A gene
             (Core-Hardware.md §5, OCD-Analysis.md §4.5)
  NE:        alertness, α1 → PFC offline under threat
             (Cortisol-Baseline.md §9.1)

Mỗi hormone = 1 file hoặc section riêng. Evidence tốt (🟢🟡).
```

### §6.2 Gap: combinatorial interaction

```
⚠️⚠️ FRAMEWORK MÔ TẢ TỪNG HORMONE RIÊNG. TƯƠNG TÁC ĐỒNG THỜI = KHÔNG.

THỰC TẾ:
  Body chạy HÀNG CHỤC hormone CÙNG LÚC, LIÊN TỤC:
    → Cortisol + Testosterone + Estrogen + Progesterone
    → + Serotonin + Dopamine + NE + Oxytocin + Vasopressin
    → + Insulin + Leptin + Ghrelin + Thyroid (T3/T4)
    → + Melatonin + Endorphins + GABA + Glutamate
    → + Cytokines (immune) + Prostaglandins + ...

  Mỗi hormone INFLUENCE hormone khác:
    → Cortisol ↔ Serotonin (cortisol suppress serotonin synthesis)
    → Cortisol ↔ Testosterone (chronic cortisol suppress testosterone)
    → Estrogen ↔ Serotonin (estrogen increase serotonin receptor sensitivity)
    → Oxytocin ↔ Cortisol (oxytocin buffer cortisol response)
    → Dopamine ↔ Serotonin (oppose in some circuits, cooperate in others)
    → ...

  = COMBINATORIAL EXPLOSION.
  N hormone × M interactions × T timepoints = gần như VÔ TẬN combinations.

PHARMACOLOGY HIỆN TẠI:
  → Nghiên cứu 1-2 hormone cùng lúc = feasible
  → Nghiên cứu 3+ hormone interaction = rất khó
  → Nghiên cứu TOÀN BỘ hormone system cùng lúc = chưa thể
  → Side effects thuốc = partly vì combinatorial interaction chưa predict được

FRAMEWORK GAP:
  Framework nói: "cortisol + NE threat → PFC offline"
  Framework KHÔNG nói: "cortisol + NE + LOW serotonin + HIGH estrogen
    + MODERATE testosterone + insulin resistance → thì SAO?"
  = Framework mô tả TỪNG CÁI. KHÔNG mô tả TỔ HỢP.
```

### §6.3 Tại sao gap này IRREDUCIBLE (ở mức hiện tại)

```
Đây KHÔNG phải lỗi framework. Đây là giới hạn của TOÀN BỘ DOMAIN:

  ① Pharmacology cũng chưa predict combinatorial effects
     → Polypharmacy (nhiều thuốc) = một trong những thách thức lớn nhất
     → Drug-drug interaction databases = có, nhưng incomplete

  ② Hormone system = nonlinear dynamic system
     → Small change ở 1 hormone → cascade effects qua nhiều hormone
     → Sensitive to initial conditions (giống chaos theory)
     → Individual variation (gene + receptor + history) nhân lên

  ③ Framework acknowledge (Framework-Boundaries.md v2.0):
     "Hormone thay đổi liên tục (cortisol, estrogen, thyroid,...)
      — mỗi cái bias valence theo 1 hướng, và chúng tương tác
      với nhau theo cách tôi chưa nắm được"
     = Hardware Variance complexity dimension

  ⭐ FRAMEWORK POSITION:
    Framework mô tả CHỨC NĂNG từng hormone (useful, testable).
    Combinatorial interaction = beyond framework scope.
    Cá nhân nào muốn predict chính xác body state tại 1 thời điểm
    → cần measurement (hormone panel, HRV, cortisol test,...).
    Framework cung cấp MAP để INTERPRET measurement — không thay thế measurement.
```

### §6.4 Research direction

```
HƯỚNG NGHIÊN CỨU TỪ GAP 5:

  RD-5.1: Hormone interaction profiles
    → Framework predict: cortisol AMPLIFY bất kỳ hướng nào
    → Test: cortisol + oxytocin → amplify bonding?
      cortisol + testosterone → amplify status competition?
    → Method: hormone administration + behavioral measurement
    → Partially tested (🟢 scattered) — unified under "amplifier" = novel

  RD-5.2: Individual hormone "configuration" mapping
    → Framework: "mỗi người = 1 configuration RIÊNG" (Core-Hardware.md §6)
    → Predict: individual hormone baseline profile → predict behavioral tendencies
    → Method: multi-hormone panel + extensive behavioral testing
    → Long-term: personalized "hardware profile" ← feasible with future tech

  RD-5.3: Menstrual cycle as natural hormone combinatorics experiment
    → Estrogen + progesterone cycle = NATURAL variation in hormone combo
    → Framework predict: cycle phase → change body-feedback sensitivity
      → change chunk activation patterns → change observation parameters
    → Method: longitudinal cycle tracking + behavior + neural measurement
    → Some evidence (🟢 menstrual cycle mood/cognition studies)
    → Connecting to framework mechanism = novel

  RD-5.4: Computational hormone interaction model
    → Model N hormones + known interactions + individual variation
    → Framework provides: BEHAVIORAL prediction for each hormone
    → Pharmacology provides: MOLECULAR interaction data
    → Combine → predict combinatorial effects → test
    → = Bridge giữa framework (behavioral) và pharmacology (molecular)
```

---

## §7 — COMPLEXITY DIMENSIONS (Scale + Hardware Variance)

```
Ngoài 5 Gaps ở §2-§6, framework có 2 complexity dimensions
ảnh hưởng KHẢ NĂNG PREDICT:

  (Nội dung tích hợp từ Framework-Boundaries.md v2.0.
   Không phải gaps trong knowledge — mà là giới hạn inherent.)
```

### §7.1 Scale: Individual → Collective

```
Chain valence ngắn ở Cấp 1 (cá nhân) → dễ quan sát:
  → Thấy bạn → vui → approach
  → Gai → đau → rút tay

Chain valence DÀI sống ở Cấp 2 (collective):
  → [học → điểm → đại học → việc → lương → body-base]
  → Mỗi link = 1 trust connection. Nhiều link = nhiều nguồn sai số.
  → Collective infrastructure hold chain → cá nhân chỉ compile short.

Framework mô tả được PATTERN ở Cấp 2 (Collective-Body.md §1-§3),
nhưng KHÔNG predict được instance cụ thể — vì quá nhiều biến
tương tác ở mỗi link trong chain.

Giống dự báo thời tiết: biết cơ chế nhưng vẫn không predict
thời tiết 30 ngày — vì quá nhiều biến tương tác cùng lúc.
```

### §7.2 Hardware Variance

```
Cùng sự kiện, khác người, kết quả khác hoàn toàn:

  → Trauma compiled từ nhỏ — chính người đó còn không verbalize được,
    thì không thể biết chunk nào đang fire

  → Hormone thay đổi liên tục (→ §6 Hormone Combinatorics)
    — mỗi cái bias valence theo 1 hướng, tương tác phức tạp

  → Hardware (gene, receptor variants) tạo ra hàng ngàn phiên bản
    tinh tế — cùng sự kiện, khác người, valence chain khác hoàn toàn

Hardware variance = IRREDUCIBLE — không phải vấn đề công cụ hay trình độ.
Mỗi người = 1 configuration RIÊNG. Framework mô tả CƠ CHẾ chung,
KHÔNG thể mô tả PHIÊN BẢN cụ thể của mỗi người.
```

### §7.3 Hệ quả

```
5 Gaps (§2-§6) + 2 Complexity Dimensions (§7.1-§7.2) có nghĩa:

  Framework mô tả được PATTERN (xu hướng chung, cơ chế phổ biến)
  nhưng KHÔNG predict được INSTANCE cụ thể
  (người NÀY, lúc NÀY, sẽ cảm thấy GÌ, làm GÌ).

  Nếu ai dùng framework để claim "tôi biết chính xác bạn đang nghĩ gì"
  — đó là overclaim, không phải điều framework nói.

  Framework giống la bàn — cho thấy hướng, không dẫn đường cụ thể.
  Hữu ích để định hướng, nhưng không thay thế
  việc tự đi và tự cảm nhận.
```

---

## §8 — FRAMEWORK AS RESEARCH ROADMAP

### §8.1 Tổng hợp: 5 Gaps × Research Directions

```
⭐ MỖI GAP = TẬP RESEARCH QUESTIONS CÓ THỂ TEST:

  ┌─────┬──────────────────────────────┬──────────┬────────────────────┐
  │ Gap │ Vấn đề                       │ Severity │ Research Directions │
  ├─────┼──────────────────────────────┼──────────┼────────────────────┤
  │  1  │ Body-Input completeness       │ 🟡 Low   │ RD-1.1 → RD-1.4   │
  │  2  │ Signal Transduction (Driver)  │ 🔴 High  │ RD-2.1 → RD-2.5   │
  │  3  │ Chunk Substrate (Blackbox)    │ 🔴 High  │ RD-3.1 → RD-3.4   │
  │  4  │ Integration → Consciousness   │ 🟡 Med   │ RD-4.1 → RD-4.3   │
  │  5  │ Hormone Combinatorics         │ 🟡 Med   │ RD-5.1 → RD-5.4   │
  └─────┴──────────────────────────────┴──────────┴────────────────────┘

  Tổng: 20 research directions cụ thể.
  Mỗi direction có: predict, method, test criteria.
```

### §8.2 Framework predictions = testable hypotheses

```
NẾU FRAMEWORK ĐÚNG, neuroscience PHẢI TÌM THẤY:

  ① Chunk = measurable biological unit (engram? assembly? distributed pattern?)
     mà behavioral properties MATCH framework description
     (strength gradient, multi-modal, never delete, compile conditions)

  ② Cortisol ở moderate level = amplifier CHO CẢ approach VÀ avoidance
     (không chỉ stress response)

  ③ Dopamine VTA signal = salience (TRƯỚC evaluation)
     Opioid = reward (SAU body-need match)
     = 2 SEPARATE signals, NOT 1 "reward" signal

  ④ Body-feedback delta rule = universal mechanism
     áp dụng cho BẤT KỲ body-input (kể cả chưa biết)
     = baseline + deviation → reward/dissonance

  ⑤ PFC reach gradient (A→B strong, A→C variable, A→D weak)
     = measurable qua connectivity strength

  ⑥ 7-layer fidelity: information loss measurable
     at each neural relay từ body → PFC

  ⑦ Compile Type A/B/C = KHÁC nhau ở molecular level
     (different LTP patterns, different neuromodulators)

  ⑧ Mỗi body-input channel mới phát hiện
     PHẢI có baseline, adaptation, delta rule properties

Nếu bất kỳ prediction nào SAI → framework cần sửa hoặc bỏ claim đó.
CẢ HAI kết quả (confirm hoặc reject) đều có giá trị.
```

### §8.3 Researcher mapping: chuyên môn nào → gap nào

```
RESEARCHER CÓ THỂ CHỌN GAP PHÙ HỢP CHUYÊN MÔN:

  Molecular neuroscientist     → Gap 2 (Driver Layer), Gap 3 (Chunk)
  Electrophysiologist          → Gap 3 (neural ensemble), Gap 4 (binding)
  Endocrinologist              → Gap 5 (Hormone Combinatorics)
  Sensory physiologist         → Gap 1 (Body-Input new channels)
  Pharmacologist               → Gap 2 (SG-2.4), Gap 5 (drug interactions)
  Computational neuroscientist → Gap 4 (predictive coding), Gap 5 (modeling)
  Sleep researcher             → Gap 2 (SG-2.6 consolidation)
  Psychophysicist              → Gap 4 (fidelity gradient measurement)
  Clinical psychologist        → All gaps at behavioral verification level
  AI/ML researcher             → Gap 3 (computational chunk model)

  Framework cung cấp BEHAVIORAL PREDICTIONS (§8.2).
  Researcher cung cấp BIOLOGICAL VERIFICATION.
  = Complement, không replace.
```

---

## §9 — AI AS DYNAMIC DRILL TOOL

```
File này liệt kê VẤN ĐỀ — không liệt kê TẤT CẢ CHI TIẾT.
Chi tiết ở mỗi gap = vô tận (đặc biệt Gap 1 body-inputs, Gap 2 pathways).

AI có thể phục vụ như DYNAMIC DRILL TOOL:

  ① User hỏi: "Retina cụ thể gồm những gì?"
     → AI: rods (~120M), cones (~6M, 3 types: S/M/L),
       ganglion cells (~20+ types), ipRGC, Müller glia,...
     → Drill sâu tới level tế bào, phân tử nếu cần

  ② User hỏi: "Cortisol gắn vào receptor nào?"
     → AI: GR (glucocorticoid receptor, NR3C1) widespread
       + MR (mineralocorticoid receptor, NR3C2) hippocampus + amygdala
     → GR: low affinity → respond khi cortisol CAO
     → MR: high affinity → respond khi cortisol THẤP/BÌNH THƯỜNG
     → = MR tonic, GR phasic — giải thích 7 modes (Cortisol-Baseline.md)

  ③ User hỏi: "Có body-input nào từ từ trường không?"
     → AI: cryptochrome (CRY1, CRY2) in retina,
       Wang et al. 2019 Caltech fMRI study,
       evidence trong birds (magnetite + cryptochrome dual mechanism),
       human = open question

  ④ User hỏi: "LTP cụ thể diễn ra thế nào?"
     → AI: glutamate → NMDA receptor (voltage-dependent, Mg2+ block)
       → depolarization releases Mg2+ → Ca2+ influx
       → CaMKII activation → AMPA receptor insertion
       → spine enlargement → LTP early phase (1-3h)
       → protein synthesis (CREB, BDNF) → LTP late phase (>3h)
       → synaptic tag-and-capture for consolidation

  = File Blackbox-Map KHÔNG CẦN chứa tất cả chi tiết này.
  = File Blackbox-Map chỉ cần MAP đúng chỗ nào là gap.
  = AI fill chi tiết ON DEMAND — theo chuyên môn + câu hỏi cụ thể của user.

  ⚠️ AI cũng có giới hạn:
     → AI knowledge = training data (có cutoff date)
     → Neuroscience frontier = đang thay đổi liên tục
     → AI có thể sai ở chi tiết molecular → user verify bằng paper gốc
     → Framework position: AI = tool, user body = final arbiter
```

---

## §10 — CROSS-REFERENCES

```
WITHIN FILE — 5 GAPS:
  §2 Gap 1 (Body-Input)       → Core-Hardware.md §4, Core-Software.md §3.2
  §3 Gap 2 (Driver Layer)     → Neural-Processing-Flow.md, Cortisol-Baseline.md
  §4 Gap 3 (Chunk Substrate)  → Chunk.md §12, Body-Base.md §10
  §5 Gap 4 (Integration)      → Feeling.md v2.1, Feeling-Mechanism-Deep.md
  §6 Gap 5 (Hormone)          → Cortisol-Baseline.md, PFC-Hardware.md

COMPLEXITY DIMENSIONS:
  §7.1 Scale     → Collective-Body.md §1-§3, Valence-Propagation.md §4-§5b
  §7.2 Variance  → PFC-Hardware.md, Feeling-Accuracy.md

SUPERSEDED:
  Research/Meta-Impact/Framework-Boundaries.md v2.0 → backup/
    §4.1-§4.2 ← Blackbox + D1 Convergence (tích hợp nguyên)
    §7.1-§7.2 ← Complexity Dimensions (tích hợp nguyên)

RELATED META-ANALYSIS:
  Creator-Lens.md             → creator bias analysis
  Epistemological-Position.md → framework vs conventional science positioning
  Core-Software.md §12        → honest assessment + scope limits + open questions

REFERENCING THIS FILE:
  (Cần update sau khi file hoàn thành)
  → Chunk.md §12, Body-Base.md §10, Core-Software.md §12
  → Ask-AI.md (AI protocol)
```

---

## Closing note

```
Blackbox-Map v1.0 — 5 Gaps + 2 Complexity Dimensions.

Framework mô tả body-brain system ở level behavioral.
Giữa behavior và neuron vật lý = 5 gaps rõ ràng.
Mỗi gap = vùng chưa biết + hướng nghiên cứu cụ thể.

Gaps KHÔNG phải yếu điểm — là ranh giới giữa 2 domains:
  Framework (behavioral)     ↔     Neuroscience (biological)
  pattern description        ↔     mechanism implementation
  observable, accessible     ↔     measurable, verifiable

20 research directions. 8 testable predictions. Open for anyone.

Nếu framework đúng → đây là FRONTIER MAP cho next steps.
Nếu framework sai → đây là nơi sẽ phát hiện ra.
Cả hai → tiến bộ.
```

---

> *Blackbox-Map v1.0 — "5 Gaps giữa behavioral framework và biological reality.
> Gap 1: Body-Input completeness (17 categories, có thể chưa đầy đủ).
> Gap 2: Signal Transduction = 'Driver Layer' lớn nhất (Layer 1→3, molecular biology).
> Gap 3: Chunk Substrate = fundamental blackbox (behavioral ↔ neural).
> Gap 4: Integration → Feeling → Consciousness (pattern described, mechanism open).
> Gap 5: Hormone Combinatorics (individual mô tả được, tổ hợp = vô tận).
> + 2 Complexity Dimensions (Scale + Hardware Variance).
> 20 research directions. AI = dynamic drill tool.
> Framework = la bàn — cho thấy hướng, không dẫn đường cụ thể."*
