# Core-Software — Cycle-Based Architecture (Software Map)

> **Trạng thái:** v1.0 — 1 trong 3 bản đồ Core v7.8
> **Ngày:** 2026-05-10
> **Bản đồ này:** SOFTWARE MAP — CHẠY THẾ NÀO (mechanism chi tiết nhất)
> **2 bản đồ khác:** Core-Hardware.md (CÁI GÌ ở ĐÂU) | Core-Interface.md (QUAN SÁT + TƯƠNG TÁC)
> **Supersedes:** Core-v7.8-Draft.md v0.2 (2026-04-19, tách thành 3 file)
> **Nguyên tắc:**
> - Cycle-based: Domain → Body-Input → Unconscious → Feeling → PFC → Body-Output → Domain
> - Chunk-System = sole substrate (mọi thứ chạy trên chunks)
> - Body-Feedback chỉ có 2 hướng: REWARD hoặc DISSONANCE
> - PFC = observer + indirect orchestrator (hold chunks, bias direction)
> - Schema, Drives, Valence = observation parameters, không phải components
> - Development = chunk density tăng dần (cùng architecture, khác chunks)
> **Tiền đề đọc:**
> - Chunk.md v2.1 — chunk substrate, trust gate, pattern hierarchy
> - Body-Feedback.md — dual-pull, H10, 3 nguồn
> - Feeling.md v2.1 — PFC observation interface, 7-layer
> - Agent-Mechanism.md v1.0 — agent = function on chunks, SPM + PR
> - Empathy.md v2.0 — SPM applied to others, 2-luồng, burnout
> - Valence-Propagation.md v1.4 — body evaluation + chain + VP §4 clarification
> - Cortisol-Baseline.md v2.0 — amplifier, not stress
> - Body-Base.md v2.0 — Model 3+1, 4-tier calibration, circuit breaker
> - Compile-Taxonomy.md v1.1 — 3 Loại A/B/C, 4 pathways, 6 trade-offs
> - Collective-Body.md v1.1 — Model 3 cấp, trust = only bridge, AI era
> - Reward-Signal-Architecture.md v1.0 — Type A/B, 5 Profiles, Interaction Model
> - PFC-Configuration.md v1.0 — 6 dynamic modes, survival matrix
> **Confidence:** 🟢 Research support | 🟡 Framework synthesis | 🔴 Hypothesis
> **Numbers (🟡):** `~X%` = calibration anchor — hướng + cỡ, KHÔNG phải đo lường.
>   `X-Y%` = range minh họa (biến thiên lớn). Insight nằm ở HƯỚNG + TƯƠNG QUAN,
>   không ở con số cụ thể. Mỗi người, mỗi context → số thực tế khác.
>   🟢 numbers (có citation) = research-backed. Chi tiết: §12.4.
> **Language:** Tiếng Việt primary + English technical terms

---

## Mục lục

- §0 — BA BẢN ĐỒ + TẠI SAO CYCLE-BASED
- §1 — KIẾN TRÚC CYCLE: SOFTWARE MAP
- §2 — DOMAIN
- §3 — BODY-INPUT (L0 + L1)
- §4 — UNCONSCIOUS PROCESSING
- §5 — FEELING (Bridge)
- §6 — PFC (Observer + Orchestrator)
- §7 — BODY-OUTPUT
- §8 — OBSERVATION PARAMETERS
- §9 — DEVELOPMENT TRAJECTORY
- §10 — MULTIPLE TIMESCALES
- §11 — KEY REFRAMES TỪ V7.5
- §12 — HONEST ASSESSMENT
- §13 — CROSS-REFERENCES

---

## §0 — BA BẢN ĐỒ + TẠI SAO CYCLE-BASED

### §0.1 Ba bản đồ Core v7.8

Framework mô tả body-brain system từ 3 góc nhìn, mỗi góc = 1 bản đồ:

| # | Bản đồ | Góc nhìn | Đối tượng | File |
|---|---|---|---|---|
| 1 | Hardware Map | CÁI GÌ ở ĐÂU | Neuroscience researcher | Core-Hardware.md |
| 2 | **Software Map** | **CHẠY THẾ NÀO** | **Framework researcher** | **File này** |
| 3 | Interface Map | QUAN SÁT + TƯƠNG TÁC | Mọi người | Core-Interface.md |

3 bản đồ mô tả CÙNG hệ thống. Khác góc nhìn. Đọc độc lập được.
Giống máy tính: sơ đồ mạch / code architecture / user guide.

### §0.2 Tại sao v7.8 cycle-based

Core-v7.5-Draft.md (2026-03) tổ chức: 4 layers + 3 drives + Schema System.
Scaffolding đó cho phép drill 63,000+ dòng phân tích (44+ files, 13 mechanism files).

Sau khi drill: 13/13 files compatible — layers/drives/schemas = observation labels,
không phải architecture. Cycle-based match cách body-brain thực sự hoạt động.

| V7.5 | V7.8 | Lý do |
|---|---|---|
| 4 layers (L0-L3) | L0 circuit breaker + L1 inputs | L2 removed, L3 collapsed |
| 3 drives | Observation parameters | Drives = emergent, không phải operators |
| Schema System | Chunk-System (sole substrate) | Schema = observation label |
| Layer priority | Signal strength | Loudest wins, not highest layer |
| Cross-cutting | Properties of cycle | Cortisol = amplifier, Empathy = function |
| Feeling (implicit) | Explicit bridge | PFC observation interface |

### §0.3 Nguyên tắc thiết kế

1. **Follow mechanism, not organization**: kiến trúc match cách body-brain thực sự hoạt động
2. **Chunk-centric**: chunks = sole substrate, mọi thứ khác = function hoặc property
3. **Cycle, not layers**: perception-action loop liên tục
4. **Observation parameters, not components**: Schema, Drives, Valence = cách quan sát
5. **Development = chunk density**: cùng architecture, khác chunks tích lũy
6. **Honest about limits**: descriptive architecture + hypothesis generator, không phải clinical protocol

---

## §1 — KIẾN TRÚC CYCLE: SOFTWARE MAP

### §1.1 Ba góc nhìn — cùng hệ thống

```
🟡 CÙNG HỆ THỐNG — BA GÓC NHÌN:

  Giống quan sát một con robot:

  HARDWARE MAP (Core-Hardware.md):
    → Mở robot ra → thấy CPU, sensors, motors, dây dẫn, pin
    → "CÁI GÌ ở ĐÂU, nối với gì, specs cá nhân"
    → Cho chuyên gia thần kinh, muốn verify từng vùng não

  SOFTWARE MAP (file này):
    → Nhìn robot hoạt động → input → process → decide → act → feedback
    → "CÁI GÌ CHẠY thế nào, flow ra sao, mechanism chi tiết"
    → Cho researcher muốn hiểu WHY hệ thống hoạt động

  INTERFACE MAP (Core-Interface.md):
    → Dùng robot → bấm nút, xem màn hình, nhận kết quả
    → "QUAN SÁT cái gì, TƯƠNG TÁC thế nào"
    → Cho mọi người, không cần biết mechanism

  Cả ba bản đồ mô tả CÙNG body-brain system.
  Hardware: 4 zones A/B/C/D. Software: 7-step cycle ①→⑦.
  Interface: observable patterns + interaction principles.
  Mapping Hardware ↔ Software → §1.3.
```

### §1.2 Software Map — Functional Cycle

