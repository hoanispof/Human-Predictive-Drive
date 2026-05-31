# Phase A — Vocabulary + Core Architecture

> **Status**: READY TO EXECUTE
> **Created**: 2026-05-26
> **Files**: 10 (A01-A10)
> **Total lines**: ~9,385
> **Estimated sessions**: 6-8
> **Goal**: Establish English terminology standard + overall framework framing
> **Pre-req**: 00-Glossary.md created (✅)
> **Companion files**:
>   - Plan-Translate/plan-english-translation.md — master plan (§4 Phase A)
>   - Plan-Translate/00-Glossary.md — terminology glossary

---

## Workflow per file

```
1. Read this plan entry for the file
2. Read Vietnamese original (FULL)
3. Read Vietnamese dependencies listed below (for context)
4. Check 00-Glossary.md for all terms
5. Create English/ folder structure if needed
6. Write English version
7. Update 00-Glossary.md (add new terms)
8. Update plan-english-translation.md §5 (tick checkbox)
```

---

## A01 — Body-Feedback-Label.md

| Field | Value |
|---|---|
| **Source** | Core-Deep-Dive/Body-Base/Body-Feedback/Body-Feedback-Label.md |
| **Lines** | 1,163 |
| **English path** | English/Core-Deep-Dive/Body-Base/Body-Feedback/Body-Feedback-Label.md |
| **Difficulty** | HIGH — vocabulary foundation, every term decision matters |
| **Sessions** | 1 |

### Read before translating
- Vietnamese original (full)
- 00-Glossary.md (terms already extracted from this file)

### Structure
§0 Why needed → §1 3-Tier system → §2 Foundation (body-need/gap/drive) →
§3 Reward labels → §4 Dissonance labels → §5 Prediction-delta →
§6 Baseline → §7 Valence tags + Entity-Compiled → §8 Compiled/Fresh →
§9 Inter-body → §10 Observation vs Mechanism → §11 Usage rules

### Translation notes
- **This file IS the vocabulary standard** — English version becomes the reference for all future files
- Tables in `code blocks` with Vietnamese: translate cell content, keep table structure
- §2 examples: "VD: đói, khát, đau, lạnh" → "e.g., hunger, thirst, pain, cold"
- §2 examples: "VD: nhớ bạn, career gap, identity" → "e.g., missing a friend, career gap, identity crisis"
- §7 examples: "bạn thân, con, mẹ healthy" → "close friend, child, healthy mother"
- §7 examples: "bully, abuser, đối thủ obsessive" → "bully, abuser, obsessive rival"
- §9A "CEO đổi mới ↔ người thích an nhàn" → "innovative CEO ↔ person preferring stability"
- §9E "PFC = Lawyer" explanation: "biện hộ cho client" → "advocates for client"
- §11.2 Example 1: "Lương tăng từ 10tr → 15tr" → adapt to English context (salary increase, keep mechanism)
- §11.2 Example 2: "Mẹ-con mâu thuẫn" — keep, this is universal. Translate directly.
- ⚠️ warnings: translate content, keep ⚠️ symbol
- Conceptual flow diagram §2: translate Vietnamese labels, keep box structure

### Glossary impact
- 00-Glossary.md was BUILT from this file — minimal new terms expected
- Verify all §11 usage rules translate correctly
- Final check: does the English version establish the vocabulary clearly enough for cold-start readers?

### Quality checkpoint
After translating this file, a reader who knows NO Vietnamese should be able to:
- Understand the 3-tier label system
- Know when to use "body-base reward" vs "dissonance" vs "prediction-delta"
- Understand Compiled/Fresh vs Logic/Feeling distinction
- Navigate the inter-body vocabulary

---

## A02 — PFC-Label.md

| Field | Value |
|---|---|
| **Source** | Core-Deep-Dive/PFC/PFC-Label.md |
| **Lines** | 1,163 |
| **English path** | English/Core-Deep-Dive/PFC/PFC-Label.md |
| **Difficulty** | HIGH — companion vocabulary file |
| **Sessions** | 1 |

