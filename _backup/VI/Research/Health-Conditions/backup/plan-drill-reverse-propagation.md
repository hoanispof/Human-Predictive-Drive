# Plan: Drill Reverse Propagation — 6 Health Files → Core Framework

> **6 drill files. ~12,000+ lines. Giờ insights quay ngược lại refine CORE.**
>
> Drill = framework NHÌN condition.
> Reverse propagation = condition REFINE framework.
>
> "Dạy để hiểu. Nhìn từ ngoài vào, thấy trong rõ hơn."
>
> Nguyên tắc: CHẬM MÀ CHẮC. REFINE, không rewrite (trừ Chunk context-tag).
> Mỗi phase = đọc kỹ target file + phân tích + triển khai + verify.

---

## DRILL FILES (nguồn insights)

```
  ┌────┬──────────────────────────────┬────────┬─────────────────────────────┐
  │ #  │ File                         │ Lines  │ Framework angle             │
  ├────┼──────────────────────────────┼────────┼─────────────────────────────┤
  │ 1  │ Nicotine-Brain-Mechanism v1.1│ 1,120L │ Dopamine HIJACK (nAChR)     │
  │ 2  │ Parkinson-Analysis v1.1      │ 1,599L │ Dopamine SOURCE LOSS (SNc)  │
  │ 3  │ ADHD-Observation v1.2        │ 1,959L │ Dopamine CLEARANCE/TUNING   │
  │ 4  │ Alzheimer-Analysis v1.1      │ 2,995L │ Chunk system LOSS (synapse) │
  │ 5  │ Autism-Observation v1.0      │ 2,789L │ Hardware CONFIGURATION      │
  │ 6  │ PTSD-Analysis v1.0           │ 2,646L │ Chunk CONTEXT-TAG FAILURE   │
  └────┴──────────────────────────────┴────────┴─────────────────────────────┘
  + OCD-Analysis v2.2 (đã enriched session trước — DONE, không thuộc plan này)
```

---

## TARGET FILES × PRIORITY

```
═══ TIER 1 — HIGH: Concepts MỚI cần formalize ═══

  ① Chunk.md v2.1 (1,147L)
     → Context-tag formalization (4 metadata types)
     → 2 encoding pathways (hippocampal vs amygdala)
     → Compile depth × resistance (Alzheimer clinical validation)
     Scope: +80-120L (new §1.3 or §2 subsection + §12 update)

  ② Dopamine-Is-Not-Reward.md v1.1 (516L)
     → Wanting≠liking CLINICAL PROOF (Parkinson: Sienkiewicz-Jarosz 2005)
     → 3-way comparison table (Hijack × Loss × Tuning)
     → NIC-PD 2024 update
     Scope: +40-60L (§3 add evidence + new §3.8 or similar)

  ③ Body-Feedback-Mechanism.md v1.2 (1,010L)
     → Context-free chunk firing = Pattern-Driven variant
     → Chronic irresolvable prediction-delta (Parkinson case)
     Scope: +30-50L (§2.2 subsection + §3 note)

═══ TIER 2 — MEDIUM: Extensions quan trọng ═══

  ④ Background-Pattern.md v1.0 (1,042L)
     → "Last in first out" = clinical validation cho compile depth
     → 5 mechanisms overdetermined (Alzheimer)
     → Sleep × Glymphatic (Hauglund 2025 NE oscillations)
     → "Architecture determines pattern, NOT cause" meta-principle
     Scope: +50-80L (§2 validation note + §4 sleep enrichment)

  ⑤ Cortisol-Baseline.md v2.0 (2,646L)
     → Yehuda HPA paradox (LOW baseline, HIGH reactivity)
     → Prenatal cortisol → offspring calibration shift
     → α-synuclein aggravation (Bhatt 2019, Parkinson bridge)
     → Serotonin restoration pattern (Nicotine)
     Scope: +40-60L (§10 enrichment, cross-refs)

  ⑥ Body-Base.md v2.0 (774L)
     → Modulatory vs Processing neurons distinction (Parkinson)
     → Braak staging validates L0→L1→L3→PFC architecture
     Scope: +20-40L (§3 or §5 note)

  ⑦ Feeling.md v2.1 (1,466L)
     → Alexithymia = observation difficulty, NOT signal difficulty (Autism)
     → Bird & Cook 2013: controlling alexithymia → empathy = typical
     Scope: +15-25L (§3 or §7 validation note)

  ⑧ PFC-Configuration.md v1.0 (1,007L)
     → PTSD: Config ④ ↔ ⑤ oscillation
     → ADHD: DMN interference = mode-sustain failure
     → Parkinson: masked face = social gate locked
     Scope: +30-50L (§2 subsections enrichment)

═══ TIER 3 — LOWER: Cross-refs + minor enrichments ═══

  ⑨  Empathy.md v2.0 — Double empathy (Milton 2012, Crompton 2025)
  ⑩  Gap-Direction.md v1.0 — SI = concentrated gap-direction (Autism)
  ⑪  Connection.md v3.1 — One-sided body-coupling (Alzheimer caregiver)
  ⑫  SPM v2.3 — Late diagnosis re-compile + C-PTSD identity
  ⑬  Attention-Spectrum.md v2.0 — ADHD inverted-U
  ⑭  07-Social-Recognition-Arc.md — TBW ~600ms (Autism)
  ⑮  Addiction-Analysis.md v3.0 — 3 misconceptions + PTSD self-medication
  ⑯  Religion.md v2.2 — Maximum compile resistance (Alzheimer data)
  Scope: mỗi file +5-15L (cross-refs, 1-2 câu validation, version bump nhỏ)
```

