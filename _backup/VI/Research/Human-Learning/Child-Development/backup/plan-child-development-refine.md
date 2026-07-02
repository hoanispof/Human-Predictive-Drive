# Plan: Child-Development Folder Refine

```
Status:    ALL 4 PHASES DONE ✅✅ (2026-05-25). Child-Dev folder COMPLETE.
Created:   2026-05-25
Scope:     4 files, ~8,725 lines total
Approach:  REFINE (không rewrite) — giữ core content, thêm concepts mới + update cross-refs
Part of:   Education Triple-Folder Refine (Child-Dev → Education-Mechanism → Education-System)
```

---

## 1. BỐI CẢNH

Child-Development/ gồm 4 file được viết 2026-04-21 (v1.0-v2.0, aligned v7.8).
Từ đó, framework đã qua ~35 ngày phát triển mạnh:
- Phase A-D drill propagation (28 sessions)
- ~30+ file mới hoặc rewrite lớn
- Nhiều concept mới chưa cascade vào Child-Dev

**Core content vẫn vững** — mechanisms, timelines, practical advice đều đúng.
Gaps chủ yếu là: concept mới thiếu + cross-refs cũ + vocabulary outdated ở vài chỗ.

---

## 2. CONCEPTS CẦN INTEGRATE

| Concept | File nguồn | Relevant cho file nào | Mức độ |
|---------|-----------|----------------------|--------|
| Hardware Subsidy | drill → Phase C | CẢ 4 file | HIGH — oxytocin, pregnancy hormones, co-regulation |
| Connection v5.0 (M1-M4, Bond-Architecture, Entity-Access, 4-Layer Sustainability, Phantom) | Connection.md v5.0 + Bond-Architecture.md v1.0 | Mechanism §4, Natural-Dev S7.3 | HIGH — attachment section outdated |
| Imagine-Final v3.0 Boundary Reframe | Imagine-Final.md v3.0 | Mechanism §9, Natural-Dev S7.6 | CRITICAL — "Pre-Imagine-Final" giờ SAI |
| Valence-Propagation v3.0 (Structural/Current, Mixed, 3 Firing Modes) | Valence-Propagation.md v3.0 | Mechanism §3, Natural-Dev S7.1-S7.2, Skill §1-§2 | HIGH |
| Entity-Compiled v1.0 (Hub-and-Spoke, Formation 40→200h, Dunbar) | Entity-Compiled.md v1.0 | Mechanism §4.4, Natural-Dev S4.3/S7.3 | HIGH |
| Entity-Access gradient Mức 0-5 | Entity-Access.md v1.2 | Mechanism §4.4, Mother §2 | MEDIUM |
| PFC Budget | PFC-Label.md v1.0 | Mechanism §1/§4, Natural-Dev S1, Skill §1/§5/§7 | MEDIUM |
| Gap-Direction v1.0 | Gap-Direction.md v1.0 | Mechanism §4.1, Natural-Dev S4.5/S7.2 | MEDIUM |
| Body-Feedback-Label v1.1 (prediction-delta, 3-tier) | Body-Feedback-Label.md v1.1 | Mechanism §5, Skill §0/§1.2/§9 | MEDIUM — vocabulary update |
| PFC-Label v1.0 | PFC-Label.md v1.0 | Mechanism §5, Natural-Dev S7.7, Skill §6.5 | MEDIUM |
| Compiled/Fresh v2.0 | Compiled-Fresh.md v2.0 | Mechanism §1-§4, Skill §1.4/§5.4 | MEDIUM |
| Simulation-Engine v1.0 | Simulation-Engine.md v1.0 | Mechanism §6/§9, Natural-Dev S2.8/S4.5/S7.6 | MEDIUM |
| 3 Satiation Types (Gap-Fill/Habituation/Compilation-Complete) | Gap-Body-Need.md v1.0 | Mechanism §2/§4, Skill §2.5/§4 | MEDIUM |
| 3 Firing Modes (Generative/Tonic/Reactive) | Valence-Propagation.md v3.0 | Mechanism §2/§5, Natural-Dev S6.4, Skill §1.5/§2 | LOW-MEDIUM |
| Coordination-Node v1.2 ("Mẹ = first node") | Coordination-Node.md v1.2 §2.5 | Mother §2.3/§6.2, Mechanism §4.4 | MEDIUM (Mother HIGH) |
| Dissonance-Signal-Architecture v1.0 | Dissonance-Signal-Architecture.md v1.0 | Mechanism §3/§4, Natural-Dev S2.5/S6.5, Skill §7.3 | LOW |
| Background-Pattern v2.0 (Triple Bias, Pattern Shiftability) | Background-Pattern.md v2.0 | Mechanism §3.1, Skill §2.6/§7.1 | LOW |
| Vehicle/Road/Engine metaphor (Gap-Body-Need) | Gap-Body-Need.md v1.0 | Mechanism §4, Natural-Dev S7.2 | LOW |
| By-Product-Gap-Resonance v1.4 | By-Product-Gap-Resonance.md v1.4 | Mechanism §6 | LOW |
| Self-Pattern-Modeling v3.1 (Match→Modeling rename) | Self-Pattern-Modeling.md v3.1 | Mechanism §6, Natural-Dev S2.7 | LOW — chỉ fix term |
| Gap-Distribution-Profile v1.1 | Gap-Distribution-Profile.md v1.1 | Mechanism §9, Skill §7.1 | LOW |