```
🟡 BẢN ĐỒ CHỨC NĂNG — "CÁI GÌ CHẠY THẾ NÀO, FLOW RA SAO":

  PFC ở trên cùng — điểm quan sát của mỗi người.
  Domain ở dưới cùng — nguồn stimuli.
  Perception ↑ đi lên. Action ↓ đi xuống.

  ┌────────────────────────────────────────────────────────────────────┐
  │                PFC (observer + orchestrator)                        │
  │                                                                    │
  │  OBSERVE: feeling + body vote + chunk activations                  │
  │  HOLD: ~4±1 WM slots (beginner: small, expert: meta-chunks)       │
  │  TYPE 4: deliberate linking = "thinking"                           │
  │  IMAGINE: combine chunks → simulate scenarios chưa xảy ra         │
  │  DOMAIN-CHECK: "smooth" hay "sai so với reality"?                  │
  │                                                                    │
  │  ⚠️ KHÔNG THỂ: feel trực tiếp | compile | override signal mạnh   │
  │  PFC effectiveness = f(chunks đã compiled cho tình huống đó)       │
  │                                                                    │
  └──────┬──────────────────────────────────────┬──────────────────────┘
    ④↑ feeling                             ⑤↓ orchestrate
    arrives                                (hold chunks →
                                            bias direction)
  ┌──────┴──────────────────────────────────────┴──────────────────────┐
  │                        FEELING (bridge)                             │
  │                                                                     │
  │  Body signals integrate → trở thành PFC-observable                  │
  │  7-layer fidelity: raw 100% → ... → explanation 20-70%             │
  │  Wise: trust L3-4 (pre-label) | Naive: trust L6-7 (lossy nhất)    │
  │                                                                     │
  └──────┬──────────────────────────────────────────────────────────────┘
    ③↑ magnitude × clarity → PFC-observable
  ┌──────┴──────────────────────────────────────────────────────────────┐
  │                   UNCONSCIOUS PROCESSING                             │
  │                                                                      │
  │  CHUNK-SYSTEM (sole substrate):                                      │
  │    Compile: repetition + emotional peak + multi-modal + sleep        │
  │    Activate: probability-weighted spreading activation               │
  │    Link: Type 1-3 auto + Type 4 PFC deliberate                      │
  │    Never delete — only probability shift                             │
  │    Proto-chunk → Compiled → Meta-chunk (gradient)                    │
  │                                                                      │
  │  BODY-FEEDBACK (continuous evaluation):                              │
  │    REWARD (input > baseline) | DISSONANCE (input < baseline)        │
  │    Dual-Pull: hardware pull (smooth) × domain pull (adapt)          │
  │    H10: 5 preconditions ALL required for full signal                 │
  │                                                                      │
  │  CORTISOL (amplifier xuyên suốt):                                   │
  │    Modulates: sensitivity + energy + direction                       │
  │    Direction gate: novelty cortisol → approach | threat → avoidance │
  │    7 modes: IDLE → LAZY → ACTIVE → FOCUSED → PUSH → FREEZE → CRASH │
  │                                                                      │
  │  FUNCTIONS trên chunks:                                              │
  │    SPM (Self-Pattern-Match): self-chunks → template → empathy        │
  │    Agent Modeling: object + logic + modeling + schema override        │
  │    Valence: body assessment stored in chunks, propagates             │
  │    Imagination: PFC combine chunks → simulate chưa xảy ra           │
  │                                                                      │
  └──────┬──────────────────────────────────────────────┬────────────────┘
    ②↑ raw signals                              ⑥↓ compiled → execute
  ┌──────┴──────────────────────────┐  ┌────────────────┴────────────────┐
  │         BODY-INPUT               │  │        BODY-OUTPUT              │
  │                                  │  │                                 │
  │  L0: Alive threshold             │  │  Motor: compiled chunks         │
  │    (circuit breaker, binary)     │  │    → movement                   │
  │  L1: 17 categories               │  │  Speech: language chunks        │
  │    (receptors → raw signals)     │  │    → verbal output              │
  │    Mỗi input: evolved baseline   │  │  Expression: facial, postural, │
  │    + individual baseline         │  │    vocal (often unconscious)    │
  │    + delta rule evaluation       │  │  PFC hold intention →           │
  │                                  │  │  vô thức execute details        │
  └──────┬───────────────────────────┘  └────────────────┬───────────────┘
    ①↑ stimuli                                      ⑦↓ effects
  ┌──────┴───────────────────────────────────────────────┴───────────────┐
  │                            DOMAIN                                     │
  │  Môi trường thực (vật lý, sinh học, xã hội, thông tin)               │
  │  Tồn tại khách quan — domain KHÔNG nói dối                           │
  │  Cục bộ thay đổi khi: tương tác + di chuyển + đổi góc nhìn          │
  └──────────────────────────────────────────────────────────────────────┘

  🔄 LOOP: ①→②→③→④ (perception ↑) + ⑤→⑥→⑦ (action ↓) → ① LIÊN TỤC
  Kể cả khi ngủ (REM processing, consolidation)
  Multiple timescales chạy ĐỒNG THỜI: ms → seconds → days → decades
  Development = cùng architecture, chunk density TĂNG DẦN
```

### §1.3 Mapping giữa Hardware và Software

```
🟡 MAPPING GIỮA HARDWARE VÀ SOFTWARE:

  ┌──────────────────────┬──────────────────────────────────────────────┐
  │ Software (chạy gì)    │ Hardware (ở đâu)                              │
  ├──────────────────────┼──────────────────────────────────────────────┤
  │ Body-Input (L0+L1)   │ Receptors → D (reflex) + C (thalamus) + B    │
  │ Chunk compile        │ B (PFC trainable) + C (indirect) + D (≈0)    │
  │ Body-Feedback fire   │ C (amygdala, VTA, brainstem) + B (insula)    │
  │ Feeling integrate    │ B (anterior insula → ACC → vmPFC)            │
  │ PFC observe + hold   │ A (dlPFC working memory)                     │
  │ PFC orchestrate      │ A → B (top-down) + A → C (vmPFC-amygdala)   │
  │ Cortisol amplifier   │ C (HPA axis) → effects xuyên A+B+C+D        │
  │ Motor execute        │ A hold → B (motor cortex) → D (spinal)      │
  │ Delta rule (VTA)     │ C (VTA fire) → signal tới B + A              │
  │ Self-signal interoc. │ B (anterior insula) đọc D qua C (vagus)     │
  └──────────────────────┴──────────────────────────────────────────────┘

  ⭐ KEY INSIGHT:
    Hardware map = 4 vùng CỤ THỂ (A/B/C/D) — verify được bằng fMRI, lesion
    Software map = 7 bước CHỨC NĂNG (①→⑦) — describe cách system HOẠT ĐỘNG
    Interface map = observable patterns — mô tả cái OBSERVER THẤY
    Cùng hệ thống. Ba góc nhìn. Chi tiết Hardware → Core-Hardware.md.
```

### §1.4 Tại sao cycle, không layers

```
V7.5 LAYERS — vấn đề gì:

  L0 > L1 > L2 > L3 implies:
  ① Fixed priority ordering (L0 luôn thắng L1)
  ② Drives = separate operators đứng trên substrate
  ③ Connection, meaning = phải "nhét vào" layer nào đó
  ④ Development = unclear (layer nào develop trước?)

  Nhưng:
  ① Priority = signal strength, không phải layer rank
     → Đau mạnh thắng đói nhẹ, nhưng đói cực nặng thắng đau nhẹ
     → = Signal strength decides, not layer position
  ② Drives = emergent patterns trong cycle, không phải operators
  ③ Connection = L1 multi-input aggregate + attachment chunks → solved
  ④ Development = chunk density → clear

V7.8 CYCLE — giải quyết:

  ① No fixed priority — signal strength decides (loudest wins)
  ② No separate operators — drives = observation labels
  ③ No placement problem — everything = function or property of cycle
  ④ Development = same cycle, more chunks → naturally explained

SO SÁNH VỚI 6-STEP LOOP (Body-Feedback.md §3):

  Body-Feedback.md §3 mô tả: Domain → Body sensory → Feedback → Schema Update → Action → Domain
  V7.8 REFINES: adds Feeling bridge + PFC observation + Orchestrate detail.
  = V7.8 = 6-step + explicit Feeling + PFC + Orchestrate.
  COMPLEMENTARY, not competing.
```

---

## §2 — DOMAIN

```
🟢 DOMAIN = MÔI TRƯỜNG THỰC MÀ CON NGƯỜI TỒN TẠI:

  VẬT LÝ: ánh sáng, âm thanh, nhiệt độ, không khí, mặt đất,...
  SINH HỌC: thực phẩm, nước, sinh vật, vi khuẩn, virus,...
  XÃ HỘI: agents (người, động vật), cộng đồng, văn hóa, ngôn ngữ,...
  THÔNG TIN: sách, internet, AI, truyền thông, giáo dục,...

  Domain CÓ CÁC ĐẶC TÍNH (Domain.md §2):
    → Tồn tại KHÁCH QUAN — không phụ thuộc vào body observation
    → KHÔNG BAO GIỜ THAY ĐỔI bản chất — luật vật lý, cấu trúc thực tế
      vẫn y nguyên. Trước con người → domain ĐÃ CÓ.
      Sau con người tuyệt chủng → domain VẪN CÒN.
    → CÁI THAY ĐỔI là domain CỤC BỘ xung quanh cá nhân:
      ① Cá nhân TƯƠNG TÁC với domain → thay đổi cục bộ (xây nhà, trồng cây)
      ② Cá nhân DI CHUYỂN trong domain → gặp phần domain khác
      ③ Cá nhân THAY ĐỔI GÓC NHÌN → chunks thay đổi → "thấy" domain khác
      → Chuyên gia xem tranh thấy bầu trời, người thường thấy đồ cũ
        = cùng domain, khác chunks → khác observation
    → KHÔNG THỂ biết hoàn toàn — body chỉ sample qua receptors (fragments)
    → Cung cấp FEEDBACK THẬT — domain không nói dối
      (domain feedback thật, NHƯNG human nhận + giải thích CÓ THỂ SAI
      → sai nằm ở interface, không nằm ở domain — Domain.md §2 ⑥)

  ANCESTRAL DOMAIN (2M+ năm):
    → Natural fractals, pink noise, tribal voices 30-150,
      daily walking 8-15 km, whole foods, natural light cycles,
      frequent social touch, multi-generational community
    → Body-input baselines CALIBRATED cho domain này
    → Why-Body-Knows.md §4: 4-tier calibration theory

  MODERN DOMAIN:
    → Screens, processed food, sedentary, artificial light,
      reduced touch, nuclear family, attention economy
    → Mismatch với ancestral baseline → "silent deficiencies"
    → Body-Input-Enumeration.md §5: baseline adaptation mechanism

  AI ERA DOMAIN:
    → Unlimited information, AI assistance, screen-mediated life
    → New mismatch patterns emerging
    → Framework concern: body-input deprivation accelerating
```

---

## §3 — BODY-INPUT (L0 + L1)

### §3.1 L0 — Alive Threshold (Circuit Breaker)