---

## IMPLEMENTATION PHASES

```
⭐ NGUYÊN TẮC:
  → Mỗi phase = vài files LIÊN QUAN nhau → batch coherent
  → Mỗi file: ĐỌC KỸ current state → phân tích gap → triển khai → verify
  → Có thể chia 1 phase thành nhiều sub-steps nếu cần
  → KHÔNG skip verify — mỗi file refine xong phải coherent
  → Cross-refs giữa files refine TRONG CÙNG phase → tránh inconsistency
```

### Phase 1 — CHUNK CONTEXT-TAG (Tier 1, largest contribution)

```
TARGET: Chunk.md v2.1 → v2.2

ĐỌC:
  → Chunk.md v2.1 FULL (1,147L)
  → PTSD-Analysis §2 (context-tag model), §3 (2 pathways), §14 (formalization)
  → Alzheimer-Analysis §5 (synapse loss chain), §13 (compile depth validation)
  → Body-Feedback-Mechanism.md §2 (Pattern-Driven, reference)

THÊM:
  → §1 hoặc §2: Context-tag subsection
    → 4 metadata types: temporal, spatial, causal, state
    → Hippocampus attaches ①②③, Amygdala attaches ④
    → Normal: 4/4 = contextual chunk. Extreme stress: state only = context-free
    → Chunk content ≠ chunk metadata → metadata determines retrieval EXPERIENCE
  → §2 hoặc §5: 2 chunk types note
    → Contextual chunks (hippocampal — declarative, malleable)
    → Context-free chunks (amygdala — implicit, resistant, cue-bound)
  → §5 hoặc §2: Compile depth × resistance note
    → Alzheimer clinical data confirms: recent (shallow) → lost first
    → 5 overdetermined mechanisms (cite Alzheimer §13)
  → §12: Update honest assessment (🟡 context-tag synthesis, 🟢 compile depth)
  → §13: Add PTSD + Alzheimer cross-refs

SCOPE: +80-120L
ESTIMATED SESSION TIME: ~1/2 session (vừa đọc vừa triển khai)

DEPENDS ON: nothing (standalone, foundational)
```

### Phase 2 — DOPAMINE + BODY-FEEDBACK (Tier 1, smaller)