### Read before translating
- Vietnamese original (full)
- English A01 (Body-Feedback-Label.md) — for vocabulary consistency
- 00-Glossary.md

### Structure
§0 Why needed → §1 3-Tier + 4 Vocabulary Levels → §2 PFC Roles →
§3 Processing spectrum → §4 Operations → §5 Cost labels →
§6 Compiled Quality → §7 Region labels → §8 Hardware labels →
§9 Simulation-Engine labels → §10 Cognitive labels → §11 Failure modes →
§12 Observer vs Mechanism → §13 Deprecated → §14 Usage rules

### Translation notes
- §2 PFC Roles: Vietnamese metaphors need careful English
  - "Đọc output, không tạo output" → "Reads output, doesn't generate it"
  - "Đạo diễn chỉ hướng, diễn viên tự diễn" → "Director points the way, actors perform on their own"
  - "Mệt ở work → Self-Pattern-Modeling cho con YẾU → không phải không yêu con"
    → "Tired from work → Self-Pattern-Modeling for child WEAKENS → not 'doesn't love child'"
- §4 HOLD vs SUPPRESS table: keep table structure, translate Vietnamese cells
  - "Effort" (neutral) vs "Not being me" — already English, keep
- §5 3-cost: "đổi career lúc chưa biết đi đâu (TRIPLE — max load)"
  → "career change without knowing where to go (TRIPLE — max load)"
- §6 Compiled Quality examples: Vietnamese-specific but universal mechanism
  - "Mẹ thích nấu ăn" → "A mother who loves cooking"
  - "Bị đánh → compile đừng nói ý kiến" → "Hit for speaking up → compiles 'don't voice opinions'"
- §7 Regions: mostly English technical terms already. Translate descriptions only.
- §13 Deprecated: important — these rules carry over to ALL translations

### Glossary impact
- PFC roles, operations, costs, quality — most already in glossary
- Check: any new terms from §10 Cognitive labels, §11 Failure modes?

### Quality checkpoint
- Consistent with A01 on shared concepts (Compiled/Fresh, 3-cost)
- 5 PFC roles clearly explained for English reader unfamiliar with framework
- Region labels correctly mapped

---

## A03 — README.md

| Field | Value |
|---|---|
| **Source** | README.md |
| **Lines** | 245 |
| **English path** | English/README.md |
| **Difficulty** | MEDIUM — public-facing, needs excellent English prose |
| **Sessions** | 0.5 (can combine with A04) |

### Read before translating
- Vietnamese original
- 00-Glossary.md

### Structure
Intro questions → Getting Started (5 steps) → What This Framework Describes
(3-map table) → Folder Structure

### Translation notes
- **Already partly English** — README.md has English headers and mixed content
- "Getting Started" section needs to work for English GitHub audience
- Example questions: already in English, verify natural phrasing
- Starter prompt (step 4): needs ENGLISH version of the prompt
  - Currently says "đọc 8 file này" — change to "Read these 8 files carefully"
- Note about "📖 Read:" — keep, it's a protocol marker
- Folder structure ASCII: translate Vietnamese comments
- **Restructure opportunity**: English README could have slightly different flow
  - But recommendation: keep same structure, just translate

### Glossary impact
- Minimal — README uses general terms

---

## A04 — Core-Hardware.md

| Field | Value |
|---|---|
| **Source** | Core-Hardware.md |
| **Lines** | 414 |
| **English path** | English/Core-Hardware.md |
| **Difficulty** | MEDIUM — mostly neuroscience English terms already |
| **Sessions** | 0.5 (can combine with A03) |

