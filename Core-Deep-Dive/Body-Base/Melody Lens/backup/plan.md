# Melody-Lens Rewrite Plan — v7.8 Aligned

> **Mục tiêu**: Rewrite toàn bộ 4 files Melody-Lens cho v7.8 quality.
> **Ngày plan**: 2026-04-20
> **Approach**: Backup cũ → viết mới từng file → chất lượng tốt nhất.

---

## CURRENT STATE (pre-rewrite)

| File | Lines | Created | Status |
|---|---|---|---|
| Personal-Melody.md | 884 | 2026-03-29 | DRAFT, v7.5 terminology |
| Melody-Arc.md | 772 | 2026-03-27 | DRAFT, v7.5 terminology |
| Global-Melody.md | 532 | 2026-03-29 | DRAFT, v7.5 terminology |
| Personal-Melody-Example.md | 324 | 2026-03-29 | DRAFT, v7.5 |
| **Total** | **2,512** | | |

---

## VẤN ĐỀ CẦN FIX

### 1. Terminology outdated
- "L2" references → v7.8 đã remove L2, chỉ có L0/L1/L3
- "cortisol = khó chịu" → cortisol = amplifier, not cause (Clarification file)
- "cortisol tag" → "avoidance tag" (approach/avoidance terminology)
- "Architecture v7.5" → Core-v7.8-Draft.md
- "Schema-Operations.md" → có thể đã backup
- "Empathy-Mirror.md" → Empathy.md + Self-Pattern-Match.md + Pattern-Resonance.md
- "Attention-Spectrum.md" → check if still exists or backed up
- "Knowledge-Flow.md" → check if still exists
- "Education-Bridge.md" → check if still exists

### 2. Missing v7.8 concepts
- Prediction delta (NOT "prediction error") — Schultz 1997
- Efference copy → Autonomy-Hardware.md (NEW)
- Approach/avoidance tag (NOT cortisol/opioid tag)
- vmPFC + DRN controllability learning (Maier & Seligman 2016)
- Chunk dynamics: Shift/Miss/Gap (Body-Feedback-Mechanism.md)
- Observation parameters framework (v7.8 §8)
- Cycle architecture (NOT layer architecture)

### 3. Structural considerations
- Personal-Melody.md role: vừa là metaphor tool VÀ observation parameter content
- Cần clarify: Melody-Lens = COMMUNICATION TOOL (metaphor)
  vs Observation/Melody = STATE (parameter)
- Có thể merge/split differently sau rewrite

### 4. Cross-references need full update
- ~20+ file references outdated trong 4 files
- Cần map tất cả references sang current file names

---

## REWRITE PLAN

### Phase 0: Backup
- Move tất cả 4 files → `Melody Lens/backup/`
- Giữ plan.md ở folder chính

### Phase 1: Personal-Melody.md (LARGEST, FIRST)
**Priority**: Highest — foundation cho các files khác
**Estimated**: ~700-900L (tương đương hoặc ngắn hơn)
**Key changes**:
- §1: Giữ metaphor explanation nhưng add: "melody = chunk network state"
  → Link tới Chunk.md v2.0, Schema.md v2.0
- §2: Start Melody (hardware) → update with PFC-Hardware.md, Neural-Architecture.md
  → Fix DRD4/COMT terminology (check if still used in current files)
- §3: Multi-Modal Sync → link Modality.md (current file)
- §4: "Gu" → giữ (content vẫn valid)
- §5: Two-Axis Tension → KEY SECTION:
  → Body-base pull vs Domain pull = vẫn core concept
  → 4 criteria "melody hay" = vẫn valid
  → ADD: link Autonomy-Hardware.md (efference copy → body pull mechanism)
  → FIX: "cortisol nhẹ" → "mild dissonance" (cortisol = amplifier)
  → ADD: "approach/avoidance tag" terminology
- §6: Imagine-Final → update references (Imagine-Final.md current version)
  → Remove "14 ngưỡng" nếu không còn trong current Imagine-Final.md
- §7: Arc Dynamics → giữ (concept valid), update terminology
- §8: Equilibrium → giữ (5 profiles vẫn valid)
- §9-14: Update references, fix terminology
- §15: Honest Assessment → update research list, add new 🟢 anchors
- §16: Cross-references → FULL UPDATE to current file names

### Phase 2: Melody-Arc.md
**Priority**: High — practical application (education, learning design)
**Estimated**: ~600-800L
**Key changes**:
- Core concept (arc = dissonance → resolve) = VALID, giữ
- ADD: Body-Feedback-Mechanism.md integration (Chunk-Shift = arc START, Gap = arc MIDDLE)
- ADD: Autonomy connection — bé tự chọn arc vs bị ép arc → khác tag
- FIX: "cortisol" language → approach/avoidance + amplifier clarification
- FIX: bridge terminology → align with Reward-Economics.md, Skill-Introduction.md
- UPDATE: cross-references
- ADD: v7.8 observation parameters as "what body observes DURING arc"
  (novelty = delta at start, boredom = delta→0 at plateau, etc.)

