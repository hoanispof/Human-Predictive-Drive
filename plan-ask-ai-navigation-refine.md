# Plan: Ask-AI §7 Navigation Table Refine

> **Mục tiêu:** Rà soát từng topic trong routing table, đảm bảo accuracy cao.
> **Nguyên tắc:** Mỗi topic = 1-3 files TỐI ƯU. Không cần nhiều — cần ĐÚNG.
> **Tại sao quan trọng:** AI đọc table → chọn files → nếu route sai → trả lời sai.

---

## Phase 1: Rà soát EXISTING topics (11 topics hiện tại)

Mỗi topic: verify file routing → đúng / cần fix / cần thêm-bớt.

| # | Topic | Current routing | Status | Finding |
|---|-------|-----------------|--------|---------|
| 1 | Stress / burnout | Cortisol-Baseline v2.2, Connection v5.0 | ✅ DONE | Fixed v2.1→v2.2 |
| 2 | Nuôi con / parenting | Natural-Development v2.1, Child-Development-Mechanism v2.0 | ✅ DONE | Drill files→practical child-dev files |
| 3 | Quan hệ / cô đơn | Connection v5.0, Empathy v4.0, Love-Unified v2.1 | ✅ DONE | Fixed v2.0→v2.1. Good 3-file set |
| 4 | Motivation / "lười" | Drive, Novelty, 03-Reward.md | ✅ DONE | No change needed |
| 5 | Tự hiểu bản thân | Schema v2.0, AI-Schema-Detection v2.1 §7 | ✅ DONE | Good combination (WHAT + HOW) |
| 6 | Attention / ADHD | Attention-Spectrum v2.1, ADHD-Observation v1.3 | ✅ DONE | PFC-Function→ADHD-Observation |
| 7 | Status / meaning | Status v2.2, Meaning v2.0 | ✅ DONE | Fixed v2.1→v2.2 |
| 8 | Học / thay đổi / habits | 09-Learning-Cycle.md, Compile-Taxonomy v2.0 | ✅ DONE | +Compile-Taxonomy |
| 9 | Body signals / feeling | Feeling-Literacy-Training-Draft, SAL | ✅ DONE | Good 2-file (training + mechanism) |
| 10 | Work / career / ngành nghề | AI-Collective-Detection, Coordination-Node, CSP | ✅ DONE | No change needed |
| 11 | AI + self-understanding | AI-Schema-Detection §7-§8, AI-Coll-Det, AI-Self-Model, SAL §5 | ✅ DONE | 4 files justified (complex topic) |

### Approach per topic:
1. Đọc file được route tới (frontmatter + scope)
2. Hỏi: "Nếu user hỏi topic này → file này có TRỰC TIẾP trả lời được không?"
3. Có file NÀO tốt hơn cho topic này không?
4. Quyết định: giữ / thay / thêm / bớt

---

## Phase 2: Missing topics

Candidate topics phổ biến mà user hay hỏi nhưng chưa có trong table:

| # | Topic candidate | Candidate files | Status | Finding |
|---|-----------------|-----------------|--------|---------|
| A | Yêu / romantic / chia tay | Love-Romantic v3.0, Love-Unified v2.1 | ✅ ADDED | vs #4 Quan hệ: romantic ≠ general social |
| B | Nghiện / addiction / phone | Addiction-Analysis v3.1, Entity-Access-Excess v1.0 | ⏸️ DEFERRED | Phức tạp — thập cẩm loại nghiện. Thảo luận riêng |
| C | Áp lực / obligation / guilt | Obligation.md v1.2 | ✅ ADDED | vs #1 Stress: social tracking ≠ cortisol |
| D | Lo lắng / OCD / ám ảnh | Threat.md v1.3, OCD-Analysis v2.2 | ✅ ADDED | vs #1 Stress: threat loop ≠ chronic stress |
| E | Autonomy / "sao ko chịu tự làm" | Autonomy-HW v1.2, Autonomy v1.2 | ⏸️ SKIPPED | Lower priority. AI can find via File-Index |
| F | Chán / boredom | Boredom.md v2.1 | ✅ ADDED | vs #7 Motivation: "no direction" ≠ "no drive" |

### Criteria thêm topic mới:
- User HAY hỏi topic này (frequency cao)
- Routing KHÔNG hiển nhiên (AI có thể route sai nếu không có guidance)
- Nếu AI đã biết route đúng mà không cần table → không cần thêm

---

## Phase 3: Cross-references block

- Verify versions
- Verify files còn tồn tại + relevant
- VP v4.0 → v4.1 (đã biết)

---

## Phase 4: Execute

- Sửa Ask-AI.md §7 table
- Test: mỗi topic → routing có make sense không?

---

## Progress

- Created: 2026-05-31
- Phase 1: ✅✅ ALL 11/11 DONE
- Phase 2: ✅ 4 ADDED (A, C, D, F). B deferred (complex). E skipped (low priority).
- Phase 3: ✅ VP v4.0→v4.1 fixed
- Phase 4: ✅ EXECUTED — Ask-AI.md §7 updated (15 topics, all versions verified)
- Remaining: Topic B (Addiction) — thảo luận riêng khi cần
