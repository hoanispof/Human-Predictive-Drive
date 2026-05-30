# Plan: Tách Entity-Valence-Dynamics.md từ Valence-Propagation.md v3.0

> **Created:** 2026-05-29
> **Goal:** Tách TRỤ 2 (entity-valence dynamics) thành file riêng + absorb 3 drill GAPs
> **Source:** Valence-Propagation.md v3.0 (~2,001L) + Drill-Entity-Valence-Dynamics v2.0 (3 GAPs)
> **Approach:** VP v3.0 đã tự chia 3 trụ rõ ràng → tách TRỤ 2 ra, giữ TRỤ 1+3 trong VP

---

## PHÂN CHIA NỘI DUNG

### File 1: Valence-Propagation.md v4.0 (TRIMMED — giữ TRỤ 1 + TRỤ 3)

Nội dung GIỮ LẠI (renumber):
```
§0 — VỊ TRÍ TRONG FRAMEWORK (update diagram: TRỤ 2 → pointer Entity-Valence-Dynamics.md)
§1 — VALENCE LÀ GÌ                          ← giữ nguyên
§2 — VALENCE PROFILE: Cấu Trúc Per-Entity   ← giữ nguyên
§3 — CÁCH VALENCE HÌNH THÀNH + UPDATE        ← cũ §14 → renumber §3
§4 — VALENCE PROPAGATION QUA SCHEMA CHAIN    ← cũ §15 → renumber §4
§5 — CHAIN PROPERTIES + WHY CHAIN DÀI        ← cũ §16 → renumber §5
§6 — CASES PHÂN TÍCH                         ← cũ §17 → renumber §6
§7 — PFC BLINDNESS + 3 NGUYÊN TẮC           ← cũ §18 → renumber §7
§8 — HONEST ASSESSMENT (trimmed)             ← cũ §19, bỏ entity-valence claims
§9 — CROSS-REFERENCES + CITATIONS (trimmed)  ← cũ §20, bỏ entity-valence refs
```

Ước tính: ~900-1,000L. Focused: WHAT valence is + HOW it propagates.

### File 2: Entity-Valence-Dynamics.md v1.0 (NEW — TRỤ 2 + drill GAPs)

Nội dung TỪ VP v3.0 (renumber):
```
§0 — VỊ TRÍ + THESIS
§1 — STRUCTURAL VALENCE vs CURRENT VALENCE   ← cũ VP §3
§2 — ENTITY-COMPILED: Body-Base Extension     ← cũ VP §4
§3 — 2-LUỒNG + 2-TẦNG × VALENCE VISIBILITY  ← cũ VP §5
§4 — 3 FIRING MODES                           ← cũ VP §6
§5 — VTA HABITUATION × HARDWARE SUBSIDY      ← cũ VP §7
§6 — VALENCE × SATIATION TYPE                ← cũ VP §8
§7 — MIXED VALENCE: PARALLEL PER-CHANNEL     ← cũ VP §9
§8 — "XA MẸ MỚI BIẾT THƯƠNG"                ← cũ VP §10
§9 — NOSTALGIA = L2 ACTIVE SELF-REGULATION   ← cũ VP §10.1
§10 — PER-ENTITY VALENCE DYNAMICS + RSA      ← cũ VP §11
§11 — EXTREME VALENCE: LOVE/HATE + DISORGANIZED  ← cũ VP §12 (lines 1285-1305)
§12 — PHANTOM RESONANCE × GRIEF              ← cũ VP §12 (lines 1228-1284)
§13 — TECHNOLOGY × VALENCE FRONTIER          ← cũ VP §13
```