```
🟢 L0 = BINARY CEASE-FUNCTION THREATS:

  Oxygen deprivation (minutes), extreme temperature (hours),
  critical dehydration (days), starvation (weeks),
  critical injury / blood loss (immediate),
  suffocation, drowning, electrocution (seconds)

  ĐẶC TÍNH:
    → BINARY: crossed = death, not crossed = function maintained
    → FIRES BEFORE unconscious processing (reflex, 50ms)
    → SUPPRESSES all other processing khi active
    → UNIVERSAL: mọi người, mọi văn hóa, mọi thời đại
    → Signal: LOUD, non-suppressible, non-habituable
    → Negativity bias + loss aversion AMPLIFIED ở L0

  KHÁC L1:
    → L1 deviations = uncomfortable but FUNCTIONAL
    → L0 crossed = function CEASES
    → L0 = circuit breaker TRƯỚC cycle
    → L1 = input cho cycle processing

  Reference: Body-Input-Enumeration.md §1.2.1
```

### §3.2 L1 — 17 Body-Input Categories

```
🟢🟡 L1 = BODY-INPUTS VỚI ADAPTIVE BASELINE:

  17 sub-categories trong 3 taxonomy chuẩn neuroscience:

  EXTEROCEPTION — sensing external world (5):
    ① Vision: fractal D ≈ 1.3-1.5 (Taylor 2006), bio motion, faces
    ② Audition: pink noise 1/f (Voss & Clarke 1975), voices
    ③ Olfaction: ~400 receptor types (Buck & Axel 1991), direct limbic
    ④ Gustation: 5+1 basic tastes, distinct from flavor
    ⑤ Tactile skin: mechanoreception + CT affective touch (Löken 2009)

  PROPRIOCEPTION — sensing body position (3):
    ⑥ Proprioception: muscle spindles + joint receptors (Sherrington 1906)
    ⑦ Vestibular: inner ear → head orientation, gravity
    ⑧ Kinesthetic: muscle dynamics, exertion, fatigue

  INTEROCEPTION — sensing internal state (9):
    ⑨ Thermoreception core: hypothalamic, ~37°C set point
    ⑩ Nociception: A-delta fast + C-fiber slow pain
    ⑪ Respiratory: breath rate, CO2 chemoreception, vagus
    ⑫ Cardiovascular: HR, HRV, blood pressure, vagal tone
    ⑬ Visceral: enteric NS (~100-500M neurons), gut-brain axis
    ⑭ Metabolic: blood glucose, hydration, ghrelin/leptin
    ⑮ Hormonal-sensed: cortisol, testosterone, oxytocin (downstream)
    ⑯ Sleep/Circadian: REM/NREM, SCN master clock, melatonin
    ⑰ Self-signal interoception META (KEYSTONE) ⭐

  ⭐ §3.2.1 Self-signal interoception = ARCHITECTURAL KEYSTONE:
    → Body's capacity to READ own internal state
    → Insula (Craig 2002, 2009) + ACC + predictive interoception (Seth 2013)
    → WITHOUT §3.2.1 functional: other inputs fire but body "cannot hear"
    → → Silent deficits accumulate without PFC awareness
    → Explains alexithymia (~10% population, Bird & Cook 2013)
    → Developmental: caregiver mirroring → child learns self-reading
    → Therapeutic targets: mindfulness, Gendlin focusing, somatic therapy
    → Reference: Body-Input-Enumeration.md §4.9

  MỖI INPUT CÓ:
    → Receptor system + neural pathway (hardware)
    → Evolved baseline range (ancestral calibration — Tier 1)
    → Individual baseline within evolved range (development — Tier 2)
    → Delta rule: deviation → reward (above) or dissonance (below)
    → Adaptation dynamics (§3.3 below)
    → Individual variation patterns

  Reference: Body-Input-Enumeration.md §2-§4 cho 8-field schema mỗi input
```

### §3.3 Baseline Adaptation Mechanism

```
🟡🟢 DELTA RULE — CORE MECHANISM (Helson 1964):

  BL(t+1) = BL(t) + α × (input_quality(t) - BL(t))

  → input > baseline → positive prediction-delta → REWARD → seek repeat
  → Repeated exposure → baseline shifts UP → same input = no reward
  → Seeking escalation → HEDONIC TREADMILL established

  EMPIRICAL VALIDATION: Hall 2019 NIH Cell Metabolism
    → Same participants, same calories offered
    → Ultra-processed diet → +500 kcal/day overconsumption
    → = Direct experimental measurement của baseline distortion

  ASYMMETRIC DECAY:
    → Baseline shifts UP fast (exploit new opportunities)
    → Baseline shifts DOWN slow (slow relinquishment)
    → Evolutionary logic: quick exploit + slow release = survival optimal
    → Modern consequence: engineered supernormal stimuli hijack "up" rapidly,
      recovery to ancestral baseline takes much longer

  UNIVERSAL ACROSS ALL 17 BODY-INPUT CATEGORIES:
    → Food (Hall 2019), sex, visual (screen), auditory (music),
      social validation, substances, mastery (Jiro)
    → One mechanism explains all — direction matters, not mechanism

  Reference: Body-Input-Enumeration.md §5
```

---

## §4 — UNCONSCIOUS PROCESSING

### §4.1 Chunk-System — Sole Substrate

```
🟡🟢 CHUNK = STRENGTH-WEIGHTED ASSOCIATIVE NETWORK COMPILED THROUGH EXPERIENCE:

  Não KHÔNG tính toán — não TÌM KIẾM trong database.
  Database = chunks. Operators = vô thức (~95%) + PFC (~5%).

  🟢 Hebb (1949): "Neurons that fire together, wire together"


  CHUNK = ATOM:
    → Nhóm neurons đã wire together → fire thành 1 ĐƠN VỊ
    → GRADIENT (yếu → mạnh), không binary (có/không)
    → Proto-chunk → Compiled → Meta-chunk
    → Multi-modal từ gốc: chunk "mẹ" = mặt + giọng + ôm + ấm

  4 COMPILE MECHANISMS:
    ① Repetition — LTP strengthening (🟢 Bliss & Lømo 1973)
    ② Emotional peak — amygdala + NE, 1 lần đủ (🟢 Brown & Kulik 1977)
    ③ Multi-modal — nhiều kênh cùng lúc → wire across cortex
    ④ Sleep consolidation — hippocampus replay (🟢 Walker 2017)

  5 EXTERNAL INSTALL MECHANISMS (Chunk.md §2.3):
    ① Co-attention ② Imitation ③ Social referencing
    ④ Label installation ⑤ Cultural transmission
    → TẤT CẢ 5 yêu cầu TRUST GATE ở mức nào đó
    → Trust = ONLY BRIDGE giữa external → internal compile
    → (Collective-Body.md §5: trust = cơ chế DUY NHẤT nối cấp 1 và cấp 2)

  3 LOẠI COMPILE (Compile-Taxonomy.md v1.1, Drill §2-§3):

    Loại A — Direct Short (~90%): body trải nghiệm trực tiếp → compile
      [toán → brain fire → reward] hoặc [không học → mắng → sợ]
      = Hardware fit (approach) hoặc Threat (avoidance). 1-2 nodes.
      PFC accuracy ~90%. Cơ chế: 4 compile mechanisms trực tiếp.

    Loại B — Compiled Expertise (~5%): repetition + PFC-directed + domain verify
      [bán hàng → feedback → adjust → compile] lặp 1000+ lần
      = Deliberate practice. Meta-chunks. "Chuyên gia = library rất sâu."
      PFC = DIRECTOR (hold + guide), Body = COMPILER (wire thật).

    Loại C — Installed via Trust + Collective (~5%): external source → trust gate → compile
      [mẹ nói học tốt → trust → compile "học=tốt"] = 1-2 nodes
      = Trust install. Social default. Chain dài SỐNG ở collective (Cấp 2).
      PFC accuracy ~30-60% (confabulation phổ biến nhất ở Loại C).

    → Cùng 4 compile mechanisms, KHÁC LOẠI sử dụng.
    → ~90%/~5% = calibration anchor (§12.4). Overlap A/C → không cộng 100%.
    → Chi tiết: Compile-Taxonomy.md §2-§3

  VP §4 CLARIFICATION (VP v1.4, Drill §6, §22):
    Chain analysis [toán→điểm→đại học→việc→lương→body-base]
    = CẤP 3 (framework giải thích tại sao behavior hoạt động).
    KHÔNG phải cách brain PROCESS ở CẤP 1 — cá nhân compile SHORT (1-2 nodes).
    Chain dài SỐNG ở CẤP 2 (collective infrastructure hold cho cá nhân).
    Vẫn CÓ GIÁ TRỊ: chẩn đoán chain gãy, thiết kế collective, verify trust.
    → Chi tiết: VP v1.4 §4, Collective-Body.md §1 (Model 3 cấp)

  COMPILE RATE:
    ≈ f(exposure × saliency × contingency × peak_valence × multi_modal_richness)
    → Individual variation EXPLAINED: different environments → different outcomes
    → = NOT "tài năng bẩm sinh" → mà "môi trường compile khác nhau"

  4 CONNECTION TYPES (Chunk.md §3):
    Type 1: Shared contamination (automatic, spreading activation)
    Type 2: Aha moment (DMN incubation → sudden burst)
    Type 3: Meta-chunk compile (repeated co-firing → merge)
    Type 4: Static logical linking (PFC deliberate — = "thinking")

  ACTIVATION DYNAMICS (Chunk.md §4):
    → Probability-weighted spreading activation (🟢 Collins & Loftus 1975)
    → 7-factor link strength: repetition, recency, emotional weight,
      multi-modal, context match, emotional state match, anchor strength
    → Competitive re-linking: new links compete with old (🟢 Nader 2000)
    → NEVER delete — only probability shift
    → Trauma = Expertise = CÙNG cơ chế, KHÁC hướng

  ANCHORS (Chunk.md §5):
    → 5 types: verbal, contextual, ritual, emotional, multi-anchor
    → Anchor = retrieval PATH (not content)
    → "Quên" = retrieval path weak (chunk still exists)
    → Label = "vé vào cửa" cho PFC planning system

  "SCHEMA" TRONG V7.8 = OBSERVATION LABEL:
    → Schema = named chunk-network pattern (chunks + links + purpose)
    → Giống "feature" trong software: tên gọi cho composition of functions
    → Schema KHÔNG phải component riêng biệt — là CÁCH QUAN SÁT chunk networks
    → Vẫn hữu ích như shorthand (giống "channel" shorthand trong Body-Base reframe)
    → Nhưng không phải đặc tính kỹ thuật của brain architecture

  MODEL 3+1 (Body-Base.md v2.0 §3, Drill §23):

    3 COMPONENTS CHẠY ĐỒNG THỜI trên chunk substrate:
      ① VÔ THỨC (~95%): compile + fire + evaluate
      ② PFC (~5%): direct + sequence + observe
      ③ TRUST: gate + modulate + connect (individual ↔ external)
    + 1 BRIDGE:
      ④ EXTERNAL TOOLS (×∞): giấy, máy tính, AI → mở rộng PFC capacity

    → Model 3+1 = REFINE §4 unconscious processing components
    → Cycle architecture KHÔNG đổi — chỉ formalize components BÊN TRONG
    → Trust = Component 3, KHÔNG phải property — vì trust GATE tất cả external install

  MODEL 3 CẤP (Collective-Body.md v1.1 §1):

    Cấp 1: Individual — compile SHORT ở body (1-2 nodes). File NÀY mô tả.
    Cấp 2: Collective — institutions/culture HOLD chain dài (distributed).
    Cấp 3: Framework — explanatory decomposition (VP §4 chain analysis).

    → Individual cycle (file này) = Cấp 1
    → Collective phenomena = Cấp 2 (chi tiết: Collective-Body.md)
    → Trust = ONLY BRIDGE giữa Cấp 1 và Cấp 2

  SO SÁNH CHUNKS VỚI CODE FUNCTIONS:
    → Functions trong code = atomic units, KHÔNG THỂ phân loại hết
    → Features trong software = named patterns of function composition
    → Chunks trong não = atomic associative networks
    → Schemas = named patterns of chunk composition
    → Giáo sư toán ≠ biết bơi: chunks toán ≠ chunks bơi, dù cùng 1 não
    → Dev game → dev web dễ hơn newbie: engine overlap, nhưng domain chunks khác
    → Nhân viên tạp hóa + giáo sư toán: cùng dùng math chunks hàng ngày,
      cùng coherence khi hoàn thành phép tính, vị trí rất khác nhau

  Reference: Chunk.md v2.1 (full detail, 14 sections)
```