---

## 3. NGUYÊN TẮC

1. **Chậm mà chắc** — chất lượng nội dung > tốc độ hoàn thành
2. **REFINE, không REWRITE** — giữ core content, thêm sections/paragraphs mới tại insertion points
3. **Chỉ thêm concept KHI RELEVANT** — không ép concept vào chỗ không cần
4. **Mother-Optimization đặc biệt** — medical-heavy, framework-light → chỉ thêm concept thật sự relevant
5. **Mỗi file cần:** đọc kỹ → xác định insertion points → thêm nội dung → update deps/cross-refs → version bump
6. **Cross-ref paths:** cập nhật Education/ → Education-Mechanism/ hoặc Education-System/ khi gặp

### MỨC ĐỘ REFINE
- **LIGHT** = +50-150L: cross-refs, brief paragraphs, terminology fixes
- **MODERATE** = +200-500L: sub-sections mới, mở rộng nội dung, structure updates
- **HEAVY** = +500-1,000L: sections viết lại hoặc thêm mới đáng kể

---

## 4. ORDERED PHASES

### Phase 1: Child-Development-Mechanism.md [✅ DONE 2026-05-25]

```
File:     Child-Development-Mechanism.md
Result:   v1.0 → v2.0, 2,197L → 2,640L (+443L)
Target:   v2.0, ~2,900-3,200L (+700-1,000L) — actual +443L (leaner, quality focused)
Priority: ✅ DONE — file nền tảng complete
```

**Phase 1 Actual Results:**
- 1.1 §4.4 Connection REWRITE: +130L (Entity-Compiled, Bond-Architecture, Hardware Subsidy,
  4-Layer Sustainability, Phantom 4-factor, Entity-Access gradient, Coordination-Node)
- 1.2 §3 Valence-Propagation v3.0: +63L (Structural/Current valence, Mixed Valence, Triple Bias, Hardware Subsidy at compile)
- 1.3 §9 Imagine-Final v3.0 CRITICAL: +32L (hardware prediction ≠ Imagine-Final, Simulation-Engine, Gap-Direction)
- 1.4 §1/§2 enrichment: +77L (PFC Budget, new §2.5 with Satiation Types, Compiled/Fresh, 3 Firing Modes)
- 1.5 §5/§6 fix: +14L (Body-Feedback-Label vocab, SELF-PATTERN-MATCH→SELF-PATTERN-MODELING, Simulation-Engine+By-Product-Gap-Resonance cross-refs)
- 1.6 §7/§8: +32L (Hardware Subsidy for autonomy, PFC Budget, Dissonance-Signal-Architecture)
- 1.7 Metadata: +95L (deps 13→34, §11 expanded, v2.0 version bump, path fixes)

