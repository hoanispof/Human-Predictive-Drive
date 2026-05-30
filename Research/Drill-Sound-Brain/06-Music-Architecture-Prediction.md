---
title: Music Architecture × Prediction Architecture — Tại Sao Nhạc Cấu Trúc Như Vậy
version: 1.2
created: 2026-05-29
updated: 2026-05-29 (v1.2 — Large&Palmer journal fixed (Cognitive Science), Bowling&Purves "across cultures" nuanced (debate with McDermott 2016))
status: REFERENCE v1.1
scope: |
  FOUNDATIONAL REFERENCE: Kiến trúc âm nhạc phổ thông = f(kiến trúc prediction của não).
  Hard numbers + established research + undeniable structural facts.
  6 hệ thống cấu trúc (Pitch, Rhythm, Harmony, Form, Repetition, Cross-Cultural).
  Framework mapping: mỗi feature cấu trúc = OPTIMIZE prediction-delta delivery.
  KHÔNG culturally biased claim — phân tách universal vs learned rõ ràng.
purpose: |
  03-Musical-Notation-Architecture.md mô tả music notation AS communication format.
  File NÀY khác: KHÔNG mô tả notation, mà hỏi TẠI SAO music cấu trúc thế.
  Music architecture = NOT arbitrary. Each feature = f(brain prediction constraint).
  Tonic exists BECAUSE brain needs prediction anchor.
  BPM exists BECAUSE neural oscillators need sync signal.
  Verse-chorus exists BECAUSE prediction-delta needs oscillation.
  Repetition exists BECAUSE prediction model needs training data.
  = Music architecture maps to Gap-Direction + Reward Pipeline + Body-Feedback.
position: |
  Research/Drill-Sound-Brain/ — foundational reference.
  Đọc SAU 01 (evidence) + 03 (reward pipeline).
  Đọc TRƯỚC 07 (entrainment + reward dynamics).
  COMPLEMENT 03-Musical-Notation-Architecture (notation = WHAT; file này = WHY).
dependencies:
  primary:
    - Prediction-Error-Is-Not-Reward.md v2.0 — PE + coherence + Goldilocks
    - Gap-Direction.md v2.0 — gap has direction, "chưa biết = không có gap"
    - Body-Feedback-Mechanism.md v2.1 — chunk dynamics, prediction-delta
  secondary:
    - Background-Pattern.md v2.0 — gist extraction, Triple Bias
    - Reward-Calibration.md v1.1 — Goldilocks per-gap, 3 zones
    - Boredom.md v2.0 — prediction-delta = 0
    - Modality.md v1.0 — multi-modal encoding
  evidence:
    - 01-Sound-Brain-Neuroscience.md — §3 (prediction), §6 (entrainment)
    - 03-Musical-Notation-Architecture.md — notation reference
  within_drill:
    - 02-Sound-Background-Pattern.md — gist, genre, satiation
    - 03-Sound-Reward-Pipeline.md — 7-step, Cheung 2019
language: Tiếng Việt primary + English technical terms
confidence: 🟢 Research support | 🟡 Framework synthesis | 🔴 Hypothesis
---

# Music Architecture × Prediction Architecture — Tại Sao Nhạc Cấu Trúc Như Vậy

> **~94% nhạc pop = 4/4.**
> **BPM phổ biến nhất = 120 (= 2 bước/giây = tốc độ đi bộ nhanh).**
> **I-V-vi-IV = 4 hợp âm xuất hiện trong HÀNG TRĂM hit.**
> **Verse-chorus chiếm 80-90%+ Billboard từ 1980s.**
> **Bài hit lặp lại nhiều hơn bài bình thường 3-6%.**
>
> **Tại sao?**
>
> **Không phải ngẫu nhiên. Không phải chỉ "truyền thống."**
> **Music architecture = f(brain prediction architecture).**
>
> **Não cần prediction anchor → nhạc có TONIC CENTER.**
> **Não cần phase-locking signal → nhạc có BPM ĐỀU ĐẶN.**
> **Não cần oscillation prediction-delta → nhạc có VERSE-CHORUS.**
> **Não cần training data → nhạc có REPETITION.**
> **Não cần gap-open → gap-fill cycle → nhạc có TENSION-RESOLUTION.**
>
> **File này: KIẾN TRÚC nào, DATA cụ thể, và TẠI SAO nó khớp prediction.**

---

## Mục lục

- §0 — Thesis: Music Architecture = Prediction Architecture Optimization
- §1 — Pitch System: 12 Notes, Tonal Hierarchy, Tonic Center
- §2 — Rhythm System: BPM, 4/4, Meter
- §3 — Harmony System: Chords, Progressions, Tension-Resolution
- §4 — Form System: Verse-Chorus, Song Length, Arc
- §5 — Repetition: Why Music Repeats Itself
- §6 — Cross-Cultural: Universal vs Learned
- §7 — Framework Mapping: Each Feature = Prediction Constraint
- §8 — Non-Standard Structures: Tại Sao Hiếm + Khi Nào Thành Công
- §9 — Honest Assessment
- §10 — Cross-References

---

## §0 — Thesis: Music Architecture = Prediction Architecture Optimization

```
⭐⭐ CORE THESIS:

  Music architecture KHÔNG arbitrary.
  Mỗi feature cấu trúc = giải pháp cho 1 CONSTRAINT
  của prediction architecture trong não.

  ┌───────────────────────┬──────────────────────────────────────────┐
  │ Brain Constraint       │ Music Solution                          │
  ├───────────────────────┼──────────────────────────────────────────┤
  │ Prediction cần anchor │ Tonic center (home note)                │
  │ Oscillators cần sync  │ BPM đều đặn                             │
  │ PE cần Goldilocks     │ Verse-chorus oscillation                │
  │ Model cần training    │ Repetition (chorus, hook, riff)         │
  │ Gap cần fill cycle    │ Tension → Resolution                    │
  │ Attention có giới hạn │ Song length ~3-4 phút                   │
  │ Motor cortex entrain  │ 4/4 time (binary, dễ entrain)          │
  │ Precision per-person  │ Genre complexity spectrum               │
  └───────────────────────┴──────────────────────────────────────────┘

  = KHÔNG PHẢI nhạc "bắt chước" não.
  = Nhạc mà KO khớp prediction architecture → KHÔNG SỐNG SÓT.
  = Natural selection ở cultural level:
    nhạc khớp não → người nghe → truyền → sống
    nhạc ko khớp → bỏ qua → chết
  = Music = cultural product SHAPED BY prediction constraints.

  ⚠️ v1.1: Prediction optimization = NOT sole driver.
  ⭐ Savage et al. 2021 (BBS): music = "coevolved system for SOCIAL BONDING."
    Isochronous beat has "clear functions for group performance but little
    or no function in solo performance."
    → Social coordination/bonding = CO-EQUAL driver alongside prediction.
    → Some features (regular beat) serve BOTH prediction AND social sync.
    → This file focuses on prediction mapping; social bonding perspective
      → see 04-Sound-Social-Resonance.md for social dimension.
```