### §4.2 Body-Feedback — Continuous Evaluation

```
🟡🟢 BODY-FEEDBACK = CÁCH BODY ĐÁNH GIÁ MỌI THỨ LIÊN TỤC:

  CHỈ 2 HƯỚNG:
    → REWARD (input above baseline, positive prediction-delta)
    → DISSONANCE (input below baseline, negative prediction-delta)
    → + NEUTRAL (at baseline, no signal)

  DUAL-PULL ARCHITECTURE (Body-Feedback.md §2):

    ① HARDWARE PULL (bảo thủ, muốn smooth):
       → Hebbian LTP: patterns quen càng mạnh
       → Habituation: VTA quen → không fire
       → Metabolic efficiency: compiled = low cost
       → Feature: comfort zone, routine, contentment
       → Dark side: stagnation, evolution lag

    ② DOMAIN PULL (đòi adapt, map reality):
       → prediction-delta: pattern mới → dopamine → attention
       → Prediction-delta: mismatch → update pressure
       → Evolutionary: không map reality → không sống sót
       → Feature: learning, growth, curiosity
       → Dark side: burnout, neural wear

    ⭐ TENSION = EVOLUTIONARY FEATURE, NOT BUG:
       → Body signals (reward/dissonance) = READOUT of this tension
       → Reward fires khi 2 lực ALIGN ("passion" = body thích + domain cần)
       → Dissonance fires khi 2 lực CONFLICT

  H10 — 5 PRECONDITIONS FOR SIGNAL FIRE (Body-Feedback.md §5):

    ┌───┬──────────────────────────┬────────────────────────────┐
    │ # │ Precondition             │ Failure → subjective        │
    ├───┼──────────────────────────┼────────────────────────────┤
    │ 1 │ Body-need gap open       │ "Không cần" / polite no     │
    │ 2 │ Chunks base adequate     │ "Chả hiểu" / confusion      │
    │ 3 │ prediction-delta threshold met  │ "Bình thường" / "quen rồi" │
    │ 4 │ Goldilocks zone (40-70%) │ Too alien or too familiar   │
    │ 5 │ Chunk association tag    │ "Ghét dù hiểu" / avoidance  │
    └───┴──────────────────────────┴────────────────────────────┘
    ALL 5 REQUIRED for full signal. Missing ANY → absent or wrong.

  3 NGUỒN KHÓ CHỊU THẬT (Body-Feedback.md §4):
    ① Nociception (physical damage — tissue → nociceptors → pain)
    ② Mismatch (schema ≠ reality — prediction-delta → "something is off")
    ③ Recalibration (neurons adjusting — "căng đầu khi học" = wiring change)
    → Cortisol arrives AFTER, KHÔNG gây đau — sustainer, not cause

  CHUNK DYNAMICS — TRỤC THỨ 4 (Body-Feedback-Mechanism.md v1.2):
    Body-feedback có 4 trục phân loại ORTHOGONAL:
      Trục 1 — Direction: reward/dissonance (dual-pull ở trên)
      Trục 2 — Magnitude: 14 levels (02-Dissonance.md)
      Trục 3 — Source: nociception/mismatch/recalibration (3 nguồn ở trên)
      Trục 4 — Chunk Dynamics: HOW chunks fire tạo signal
        → 2 input sources: Sensory-Driven / Pattern-Driven
        → 3 dynamics: Chunk-Shift / Chunk-Miss / Chunk-Gap
        → Compound: multi-layer chunk firing = multi-flavor signal
    Reference: Body-Feedback-Mechanism.md v1.2

  REWARD SIGNAL ARCHITECTURE (Reward-Signal-Architecture.md v1.0):
    → Type A: Evaluative (opioid) — H10 pass → VTA → opioid reward
    → Type B: Direct State (non-opioid) — body-state change itself IS reward
    → A₀→A₃: Complexity gradient (simple match → creative insight)
    → A Gates B: evaluative layer modulates direct-state reward
    → 5 Reward Profiles: "hương vị" reward (cognitive, social, body, creative, flow)
    Reference: Reward-Signal-Architecture.md v1.0

  Reference: Body-Feedback.md + 01-04 drill files (~7,100L)
```

### §4.3 Cortisol — Amplifier

```
🟡🟢 CORTISOL = CHANGE-READINESS AMPLIFIER, KHÔNG PHẢI STRESS HORMONE:

  Cortisol KHÔNG phải component riêng biệt.
  Cortisol = PHYSICAL MECHANISM (hormone thật) chạy XUYÊN QUA toàn bộ cycle.

  MODULATES 3 THINGS:
    → SENSITIVITY: how strong body-input signals register
    → ENERGY: how sustained action can be
    → DIRECTION: approach (novelty) vs avoid (threat) — at compile time

  DIRECTION GATE (Chunk.md §2.4 NT7):
    → Cortisol tại compile time = determines chunk association tag
    → Novelty-direction cortisol → chunks tag APPROACH
    → Threat-direction cortisol → chunks tag AVOIDANCE
    → CÙNG cortisol level → KHÁC direction → KHÁC outcome hoàn toàn

  7 MODES (inverted-U):
    IDLE (quá thấp) → LAZY → ACTIVE → FOCUSED (optimal) → PUSH → FREEZE → CRASH (quá cao)

  ⚠️ PHÂN BIỆT QUAN TRỌNG — 2 cơ chế KHÁC NHAU:

    NE (Norepinephrine) → FREEZE TỨC THỜI (Cortisol-Baseline §9.1):
      → Threat detect → amygdala → NE flood → α1 receptors → PFC OFFLINE
      → Timeline: milliseconds
      → KHÔNG phải damage — là DESIGN FEATURE (circuit breaker)
      → Tắt PFC để nhường subcortical (nhanh hơn cho survival)
      → Recovery: seconds sau khi threat qua → PFC bật lại hoàn toàn
      → 🟢 Arnsten 2009, 2015 — α1/α2 mechanism

    CORTISOL → NEURAL WEAR MÃN TÍNH (Cortisol-Baseline §9.2-§9.4):
      → Cortisol baseline CAO MÃN TÍNH (weeks-months-years)
      → → Glutamate cao liên tục → PFC dendrite retraction
      → → Worse pattern recognition → worse solving → more cortisol → loop
      → = Trauma loop 4-stage degradation (Body-Feedback.md §7)
      → 🟢 Arnsten 2009, McEwen 2007

    ORDER: Schema detect → NE spike (ms) → Adrenaline (1-2s) →
      Cortisol peak (5-20min) → Cortisol sustain → merge baseline
    → NE = ACUTE circuit breaker (instant, recoverable)
    → Cortisol = CHRONIC wear (cumulative, slow damage)

  Reference: Cortisol-Baseline.md v2.0 (full 3,059L)
```

