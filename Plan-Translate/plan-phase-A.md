# Phase A — Vocabulary + Core Architecture

> **Status**: READY TO EXECUTE
> **Created**: 2026-05-26
> **Updated**: 2026-06-05 (v4.0 — +2 files, line counts verified, version notes updated)
> **Files**: 12 (A01-A12)
> **Total lines**: ~8,909
> **Estimated sessions**: 5-7
> **Goal**: Establish English terminology standard + overall framework framing
> **Pre-req**: 00-Glossary.md created (✅)
> **Companion files**:
>   - Plan-Translate/plan-english-translation.md — master plan (§3 Phase A)
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
8. Update plan-english-translation.md §4 (tick checkbox)
```

---

## A01 — Body-Feedback-Label.md

| Field | Value |
|---|---|
| **Source** | Core-Deep-Dive/Body-Base/Body-Feedback/Body-Feedback-Label.md |
| **Lines** | 1,004 |
| **Version** | v2.0 |
| **English path** | English/Core-Deep-Dive/Body-Base/Body-Feedback/Body-Feedback-Label.md |
| **Difficulty** | HIGH — vocabulary foundation, every term decision matters |
| **Sessions** | 1 |

### Read before translating
- Vietnamese original (full)
- 00-Glossary.md (terms already extracted from this file)

### Structure
§0 Why needed → §1 3-Tier system → §2 Foundation (body-need/gap/drive) →
§3 Reward labels → §4 Dissonance labels → §5 Prediction-delta →
§6 Baseline → §7 Compiled (approach/avoidance) vs momentary →
§8 Body-feedback ≠ Feeling → §9 Usage rules + examples

### Translation notes
- **This file IS the vocabulary standard** — English version becomes the reference for all future files
- Tables in `code blocks` with Vietnamese: translate cell content, keep table structure
- §2 examples: "VD: đói, khát, đau, lạnh" → "e.g., hunger, thirst, pain, cold"
- §2 examples: "VD: nhớ bạn, career gap, identity" → "e.g., missing a friend, career gap, identity crisis"
- §7 examples: Entity-Compiled positive/negative/mixed — translate carefully
- ⚠️ warnings: translate content, keep ⚠️ symbol
- Conceptual flow diagram §2: translate Vietnamese labels, keep box structure
- v2.0: Reward-Signal-Architecture integration (Evaluative/Direct-State), Body-Feedback-Precondition references

### Glossary impact
- 00-Glossary.md was BUILT from this file — minimal new terms expected
- Verify all usage rules translate correctly
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
| **Lines** | 1,014 |
| **Version** | v1.0 |
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
- §4 HOLD vs SUPPRESS table: keep table structure, translate Vietnamese cells
- §5 3-cost: translate examples naturally
- §6 Compiled Quality: genuine/schema/threat — critical distinction for English readers
- §7 Regions: mostly English technical terms already. Translate descriptions only
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
| **Lines** | 196 |
| **English path** | English/README.md |
| **Difficulty** | LOW-MEDIUM — already mostly English, needs polishing |
| **Sessions** | 0.3 (combine with A04) |

### Read before translating
- Vietnamese original
- 00-Glossary.md

### Translation notes
- **Already mostly English** — Vietnamese is mainly in explanatory sections
- Starter prompt: needs ENGLISH version (currently Vietnamese instructions)
- Folder structure ASCII: translate Vietnamese comments
- Keep same structure, just translate remaining Vietnamese

### Glossary impact
- Minimal — README uses general terms

---

## A04 — Core-Hardware.md

| Field | Value |
|---|---|
| **Source** | Core-Hardware.md |
| **Lines** | 330 |
| **English path** | English/Core-Hardware.md |
| **Difficulty** | MEDIUM — mostly neuroscience English terms already |
| **Sessions** | 0.3 (combine with A03) |

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
- §0 table: translate "Bản đồ", "Góc nhìn", "Đối tượng"
- §1 "4 zones A/B/C/D" — keep zone labels, translate descriptions
- §6 "Hardware Sets Range, Chunks Choose Position" — important principle

### Glossary impact
- May add: Zone A/B/C/D definitions, PFC Reach Gradient

---

## A05 — Core-Software.md ⭐ KEY FILE

| Field | Value |
|---|---|
| **Source** | Core-Software.md |
| **Lines** | 1,600 |
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
- §1 Cycle diagram in code block: translate Vietnamese labels, keep ASCII art
- §4 "Unconscious Processing": heaviest section — chunk dynamics, body-feedback, cortisol
- §8 Observation Parameters: brief descriptions → must match Observation/ file vocabulary
- §11 "Key Reframes": 20+ reframes — CRITICAL for English reader
  - Each reframe: "Mainstream says X → Framework says Y"
  - These must be sharp, clear English
- §12 "Honest Assessment": confidence levels + limitations — keep honest tone
- YAML header "Tiền đề đọc" lists prerequisites — translate this list
- v7.8 specific: 3 Satiation Types, ENGINE/ROAD/VEHICLE, Body-Feedback-Precondition references

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
| **Lines** | 621 |
| **English path** | English/Ask-AI.md |
| **Difficulty** | MEDIUM-HIGH — user-facing, needs natural English |
| **Sessions** | 0.5 |

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
- §0 roles: Catalyst / Compass / Partner — translate metaphors naturally
- §2 Protocol: 6-step — DETECT→READ→ADAPT→PRESENT→ITERATE→DEEPEN
  - Already English terms — translate explanations
- §3 DANGER ZONES: positions where framework ≠ mainstream
  - CRITICAL: these must be crystal clear in English
- §5 Example conversations: Vietnamese examples → natural English equivalents
  - "Tại sao tôi hay trì hoãn?" → "Why do I keep procrastinating?"
  - "Con tôi 3 tuổi hay ăn vạ..." → "My 3-year-old throws tantrums..."
- §6 Dual Check: body = quality controller, domain = final arbiter
- §7 Navigation: file map with paths → keep paths as-is

### Glossary impact
- "Danger Zones" terms — verify matches glossary
- Dual Check phrasing — verify consistency

---

## A07 — Neural-Architecture.md

| Field | Value |
|---|---|
| **Source** | Core-Deep-Dive/Neural-Architecture.md |
| **Lines** | 802 |
| **Version** | v1.2 (added §7 Bilateral Architecture) |
| **English path** | English/Core-Deep-Dive/Neural-Architecture.md |
| **Difficulty** | MEDIUM — heavy neuroscience, mostly English terms |
| **Sessions** | 0.5 |

### Read before translating
- Vietnamese original
- English A04 (Core-Hardware) — shared zone model
- 00-Glossary.md

### Structure
§0 Why → §1 Overview: 4 Zones → §2 Zone A: PFC → §3 Zone B: Cortical →
§4 Zone C: Subcortical → §5 Zone D: Peripheral → §6 Connectivity →
§7 Bilateral Architecture (NEW v1.2) → §8 Chunks across A/B/C/D → §9 Implications

### Translation notes
- Neuroscience content = mostly English terms already
- Vietnamese is explanatory: translate naturally
- Zone descriptions: translate function descriptions, keep region names
- **§7 Bilateral Architecture is NEW** (v1.2): corpus callosum, lateralization, split-brain (Gazzaniga)
  - "Unity = emergent from harmony, NOT structural" — key principle
  - Framework hemisphere-agnostic by design
- Connectivity map: likely ASCII diagram — translate labels

### Glossary impact
- Verify Zone A/B/C/D definitions match Core-Hardware
- May add: bilateral architecture terms

---

## A08 — Neural-Processing-Flow.md

| Field | Value |
|---|---|
| **Source** | Core-Deep-Dive/Neural-Processing-Flow.md |
| **Lines** | 1,025 |
| **English path** | English/Core-Deep-Dive/Neural-Processing-Flow.md |
| **Difficulty** | MEDIUM-HIGH — flow diagrams + Compilable Architecture |
| **Sessions** | 0.5-1 |

### Read before translating
- Vietnamese original
- English A04 + A07 (hardware context)
- English A05 (Core-Software) — shared architecture
- 00-Glossary.md

### Structure
§0 Position in framework → §1 Full Flow: Sensor → Thalamus → Cortex → PFC → Output →
§2 Compilable Architecture connection → later sections

### Translation notes
- Flow diagram (ASCII): translate Vietnamese labels, keep arrow structure
- v2.0: Compilable Architecture, Compiled/Fresh at physical level, PFC=Lawyer, 5-Channel
- 4-layer stack diagram §0: translate layer names
- Verify all terms match glossary

### Glossary impact
- May add: specific pathway terms (thalamus relay, binding, etc.)

---

## A09 — Modality.md

| Field | Value |
|---|---|
| **Source** | Core-Deep-Dive/Modality.md |
| **Lines** | 589 |
| **English path** | English/Core-Deep-Dive/Modality.md |
| **Difficulty** | MEDIUM |
| **Sessions** | 0.3 (combine with A10) |

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

### Glossary impact
- 6 modality names (already in glossary)
- May add: "depth = modality count" principle

---

## A10 — Blackbox-Map.md

| Field | Value |
|---|---|
| **Source** | Core-Deep-Dive/Blackbox-Map.md |
| **Lines** | 886 |
| **English path** | English/Core-Deep-Dive/Blackbox-Map.md |
| **Difficulty** | MEDIUM-HIGH — honest assessment, needs clear English |
| **Sessions** | 0.5 |

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
- §1 5-Layer model: translate layer names
- §2-§6 Each GAP: "GAP LỚN NHẤT" → "LARGEST GAP" — keep emphasis
- §8 Research roadmap: strong vision statement, translate with impact
- §9 AI as drill tool: framework-specific AI usage

### Glossary impact
- 5 GAPs terminology (may add to glossary)
- "Signal Transduction Driver Layer" — verify term

---

## A11 — Reading-Roadmap.md ⭐ NEW

| Field | Value |
|---|---|
| **Source** | Reading-Roadmap.md |
| **Lines** | 283 |
| **Version** | v1.0 (2026-05-31) |
| **English path** | English/Reading-Roadmap.md |
| **Difficulty** | MEDIUM — navigation file, many file paths + descriptions |
| **Sessions** | 0.3 (combine with A03) |

### Read before translating
- Vietnamese original
- English README.md (companion)
- English Ask-AI.md (references same setup)
- 00-Glossary.md

### Structure
Tổng quan table → Pillar diagram → Tier 0 Foundation (8 files) →
Tier 1 Mechanism (14 files + enrichment) → Tier 2 Entity (8 files + enrichment) →
Tier 3 Observation (13 files + enrichment) → Tier 4 Collective (6 files) →
Tier 5 Domain (6 files) → Bridges → Reference → Tổng kết

### Translation notes
- **Structure-heavy file**: tables, ASCII diagrams, file listings
- File paths: keep EXACTLY as-is
- Line counts in tables: these may not match current counts (file was written 2026-05-31)
  - Decision: keep original counts OR update? → recommend keep (this is a reading guide, not audit)
- Vietnamese descriptions per file: translate concisely
- "Vai trò" column → "Role"
- "Sau tier này, bạn hiểu..." → "After this tier, you understand..."
- "Đọc tới đâu, hiểu tới đó" → "Read as far as you need — each tier is a level deeper"
- "3 trụ cột" → "3 pillars" (Individual, Collective, Domain)
- Pillar ASCII diagram: translate labels
- Enrichment sections: "Đọc thêm nếu muốn sâu hơn" → "Optional deeper reading"
- Bridges table: translate concise descriptions
- Final note: "Không cần đọc 97 files" → "You don't need to read all 97 files"

### Glossary impact
- Minimal — this is a navigation file, uses terms defined elsewhere
- Verify tier names are consistent with English versions of referenced files

### Quality checkpoint
- English reader can navigate the entire framework using only this file
- Tier structure clear: each tier = 1 level of understanding
- File descriptions accurate and inviting (not just dry listings)

---

## A12 — Auditory-Hardware.md ⭐ NEW

| Field | Value |
|---|---|
| **Source** | Core-Deep-Dive/Auditory-Hardware.md |
| **Lines** | 559 |
| **Version** | v1.0 (2026-05-30) |
| **English path** | English/Core-Deep-Dive/Auditory-Hardware.md |
| **Difficulty** | MEDIUM — neuroscience + framework synthesis, heavy code blocks |
| **Sessions** | 0.5 |

### Read before translating
- Vietnamese original (full)
- English A09 (Modality.md) — this file deep-dives one modality
- 00-Glossary.md

### Structure
§0 Position + Thesis → §1 6 Unique Hardware Properties (§1.1-§1.6) →
§2 Cross-Parameter Mapping (§2.1-§2.8 + summary) →
§3 Evolutionary Logic → §4 Honest Assessment → §5 Cross-References

### Translation notes
- **Heavily structured in code blocks** — preserve all box-drawing, alignment
- §0 Thesis: "Sound = T1 hardware channel, NOT observation parameter"
  - Camera/Microphone analogy: works perfectly in English
- §1 Six properties: each has CLAIM → EVIDENCE → SO SÁNH → FRAMEWORK MAPPING pattern
  - §1.1 Always-on: "con người KHÔNG CÓ 'eyelid' cho tai" → "humans have no 'eyelid' for ears"
  - §1.2 Cross-barrier: physics + binaural — mostly English already
  - §1.3 Pre-birth: DeCasper citations — keep verbatim
  - §1.4 Temporal > Spatial: complementary prediction system
  - §1.5 Activation efficiency: Grahn, Salimpoor, Blood & Zatorre — all English citations
  - §1.6 Dual Tonic/Cyclic: MMN + cocktail party — translate framework labels
- §2 Cross-parameter summary table: translate cell content, keep box-drawing EXACT
- §3 Evolutionary: 4 pressures → translate naturally
- §4 Honest assessment: 🟢/🟡/🔴 sections + caveats
  - Caveat ⑤ "KHÔNG PHẢI sound quan trọng hơn" → "NOT claiming sound is more important"
- §5 Cross-references: keep file paths, translate descriptions after →

### Vietnamese cultural content
- Minimal — this is a neuroscience file with very little cultural content
- "Nghe bước chân bên kia tường → biết có người" → "Hearing footsteps through the wall → knowing someone is there"

### Glossary impact
- May add: "activation efficiency", "sentinel function"
- Tonic/Cyclic labels — verify consistency with Gap-Body-Need.md terms
- "T1 hardware property" — verify usage

### Quality checkpoint
- 6 properties clearly distinguished
- Cross-parameter mapping table readable
- Honest assessment preserves 🟢/🟡/🔴 balance
- English reader understands WHY auditory is architecturally unique (not "better")

---

## Phase A Completion Checklist

After all 12 files:
- [ ] All files created in English/ with correct folder structure
- [ ] 00-Glossary.md updated with any new terms discovered
- [ ] plan-english-translation.md §4 Phase A checkboxes all ticked
- [ ] Consistency review: shared concepts (Compiled/Fresh, 3-cost, PFC roles) use identical phrasing across all 12 files
- [ ] Core-Software.md (A05) establishes vocabulary that Body-Feedback-Label (A01) defined
- [ ] README.md (A03) + Reading-Roadmap.md (A11) work as standalone English entry points
- [ ] Auditory-Hardware.md (A12) cross-references consistent with Modality.md (A09)

## Suggested groupings (can combine small files)

| Session | Files | Lines | Note |
|---|---|---|---|
| 1 | A01 Body-Feedback-Label | 1,004 | Vocabulary foundation — do alone |
| 2 | A02 PFC-Label | 1,014 | Vocabulary companion — do alone |
| 3 | A03 README + A04 Core-Hardware + A11 Reading-Roadmap | 726 | Small files, combine |
| 4 | A05 Core-Software (Part 1: §0-§6) | ~800 | Split large file |
| 5 | A05 Core-Software (Part 2: §7-§13) | ~800 | Complete large file |
| 6 | A06 Ask-AI + A09 Modality | 1,210 | Medium files, combine |
| 7 | A07 Neural-Architecture + A08 Neural-Processing-Flow | 1,827 | Hardware pair |
| 8 | A10 Blackbox-Map + A12 Auditory-Hardware | 1,445 | Hardware complement pair |

## Lessons to capture for Phase B plan

After completing Phase A, note:
1. How long did each file actually take?
2. What restructuring level felt right? (light? medium?)
3. How did Vietnamese examples translate? (keep + annotate? replace?)
4. Any glossary terms that needed revision?
5. What was the biggest surprise / challenge?
6. How did the new files (A11, A12) fit into the flow?

→ Feed these answers into plan-phase-B.md