---

## §1 — Pitch System: 12 Notes, Tonal Hierarchy, Tonic Center

### §1.1 — 12 Notes: Mathematical Fact

```
🟢 12-TONE EQUAL TEMPERAMENT (12-TET):

  Mỗi octave chia thành 12 nốt đều nhau.
  Mỗi nốt = tần số × 2^(1/12) ≈ 1.05946 so với nốt trước.
  12 nốt × 1.05946 = ×2 → octave = gấp đôi tần số.

  TẠI SAO 12?
    → 12 xấp xỉ TỐT NHẤT các tỉ lệ tự nhiên:
      Perfect fifth (3:2) ≈ 7 semitones (2^(7/12) = 1.4983, sai ~2 cents)
      Perfect fourth (4:3) ≈ 5 semitones
      Major third (5:4) ≈ 4 semitones
    → 12 quãng Pythagorean fifths liên tiếp vượt 7 octaves
      chênh ~23.46 cents (Pythagorean comma)
    → 12-TET phân bổ sai số ĐỀU qua 12 nốt (~2 cents mỗi nốt)
    → = Compromise TỐI ƯU: đủ chính xác + cho phép chuyển giọng tự do

  LỊCH SỬ:
    → Zhu Zaiyu (Trung Quốc, 1584): tính 12th root of 2
    → Simon Stevin (Hà Lan, ~1585): mô tả tương tự
    → Bach era (~1700s): phổ biến hóa qua Well-Tempered Clavier

  HỆ THỐNG KHÁC TỒN TẠI:
    → 24-TET (Arabic quarter-tones)
    → 19-TET, 31-TET, 53-TET (microtonal)
    → Gamelan (Indonesia): 5 hoặc 7 nốt, KHÔNG equal-tempered
    → = 12-TET KHÔNG phải "duy nhất đúng" — là "phổ biến nhất"

  🟢 Mathematical fact — không debatable
```

### §1.2 — Tonal Hierarchy: Brain Ranks Notes

```
🟢 PROBE-TONE PROFILES — BRAIN TỰ ĐỘNG XẾP HẠNG NỐT:

  🟢 Krumhansl & Kessler 1982 (Psychological Review):
    Method: play tonal context → probe single tone → listener rate "fit"
    Finding: listeners CONSISTENTLY rank:
      Tonic > Fifth > Third > Other diatonic > Chromatic
    → = Tonal HIERARCHY, not equal-importance

  REPLICATION STATUS:
    → 🟢 Castellano, Bharucha & Krumhansl 1984:
      North Indian raga listeners → ANALOGOUS hierarchy (Sa > Pa > Ga...)
    → 🟢 Kessler, Hansen & Shepard 1984:
      Balinese music → hierarchical structure tồn tại
    → 🟢 2021 (Music Perception, UC Press):
      Rock music → "less differentiated" nhưng hierarchy VẪN CÓ
    → = Cross-cultural, cross-genre. ROBUST finding.

  🟢 Janata et al. 2002 (Science):
    rmPFC (rostromedial PFC) ACTIVELY TRACKS tonal center
    khi music modulate qua các keys
    → Tonal center = MAINTAINED REPRESENTATION trong PFC
    → PFC continuously update "home" = tonic

  🟢 Hannon & Trainor 2007:
    6 tháng: respond broadly (native + foreign tonal structures)
    12 tháng: culture-specific patterns (adult-like)
    → Tonal hierarchy = LEARNED through enculturation
    → Hardware + exposure → emergence, NOT hardwired per-culture
```

### §1.3 — Tonic Center: Why "Home Note" Must Exist

```
🟡 FRAMEWORK MAPPING: TONIC = PREDICTION ANCHOR

  Gap-Direction.md §1: gap direction = f(surrounding chunk network)
  Prediction-Error-Is-Not-Reward.md: PE cần BASELINE để compare

  TONIC = BASELINE cho musical prediction:
    → Brain builds prediction model CENTERED on tonic
    → Mọi nốt khác = deviation from baseline
    → Deviation = prediction-delta → VTA fire → attention
    → Return to tonic = prediction COMPLETION → reward

  VÌ SAO TẤT CẢ MUSIC CẦN "HOME":
    → Prediction CẦN reference point
    → Không có reference → mọi nốt EQUIVALENT → không predict được
    → Không predict → không PE → không reward
    → = Music WITHOUT tonic = random notes = Spotify test
      (Prediction-Error-Is-Not-Reward.md §3: random = PE nhưng DỞ)

  TONIC ≠ CỐ ĐỊNH:
    → Modulation (chuyển giọng) = SHIFT tonic
    → Brain CAN update → Janata 2002: PFC tracks dynamically
    → Modulation lên nửa cung cuối bài → prediction anchor SHIFT UP
    → New tonic = NEW baseline → OLD patterns = slightly unpredicted
    → = VTA fire lại → energy boost → "hưng phấn cuối bài"

  🟢 Tonal hierarchy: established
  🟡 Tonic = prediction anchor: framework mapping (logical, components validated)
```

---

## §2 — Rhythm System: BPM, 4/4, Meter

### §2.1 — BPM: Human Resonance Frequency

```
🟢 SPONTANEOUS MOTOR TEMPO = ~120 BPM:

  🟢 Moelants 2002 (7th ICMPC, N=74,000+ pieces):
    Spontaneous motor tempo centers around 120 BPM (~500ms inter-onset)
    → Revise Fraisse's earlier estimate (~100 BPM)
    → Preferred listening tempo clusters 120-130 BPM

  TẠI SAO 120 BPM?
    → Brisk walking = 120-130 steps/min
    → Moderate heart rate exercise = 100-130 BPM
    → = Natural RESONANCE FREQUENCY of human locomotion
    → Body ALREADY oscillates at ~2 Hz → music at 2 Hz = easiest entrain

  BPM DISTRIBUTION TRONG POPULAR MUSIC:
    → EDM: ~120-140 BPM
    → Pop: ~100-130 BPM
    → Rock: ~110-140 BPM
    → Hip-hop: ~70-100 BPM (half-time feel = ~140-200 in double-time)
    → Ballad: ~60-80 BPM
    → ⭐ MOST popular music clusters around 100-130 BPM = locomotion zone

  THAY ĐỔI THEO THỜI ĐẠI:
    → Billboard Hot 100: tempo tăng 1990s→2014 (dance-pop/EDM era)
    → Giảm với hip-hop dominance + streaming era
    → Trung bình hiện tại ~110-120 BPM

  🟢 Moelants 2002: established (74,000+)
  🟢 Locomotion resonance: well-documented
```

### §2.2 — 4/4 Time Signature: Why ~94% of Pop