### §4.4 Functions chạy trên Chunk Substrate

```
🟡 MỌI "MODULE" CŨ = FUNCTION CHẠY TRÊN CÙNG CHUNK SUBSTRATE:

  SELF-PATTERN-MATCH (Agent-Mechanism.md §0 / SPM.md v2.2):
    → 2 Functions: F1 (forward simulation) + F2 (generate from template)
    → Dùng self-chunks làm template → simulate target's state
    → = "Empathy mechanism" khi applied to others
    → = "Self-awareness" khi applied to self
    → Quality = f(chunk library depth × overlap × feedback)
    → Valence gate: ❸ positive → F1 engage, ❸ negative → F1 suppress

  AGENT MODELING (Agent-Mechanism.md §3):
    → 4-layer: Object chunks + Logic + Modeling overlay + Schema override
    → Logic + Modeling run PARALLEL, different mix ratios per entity
    → Mix: cục đá 100% logic / bạn thân 70% modeling / Đức Mẹ Mode 1 100% schema

  EMPATHY (Empathy.md v2.0):
    → = Self-Pattern-Match applied to other agent's states
    → Connection ⊃ Empathy (mechanism ⊃ observation)
    → 2-luồng: L1 (SPM-owned, momentary) + L2 (Entity-owned, structural)
    → Burnout = f(L1/L2 ratio): too much L1, not enough L2
    → 🟢 Bird & Cook 2013: self-awareness = prerequisite for empathy

  VALENCE (Valence-Propagation.md v1.4):
    → Body's assessment of how entity affects body-inputs
    → Multi-channel profile (NOT good/bad binary)
    → Stored as property of chunks (valence tag at compile time)
    → Propagates qua chunk links — PFC often BLIND to chains
    → VP §4 chains = EXPLANATORY (Cấp 3), not processing (Cấp 1)

  IMAGINATION (Imagine-Final concept):
    → PFC combines existing chunks → simulate scenarios chưa xảy ra
    → Body-feedback evaluates imagined scenarios (body reacts to imagination)
    → Imagined chunks CAN trigger real body-base responses
    → = PFC "hijack" body-input: vẽ ra giấy → mắt thấy → continue imagine

  NONE of these need separate module. ALL run on chunk substrate.
```

---

## §5 — FEELING (Bridge Unconscious → PFC)

```
🟡🟢 FEELING = WHAT PFC SEES KHI OBSERVE BODY-CHUNK INTERACTION:

  KHÔNG PHẢI hệ thống riêng biệt. KHÔNG có "feeling module."
  Feeling = INTERFACE giữa body computation và PFC awareness.
  Body = tính toán. Feeling = kết quả hiện lên. PFC = observe.

  3 ĐẶC TÍNH DEFINING:
    ① MULTI-SOURCE: convergence từ nhiều body systems đồng thời
    ② INTEGRATED: unified sense, không phải list of signals
    ③ OBSERVABLE: threshold phụ thuộc magnitude × clarity (2 chiều)

  7-LAYER FIDELITY GRADIENT (Feeling.md §2):

    Layer 1: Raw body signals              100% fidelity
    Layer 2: Integration (insula+ACC+VMPFC)  ~95%
    Layer 3: Consciousification              ~90%
    ════════ PFC THRESHOLD ════════════════════════
    Layer 4: Observation                     ~85%
    Layer 5: Location                        70-90%
    Layer 6: Labeling                        40-80%  ← CRITICAL LOSS
    Layer 7: Explanation                     20-70%  ← MOST RISKY

    → Wise: trust Layer 3-4 (body noticeable, pre-label)
    → Naive: trust Layer 6-7 (label + explanation = lossy nhất)
    → Training = đưa attention ngược về Layer 3-4

    🟡 % = calibration anchor, KHÔNG phải đo lường (§12.4).
       Insight: fidelity GIẢM DẦN + drop critical ở L6-L7.
       Mỗi người/domain/context → % thực tế khác.

  ⭐ PFC OBSERVATION THRESHOLD — 2 CHIỀU (magnitude × clarity):

    Threshold KHÔNG chỉ phụ thuộc cường độ signal.
    Còn phụ thuộc ĐỘ RÕ = f(chunk density cho lĩnh vực đó).

    MAGNITUDE = cường độ body signal (body-feedback generate):
      → prediction-delta, nociception, mismatch, cortisol amplification
      → Cao: đau, sợ, phấn khích → signal loud → PFC khó bỏ qua
      → Thấp: lấn cấn nhẹ, vi sai nhỏ → signal quiet → dễ lọt

    CLARITY = chunk density cho phép PFC PHÂN BIỆT signal nói gì:
      → Chunks tích lũy trong domain + self-signal interoception (§3.2.1)
      → Cao: expert biết chính xác "đây là gì" → detect dù magnitude nhẹ
      → Thấp: novice thấy "có gì đó" nhưng không biết gì → cần mạnh mới notice

    ┌────────────┬──────────────────────┬──────────────────────────┐
    │            │ MỜ (ít chunks)        │ RÕ (nhiều chunks)         │
    ├────────────┼──────────────────────┼──────────────────────────┤
    │ MẠNH       │ PFC thấy nhưng mờ    │ PFC thấy rõ ràng         │
    │ (cường độ  │ "có gì đó sai"       │ "cái này sai ở ĐÂY"     │
    │  cao)      │ Vague anxiety,       │ Expert crisis response,  │
    │            │ panic không rõ nguồn │ bác sĩ cấp cứu           │
    ├────────────┼──────────────────────┼──────────────────────────┤
    │ NHẸ        │ PFC không notice     │ PFC tinh tế phát hiện    │
    │ (cường độ  │ Signal quá yếu +    │ Expert subtle detection:  │
    │  thấp)     │ quá mờ → bỏ qua    │ chuyên gia xem tranh ở   │
    │            │ hoàn toàn           │ chợ đồ cũ, sommelier      │
    └────────────┴──────────────────────┴──────────────────────────┘

    → Clarity CAO = HẠ magnitude threshold → expert "thấy nhiều hơn"
    → Cùng input, cùng cường độ → expert thấy rõ, novice bỏ qua
    → = Giải thích tại sao chuyên gia phát hiện patterns người khác miss
    → Self-signal interoception (§3.2.1) = clarity cho TOÀN BỘ feeling
    → Alexithymia = clarity thấp cho self-signal → PFC "deaf" to own body
    → Connection: H10 P2 "chunks base adequate" = clarity cho body-feedback

  7 LOẠI FEELING (cùng mechanism):
    ① Body-physical: "đói", "mệt", "đau"
    ② Emotional: "vui", "buồn", "giận", "sợ"
    ③ Social reading: "người kia không tin"
    ④ Cognitive/prediction: "bài này đúng"
    ⑤ Predictive/intuition: "có gì đó không ổn"
    ⑥ Valence: "thích cái này", "ghét cái tên"
    ⑦ Schema-triggered: "bình yên khi về nhà"
    → TẤT CẢ = cùng mechanism: integrated body signal → PFC observe

  6-POINT FEELING-INTUITION GRADIENT (Chunk.md §10):
    ① Body Signal (clear, <100ms) → ⑥ Pre-monition (vague, hours)
    → NOT discrete types — CONTINUOUS spectrum
    → Expert intuition = position ④ but HIGH accuracy (calibrated chunks)
    → Beginner gut feeling = position ③ but LOW accuracy (few chunks)

  TEMPORAL ORDER (invariant):
    Body compute FIRST → Feeling emerge → PFC observe LAST
    → 🟢 Damasio 1994, 1999: somatic markers PRECEDE conscious decision
    → Feeling KHÔNG tạo ra thông tin mới — feeling REPORT body state

  Reference: Feeling.md v2.1 (full 14 sections)
```

---

## §6 — PFC (Observer + Orchestrator)

### §6.1 PFC = Observer, KHÔNG phải Controller

```
🟡🟢 PFC CÓ THỂ:
  → OBSERVE: đọc feeling, detect chunk activations
  → HOLD: ~4±1 WM slots (🟢 Cowan 2001)
  → SEARCH: hold chunks → bias spreading activation direction
  → TYPE 4 LINKING: deliberate "thinking" (PFC hold A + B → check overlap → body vote)
  → IMAGINATION: combine chunks → simulate scenarios chưa xảy ra
  → DOMAIN-CHECK: verify "smooth" vs reality (1A vs 1B selection pressure)
  → ORCHESTRATE: hold goals → bias unconscious processing direction

🟡🟢 PFC KHÔNG THỂ:
  → FEEL directly (phải NHẬN từ body qua feeling bridge)
  → COMPILE tự động (vô thức compile, PFC chỉ observe kết quả)
  → RUN 95% background processing
  → OVERRIDE body-base khi signal quá mạnh (đói cực → ăn ngấu, crush → ấp úng)
  → CONTROL motor trực tiếp (PFC hold "viết con chó" → vô thức execute gõ phím)

  ⭐ PFC HARDWARE SPECS (COMT, DRD4, WM capacity, modality balance,
  connectivity limits) → Core-Hardware.md §5.
  File này chỉ mô tả PFC FUNCTION — CÓ THỂ và KHÔNG THỂ làm gì.
```