Nội dung MỚI từ drill GAPs (absorb vào sections phù hợp):
```
§6b — "CHÁN" × VALENCE DECLINE (satiation type decomposition)    ← drill §14 GAP
       Cyclic = immune to "chán" (oscillate)
       Tonic = vulnerable to invisibility (NOT actual decline)
       Generative = vulnerable to ACTUAL "chán" (novelty hết)
       "Chán" = Generative dies + Tonic survives
       Boredom-Mechanism connection
       Per-entity "chán" patterns (mẹ=rare, bạn=natural, romantic=highest risk)
       → Absorb vào §6 (Valence × Satiation Type) hoặc thành §6b riêng

§4b — 8 KÊNH L2 TRỞ NÊN VISIBLE (formal taxonomy)              ← drill §6 GAP
       A: Invisible khi stable
       B: External Trigger (sensory/narrative/context)
       C: Self-Pattern-Modeling Output
       D: Loss / Chunk-Miss
       E: Logic-Feeling Mismatch
       F: PFC Recall (proxy trigger)
       G: Social Media Trigger (technology era)
       H: AI Partial Trigger (technology era)
       → Absorb vào §4 (3 Firing Modes) dưới dạng sub-section

§10b — VERBALIZATION = PFC OBSERVATION × RSA (mapping)           ← drill §12 GAP
       "ghét" = avoidance channels dominate PFC observation
       "thương" = approach B dominant (warm)
       "thích" = approach A dominant (exciting)
       "nhớ" = Chunk-Miss hoặc Context-Trigger
       "trống/mất mát" = EC fire → no response
       "không cảm thấy gì" = L2 habituated → below threshold
       "chán" = Generative dead + Tonic invisible
       → Absorb vào §10 (Per-entity Dynamics) dưới dạng sub-section
```

Kết thúc file:
```
§14 — HONEST ASSESSMENT (entity-valence claims từ VP §19 + drill §19)
§15 — CROSS-REFERENCES + CITATIONS (entity-valence refs + drill §20-§21)
```

Ước tính: ~1,100-1,300L. Focused: HOW valence behaves per-entity over time.

---

## PHASES

### Phase 1 — ✅ DONE (session 1) — Tạo Entity-Valence-Dynamics.md v1.0

**Input:** VP v3.0 §3-§13 + Drill v2.0 §6, §12, §14
**Steps:**
1. Copy VP §3-§13 content vào file mới
2. Viết §0 mới (Position + Thesis — synthesize từ drill §0 + VP §0)
3. Absorb drill §14 → §6b (Chán × Valence Decline)
4. Absorb drill §6 → §4b (8-channel taxonomy)
5. Absorb drill §12 → §10b (Verbalization × RSA mapping)
6. Tách VP §12 thành §11 (Love/Hate + Disorganized) và §12 (Phantom × Grief) — hiện VP gộp chung
7. Viết §14 Honest Assessment (tách entity-valence claims từ VP §19 + thêm drill §19)
8. Viết §15 Cross-references + Citations (tách entity-valence refs + thêm drill §20-§21)
9. Viết YAML header (title, version, dependencies, scope)
10. Review renumbering consistency

**Vị trí:** Core-Deep-Dive/Body-Base/Entity-Valence-Dynamics.md
(cùng level VP và Body-Coupling — valence là Body-Base concept)

### Phase 2 — ✅ DONE (session 2) — Trim Valence-Propagation.md → v4.0

**Steps:**
1. Xóa §3-§13 (đã chuyển sang file mới)
2. Renumber §14→§3, §15→§4, §16→§5, §17→§6, §18→§7
3. Update §0 diagram: TRỤ 2 → pointer "Entity-Valence-Dynamics.md v1.0"
4. Trim §19 (Honest Assessment): bỏ entity-valence claims, giữ propagation claims
5. Trim §20 (Cross-refs + Citations): bỏ entity-valence refs (R1-R33 move to new file), giữ propagation refs (R34-R55)
6. Update YAML header (v3.0 → v4.0, scope, deps)
7. Thêm brief pointer ở đầu file: "Per-entity valence dynamics → Entity-Valence-Dynamics.md"

### Phase 3 — ✅ DONE (session 2+3) — Cross-reference Updates

**Session 2 (21 edits, 15 Core files):**
- PFC-Operations, Compliance-Floor, Knowledge-Flow, Status (×2),
  Connection (×4), Liking-Wanting, Obligation (×3), Autonomy-Hardware,
  Empathy (×3), Collective, Chunk, Bond-Architecture, Resonance-Per-Entity