```
🟢 4/4 DOMINANCE — HARD NUMBER:

  ~94% nhạc pop = 4/4 time signature
  (Analysis of 440 pop songs; all 17 UK No.1 singles 2018 = 4/4)
  🟢 Aravind et al. 2025 (arXiv, "Skip That Beat"):
    Beat-tracking datasets overwhelmingly 4/4
    Non-4/4 drastically underrepresented

  TẠI SAO 4/4?
    → 4/4 = 4 beats per bar = BINARY division (4 = 2²)
    → Binary = simplest metrical structure cho entrainment
    → 2 là NHỊP NHỊ PHÂN:
      Strong-Weak-Strong-Weak (1-2-3-4)
      = Alternating emphasis = easiest prediction
    → Compare 3/4: ternary → less intuitive body entrainment
    → Compare 7/8: PRIME number → much harder to predict

  🟡 FRAMEWORK MAPPING:
    → 4/4 = LOWEST COMPLEXITY for meter prediction
    → Low complexity = prediction model builds FASTEST
    → Fast prediction model = reach Goldilocks zone SOONEST
    → = MAXIMUM ACCESSIBILITY (anyone can entrain immediately)
    → Phức tạp hơn (5/4, 7/8) = cần MORE chunks để predict
    → = Body-Feedback-Precondition Precondition-2 barrier HIGHER → smaller audience

  NEXT COMMON:
    → 3/4 (waltz): folk, country, ballads
    → 6/8 (compound): ballads, marches
    → 5/4, 7/8: progressive rock, Balkan music, jazz
    → = Phức tạp hơn → niche audiences
```

### §2.3 — BPM × Neural Entrainment

```
🟢 NEURAL OSCILLATORS PHASE-LOCK TO BPM:

  🟢 Large & Snyder 2009 (NYAS):
    Neural resonance theory: neural oscillations ENTRAIN to beat frequency
    Beta oscillations (13-30 Hz) facilitate sensorimotor coupling

  🟢 Snyder & Large 2005, replicated Fujioka 2009, 2012:
    Beta oscillations: DECREASE after beat → REBOUND before next beat
    = ANTICIPATORY: brain "prepare" for next beat
    Gamma oscillations: fire BEFORE beat → PERSIST even when beat MISSING
    = Brain PREDICT beat → fire even when absent ("missing pulse")

  🟢 Nozaradan et al. 2011 (Journal of Neuroscience):
    EEG steady-state evoked potentials at EXACT beat frequency
    When imagining binary vs ternary meter on same beat:
    EEG enhanced at IMAGINED meter frequency
    = TOP-DOWN entrainment, not just bottom-up

  ⭐ BPM ĐỀU ĐẶN = SYNCHRONIZATION SIGNAL:
    → Regular interval → oscillators PHASE-LOCK dễ hơn
    → Phase-locked oscillators across regions → MORE coherent processing
    → More coherent → better prediction → more compound reward
    → = BPM regularity = optimization for DISTRIBUTED NEURAL SYNC

  🟢 Neural entrainment: most robust finding in music neuroscience
  🟡 BPM as sync optimization: framework mapping
```

---

## §3 — Harmony System: Chords, Progressions, Tension-Resolution

### §3.1 — Chord Frequency in Popular Music

```
🟢 DE CLERCQ & TEMPERLEY 2011 (Popular Music, Cambridge):
    Corpus: 100 songs from Rolling Stone's 500 Greatest Songs

    CHORD FREQUENCY:
      I   = ~33% of all chord instances (tonic — "home")
      IV  = ~17% (subdominant)
      V   = ~12% (dominant)
      bVII = ~8%
      vi  = ~7%
      → Top 3 chords (I, IV, V) = ~62% of ALL chords in THIS CORPUS
    ⚠️ 62% = derived sum (33+17+12), not independently published figure.
       Corpus = 100 songs from Rolling Stone 500 Greatest — may not represent
       all pop music. Directionally valid: I, IV, V are consistently TOP 3
       across harmonic studies, but exact % varies by corpus.

    ⭐ NOTABLE: IV > V in rock/pop
      → Classical: V (dominant) resolves TO I (strongest resolution)
      → Rock/pop: IV (subdominant) more common than V
      → = Slightly different harmonic language, SAME tonic-centered hierarchy

    COMMON PROGRESSIONS:
      I-V-vi-IV  ("Axis progression" — Let It Be, No Woman No Cry, etc.)
      I-IV-V-IV  (blues-derived)
      I-vi-IV-V  ("50s progression" — Stand By Me, etc.)
      i-bVI-bIII-bVII (minor variant)
      12-bar blues: I-I-I-I-IV-IV-I-I-V-IV-I-V

  HARMONIC RHYTHM:
    🟢 De Clercq 2023 (Musicae Scientiae 27(3)):
      Common pattern: 1 chord per bar (4 beats) hoặc per 2 beats
      At 120 BPM: 1 bar ≈ 2 seconds
      → Harmonic change every ~2 seconds = manageable prediction rate

  🟡 FRAMEWORK MAPPING:
    → I (tonic chord) = harmonic "home" → prediction ANCHOR
    → IV, V = most common DEVIATIONS → moderate prediction-delta
    → Progression = PREDICTABLE sequence → model builds across repeats
    → Return to I = resolution → gap-fill → reward
```

### §3.2 — Tension-Resolution: The Core Emotional Engine

```
🟢 TENSION-RESOLUTION = UNIVERSAL PRINCIPLE:

  🟢 Meyer 1956 (Emotion and Meaning in Music, University of Chicago):
    FOUNDATIONAL: Musical emotion = confirmation/violation of LEARNED expectations
    Deviation from expected progression → tension (prediction-delta HIGH)
    Resolution to expected → release (prediction match → reward)

  MECHANISM:
    V chord (dominant) → "chưa xong" → body: TENSION (gap OPEN)
    I chord (tonic) → "xong rồi" → body: RESOLUTION (gap FILL)
    → Dominant → Tonic = STRONGEST resolution in Western harmony
    → ii-V-I = build → peak tension → complete resolution

  ⭐ FRAMEWORK MAPPING — Gap-Direction applied:
    
    TENSION = GAP-OPEN:
      → V chord → brain predict "I should come next"
      → I CHƯA TỚI → gap: "resolution nên ở đây nhưng chưa có"
      → = Chunk-Gap (Body-Feedback-Mechanism §3.3)
      → Body signal: bứt rứt nhẹ, chờ đợi, anticipation
      → = prediction-delta + coherence predicted → dopamine (anticipation)

    RESOLUTION = GAP-FILL:
      → I chord arrives → MATCH gap direction CHÍNH XÁC
      → = Gap-Direction §1: fill match direction → reward
      → Body signal: thỏa mãn, "đúng rồi", release
      → = Body-Feedback-Precondition pass → opioid (experience)

    DECEPTIVE CADENCE = DIRECTION MISMATCH:
      → Brain predict I → nhưng nhận vi (relative minor)
      → = Prediction miss NHƯNG coherent (vi shares notes with I)
      → = PE + partial coherence → Cheung 2019 model
      → Body: "surprise nhưng hay" → VTA fire + partial opioid
      → = Goldilocks zone for harmonic surprise

  ⭐ TOÀN BỘ BÀI NHẠC = CHUỖI GAP-OPEN → GAP-FILL:
    Verse: moderate tension (build)
    Pre-chorus: increasing tension (gap widening)
    Chorus: resolution (gap fill — partial or full)
    Bridge: HIGH tension (new gap, unexpected)
    Final chorus: BIGGEST resolution (largest gap-fill → peak reward)
    → = Designed sequence of prediction-delta oscillation

  🟢 Meyer 1956: foundational, 3,000+ citations
  🟢 Huron 2006: ITPRA theory, evolutionary grounding
  🟡 Gap-open/gap-fill mapping: framework application
```