### §6.2 PFC Orchestrate — Indirect Control

```
🟡 PFC KHÔNG ĐIỀU KHIỂN TRỰC TIẾP BODY-BASE:

  PFC hold chunks → BIAS spreading activation trong vô thức
  → Vô thức tự phản ứng dây chuyền theo bias
  → Body-output tự execute theo compiled chunks

  VÍ DỤ CƠ CHẾ:

    PFC hold "viết con chó":
      → Vô thức đã compile [gõ c-o-n space c-h-ó]
      → Ngón tay tự gõ → PFC nhìn lại: đúng ✓

    PFC hold "nói con chó":
      → Vô thức đã compile [thanh quản + lưỡi + hơi thở]
      → Miệng tự nói → PFC nghe lại: đúng ✓
      → PFC KHÔNG nghĩ gì tới cổ họng

    Chuyên gia xem tranh ở chợ đồ cũ:
      → Lướt qua → vô thức match weak pattern "nét vẽ kỳ lạ"
      → PFC notice → cầm lên, dùng kính lúp
      → PFC CHỦ ĐỘNG amplify input cho vô thức (xem kỹ hơn)
      → Vô thức match SÂU hơn → "bức tranh đặc biệt thật"
      → PFC không "thấy" tranh đẹp — PFC hold attention → vô thức match → body reward

    Đàm phán với đối tác:
      → TRƯỚC: PFC pre-compile chunks (đọc sách, kinh nghiệm, rehearsal)
      → TRONG: PFC hold 3 goals, switch qua lại:
        ① "nói chuyện với đối tác"
        ② "làm đối tác tin tưởng"
        ③ "lợi ích tối đa"
      → Vô thức đã có chunks cho từng goal → PFC chỉ direct attention
      → PFC observe: "đang ok" hoặc "cần switch goal"

  KHI PFC BẤT LỰC:

    Đói cực nặng → body-base signal quá mạnh:
      → PFC hold "ăn lịch sự" nhưng signal overwhelm
      → Vô thức override → ăn ngấu nghiến
      → PFC KHÔNG ĐỦ "lực" override body-base signal mạnh

    Gặp crush → body fire quá mạnh:
      → Tim đập, rạo rực, ấp úng
      → PFC hold "bình tĩnh" nhưng body overwhelm
      → Chunks cho tình huống rạo rực quá mức CHƯA COMPILED
      → Vô thức không có gì để run → PFC bất lực

  → PFC effectiveness = f(chunks đã compiled cho tình huống đó)
  → Nhiều chunks → PFC chỉ hold direction, vô thức run
  → Ít chunks → PFC bất lực dù hold mạnh cỡ nào
```

### §6.3 PFC Activation ≈ f(dissonance)

```
🟡 95/5 = OBSERVATION PARAMETER, KHÔNG PHẢI RATIO CỐ ĐỊNH:

  PFC hoạt động 100% NĂNG LỰC của nó — nhưng PHẠM VI kiểm soát giới hạn.
  PFC activation level TƯƠNG ỨNG với dissonance level:

    Vô thức ổn, môi trường ổn → PFC ~ 0% (không cần)
    Mild novelty → PFC ~ 5-15% (observe, light hold)
    Active problem → PFC ~ 20-40% (Type 4 linking, search)
    High stakes → PFC ~ 40-70% (strategic hold, domain-check)
    Crisis → PFC ~ 70-95% (full engagement, override attempts)
    Acute threat → NE α1 FREEZE — PFC offline tạm (ms, design feature, recover instant)
    Chronic overload → Cortisol neural wear — PFC dendrite retraction (weeks+, DAMAGE)

  → "95% vô thức" = observation that MOST processing doesn't need PFC
  → NOT "PFC only runs 5% of time"
  → PFC có thể tham gia bất cứ lúc nào nếu dissonance sufficient
  → % trên mỗi level = calibration anchor (§12.4). Mỗi người/context → khác.
```

### §6.4 PFC Dynamic Configurations

```
🟡 PFC KHÔNG PHẢI ON/OFF — CÓ 6 CONFIGURATION MODES (PFC-Configuration.md v1.0):

  ① Normal: full function suite available
  ② Reallocation (Flow): task-serving ON, self-monitoring OFF — effortless
  ③ Reconfigured: stress shifts function balance
  ④ Disconnected (Threat): NE α1 → ALL PFC functions OFF — subcortical takeover
  ⑤ Hyperactivated (Dissociation): 4 functions WEAPONIZED — emotional numbness
  ⑥ Disintegrated (Psychedelic): nearly ALL OFF, Modify ENHANCED — structural change

  Configuration ≠ Participation (Drive.md §2). Orthogonal:
  "PFC bận CỠ NÀO" (participation) ≠ "PFC wired THẾ NÀO" (configuration).

  Reference: PFC-Configuration.md v1.0 (full 24 Functions × 6 Modes matrix)
```

---

## §7 — BODY-OUTPUT

```
🟡 BODY-OUTPUT = HÀNH VI ẢNH HƯỞNG DOMAIN:

  MOTOR: compiled chunks → movement
    → Walking, reaching, typing, cooking,...
    → PFC hold intention → vô thức execute motor details
    → Expert: meta-chunks → smooth auto execution
    → Beginner: PFC micromanage → clumsy

  SPEECH: compiled language chunks → verbal output
    → PFC hold "what to say" → vô thức: phonology + prosody + grammar
    → 3-tier anchor system: individual → group → global (lossy)

  EXPRESSION: facial, postural, vocal (often unconscious)
    → Micro-expressions: vô thức fire BEFORE PFC can suppress
    → Body language: compiled postural schemas
    → Vocal tone: autonomic modulation (Porges polyvagal)

  → BODY-OUTPUT thay đổi DOMAIN CỤC BỘ → new stimuli → loop continues
  → Domain bản chất không đổi — cá nhân tương tác + di chuyển + đổi góc nhìn
  → Feedback: reality responds (domain feedback thật) → body evaluate → adjust
```

---

## §8 — OBSERVATION PARAMETERS

```
🟡 "DRIVES" VÀ "SCHEMAS" CŨ = THAM SỐ PHỤC VỤ QUAN SÁT:

  Không phải components kiến trúc. Là named patterns quan sát từ cycle.
  Giá trị: giúp mô tả, predict, communicate. Không phải mechanism.

  ┌──────────────┬──────────────────────────────────────────────────────┐
  │ Parameter    │ Quan sát cái gì                                       │
  ├──────────────┼──────────────────────────────────────────────────────┤
  │ Schema       │ Named chunk-network pattern (software "feature")      │
  │              │ Chunks + links + purpose = observation, not component  │
  ├──────────────┼──────────────────────────────────────────────────────┤
  │ Novelty      │ Positive prediction-delta pattern                      │
  │              │ Direct: đồ ăn ngon, cảnh đẹp, nhạc mới              │
  │              │ Via Imagination: sáng tác, Einstein years of novelty  │
  │              │ Tendency: người thích novelty X → xu hướng tiếp tục   │
  ├──────────────┼──────────────────────────────────────────────────────┤
  │ Threat       │ Dissonance from predicted harm                        │
  │              │ Body-base signal + anticipatory schema fire            │
  ├──────────────┼──────────────────────────────────────────────────────┤
  │ Status       │ Resource Access Map (Status.md v2.0)                  │
  │              │ Evolutionary: resource access = body-base reward THẬT │
  │              │ Spectrum: hổ(1D) → khỉ(hierarchy) → người(multi-dim) │
  │              │ 3 modes: Lấy/Trao đổi/Comply                         │
  │              │ Disruption→re-calibrate cycle                         │
  ├──────────────┼──────────────────────────────────────────────────────┤
  │ Protect      │ Loss aversion + ownership chunk patterns              │
  │              │ "Tính sở hữu": tay tôi, con tôi, laptop tôi         │
  │              │ Mức độ: laptop hỏng + đủ tiền mua mới → ok           │
  │              │         laptop hỏng + không đủ tiền → ghét bạn       │
  │              │ = f(perceived replaceability × attachment chunks)     │
  ├──────────────┼──────────────────────────────────────────────────────┤
  │ Connection   │ 3 Generative Primitives (Connection.md v3.1)          │
  │              │ ❶ Hardware × ❷ SPM F1/F2 × ❸ Per-Agent Valence       │
  │              │ 2-tầng: ❶ body-level pre-SPM + ❷ SPM adds precision  │
  │              │ "Cô đơn" = ❶ social dissonance + no anchor override  │
  ├──────────────┼──────────────────────────────────────────────────────┤
  │ Meaning      │ Life-level Anchor-Schema ổn định (Meaning.md v2.0)    │
  │              │ 5 types: GOAL/STATE/IDENTITY/FAITH/ROLE               │
  │              │ Mỗi người meaning KHÁC vì optimal anchor KHÁC        │
  │              │ Frankl: cùng body-inputs, khác anchor → khác outcome  │
  ├──────────────┼──────────────────────────────────────────────────────┤
  │ Mastery      │ Domain chunk accumulation + sustained delta rule      │
  │              │ Nhân viên tạp hóa + giáo sư toán: cùng math chunks,  │
  │              │ cùng coherence khi tính xong, vị trí rất khác        │
  ├──────────────┼──────────────────────────────────────────────────────┤
  │ Autonomy     │ Prediction accuracy pattern (agency feeling)          │
  │              │ "Tôi quyết định → kết quả tôi muốn" = high accuracy  │
  │              │ "Bị ép buộc" = prediction override → dissonance       │
  ├──────────────┼──────────────────────────────────────────────────────┤
  │ Disgust      │ Gustatory/olfactory rejection threshold               │
  │              │ Hardware: rejection threshold innate                   │
  │              │ What triggers: heavily learned (cultural)              │
  ├──────────────┼──────────────────────────────────────────────────────┤
  │ Melody       │ Emergent state of all systems running simultaneously │
  │              │ Good Melody 4 criteria: hardware smooth + map accurate │
  │              │ + map wide + sustainable long-term                     │
  ├──────────────┼──────────────────────────────────────────────────────┤
  │ Gratitude    │ Tầng 5 observation (Gratitude.md v1.1)                │
  │              │ 9 prerequisites đồng thời, agent-entity only          │
  │              │ 3 anti-habituation mechanisms. "Cảm ơn" = body tool  │
  ├──────────────┼──────────────────────────────────────────────────────┤
  │ Obligation   │ Compiled prediction về cost duy trì access           │
  │              │ (Obligation.md v1.0) 5-factor + StatusGap. 6 types   │
  │              │ Tiền = obligation technology. Access cost = mode shift│
  ├──────────────┼──────────────────────────────────────────────────────┤
  │ Passion      │ When hardware pull + domain pull ALIGN (rare, quý)   │
  └──────────────┴──────────────────────────────────────────────────────┘

  CROSS-SPECIES PATTERN:
    Ở động vật: hardware (hormone) → behavior trực tiếp
    Ở con người: hardware → chunk processing → behavior
    = Cùng hormones, nhưng chunk system phức tạp → override đáng kể
    = Giải thích tại sao human behavior khó đoán hơn nhiều

  GIÁ TRỊ CỦA OBSERVATION PARAMETERS:
    → Predict patterns: người thích novelty X → xu hướng tiếp tục
    → Communicate: "anh ấy rất protect" dễ hiểu hơn "ownership chunks + loss aversion"
    → Diagnose: status thấp + connection thiếu + meaning absent = depression risk
    → NHƯNG: không phải mechanism — không dùng để thiết kế can thiệp
    → Can thiệp phải ở level mechanism: thay đổi body-input, compile chunks mới
```