**1.1 — §4.4 Connection/Attachment REWRITE** [HEAVY — ưu tiên cao nhất]
- Hiện tại: chỉ nói "Connection.md §1, §2" + basic attachment
- Cần thêm:
  - Entity-Compiled v1.0: caregiver = first entity-compiled, Hub-and-Spoke, Formation 40-200h
  - Bond-Architecture v1.0: mother-child = first bond, Entity-Compiled = 1 mechanism × 4 bond types
  - Entity-Access gradient: caregiver = Mức 4-5 (body-base extension)
  - Hardware Subsidy: oxytocin + CT fibers = hardware subsidized bond
  - 4-Layer Sustainability: secure attachment = all 4 layers active
  - Phantom 4-factor: separation anxiety = phantom activation
  - Coordination-Node: mẹ = first coordination node (Coordination-Node v1.2 §2.5)
- Ước tính: +200-300L

**1.2 — §3 Approach/Avoidance + Valence-Propagation v3.0** [MODERATE]
- Hiện tại: approach/avoidance tags, body-state-at-compile, reconsolidation
- Cần thêm:
  - Structural vs Current valence: trẻ = tags chủ yếu Current (chưa Structural)
  - Mixed Valence: trẻ thường có mixed tags ("vừa thích vừa sợ")
  - Background-Pattern v2.0 Triple Bias: tại sao first experiences quan trọng
  - Hardware Subsidy: dopamine/oxytocin tại compile = hardware-subsidized approach tag
- Ước tính: +80-120L

**1.3 — §9 Observation Parameters + Imagine-Final v3.0** [MODERATE — CRITICAL fix]
- Hiện tại: observation emergence timeline + Imagine-Final trajectory
- Cần fix:
  - Imagine-Final v3.0: hardware prediction ≠ Imagine-Final → reframe developmental trajectory
  - Simulation-Engine: pretend play = first Simulation-Engine usage
  - Boredom v2.0: update boredom description (now has M1-M4, unified formula)
  - Gap-Direction: trẻ có gap ít direction vì ít chunks
  - Gap-Distribution-Profile: gap distribution thay đổi mạnh 0-6
- Ước tính: +100-150L

**1.4 — §1/§2 PFC + Compile enrichment** [LIGHT-MODERATE]
- §1: thêm PFC Budget concept, Simulation-Engine mention
- §2: thêm 3 Satiation Types, Compiled/Fresh formal terms, Hardware Subsidy at emotional peak compile
- §2: thêm 3 Firing Modes brief note (trẻ = chủ yếu Reactive → dần Generative)
- Ước tính: +80-120L

**1.5 — §5 Feeling + §6 Self-Pattern-Modeling** [LIGHT]
- §5: cross-ref Body-Feedback-Label v1.1, PFC-Label v1.0
- §6: fix "SELF-PATTERN-MATCH" → "SELF-PATTERN-MODELING" (line 1337)
- §6: cross-ref Simulation-Engine, By-Product-Gap-Resonance, Resonance-Per-Entity
- Ước tính: +50-80L

**1.6 — §7 Autonomy + §8 Cortisol** [LIGHT]
- §7: Hardware Subsidy (self-action opioid), PFC Budget, Compiled/Fresh
- §8: Dissonance-Signal-Architecture, PFC Budget
- Ước tính: +30-50L

**1.7 — Header deps + §11 Cross-refs** [LIGHT]
- Update dependency list: thêm ~15 file mới
- §11: thêm ~20 cross-references, update ~10 version numbers
- Fix Education/ → Education-Mechanism/ paths
- Ước tính: +100-150L

---

### Phase 2: Natural-Development.md [✅ DONE 2026-05-25]

```
File:     Natural-Development.md
Result:   v2.0 → v2.1, 2,085L → 2,404L (+319L)
Target:   v2.1, ~2,500-2,700L (+400-600L) — actual +319L (quality focused)
Priority: ✅ DONE — framework lens sections fully updated
```