```
TARGET A: Dopamine-Is-Not-Reward.md v1.1 → v1.2

ĐỌC:
  → Dopamine-Is-Not-Reward.md FULL (516L — ngắn)
  → Parkinson §6.2 (wanting impaired, liking preserved)
  → ADHD §2 (DAT + DRD4 double hit)
  → Nicotine §1 (2 pathways)

THÊM:
  → §3: Clinical evidence from Parkinson
    → Sienkiewicz-Jarosz 2005: taste pleasantness PRESERVED in PD
    → Loas 2012: anhedonia = MOTIVATIONAL (can't want), not hedonic (can enjoy)
    → = Steps 2-4 weakened, Step 5 preserved → 7-step CONFIRMED clinically
  → §3 or §5: 3-way comparison table (or reference to ADHD §3)
    → Hijack (Nicotine) × Loss (Parkinson) × Tuning (ADHD)
    → Cùng dopamine, 3 cơ chế KHÁC → 3 outputs KHÁC
  → §5: NIC-PD 2024 update (nicotine NOT protective)
  → §6: Update honest assessment
  → §7: Update cross-refs (3 drill files)

SCOPE: +40-60L

---

TARGET B: Body-Feedback-Mechanism.md v1.2 → v1.3

ĐỌC:
  → Body-Feedback-Mechanism.md FULL (1,010L)
  → PTSD §4 (flashback = context-free chunk firing)
  → Parkinson §5 (chronic irresolvable prediction-delta)

THÊM:
  → §2.2 (Pattern-Driven): Add context-free chunk variant
    → PTSD: chunk fires WITHOUT context → body responds AS IF in original event
    → = Pattern-Driven firing WHERE pattern = sensory cue match trauma chunk
    → Cross-ref Chunk.md context-tag (Phase 1)
  → §3 (Chunk dynamics): Add irresolvable prediction-delta note
    → Parkinson: predict "move" → body doesn't → CANNOT resolve
    → Normal Chunk-Miss: miss → adjust → succeed (seconds)
    → PD Chunk-Miss: miss → try harder → STILL fail → chronic irresolvable
    → = New variant: chronic delta that HARDWARE prevents resolving
  → §9: Update honest assessment
  → §10: Update cross-refs

SCOPE: +30-50L

TOTAL PHASE 2: +70-110L, ~1/2 session
DEPENDS ON: Phase 1 ideally (context-tag reference), nhưng CÓ THỂ song song
```

### Phase 3 — BACKGROUND-PATTERN + CORTISOL (Tier 2, thematic pair)

```
TARGET A: Background-Pattern.md v1.0 → v1.1

ĐỌC:
  → Background-Pattern.md FULL (1,042L)
  → Alzheimer §13 (5 mechanisms "last in first out")
  → Alzheimer §17 (reverse-engineering lens, architecture determines pattern)
  → Alzheimer §11 (sleep × glymphatic, Hauglund 2025)

THÊM:
  → §2: Clinical validation note for compile depth model
    → Alzheimer "last in first out" = clinical data confirms framework prediction
    → 5 overdetermined mechanisms (consolidation + depth×distribution +
      activity-dependent + multiple trace + myelination order)
    → "Architecture determines pattern, NOT cause"
    → CITE: Reisberg 2002 retrogenesis, Bartzokis 2004 myelin
  → §4 (Sleep): Glymphatic enrichment
    → Hauglund 2025 (Cell): NE oscillations pump CSF
    → Glymphatic clearance requires SLEEP-specific NE pattern
    → Zolpidem WARNING: sedation ≠ glymphatic (sleep without cleanup)
  → §8 or new: Alzheimer as reverse-engineering lens note
    → "Dù lửa bắt đầu từ đâu, tòa nhà sụp từ tầng cao nhất"
  → Update honest assessment + cross-refs

SCOPE: +50-80L

---

TARGET B: Cortisol-Baseline.md v2.0 → v2.1

ĐỌC:
  → Cortisol-Baseline.md §10 (trauma section) + §0 (4-tier calibration)
  → PTSD §5 (HPA paradox), §13 (intergenerational)
  → Parkinson §3.8 (cortisol × α-synuclein, Bhatt 2019)

THÊM:
  → §10 (trauma section): Yehuda HPA paradox enrichment
    → LOW baseline + HIGH reactivity (not simple "high cortisol")
    → Acute HIGH → chronic LOW transition
    → Enhanced negative feedback → GR supersensitivity
  → §6 or §10: Prenatal cortisol pathway note
    → Maternal PTSD → reduced 11β-HSD2 → fetal HPA recalibrated
    → = §6 tầng 2 (Development) disrupted IN UTERO
  → §3 or §9: α-synuclein aggravation (Parkinson bridge)
    → Bhatt 2019: chronic cortisol aggravates α-syn spreading
    → = Cortisol ↔ neurodegeneration connection
  → Update cross-refs (PTSD, Parkinson, Nicotine files)

SCOPE: +40-60L

TOTAL PHASE 3: +90-140L, ~1 session
DEPENDS ON: Phase 1 (context-tag referenced in cortisol trauma section)
```