---

## §3b — Hierarchical Nesting: Tension-Resolution ở MỌI Cấp Độ

```
⭐⭐ FRACTAL STRUCTURE — CÙNG PATTERN, MỌI TIMESCALE:

  Tension-resolution KHÔNG chỉ xảy ra ở level bài nhạc (intro→peak→resolve).
  Nó xảy ra ĐỒNG THỜI ở MỌI cấp độ — từ 1 beat tới cả bài.
  = HIERARCHICAL NESTING = cùng nguyên tắc, lặp lại ở mỗi zoom level.


  ═══ CẤP 1 — TRONG 1 BEAT (~500ms) ═══

    🟢 Wang et al. 2024 (Cerebral Cortex):
      Strong beat = tension CAO hơn weak beat (measured bằng EEG + rating)
      2/4: t(34)=5.75, p<0.001
      3/4: F(2,68)=42.25, p<0.001, η²=0.554
      4/4: F(3,102)=37.85, p<0.001, η²=0.527
      → Effect size η²>0.5 = RẤT MẠNH
      → Beta-band desynchronization correlate với tension (r=-0.142)

    → TRONG MỖI NHỊP: strong beat = micro-tension → weak beat = micro-release
    → = Prediction-delta cycle NHỊP ĐẬP (500ms per cycle at 120 BPM)
    → Appoggiatura (note lệch trên strong beat → resolve stepwise)
      = textbook micro tension-resolution trong 1 beat


  ═══ CẤP 2 — TRONG 1 PHRASE (4 bars, ~8 giây) ═══

    🟢 Huron 1996 (Computing in Musicology, 6,251 melodies):
      Melodic arch = DOMINANT contour: melody đi LÊN nửa đầu, XUỐNG nửa sau
      → Highest pitches cluster near/slightly past CENTER of phrase
      → Replicated: Baker 2019, Goldstein et al. 2023

    🟢 Narmour 1990 (Implication-Realization model):
      Large interval → brain EXPECTS reversal ("gap-fill"):
        Jump UP → expect stepwise motion DOWN → resolution
      → Schellenberg 1997: simplified to 2 factors (proximity + reversal)
        = equal/better predictive accuracy

    → MỖI PHRASE: melody depart from tonic area → rise → RETURN
    → = Gap-OPEN (depart) → Gap-FILL (return) within 8 seconds
    → ⭐ Bạn đúng: "note gốc → lên → về" = melodic arch = dominant pattern


  ═══ CẤP 3 — TRONG 1 SECTION (verse/chorus, ~30-60 giây) ═══

    🟢 Lerdahl & Krumhansl 2007 (Music Perception 24:329-366):
      4-component tension model: prolongational structure + pitch-space distance
      + surface tension + melodic attraction
      → Predicts listener continuous tension ratings SIGNIFICANTLY
      → Tension builds toward CADENCE points → resolves AT cadences
      → = Section-level tension arc: build → cadential resolution

    → Chord progression within section: depart from I → build tension → return to I
    → = Harmonic gap-open → gap-fill at section boundary


  ═══ CẤP 4 — CẢ BÀI (3-4 phút) ═══

    → Macro arc: intro → build → peak → resolve (§4.3)
    → = Largest-scale tension-resolution
    → Bridge = widest gap-open → final chorus = largest resolution


  ═══ CẤP 5 — ALBUM / CONCERT ═══

    → Opening track/song → journey → encore/closing
    → = Even larger scale, same principle


  ⭐⭐ FRACTAL EVIDENCE — 1/f NOISE:

    🟢 Voss & Clarke 1975 (Nature):
      Music amplitude fluctuations exhibit 1/f noise (pink noise)
      = Equal energy per octave of frequency
      = Statistical signature of SELF-SIMILAR processes
      → SAME statistical pattern at DIFFERENT timescales

    🟢 Hsü & Hsü 1991 (PNAS):
      Bach + Mozart PITCH interval sequences = fractal geometry
      "Scale-independency" — same pattern at different zoom levels
      → Directly supports: tension-resolution is self-similar across hierarchy

    🟢 Levitin et al. 2012: 1/f confirmed in RHYTHM
    🟢 Hennig et al. 2011 (PLOS ONE):
      1/f from short-range autocorrelations at MULTIPLE hierarchical time lags
      → Fractal structure ENABLES prediction (Rankin et al. 2014, JASA)


  ⭐ FRAMEWORK MAPPING — MULTI-SCALE PREDICTION:

    Mỗi cấp = 1 prediction-delta cycle:
      Beat (500ms): micro-prediction → micro-match → micro-reward
      Phrase (8s): melodic arch → depart-return → phrase reward
      Section (30-60s): harmonic build → cadence → section reward
      Song (3-4 min): macro arc → final resolution → peak reward

    ALL LEVELS FIRE SIMULTANEOUSLY:
      → Não xử lý prediction ở TẤT CẢ levels cùng lúc
      → Farbood 2012: "moving perceptual window" tracks tension
        at MULTIPLE timescales simultaneously
      → = COMPOUND prediction matching across hierarchy
      → = Tại sao music reward PHONG PHÚ: không chỉ 1 prediction stream,
        mà NHIỀU prediction streams ở nhiều timescales ĐỒNG THỜI

    ⭐ CONNECTS TO 07 §3:
      "Multi-scale prediction matching" = what this section formalizes
      Level 1-5 = 5 simultaneous prediction channels × multi-modal
      = Compound reward from BOTH hierarchy (5 levels) AND modality (3+ senses)

  🟢 Fractal 1/f: Voss & Clarke 1975, Hsü & Hsü 1991 (established)
  🟢 Beat-level tension: Wang et al. 2024 (strong effect)
  🟢 Melodic arch: Huron 1996, 6,251 melodies (established)
  🟢 Section-level tension: Lerdahl & Krumhansl 2007 (validated model)
  🟡 Multi-scale compound reward: framework mapping
```

