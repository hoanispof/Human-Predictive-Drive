# Plan: Drill 6 Health Conditions Qua Framework v7.8

> **6 chủ đề. 6 góc nhìn KHÁC NHAU của cùng kiến trúc.**
>
> Thuốc lá = dopamine HIJACK (chất bên ngoài cướp reward loop)
> Parkinson = dopamine LOSS (hardware thoái hóa dần, execution fail)
> Alzheimer = chunk system LOSS (bộ nhớ/retrieval sụp, identity tan)
> Tự kỷ = hardware CONFIGURATION KHÁC (không phải hỏng — khác cách compile)
> ADHD = CÙNG hardware, TUNING KHÁC (regulation ≠ loss ≠ hijack ≠ config)
> PTSD = chunk CONTEXT TAG MẤT (flashback = chunks fire sai context)
>
> Progression: Đơn giản → Phức tạp. Có template → Category mới → Thách thức lớn nhất.

---

## Nguyên tắc chọn: PREVALENCE + DATA HÀNH VI

```
Ưu tiên conditions PHỔ BIẾN:
  → Phổ biến hơn = nhiều data hành vi hơn = phân tích chính xác hơn
  → Ít phổ biến = chưa chắc đo lường hành vi đã đầy đủ

SKIP (và lý do):
  Chronic Pain  (1.5 tỷ nhưng SKIP) — body-input = blackbox, hardware-level phức tạp,
    framework không đủ thông tin sinh lý để drill. Chuyên gia CÓ THỂ dùng framework
    sau này nếu framework đúng, nhưng bây giờ viết = nông.
  Insomnia (750M-2B nhưng SKIP) — SYMPTOM, không phải condition. Bất kỳ bệnh nào
    (hardware tới tâm lý) đều dẫn tới mất ngủ. 1 file không cover nổi.
  Depression (280M nhưng SKIP) — compound OUTCOME, không phải mechanism riêng.
    = neural wear (cortisol chronic) + trauma + body-base buông xuôi.
    Mechanisms ĐÃ CÓ rải rác trong framework. Viết file = synthesis, ít refine mới.
  Anxiety (301M nhưng SKIP) — đã cover qua Cortisol-Baseline + Threat + Self-Created-Threat.
  Schizophrenia (24M) — prevalence thấp, data hành vi ít accessible.
  Bipolar (40M) — prevalence trung bình, oscillation mechanism phức tạp.
  Eating Disorders (30-70M) — prevalence trung bình, SPM + body hay nhưng scope hẹp.
  Phantom Limb (<10M) — niche, clean case nhưng quá nhỏ.

DRILL (6 files + 1 refine — prevalence + framework value):
  1. Nicotine/Smoking  — 1.3 TỶ người — Hijack/
  2. Parkinson          — 8.5 triệu    — Neurodegeneration/ (giữ vì dopamine contrast)
  3. ADHD               — 200-370 triệu — Neurodiversity/ (dopamine cluster)
  4. Alzheimer          — 55 triệu     — Neurodegeneration/ (bridge acetylcholine→Nicotine)
  5. Autism             — 75-80 triệu  — Neurodiversity/ (phức tạp nhất)
  6. PTSD               — 200-250 triệu — Research/ (trauma/context-tag)
  R. ADHD Refine        — sau Autism    — cập nhật config vs tuning distinction
```

---

## Thứ tự triển khai + Lý do

```
══ CLUSTER 1: DOPAMINE × 3 CƠ CHẾ (Session A-C) ══

  Cùng phân tử dopamine, 3 cơ chế HOÀN TOÀN KHÁC:
    Nicotine = SOURCE bị ÉP fire (hijack VTA)
    Parkinson = SOURCE bị CHẾT (neuron SNc thoái hóa)
    ADHD = CLEARANCE quá nhanh (DAT+COMT tại PFC)
  → Drill liền nhau = 3-way comparison table ngay khi xong

FILE 1 — Nicotine-Brain-Mechanism.md    [Hijack/]
  → Template sẵn: Alcohol-Brain-Mechanism.md v1.0 (849L)
  → Addiction-Analysis.md v3.0 = overview đã có
  → Dễ nhất: thêm 1 substance vào Hijack/ folder
  → Pathway chính: Mesolimbic (VTA→NAcc)

FILE 2 — Parkinson-Analysis.md          [Neurodegeneration/]  ← NEW FOLDER
  → Builds on File 1: dopamine HIJACK (quá nhiều) → dopamine LOSS (quá ít)
  → Contrast đẹp: cùng hệ dopamine, 2 hướng hỏng
  → Mở category mới: hardware degradation (phần cứng thoái hóa dần)
  → Pathway chính: Nigrostriatal (SNc→Striatum) + later Mesolimbic
  → Framework question: prediction model CÒN nhưng execution FAIL = gì xảy ra?

FILE 3 — ADHD-Observation.md v1.0       [Neurodiversity/]  ← NEW FOLDER
  → Builds on File 1+2: so sánh 3 cơ chế dopamine khác nhau
  → Framework ĐÃ CÓ Attention-Spectrum.md → build on top
  → Pathway chính: Mesocortical (VTA→PFC) — clearance issue
  → 3-WAY COMPARISON TABLE viết tại đây (Hijack × Loss × Tuning)
  → ⚠️ v1.0 = dopamine-focused. Sẽ REFINE sau Autism (Session R)

══ CLUSTER 2: NEURODEGENERATION + NEURODIVERSITY (Session D-E) ══

FILE 4 — Alzheimer-Analysis.md          [Neurodegeneration/]
  → Builds on File 2: Parkinson = motor/reward fail. Alzheimer = chunk/memory fail
  → Cùng "progressive degradation" nhưng HỆ THỐNG KHÁC
  → Framework question: khi chunk system TỰ NÓ hỏng = toàn bộ architecture ảnh hưởng
  → Bridge: acetylcholine link với nicotine (File 1) — cholinergic hypothesis

FILE 5 — Autism-Observation.md          [Neurodiversity/]
  → PHỨC TẠP NHẤT — KHÔNG PHẢI bệnh, là configuration khác
  → Benefit từ TẤT CẢ 4 files trước (dopamine ×3, neurodegeneration, chunk system)
  → Framework CHỈ phân tích ở những điểm CÓ KHẢ NĂNG
  → Observation file — framework observe, không chẩn đoán
  → KEY: phân biệt configuration (Autism) vs tuning (ADHD) → inform ADHD refine

══ CLUSTER 3: TRAUMA + REFINE (Session F-G) ══

FILE 6 — PTSD-Analysis.md               [Research/]
  → Builds on ALL previous: dopamine (1-3), hardware damage (2,4), chunk system (4),
    sensory processing (5), attention/executive (3) — PTSD touches ALL
  → Cortisol-Baseline.md §7 already scaffolds trauma 4-stage
  → Framework question: khi chunk RETRIEVAL mất CONTEXT TAG = flashback mechanism
  → Refine framework: chunk context-tagging (chưa formalized kỹ), amygdala role

REFINE R — ADHD-Observation.md v1.0 → v1.1   [Neurodiversity/]
  → SAU Autism (File 5) — update ADHD với:
    ① Configuration vs Tuning distinction (2-dimension neurodiversity model)
    ② Autism × ADHD co-occurrence §8 (so sánh trực tiếp, có cả 2 file)
    ③ Sensory processing overlap/difference
    ④ Framework prediction refinement
  → ADHD v1.0 (dopamine-focused) + Autism insights = ADHD v1.1 (complete)
  → Đảm bảo chất lượng ĐẦY ĐỦ NHẤT cho cả 2 file Neurodiversity
```

---

## ═══════════════════════════════════════════
## FILE 1 — Nicotine-Brain-Mechanism.md
## ═══════════════════════════════════════════

### Vị trí: Research/Health-Conditions/Hijack/Nicotine-Brain-Mechanism.md