**Phase 2 Actual Results:**
- 2.1 §7.6 Imagine-Final REFRAME CRITICAL: +38L ("Pre-Imagine-Final"→"Hardware Prediction Only",
  Simulation-Engine 3 components, Gap-Direction, Gap-Distribution-Profile)
- 2.2 §7.3 Connection EXPANDED: +63L (Entity-Compiled, Bond-Architecture, Hardware Subsidy,
  M1-M4, Coordination-Node 5 capabilities, Phantom, 4-Layer, Entity-Access gradient)
- 2.3 §7.1-7.2 Valence+Chunks: +70L (Structural/Current, Mixed Valence, 3 Firing Modes,
  Gap-Direction, 3 Satiation Types, Background-Pattern Triple Bias)
- 2.4 §7.7 Feeling/Self-Pattern-Modeling: +10L (Body-Feedback-Label 3-tier, PFC-Label, prediction-delta)
- 2.5 §2 enrichments: +15L (fix SELF-PATTERN-MATCH→MODELING, Dissonance-Signal-Architecture, Simulation-Engine)
- 2.6 §4 Timeline: +16L (Entity-Compiled separation anxiety, Dissonance-Signal-Architecture tantrums, Gap-Direction,
  Phantom imaginary friend, 4-Layer friendships)
- 2.7 §6 Sai lầm: +14L (3 Satiation/Firing Modes screen, PFC Budget, Structural valence)
- 2.8 Header+§10: +93L (deps 9→25, paths fixed, 17 new cross-refs, changelog)

**2.1 — S7.6 Imagine-Final REFRAME** [CRITICAL — làm đầu tiên]
- "Pre-Imagine-Final" (line 1768-1770) giờ SAI per Imagine-Final v3.0
- Body expectations = hardware prediction, KHÔNG PHẢI Imagine-Final
- Reframe: hardware prediction (0-6mo) → proto-simulation (6-18mo) → early Simulation-Engine (18mo-3y) → emerging Imagine-Final (3-6y)
- Ước tính: +60-80L

**2.2 — S7.3 Connection × Attachment** [MODERATE]
- Hiện tại: "hardware drive, virtual chunks" — quá sơ sài so với Connection v5.0
- Cần thêm: M1-M4, Bond-Architecture, Entity-Access, Entity-Compiled, 4-Layer Sustainability, Hardware Subsidy, Coordination-Node
- Ước tính: +100-150L

**2.3 — S7.1-S7.2 Valence + Chunk Dynamics** [MODERATE]
- S7.1: thêm Structural/Current valence, Hardware Subsidy, 3 Firing Modes
- S7.2: thêm Gap-Direction, 3 Satiation Types, Vehicle/Road/Engine metaphor
- S7.2: Background-Pattern v2.0 cho compound dynamics
- Ước tính: +80-120L

**2.4 — S7.7 Feeling + Self-Pattern-Modeling** [LIGHT]
- Cross-ref PFC-Label v1.0, Body-Feedback-Label v1.1
- Update Self-Pattern-Modeling per v3.1
- Ước tính: +30-50L

**2.5 — S2 Hành vi tự nhiên enrichment** [LIGHT]
- S2.1: oxytocin = Hardware Subsidy example
- S2.5: Dissonance-Signal-Architecture khi baby's signal bị ignore
- S2.7: fix "SELF-PATTERN-MATCH" → "SELF-PATTERN-MODELING" (line 597)
- S2.8: Simulation-Engine cho pretend play
- Ước tính: +40-60L

**2.6 — S4 Timeline enrichment** [LIGHT]
- S4.3: Entity-Compiled (separation anxiety)
- S4.4: Dissonance-Signal-Architecture (tantrums)
- S4.5: Gap-Direction ("tại sao?"), Simulation-Engine (pretend play), Phantom (imaginary friend)
- S4.6: 4-Layer Sustainability cho childhood friendships
- Ước tính: +50-80L