---

## §3c — Integer Ratio Principle: 1 Nguyên Lý Xuyên Tầng

```
⭐ UNIFYING PRINCIPLE ACROSS PITCH, RHYTHM, AND OSCILLATION:

  Não lock phase DỄ khi tỷ lệ giữa các tần số = SỐ NGUYÊN ĐƠN GIẢN.
  Não VẬT LỘN khi tỷ lệ phức tạp.

  CÙNG 1 nguyên lý hoạt động ở MỌI tầng âm nhạc:

  ┌──────────────────────────────────────────────────────────────────┐
  │ Tầng              │ Simple ratio → dễ chịu  │ Complex → khó chịu│
  ├────────────────────┼─────────────────────────┼───────────────────┤
  │ PITCH              │ Octave 2:1, Fifth 3:2   │ Minor 2nd 16:15   │
  │ (consonance/       │ → consonance            │ → dissonance      │
  │  dissonance)       │                         │                   │
  ├────────────────────┼─────────────────────────┼───────────────────┤
  │ RHYTHM             │ Beat:downbeat 2:1       │ 120 vs 121 BPM    │
  │ (groove/no groove) │ Hihat:beat 2:1 → groove │ → phase drift     │
  │                    │                         │ → mất groove      │
  ├────────────────────┼─────────────────────────┼───────────────────┤
  │ NESTED OSCILLATION │ Delta:Theta ≈ 1:2-4     │ Tần số lệch →    │
  │ (brain waves)      │ → lock tốt              │ không lock        │
  └──────────────────────────────────────────────────────────────────┘


  ⭐ VÍ DỤ CỤ THỂ — bài 120 BPM:

    Layer          BPM     Tỷ lệ với beat    Lock?
    ──────────────────────────────────────────────
    Downbeat       60      1:2                ✅ lock dễ
    Beat (gốc)     120     1:1                ─
    Hihat          240     2:1                ✅ lock dễ
    16th notes     480     4:1                ✅ lock dễ
    ──────────────────────────────────────────────
    Layer lệch     121     ~1:1.008           ✗ phase drift → mất groove

    → Steve Reich "Piano Phase" (1967): 2 piano lệch tempo rất nhẹ
      → Kết quả: hypnotic, disorienting, tension — KHÔNG phải groove
      → = DESIGNED violation of integer ratio → DESIGNED tension
      → 🟢 Landmark minimalist piece, confirms principle by violation


  ⭐ TẠI SAO ĐÂY LÀ 1 NGUYÊN LÝ, KHÔNG PHẢI 3:

    Consonance (pitch), groove (rhythm), neural entrainment (oscillation)
    thường được nghiên cứu RIÊNG ở 3 subfields.
    Nhưng cơ chế NÃO = CÙNG 1:
      → Phase-locking between oscillators
      → Simple integer ratios = resonance peaks
      → Complex ratios = destructive interference

    = Tại sao consonance SƯỚNG VÀ groove SƯỚNG bằng CÙNG cơ chế:
      cả hai = brain oscillators lock phase dễ → coherence → reward

    🟢 Large & Palmer 2002 (Cognitive Science 26(1):1-37):
      Neural resonance theory — internal oscillators resonate at
      integer-ratio related frequencies to external rhythmic patterns
      ⚠️ v1.2: Journal corrected (NOT Ecological Psychology)

    🟢 Lots & Stone 2008 (Perception):
      Cross-domain: temporal ratios judged "better" when near
      simple integer ratios — applies to BOTH pitch AND rhythm

    🟢/⚠️ Bowling & Purves 2015 (PNAS 112:11155-11160):
      Argue consonance = attraction to voice-like harmonic spectra (biological)
      ⚠️ DEBATE ONGOING: McDermott 2016 found Tsimané people DON'T share
      consonance preferences → suggests cultural learning dominates.
      Bowling 2017 response questioned McDermott's methods.
      Current consensus: both biology AND culture contribute, relative weight debated.
      → "Across cultures" claim in drill = OVERSIMPLIFIED. See file 01 §8.

  FRAMEWORK MAPPING:
    Integer ratio = PREDICTION EFFICIENCY condition
    Simple ratio → oscillators PREDICT next cycle easily
    → Prediction MATCH → reward (prediction-delta = positive coherence)
    Complex ratio → oscillators CANNOT predict reliably
    → Prediction MISS → discomfort (prediction-delta = error signal)

    = Body-Feedback-Mechanism §3: prediction-delta
    = §2 (BPM) + §1 (pitch) + §3b (nested) UNIFIED into 1 principle

  🟢 Phase-locking + integer ratios: established (psychoacoustics + neuroscience)
  🟢 Cross-domain application (pitch + rhythm): Large & Palmer 2002, Lots & Stone 2008
  🟡 "1 principle, not 3": framework unification (converging ✅ evidence)
```

---

## §4 — Form System: Verse-Chorus, Song Length, Arc

### §4.1 — Verse-Chorus Dominance

```
🟢 VERSE-CHORUS = 80-90%+ BILLBOARD TỪ 1980s:

  🟢 Summach 2012 (PhD, Yale):
    1955-1989: shift from AABA (Tin Pan Alley) → verse-chorus
    By mid-1960s: verse-chorus rapidly taking over rock

  🟢 De Clercq 2017 (Music Theory Online 23.3):
    By early 1980s: verse-chorus dominates Billboard No.1 hits

  🟢 Nobile 2022 (Music Theory Online 28.3):
    By ~2010: verse-prechorus-chorus = "default" mainstream pop

  TYPICAL STRUCTURE:
    Intro → Verse 1 → Pre-Chorus → Chorus →
    Verse 2 → Pre-Chorus → Chorus →
    Bridge → Final Chorus → Outro

  TẠI SAO VERSE-CHORUS THẮNG:

    ① CHORUS = PREDICTION CONFIRMED → REWARD:
      → Chorus repeats → listener ALREADY KNOWS melody/lyrics
      → Hearing familiar chorus = prediction MATCH
      → = Reward from prediction completion (Cheung 2019)
      → = "Phần mà ai cũng hát theo"

    ② VERSE = MODERATE NOVELTY → VTA FIRE:
      → Verse lyrics DIFFERENT each time → prediction-delta
      → Verse melody/chords SIMILAR → enough context to follow
      → = Goldilocks: new enough for attention, familiar enough for coherence

    ③ OSCILLATION VERSE ↔ CHORUS:
      → Verse (novelty, prediction-delta) → Chorus (familiar, reward)
      → → Verse (novelty again) → Chorus (reward again)
      → = DESIGNED oscillation → prevents both boredom AND overwhelm
      → = Boredom.md formula applied: prediction-delta NEVER stays at 0

    ④ BRIDGE = HIGH PREDICTION-DELTA INJECTION:
      → New harmonic territory → VTA fire STRONG
      → After bridge → chorus = LARGEST prediction confirmed
      → = Biggest gap-open → biggest gap-fill → peak reward

  🟡 TRƯỚC VERSE-CHORUS:
    AABA (Tin Pan Alley, 1920s-1950s):
      A section × 3 + B (bridge) + A
      → Also has repetition + contrast, but LESS oscillation
      → Verse-chorus = MORE frequent reward cycles
      → = "Upgrade" cho prediction oscillation rate
```