### Phase 4 — BODY-BASE + FEELING + PFC-CONFIG (Tier 2, architecture trio)

```
TARGET A: Body-Base.md v2.0 → v2.1

ĐỌC:
  → Body-Base.md FULL (774L — ngắn)
  → Parkinson §2 (modulatory vs processing distinction)
  → Parkinson §4.2 (Braak maps to L0→L1→L3→PFC)

THÊM:
  → §3 or §5: Modulatory vs Processing neurons note
    → Processing = mạch CHÍNH (glutamate/GABA, xử lý + điều khiển)
    → Modulatory = mạch PHỤ (dopamine/serotonin/NE/ACh, điều chỉnh gain)
    → Framework L0/L1 = body-base, L3 = modulatory (phần lớn), PFC = processing
    → Parkinson: modulatory chết → processing CÒN nhưng không được modulate
    → Braak staging = α-syn ascending L0→L1→L3→PFC = validates framework stack
  → Update honest assessment + cross-refs

SCOPE: +20-40L

---

TARGET B: Feeling.md v2.1 → v2.2

ĐỌC:
  → Feeling.md §3 (core claim) + §7 (gradient)
  → Autism §7 (alexithymia section)

THÊM:
  → §3 or §7: Alexithymia validation note
    → Autism drill: ~50% autistic people have alexithymia (Kinnaird 2019)
    → Bird & Cook 2013: controlling alexithymia → NO independent autism effect
      on emotion recognition
    → = CONFIRMS: feeling = PFC OBSERVATION of body-feedback
    → Alexithymia = observation DIFFICULTY, not signal difficulty
    → Body-feedback signals VẪN FIRE → reading/labeling bị trở ngại
  → Update honest assessment + cross-refs

SCOPE: +15-25L

---

TARGET C: PFC-Configuration.md v1.0 → v1.1

ĐỌC:
  → PFC-Configuration.md §2 (6 modes)
  → PTSD §4.4 (Config ④ ↔ ⑤ oscillation)
  → ADHD §8 (DMN interference)
  → Parkinson §5.4 (masked face)

THÊM:
  → §2 (Mode ④ Disconnected): PTSD clinical illustration
    → PTSD: PFC ④ ↔ ⑤ OSCILLATION (flooding ↔ dissociation)
    → Dissociative subtype: compiled ⑤ as DEFAULT
    → Body-Feedback → PFC online/offline cycle
  → §2 (Mode ① Normal): ADHD DMN interference note
    → DMN interference = Mode ① UNSTABLE → drift toward ② or sub-threshold ④
    → Methylphenidate stabilizes: by fueling PFC → sustain Mode ①
  → §2 or §6: Parkinson social gate locked note (optional — minor)
  → Update honest assessment + cross-refs

SCOPE: +30-50L

TOTAL PHASE 4: +65-115L, ~1 session
DEPENDS ON: Phase 1 (context-tag), Phase 2 (body-feedback context-free)
```

### Phase 5 — TIER 3 BATCH (cross-refs + validation sweep)

