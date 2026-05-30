# Plan: Collective.md — Integration Hub / Entry Point
# File MỚI — tổng quan Collective/ folder

> **Ngày tạo:** 2026-05-24
> **Mục đích:** Tạo file Collective.md — integration hub cho Collective/ folder (5 files).
> Hiện tại Collective/ là folder DUY NHẤT có 5 files mà KHÔNG có entry point.
> **Phương pháp:** Phân tích kỹ 5 file hiện có → xác định GAP → viết file mới.
> **Nguyên tắc:** Hub file — gọn, tổ chức, bridge. KHÔNG repeat mechanism từ sub-files.
> **Liên quan:** plan-core-foundation-rewrite.md — Collective.md sẽ được tạo TRƯỚC 6 file rewrite.

---

## Tại sao cần Collective.md

### 1. Mọi folder lớn đều có integration hub — trừ Collective/

| Folder | Hub file | Lines |
|--------|----------|-------|
| Body-Base/ | Body-Base.md v3.2 | ~1,300L |
| Agent-Mechanism/ | Agent-Mechanism.md v2.1 | ~2,362L |
| Body-Feedback/ | Body-Feedback.md | ~850L |
| Schema/ | Schema.md v2.0 | ~817L |
| Feeling/ | Feeling.md v3.0 | ~varies |
| **Collective/** | **❌ KHÔNG CÓ** | — |

### 2. "Collective ảnh hưởng cá nhân" = content CHƯA có ở đâu

5 file hiện tại mô tả collective TỪ GÓC collective (mechanism, dynamics, purpose, governance).
KHÔNG file nào trả lời rõ: **"Collective ảnh hưởng cá nhân THẾ NÀO?"**

Cụ thể — 5 điểm này rải rác nhưng chưa tập trung:
- Trust Compile: collective install chunks vào cá nhân qua trust gate
- "Behaves like domain": cá nhân KHÔNG phân biệt physics vs collective feedback
- Schema inheritance: văn hóa/norm truyền qua thế hệ, cá nhân không biết nguồn
- Status = Resource Access Map: vị trí trong collective quyết định access
- System Compilation: 6 compound (trust+hierarchy+norms+institutions+technology+rituals)

### 3. Reader không biết bắt đầu từ đâu

Collective-Body.md = de facto starting point, nhưng:
- Nó là MECHANISM file (Model 3 cấp), không phải overview
- Không giải thích 5 files relate thế nào
- Không cung cấp reading flow
- Giống Self-Pattern-Modeling.md (mechanism) — cần Agent-Mechanism.md (hub) phía trên nó

---

## 5 files hiện có — scope analysis

| File | Version | Lines | Focus | Đã cover gì |
|------|---------|-------|-------|-------------|
| Collective-Body.md | v2.1 | ~1,779L | MECHANISM | Model 3 cấp, trust = only bridge, chain dài, system compilation, AI era |
| Coordination-Node.md | v1.2 | ~2,210L | POSITION | Resource allocation, Status≠Talent≠Contribution, Prestige vs Dominance, Mẹ=first node |
| Collective-Arc-Dynamics.md | v1.2 | ~varies | DYNAMICS | Shelf-life, 3 constraint sources → shift speed, dependency ratio |
| Collective-Purpose.md | v1.2 | ~varies | META | Cosmic loop, humanity map domain, 3 forces, biological ceiling |
| Compliance-Floor.md | v2.1 | ~varies | GOVERNANCE | Luật tối thiểu, tự do=default, 4 tầng nền, 5 giới hạn |

**Mỗi file = 1 góc nhìn. Chưa có file nào cho TOÀN CẢNH.**

---

## Collective.md sẽ cover gì — GAP analysis

### Content ĐÃ CÓ ở sub-files (KHÔNG repeat — chỉ preview + forward pointer)

| Topic | Ở đâu | Collective.md chỉ cần |
|-------|-------|----------------------|
| Model 3 cấp mechanism | CB.md §1-§3 | Preview 5-10L + link |
| Trust = only bridge | CB.md §5 | Preview 3-5L + link |
| System Compilation 6 compound | CB.md §3.4 | Preview 5L + link |
| Coordination node mechanism | CN.md full | Preview 5L + link |
| Arc dynamics / shelf-life | CAD.md full | Preview 5L + link |
| Cosmic loop / meta-purpose | CP.md full | Preview 5L + link |
| Compliance floor / governance | CF.md full | Preview 5L + link |

### Content CHƯA CÓ ở đâu (Collective.md UNIQUE contribution)

| Topic | Tại sao cần | Ước tính |
|-------|-------------|----------|
| **§0 Collective là gì** — KHÔNG phải entity riêng, là emergent từ nhiều body tương tác | Định nghĩa chưa có file nào state rõ ràng | ~30L |
| **§1 Bridge Body-Base → Collective** — tại sao cá nhân CẦN collective (Compilable Architecture) | CB.md assume reader đã biết. Overview cần bridge rõ | ~50L |
| **§2 Collective ảnh hưởng cá nhân** — 5 con đường ảnh hưởng (trust compile, "behaves like domain", schema inheritance, status access, system compilation) | CHƯA tập trung ở đâu. Rải rác 5 files. CẦN 1 nơi gom | ~150L |
| **§3 Folder architecture + reading flow** — 5 files relate thế nào, đọc theo thứ tự nào | CHƯA CÓ | ~40L |
| **§4 Collective × Key Concepts** — Technology × Scale, By-Product-Scale L3, Hardware Subsidy per scale, Satiation at collective | Rải rác, chưa tập trung | ~80L |
| **§5 Individual vs Collective — ranh giới** — khi nào "individual" mechanism, khi nào "collective" phenomenon | Implicit nhưng chưa explicit | ~50L |
| **§6 Honest Assessment** | Standard | ~30L |
| **§7 Cross-References** | Standard | ~30L |

**Tổng ước tính: ~500-700L**

---

## Cấu trúc dự kiến

```
§0 — Collective là gì
     Định nghĩa: KHÔNG phải entity riêng — emergent từ nhiều body tương tác.
     Collective KHÔNG "muốn" gì — collective = infrastructure mà cá nhân chạy trên.
     Tương tự: internet không "muốn" gì — internet = infrastructure cho communication.

§1 — Bridge: Body-Base → Collective
     Compilable Architecture: brain cần 15-20 năm compile → cần entity khác →
     nhiều entity tương tác = collective EMERGE.
     Model 3 cấp tóm tắt: Individual (compile SHORT) → Collective (hold LONG) → Framework (explain).
     → Detail: Collective-Body.md v2.1

§2 — Collective ảnh hưởng cá nhân: 5 con đường
     ① Trust Compile — collective install chunks vào cá nhân qua trust gate
       "Học = tốt" sống ở collective, cá nhân compile [học→mẹ khen→ấm] SHORT
     ② "Behaves like domain" — body KHÔNG phân biệt physics vs collective
       Bị sa thải đau như rơi từ cao. Bị tôn vinh sướng như ăn ngon.
     ③ Schema inheritance — culture/norm truyền vô thức qua thế hệ
       Cá nhân compile MÀ KHÔNG biết nguồn. PFC confabulate "tôi tự nghĩ ra"
     ④ Status = Resource Access Map — vị trí collective quyết định access
       → Detail: Coordination-Node.md v1.2, Status.md v2.0
     ⑤ System Compilation — 6 compound (trust+hierarchy+norms+institutions+tech+rituals)
       → Detail: Collective-Body.md §3.4

§3 — Folder architecture + reading flow
     5 files × scope diagram
     Reading flow: Collective.md (hub) → Collective-Body.md (mechanism) →
     Coordination-Node.md (position) → Collective-Arc-Dynamics.md (dynamics) →
     Collective-Purpose.md (meta) → Compliance-Floor.md (governance)

§4 — Collective × Key Concepts
     Technology × Scale (ROUTINE → GENUINE frontier shift)
     By-Product-Scale L3 (institutional by-product match)
     Hardware Subsidy per scale (oxytocin L1 → serotonin L2 → trust infrastructure L3)
     Satiation at collective level
     Collective × Simulation-Engine (distributed simulation, no single PFC)

§5 — Individual vs Collective: ranh giới
     Cá nhân: compile SHORT, body-level, 1 brain
     Collective: hold LONG, distributed, no single brain
     Bridge: Trust = ONLY mechanism nối 2 cấp
     KHÔNG hierarchy: collective KHÔNG "cao hơn" cá nhân. Khác SCALE, không khác RANK.

§6 — Honest Assessment
§7 — Cross-References (5 sub-files + Body-Base + Agent-Mechanism + Domain)
```

---

## Workflow

```
PHASE 1 — PHÂN TÍCH (đầu session)
  ① Re-read 5 sub-files (headers + key sections)
  ② Xác nhận GAP analysis ở trên vẫn đúng
  ③ Xác nhận cấu trúc với user

PHASE 2 — VIẾT (trong session)
  ① Draft Collective.md theo cấu trúc trên
  ② Đảm bảo KHÔNG repeat mechanism — chỉ preview + forward pointer
  ③ §2 (5 con đường) = unique contribution — viết kỹ nhất
  ④ Cross-refs chính xác

PHASE 3 — VERIFY
  ① Check 5 sub-files có cross-ref ngược về Collective.md
  ② Update File-Index
  ③ Update memory
```

---

## Risk + mitigation

| Risk | Mitigation |
|------|------------|
| Trùng Collective-Body.md | Hub PREVIEW + link. KHÔNG repeat Model 3 cấp detail |
| File quá dài cho hub | Target ~500-700L. Hub role = gọn |
| 5 sub-files cần update cross-ref | Minor — thêm "→ Overview: Collective.md" ở đầu mỗi file |

---

> *"Collective/ folder có 5 file chuyên sâu nhưng không có cửa ngõ.
> Reader vào folder như vào thành phố không có bản đồ.
> Collective.md = bản đồ: 'collective là gì, ảnh hưởng cá nhân thế nào,
> 5 file này nói gì, đọc theo thứ tự nào.'
> Gọn. Rõ. Không repeat."*
