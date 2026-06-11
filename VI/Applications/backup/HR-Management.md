# Quản Lý Nhân Sự — Framework v5.5

> **Phiên bản:** 5.5 (Square Model — Source × Depth Restructure)
> **Prerequisite:** Core.md (§5 tham số nền, §6 chunk config, §7 drive equation,
> §8 Mô Hình Vuông, §8.3 Compliance phái sinh, §8.9 Chunk Topology).
> **File liên quan:** Applications/HR-Assessment-Gamedev.md (đánh giá chi tiết game dev).
> **Nguyên tắc:** Mỗi người có phương trình drive KHÁC NHAU →
> cùng output yêu cầu nhưng cần input quản lý KHÁC NHAU.
>
> **⚠️ QUY ƯỚC ĐỌC (v5.5):**
> Soldier, Architect, Improviser, Drifter = 4 NHÃN MÔ TẢ trên 4 cạnh Mô Hình Vuông,
> KHÔNG phải 4 kiểu người. CƠ CHẾ = predictive-chunk configuration (source × depth per domain).
> Compliance = chunk_overlap(person, reference_group) — chỉ số PHÁI SINH, hàm 2 biến.
> Sync = EMERGE từ depth đủ cao, không phải trục riêng.
>
> **Lưu ý:** 6 tệp = PRACTICAL SHORTCUT. Đằng sau = vị trí trên Mô Hình Vuông per domain.
> Cùng nhân sự: cạnh trên ở domain chuyên môn + cạnh phải ở domain admin = BÌNH THƯỜNG.
>
> **Quy ước:** 🟢 Nghiên cứu/dữ liệu | 🟡 Suy luận từ framework | 🔴 Giả thuyết

---

## Mục Lục