**Tại sao Hijack/**: Nicotine = chemical hijack substance. Cùng folder với Alcohol-Brain-Mechanism.md.
Addiction-Analysis.md v3.0 = overview (đã có §0 table ghi "nicotine — drill sau nếu cần").

### Template: Alcohol-Brain-Mechanism.md (849L)

Alcohol-Brain-Mechanism.md structure → adapt cho nicotine:

```
§0 — VỊ TRÍ TRONG FRAMEWORK
§1 — NICOTINE VÀ NÃO: CƠ CHẾ TÁC ĐỘNG
  §1.1 — nAChR (nicotinic acetylcholine receptor) — receptor target
  §1.2 — Acetylcholine system bị hijack (khác alcohol: 1 hệ primary, không phải 5)
  §1.3 — VTA dopamine release pathway (mesolimbic activation)
  §1.4 — Norepinephrine + HPA axis (tỉnh táo + cortisol)
  §1.5 — So sánh: Nicotine vs Alcohol vs Opioid (single-target vs multi-system)
§2 — GRADIENT LIỀU: TỪ 1 HƠI ĐẾN CHAIN-SMOKER
  §2.1 — Liều thấp: "tỉnh táo, tập trung" (misconception lớn nhất)
  §2.2 — Liều trung: tolerance build, receptor upregulation
  §2.3 — Liều cao / chronic: baseline shift hoàn toàn
§3 — "THUỐC LÁ GIÚP TẬP TRUNG" = MISCONCEPTION
  §3.1 — Nicotine RESTORE baseline, KHÔNG enhance beyond baseline
  §3.2 — Withdrawal cognitive fog → nicotine fix fog → "tập trung hơn" = illusion
  §3.3 — Framework: prediction-delta khi có vs không có nicotine
§4 — BIẾN THỂ CÁ NHÂN
  §4.1 — CYP2A6 gene (tốc độ chuyển hóa nicotine — 3 biến thể)
  §4.2 — CHRNA5 gene (receptor sensitivity)
  §4.3 — COMT × nicotine (PFC dopamine clearance)
  §4.4 — Cortisol baseline × smoking motivation
  §4.5 — Age of first exposure (chunk compilation window)
§5 — "HÚT THUỐC" QUA CHUNK DYNAMICS
  §5.1 — Context chunks: sau cơm, khi stress, khi buồn, khi chờ
  §5.2 — Body-Coupling: ritual binding (tay cầm, miệng hít, khói thở)
  §5.3 — Social chunks: nhóm bạn hút, culture hút
  §5.4 — Identity chunks: "tôi là người hút thuốc" = SPM compiled
§6 — WITHDRAWAL = RECEPTOR UPREGULATION REBOUND
  §6.1 — Mechanism: chronic nicotine → receptor desensitization → upregulation
  §6.2 — Removal → too many EMPTY receptors → deficit signal
  §6.3 — Timeline: peak 48-72h, 2-4 tuần physical, months-years chunk triggers
  §6.4 — So sánh withdrawal Alcohol vs Nicotine (GABA/NMDA vs nAChR)
§7 — PFC + BODY IMPACT (LONG-TERM)
  §7.1 — CO (carbon monoxide) + vasoconstriction → chronic PFC oxygen reduction
  §7.2 — Body-base hardware damage (phổi, tim, mạch)
  §7.3 — Framework: body-feedback signals bị distort qua nicotine filter
§8 — NICOTINE × NEURODEGENERATION (BRIDGE TO FILE 2+3)
  §8.1 — Nicotine × Parkinson: protective association (PARADOX — nAChR stimulation)
  §8.2 — Nicotine × Alzheimer: cholinergic hypothesis link
  §8.3 — Framework interpretation: tại sao hijack ở 1 hệ có thể "protect" hệ khác
§9 — CÁC DẠNG NICOTINE DELIVERY (thuốc lá vs vape vs patch vs snus)
  §9.1 — Tốc độ delivery = tốc độ dopamine spike = mức addictive
  §9.2 — Thuốc lá: nicotine + 7000 hóa chất (TAR, CO, formaldehyde)
  §9.3 — Vape/E-cigarette: nicotine purer nhưng delivery nhanh + mới → data thiếu
  §9.4 — NRT (patch, gum): nicotine chậm, controlled = ít addictive hơn
§10 — HONEST ASSESSMENT
§11 — CROSS-REFERENCES
```

### Dependencies (đọc trước/song song)

```
PHẢI ĐỌC (core mechanism):
  ├── Addiction-Analysis.md v3.0 — overview, chunk-reward loop hijack
  ├── Dopamine-Is-Not-Reward.md v1.1 — 7-step, dopamine ≠ reward
  ├── 03-Reward.md — H10 5 preconditions, 7-step VTA
  ├── Reward-Signal-Architecture.md v1.0 — Type A/B
  ├── Reward-Calibration.md v1.1 — Goldilocks, over-reward
  └── Cortisol-Baseline.md v2.0 — stress→smoking loop

THAM KHẢO (context):
  ├── Alcohol-Brain-Mechanism.md v1.0 — template + so sánh
  ├── Body-Coupling.md v1.1 — ritual binding mechanism
  ├── PFC-Hardware.md v1.1 — COMT, individual variation
  ├── Collective-Body.md v1.1 — smoking culture
  └── Body-Feedback-Mechanism.md v1.2 — body-feedback dynamics
```

### Research cần tìm

```
🟢 Cần verify (established research):
  → nAChR receptor subtypes (α4β2, α7) — Dani & Bertrand 2007
  → VTA dopamine release via nAChR — Maskos et al. 2005
  → Receptor upregulation mechanism — Benowitz 2010
  → CYP2A6 genetic variation — Tyndale & Sellers 2002
  → Nicotine × Parkinson protective — Hernán et al. 2002 (meta-analysis)
  → Cholinergic hypothesis Alzheimer — Francis et al. 1999

🟡 Framework synthesis:
  → Chunk-reward loop hijack applied to nicotine
  → Context-chunk binding (rituals)
  → "Tập trung" misconception qua prediction-delta
  → Body-Coupling ritual binding

🔴 Hypothesis:
  → Nicotine as nAChR agonist → paradoxical neuroprotection mechanism
  → Identity chunk "tôi là người hút thuốc" × SPM × recovery
```

---

## ═══════════════════════════════════════════
## FILE 2 — Parkinson-Analysis.md
## ═══════════════════════════════════════════

### Vị trí: Research/Health-Conditions/Neurodegeneration/Parkinson-Analysis.md ← NEW FOLDER

**Tại sao folder mới**: Parkinson + Alzheimer = progressive neurodegeneration. Khác Hijack/ (external substance attack). Khác Global/ (social phenomena). Đây là category mới: HARDWARE TỰ THOÁI HÓA.

### Structure (dự kiến)

```
§0 — VỊ TRÍ TRONG FRAMEWORK
  → Category mới: Hardware Degradation (so với Hijack = external attack)
  → Đối lập Nicotine: dopamine HIJACK (quá nhiều) vs LOSS (quá ít)
§1 — PARKINSON: BỨC TRANH TỔNG QUÁT
  §1.1 — Substantia Nigra pars compacta (SNpc): dopamine neuron degeneration
  §1.2 — 60-80% loss TRƯỚC KHI triệu chứng → "silent degradation"
  §1.3 — Motor + Non-motor symptoms: tremor chỉ là bề mặt
  §1.4 — Timeline progression
§2 — FRAMEWORK MECHANISM: PREDICTION MÔ HÌNH CÒN — EXECUTION FAIL
  §2.1 — Prediction model (PFC + cortical) VẪN HOẠT ĐỘNG
  §2.2 — Motor commands KHÔNG EXECUTE ĐƯỢC (basal ganglia → motor cortex disrupted)
  §2.3 — Prediction-delta LIÊN TỤC: model predict "di chuyển" → body doesn't → mismatch
  §2.4 — "Freezing of gait" qua prediction-delta lens
  §2.5 — Bradykinesia (chậm): motor command signal WEAK, không phải ABSENT
§3 — DOPAMINE DEPLETION × FRAMEWORK ARCHITECTURE
  §3.1 — Dopamine = salience signal (Dopamine-Is-Not-Reward.md) → loss = salience detection impaired
  §3.2 — Novelty detection giảm → thế giới trở nên "phẳng", ít signal
  §3.3 — VTA pathway (mesolimbic) → anhedonia, motivation loss
  §3.4 — Nigrostriatal pathway → motor, balance
  §3.5 — Mesocortical pathway → PFC, cognition
  §3.6 — 3 pathways × framework: prediction (PFC) + execution (motor) + reward (VTA) đều impaired
§4 — NON-MOTOR: DEPRESSION + APATHY + COGNITIVE DECLINE
  §4.1 — Depression: NOT "buồn vì bệnh" → MESOLIMBIC dopamine LOSS → reward pathway degraded
  §4.2 — Apathy: drive system HARDWARE weakened (Novelty detection impaired)
  §4.3 — Cognitive decline: executive function (PFC) + attention + working memory
  §4.4 — Sleep disruption: REM behavior disorder × prediction-delta
  §4.5 — Framework: khi TOÀN BỘ dopamine system degrade → cascade effect lên architecture
§5 — LEVODOPA PARADOX
  §5.1 — Levodopa = restore dopamine → motor improvement
  §5.2 — NHƯNG: overshoot → impulse control disorders (gambling, hypersexuality, compulsive shopping)
  §5.3 — Framework interpretation: depleted system + external dopamine flood
       = giống hijack TRÊN NỀN hardware yếu
  §5.4 — Dosage Goldilocks: quá ít = motor fail, quá nhiều = impulse fail
  §5.5 — ON/OFF phenomenon: prediction model TỰ THAY ĐỔI khi medication wears off
§6 — BODY-FEEDBACK TRONG PARKINSON
  §6.1 — Body-feedback signals vẫn fire nhưng RESPONSE bị delay/distort
  §6.2 — Pain: 40-85% Parkinson patients → central pain processing change
  §6.3 — Autonomic: constipation, blood pressure, temperature → body-base signals NOISY
  §6.4 — Framework: khi body-feedback loop bị phá → calibration system mất
§7 — PARKINSON × NICOTINE (BRIDGE FILE 1→2)
  §7.1 — Nicotine = nAChR agonist → tại sao người hút thuốc ÍT Parkinson hơn
  §7.2 — nAChR stimulation → neuroprotective cho dopamine neurons?
  §7.3 — Framework: external stimulation PREVENT internal degradation?
  §7.4 — ⚠️ CORRELATION, chưa verified causation
§8 — DBS (DEEP BRAIN STIMULATION)
  §8.1 — Hardware intervention: stimulate subthalamic nucleus
  §8.2 — Framework: bypass degraded pathway bằng external signal
  §8.3 — DBS side effects: mood, speech, cognition → tradeoff lên framework architecture
§9 — SO SÁNH: HIJACK vs DEGRADATION
  §9.1 — Addiction (Hijack): external substance → reward loop bị cướp
  §9.2 — Parkinson (Degradation): internal hardware thoái hóa → reward loop bị mất
  §9.3 — Common ground: dopamine system central → cả 2 disrupt prediction-reward
  §9.4 — Key difference: Hijack = TOO MUCH wrong signal. Degradation = NOT ENOUGH signal.
§10 — HONEST ASSESSMENT
§11 — CROSS-REFERENCES
```

### Dependencies

```
PHẢI ĐỌC:
  ├── Dopamine-Is-Not-Reward.md v1.1 — CRITICAL (3 pathways)
  ├── Core-Software.md v1.0 — prediction cycle
  ├── Body-Feedback-Mechanism.md v1.2 — body-feedback dynamics
  ├── Reward-Calibration.md v1.1 — calibration disruption
  ├── Cortisol-Baseline.md v2.0 — amplifier affected
  └── Nicotine-Brain-Mechanism.md (File 1) — nicotine × Parkinson bridge

THAM KHẢO:
  ├── Addiction-Analysis.md v3.0 — hijack vs degradation comparison
  ├── PFC-Hardware.md v1.1 — PFC individual variation
  ├── Novelty.md — novelty detection (impaired in PD)
  ├── Drive.md — drive system (weakened in PD)
  └── Feeling.md v2.0 — feeling observation impaired
```

### Research cần tìm

```
🟢 Established:
  → Braak staging (α-synuclein progression) — Braak et al. 2003
  → 3 dopamine pathways — mesolimbic/nigrostriatal/mesocortical
  → Levodopa impulse control — Weintraub et al. 2010
  → DBS mechanism — Benabid et al. 2009
  → Non-motor symptoms — Chaudhuri et al. 2006
  → Depression in PD — Aarsland et al. 2012
  → Freezing of gait — Nutt et al. 2011

🟡 Framework synthesis:
  → Prediction model intact + execution fail = unique framework case
  → "Silent degradation" 60-80% → prediction-delta ACCUMULATES sub-threshold
  → Levodopa paradox = re-hijack on depleted hardware
  → Nicotine × Parkinson protective mechanism interpretation

🔴 Hypothesis:
  → Parkinson progression as chunk-system RECALIBRATION attempt
  → DBS as external prediction-delta override
```

---

## ═══════════════════════════════════════════
## FILE 3 — Alzheimer-Analysis.md
## ═══════════════════════════════════════════

### Vị trí: Research/Health-Conditions/Neurodegeneration/Alzheimer-Analysis.md

### Structure (dự kiến)

```
§0 — VỊ TRÍ TRONG FRAMEWORK
  → So sánh Parkinson (motor/reward) vs Alzheimer (memory/identity)
  → Cùng "progressive degradation" nhưng HỆ THỐNG KHÁC
§1 — ALZHEIMER: BỨC TRANH TỔNG QUÁT
  §1.1 — Amyloid plaques + Tau tangles: 2 đặc điểm bệnh lý
  §1.2 — Hippocampus → Cortex spread: progression pattern
  §1.3 — Preclinical → MCI → Mild → Moderate → Severe: giai đoạn
  §1.4 — ⚠️ Framework KHÔNG chẩn đoán hay đề xuất điều trị
§2 — FRAMEWORK MECHANISM: CHUNK SYSTEM DEGRADATION
  §2.1 — Hippocampus = chunk COMPILATION CENTER → damage = new chunks KHÔNG compile được
  §2.2 — "Quên" = chunk retrieval fail → chunk ITSELF degrade
  §2.3 — Cortical spread = COMPILED chunks bị phá dần (old memories, skills, identity)
  §2.4 — So sánh Parkinson: PD = execution fail (chunks còn). AD = chunks TỰ MẤT
  §2.5 — Anterograde (không compile mới) → Retrograde (mất cũ): 2 giai đoạn chunk loss
§3 — SPM + IDENTITY FRAGMENTATION
  §3.1 — Self-Pattern-Match PHẢI CÓ self-chunks để hoạt động
  §3.2 — Khi self-chunks degrade → SPM fail → "không biết mình là ai"
  §3.3 — NHƯNG: old deep-compiled chunks (childhood) RESIST degradation lâu hơn
  §3.4 — "Nhớ thuở nhỏ, quên hôm qua" = recent chunks (shallow compile) mất trước
  §3.5 — Framework prediction: compile DEPTH quyết định thứ tự mất
  §3.6 — Identity dissolution timeline qua SPM lens
§4 — BODY-FEEDBACK: SIGNAL CONFUSION
  §4.1 — Body-feedback signals vẫn fire → nhưng PFC KHÔNG compile được meaning
  §4.2 — Agitation, wandering, sundowning → body-feedback UNPROCESSED
  §4.3 — Pain in AD: body signals đau nhưng CAN'T REPORT/LOCATE → under-treated
  §4.4 — Framework: body-base STILL ALIVE nhưng software layer COLLAPSING
§5 — CONNECTION: CAREGIVER + PATIENT
  §5.1 — Patient: Connection chunks degrade → không nhận ra người thân
  §5.2 — Caregiver: SPM run → nhưng RESPONSE KHÔNG ĐẾN → Connection frustration
  §5.3 — "Ambiguous loss" (Boss 2000): person physically present, psychologically absent
  §5.4 — Framework: Body-Coupling DISRUPTED one-sided (caregiver still coupled, patient decoupling)
  §5.5 — Caregiver burnout: L1 drain without L2 reciprocation → sustainable impossible
§6 — ACETYLCHOLINE + CHOLINERGIC HYPOTHESIS
  §6.1 — Acetylcholine system degraded (basal forebrain cholinergic neurons)
  §6.2 — Cholinesterase inhibitors: boost remaining acetylcholine
  §6.3 — BRIDGE to File 1: Nicotine = acetylcholine receptor agonist → protective association
  §6.4 — Framework: acetylcholine × chunk compilation? (hypothesis)
§7 — PROGRESSION MODEL QUA FRAMEWORK
  §7.1 — Stage 1: Hippocampal → anterograde amnesia (cannot form new chunks)
  §7.2 — Stage 2: Temporal/Parietal → language + spatial chunks degrade
  §7.3 — Stage 3: Frontal → PFC functions offline → personality changes
  §7.4 — Stage 4: Global → body-base regulation fails → death
  §7.5 — Framework mapping: chunk system → observation parameters → drives → body-base
  §7.6 — "Regression": skills lost in REVERSE ORDER of acquisition (last in, first out)
§8 — SO SÁNH: PARKINSON vs ALZHEIMER
  §8.1 — Dopamine vs Acetylcholine (primary system affected)
  §8.2 — Execution fail vs Memory fail
  §8.3 — Motor symptoms vs Cognitive symptoms (early)
  §8.4 — Identity preserved (PD) vs Identity fragmented (AD)
  §8.5 — Common: progressive, neurodegenerative, body-feedback disrupted
  §8.6 — Framework unifying: cả 2 = hardware degradation → cascade effect lên architecture
§9 — MUSIC + PROCEDURAL MEMORY PRESERVATION
  §9.1 — Music recognition RESIST degradation (deep compile + distributed storage)
  §9.2 — Procedural skills RESIST (different pathway — cerebellum + basal ganglia)
  §9.3 — Framework: compile DEPTH + DISTRIBUTION = resistance to degradation
  §9.4 — Music therapy: activates PRESERVED pathways → temporary connection restoration
§10 — HONEST ASSESSMENT
§11 — CROSS-REFERENCES
```

### Dependencies

```
PHẢI ĐỌC:
  ├── Self-Pattern-Match.md v2.3 — SPM + identity (critical)
  ├── Chunk.md v2.1 — chunk substrate, compilation
  ├── Connection.md v3.1 — connection mechanism (caregiver analysis)
  ├── Body-Feedback-Mechanism.md v1.2 — signal confusion
  ├── Parkinson-Analysis.md (File 2) — comparison
  └── Nicotine-Brain-Mechanism.md (File 1) — acetylcholine bridge

THAM KHẢO:
  ├── Empathy.md v2.0 — caregiver empathy dynamics
  ├── Meaning.md v2.0 — identity anchor dissolution
  ├── Body-Coupling.md v1.1 — one-sided decoupling
  ├── Protect.md v1.0 — ownership + loss aversion (caregiver)
  ├── Gap-Direction.md v1.0 — "quên" = gap KHÔNG CÓ HƯỚNG
  └── Feeling.md v2.0 — feeling observation impaired
```

### Research cần tìm

```
🟢 Established:
  → Braak staging Alzheimer — Braak & Braak 1991
  → Hippocampal atrophy — Jack et al. 2010
  → Cholinergic hypothesis — Bartus et al. 1982
  → Ambiguous loss — Boss 1999, 2000
  → Music preservation — Jacobsen et al. 2015
  → Procedural memory preservation — Reber 2013
  → Caregiver burden — Brodaty & Donkin 2009
  → Retrograde temporal gradient (Ribot's Law)

🟡 Framework synthesis:
  → Chunk compilation depth × degradation resistance
  → SPM dissolution as identity mechanism
  → Body-base alive + software collapsing = framework unique case
  → Caregiver: L1/L2 asymmetry → burnout mechanism

🔴 Hypothesis:
  → "Last in first out" compile depth prediction
  → Music resistance = compile depth + distribution hypothesis
  → Acetylcholine × chunk compilation role
```

---

## ═══════════════════════════════════════════
## FILE 4 — Autism-Observation.md
## ═══════════════════════════════════════════

### Vị trí: Research/Health-Conditions/Neurodiversity/Autism-Observation.md ← NEW FOLDER

**Tại sao "Observation" không phải "Analysis"**: Framework QUAN SÁT autism qua lens kiến trúc. 
KHÔNG đủ cơ sở để "analyze" toàn diện — cần empirical per-individual measurement.
KHÔNG phải bệnh → KHÔNG đặt cạnh Neurodegeneration.

**Tại sao folder Neurodiversity/**: Tự kỷ = hardware configuration khác, KHÔNG phải hỏng. 
Folder riêng thể hiện framing đúng.

### Scope: Chỉ phân tích ở những điểm framework CÓ KHẢ NĂNG

```
FRAMEWORK CÓ THỂ PHÂN TÍCH:
  ✅ Sensory processing differences → cascading effect lên chunk compilation
  ✅ SPM development: F1/F2 balance khác → social interaction khác
  ✅ Multisensory integration differences → chunk compilation pathway
  ✅ Special interests qua gap-direction + reward mechanism
  ✅ Predictability preference qua prediction-delta lens
  ✅ Alexithymia overlap: body-feedback reading vs body-feedback HAVING
  ✅ Phân loại framework: các dimensions mà autism differ
  ✅ Developmental trajectory qua child-dev mechanism
  ✅ Social chunk compilation: khác timeline, khác pathway
  ✅ Meltdown/shutdown qua body-feedback overload lens

FRAMEWORK KHÔNG THỂ:
  ❌ Chẩn đoán (clinical, ngoài scope)
  ❌ Xác định nguyên nhân gen/epigenetic cụ thể
  ❌ Đề xuất "điều trị" (không phải bệnh để trị)
  ❌ Predict per-individual presentation từ general mechanism
  ❌ Thay thế clinical assessment
```

### Structure (dự kiến)

```
§0 — VỊ TRÍ TRONG FRAMEWORK
  → KHÁC BIỆT với Neurodegeneration (không phải thoái hóa)
  → KHÁC BIỆT với Hijack (không phải chất bên ngoài)
  → Configuration khác từ đầu → cascade khác → outcome khác
  → ⚠️ Framework OBSERVE, không chẩn đoán, không "chữa"
§1 — AUTISM: FRAMING
  §1.1 — Spectrum, không phải binary (DSM-5 ASD: Level 1/2/3)
  §1.2 — Tại sao "disorder" = problematic: framework nhìn = CONFIGURATION
  §1.3 — Heterogeneity: mỗi autistic person = unique combination
  §1.4 — Co-occurring conditions: alexithymia, ADHD, anxiety → overlapping mechanisms
§2 — SENSORY PROCESSING × CHUNK COMPILATION
  §2.1 — Hyper/Hypo sensitivity: input GAIN khác nhau per-modality
  §2.2 — Framework: sensory input = raw material for chunk compilation
       → khác input GAIN = khác raw material = khác compiled chunks
  §2.3 — Sensory overload: quá nhiều high-gain input ĐỒNG THỜI
       → body-feedback overwhelm → meltdown/shutdown
  §2.4 — Sensory seeking: hypo input cần MÔI TRƯỜNG stimulation cao hơn
  §2.5 — Framework prediction: sensory profile → predict chunk compilation bias
  §2.6 — Cross-ref: Sensitivity-Classification.md (sensor × processing 2-layer)
§3 — MULTISENSORY INTEGRATION
  §3.1 — Mainstream: multisensory integration differences (Stevenson et al. 2014)
  §3.2 — Framework: 07-Social-Recognition-Arc.md §6 — 4 binding mechanisms
       → nếu 1+ mechanism DIFFERENT (không phải absent) → binding pattern khác
  §3.3 — Temporal binding window wider/narrower → cross-modal chunk compilation khác
  §3.4 — Social input = inherently multi-modal → integration difference
       = social chunk compilation cascade difference
  §3.5 — Framework prediction: integration difference magnitude
       → predict social difficulty magnitude (testable hypothesis)
§4 — SPM DEVELOPMENT: F1/F2 BALANCE
  §4.1 — F1 (feeling simulation) vs F2 (logic prediction): 2 functions của SPM
  §4.2 — Observation: nhiều autistic people có F2 STRONG (logic, pattern, system)
       nhưng F1 DIFFERENT (not absent — different pathway)
  §4.3 — "Thiếu empathy" = MISCONCEPTION → F1 path KHÁC, không phải F1 ABSENT
  §4.4 — Double empathy problem (Milton 2012): non-autistic CŨNG fail SPM autistic people
  §4.5 — Framework: F1/F2 balance ≠ fixed → CÓ THỂ PHÁT TRIỂN, nhưng pathway khác
  §4.6 — Masking: compile "social protocol" chunks (Type C) để hoạt động trong NT world
       → body-feedback cost (Cortisol-Baseline.md — chronic mismatch)
§5 — SPECIAL INTERESTS × GAP-DIRECTION
  §5.1 — Special interests ≠ "fixation" (pathology framing) = INTENSE GAP-DIRECTION FOCUS
  §5.2 — Gap-Direction.md: gap has direction = f(surrounding chunks)
  §5.3 — Autistic special interest: gap-direction CONCENTRATED into narrow domain
       → extreme depth (Type A compile) → deep expertise possible
  §5.4 — Reward system: H10 met in special interest domain → genuine reward
  §5.5 — KHÁC OCD: OCD = "done" pipeline fail (loop). Special interest = genuine gap fill (reward)
  §5.6 — Framework: special interest = architecture FEATURE, không phải bug
§6 — PREDICTABILITY × PREDICTION-DELTA
  §6.1 — Preference for predictability, routine, sameness
  §6.2 — Framework hypothesis: prediction-delta THRESHOLD lower?
       OR prediction-delta AMPLIFIED? (2 possible mechanisms)
  §6.3 — Change = large prediction-delta → larger body-feedback response → distress
  §6.4 — Routine = reduce prediction-delta → reduce body-feedback load → regulation
  §6.5 — Framework: tương tự "cortisol baseline HIGH" nhưng cơ chế khác
       (sensory gain + prediction sensitivity, không phải cortisol pathway)
  §6.6 — KHÔNG ĐỦ DỮ LIỆU: cần EEG/fMRI per-individual to distinguish mechanisms
§7 — ALEXITHYMIA: BODY-FEEDBACK READING vs HAVING
  §7.1 — ~50% autistic people have alexithymia (nhưng alexithymia ≠ autism)
  §7.2 — Body-feedback signals VẪN FIRE (body-base alive)
  §7.3 — READING signals khó → chunking body-feedback into labels khó
  §7.4 — Framework: Feeling.md v2.0 — "feeling = PFC observation of body-feedback"
       → alexithymia = OBSERVATION difficulty, not SIGNAL difficulty
  §7.5 — Cross-ref: Somatic-Articulation-Loop.md — body knowledge without words
  §7.6 — ⚠️ alexithymia NOT autism-specific (exists in non-autistic too)
§8 — DEVELOPMENTAL TRAJECTORY
  §8.1 — Child-Development-Mechanism.md: 4+1 channel compile
  §8.2 — Autistic development: channels compile at DIFFERENT rates/intensities
  §8.3 — Social Recognition Arc (07): gaze following, social smile timing → different
  §8.4 — Language development: wide range (non-verbal → hyperlexia)
  §8.5 — Motor development: often delayed (vestibular + proprioceptive differences)
  §8.6 — Framework: KHÔNG "delayed" — DIFFERENT PATHWAY, different timeline
§9 — MELTDOWN/SHUTDOWN QUA BODY-FEEDBACK LENS
  §9.1 — Meltdown: body-feedback OVERLOAD → PFC offline → motor/emotional discharge
  §9.2 — Shutdown: body-feedback OVERLOAD → PFC WITHDRAWAL → freeze/collapse
  §9.3 — Framework: giống Threat.md NE cascade → PFC disconnect
       nhưng trigger = SENSORY + PREDICTION-DELTA, không nhất thiết threat
  §9.4 — Recovery: body-feedback must DRAIN before PFC re-engage
  §9.5 — Stimming: REGULATION mechanism → reduce body-feedback load
       (giống Fidgeting-Analysis.md nhưng stronger → greater regulation need)
§10 — FRAMEWORK PREDICTIONS (TESTABLE)
  §10.1 — Sensory profile → predict chunk compilation bias (testable)
  §10.2 — Integration window → predict social difficulty magnitude (testable)
  §10.3 — F1/F2 balance → predict social interaction style (testable)
  §10.4 — Special interest pattern → predict reward mechanism engagement (testable)
  §10.5 — Prediction-delta threshold → predict predictability preference intensity (testable)
  §10.6 — ⚠️ ALL predictions = HYPOTHESIS — cần empirical validation per-individual
§11 — HONEST ASSESSMENT
  → Framework CAN: provide observation lens, generate testable hypotheses
  → Framework CANNOT: diagnose, prescribe, replace clinical assessment
  → Confidence: mostly 🟡 (synthesis) and 🔴 (hypothesis)
  → Tự kỷ = MOST COMPLEX topic — mỗi individual = unique configuration
§12 — CROSS-REFERENCES
```

### Dependencies

```
PHẢI ĐỌC:
  ├── Self-Pattern-Match.md v2.3 — F1/F2, valence, context-dependent
  ├── Body-Feedback-Mechanism.md v1.2 — overload, dynamics
  ├── Sensitivity-Classification.md v1.0 — sensor × processing 2-layer
  ├── 07-Social-Recognition-Arc.md — social development + binding mechanisms
  ├── Child-Development-Mechanism.md v1.0 — developmental baseline
  ├── Feeling.md v2.0 — alexithymia link (PFC observation interface)
  └── Gap-Direction.md v1.0 — special interests

THAM KHẢO:
  ├── Fidgeting-Analysis.md v1.0 — stimming comparison
  ├── OCD-Analysis.md v2.1 — special interest vs OCD distinction
  ├── Threat.md — meltdown/shutdown NE cascade
  ├── Cortisol-Baseline.md v2.0 — masking cost
  ├── By-Product-Gap-Resonance.md — social resonance differences
  ├── Empathy.md v2.0 — double empathy problem
  ├── Somatic-Articulation-Loop.md — body knowledge without words
  ├── Connection.md v3.1 — social connection differences
  └── Parkinson + Alzheimer (File 2+3) — degradation vs configuration distinction
```

### Research cần tìm

```
🟢 Established:
  → DSM-5 ASD criteria — APA 2013
  → Sensory processing — Marco et al. 2011, Baranek 2002
  → Multisensory integration — Stevenson et al. 2014, Foss-Feig et al. 2010
  → Double empathy — Milton 2012
  → Alexithymia overlap — Kinnaird et al. 2019 (50% prevalence)
  → Masking/camouflaging — Hull et al. 2017
  → Special interests — Grove et al. 2018

🟡 Framework synthesis:
  → Sensory gain → chunk compilation cascade
  → F1/F2 balance reframe (not deficit — different)
  → Meltdown/shutdown as body-feedback overload
  → Stimming as regulation (not pathology)
  → Special interest as gap-direction feature

🔴 Hypothesis:
  → Prediction-delta threshold/amplification
  → Compile depth correlation with interest intensity
  → Integration window → social difficulty magnitude
```

---

## ═══════════════════════════════════════════
## FILE 5 — ADHD-Observation.md
## ═══════════════════════════════════════════

### Vị trí: Research/Health-Conditions/Neurodiversity/ADHD-Observation.md

**Tại sao "Observation"**: Giống Autism — framework OBSERVE qua lens, không chẩn đoán.
**Tại sao Neurodiversity/**: ADHD = different regulation, không phải bệnh cần "chữa".
ADHD co-occur ~30-50% với Autism → cùng folder = so sánh trực tiếp.

**QUAN TRỌNG: Attention-Spectrum.md ĐÃ CÓ**
Framework đã có Attention-Spectrum.md v2.0 tại Core-Deep-Dive/PFC/:
  §1 — Multi-Factor Model (COMT + chunk threshold + NE + cortisol)
  §3 — Hyperfocus: Threshold cao = Noise Cancelling
  §5 — Methylphenidate (Ritalin) mechanism
  "ADHD = spectrum, not binary"
→ ADHD-Observation.md build ON TOP, KHÔNG duplicate. Reference Attention-Spectrum cho foundations.

### Scope: Những gì Attention-Spectrum CHƯA cover

```
ATTENTION-SPECTRUM ĐÃ CÓ (reference, không lặp):
  ✅ Multi-factor attention model
  ✅ Hyperfocus mechanism
  ✅ Methylphenidate (Ritalin) brief
  ✅ Classroom × spectrum
  ✅ AI era × attention

ADHD-OBSERVATION THÊM (new value):
  ✅ DAT (dopamine transporter) chi tiết — TẠI SAO regulation khác
  ✅ Executive function BEYOND attention (planning, time, working memory)
  ✅ Emotional dysregulation (RSD — rejection sensitive dysphoria)
  ✅ Time perception differences (time blindness qua prediction-delta)
  ✅ ADHD × lifespan: child → adult trajectory
  ✅ ADHD × Autism co-occurrence: overlap vs distinction
  ✅ ADHD × other conditions: anxiety, depression, OCD
  ✅ Medication deep-dive (Methylphenidate + Amphetamine + non-stimulant)
  ✅ Framework unique: "deficit" reframe → regulation TUNING khác

FRAMEWORK KHÔNG THỂ:
  ❌ Chẩn đoán (clinical, DSM-5 criteria = y khoa)
  ❌ Prescribe medication (outside scope)
  ❌ Determine per-individual cause
```

### Structure (dự kiến)

```
§0 — VỊ TRÍ TRONG FRAMEWORK
  → Build on Attention-Spectrum.md (reference, không lặp)
  → KHÁC Autism (config) vs ADHD (tuning): phân biệt rõ
  → ⚠️ Framework OBSERVE, không chẩn đoán
§1 — ADHD: REFRAME
  §1.1 — "Attention Deficit" = MISNOMER: không thiếu attention, REGULATE khác
  §1.2 — DSM-5 3 presentations: Inattentive / Hyperactive-Impulsive / Combined
  §1.3 — Prevalence: ~5-7% children, ~2.5-4% adults (KHÔNG "hết" khi trưởng thành)
  §1.4 — Framework framing: ADHD = attention regulation TUNING trên spectrum liên tục
§2 — NEUROCHEMISTRY: DAT + DOPAMINE REGULATION
  §2.1 — DAT (dopamine transporter) density → dopamine clearance speed
  §2.2 — Higher DAT → faster clearance → dopamine signal SHORTER
       → cần stimulus MẠNH HƠN để duy trì attention = novelty-seeking
  §2.3 — Norepinephrine regulation → PFC sustained attention (Arnsten 2009)
  §2.4 — KHÁC Parkinson: Parkinson = neuron CHẾT. ADHD = neuron CÒN, regulation KHÁC
  §2.5 — KHÁC Nicotine hijack: substance ADD dopamine. ADHD = endogenous CLEARANCE nhanh
  §2.6 — 3-way comparison table: Hijack × Loss × Tuning
§3 — EXECUTIVE FUNCTION BEYOND ATTENTION
  §3.1 — Working memory: hold fewer items actively → PFC-Hold-Dimensions.md link
  §3.2 — Planning + sequencing: multi-step task chunking difficulty
  §3.3 — Inhibition: response inhibition ≠ "self-control" → mechanism khác
  §3.4 — Task switching: HYPER task-switching (novelty-driven) vs HYPO sustained
  §3.5 — Framework: PFC-Configuration.md Mode ① Normal → ADHD = Mode ① UNSTABLE
       → drift toward Mode ② hoặc sub-threshold Mode ④ quickly
§4 — EMOTIONAL DYSREGULATION
  §4.1 — RSD (Rejection Sensitive Dysphoria) — emotional response AMPLIFIED
  §4.2 — Framework: prediction-delta AMPLIFIED for social signals
       → small rejection → large body-feedback → large reaction
  §4.3 — Emotional regulation = PFC function ⑧ (Emotional regulation) — under-fueled
  §4.4 — NOT "immaturity" — HARDWARE regulation difference
  §4.5 — Connection to Cortisol-Baseline: emotional events → cortisol CASCADE faster
§5 — TIME PERCEPTION: TIME BLINDNESS
  §5.1 — "Time blindness" = subjective time perception different
  §5.2 — Framework hypothesis: prediction model TIME RESOLUTION lower
       → future predictions LESS GRANULAR → deadlines "suddenly" arrive
  §5.3 — Hyperfocus = time perception COLLAPSES (no prediction-delta for time passing)
  §5.4 — NOW vs NOT-NOW: binary time model (Russell Barkley's framework, connects to ours)
§6 — HYPERFOCUS × GAP-DIRECTION
  §6.1 — Reference: Attention-Spectrum.md §3 (foundation, không lặp)
  §6.2 — THÊM: Hyperfocus = gap-direction + H10 met + prediction-delta suppressed for OTHER
  §6.3 — Framework: hyperfocus = PFC FULLY ENGAGED nhưng NARROW
       → Config ② Flow (task-serving ON, self-monitoring OFF)
  §6.4 — Paradox giải quyết: "Không tập trung" nhưng hyperfocus 6 giờ
       = cùng mechanism, khác trigger threshold
§7 — ADHD × LIFESPAN
  §7.1 — Childhood: hyperactivity visible → diagnosis easier
  §7.2 — Adolescent: internalize → "lazy" label → identity chunk damage
  §7.3 — Adult: compensation strategies compiled → nhưng COST (cortisol chronic)
  §7.4 — Late diagnosis: "Ah, tất cả explained" → identity chunk RE-COMPILE
  §7.5 — Framework: SPM self-chunks shift khi diagnosis → can be relief OR crisis
§8 — ADHD × AUTISM: CO-OCCURRENCE
  §8.1 — ~30-50% co-occur — WHY? (shared mechanism? adjacent on spectrum?)
  §8.2 — Overlap: sensory processing, executive function, social difficulty
  §8.3 — Distinction: Autism = social chunk compile KHÁC. ADHD = attention REGULATE khác
  §8.4 — Framework: 2 DIMENSIONS (Configuration × Tuning) — CÓ THỂ overlap
  §8.5 — Table: Autism vs ADHD vs Both — feature comparison qua framework
§9 — MEDICATION MECHANISM QUA FRAMEWORK
  §9.1 — Methylphenidate: block DAT → dopamine stays LONGER → PFC gets enough fuel
  §9.2 — Amphetamine: REVERSE DAT → push dopamine OUT → more available
  §9.3 — Non-stimulant (Atomoxetine): block NET → norepinephrine stays longer → PFC sustain
  §9.4 — Paradox: stimulant CALMS ADHD → framework: PFC UNDER-FUELED →
       add fuel → PFC CAN SUSTAIN → regulation POSSIBLE → calmer output
  §9.5 — Medication ≠ cure → COMPENSATE hardware tuning, không thay đổi tuning
  §9.6 — Reference: Attention-Spectrum.md §5 (foundation)
§10 — FRAMEWORK PREDICTIONS (TESTABLE)
  §10.1 — DAT density → predict attention sustainability (testable via PET)
  §10.2 — Emotional amplification magnitude → predict RSD severity (testable)
  §10.3 — Time perception resolution → predict deadline management (testable)
  §10.4 — Hyperfocus trigger profile → predict domain engagement (testable)
  §10.5 — ⚠️ ALL predictions = HYPOTHESIS — cần empirical validation
§11 — HONEST ASSESSMENT
§12 — CROSS-REFERENCES
```

### Dependencies

```
PHẢI ĐỌC:
  ├── Attention-Spectrum.md v2.0 — FOUNDATION (không lặp, reference)
  ├── PFC-Hardware.md v1.1 — COMT, DRD4, NE receptors
  ├── PFC-Configuration.md v1.0 — 6 modes, mode drift
  ├── Dopamine-Is-Not-Reward.md v1.1 — dopamine = salience
  ├── Body-Feedback-Mechanism.md v1.2 — prediction-delta
  ├── Autism-Observation.md (File 4) — configuration vs tuning distinction
  └── Gap-Direction.md v1.0 — hyperfocus × gap-direction

THAM KHẢO:
  ├── PFC-Function.md — 24 functions (which under-fueled in ADHD)
  ├── PFC-Hold-Dimensions.md — ~4±1 slots, working memory
  ├── Cortisol-Baseline.md v2.0 — emotional cascade
  ├── Self-Pattern-Match.md v2.3 — identity chunks, late diagnosis
  ├── Reward-Calibration.md v1.1 — reward threshold
  ├── Novelty.md — novelty-seeking mechanism
  └── OCD-Analysis.md v2.1 — ADHD × OCD distinction (both involve executive)
```

### Research cần tìm

```
🟢 Established:
  → DAT density and ADHD — Spencer et al. 2005 (PET imaging)
  → Methylphenidate mechanism — Volkow et al. 2001, 2012
  → ADHD executive function — Barkley 1997 (executive function model)
  → Emotional dysregulation — Shaw et al. 2014
  → ADHD + Autism co-occurrence — Rommelse et al. 2010
  → ADHD adult persistence — Faraone et al. 2006
  → RSD — Dodson 2005 (clinical observation, limited formal research)
  → Arnsten 2009 — PFC catecholamine modulation

🟡 Framework synthesis:
  → DAT clearance speed → prediction-delta duration → attention sustain
  → Hyperfocus = Config ② Flow triggered by high gap-direction
  → RSD = prediction-delta AMPLIFIED for social → body-feedback cascade
  → Time blindness = prediction model temporal resolution hypothesis
  → Config vs Tuning: 2-dimension neurodiversity model

🔴 Hypothesis:
  → Time perception as prediction temporal resolution
  → 2D neurodiversity model (Configuration × Regulation Tuning)
  → Late diagnosis identity re-compilation mechanism
```

---

## ═══════════════════════════════════════════
## FILE 6 — PTSD-Analysis.md
## ═══════════════════════════════════════════

### Vị trí: Research/PTSD-Analysis.md

**Tại sao Research/ root (không sub-folder)**: PTSD = standalone analysis, giống OCD-Analysis.md.
Không đủ files cho riêng 1 folder "Trauma/". Nếu sau này drill thêm (Complex-PTSD, Developmental Trauma)
→ tạo folder + move.

**Cortisol-Baseline.md §7 ĐÃ SCAFFOLD**: Trauma 4-stage (acute → chronic → PTSD → complex).
PTSD-Analysis.md drill SÂU HƠN mechanism, đặc biệt CHUNK CONTEXT-TAGGING.

### Tại sao file này refine framework

```
FRAMEWORK CẦN FORMALIZE:
  🔴 Chunk context-tagging mechanism — CHƯA formalized kỹ
     → PTSD = case chunks fire WITHOUT context = buộc framework giải thích
  🔴 Amygdala role in chunk storage — CHƯA drill chi tiết
     → PTSD: trauma chunks stored via amygdala (fast, no context)
     vs hippocampus (slow, with context) → 2 pathways cần formalize
  🟡 Body > PFC in extreme cases — framework nói body-first nhưng PTSD
     = EXTREME case: PFC BIẾT "an toàn" nhưng body KHÔNG NGHE
     → cần formalize tại sao và khi nào body completely override PFC
```

### Structure (dự kiến)

```
§0 — VỊ TRÍ TRONG FRAMEWORK
  → Builds on Cortisol-Baseline.md §7 trauma 4-stage (reference)
  → Category: chunk context-tag failure (not degradation, not hijack, not config)
  → ⚠️ Framework KHÔNG thay thế trauma therapy — observation lens only
§1 — PTSD: BỨC TRANH TỔNG QUÁT
  §1.1 — DSM-5 criteria: re-experiencing, avoidance, negative cognition, hyperarousal
  §1.2 — Prevalence: ~6-7% lifetime (US), ~3.9% global
  §1.3 — PTSD ≠ "yếu đuối": hardware response, không phải personality
  §1.4 — Not all trauma → PTSD (~20-30% of trauma-exposed develop PTSD)
§2 — CORE MECHANISM: CHUNK CONTEXT-TAG FAILURE
  §2.1 — Normal memory: hippocampus encodes EVENT + CONTEXT + TIME TAG
       → chunk compile WITH context → retrieval = context-appropriate
  §2.2 — Traumatic memory: amygdala hijack encoding
       → extreme NE + cortisol → hippocampus SUPPRESSED → amygdala DOMINANT
       → chunk compile WITHOUT context tag (or WEAK context tag)
  §2.3 — Result: trauma chunk = VIVID body-feedback + ABSENT context
       → trigger (sensory match) → chunk fires → body RESPONDS as if IN trauma
       → PFC knows "hiện tại" but body is "ở quá khứ"
  §2.4 — Framework formalization: CONTEXT TAG = metadata attached to chunk
       → trauma = metadata STRIPPED or CORRUPTED
  §2.5 — Why trauma memories VIVID: emotional peak → opioid/NE → DEEP compile
       → paradox: DEEPLY compiled but POORLY contextualized
§3 — FLASHBACK QUA CHUNK DYNAMICS
  §3.1 — Trigger: sensory input MATCHES trauma chunk (mùi, tiếng, hình, xúc giác)
  §3.2 — Chunk-Miss: current sensory → trauma chunk fire → MISMATCH with current reality
  §3.3 — Body-feedback: body PRODUCES full trauma response
       (heart rate, muscle tension, cortisol, adrenaline)
  §3.4 — PFC: KNOWS "this is a memory" → but body-feedback OVERRIDES
  §3.5 — Framework: body-first invariant (Feeling-Mechanism-Deep.md)
       → in PTSD, body-first = BODY WINS over PFC every time
  §3.6 — Dissociation: khi body-feedback TOO INTENSE → PFC-Configuration ⑤ Dissociated
       → emotional numbness = DEFENSE, not "not caring"
§4 — HIPPOCAMPUS × AMYGDALA: 2 ENCODING PATHWAYS
  §4.1 — Hippocampus: declarative, contextual, explicit, slow, malleable
  §4.2 — Amygdala: emotional, non-contextual, implicit, fast, RESISTANT to change
  §4.3 — Normal: both work together → integrated memory (fact + feeling + context)
  §4.4 — Trauma: cortisol SUPPRESSES hippocampus → amygdala ALONE encodes
       → feeling WITHOUT fact, body-feedback WITHOUT context
  §4.5 — Framework contribution: 2 encoding pathways = 2 CHUNK TYPES
       → contextual chunks (hippocampal) vs context-free chunks (amygdala)
       → PTSD = over-reliance on context-free chunks for threat detection
  §4.6 — Hippocampal volume reduction in PTSD (Bremner 2006) →
       hardware DAMAGE from chronic cortisol → further impairs contextual encoding
       → cross-ref Alzheimer §2.1 (hippocampus damage → chunk compilation impaired)
§5 — HYPERAROUSAL: CORTISOL BASELINE SHIFT
  §5.1 — Reference: Cortisol-Baseline.md §7 (foundation, không lặp)
  §5.2 — THÊM: HPA axis RECALIBRATED → threat baseline PERMANENTLY SHIFTED
  §5.3 — Hypervigilance: prediction model SET TO "threat expected"
       → prediction-delta for NEUTRAL events → body-feedback fires for safe situations
  §5.4 — Startle response AMPLIFIED: NE α1 threshold LOWERED
       → PFC-Hardware.md §6 NE circuit breaker → fires TOO EASILY
  §5.5 — Sleep: REM processing DISRUPTED → chunks CANNOT re-contextualize
       → Background-Pattern.md: sleep = chunk compile + prune → PTSD sleep = failed processing
§6 — AVOIDANCE: BEHAVIORAL + EMOTIONAL
  §6.1 — Behavioral avoidance: avoid TRIGGERS → avoid chunk firing
  §6.2 — Emotional avoidance: numbing, dissociation → PFC-Config ⑤
  §6.3 — Framework: avoidance = LOGICAL response to body-feedback pain
       → NOT "avoiding healing" — avoiding BODY PAIN
  §6.4 — Cost: avoidance NARROWS life → Imagine-Final shrinks → meaning dissolves
  §6.5 — PTSD + depression: avoidance → reward system UNUSED → anhedonia
§7 — TREATMENT MECHANISMS QUA FRAMEWORK LENS
  §7.1 — Exposure therapy: controlled chunk retrieval + NEW context tag attachment
       → hippocampus RE-ENCODES trauma chunk WITH safe context
  §7.2 — EMDR: bilateral stimulation → reduce amygdala activation during retrieval
       → allow hippocampal REPROCESSING → context tag ADDED
  §7.3 — CPT (Cognitive Processing Therapy): PFC REFRAMES trauma chunks
       → not changing body-feedback, but adding PFC INTERPRETATION layer
  §7.4 — Medication (SSRI): serotonin → reduce body-feedback AMPLITUDE
       → enough space for PFC to engage during retrieval
  §7.5 — Framework unifying: ALL treatments = help hippocampus ADD context to trauma chunks
       → chunk ITSELF doesn't change → CONTEXT TAG changes → body-feedback changes
  §7.6 — ⚠️ Framework ĐỀ XUẤT mechanism, KHÔNG prescribe treatment
§8 — COMPLEX PTSD (C-PTSD)
  §8.1 — Repeated, prolonged trauma (childhood abuse, captivity, war)
  §8.2 — KHÁC single-event PTSD: self-concept disrupted, emotional regulation impaired,
       interpersonal difficulties
  §8.3 — Framework: C-PTSD = DEVELOPMENTAL chunk compilation under CHRONIC THREAT
       → SPM compiled UNDER threat → self-chunks = threat-organized
       → Cross-ref Child-Development-Mechanism.md §8 (Cortisol × phát triển)
  §8.4 — Recovery = SPM RE-COMPILATION (not just adding context to 1 event)
       → much longer, much harder
§9 — PTSD × OTHER CONDITIONS
  §9.1 — PTSD × Depression: avoidance → anhedonia → compound
  §9.2 — PTSD × Addiction: substance = body-feedback SUPPRESSION tool
       → cross-ref Addiction-Analysis.md §8 Self-medication
  §9.3 — PTSD × ADHD: hyperarousal MIMICS ADHD symptoms → misdiagnosis risk
  §9.4 — PTSD × Parkinson: chronic cortisol → potential neurodegeneration pathway?
§10 — HONEST ASSESSMENT
§11 — CROSS-REFERENCES
```

### Dependencies

```
PHẢI ĐỌC:
  ├── Cortisol-Baseline.md v2.0 — §7 trauma 4-stage (FOUNDATION)
  ├── Threat.md v1.0 — threat mechanism, 3 nguồn, spectrum
  ├── Body-Feedback-Mechanism.md v1.2 — Chunk-Shift/Miss, compound
  ├── PFC-Configuration.md v1.0 — Mode ④ Disconnected, Mode ⑤ Dissociated
  ├── Chunk.md v2.1 — chunk substrate, context storage
  ├── Self-Pattern-Match.md v2.3 — SPM + C-PTSD identity
  └── Feeling-Mechanism-Deep.md — body-first invariant

THAM KHẢO:
  ├── PFC-Hardware.md v1.1 — NE α1/α2 circuit breaker
  ├── Background-Pattern.md v1.0 — sleep + chunk processing
  ├── Addiction-Analysis.md v3.0 — self-medication pattern
  ├── Connection.md v3.1 — trust disruption
  ├── Child-Development-Mechanism.md v1.0 — C-PTSD developmental
  ├── Alzheimer-Analysis.md (File 3) — hippocampus comparison
  ├── ADHD-Observation.md (File 5) — hyperarousal vs ADHD distinction
  └── Meaning.md v2.0 — meaning dissolution in avoidance
```

### Research cần tìm

```
🟢 Established:
  → Fear conditioning + amygdala — LeDoux 1996, 2000
  → Hippocampal volume reduction — Bremner 2006
  → HPA axis dysregulation — Yehuda 2001, 2004
  → EMDR mechanism — Shapiro 2001; van der Kolk 2014
  → Exposure therapy — Foa & Kozak 1986 (emotional processing theory)
  → Complex PTSD — Herman 1992; WHO ICD-11
  → PTSD prevalence — Kessler et al. 2005
  → Dual representation theory — Brewin et al. 2010

🟡 Framework synthesis:
  → Chunk context-tag formalization (PTSD forces this)
  → 2 encoding pathways: contextual (hippocampal) vs context-free (amygdala)
  → Body-override-PFC as extreme body-first case
  → Treatment unification: all = help add context to trauma chunks
  → C-PTSD = developmental SPM under chronic threat

🔴 Hypothesis:
  → Context tag as chunk metadata (formalization)
  → Amygdala-encoded chunks as separate chunk TYPE
  → PTSD recovery = chunk re-contextualization (not chunk deletion)
```

---

## ═══════════════════════════════════════════
## WORKFLOW MỖI FILE — "CHẬM MÀ CHẮC"
## ═══════════════════════════════════════════

```
⭐ NGUYÊN TẮC: Mỗi file = 1+ session RIÊNG. KHÔNG vội. KHÔNG gộp.
   Chia thành NHIỀU PHASE, phân tích kỹ từng phần, sau đó tổng hợp.
   Chất lượng > tốc độ. Mọi lúc.

══ PHASE 1 — ĐỌC + RESEARCH (đầu session) ══

  BƯỚC 1.1 — Đọc dependencies
    → Đọc KỸ các file mechanism liên quan (listed trong plan mỗi file)
    → Ghi chú cross-reference points cụ thể (§ nào, mechanism nào)
    → Hiểu rõ framework ĐÃ NÓI GÌ về topic này

  BƯỚC 1.2 — Research bên ngoài
    → Web search cho established research (🟢 citations)
    → Verify citations cụ thể, tìm key papers
    → Note data points, prevalence, neuroscience findings
    → Phân biệt: 🟢 established / 🟡 debated / 🔴 hypothesis

══ PHASE 2 — PHÂN TÍCH (giữa session) ══

  BƯỚC 2.1 — Phân tích từng khía cạnh RIÊNG
    → Mechanism cụ thể (neuroscience)
    → Framework mapping (kiến trúc v7.8 áp dụng thế nào)
    → So sánh với files đã drill trước (bridges)
    → Identify: framework ADD GIÁ TRỊ gì? Giới hạn ở đâu?

  BƯỚC 2.2 — Tổng hợp
    → Gộp phân tích → bức tranh tổng thể
    → Xác định structure file (§ nào, order nào)
    → Xây dựng plan triển khai chi tiết CHO FILE ĐÓ
    → ⚠️ DỪNG ở đây nếu cần compact — plan triển khai là checkpoint

══ PHASE 3+ — TRIỂN KHAI (cuối session hoặc session tiếp) ══

  BƯỚC 3.1 — Viết từng phần
    → Mỗi phase viết = vài sections (§0→§2, §3→§5, ...)
    → KHÔNG viết cả file 1 lần — chia nhỏ, review từng phần
    → Cross-reference chính xác (file + § + mechanism name)
    → Tone: respectful existing research, framework ADDS lens

  BƯỚC 3.2 — Honest Assessment
    → 🟢 / 🟡 / 🔴 cho từng claim
    → Open questions (cái gì CHƯA BIẾT)
    → Giới hạn scope rõ ràng (framework CAN vs CANNOT)

  BƯỚC 3.3 — Update hệ thống
    → 01-File-Index.md: thêm entry cho file mới
    → Cross-reference ngược nếu cần (files khác mention file mới)
    → Memory: update progress

══ QUALITY CHECKPOINTS ══

  ✅ Sau Phase 1: "Đã hiểu đủ chưa? Cần đọc/search thêm gì?"
  ✅ Sau Phase 2: "Plan triển khai có chắc chắn? Structure file hợp lý?"
  ✅ Sau mỗi batch §: "Sections vừa viết có consistent? Cross-refs đúng?"
  ✅ Cuối file: "Honest assessment thật sự honest? Open questions đủ?"

  Nếu BẤT KỲ checkpoint nào KHÔNG pass → DỪNG, refine, rồi mới tiếp.
  KHÔNG skip checkpoint vì "gần xong rồi".
```

---

## ═══════════════════════════════════════════
## TIMELINE DỰ KIẾN
## ═══════════════════════════════════════════

```
══ CLUSTER 1: DOPAMINE × 3 CƠ CHẾ ══

Session A — File 1: Nicotine-Brain-Mechanism.md
  → Đọc dependencies + research + viết
  → Dự kiến: ~800-1200L
  → Folder: Research/Health-Conditions/Hijack/

Session B — File 2: Parkinson-Analysis.md
  → Đọc dependencies + research + viết
  → Dự kiến: ~1000-1500L
  → Folder: Research/Health-Conditions/Neurodegeneration/ (tạo mới)

Session C — File 3: ADHD-Observation.md v1.0
  → Build on Attention-Spectrum.md + dopamine comparison (File 1+2)
  → 3-WAY COMPARISON TABLE: Hijack × Loss × Tuning
  → Dự kiến: ~1200-1600L
  → Folder: Research/Health-Conditions/Neurodiversity/ (tạo mới)
  → ⚠️ v1.0 = dopamine-focused. Refine sau Autism.

══ CLUSTER 2: NEURODEGENERATION + NEURODIVERSITY ══

Session D — File 4: Alzheimer-Analysis.md
  → Đọc dependencies + research + viết
  → Dự kiến: ~1200-1800L
  → Folder: Research/Health-Conditions/Neurodegeneration/

Session E — File 5: Autism-Observation.md
  → PHỨC TẠP NHẤT — benefit từ tất cả 4 files trước
  → Dự kiến: ~1500-2000L
  → Folder: Research/Health-Conditions/Neurodiversity/

══ CLUSTER 3: TRAUMA + REFINE ══

Session F — File 6: PTSD-Analysis.md
  → Builds on ALL previous + Cortisol-Baseline scaffold
  → Dự kiến: ~1200-1800L (refine framework: chunk context-tagging)
  → Folder: Research/

Session G — ADHD Refine: v1.0 → v1.1
  → Update ADHD với Autism insights:
    Config vs Tuning distinction, co-occurrence §8, sensory overlap
  → Dự kiến: thêm ~200-400L vào file có sẵn
  → Folder: Research/Health-Conditions/Neurodiversity/ (update existing file)

Session H (optional) — Cross-file refinement
  → So sánh 6 files, update cross-references
  → Update 01-File-Index.md
  → Neurodegeneration/ + Neurodiversity/ overview files nếu cần
  → Framework refinement: chunk context-tag formalization từ PTSD drill
```

---

## ═══════════════════════════════════════════
## LƯU Ý QUAN TRỌNG
## ═══════════════════════════════════════════

```
1. KHÔNG THAY THẾ Y KHOA
   → Mỗi file PHẢI có disclaimer rõ ràng
   → Framework = observation lens, không phải diagnostic tool
   → Đặc biệt autism + ADHD: KHÔNG "chữa" cái không phải bệnh
   → PTSD: respectful, observation only, không prescribe treatment

2. RESPECTFUL FRAMING
   → Parkinson/Alzheimer: respectful tới patients + caregivers
   → Autism + ADHD: "different" not "disordered" (framework-consistent)
   → Nicotine: không moralize, chỉ mechanism
   → PTSD: "hardware response" not "weakness"

3. HONEST ASSESSMENT
   → Phần lớn = 🟡 framework synthesis
   → Autism = nhiều 🔴 hypothesis nhất
   → Nicotine = nhiều 🟢 nhất (established research)
   → PTSD = nhiều 🟡 + framework PHẢI refine (chunk context-tag)
   → ADHD = 🟢 neurochemistry + 🟡 regulation model + 🔴 time perception

4. BRIDGE BETWEEN FILES
   DOPAMINE CLUSTER (File 1→2→3):
   → Nicotine → Parkinson: nAChR protective association + dopamine contrast
   → Nicotine → ADHD: cùng VTA-related nhưng hijack vs clearance
   → Parkinson → ADHD: cùng dopamine nhưng SOURCE chết vs CLEARANCE nhanh
   → 3-way comparison: Hijack × Loss × Tuning (table tại ADHD v1.0)
   
   CROSS-CLUSTER:
   → Nicotine → Alzheimer: cholinergic hypothesis (acetylcholine bridge)
   → Parkinson → Alzheimer: 2 loại neurodegeneration (motor vs memory)
   → ADHD v1.0 → Autism → ADHD v1.1: config vs tuning 2-dimension model
   → Autism ↔ ADHD: co-occur ~30-50%, overlap + distinction
   → ADHD → PTSD: hyperarousal MIMICS ADHD (misdiagnosis risk)
   → Alzheimer ↔ PTSD: both hippocampus (progressive vs acute)
   → PTSD → Addiction: self-medication pattern (bidirectional)

5. USER INSIGHTS
   → Tự kỷ: "phải từng case cụ thể đo lường sinh học cụ thể thì mới biết"
     Framework AGREES: mỗi individual = unique configuration
   → Chronic Pain: "framework có thể hỗ trợ sau này nếu framework đúng.
     chuyên gia có thể dùng framework để dự đoán nguyên nhân cụ thể"
     = SKIP now, POSSIBLE FUTURE via domain experts
   → Depression: "chính là neuralwear + trauma + buông xuôi" = compound outcome
     → mechanisms ĐÃ CÓ, viết file = synthesis ít giá trị refine
   → Insomnia: "rất nhiều nguyên nhân, không thể phân tích tổng quát bằng 1 file"
     = SYMPTOM, not condition

6. FRAMEWORK REFINEMENT FROM DRILL
   → File 6 (PTSD) CÓ KHẢ NĂNG refine framework nhiều nhất:
     → Chunk context-tagging formalization
     → Amygdala role in chunk storage
     → Body-override-PFC extreme cases
   → File 5 (ADHD) refine PFC model:
     → Regulation vs Configuration 2-dimension model
     → Methylphenidate paradox → PFC fuel mechanism
   → File 4 (Autism) refine chunk compilation:
     → Sensory gain → cascade effect
     → Multisensory binding → social chunk compilation
```