### §4.2 — Song Length: ~3-4 Minutes

```
🟢 TẠI SAO ~3-4 PHÚT:

  HISTORICAL ORIGIN:
    🟢 78 rpm records: ~3-5 min per side (physical constraint)
    → 45 rpm singles: reinforced ~3 min standard
    → AM radio: preferred short songs (more ads)
    → = TECHNOLOGICAL constraint → became CULTURAL norm

  CURRENT DATA:
    → 1990: average Billboard Hot 100 song = ~4:00
    → 2020: average = ~3:17 (Washington Post 2024)
    → 2022: half of US top 20 songs < 3 minutes
    → Streaming era: shorter trending (Spotify pays per play after 30s)

  🟡 FRAMEWORK MAPPING — TẠI SAO ~3-4 PHÚT "ĐÚNG":

    → KHÔNG CHỈ technological accident:
    → 3-4 phút ≈ GOLDILOCKS cho attention + satiation:
      < 2 phút: chưa đủ thời gian build prediction model → weak reward
      3-4 phút: enough repetition to compile chunks + variety to prevent boredom
      > 6 phút: prediction-delta risk reaching 0 → boredom risk ↑

    → Cyclic satiation (Gap-Body-Need §2):
      1 bài nhạc = 1 Cyclic cycle
      Fill → satisfaction → off → ready for next
      ~3-4 phút ≈ 1 natural Cyclic unit cho auditory experience

    → EXCEPTION: classical, progressive, ambient = LONGER
      → Different audience (more compiled chunks → wider Goldilocks window)
      → Different satiation type (Generative/Tonic, not Cyclic)

  🟢 Historical origin: documented
  🟡 3-4 min as natural Goldilocks: framework hypothesis
```

### §4.3 — Emotional Arc: Build → Peak → Resolve

```
🟡 TYPICAL POP SONG ARC:

  ┌──────────────────────────────────────────────────────────┐
  │                                                          │
  │  Emotional                    ★ Peak                     │
  │  Intensity        ★         (final chorus)               │
  │            ★    (chorus)   ↗                              │
  │           ↗    ↗     ↘   ↗ ★ (bridge)                    │
  │     ★   ↗    ↗       ↘ ↗                                 │
  │   (intro)  (verse)    ↘↗                                  │
  │  ↗                   (verse 2)                            │
  │ ↗                                                  ↘      │
  │                                                   (outro) │
  │──────────────────────────────────────────────────────────│
  │  0:00  0:30  1:00  1:30  2:00  2:30  3:00  3:30  4:00  │
  └──────────────────────────────────────────────────────────┘

  MAPPING ONTO PREDICTION FRAMEWORK:
    Intro:       establish tonic + tempo → build prediction BASELINE
    Verse 1:     introduce melody/lyrics → prediction model FORMING
    Pre-chorus:  increase tension → prediction-delta RISING
    Chorus 1:    release + familiar hook → prediction CONFIRMED → reward
    Verse 2:     new lyrics, same melody → moderate delta (known structure)
    Bridge:      NEW harmonic territory → prediction-delta PEAK
    Final chorus: BIGGEST resolution → prediction MOST confirmed → peak reward
    Outro:       wind down → prediction-delta → 0 → satisfaction

  = Designed as PREDICTION-DELTA CURVE optimized for Goldilocks
```

---

## §5 — Repetition: Why Music Repeats Itself

### §5.1 — Hard Numbers on Repetition

```
🟢 MUSIC = HIGHLY REPETITIVE (quantified):

  🟢 Colin Morris 2017 (Lempel-Ziv compression analysis):
    Average song compressibility:
      1960: 45.8% compressible
      2014: 54% compressible
    → Music became MORE repetitive over 50 years

    Billboard Top 10 songs = 3-6% MORE compressible than average
    → = Hit songs are MORE repetitive than non-hits
    → Repetition PREDICTS commercial success

    Extreme: Daft Punk "Around the World" = 98% compressible

  🟢 Margulis 2014 (On Repeat, Oxford University Press):
    Repetition = FUNDAMENTAL to music experience
    "Repetition is a defining feature of music"
    Mere repetition → increased liking (processing fluency)
    Repeated passages sound MORE "musical" than first hearing

  NOTE: Morris data = LYRIC compression.
  Musical repetition (melody, harmony, rhythm) = estimated even HIGHER.
  Chorus alone = repeats 3-4× per song.
  → Actual musical repetition likely 60-70%+ of total content.
```

### §5.2 — Why Repetition Works

```
🟡 FRAMEWORK EXPLANATION — 3 REASONS:

  ① PREDICTION MODEL TRAINING:
    → Lần 1 nghe chorus: prediction model FORMING
    → Lần 2: model IMPROVING → some PE still (details)
    → Lần 3+: model GOOD → prediction match → reward RELIABLE
    → = Repetition = TRAINING DATA cho internal model
    → = "Chưa biết = không có gap" (Gap-Direction §3):
      cần nghe ĐỦ LẦN để gap HÌNH THÀNH → reward POSSIBLE

  ② PROCESSING FLUENCY → LIKING:
    → 🟢 Reber et al. 2004: easier processing = experienced as POSITIVE
    → Repetition → easier processing → misattributed as "hay"
    → = Body interpret fluency as QUALITY signal
    → ≠ deception — fluency IS a valid quality signal
      (things that are coherent ARE easier to process)

  ③ GOLDILOCKS MAINTENANCE:
    → Too much novelty = PE quá cao → overwhelming
    → Too much repetition = PE = 0 → boredom
    → DESIGNED repetition with variation:
      Chorus same melody + DIFFERENT intensity/production each time
      → = Enough familiar for prediction + enough variation for PE
      → = Goldilocks MAINTAINED across song duration
```

---

## §6 — Cross-Cultural: Universal vs Learned

### §6.1 — What IS Universal