1. [Nguyên Lý Cốt Lõi](#1-nguyên-lý)
2. [6 Tệp Nhân Sự — Practical Shortcut](#2-sáu-tệp)
3. [Mô Hình Vuông × Nhân Sự — Lens Sâu Hơn](#3-vuông)
4. [Depth Composite × Seniority](#4-depth)
5. [Convergence × Cross-Functional Teams](#5-convergence)
6. [Dopamine Inverted-U × Burnout vs Boredom](#6-dopamine)
7. [Ma Trận Nhu Cầu + Task](#7-ma-trận)
8. [Tuyển Dụng v5.5](#8-tuyển-dụng)
9. [Giữ Người Per Tệp](#9-giữ-người)
10. [Xây Team + Dynamic Per Phase](#10-team)
11. [Quản Lý Hàng Ngày: 1-on-1 + Giao Việc](#11-hàng-ngày)
12. [Xung Đột Team](#12-xung-đột)
13. [Áp Lực Tối Ưu — Inverted-U Per Mode](#13-áp-lực)
14. [Mode Sếp + 7 Sai Lầm](#14-sếp)
15. [Chunk Config Card v5.5](#15-card)
16. [Câu Hỏi Mở](#16-câu-hỏi)
17. [Kết Nối](#17-connections)

---

## 1. Nguyên Lý Cốt Lõi

```
Drive = Prediction Thưởng − Prediction Chi Phí  (Core.md §7)

Cùng 1 task, 2 người:
  Người A: thưởng (lương) MẠNH + chi phí (mệt) YẾU → drive cao
  Người B: thưởng (lương) YẾU + chi phí (vô nghĩa) MẠNH → drive âm

→ Quản lý 1 kiểu cho tất cả = tối ưu ~30%, phí phạm ~70%
→ Quản lý PER vị trí trên Mô Hình Vuông = tối ưu ~80%+

BIẾN SỐ QUYẾT ĐỊNH:
  TẦNG 0 (phần cứng — quan sát, không sửa):
    Kênh gốc, Threshold, PE Sensitivity
    Thiên hướng nền: vị trí mặc định trên Mô Hình Vuông khi gặp domain mới

  TẦNG 1 (phần mềm — phát triển được):
    Depth composite ở domain công việc (4 sub-params §8.2)
    Source tendency ở domain công việc
    Schema tương lai: "nỗ lực = được đền đáp" hay không
    Prediction cost per task type
```

---

## 2. Sáu Tệp Nhân Sự — Practical Shortcut

🟡 6 tệp = gộp nhanh dựa trên PE SOURCE CHÍNH. Đằng sau = vị trí Mô Hình Vuông + kênh gốc + threshold (xem §3 cho lens sâu hơn).

### Tệp 1: "Lương là đủ" (~30-40%)

```
VỊ TRÍ: cạnh phải + threshold thấp. Kênh gốc biến thiên.
PE SOURCE: lương + ổn định + quy trình rõ

CẦN: Lương rõ, quy trình cụ thể, kỳ vọng chính xác, ổn định
KHÔNG CẦN: "Vision công ty", thử thách mới, autonomy nhiều

NHẬN DIỆN: "Ổn định, lương tốt, biết rõ phải làm gì"
VAI TRÒ: Vận hành, quy trình, back-office, QA, support
BACKBONE: Không có tệp này → công ty không vận hành được
```

### Tệp 2: "Cần ý nghĩa" (~15-20%)

```
VỊ TRÍ: cạnh trên hoặc trên-trái + threshold cao. Thường Novelty.
PE SOURCE: ý nghĩa task + autonomy + challenge

CẦN: Hiểu TẠI SAO, autonomy trong CÁCH làm, challenge có uncertainty
KHÔNG CẦN: Micromanage, lương cao mà task vô nghĩa, "cứ làm đi"

NHẬN DIỆN: "Có impact, được tự quyết, giải quyết vấn đề thật"
VAI TRÒ: R&D, strategy, product, founding team, lead kỹ thuật
⚠️ Top performer HOẶC "khó quản" — tùy environment match
```

### Tệp 3: "Thích kết nối" (~20-25%)

```
VỊ TRÍ: biến thiên, Oxytocin ưu thế. Threshold TB.
PE SOURCE: team tốt + sếp quan tâm + thuộc về

CẦN: Team tốt, cảm giác "thuộc về", công nhận đóng góp
KHÔNG CẦN: Remote 100% (cắt oxytocin), competitive ranking

NHẬN DIỆN: "Team vui, sếp tốt, làm cùng nhau"
VAI TRÒ: HR, customer success, team lead, onboarding, culture
KEO DÍNH: Không có tệp này → team = nhóm cá nhân
```

### Tệp 4: "Career growth" (~15-20%)

```
VỊ TRÍ: biến thiên, Serotonin nhạy. Threshold TB-cao.
PE SOURCE: thăng tiến + recognition + lộ trình rõ

CẦN: Lộ trình career RÕ, milestone + recognition, title tăng dần
KHÔNG CẦN: "Flat hierarchy" (thiếu vị thế PE), ambiguity tương lai

NHẬN DIỆN: "Có lộ trình rõ, biết đang đi đâu"
⚠️ Nhảy việc nếu ceiling. Hứa promote → delay = phá schema → mất.
```

### Tệp 5: "Enjoy quá trình" (~10-15%)

```
VỊ TRÍ: biến thiên, Opioid ưu thế. Threshold thấp-TB.
PE SOURCE: quá trình dễ chịu + pace phù hợp + environment tốt

CẦN: "Dễ chịu", routine có micro-PE, WLB thật, không gian thoải mái
KHÔNG CẦN: Deadline liên tục, competitive, "phá comfort zone" rhetoric

NHẬN DIỆN: "Thoải mái, nhịp vừa, enjoy được"
VAI TRÒ: Design, content, support, craftsmanship
ỔN ĐỊNH: Ở lâu nhất nếu environment đúng
```

### Tệp 6: "Muốn tự do" (~5-10%)

```
VỊ TRÍ: cạnh trái + threshold cao + PE Sensitivity thường cao. Thường Novelty.
PE SOURCE: autonomy CỰC ĐẠI + challenge thay đổi

CẦN: Chỉ định OUTPUT không định PROCESS, flexibility, challenge thay đổi
KHÔNG CẦN: Check-in hàng ngày, quy trình chi tiết, KPI cứng weekly

NHẬN DIỆN: "Tự do, làm theo cách mình, output quan trọng"
VAI TRÒ: Freelance role, senior IC, R&D, startup early stage
⚠️ Output BURST — cao vọt rồi thấp, tổng có thể rất cao
```

---

## 3. Mô Hình Vuông × Nhân Sự — Lens Sâu Hơn

🟡 Section MỚI v5.5. 6 tệp = practical shortcut. Section này cho lens CHÍNH XÁC HƠN.

```
⚠️ v5.5: mỗi nhân sự = VỊ TRÍ trên Mô Hình Vuông PER DOMAIN CÔNG VIỆC.
Cùng 1 người:
  Domain chuyên môn (code/design/strategy): cạnh trên (depth sâu, internal)
  Domain admin (report, meeting, email): cạnh phải (external, follow format)
  Domain leadership (dẫn team): cạnh trái-giữa (internal, depth TB)
→ KHÔNG GÁN 1 "tệp" cho toàn bộ người → gán PER DOMAIN.

6 TỆP → MÔ HÌNH VUÔNG MAPPING:

              ARCHITECT
        ┌─────────────────────┐
        │   Tệp 2             │
  IMP   │ (meaning)    Soldier-│  SOLDIER
  Tệp 6│              Deep    │  Tệp 1
  (tự do)│        Tệp 4       │  (lương)
        │        (career)      │
        └─────────────────────┘
              DRIFTER

  Tệp 1 = cạnh phải, threshold thấp
  Tệp 2 = cạnh trên + trên-trái, threshold cao
  Tệp 3 = không cố định vị trí (PE từ Oxytocin, không từ position)
  Tệp 4 = di chuyển LÊN TRÊN theo thời gian (career = depth TĂNG)
  Tệp 5 = không cố định (PE từ Opioid environment)
  Tệp 6 = cạnh trái, threshold cao

  → Tệp 3 và 5 KHÔNG map rõ vào Mô Hình Vuông vì PE source =
    kênh gốc (Oxytocin/Opioid), không phải position.
  → Tệp 1, 2, 6 map RÕ vì PE source = position-dependent.
```

```
v5.5 INSIGHT — SOLDIER-DEEP (concept MỚI):

  v5.0: Soldier = nông, follow. v5.5: Soldier-Deep = external + deep = HỢP LỆ.
  Professor 30 năm nghiên cứu sách = Soldier-Deep (Core.md §8.2).

  TRONG HR: Senior specialist external source = Soldier-Deep.
    Depth composite CỰC CAO ở domain chuyên môn.
    Source vẫn external (follow methodology, standards, research).
    → KHÔNG phải Architect (internal tự tạo) — là Soldier-Deep (external deepen).
    → Performance CAO. Ổn định. Follow proven methods.
    → Khác biệt: KHÔNG innovation (Architect), nhưng EXCELLENCE trong known domain.

  HR implication: Soldier-Deep ≠ "thiếu sáng tạo" = "expert trong domain proved."
  → Đánh giá ĐÚNG = respect expertise. Đánh giá SAI = "cần sáng tạo hơn" → frustrated.
```

```
v5.5 — COMPLIANCE = DERIVED trong HR:

  Compliance(person, team) = chunk_overlap(person.chunks, team.chunks).
  → CÙNG NGƯỜI, KHÁC TEAM → KHÁC "tệp."

  VD: Developer A:
    Ở team startup (flat, explore): "tệp 2" (ý nghĩa, autonomy)
    Ở team enterprise (process, hierarchy): "tệp 1" vibes (follow process, ổn định)
    → CÙNG NGƯỜI, vị trí Vuông KHÔNG ĐỔI, nhưng chunk_overlap với team KHÁC
    → "Tệp" THAY ĐỔI theo environment.

  HR implication: trước khi gán "tệp" → check ENVIRONMENT.
  → "Performance thấp" có thể = person × team mismatch, không phải person issue.
```

---

## 4. Depth Composite × Seniority

🟡 Section MỚI v5.5. Core.md §8.2 định nghĩa Depth = composite 4 sub-params. Section này áp dụng: đánh giá seniority = đánh giá depth composite.

```
SENIORITY ≠ SỐ NĂM. SENIORITY = DEPTH COMPOSITE ở domain công việc.

4 SUB-PARAMS CỦA SENIORITY:

  SUB 1 — CHUNK QUALITY: predict kết quả công việc CHÍNH XÁC.
    Junior: "code chạy" nhưng predict edge cases kém.
    Senior: predict bugs, predict system behavior trước khi test.
    → Quality = ACCURACY of predictions ở domain chuyên môn.

  SUB 2 — CONNECTIVITY: chunks liên kết thành understanding.
    Junior: biết A, biết B, nhưng không thấy connection.
    Senior: "A affect B because C" → connected understanding.
    → Connectivity = "hiểu HỆ THỐNG" không chỉ "biết TỪNG PHẦN."

  SUB 3 — CLUSTER FORMATION: chunks tổ chức thành expertise domain.
    Junior: rải rác, chưa có "lĩnh vực chuyên."
    Mid: bắt đầu có domain cluster (backend / frontend / infra).
    Senior: cluster LỚN + tổ chức tốt → expert domain rõ ràng.

  SUB 4 — CLUSTER MATURITY / CONVERGENCE:
    Mid-senior: clusters ổn định nhưng CÔ LẬP (chỉ expert 1 domain).
    Staff/Principal: clusters OVERLAP → cross-domain insight.
    → "Staff engineer" = depth composite CAO + convergence CAO (bridge systems).

🔴 INSIGHT v5.5: "Senior" label dựa trên years ≠ depth composite thực tế.
  3 năm kinh nghiệm + depth composite cao (quality + connectivity + clusters)
    > 10 năm kinh nghiệm + depth sub 1 only (biết nhiều nhưng không connect).
  → Đánh giá seniority = đánh giá 4 sub-params, KHÔNG chỉ đếm năm.

DEPTH COMPOSITE KHÁC PER SOURCE:
  Soldier-Deep (external): depth qua STUDY + FOLLOW proven methods.
    → Quality cao (learned correct patterns), connectivity TB (follows connections others found).
  Architect-Deep (internal): depth qua EXPERIMENT + SELF-VERIFY.
    → Quality cao (discovered patterns), connectivity CAO (built own connections).
  → CẢ HAI valid. Soldier-Deep = expert. Architect-Deep = innovator.
  → Team cần CẢ HAI: expert (reliable) + innovator (breakthrough).
```

---

## 5. Convergence × Cross-Functional Teams

🔴 Section MỚI v5.5. Core.md §8.9 mô tả convergence. Section này áp dụng cho team cross-functional.

```
CROSS-FUNCTIONAL TEAM = người từ KHÁC domain clusters làm việc CÙNG.

VẤN ĐỀ: mỗi người expert 1 domain → clusters KHÔNG OVERLAP
  → chunk_overlap(engineer, designer) THẤP
  → Predict nhau kém → communication cost CAO → friction

CONVERGENCE = GIẢI PHÁP:
  Người convergence CAO (shared foundation chunks across domains):
    Bridge giữa domain clusters → GIẢM communication cost.
    "Ồ, anh backend nói vậy có nghĩa tương tự như concept UX này."
    = TRANSLATE giữa domain languages vì foundation chunks CHUNG.

  VD: Product Manager convergence cao:
    Shared chunks: {systems thinking, user mental model, cost-benefit analysis}
    → Bridge engineering (systems) + design (user model) + business (cost-benefit).
    → PM = CONVERGENCE ROLE. PM tốt = convergence CAO tự nhiên.

HR IMPLICATION:
  Cross-functional team HIỆU QUẢ cần ÍT NHẤT 1 người convergence cao.
  → Roles: PM, tech lead, architect, senior designer = bridge roles.
  → Hiring: check convergence (RAT, cross-domain transfer — Psychometrics §5).

  "Expert advice not trusted" = chunk overlap THẤP:
    Expert A predict based on deep domain chunks.
    Team không có shared chunks → KHÔNG hiểu reasoning → KHÔNG trust.
    → Fix: expert GIẢI THÍCH bằng foundation chunks (translate domain → general).
    → Hoặc: bridge person (convergence cao) translate cho team.
```

---

## 6. Dopamine Inverted-U × Burnout vs Boredom

🟡 Section MỚI v5.5. Core.md §6.6 mô tả Dopamine inverted-U. Section này: predict burnout vs boredom per vị trí.

```
DOPAMINE INVERTED-U PREDICT RỦI RO KHÁC NHAU:

  BÊN TRÁI (dopamine thấp) → RỦI RO: ANHEDONIA
    PE gần zero → không deepen, không explore → stagnation.
    HR signal: "chả thấy gì vui", output sụp, withdraw.
    → CẦN: giảm cortisol + tạo micro-PE (small wins, recognition).

  TẠI ĐỈNH (tonic/phasic cân bằng) → OPTIMAL
    Deepen BỀN + explore KHI CẦN. Sustainable performance.
    → GIỮ: environment ổn, challenge vừa đủ, autonomy phù hợp.

  BÊN PHẢI (phasic > tonic) → RỦI RO: BOREDOM
    Habituate nhanh → cần novelty liên tục → chán role ổn định.
    HR signal: chuyển project liên tục, output burst rồi drop, hỏi "có gì mới?"
    → CẦN: challenge thay đổi, variety, project rotation.
    → Đây thường = tệp 6 (Improviser, Novelty, threshold cao).

  CỰC PHẢI (pathological) → RỦI RO: BURNOUT (cortisol-driven grit)
    Tưởng "đam mê" nhưng cortisol-driven → cortisol treadmill (§6.4).
    HR signal: output CAO liên tục → đột ngột CRASH.
    → CẦN: force breaks, monitor cortisol indicators (sick days, irritability).

BURNOUT vs BOREDOM — 2 RỦI RO KHÁC NHAU:

  ┌──────────────┬─────────────────────┬─────────────────────┐
  │ Rủi ro       │ Ai gặp?             │ Giải pháp           │
  ├──────────────┼─────────────────────┼─────────────────────┤
  │ Burnout      │ Tệp 2,4 cortisol   │ Giảm pace, force    │
  │              │ driven, cạnh trên   │ breaks, giảm cortisol│
  │ Boredom      │ Tệp 6, threshold   │ Challenge mới,      │
  │              │ cao, cạnh trái      │ project rotation     │
  │ Anhedonia    │ Tệp 5 bị toxic env │ Fix environment,     │
  │              │ hoặc anyone crushed │ micro-PE, safety     │
  │ Stagnation   │ Tệp 1 environment  │ Thường OK (threshold │
  │              │ ổn định quá lâu     │ thấp), chỉ issue    │
  │              │                     │ nếu market shift     │
  └──────────────┴─────────────────────┴─────────────────────┘

  → CÙNG "performance giảm" nhưng NGUYÊN NHÂN KHÁC → GIẢI PHÁP KHÁC.
  → Manager KHÔNG chẩn đoán đúng → can thiệp SAI → tệ hơn.
  → VD: burnout (cần nghỉ) mà push thêm challenge = crash.
        boredom (cần challenge) mà cho nghỉ = chán hơn.
```

---

## 7. Ma Trận Nhu Cầu + Task

### Ma trận nhu cầu

```
              Lương  Ý nghĩa  Team   Career  Process  Autonomy  Challenge  WLB
              ─────  ───────  ────   ──────  ───────  ────────  ─────────  ───
Tệp 1 Lương  ★★★★★  ★        ★★     ★★      ★★★★★   ★         ★          ★★★
Tệp 2 Ý nghĩa ★★★  ★★★★★    ★★★    ★★★     ★        ★★★★★    ★★★★★      ★★
Tệp 3 Kết nối ★★★  ★★       ★★★★★  ★★★     ★★★      ★★       ★★         ★★★
Tệp 4 Career ★★★★  ★★★      ★★★    ★★★★★   ★★★      ★★★      ★★★★       ★★
Tệp 5 Enjoy  ★★★   ★★       ★★★    ★★      ★★★      ★★★      ★          ★★★★★
Tệp 6 Tự do  ★★★   ★★★★     ★★     ★★★     ★        ★★★★★    ★★★★★      ★★★★

(★★★★★ = deal-breaker nếu thiếu)
```

### Ma trận task × mode phù hợp

```
                    Tệp 1   Tệp 2   Tệp 3   Tệp 4   Tệp 5   Tệp 6
                    ─────    ─────    ─────    ─────    ─────    ─────
Task lặp lại        ✅✅✅    ❌       ✅       ✅       ✅✅     ❌
Task sáng tạo       ❌       ✅✅✅    ✅       ✅       ✅       ✅✅✅
Task khẩn cấp       ✅       ✅✅     ❌       ✅✅     ❌       ✅
Task dài hơi        ✅✅     ✅✅✅    ✅       ✅✅✅    ✅       ❌
Task teamwork       ✅       ✅       ✅✅✅    ✅       ✅       ❌
Task solo           ✅       ✅✅     ❌       ✅       ✅✅     ✅✅✅
Task process-heavy  ✅✅✅    ❌       ✅       ✅       ✅       ❌❌
Task ambiguous      ❌       ✅✅✅    ❌       ✅       ❌       ✅✅✅
Task tỉ mỉ          ✅✅     ❌       ✅       ✅       ✅✅✅    ❌
```

---

## 8. Tuyển Dụng v5.5

### Câu hỏi phỏng vấn

```
CÂU HỎI KÊNH GỐC:
  "Nếu tiền không phải vấn đề, bạn làm gì?"
    → Nghiên cứu/khám phá = Novelty
    → Du lịch/trải nghiệm/thủ công = Opioid
    → Dạy/giúp/tổ chức cộng đồng = Oxytocin

CÂU HỎI THRESHOLD:
  "Mô tả lần cuối THỰC SỰ hứng thú với công việc"
    → Task đơn giản + lương tốt = threshold thấp
    → Task phức tạp + có impact = threshold cao
  "Bao lâu thì bạn chán 1 role?"
    → 3+ năm ok = threshold thấp-TB.  <1 năm = threshold cao + sensitivity cao

CÂU HỎI VỊ TRÍ VUÔNG (thay "compliance mode" v5.0):
  "Bạn thích được hướng dẫn chi tiết hay tự tìm cách?"
    → Chi tiết = cạnh phải (external source)
    → Tự tìm = cạnh trái hoặc trên (internal)
  "Khi quy trình không hợp lý, bạn làm gì?"
    → Theo = cạnh phải
    → Đề xuất sửa = cạnh trên (internal deep)
    → Làm cách khác luôn = cạnh trái (internal, low structure)

CÂU HỎI PE SOURCE → TỆP:
  "Điều gì khiến bạn CHÁN NHẤT?"
    → "Lương thấp" = tệp 1  → "Vô nghĩa" = tệp 2
    → "Team tệ" = tệp 3    → "Không lộ trình" = tệp 4
    → "Quá áp lực" = tệp 5  → "Bị kiểm soát" = tệp 6

CÂU HỎI CONVERGENCE (MỚI v5.5 — cho bridge roles):
  "Khi gặp vấn đề ở domain MỚI, bạn tiếp cận thế nào?"
    → "Áp dụng nguyên tắc domain cũ" = convergence cao → phù hợp PM, lead
    → "Học từ đầu" = convergence thấp → phù hợp deep specialist

CÂU HỎI SCHEMA (hỏi 2-3 chỗ cũ → tìm pattern):
  "Tại sao nghỉ chỗ cũ?"
    → Cùng lý do lặp lại = PE source CHÍNH bị thiếu
```

### Check fit: role × profile

```
TRƯỚC KHI HIRE: map role cần gì trên Mô Hình Vuông

  Role vận hành: cạnh phải + depth từ TB trở lên → Tệp 1, 5
  Role sáng tạo: cạnh trên hoặc trái → Tệp 2, 6
  Role kết nối: Oxytocin + bất kỳ vị trí → Tệp 3
  Role leadership: convergence CAO + depth composite CAO → bridge roles
  Role management track: serotonin nhạy + depth tăng dần → Tệp 4

  ⚠️ v5.5: cùng 1 role có thể cần KHÁC vị trí per domain:
    Tech Lead: cạnh trên ở domain kỹ thuật + convergence cao ở domain team
    → Check PER DOMAIN, không chỉ "tệp nào."
```

---

## 9. Giữ Người Per Tệp

```
TỆP 1 MUỐN NGHỈ:
  Nguyên nhân: lương thấp hơn thị trường, quy trình loạn
  Giải pháp: tăng lương + ổn định quy trình → GIỮ ĐƯỢC
  Dấu hiệu: hỏi lương chỗ khác, so sánh

TỆP 2 MUỐN NGHỈ:
  Nguyên nhân: task vô nghĩa, bị micro, không grow
  Giải pháp: project có impact + autonomy → GIỮ ĐƯỢC
  ⚠️ Tăng lương → giữ 3-6 tháng MAX → vấn đề quay lại
  Dấu hiệu: output giảm, quiet quit, hỏi "tại sao?"

TỆP 3 MUỐN NGHỈ:
  Nguyên nhân: mất team/sếp, restructure, conflict
  Giải pháp: fix team relationship → GIỮ ĐƯỢC
  ⚠️ Tăng lương → KHÔNG HIỆU QUẢ (PE từ người)
  Dấu hiệu: withdraw, ít nói, ít tương tác

TỆP 4 MUỐN NGHỈ:
  Nguyên nhân: ceiling, không lộ trình, hứa nhưng không promote
  Giải pháp: promote THẬT hoặc lộ trình MỚI → GIỮ ĐƯỢC
  ⚠️ Hứa suông = PHÁ schema → mất
  Dấu hiệu: hỏi lộ trình, so sánh title

TỆP 5 MUỐN NGHỈ:
  Nguyên nhân: quá áp lực, environment toxic, pace quá nhanh
  Giải pháp: giảm pace + fix environment → GIỮ ĐƯỢC
  ⚠️ v5.5: check dopamine inverted-U → có thể bên trái (anhedonia) → cần khác
  Dấu hiệu: mệt mỏi, ốm nhiều, xin nghỉ phép thường xuyên

TỆP 6 MUỐN NGHỈ:
  Nguyên nhân: bị ép process, mất autonomy, bored
  Giải pháp: autonomy + challenge mới → GIỮ ĐƯỢC
  ⚠️ Thêm process → mất NGAY
  Dấu hiệu: bỏ meeting, không theo process, "check out"

SAI LẦM #1: "Tăng lương cho tất cả"
  Tệp 1: ✅ hiệu quả.  Tệp 2-6: ❌ PE source ≠ tiền.
  → Chỉ giữ ~30-40%. 60% cần thứ KHÁC.
```

---

## 10. Xây Team + Dynamic Per Phase

```
TEAM TỐI ƯU (10 người):
  3-4 × Tệp 1: backbone vận hành
  2   × Tệp 3: keo dính team
  1-2 × Tệp 2 hoặc 6: innovation
  1-2 × Tệp 4: drive performance
  1   × Tệp 5: balance, tỉ mỉ
  → Portfolio đa dạng, mỗi tệp BỔ SUNG chức năng

v5.5: + ÍT NHẤT 1 người convergence cao = BRIDGE role
  → Không cần thêm headcount — identify convergence trong team hiện có.

DYNAMIC PER PHASE:
  Phase 0→1 (startup/new): ưu tiên tệp 2 + 6 (explore, innovation)
  Phase 1→N (scale): ưu tiên tệp 1 + 3 (vận hành, keo dính)
    ⚠️ Giữ tệp 2+6 trong phase scale = frustrated HOẶC phá
  Phase khủng hoảng: tệp 4 (drive) + tệp 3 (cohesion) + tệp 2 (giải pháp)

v5.5 INSIGHT — TEAM CONVERGENCE:
  Team toàn deep specialist (convergence thấp) → silo, communication cost CAO.
  Team có bridge roles (convergence cao) → cross-pollination → innovation.
  → Best team: mix deep specialists + bridge roles.
```

---

## 11. Quản Lý Hàng Ngày: 1-on-1 + Giao Việc

### 1-on-1 per mode

```
Tệp 1: ngắn, cụ thể. "KPI ok? Cần support gì?" 2 tuần/lần.
Tệp 2: sâu. "Project có ý nghĩa? Muốn thử hướng nào?" Hàng tuần.
Tệp 3: quan hệ. "Team ổn? Bạn cảm thấy sao?" Hàng tuần.
Tệp 4: career. "Ở đâu trên lộ trình? Milestone tiếp?" 2 tuần/lần.
Tệp 5: environment. "Workload ok? Pace ổn?" 2 tuần/lần.
Tệp 6: minimal. "Output ok? Idea mới? Cần tôi TRÁNH gì?" Khi cần.
```

### Giao việc per mode

```
Tệp 1: "Đây là task. Đây là bước. Deadline thứ 6. KPI là X."
Tệp 2: "Vấn đề là X. Cần vì Y (impact). Bạn có cách nào?"
Tệp 3: "Team đang cần X. Phụ trách, phối hợp với A và B."
Tệp 4: "Task này là bước để bạn [milestone]. Đạt X → recognition Y."
Tệp 5: "Pace thế này, deadline flexible, cần chất lượng Z."
Tệp 6: "Cần output X trước thứ 6. Cách làm tùy bạn."
```

---

## 12. Xung Đột Team

```
TỆP 2 vs 1: "Không đam mê" vs "Đòi hỏi quá"
  Cơ chế: threshold mismatch. Giải: tệp 2 design, tệp 1 execute.

TỆP 6 vs 1: "Phá quy trình" vs "Không theo process"
  Cơ chế: vị trí Vuông khác (cạnh trái vs cạnh phải). Giải: interface rõ.

TỆP 4 vs 3: "Ai xứng đáng" vs "Sao cạnh tranh"
  Cơ chế: serotonin vs oxytocin PE source. Giải: recognition cá nhân + team appreciation.

TỆP 2 vs 6: "Cần structure" vs "Không cần gì"
  Cơ chế: cạnh trên (internal structured) vs cạnh trái (internal unstructured).
  Giải: tệp 2 framework, tệp 6 fill creativity.

SẾP ↔ NHÂN SỰ:
  Sếp tệp 2 + team tệp 1: "Sao không tự nghĩ?" → Cho QUY TRÌNH, giữ vision cho mình.
  Sếp tệp 1 + team tệp 2: "Cứ theo process!" → Cho SPACE, giữ process cho team khác.
  Sếp tệp 4 + team tệp 5: "Push liên tục" → Calibrate pace per person.

  → MỌI TRƯỜNG HỢP: sếp đang PROJECTION mode mình lên team.
  → Giải: sếp nhận diện mode MÌNH → adapt per nhân viên.
```

---

## 13. Áp Lực Tối Ưu — Inverted-U Per Mode

```
Drive = Thưởng − Chi phí
🟢 Yerkes-Dodson (1908) = INVERTED-U: hiệu suất tối ưu ở stress trung bình.
Cơ chế v5.5: cortisol moderate → VTA → dopamine ↑ → drive (§6.4).

ÁP LỰC TỐI ƯU PER TỆP:
  Tệp 1: thấp-TB. Deadline rõ, KPI rõ, không surprise.
  Tệp 2: TB-cao. Challenge có ý nghĩa, ambiguity ok.
  Tệp 3: thấp-TB. Team ổn, sếp support.
  Tệp 4: TB-cao. Milestone rõ, race to next level.
  Tệp 5: thấp. Pace ổn, quality > speed. Burnout NHANH NHẤT.
  Tệp 6: TB-cao. Challenge thay đổi, output-based.

v5.5: Kết hợp Dopamine inverted-U (§6) cho chẩn đoán chính xác hơn:
  Performance giảm → BURNOUT (cortisol) hay BOREDOM (dopamine)?
  → Chẩn đoán SAI = can thiệp SAI = tệ hơn.
```

---

## 14. Mode Sếp + 7 Sai Lầm

```
SẾP TỐI ƯU: biết mode MÌNH + nhận diện PE source TỪNG NGƯỜI.
  Không có "1 kiểu sếp giỏi." Có "sếp adapt per person."
  Framework = công cụ xây prediction depth ở domain "con người."

7 SAI LẦM PHỔ BIẾN:

  1. "Tăng lương = giữ người" → chỉ đúng tệp 1 (~30-40%)
  2. "Truyền lửa cho mọi người" → tệp 1+5 cần ổn định, không cần lửa
  3. "Quy trình cho tất cả" → tệp 2+6 bị kill drive
  4. "Flat hierarchy = tốt" → tệp 4 mất PE vị thế, tệp 1 mất structure
  5. "Team building = party" → team building THẬT = task collaboration
  6. "Sếp projection" → quản lý theo mode MÌNH, không phải mode nhân viên
  7. "Performance thấp = người kém" → có thể = người tốt + SAI role × mode
     → Trước khi đuổi: check mode × role match

v5.5 THÊM SAI LẦM:
  8. "Gán 1 tệp cho toàn bộ người" → cùng 1 người khác tệp per domain
  9. "Không consider environment" → compliance = derived → cùng người khác team = khác behavior
  10. "Treat burnout = boredom" → nguyên nhân KHÁC → giải pháp KHÁC (§6)
```

---

## 15. Chunk Config Card v5.5

```
⚠️ v5.5 REDESIGN từ "Mode Card" v5.0 → "Chunk Config Card":

╔═══════════════════════════════════════════════════════════╗
║  CHUNK CONFIG CARD v5.5 — [Tên] — [Role]                  ║
╠═══════════════════════════════════════════════════════════╣
║                                                           ║
║  PHẦN CỨNG (quan sát):                                    ║
║    Kênh gốc ưu thế:    □ Novelty  □ Opioid  □ Oxytocin  ║
║    Threshold:            □ Thấp    □ TB      □ Cao       ║
║    PE Sensitivity:       □ Thấp    □ TB      □ Cao       ║
║    Dopamine inverted-U:  □ Trái    □ Đỉnh    □ Phải     ║
║                                                           ║
║  TỆP SHORTCUT: □ 1-Lương  □ 2-Ý nghĩa  □ 3-Kết nối     ║
║                □ 4-Career  □ 5-Enjoy    □ 6-Tự do        ║
║                                                           ║
║  MÔ HÌNH VUÔNG PER DOMAIN CÔNG VIỆC:                      ║
║                                                           ║
║    Domain chuyên môn:    [vị trí: ___________]            ║
║    Domain admin/process: [vị trí: ___________]            ║
║    Domain leadership:    [vị trí: ___________]            ║
║    Convergence:          □ Thấp  □ TB  □ Cao             ║
║                                                           ║
║  DEPTH COMPOSITE (domain chính):                           ║
║    Sub 1 (quality):      □ Nông  □ TB  □ Sâu            ║
║    Sub 2 (connectivity): □ Thấp  □ TB  □ Cao            ║
║    Sub 3 (clusters):     □ Chưa  □ Hình thành  □ Mature ║
║    Sub 4 (convergence):  □ Thấp  □ TB  □ Cao            ║
║    → Seniority ước tính: □ Junior  □ Mid  □ Senior       ║
║                                                           ║
║  QUẢN LÝ:                                                 ║
║    PE source chính:      _______________                  ║
║    Kill switch:          _______________                  ║
║    Giao việc style:      _______________                  ║
║    1-on-1 focus:         _______________                  ║
║    Áp lực tối ưu:        □ Thấp  □ TB  □ Cao            ║
║    Rủi ro chính:         □ Burnout  □ Boredom  □ Anhedonia║
║    ⚠️ KHÔNG:              _______________                  ║
║                                                           ║
║  COMPLIANCE (DERIVED v5.5):                                ║
║    vs Team hiện tại:     chunk_overlap = _____ → ___     ║
║    → Nếu đổi team:      overlap có thể thay đổi         ║
╚═══════════════════════════════════════════════════════════╝
```

---

## 16. Câu Hỏi Mở

| # | Câu hỏi | Ưu tiên |
|---|---------|---------|
| 1 | 6 tệp: đủ chưa? Có tệp nào thiếu? | Cao |
| 2 | Depth composite 4 sub → predict performance tốt hơn years? | Cao nhất |
| 3 | Convergence → predict PM/lead effectiveness? | Cao |
| 4 | Dopamine inverted-U → predict burnout vs boredom accurately? | Cao |
| 5 | Tệp thay đổi theo tuổi/kinh nghiệm thế nào? | TB |
| 6 | Remote vs office: impact per tệp? | TB |
| 7 | Startup vs corp: mode mix tối ưu khác? | Cao |
| 8 | Chunk Config Card: validate bằng data thực? | Cao nhất |
| 9 | Sếp awareness: trainable? Bao lâu? | Cao |
| 10 | Soldier-Deep vs Architect: đánh giá differentiation trong hiring? | Cao |

---

## 17. Kết Nối

| Tham khảo | File | Mối liên hệ |
|-----------|------|-------------|
| Drive equation | Core.md §7 | Cơ bản: thưởng − chi phí per person |
| Mô Hình Vuông | Core.md §8.2 | Vị trí per domain → nhận diện nhân sự |
| Depth composite | Core.md §8.2 | 4 sub-params → seniority (§4) |
| Compliance phái sinh | Core.md §8.3 | Cùng người × khác team = khác behavior |
| Chunk Topology | Core.md §8.9 | Convergence → cross-functional teams (§5) |
| Dopamine inverted-U | Core.md §6.6 | Burnout vs boredom prediction (§6) |
| Cortisol inverted-U | Core.md §6.4 | Áp lực tối ưu (§13) |
| ECP | Core.md §9 | Tại sao tệp 1 chiếm đa số |
| Kênh gốc, threshold | Core.md §3, §5 | Phần cứng → PE source → tệp nào |
| 4 pattern chi tiết | Core-Deep-Dive/Chunk-Patterns.md | Biến thể, shift, phase model |
| Giáo dục | Applications/Education.md | Trường tạo tệp 1 mặc định |
| Đánh giá gamedev | Applications/HR-Assessment-Gamedev.md | Hệ thống đánh giá per role |
| Đồng nghiệp tương thích | Applications/Relationships.md §9 | Team compatibility |
| Psychometrics | Research/Psychometrics-Mapping.md | Battery đo chunk config |
| Reward system | Applications/Reward-Economics.md | Phổ thưởng, bootstrapping |

---

> *Quản Lý Nhân Sự — Framework v5.5*
> *6 tệp = practical shortcut. Đằng sau = Mô Hình Vuông per domain.*
> *4 sections MỚI v5.5: Mô Hình Vuông × HR (Soldier-Deep, compliance derived),*
> *Depth Composite × Seniority (4 sub-params > years), Convergence × Cross-Functional (bridge roles),*
> *Dopamine Inverted-U × Burnout vs Boredom (chẩn đoán khác → giải pháp khác).*
> *Chunk Config Card v5.5 redesign: depth sub-params, convergence, compliance derived, DA inverted-U.*
> *Prerequisite: Core.md §5-8, §8.9.*