```
TARGETS (8 files, mỗi file nhỏ):

  ⑨ Empathy.md v2.0
     +10-15L: Double empathy (Milton 2012, Crompton 2025).
     Non-autistic CŨNG fail SPM autistic people.
     §section liên quan: có thể §2 hoặc §8

  ⑩ Gap-Direction.md v1.0
     +5-10L: Autism SI = concentrated gap-direction → clinical validation.
     "Feature not bug" — same mechanism, concentrated application.

  ⑪ Connection.md v3.1
     +5-10L: Alzheimer caregiver = one-sided body-coupling.
     "Ambiguous loss" (Boss 1999/2000). L1 drain without L2.

  ⑫ SPM v2.3
     +10-15L: Late diagnosis identity re-compile (ADHD + Autism).
     C-PTSD = SPM compiled under chronic threat → developmental identity.

  ⑬ Attention-Spectrum.md v2.0
     +10-15L: ADHD inverted-U model (Frontiers 2022).
     Environment shifts peak position on curve.

  ⑭ 07-Social-Recognition-Arc.md
     +5-10L: TBW ~600ms (Autism, Foss-Feig 2010, Stevenson 2014).
     Wider TBW → social input integration KHÁC.

  ⑮ Addiction-Analysis.md v3.0
     +10-15L: 3 misconceptions unified pattern (Nicotine §5).
     PTSD self-medication bridge (Khantzian 1985).

  ⑯ Religion.md v2.2
     +5-10L: AD data confirms maximum compile resistance.
     Kaufman 2007: spirituality → slower cognitive decline.
     6 memory systems engaged simultaneously.

TOTAL PHASE 5: +60-100L across 8 files, ~1 session
DEPENDS ON: Phase 1-4 complete (cross-refs point to updated §numbers)
```

### Phase 6 — FINAL SWEEP + INDEX UPDATE

```
TARGETS:
  → 01-File-Index.md: Update version numbers for ALL refine files
  → Verify ALL cross-refs point to correct §numbers (post-refine)
  → Check no circular dependency or inconsistency introduced
  → Memory update

SCOPE: small, ~1/2 session
DEPENDS ON: ALL previous phases complete
```

---

## SUMMARY TABLE

```
  ┌─────────┬──────────────────────────────────────────┬──────────┬──────────┐
  │ Phase   │ Target files                             │ Est.lines│ Sessions │
  ├─────────┼──────────────────────────────────────────┼──────────┼──────────┤
  │ Phase 1 │ Chunk.md (context-tag)                   │ +80-120L │ ~1/2     │
  │ Phase 2 │ Dopamine-Is-Not-Reward + BFM             │ +70-110L │ ~1/2     │
  │ Phase 3 │ Background-Pattern + Cortisol-Baseline   │ +90-140L │ ~1       │
  │ Phase 4 │ Body-Base + Feeling + PFC-Configuration  │ +65-115L │ ~1       │
  │ Phase 5 │ 8 files (Tier 3 batch)                   │ +60-100L │ ~1       │
  │ Phase 6 │ Index + verify + memory                  │ small    │ ~1/2     │
  ├─────────┼──────────────────────────────────────────┼──────────┼──────────┤
  │ TOTAL   │ ~16 files refine                         │+365-585L │ ~4 sess  │
  └─────────┴──────────────────────────────────────────┴──────────┴──────────┘

  So sánh: Health Conditions DRILL = ~12,000L (tạo MỚI)
  Reverse propagation = ~500L (refine EXISTING) — nhưng MỖI dòng quan trọng hơn
  vì nó SỬA CỐT LÕI, không phải thêm nhánh mới.
```

---

## WORKFLOW MỖI PHASE — "CHẬM MÀ CHẮC"

```
⭐ CÙNG workflow như drill, nhưng scope nhỏ hơn + precision cao hơn:

  BƯỚC 1 — ĐỌC KỸ target file (current state)
    → Đọc TOÀN BỘ file target
    → Hiểu §structure, cross-refs, style, confidence markers
    → Identify CHÍNH XÁC vị trí thêm (§ nào, sau dòng nào)

  BƯỚC 2 — ĐỌC KỸ drill source (specific sections)
    → Chỉ đọc §sections CẦN cho refine (đã list trong plan)
    → Extract: data points, citations, framework synthesis, confidence level

  BƯỚC 3 — PHÂN TÍCH GAP
    → Target file ĐÃ NÓI GÌ → drill THÊM GÌ → gap = ?
    → Determine: thêm subsection mới? thêm vào §có sẵn? chỉ cross-ref?
    → CHECK: có contradictions không? (resolve trước khi viết)

  BƯỚC 4 — TRIỂN KHAI
    → Viết COHERENT với style file target (không import style từ drill)
    → Confidence markers chính xác (🟢🟡🔴)
    → Cross-refs chính xác (file + § + concept)
    → Version bump in header

  BƯỚC 5 — VERIFY
    → Đọc lại phần vừa thêm IN CONTEXT (trước + sau)
    → Cross-refs đúng §numbers?
    → Không introduce contradictions?
    → Honest assessment updated?

  NẾU BẤT KỲ bước nào KHÔNG pass → DỪNG, analyze, rồi tiếp.
```