**2.7 — S6 Sai lầm phổ biến enrichment** [LIGHT]
- S6.4: 3 Satiation Types cho screen time (Habituation), 3 Firing Modes (screen = Reactive)
- S6.5: Dissonance-Signal-Architecture + PFC-Label
- S6.6: PFC Budget (over-scheduling = PFC depleted)
- S6.7: Structural valence (comparison → negative Structural valence)
- Ước tính: +40-60L

**2.8 — Header + S10 Cross-refs** [LIGHT]
- Fix `Agent/` → `Agent-Mechanism/` paths (2 occurrences)
- Thêm ~14 file mới vào cross-refs
- Update version numbers
- Fix Education/ paths
- Ước tính: +60-80L

---

### Phase 3: Skill-Introduction.md [✅ DONE 2026-05-25]

```
File:     Skill-Introduction.md
Result:   v2.0 → v2.1, 2,087L → 2,276L (+189L)
Target:   v2.1, ~2,300-2,450L (+200-350L) — actual +189L (lean, quality focused)
Priority: ✅ DONE — vocabulary updated, framework lens enriched
```

**Phase 3 Actual Results:**
- 3.1 Vocabulary: Body-Feedback-Label 3-tier replace "feeling layer 1-2" (§0.3, §1.2, §9),
  "implicit/explicit"→Compiled/Fresh (§5.4), "body-base schema"→compiled chunk cluster (§3.2),
  +prediction-delta throughout
- 3.2 §1: +Gap-Direction (§1.1), +Dissonance-Signal-Architecture (§1.2), +Simulation-Engine (§1.3),
  +Compiled/Fresh + 3 Firing Modes (§1.4), +Hardware Subsidy (§1.5)
- 3.3 §2: +Valence Dynamics Current→Structural (§2 header), +Hardware Subsidy (§2.3),
  +Habituation Satiation (§2.5), +Triple Bias + Pattern Shiftability (§2.6)
- 3.4 §7: +Gap-Distribution-Profile (§7 intro), +Compiled/Fresh (§7.2, §7.4),
  +PFC Budget + Dissonance-Signal-Architecture amplification (§7.3)
- 3.5 §8: +M1-M4 burnout, +4-Layer Sustainability, +Cortisol precision (§8.2)
- 3.6 Header: deps 11→22, position paths fixed, §11 reorganized +18 new files, changelog

**3.1 — Vocabulary update (Body-Feedback-Label v1.1)** [CRITICAL — xuyên suốt]
- "feeling layer 1-2" → Body-Feedback-Label v1.1 (3-tier: Hardware-Signal / Evaluative-Signal / Integration-Signal)
- Affected: §0 (line 159-165), §1.2 (line 213-214), §9 (line 1927)
- "body-base schema" → "Compiled chunk cluster (with valence)"
- "implicit/explicit learning" (§5.4) → Compiled/Fresh processing
- Ước tính: ~20 replacements, +20-30L annotations