---

## §9 — DEVELOPMENT TRAJECTORY

```
🟡 DEVELOPMENT = CHUNK DENSITY TĂNG DẦN:

  Cùng architecture từ sơ sinh tới chuyên gia.
  Khác: lượng chunks tích lũy + compiled depth.

  ┌────────────┬────────────────────────────────────────────────────────┐
  │ Stage      │ Chunk state → Behavior                                 │
  ├────────────┼────────────────────────────────────────────────────────┤
  │ Newborn    │ Near-zero chunks (some prenatal compiled)              │
  │            │ → Gross reward/dissonance → cry/smile                  │
  │            │ → PFC hardware online BUT chunks missing               │
  │            │ → Pattern matching limbic (arousal contagion, NOT mirror)│
  ├────────────┼────────────────────────────────────────────────────────┤
  │ Infant     │ Proto-chunks building rapidly                          │
  │ (0-12mo)   │ → Visual arc, auditory arc, motor arc compiling       │
  │            │ → Social referencing start (6-9mo)                     │
  │            │ → Body-state discrimination improving                  │
  ├────────────┼────────────────────────────────────────────────────────┤
  │ Toddler    │ Compiled chunks + self-other distinction              │
  │ (1-3yr)    │ → Rouge test (18-24mo, Amsterdam 1972)                │
  │            │ → TRUE empathy starts (14-24mo, Warneken 2006)         │
  │            │ → Verbal labels begin → feeling detection improves    │
  │            │ → "Biết đói", "biết buồn đái" → chunks for body-state │
  ├────────────┼────────────────────────────────────────────────────────┤
  │ Child      │ Language chunks + label system                        │
  │ (3-10yr)   │ → Logic-planning enabled via verbal anchors            │
  │            │ → Complex emotions: ấm ức, ghen tị, tự hào            │
  │            │ → Theory of Mind deepening                             │
  │            │ → Cultural chunk installation accelerating             │
  ├────────────┼────────────────────────────────────────────────────────┤
  │ Teen       │ Abstract chunks + identity schemas                    │
  │ (10-18yr)  │ → "Tôi là ai", "ý nghĩa cuộc đời"                   │
  │            │ → Future planning via Imagination                      │
  │            │ → Domain specialization starting                       │
  ├────────────┼────────────────────────────────────────────────────────┤
  │ Adult      │ Deep domain chunks + nuanced feeling                  │
  │            │ → Expert intuition in practiced domains               │
  │            │ → Cross-domain linking possible                        │
  │            │ → Chunk system override hormone significantly         │
  ├────────────┼────────────────────────────────────────────────────────┤
  │ Expert     │ Deep + cross-domain → creative, accurate intuition    │
  │            │ → 50,000+ patterns (Chase & Simon 1973 chess)          │
  │            │ → Meta-chunks → PFC freed → fluid performance         │
  │            │ → Expertise = large trigger surface + novelty direction│
  │            │   (Chunk.md §4.4: trauma = same mechanism, threat dir.)│
  └────────────┴────────────────────────────────────────────────────────┘

  CRITICAL PERIODS:
    → Some baselines lock during sensitive periods
    → Native phoneme by 7-10 (Kuhl 1992)
    → Attachment style by 1-3
    → Self-signal interoception developmental foundation (early caregiving)
    → CHUNKS compiled during critical periods = especially durable + influential

  RECEPTIVE-PRODUCTIVE ASYMMETRY (Chunk.md §11.3):
    → Receptive chunk formation PRECEDES productive by ~6-12 months
    → "Hiểu" trước "làm được" = receptive compiled, productive chưa
    → Applies to ANY skill, not just language
```

---

## §10 — MULTIPLE TIMESCALES

```
🟡 CYCLE CHẠY Ở NHIỀU TIMESCALES ĐỒNG THỜI:

  ms:       L0 reflex (circuit breaker, trước unconscious)
  100ms:    Chunk activation, spreading activation, body-feedback
  seconds:  Perception-action micro-cycle, feeling emerge
  minutes:  Mood shift, state change, deliberate thinking
  hours:    Problem solving, schema update, reconsolidation window
  days:     Baseline adaptation (delta rule), habit strengthening
  weeks:    Chunk network restructuring, new skill compile
  months:   Schema restructuring, identity shift, therapy effects
  years:    Development trajectory, expertise build
  decades:  Permanent baseline calibration, critical period effects

  TẤT CẢ CHẠY ĐỒNG THỜI — không tuần tự.
  Framework phải handle tất cả timescales, không chỉ acute.
```

---

## §11 — KEY REFRAMES TỪ V7.5

```
📌 SUMMARY CÁC THAY ĐỔI SO VỚI V7.5:

  1. L2 Quality layer REMOVED (Phase R reframe 2026-04-14)
     → "Quality channels" = L1 inputs với baseline shifted by delta rule

  2. L3 Drives COLLAPSED → observation parameters
     → Novelty = positive prediction-delta pattern
     → Status = self-assessment chunks + serotonin baseline
     → Protect = loss aversion + ownership chunks
     → ALL are emergent từ body-feedback + chunks, not separate operators

  3. Schema System → Chunk-System (sole substrate)
     → Schema = observation label cho chunk network patterns
     → Analogy: features in software = observation, not architecture

  4. Layer priority (L0>L1>L2>L3) → Signal strength
     → Loudest signal wins, regardless of "layer"
     → L0 signals HAPPEN to be loudest (evolutionary design)

  5. Cross-cutting → Properties of cycle
     → Cortisol = physical mechanism (amplifier, not component)
     → Empathy = function on chunk substrate (SPM, not module)

  6. Imagine (PFC layer) → PFC (component in cycle)
     → PFC = observer + orchestrator
     → Imagination = one PFC function among several

  7. Connection (unclear position) → Solved
     → L1 multi-input aggregate + attachment chunks
     → No special component needed

  8. Feeling (implicit) → Explicit bridge
     → Feeling = interface between unconscious and PFC
     → 7-layer fidelity gradient
     → Critical position in cycle

  9. Development (unclear) → Chunk density trajectory
     → Same architecture, different chunk density
     → PFC hardware online from birth (NT4)

  10. Architecture metaphor: Layers → Cycle
      → From stack (priority ordering) to loop (continuous processing)
      → Better matches actual brain-body mechanism
```

---

## §12 — HONEST ASSESSMENT

### §12.1 Cái framework này provides

```
🟡 THEORETICAL CONTRIBUTIONS:

  → Cycle-based architecture matching actual mechanism
  → Chunk-System as sole substrate (simplification + accuracy)
  → Observation parameters replacing component taxonomy
  → PFC as observer + indirect orchestrator
  → Development as chunk density trajectory
  → Body-Feedback 2-signal model (reward/dissonance)
  → H10 5-precondition hypothesis
  → Dual-Pull architecture
  → Signal strength replacing layer priority
  → "Schema = observation label" reframe

🟢 EMPIRICAL GROUNDING:

  → 13 reference files, all compatible
  → 63,000+ dòng deep analysis across 44+ files
  → ~80 research citations across 16 topic areas
  → 15/15 case tests PASS (Phase R)
  → 50 extreme cases analyzed (Body-Base-Example.md)
  → Hall 2019 NIH = direct empirical validation
```