```
🟢 CROSS-CULTURAL UNIVERSALS (established):

  🟢 Mehr, Singh et al. 2019 (Science, 315 societies):
    → Music = UNIVERSAL across all sampled cultures
    → Certain forms (lullabies, dance, healing, love songs)
      have cross-cultural acoustic regularities
    → Within-society variation 6× GREATER than between-society variation

  🟢 Savage et al. 2015 (PNAS, 304 recordings):
    18 statistical universals identified:
      → Discrete pitches (not continuous)
      → ≤ 7 scale degrees per octave
      → Repetitive rhythmic patterns
      → Group coordination
      → Hierarchical meter
    → No ABSOLUTE universals, but STRONG tendencies

  🟢 Pentatonic scale: appears independently in:
    → Chinese, Japanese, Korean, Celtic, West African,
      sub-Saharan African, Native American, Andean
    → Independent emergence across unconnected cultures, every continent

  🟢 Tonal center exists in:
    → Western music (tonic)
    → Indian raga (Sa — always present as drone)
    → Arabic maqam (qarar — tonal center)
    → Gamelan (cyclic gong structure center)
    → = Cross-cultural convergence on "home note" concept

  🟢 Layered rhythm exists in:
    → African polyrhythm (multiple layers over regular pulse)
    → Western pop (drums + bass + melody layers)
    → Indian tala (rhythmic cycle)
    → = Convergence on "multiple layers over regular pulse"
```

### §6.2 — What IS Learned

```
🟢 CULTURALLY SPECIFIC (NOT universal):

  🟢 McDermott et al. 2016 (Nature 535):
    Tsimané people (remote Bolivia): did NOT share Western
    consonance > dissonance preference
    → Consonance preference = LEARNED, not innate

  🟡 Major = happy / Minor = sad:
    REVERSED for Northwest Pakistani listeners
    → Tracks prevalence of chord types in native music
    → = Compiled association, NOT hardwired

  🟡 Specific scale systems:
    → 12-TET (Western) ≠ universal
    → 24-TET (Arabic), gamelan slendro/pelog, raga scales
    → = Culturally specific BUT all share: discrete pitches + hierarchy

  🟡 Form structures:
    → Verse-chorus = Western pop (1960s+)
    → Indian raga: development-based (no chorus)
    → Arabic maqam: improvisation-based
    → = Culturally specific structures, DIFFERENT from each other
```

### §6.3 — Framework Interpretation

```
🟡 UNIVERSAL = PREDICTION ARCHITECTURE CONSTRAINTS:
  → Tonal center (prediction anchor)
  → Regular pulse (entrainment)
  → Discrete pitches (categorical → predict-able)
  → Hierarchical structure (levels of prediction)
  → Repetition (training data)
  → = Brain prediction architecture → SAME everywhere

  LEARNED = SPECIFIC SOLUTIONS to those constraints:
  → 12 notes vs 5 vs 7 vs 24
  → 4/4 vs 7/8 vs tala
  → Verse-chorus vs raga development
  → Major-happy vs other associations
  → = KHÁC implementation, CÙNG underlying constraint

  ⭐ Analogy:
  → Universal: "buildings need foundation" (gravity constraint)
  → Learned: "foundation = concrete" vs "foundation = stone" vs "foundation = stilts"
  → Different solutions, same constraint
```

---

## §7 — Framework Mapping: Each Feature = Prediction Constraint

```
⭐⭐ COMPREHENSIVE MAP:

  ┌──────────────────┬──────────────────────────┬────────────────────────────┐
  │ Music Feature    │ Brain Constraint          │ Framework Mechanism        │
  ├──────────────────┼──────────────────────────┼────────────────────────────┤
  │ Tonic center     │ Prediction needs baseline│ Gap-Direction: anchor      │
  │                  │ (reference point for PE)  │ = prediction model center  │
  │                  │                          │                            │
  │ BPM regular      │ Oscillators need phase-  │ Body-Feedback-Mechanism:   │
  │                  │ locking signal            │ entrainment → coherent     │
  │                  │                          │ processing → compound      │
  │                  │                          │                            │
  │ 4/4 time         │ Binary = lowest complex- │ Body-Feedback-Precondition Precondition-2: lower chunk req │
  │                  │ ity for meter prediction  │ = wider accessibility      │
  │                  │                          │                            │
  │ I-IV-V chords    │ Simplest harmonic set    │ Background-Pattern: gist   │
  │ (top 3 in most   │ around tonic → easiest   │ extraction → genre = few   │
  │  corpora)        │ prediction model          │ chords, many songs         │
  │                  │                          │                            │
  │ Tension-         │ Gap-open → gap-fill      │ Gap-Direction: direction   │
  │ resolution       │ = prediction + reward     │ match → reward. V→I =     │
  │ (V→I)           │ cycle                     │ strongest direction fill   │
  │                  │                          │                            │
  │ Verse-chorus     │ prediction-delta needs   │ Boredom.md: oscillation    │
  │                  │ oscillation (not flat)   │ prevents delta = 0.        │
  │                  │                          │ Cyclic channel: fill→off→  │
  │                  │                          │ fill                       │
  │                  │                          │                            │
  │ Repetition       │ Model needs training;    │ "Chưa biết = không gap":  │
  │ (45→54%)        │ fluency → liking          │ repetition builds chunks   │
  │                  │                          │ → gap FORMS → reward       │
  │                  │                          │                            │
  │ ~3-4 min length  │ Attention window +       │ Cyclic satiation: 1 song  │
  │                  │ satiation timing          │ = 1 Cyclic unit           │
  │                  │                          │                            │
  │ Emotional arc    │ prediction-delta curve   │ Reward-Calibration:        │
  │ (build→peak→     │ optimized for sustained  │ Goldilocks maintained      │
  │  resolve)        │ Goldilocks               │ across duration            │
  │                  │                          │                            │
  │ Modulation       │ Prediction anchor shift  │ VTA fire on NEW baseline   │
  │ (key change)     │ = novel context same     │ → "energy boost" cuối bài  │
  │                  │ content                   │                            │
  │                  │                          │                            │
  │ Bridge section   │ High prediction-delta    │ Gap-OPEN wide →            │
  │                  │ injection BEFORE final   │ return chorus = BIGGEST    │
  │                  │ resolution                │ gap-fill → peak reward     │
  └──────────────────┴──────────────────────────┴────────────────────────────┘
```

---

## §8 — Non-Standard Structures: Tại Sao Hiếm + Khi Nào Thành Công