**3.2 — §1 Core Principles enrichment** [LIGHT]
- §1.1: Gap-Direction (readiness = gap hướng toward skill)
- §1.2: prediction-delta vocabulary, Dissonance-Signal-Architecture
- §1.3: Simulation-Engine (child's PFC simulation)
- §1.4: Compiled/Fresh (deep = Fresh→Compiled), 3 Firing Modes (deep = Generative)
- §1.5: Hardware Subsidy (process-focused dopamine)
- Ước tính: +40-60L

**3.3 — §2 Exposure→Structure enrichment** [LIGHT]
- §2.1-2.4: 3 Firing Modes, Valence-Propagation v3.0, Hardware Subsidy, Entity-Compiled
- §2.5: 3 Satiation Types (Habituation vs Gap-Fill), Autonomy split
- §2.6: Background-Pattern v2.0 (Pattern Shiftability × sensitive periods)
- Ước tính: +40-60L

**3.4 — §7 Calibrate per-child** [LIGHT]
- §7.1: Gap-Distribution-Profile, Boredom v2.0
- §7.2: Compiled/Fresh processing styles
- §7.3: Dissonance-Signal-Architecture + PFC Budget (HSC overwhelm)
- §7.4: Compiled/Fresh (cautious = more Fresh processing)
- Ước tính: +30-50L

**3.5 — §8 Warning signs** [LIGHT]
- Cortisol-Baseline v2.0 precision
- M1-M4 for burnout (M1 Compiled suppress)
- 4-Layer Sustainability for skill practice
- Ước tính: +20-30L

**3.6 — Header + §11 Cross-refs** [LIGHT]
- Update frontmatter dependencies (Connection, Imagine-Final, Empathy versions)
- Thêm ~18 file mới vào cross-refs
- Update ~8 version numbers
- Ước tính: +60-80L

---

### Phase 4: Mother-Optimization.md [✅ DONE 2026-05-25]

```
File:     Mother-Optimization.md
Result:   v2.0 → v2.1, 2,356L → 2,562L (+206L)
Priority: NHẸ NHẤT — medical-heavy, framework-light. CHỈ thêm concept thật sự relevant.
```

**Phase 4 Actual Results (2026-05-25):**
- 4.1 Hardware Subsidy: §0.4 definition (+11L), §2.3 pregnancy hormones (+10L),
  §3.1 11β-HSD2 biochemical (+6L), §6.2 social support oxytocin (+7L)
- 4.2 Coordination-Node + Entity: §2.3 mẹ=first node (+12L),
  §6.2 partner=secondary node (+5L), §2 Entity-Access Mức 0 (+8L)
- 4.3 Light enrichment: §3.2 Structural valence (+7L), §3.1 Body-Feedback
  Pipeline (+5L), §6.2 PFC Budget stress tools (+10L)
- 4.4 Header: deps 8→20, position paths fixed, v2.0→v2.1.
  §11 +3 open questions (⑩⑪⑫). §12 complete rewrite (+12 new cross-refs,
  reorganized by folder). Footer: version bump, changelog added.
  §0.2 vocab fix (feeling layers → body-feedback prediction-delta)

---

## 5. TỔNG KẾT

| Phase | File | Mức độ | Lines thêm | Sessions | Result |
|-------|------|--------|-----------|----------|--------|
| 1 | Child-Development-Mechanism.md | MODERATE-HEAVY | +443L | 1 | ✅ v2.0 (2,640L) |
| 2 | Natural-Development.md | MODERATE | +319L | 1 | ✅ v2.1 (2,404L) |
| 3 | Skill-Introduction.md | LIGHT-MODERATE | +189L | 1 | ✅ v2.1 (2,276L) |
| 4 | Mother-Optimization.md | LIGHT | +206L | 1 | ✅ v2.1 (2,562L) |
| **Tổng** | **4 files** | | **+1,157L** | **4 sessions** | ✅✅ ALL DONE |

### Thứ tự ưu tiên trong mỗi Phase:
1. **CRITICAL fixes trước** (Imagine-Final v3.0 reframe, "SELF-PATTERN-MATCH" terminology)
2. **HIGH gaps** (Connection v5.0 + Bond-Architecture + Entity-Compiled, Hardware Subsidy, Valence-Propagation v3.0)
3. **MEDIUM enrichment** (PFC Budget, Gap-Direction, Body-Feedback-Label vocabulary, Compiled/Fresh)
4. **Cross-refs + deps cuối** (sau khi content đã stable)

### Deliverables mỗi session:
- Version bump file đã refine
- Verify cross-refs consistency
- Update File-Index nếu description thay đổi đáng kể

---

## 6. CHECKLIST PER-FILE (dùng khi execute)

```
□ Đọc file hiện tại (full)
□ Xác định insertion points
□ Viết nội dung mới
□ Fix old terminology
□ Update dependency header
□ Update cross-references section
□ Fix old paths (Education/, Agent/, etc.)
□ Version bump
□ Update File-Index description nếu cần
□ Final read-through kiểm tra consistency
```