---

## KEY DECISIONS

```
1. REFINE, không rewrite
   → Core files đã ở v2.0+ quality → chỉ thêm insights, không restructure
   → Exception: Chunk.md context-tag = section MỚI (vì concept chưa có)

2. Mỗi phase = COHERENT batch
   → Files liên quan cùng phase → cross-refs consistent trong batch
   → Phase 1 = foundation (Chunk) → Phase 2-4 reference nó

3. Tier 3 = batch vì mỗi file chỉ thêm vài dòng
   → Không worth 1 session riêng → gộp

4. Confidence markers phải HONEST
   → Drill insights phần lớn = 🟡 synthesis → ghi rõ trong core files
   → Clinical data = 🟢 → add research citations
   → Framework hypotheses = 🔴 → mark clearly

5. KHÔNG thay đổi existing conclusions
   → Chỉ ADD evidence, ADD validation, ADD connections
   → Nếu drill insight CONTRADICTS core → flag, discuss, KHÔNG overwrite
   → (Hiện tại: drill CONFIRMS core → không có contradictions phát hiện)

6. Cross-ref style: nhẹ nhàng
   → "(Parkinson-Analysis.md §6.2 confirms clinically)"
   → KHÔNG copy nội dung drill vào core → chỉ note + point
   → Core files = concise. Drill files = chi tiết.
```

---

## DEPENDENCIES

```
  Phase 1 (Chunk context-tag)
    ↓
  Phase 2 (Dopamine + BFM) — refs context-tag
    ↓
  Phase 3 (Background-Pattern + Cortisol) — refs context-tag
    ↓
  Phase 4 (Body-Base + Feeling + PFC-Config) — refs Phase 1-3
    ↓
  Phase 5 (Tier 3 batch) — refs Phase 1-4 §numbers
    ↓
  Phase 6 (Index + verify)

  ⚠️ Phase 2 và Phase 3 CÓ THỂ song song (nếu §numbers Phase 1 đã stable)
  ⚠️ Phase 4 NÊN sau Phase 1-3 (nhiều cross-refs)
  ⚠️ Phase 5 PHẢI sau tất cả (cross-ref §numbers)
```

---

## CHƯA QUYẾT ĐỊNH (session sau có thể thay đổi)

```
  ? Chunk.md context-tag: section MỚI (§1.3?) hay §2 subsection?
    → Cần đọc full file để quyết định vị trí tự nhiên nhất

  ? Background-Pattern "architecture determines pattern" = thêm vào BP
    hay tạo note riêng ở level cao hơn?
    → Insight có thể thuộc meta-framework hơn là 1 file cụ thể

  ? Tier 3 files: nên update cross-refs header CÙNG LÚC hay sau?
    → Đề xuất: update header (dependencies version) trong Phase 5
    → Full index update trong Phase 6

  ? 2D Neurodiversity model (Config × Tuning): thêm vào core hay chỉ ở drill?
    → Hiện tại: chỉ ở ADHD/Autism drill files
    → Có thể: note ở Body-Base.md §5 hoặc tạo overview file sau
    → QUYẾT ĐỊNH sau khi Phase 1-4 xong
```

---

> **Reverse propagation plan — v1.0**
> **~16 files refine, ~500L additions, ~4 sessions estimated**
> **Mỗi session: đọc + phân tích + triển khai + verify**
> **"Drill insights refine core = insights quay về nhà."**