**Session 3 (remaining heavy files):**
- Body-Coupling.md: ~45 edits (YAML + §3→EVD§1, §4→EVD§2, §6→EVD§4, §7→EVD§5, §8→EVD§6)
- Background-Pattern.md: ~21 edits (YAML + §3→EVD§1, §6→EVD§4, §7→EVD§5, §8→EVD§6, §12→EVD§12)
- Empathy.md: 7 edits (§2→VP v4.0§2, §7→EVD§5, §8→EVD§6, changelog)
- Education files (8 files): ~40 edits (§7→EVD§5, §11→EVD§10/§12, YAML deps, VN headers/cross-refs)
  - Education-System.md: §11 pre-existing error corrected (Phantom→EVD§12, not §11)
  - Hardware-Calibration, Curriculum-Framework, Era-Analysis, 00_Overview: all updated
  - VN-Recommendations, VN-Education-Status, VN-Cultural-Factors: all updated

**Coincidental match note:** Collective-Body.md "VP §3,§4,§5" = v2.0 numbering = v4.0 propagation §3,§4,§5. NO edit needed.

**Remaining (lower priority):** ~30 files still reference "Valence-Propagation v3.0" in YAML deps (general file-level, no §). These are version-string updates, not content pointer errors. Separate cleanup session if needed.

### Phase 4 — ✅ DONE (session 2) — Update Index + Meta Files

1. **01-File-Index.md**: Thêm entry Entity-Valence-Dynamics.md, update VP entry
2. **Body-Base.md v3.3**: Update §10 Reading Guide + §12 Cross-refs (thêm EVD)
3. **Core-Software.md**: Update dependency nếu có VP ref (check)
4. **00-Parameter-Overview.md**: Update Valence section (thêm EVD)
5. VP v3.0 → backup/Valence-Propagation-v3.0-backup.md

### Phase 5 — ✅ DONE (session 3) — Quality Check

1. EVD v1.0: Đọc lại toàn bộ → check flow giữa sections
2. VP v4.0: Đọc lại → check flow sau trim (§2 → §3 smooth transition?)
3. Cross-refs: Grep "Valence-Propagation.*§" → verify tất cả § numbers correct
4. 3 drill GAPs: Verify tất cả 28 insights đã absorbed (drill §18 checklist)
5. Dependencies: YAML header cả 2 files → deps list correct?
6. Thống kê: total lines, citations, insights

---

## RỦI RO + MITIGATION

| Rủi ro | Mitigation |
|--------|------------|
| Section renumbering sai | Phase 5: grep all §X references, verify per-file |
| Collective-Body.md §3,§4,§5 confusion (v2.0 vs v3.0 numbering) | Verify nội dung từng reference, không chỉ number |
| VP v4.0 flow bị gãy (§2 → §3 jump topic) | Viết 1-2 câu bridge ở đầu §3 mới |
| EVD §0 không self-contained | Viết rõ: đọc VP §1-§2 trước, file này = TRỤ 2 |
| Quên update backup cross-refs | Chỉ update non-backup files. Backup files giữ nguyên |

---

## THỐNG KÊ ƯỚC TÍNH

| Metric | VP v3.0 (hiện tại) | VP v4.0 (sau tách) | EVD v1.0 (mới) |
|--------|--------------------|--------------------|-----------------|
| Dòng | ~2,001 | ~900-1,000 | ~1,100-1,300 |
| Sections nội dung | 18 (§1-§18) | 7 (§1-§7) | 13+3 GAPs (~15) |
| Citations | 55 | ~20 (propagation) | ~35 (entity-valence) |
| Drill insights | 28 | 0 | 28 + 3 GAPs |

---

## SESSION MỚI CHECKLIST

Khi bắt đầu session mới, đọc:
1. File này (plan)
2. VP v3.0 §0 (position diagram — understand 3 trụ)
3. VP v3.0 §3-§13 headings (confirm what moves)
4. Drill v2.0 §6, §12, §14 (3 GAPs to absorb)
5. Bắt đầu Phase 1 → 2 → 3 → 4 → 5