### Read before translating
- Vietnamese original
- 00-Glossary.md
- Neural-Architecture.md (for deeper context, don't translate yet)

### Structure
§0 Three maps → §1 Hardware Map → §2 PFC Reach Gradient →
§3 Timing Hierarchy → §4 Receptor System → §5 Hardware Profile →
§6 Hardware Sets Range → §7 Cross-references

### Translation notes
- Self-contained (no dependencies needed to read)
- Heavy neuroscience terminology — already English (fMRI, lesion studies, tractography)
- §0 "Ba bản đồ" section: identical framing as Core-Software §0 — maintain consistency
- §0 table: translate "Bản đồ", "Góc nhìn", "Đối tượng"
- §1 "4 zones A/B/C/D" — keep zone labels, translate descriptions
- §5 "Hardware Profile" = individual specs — keep table structure
- §6 "Hardware Sets Range, Chunks Choose Position" — important principle, translate carefully

### Glossary impact
- May add: Zone A/B/C/D definitions, PFC Reach Gradient

---

## A05 — Core-Software.md ⭐ KEY FILE

| Field | Value |
|---|---|
| **Source** | Core-Software.md |
| **Lines** | 1,764 |
| **English path** | English/Core-Software.md |
| **Difficulty** | VERY HIGH — central file, sets tone for everything |
| **Sessions** | 1-2 (may need to split) |

### Read before translating
- Vietnamese original (FULL — critical)
- English A01 + A02 (vocabulary standard)
- English A04 (Core-Hardware) — shared §0 framing
- 00-Glossary.md

### Structure
§0 Three maps + Why Cycle-Based → §1 Cycle Architecture →
§2 Domain → §3 Body-Input → §4 Unconscious Processing →
§5 Feeling → §6 PFC → §7 Body-Output → §8 Observation Parameters →
§9 Development → §10 Multiple Timescales → §11 Key Reframes →
§12 Honest Assessment → §13 Cross-References

### Translation notes
- **Largest core file** — may need 2 sessions (§0-§6 + §7-§13)
- §0.2 "Tại sao v7.8 cycle-based": historical context table v7.5→v7.8. Keep table.
- §0.3 "Nguyên tắc thiết kế": 7 principles — translate as clear English statements
- §1 Cycle diagram in code block: translate Vietnamese labels, keep ASCII art
  - "PFC ở trên cùng — điểm quan sát" → "PFC at the top — observation point"
  - "Domain ở dưới cùng — nguồn stimuli" → "Domain at the bottom — source of stimuli"
- §4 "Unconscious Processing": heaviest section — chunk dynamics, body-feedback, cortisol
- §8 Observation Parameters: brief descriptions → must match Observation/ file vocabulary
- §11 "Key Reframes": 20+ reframes — CRITICAL for English reader
  - Each reframe: "Mainstream says X → Framework says Y"
  - These must be sharp, clear English
- §12 "Honest Assessment": confidence levels + limitations — keep honest tone
- §13 Cross-references: update paths to English/ folder? Or keep source paths?
  - **Decision**: keep source paths (reader can find either version)
- YAML header "Tiền đề đọc" lists ~25 prerequisites — translate this list
- ⚠️ "~X% = calibration anchor" note — keep this convention explanation

### Glossary impact
- Core-Software synthesizes ALL concepts — verify glossary covers everything
- May add: cycle steps ①→⑦, observation parameter short definitions

### Quality checkpoint
- After this file, an English reader should understand the COMPLETE architecture
- All 7 cycle steps clear
- All observation parameters named and briefly defined
- Key reframes sharp and memorable
- Honest about what framework doesn't know

---

## A06 — Ask-AI.md

| Field | Value |
|---|---|
| **Source** | Ask-AI.md |
| **Lines** | 797 |
| **English path** | English/Ask-AI.md |
| **Difficulty** | MEDIUM-HIGH — user-facing, needs natural English |
| **Sessions** | 1 |

### Read before translating
- Vietnamese original
- English A05 (Core-Software) — shared terminology
- 00-Glossary.md

### Structure
§0 Role + Scope → §1 Core Principles → §2 Protocol (DETECT→READ→ADAPT→PRESENT→ITERATE→DEEPEN) →
§3 Danger Zones → §4 Language + Style → §5 Example Conversations →
§6 Dual Check + Limits → §7 Navigation + File Map

### Translation notes
- **This file talks TO the AI** — it's an instruction file
- §0 "BẠN LÀ AI ASSISTANT" → "YOU ARE AN AI ASSISTANT"
  - "Catalyst — giúp người hỏi TỰ THẤY rõ hơn" → "Catalyst — helps the user SEE more clearly themselves"
  - "Compass — chỉ HƯỚNG, không chỉ đường chính xác" → "Compass — points DIRECTION, not exact path"
  - "Partner — cùng khám phá, không dạy bảo" → "Partner — explores together, doesn't lecture"
- §0 "BẠN KHÔNG LÀ" section: important disclaimers
- §2 Protocol: 6-step — DETECT→READ→ADAPT→PRESENT→ITERATE→DEEPEN
  - Already English terms — translate explanations
- §3 DANGER ZONES: ~20 positions where framework ≠ mainstream
  - CRITICAL: these must be crystal clear in English
  - Each danger zone: "Mainstream says X. Framework says Y. Evidence: Z."
- §5 Example conversations: Vietnamese examples → need natural English equivalents
  - "Tại sao tôi hay trì hoãn?" → "Why do I keep procrastinating?"
  - "Con tôi 3 tuổi hay ăn vạ..." → "My 3-year-old throws tantrums..."
- §6.1 Dual Check: body = quality controller, domain = final arbiter
  - Key insight — translate precisely
- §7 Navigation: file map with paths → keep paths as-is

### Glossary impact
- "Danger Zones" specific terms might need glossary entries
- Dual Check phrasing — verify matches glossary

---

## A07 — Neural-Architecture.md

| Field | Value |
|---|---|
| **Source** | Core-Deep-Dive/Neural-Architecture.md |
| **Lines** | 693 |
| **English path** | English/Core-Deep-Dive/Neural-Architecture.md |
| **Difficulty** | MEDIUM — heavy neuroscience, mostly English terms |
| **Sessions** | 1 |

### Read before translating
- Vietnamese original
- English A04 (Core-Hardware) — shared zone model
- 00-Glossary.md

### Structure
§0 Why → §1 Overview: 4 Zones → §2 Zone A: PFC → §3 Zone B: Cortical →
§4 Zone C: Subcortical → §5 Zone D: Peripheral → §6 Connectivity →
§7 Chunks across A/B/C/D → §8 Implications

### Translation notes
- Neuroscience content = mostly English terms already
- Vietnamese is explanatory: "Vùng não NÀO? Con đường NÀO?"
  → "WHICH brain region? WHICH pathway?"
- Zone descriptions: translate function descriptions, keep region names
- v1.1 additions: Simulation-Engine mapping, Entity-Access mapping — verify glossary terms
- Connectivity map: likely ASCII diagram — translate labels

### Glossary impact
- Verify Zone A/B/C/D definitions match Core-Hardware

---

## A08 — Neural-Processing-Flow.md

| Field | Value |
|---|---|
| **Source** | Core-Deep-Dive/Neural-Processing-Flow.md |
| **Lines** | 1,271 |
| **English path** | English/Core-Deep-Dive/Neural-Processing-Flow.md |
| **Difficulty** | MEDIUM-HIGH — flow diagrams + Compilable Architecture |
| **Sessions** | 1 |

### Read before translating
- Vietnamese original
- English A04 + A07 (hardware context)
- English A05 (Core-Software) — shared architecture
- 00-Glossary.md

### Structure
§0 Position in framework → §1 Full Flow: Sensor → Thalamus → Cortex → PFC → Output →
§2 Compilable Architecture connection → later sections TBD

### Translation notes
- Flow diagram (ASCII): translate Vietnamese labels, keep arrow structure
- "Khi mắt thấy, tai nghe, da chạm, tim đập — tín hiệu đi CON ĐƯỜNG NÀO?"
  → "When eyes see, ears hear, skin touches, heart beats — WHICH PATHWAY does the signal take?"
- v2.0 additions: Compilable Architecture, Compiled/Fresh at physical level, PFC=Lawyer, 5-Channel
  — all these terms in glossary, verify
- 4-layer stack diagram §0: translate layer names

### Glossary impact
- May add: specific pathway terms (thalamus relay, binding, etc.)

---

## A09 — Modality.md

| Field | Value |
|---|---|
| **Source** | Core-Deep-Dive/Modality.md |
| **Lines** | 751 |
| **English path** | English/Core-Deep-Dive/Modality.md |
| **Difficulty** | MEDIUM |
| **Sessions** | 0.5 (can combine with A10) |

### Read before translating
- Vietnamese original
- English A07 + A08 (hardware context)
- 00-Glossary.md

### Structure
§0 What is Modality → §1 6 Modalities → §2 Hardware Basis →
§3 Chunk × Modality → §4 Modality Interaction → §5 × Thinking Direction →
§6 × Development → §7 × Therapy → §8 Honest Assessment → §9 Cross-refs

### Translation notes
- 6 modalities: Visual / Auditory / Somatic / Motor / Emotional / Communication
  — already English, translate descriptions
- §3 "Depth = Modality Count" — key insight, translate clearly
- §5 "Dọc / Ngang" → "Vertical / Horizontal" (thinking direction)
- §7 "Fix Đúng Kênh" → "Fix the Right Channel" — therapy matching
- Examples may have Vietnamese cultural references — check and annotate

### Glossary impact
- 6 modality names (already in glossary)
- May add: "depth = modality count" principle

---

## A10 — Blackbox-Map.md

| Field | Value |
|---|---|
| **Source** | Core-Deep-Dive/Blackbox-Map.md |
| **Lines** | 1,124 |
| **English path** | English/Core-Deep-Dive/Blackbox-Map.md |
| **Difficulty** | MEDIUM-HIGH — honest assessment, needs clear English |
| **Sessions** | 1 |

### Read before translating
- Vietnamese original
- English A04 + A05 (architecture context)
- 00-Glossary.md

### Structure
§0 Why important → §1 5-Layer Model: Computer Analogy → §2-§6 GAP 1-5 →
§7 Complexity Dimensions → §8 Framework as Research Roadmap →
§9 AI as Dynamic Drill Tool → §10 Cross-references

### Translation notes
- Computer analogy throughout — works perfectly in English
  - "Giống máy tính: chuột USB và con trỏ trên màn hình"
    → "Like a computer: USB mouse and cursor on screen"
  - "Driver code ở giữa — bạn không viết, không đọc, không kiểm soát"
    → "The driver code in between — you didn't write it, can't read it, can't control it"
- §1 5-Layer model: translate layer names
- §2-§6 Each GAP: "GAP LỚN NHẤT" → "LARGEST GAP" — keep emphasis
- §8 Research roadmap: "Nếu framework đúng → đây là bản đồ FRONTIER"
  → "If the framework is correct → this is a map of the FRONTIER"
- §9 AI as drill tool: framework-specific AI usage — translate naturally

### Glossary impact
- 5 GAPs terminology (may add to glossary)
- "Signal Transduction Driver Layer" — verify term

---

## Phase A Completion Checklist

After all 10 files:
- [ ] All files created in English/ with correct folder structure
- [ ] 00-Glossary.md updated with any new terms discovered
- [ ] plan-english-translation.md §5 Phase A checkboxes all ticked
- [ ] Consistency review: shared concepts (Compiled/Fresh, 3-cost, PFC roles) use identical phrasing across all 10 files
- [ ] Core-Software.md (A05) establishes vocabulary that Body-Feedback-Label (A01) defined
- [ ] README.md (A03) works as standalone English entry point

## Lessons to capture for Phase B plan

After completing Phase A, note:
1. How long did each file actually take?
2. What restructuring level felt right? (light? medium?)
3. How did Vietnamese examples translate? (keep + annotate? replace?)
4. Any glossary terms that needed revision?
5. What was the biggest surprise / challenge?

→ Feed these answers into plan-phase-B.md