### Phase 3: Global-Melody.md
**Priority**: Medium — collective level, less core
**Estimated**: ~400-500L
**Key changes**:
- Core concept (melodies interact at group/culture/global) = VALID
- FIX: "Empathy-Mirror.md" → Empathy.md + Self-Pattern-Match.md
- FIX: "Status-Analysis-v2" → Status.md (Observation/)
- ADD: Collective-Purpose.md integration ("vô danh ≠ vô nghĩa")
- ADD: Meaning.md connection (collective coherence)
- UPDATE: all cross-references

### Phase 4: Personal-Melody-Example.md
**Priority**: Low — examples, dependent on Personal-Melody.md
**Estimated**: ~300L
**Key changes**:
- Update 3 profiles to use v7.8 terminology
- Ensure examples reference current observation parameters
- Likely LAST to rewrite (depends on Personal-Melody.md structure)

---

## ORDER & DEPENDENCIES

```
Phase 0: Backup (5 min)
  ↓
Phase 1: Personal-Melody.md (foundation)
  ↓
Phase 2: Melody-Arc.md (depends on §5, §7 of Personal-Melody)
  ↓
Phase 3: Global-Melody.md (depends on Personal-Melody concepts)
  ↓
Phase 4: Personal-Melody-Example.md (depends on all above)
```

---

## PRE-REWRITE CHECKLIST (for next session)

Before writing, cần đọc/verify:
1. ☐ Core-v7.8-Draft.md §8 — observation parameters full list
2. ☐ Chunk.md v2.0 — current chunk terminology
3. ☐ Modality.md — check if replaces "Modality-Analysis.md"
4. ☐ Imagine-Final.md — current structure (còn "14 ngưỡng"?)
5. ☐ Check which old references still exist vs backed up:
   - ☐ Knowledge-Flow.md
   - ☐ Schema-Operations.md
   - ☐ Attention-Spectrum.md
   - ☐ Education-Bridge.md
   - ☐ Innovation-Geography.md
   - ☐ Conflict-Dynamics.md
6. ☐ Autonomy-Hardware.md §0 — emergent pattern comparison table
7. ☐ Cortisol-Baseline.md §7.2-§7.3 — approach/avoidance tag (refined)
8. ☐ Body-Feedback-Mechanism.md — Shift/Miss/Gap (arc mapping)
9. ☐ Meaning.md — schema coherence (melody state ≈ meaning state?)
10. ☐ Drive.md — PFC smooth melody role

---

## KEY DECISIONS FOR REWRITE

**Q1: Melody-Lens = metaphor ONLY? Or also observation parameter?**
→ Đề xuất: Melody-Lens = METAPHOR COMMUNICATION TOOL.
  Observation/Melody.md (nếu cần) = SHORT parameter reference.
  Nhưng Personal-Melody.md §5 (4 criteria) = core definition regardless.

**Q2: Giữ music metaphor hay chuyển sang mechanism language?**
→ Đề xuất: KEEP music metaphor — đó là VALUE của Melody-Lens.
  Nhưng ADD mechanism link ở mỗi section (metaphor → mechanism).
  "Earworm = compiled chunks tự fire" → giữ VÀ explain.

**Q3: Position trong folder structure?**
→ Đề xuất: GIỮ ở `Schema/Melody Lens/` — vì đây là lens (cách nhìn),
  không phải mechanism file. Nhưng add note: "observation parameter = 
  Observation/Melody.md nếu cần short reference."
  HOẶC: move lên Core-Deep-Dive/ level nếu coi là core integration.

**Q4: Scope — giữ 4 files hay merge/split?**
→ Đề xuất: GIỮ 4 files. Structure tốt:
  Personal (1 người) → Arc (learning) → Global (tập thể) → Example.
  Có thể ADD 1 file: Melody-Observation.md (short, parameter format).

---

## ESTIMATED TOTAL EFFORT

| Phase | Est. lines | Sessions |
|---|---|---|
| Phase 1 (Personal-Melody) | 700-900 | 1 session |
| Phase 2 (Melody-Arc) | 600-800 | 1 session |
| Phase 3 (Global-Melody) | 400-500 | 0.5 session |
| Phase 4 (Examples) | 250-350 | 0.5 session |
| **Total** | **~2000-2500** | **~3 sessions** |

---

## SESSION PLAN

**Session N+1**: Phase 0 (backup) + Phase 1 (Personal-Melody.md rewrite)
**Session N+2**: Phase 2 (Melody-Arc.md rewrite) + Phase 3 start
**Session N+3**: Phase 3 finish + Phase 4 (Examples)

Mỗi session: đọc reference files → phân tích → viết → review conventions.
Chậm mà chắc. Từng file một.