### §12.2 Cái framework này KHÔNG provides

```
⚠️ SCOPE LIMITS:

  → Quantitative individual baselines (descriptive only)
  → Precise adaptation rates (qualitative)
  → Clinical protocols (hypothesis generator, not treatment)
  → Biomarker specifications (architecture, not measurement)
  → Dose-response cho interventions (future + empirical work)
  → Consciousness/qualia explanation (out of scope)
```

### §12.3 Open questions

```
✅ RESOLVED (1/10):

  3. Collective architectures scope limit (Gap 3)
     → ✅ RESOLVED — Collective-Body.md v1.1 (Model 3 cấp, 1,259L)

🟡 PARTIALLY RESOLVED (5/10):

  1. Meaning cases not directly tested (B21-B23, Gap 1 từ Phase R)
     → PARTIALLY — B21-B23 tested in Body-Base-Example.md + Meaning.md v2.0 (5 types, anchor-schema)
     Remaining: Phase R original test protocol not replicated
  2. Mastery compound under-specified (Gap 2)
     → PARTIALLY — Autonomy.md §4.7 (Mastery = Competence + Autonomy compound, approach/avoidance tag)
     Remaining: quantitative accumulation thresholds
  4. Schema-body coupling via predictive processing (Gap 4)
     → PARTIALLY — Body-Coupling.md v1.1 (2D Depth×Direction, 3 Phase, compile rate mechanism)
     Remaining: underlying predictive processing neuroscience detail
  7. How exactly PFC "hold" biases spreading activation (mechanism detail)
     → PARTIALLY — PFC-Function.md ⑯ (functional level: hold → bias → cortical amplify)
     Remaining: neural circuit specifics (TRN gating, subregion projections)
  9. Whether observation parameters list is complete
     → PARTIALLY — 14 params total (+Gratitude v1.1, +Obligation v1.0 added to §8)
     Remaining: no formal closure — list may expand

🔴 STILL OPEN (4/10):

  5. Cultural specificity beyond amplification (Gap 5)
     WHERE culture acts identified (schema compilation, role, obligation types) — cross-cultural data lacking
  6. Precise boundary between L0 reflex và L1 processing
     Timescale known (ms vs 100ms) — transition mechanism = neuroscience open question
  8. Protect parameter: hormone contribution vs chunk contribution ratio
     Position: vasopressin SET bias, chunks DETERMINE expression — exact ratio unknown
     Needs: pharmacological studies + behavioral correlation
  10. Quantitative: khi nào PFC override thành công vs thất bại
     Factors identified: f(PFC hold strength, body signal intensity, compiled chunks)
     PFC-Configuration.md v1.0 maps 6 modes — quantitative thresholds missing
```

### §12.4 Number Convention

```
🟡 SỐ LIỆU TRONG FRAMEWORK = CALIBRATION ANCHOR:

  Framework dùng con số để giúp ước lượng HƯỚNG + CỠ.
  KHÔNG phải đo lường chính xác. KHÔNG phải ratio cố định.

  QUY ƯỚC:
    ~X%     = order of magnitude ("roughly this scale")
    X-Y%    = range minh họa ("biến thiên lớn, nằm trong khoảng này")
    🟢 + %  = research-backed (có citation, empirical basis)
    🟡 + %  = framework estimate (calibration anchor, không có measurement basis)

  VÍ DỤ:
    "~95% vô thức / ~5% PFC"
      → INSIGHT: phần lớn processing KHÔNG cần PFC. PFC = phần nhỏ.
      → KHÔNG PHẢI: PFC chính xác chạy 5.0% thời gian.
      → Context khác → tỷ lệ khác (§6.3: PFC 0-95% tùy dissonance level).

    "7-layer fidelity: 100% → ... → 20-70%"
      → INSIGHT: fidelity GIẢM DẦN qua processing. Drop lớn ở labeling + explanation.
      → KHÔNG PHẢI: Layer 4 luôn chính xác 85% cho tất cả mọi người.
      → Người có chunk density cao cho domain đó → fidelity cao hơn.

    "~90% Loại A / ~5% Loại B"
      → INSIGHT: PHẦN LỚN behavior = direct compiled. Expertise = phần nhỏ.
      → KHÔNG PHẢI: chính xác 90.0% behavior là Loại A.
      → Overlap A/C → không cộng thành 100% (Compile-Taxonomy.md §3).

  TẠI SAO GIỮ SỐ:
    → "Phần lớn" quá mơ hồ → không giúp calibrate
    → "~95%" cho directional anchor rõ ràng → giúp người đọc ước lượng
    → Con số = CÔNG CỤ giao tiếp, không phải claim chính xác

  TẠI SAO KHÔNG ÉP CHẶT:
    → Mỗi người khác: chunk density, hardware config (COMT, MAO-A), experience history
    → Mỗi context khác: stress level, sleep, environment, social, domain familiarity
    → Cùng mechanism, khác inputs → khác outputs → KHÔNG CÓ 1 số đúng cho tất cả

  → Đọc số trong framework = đọc HƯỚNG + CỠ, không đọc measurement.
```

---

## §13 — CROSS-REFERENCES

### §13.1 Hai bản đồ khác

```
  Core-Hardware.md              — CÁI GÌ ở ĐÂU: 4 zones A/B/C/D, PFC hardware specs, receptors
  Core-Interface.md             — QUAN SÁT + TƯƠNG TÁC: observer perspective, practical principles
```

### §13.2 Core mechanism files (đọc song song)

```
  Chunk.md v2.1               — chunk substrate, trust gate, pattern hierarchy
  Body-Feedback.md            — dual-pull, H10, 3 nguồn, cases
  Body-Feedback-Mechanism.md v1.2 — 4th axis: chunk dynamics classification
  Feeling.md v2.1             — PFC observation interface, 7-layer, Type A/B
  Agent-Mechanism.md v1.0     — agent = function on chunks, SPM + PR
  SPM.md v2.2                 — 2 Functions F1/F2, valence gate, professional SPM
  Reward-Signal-Architecture.md v1.0 — Type A/B, 5 Profiles, A Gates B, Interaction Model
  PFC-Configuration.md v1.0   — 6 dynamic modes, survival matrix, A→B transition
  PFC-Function.md v1.1        — 24 functions, confabulation, proxy trigger
  Empathy.md v2.0             — SPM applied, 2-luồng, burnout, moral injury
  Valence-Propagation.md v1.4 — body evaluation + chain + VP §4 clarification
  Cortisol-Baseline.md v2.0   — amplifier, direction gate, 7 modes
  Body-Base.md v2.0           — Model 3+1, 4-tier calibration, circuit breaker
  Compile-Taxonomy.md v1.1    — 3 Loại A/B/C, 4 pathways, 6 trade-offs
  Collective-Body.md v1.1     — Model 3 cấp, trust = only bridge, AI era
  Body-Coupling.md v1.1       — 2D Depth×Direction, L2 phenomenology
  Connection.md v3.1          — 3 Generative Primitives, 2-tầng, 2-luồng
```

### §13.3 Evidence files

```
  Body-Base-Example.md        — 50 extreme cases, cross-case synthesis
  Body-Base-Deep-Cases.md     — 2 deep cases multi-angle triangulation
  Body-Input-Enumeration.md   — 17 body-inputs, delta rule, 15/15 case test
  Feel-Example-Draft.md       — 124 feeling examples developmental
  Chunk/Child-Chunk-Development/ — 12 files, developmental arcs
```

### §13.4 Application files

```
  AI-Schema-Detection.md v2.0  — GATEWAY: 9 AI capabilities, compile type, self-drill
  Body-Personal-Optimization.md — personal tuning
  Body-Parenting-Optimization.md — parenting application
  Research/Education/           — education applications (Mechanism + Domain-Map + Empathy-Education)
  Research/Child-Development/   — child development applications (4 files v7.8-aligned)
```

### §13.5 Superseded files

```
  Core-v7.8-Draft.md v0.2       → backup (_backup/Core-v7.8-Draft-pre-3maps.md)
  Core-v7.5-Draft.md            → backup (layer-based architecture)
  Domain/backup/Object-Agent.md → replaced by Agent.md
  Core-Deep-Dive/backup/Empathy-Mirror.md → replaced by Empathy.md
  Feeling/backup/ (old files)  → replaced by v2.0 files
```

---

## Closing note

**Core-Software v1.0** — 1 trong 3 bản đồ Core v7.8.

Bản đồ phần mềm mô tả CHI TIẾT NHẤT cách body-brain system HOẠT ĐỘNG.
Cycle-based architecture emerge từ 63,000+ dòng phân tích chuyên sâu.
13/13 mechanism files compatible. Architecture stable. Detail deepens with each drill.

Muốn biết CÁI GÌ ở ĐÂU → Core-Hardware.md.
Muốn QUAN SÁT + TƯƠNG TÁC → Core-Interface.md.

> *Core-Software — "Perception-Action Cycle: Domain → Body-Input → Unconscious(Chunks) →
> Feeling → PFC → Body-Output → Domain. Chunks = sole substrate. Body-Feedback = reward
> hoặc dissonance. PFC = observer + indirect orchestrator. Schema, Drives = observation
> parameters. Development = chunk density. 3 Loại compile (A/B/C) on same substrate.
> Model 3+1 (Unconscious + PFC + Trust + Tools). Individual = Cấp 1, Collective = Cấp 2.
> Trust = only bridge. Framework iterates."*