```
🟡 NON-STANDARD = HIGHER Precondition-2 REQUIREMENT:

  STANDARD structures (verse-chorus, 4/4, I-IV-V):
    → Low Precondition-2 requirement: most listeners CAN predict
    → = Wide audience → commercial success
    → = "Ai cũng entrain được"

  NON-STANDARD structures:
    → Higher Precondition-2: need more compiled chunks to follow
    → = Narrower audience → niche success
    → = "Cần nghe quen mới thấy hay"


  SUCCESSFUL NON-STANDARD EXAMPLES:

  Bohemian Rhapsody (Queen 1975):
    → 6 min, no chorus, 5 distinct sections
    → = prediction-delta CONTINUOUSLY HIGH → requires RICH chunk library
    → SUCCESS vì: compositional craft CỰC CAO + cultural moment
    → Every section INTERNALLY coherent → Body-Feedback-Precondition Precondition-4 still met per-section
    → = Exception proves rule: needs MORE coherence to compensate no repetition

  Progressive Rock (Yes, Pink Floyd, Genesis):
    → Extended structures, complex meters, minimal repetition
    → Audience: compiled music listeners (high Precondition-2)
    → → Niche nhưng LOYAL (gu cứng = snowball)

  Jazz Improvisation:
    → Real-time composition → prediction-delta HIGH continuously
    → Requires: DEEP compiled jazz chunks to follow
    → → Precondition-2 barrier = HIGH → audience = jazz-compiled listeners only

  Ambient (Brian Eno):
    → NO traditional structure → pure Tonic channel
    → → Prediction-delta ~0 → NOT reward-seeking
    → → Purpose: body-base modulation, not reward


  GENERAL PRINCIPLE:
    → Standard structure = optimize for WIDEST Goldilocks zone
    → Non-standard CAN succeed IF:
      ① Internal coherence VERY HIGH (compensate lack of repetition)
      ② Target audience has HIGH Precondition-2 (enough chunks to follow)
      ③ Cultural moment supports novelty (collective appetite)
    → = NOT "non-standard = bad" — "non-standard = higher barrier"

  🟡 Precondition-2 barrier analysis: framework application
```

---

## §9 — Honest Assessment

```
  UNDENIABLE FACTS (🟢):
    → 12-TET mathematical basis
    → ~94% pop = 4/4 time signature
    → Spontaneous motor tempo ~120 BPM (Moelants 2002, N=74,000+)
    → Tonal hierarchy (Krumhansl 1982, cross-culturally replicated)
    → PFC tracks tonal center (Janata 2002)
    → Tonal hierarchy = learned (Hannon & Trainor 2007)
    → Tension-resolution as emotional mechanism (Meyer 1956)
    → Verse-chorus dominance 1980s+ (Summach, De Clercq, Nobile)
    → Repetition increases with hits (Morris 2017)
    → Music universal, specific features cultural (Mehr 2019, Savage 2015)
    → Consonance preference = learned (McDermott 2016)
    → Neural entrainment (Snyder/Large, Nozaradan, Fujioka)

  FRAMEWORK SYNTHESIS (🟡):
    → Tonic = prediction anchor (logical, Janata supports)
    → BPM = sync optimization (logical, entrainment data supports)
    → 4/4 = lowest complexity entrainment (logical)
    → Verse-chorus = prediction oscillation (logical application)
    → Repetition = gap formation training (logical, fluency data supports)
    → ~3-4 min = Cyclic satiation unit (logical, weaker support)
    → Non-standard = higher Precondition-2 (logical application)
    → Emotional arc = prediction-delta curve (logical)
    → Cultural evolution = prediction constraint filter (hypothesis)

  CORRECTED (v1.1):
    → I-IV-V "~62%": clarified as derived sum from 100-song corpus, not standalone figure
    → Prediction as sole driver: Savage 2021 adds social bonding as CO-EQUAL
    → 4/4 dominance: noted as Western-specific (Balkan, Indian, Turkish use asymmetric)

  DEBATED (⚠️):
    → 12 notes = "best" compromise (alternatives exist: 19-TET, 31-TET)
    → Hit prediction from audio features alone (Pachet 2012: not reliable)
    → Exact % verse-chorus (no single definitive large-N study)
    → Whether 120 BPM = truly "optimal" or just "most common"
    → Prediction vs social bonding: which is PRIMARY driver (both have evidence)
```

---

## §10 — Cross-References

```
PRIMARY:
  Prediction-Error-Is-Not-Reward.md v2.0 — PE + coherence + Goldilocks
  Gap-Direction.md v2.0 — "chưa biết = không có gap", direction match
  Body-Feedback-Mechanism.md v2.1 — chunk dynamics, prediction-delta

SECONDARY:
  Background-Pattern.md v2.0 — gist extraction, Triple Bias, snowball
  Reward-Calibration.md v1.1 — Goldilocks per-gap, 3 zones
  Boredom.md v2.0 — prediction-delta = 0
  Modality.md v1.0 — multi-modal encoding

EVIDENCE:
  01-Sound-Brain-Neuroscience.md — §3 (prediction), §6 (entrainment)
  03-Musical-Notation-Architecture.md — notation reference, §1-§7

WITHIN DRILL:
  02-Sound-Background-Pattern.md — gist → "gu", genre context
  03-Sound-Reward-Pipeline.md — 7-step, Cheung 2019 validation
  05-Multi-Modal-Compound.md — coherence condition, multi-modal

RESEARCH CITATIONS:
  Krumhansl & Kessler 1982 — Psychological Review — tonal hierarchy
  Janata et al. 2002 — Science — PFC tracks tonal center
  Hannon & Trainor 2007 — tonal sensitivity learned
  Moelants 2002 — 7th ICMPC — spontaneous motor tempo 120 BPM, N=74,000
  Large & Snyder 2009 — NYAS — neural resonance theory
  Snyder & Large 2005 — beta/gamma entrainment
  Fujioka et al. 2009, 2012 — beta replication
  Nozaradan et al. 2011 — J Neuroscience — steady-state EEG
  De Clercq & Temperley 2011 — Popular Music — rock harmony corpus
  De Clercq 2023 — Musicae Scientiae — harmonic rhythm
  Meyer 1956 — Emotion and Meaning in Music — foundational
  Huron 2006 — Sweet Anticipation — ITPRA theory
  Cheung et al. 2019 — Current Biology — 80k chords
  Summach 2012 — PhD Yale — form 1955-89
  Nobile 2022 — Music Theory Online — verse-prechorus-chorus
  Margulis 2014 — On Repeat — Oxford
  Morris 2017 — Lempel-Ziv compression analysis
  Reber et al. 2004 — processing fluency
  Mehr et al. 2019 — Science — 315 societies
  Savage et al. 2015 — PNAS — 18 statistical universals
  McDermott et al. 2016 — Nature — consonance = learned
  Aravind et al. 2025 — arXiv — beat-tracking 4/4 dominance
  Savage et al. 2021 — BBS — music as coevolved social bonding system
```

---

> *06-Music-Architecture-Prediction v1.0 — Music architecture = prediction architecture optimization.
> ~94% pop = 4/4. BPM clusters 120 BPM = locomotion resonance. I-IV-V = top 3 chords.
> Verse-chorus 80-90%+ Billboard 1980s+. Hit songs 3-6% more repetitive.
> Tonic = prediction anchor. BPM = sync signal. Repetition = training data.
> Tension-resolution = gap-open → gap-fill cycle.
> Universal: tonal center, regular pulse, discrete pitch, hierarchy, repetition.
> Learned: specific scales, meters, forms, consonance preference.
> Non-standard = higher Precondition-2 barrier, not "wrong."*
