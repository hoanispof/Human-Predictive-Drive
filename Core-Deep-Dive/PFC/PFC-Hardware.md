---
title: PFC-Hardware — Individual Hardware Parameters
version: 1.1
created: 2026-04-19
updated: 2026-05-10 (v1.1 — §3.4-§3.5 COMT×Reward, §4.7-§4.8 DRD4×Reward+COMT×DRD4, §8b-§8c Receptor×Profiles+Shorthand)
status: REFERENCE v1.1
scope: |
  Hardware parameters tạo sự khác biệt PFC giữa các cá nhân.
  Focus: COMT, DRD4, NE receptors, Capacity/Quality.
  Cùng 24 functions (PFC-Function.md) nhưng KHÁC hardware → KHÁC output.
supersedes: |
  PFC/Imagination/backup/PFC-Analysis-v1.1.md §8 (2026-03-15, ~985L)
  Insights integrated, framing updated to v7.8 cycle-based.
related: |
  PFC-Function.md — 24 functions PFC thực hiện
  PFC-Development.md — PFC qua giai đoạn đời + training
  PFC-Hold-Dimensions.md — Tại sao ~4±1 dimensions
  Neural-Architecture.md §2 — Physical PFC sub-regions
  Cortisol-Baseline.md v2.0 — Cortisol affects PFC function
  Core-v7.8-Draft.md §6 — PFC trong kiến trúc tổng thể
language: Tiếng Việt primary + English technical terms
confidence: 🟢 Research support | 🟡 Framework synthesis | 🔴 Hypothesis
---

# PFC Hardware — Tại Sao Cùng 24 Functions Mà Output Khác Nhau

> **Cùng 24 functions (PFC-Function.md), cùng ~4±1 slots (Hold).**
> **Khác HARDWARE → khác OUTPUT.**
>
> Hardware = CÁI KHÔNG THAY ĐỔI (hoặc thay đổi cực chậm).
> Training = CÁI THAY ĐỔI ĐƯỢC (PFC-Development.md).
>
> File này trả lời: tại sao 2 người cùng trải nghiệm, cùng chunks,
> mà 1 người "chán nhanh" còn 1 người "đào sâu"?
> = Hardware khác, không phải "ý chí" khác.

---

## Mục lục

- §1 — 2 Thuộc Tính Hardware Chính
- §2 — Observed Capacity ≠ Hardware Ceiling
- §3 — COMT: Clear Speed (Improviser vs Specialist)
- §4 — DRD4: Chunk Threshold (Data, Lỗ Hổng, Hypothesis D)
- §5 — MAO-A: Mood Stability (Toàn Não)
- §6 — NE α2/α1: PFC Circuit Breaker
- §7 — VTA Detection Loop (7 Bước)
- §8 — 4 Receptor Systems Summary
- §9 — Honest Assessment
- §10 — Cross-References

---

## §1 — 2 Thuộc Tính Hardware Chính

```
⚠️ LƯU Ý: Capacity và Clear Speed là HIỆN TƯỢNG ĐO ĐƯỢC
   (người khác nhau rõ ràng — observable, measurable).
   Research (COMT, DRD4,...) là CANDIDATE tốt nhất hiện tại
   để giải thích cơ chế — khả năng cao map đúng, chưa chắc
   tuyệt đối chính xác. Framework dùng với mức tin cậy này.

  ┌─────────────┬──────────────────────────────┬──────────────────┐
  │             │ ① PFC-QUALITY                │ ② CLEAR SPEED    │
  ├─────────────┼──────────────────────────────┼──────────────────┤
  │ Là gì       │ CHẤT LƯỢNG workspace:        │ Tốc độ xóa      │
  │             │ Mọi người đều hold ~4±1 slots.│ draft cũ để     │
  │             │ (Interference limit = physics,│ nhường chỗ      │
  │             │ KHÔNG phải thiếu neurons.)    │ draft mới.      │
  │             │ Quality KHÔNG ảnh hưởng SỐ   │                  │
  │             │ slots mà ảnh hưởng CHẤT LƯỢNG│                  │
  │             │ xử lý PER-SLOT:              │                  │
  │             │ ① Resolution: rõ hay mờ      │                  │
  │             │ ② Noise filter: giữ sạch dù  │                  │
  │             │    có nhiễu hay dễ mất        │                  │
  │             │ ③ Retrieval: lấy chunk từ B   │                  │
  │             │    nhanh/đúng hay chậm/sai   │                  │
  │             │ ④ Compression: compile chunk  │                  │
  │             │    chặt → mỗi slot chứa NHIỀU│                  │
  ├─────────────┼──────────────────────────────┼──────────────────┤
  │ Hardware    │ PFC connection density +     │ COMT variant     │
  │             │ wiring quality (KHÔNG phải   │ (PFC-specific    │
  │             │ số neurons — 10 tỉ vs 12 tỉ │ enzyme)          │
  │             │ vẫn ~4±1 slots, nhưng chất   │                  │
  │             │ lượng per-slot KHÁC)         │                  │
  ├─────────────┼──────────────────────────────┼──────────────────┤
  │ CAO =       │ 4±1 slots × high resolution  │ Clear nhanh      │
  │             │ × clean × fast retrieve      │ → workspace      │
  │             │ × deep compression           │ TRỐNG nhanh      │
  │             │ = "Nhìn 4 thứ nhưng THẤY    │ → fresh rebuild  │
  │             │ cả vũ trụ" (expert)          │                  │
  ├─────────────┼──────────────────────────────┼──────────────────┤
  │ THẤP =      │ 4±1 slots × low resolution   │ Clear chậm       │
  │             │ × noisy × slow retrieve      │ → draft GIỮ LÂU  │
  │             │ × shallow compression        │ → incremental    │
  │             │ = "Nhìn 4 thứ chỉ THẤY 4    │ modify           │
  │             │ thứ" (novice)                │                  │
  ├─────────────┼──────────────────────────────┼──────────────────┤
  │ Ảnh hưởng   │ CẢ improviser VÀ specialist  │ CHÍNH cho        │
  │             │ đều lợi khi quality CAO      │ Improviser vs    │
  │             │                              │ Specialist       │
  │             │                              │ tendency         │
  └─────────────┴──────────────────────────────┴──────────────────┘

  ⚠️ QUAN TRỌNG: "4±1 slots" = CỐ ĐỊNH do physics (interference limit)
     10 tỉ vs 20 tỉ neurons PFC → VẪN ~4±1 slots
     → Evolution giải quyết bằng: compile → stack → pyramidal
     → KHÔNG cần PFC lớn hơn → cần compile CHẤT LƯỢNG hơn
     → Chi tiết: PFC-Hold-Dimensions.md

  2 thuộc tính INDEPENDENT → tạo NHIỀU profiles:
    Quality cao + Clear nhanh = "improviser có chiều sâu"
    Quality cao + Clear chậm  = "specialist có chiều rộng"
    Quality thấp + Clear nhanh = "nhảy lung tung, không sâu"
    Quality thấp + Clear chậm  = "chậm và hẹp"
```

🟢 Evidence: Cowan 2001 (~4±1), Bays & Husain 2008 (interference = precision drop),
Kane & Engle 2002 (WM capacity = noise filter), Chase & Simon 1973 (expert = compression quality)

---

## §2 — Observed Capacity ≠ Hardware Ceiling

```
🟡 "PFC mạnh/yếu" = MƠ HỒ. Observed Capacity là EMERGENT từ 4 yếu tố:

  OBSERVED CAPACITY = Hardware Ceiling × Chunks Quality × Cortisol State × Context Fit

  ① Hardware Ceiling (genetics — thay đổi CỰC CHẬM):
     → Connection density, wiring quality → set RANGE
     → Đo KHÓ NHẤT + can thiệp ÍT NHẤT
     → 🟢 Neural efficiency: người giỏi fire ÍT hơn, KHÔNG nhiều hơn
        (Haier 1992, Neubauer & Fink 2009) → hiệu quả > dung tích
     → 🟢 Brain size vs IQ: tương quan RẤT YẾU (~0.24, ~6% variance)
        (Pietschnig 2015, meta-analysis 148 studies)

  ② Chunks Quality (education + experience — thay đổi qua NĂM):
     → Chunks compiled SÂU + TỔ CHỨC TỐT → retrieval nhanh, đúng
     → Chunks PHONG PHÚ → PFC có NGUYÊN LIỆU → output giàu
     → Chunks NGHÈO → PFC draft trong trống → output nghèo dù PFC tốt
     → Compression pyramidal (4×4×4) CHỈ hoạt động khi chunks ĐÃ COMPILED
     → = "PFC giỏi nhưng B areas trống = xưởng tốt, không nguyên liệu"
     → CAN THIỆP ĐƯỢC: giáo dục + experience + compile time (ngủ đủ)

  ③ Cortisol State (mode — thay đổi qua GIỜ):
     → Cortisol thấp → PFC clean, filter tốt, retrieve chính xác
     → Cortisol cao → PFC noisy, filter kém, retrieve sai/chậm
     → CÙNG hardware + CÙNG chunks + KHÁC cortisol = KHÁC output
     → = "Sáng khỏe nghĩ ra, chiều mệt nghĩ không ra" = cùng PFC
     → CAN THIỆP ĐƯỢC: ngủ đủ, giảm stress, body care

  ④ Context Fit (match domain — thay đổi khi đổi MÔI TRƯỜNG):
     → Chunks MATCH domain hiện tại → PFC retrieve NGAY → "nhanh"
     → Chunks KHÔNG match → PFC phải build mới → "chậm" dù PFC tốt
     → = Chuyên gia đổi ngành → "chậm" dù IQ không đổi
     → ≈ KHÔNG can thiệp trực tiếp — chỉ tích lũy experience mới

  → IQ test đo TỔNG ①②③④ CÙNG LÚC → KHÔNG tách được ① riêng
  → "Không cần PFC tốt hơn — cần DÙNG PFC hiện có TỐT HƠN"
     bằng: chunks giàu (②) + cortisol thấp (③) + context match (④)

  Focus can thiệp: ②③ (giáo dục + cortisol management)
  vì ① không đổi + ④ khó can thiệp trực tiếp
```

---

## §3 — COMT: Clear Speed (Improviser vs Specialist)

```
① COMT (Catechol-O-Methyltransferase)
   🟢 CHÍNH — well-replicated

   COMT = enzyme phân hủy dopamine TẠI PFC (PFC-specific, không toàn não)

   Val/Val: enzyme NHANH → dopamine clear NHANH → PFC flexible, unstable
   Met/Met: enzyme CHẬM → dopamine tồn tại LÂU → PFC stable, less flexible

   🟢 Egan et al. 2001:
     fMRI khi làm WM tasks (Wisconsin Card Sort, N-back)
     Val/Val: PFC hiệu quả hơn khi SWITCH tasks
     Met/Met: PFC hiệu quả hơn khi MAINTAIN focus
     = 2 strategies, KHÔNG phải 1 giỏi 1 kém. Well-replicated.


SPECIALIST DRAFT MODE — COMT Met/Met (clear CHẬM):
  ┌──────────────────────────────────────────────────────┐
  │ Dopamine ở LÂU trong PFC                             │
  │ → Draft KHÔNG bị xóa nhanh                           │
  │ → WM GIỮ draft → sửa TRÊN NỀN draft cũ              │
  │                                                       │
  │ Quy trình:                                           │
  │   Draft v1: [A]-[B]-[C]-[D]                          │
  │   Sửa: xóa [C] → viết [C'] (liên quan A,B,D)       │
  │   Draft v2: [A]-[B]-[C']-[D]                         │
  │   → INCREMENTAL modification                         │
  │   → Mỗi phần mới BUỘC liên quan phần còn lại        │
  │   → = ĐÀO SÂU trong 1 hướng                         │
  │   → Mạnh: chính xác, nhất quán, deep                 │
  │   → Yếu: khó break khỏi hướng đã chọn               │
  └──────────────────────────────────────────────────────┘

IMPROVISER DRAFT MODE — COMT Val/Val (clear NHANH):
  ┌──────────────────────────────────────────────────────┐
  │ Dopamine bị CLEAR NHANH khỏi PFC                     │
  │ → Draft bị "xóa" trước khi sửa xong                 │
  │ → Workspace TRỐNG → sẵn sàng draft HOÀN TOÀN MỚI    │
  │                                                       │
  │ Quy trình:                                           │
  │   Draft v1: [A]-[B]-[C]-[D]                          │
  │   Clear: [ ]-[ ]-[ ]-[ ] (workspace trống)           │
  │   Input mới từ B+C → context mới                     │
  │   Draft v2: [X]-[Y]-[Z]-[W] (KHÁC HẲN v1)           │
  │   → FRESH rebuild từ input mới                        │
  │   → KHÔNG bị constrain bởi draft cũ                  │
  │   → = NHẢY sang hướng hoàn toàn khác                 │
  │   → Mạnh: cross-domain, creative, unexpected          │
  │   → Yếu: thiếu depth, inconsistent                   │
  └──────────────────────────────────────────────────────┘

  ⭐ KEY INSIGHT:
    Val/Val switch nhiều KHÔNG phải vì "muốn" switch
    → Mà vì draft CŨ MẤT → BUỘC phải build mới
    Met/Met ở lại KHÔNG phải vì "không muốn" switch
    → Mà vì draft CŨ CÒN → chưa có chỗ cho draft mới
    → = HARDWARE quản lý DRAFT, không phải "ý chí" quản lý behavior

  "Chán nhanh" = DRAFT CLEAR NHANH, không phải "lỗi" hay "thiếu reward"
    → ~15-20% dân số có hardware Val/Val → designed cho explore
    → ~60-70% có hardware Met/Met → designed cho maintain
    → CẢ HAI cần thiết cho xã hội
```


### §3.4 — COMT × Reward Pattern (v1.1 new — Drill R8)

```
🟡 COMT EXTEND: COGNITION → REWARD

  §3 phân tích COMT cho COGNITION (draft management).
  Drill R8 extends: COMT cũng ảnh hưởng REWARD patterns.

  PFC draft management → reward timing + depth:

  ┌──────────────────────┬──────────────────────────────────────────┐
  │ Val/Val (Improviser) │ Met/Met (Specialist)                      │
  ├──────────────────────┼──────────────────────────────────────────┤
  │ ② MANY shallow       │ ② FEWER but DEEPER insights              │
  │ insights → MANY      │ → FEWER but STRONGER rewards             │
  │ micro-rewards        │                                          │
  ├──────────────────────┼──────────────────────────────────────────┤
  │ Afterglow: SHORT     │ Afterglow: LONG                          │
  │ (draft clears →      │ (draft persists → re-derive →            │
  │  next topic)         │  additional opioid pulses)               │
  ├──────────────────────┼──────────────────────────────────────────┤
  │ Cross-domain ②:      │ Cross-domain ②: HARDER                   │
  │ NATURAL (workspace   │ (workspace occupied → new domain         │
  │  clears → new domain)│  blocked by existing draft)              │
  ├──────────────────────┼──────────────────────────────────────────┤
  │ Flow: HARDER to      │ Flow: EASIER to sustain                  │
  │ sustain (draft clears│ (draft persists → continuous             │
  │ during flow →        │  coherence stream)                       │
  │ interruption)        │                                          │
  ├──────────────────────┼──────────────────────────────────────────┤
  │ Compound: MORE VARIED│ Compound: LESS varied but DEEPER         │
  │ (many domains)       │ (same domain = deep stack)               │
  ├──────────────────────┼──────────────────────────────────────────┤
  │ Risk: "dopamine      │ Risk: "stuck in rut"                     │
  │ chasing" — jump to   │ (can't escape domain even when           │
  │ next novelty before  │  diminishing returns)                    │
  │ depth compiles       │                                          │
  └──────────────────────┴──────────────────────────────────────────┘

  Val/Met Heterozygous (~50% population):
    → Context-dependent switching → FLEXIBLE reward pattern.
    → Can flow AND explore depending on state.

  ⭐ KEY INSIGHT:
    "Improviser gets BORED not because reward is LOW — because DRAFT CLEARS
    before depth compiles. Specialist gets STUCK not because curiosity is
    LOW — because draft WON'T CLEAR for new domain."
    → ≠ personality trait → = HARDWARE managing DRAFTS differently

  → Chi tiết reward types: Reward-Signal-Architecture.md §4 (5 Profiles)
  🟡 COMT × Reward extension = inferred from COMT × Cognition, not directly tested.
  Source: Drill §3.22 ❸ (R8).
```


### §3.5 — COMT × Childhood Compilation (v1.1 new — Drill R8)

```
🟡 HARDWARE × CHILDHOOD = 4 REWARD TRAJECTORIES:

  COMT sets RANGE (how fast drafts clear).
  Childhood P5 tags set DIRECTION (approach vs avoidance).
  Combination → 4 distinct reward life trajectories:

  ┌────────────────────┬──────────────────────┬──────────────────────┐
  │ Combination        │ Reward Life          │ Implication          │
  ├────────────────────┼──────────────────────┼──────────────────────┤
  │ Met/Met + approach │ DEEP FLOW expert     │ Best case for ②      │
  │ childhood          │ (draft stays +       │ Sustainable decades  │
  │                    │ approach-tagged)      │                      │
  ├────────────────────┼──────────────────────┼──────────────────────┤
  │ Met/Met + avoidance│ RIGID ANXIETY        │ Draft stuck +        │
  │ childhood          │ (cannot escape +     │ threat-tagged =      │
  │                    │ threat-tagged domain)│ WORST combination    │
  ├────────────────────┼──────────────────────┼──────────────────────┤
  │ Val/Val + approach │ CREATIVE EXPLORER    │ Breadth + approach   │
  │ childhood          │ (jumps freely +      │ = versatile joy      │
  │                    │ approach-tagged)      │                      │
  ├────────────────────┼──────────────────────┼──────────────────────┤
  │ Val/Val + avoidance│ SCATTERED ANXIETY    │ Jump + avoid = chaos │
  │ childhood          │ (drafts clear +      │ Nothing feels safe   │
  │                    │ threat-tagged)        │ or deep enough       │
  └────────────────────┴──────────────────────┴──────────────────────┘

  ⭐ SAME hardware, DIFFERENT childhood = COMPLETELY DIFFERENT reward life.
  → Hardware sets RANGE. Childhood sets DIRECTION within range.
  → = "Nature sets the instrument. Nurture plays the tune."

  Implications:
    → Met/Met + avoidance = most urgently needs intervention
      (draft stuck ON threat-tagged chunks → cannot escape anxiety loop)
    → Val/Val + avoidance = chaotic but LESS stuck
      (drafts clear → can encounter new approach-tagged experiences)
    → Approach childhood = protective for BOTH COMT variants
    → Avoidance childhood = damaging for BOTH, worse for Met/Met

  → Chi tiết childhood P5 tags: Compile-Taxonomy.md §3, Reward-Signal-Architecture.md §8.4
  🟡 COMT × Childhood = framework synthesis, observational consistency.
  Source: Drill §3.22 ❺ (R8).
```

---

## §4 — DRD4: Chunk Threshold

```
③ DRD4 (Dopamine Receptor D4)
   ⚠️ FRAMEWORK KHÔNG SỬ DỤNG DRD4 LÀM CƠ CHẾ CHÍNH.
   Ghi lại để tham khảo và giải thích TẠI SAO KHÔNG DÙNG.


§4.1 DATA (đo đạc được — không thể bác bỏ) 🟢:

  → DRD4-7R receptor gắn dopamine YẾU HƠN 4R ở mức phân tử
    (Van Tol et al. 1992 — in vitro, measured) = FACT
  → Người mang DRD4-7R CÓ XU HƯỚNG score Novelty Seeking CAO hơn
    (Ebstein 1996 + một số studies sau) = OBSERVATION
    (dù effect nhỏ ~10% và replication không hoàn toàn consistent)


§4.2 INTERPRETATION CŨ (có lỗ hổng — framework KHÔNG dùng) ❌:

  Narrative phổ biến:
    "7R kém nhạy → ít sướng → phải novelty nhiều hơn để bù cho bằng"

  LỖ HỔNG LOGIC:
    Nếu 7R receptor kém nhạy dopamine:
      → Novelty CŨNG cho ÍT reward hơn (novelty dùng cùng dopamine system)
      → Gặp khó trong domain mới → reward ÍT → phải BỎ CUỘC sớm hơn?
      → Switch domain cần XÂY chunks nền → effort LỚN, reward NHỎ → tại sao chịu?
    Nếu 4R receptor nhạy hơn:
      → Novelty cho reward NHIỀU hơn → tại sao KHÔNG switch liên tục?
      → Scroll MXH = sướng hơn → phải NGHIỆN hơn?
    → Logic "kém nhạy → seek MORE" mâu thuẫn nội tại
    → COMT giải thích cùng behavior KHÔNG mâu thuẫn (§3)


§4.3 HYPOTHESIS D — Chunk Threshold (framework đề xuất) 🔴⭐:

  CƠ SỞ:
    Berridge (1998, 2003): dopamine ≠ reward, dopamine = signal
    → Dopamine KHÔNG gây sướng → chỉ THÔNG BÁO "chunk mới có giá trị"
    → Sướng thật = opioid = body-base response khi confirm chunk có giá trị

  MÔ HÌNH:
    ① B+C neurons fire liên tục → thử đồng bộ → patterns hình thành
    ② VTA detect ĐỒNG BỘ MẠNH BẤT THƯỜNG (vượt baseline)
    ③ VTA fire → dopamine → gắn DRD4 receptor TRÊN PFC neuron
    ④ DRD4-7R kém nhạy → DISTURBANCE THRESHOLD CAO:
       Biến động NHỎ = PFC THẬT SỰ KHÔNG BIẾT (receptor không mở)
       Chỉ biến động LỚN mới vượt → PFC nhận ÍT signal, mỗi signal = LỚN
    ⑤ DRD4-4R nhạy → THRESHOLD THẤP:
       Biến động NHỎ cũng vượt → PFC nhận NHIỀU signal
    ⑥ PFC spotlight xuống vùng có signal → body-base check
    ⑦ Kết quả:
       7R: ÍT detect → mỗi lần = chunk LỚN → body reward CAO → THÍCH novelty
       4R: NHIỀU detect → mỗi lần = chunk NHỎ → body reward NHỎ → ĐỦ với routine
       7R: "........ AHA!" (chờ lâu, 1 insight lớn)
       4R: "ồ... ồ... ồ..." (nhiều, nhỏ, liên tục)


§4.4 XÁC THỰC Hypothesis D — test với cases:

  Scroll MXH:
    7R: chunk nhỏ liên tục → KHÔNG vượt threshold → "chán, không hay" → DỪNG sớm
    4R: chunk nhỏ VƯỢT threshold → mỗi post = reward nhẹ → tiếp tục
    → ✅ 7R scroll ÍT, 4R scroll NHIỀU (ngược interpretation cũ)

  Cờ bạc:
    7R: near-miss = chunk lớn → body tưởng "GẦN THẮNG" → hook MẠNH
    4R: near-miss = chunk nhỏ → body "hmm" nhưng KHÔNG mạnh
    → ✅ 7R dễ bị hook near-miss (consistent gambling observation)

  Gặp vấn đề khó:
    7R: chờ chunk LỚN → NẾU chunks nền ĐỦ → "AHA!" → reward CỰC CAO
                       → NẾU chunks nền THIẾU → chờ mãi → frustrate → bỏ
    4R: chunk nhỏ liên tục → mỗi bước = reward → steady progress
    → ✅ 7R = breakthrough OR frustrate. 4R = incremental steady.

  → MỌI CASE consistent ✅. KHÔNG mâu thuẫn ở bất kỳ scenario nào.


§4.5 4 Hypotheses so sánh:

  Hypothesis A (PFC draft retention):
    ✅ Giải thích SWITCH behavior
    ❌ KHÔNG giải thích tại sao 7R THÍCH novelty (motivation)

  Hypothesis B (tonic vs phasic):
    ✅ Giải thích "ở yên = khó chịu"
    ❌ KHÔNG giải thích gambling near-miss hook

  Hypothesis C (gene linkage):
    ✅ Giải thích data inconsistency (GWAS không tìm DRD4 significant)
    ❌ KHÔNG giải thích mechanism gì cả

  Hypothesis D (chunk threshold) ⭐:
    ✅ SWITCH (7R bỏ qua chunk nhỏ → tìm chunk lớn)
    ✅ MOTIVATION (chunk lớn → reward lớn)
    ✅ GAMBLING (near-miss = chunk lớn → body tưởng thật)
    ✅ SCROLL (chunk nhỏ < threshold → chán nhanh)
    ✅ DEEP WORK (cần chunks nền + thời gian → AHA or frustrate)
    ✅ Dựa trên: Berridge (dopamine ≠ reward) = established
    ✅ Consistent với TẤT CẢ data đo được (Van Tol + Ebstein)

  → Framework prefer Hypothesis D
  → A có thể BỔ SUNG cho D (2 effects chồng lấp)


§4.6 Testable Predictions:

  Predict 1: 7R respond MẠNH HƠN 4R khi chunk LỚN
             7R respond YẾU HƠN 4R khi chunk NHỎ
             4R respond ĐỀU cho mọi size chunk

  Predict 2: Chất kích thích — 7R cần LIỀU CAO hơn 4R
             (threshold cao → cần dopamine signal MẠNH hơn)
             🟢 Có support nhẹ: ADHD medication — 7R carriers
                thường cần liều CAO hơn stimulant

  → Nếu predict đúng = confirm hypothesis
  → Nếu predict sai = cần revise
```


### §4.7 — DRD4 × Reward Profile (v1.1 new — Drill R8)

```
🔴 DRD4 HYPOTHESIS D × REWARD (extending §4.3):

  DRD4-7R = HIGH chunk threshold (detects LARGE chunks only).
  DRD4-4R = LOW chunk threshold (detects small chunks).

  Extension to REWARD patterns (IF Hypothesis D correct):

    7R: ② rewards RARE but INTENSE ("AHA!" type)
        Sensory: need STRONGER stimulus for same pleasure
        Flow: once IN flow MORE intense, getting INTO flow HARDER
        Domain: NEEDS deep chunk library → shallow domain = frustrate
        Risk: "can't find anything interesting" if domain wrong

    4R: ② rewards FREQUENT but MILD ("ồ..." — steady accumulation)
        Sensory: mild stimulus sufficient
        Flow: easier entry, less intense peak
        Domain: satisfies across breadth → less domain-dependent
        Risk: "content with surface" → may not develop depth

  ⚠️ DRD4 = Hypothesis D (framework 🔴), NOT established.
  BUT consistent with observed individual differences in reward intensity.
  AND: Type B reward = hardware-level → NOT affected by DRD4
    (B below VTA threshold system → "democratic reward").

  → Chi tiết Type A/B: Reward-Signal-Architecture.md §1
  Source: Drill §3.22 ❹ (R8).
```


### §4.8 — COMT × DRD4 Interaction (v1.1 new — Drill R8)

```
🔴 INTERACTION EFFECTS — WHY "TYPE" DESCRIPTIONS FAIL:

  Simple trait psychology: "extrovert = high reward sensitivity."
  Framework: reward sensitivity = 5-axis emergent →
  trait descriptions = LOSSY COMPRESSION.

  COMT × DRD4 → 4 COMPOUND REWARD PATTERNS:

  ┌────────────────────┬──────────────────────┬──────────────────────┐
  │ Combination        │ Reward Pattern       │ Popular Label        │
  ├────────────────────┼──────────────────────┼──────────────────────┤
  │ Val/Val + 7R       │ Clear fast + high    │ "Thrill seeker"      │
  │                    │ threshold = NEED     │ Jumps to big novel   │
  │                    │ novel BIG experiences│ experiences           │
  ├────────────────────┼──────────────────────┼──────────────────────┤
  │ Met/Met + 4R       │ Clear slow + low     │ "Obsessive expert"   │
  │                    │ threshold = SATISFY  │ Deep within single   │
  │                    │ within single domain │ domain               │
  ├────────────────────┼──────────────────────┼──────────────────────┤
  │ Val/Val + 4R       │ Clear fast + low     │ "Social butterfly"   │
  │                    │ threshold = many     │ Many small rewards   │
  │                    │ small rewards, none  │ from many domains    │
  │                    │ deep                 │                      │
  ├────────────────────┼──────────────────────┼──────────────────────┤
  │ Met/Met + 7R       │ Clear slow + high    │ "Frustrated genius   │
  │                    │ threshold = draft    │  or true genius"     │
  │                    │ stuck + needs BIG    │ BIMODAL: highest     │
  │                    │ chunks              │ genius OR highest    │
  │                    │                      │ frustration          │
  └────────────────────┴──────────────────────┴──────────────────────┘

  ⭐ Met/Met + 7R = MOST EXTREME BIMODAL:
    → IF domain right + deep chunks: draft persists + big threshold met
      = DEEPEST flow, most intense ②, most productive
    → IF domain wrong + shallow: draft stuck + threshold never met
      = HIGHEST frustration, most miserable

  → = "Tài năng" hay "khổ sở" = SAME hardware, khác DOMAIN FIT
  → = Counseling implication: Met/Met + 7R NEEDS right domain most urgently

  ⚠️ COMT × DRD4 interaction = framework reasoning, NOT tested.
  ⚠️ DRD4 = Hypothesis D (🔴). COMT × DRD4 = 🔴 × 🔴 = highly speculative.
  ⚠️ "Popular labels" = ILLUSTRATIVE, not clinical categories.
  Source: Drill §3.22 ❺ (R8).
```

---

## §5 — MAO-A: Mood Stability (Toàn Não)

```
② MAO-A (Monoamine Oxidase A)
   🟢 BỔ SUNG — replicated

   MAO-A = enzyme phân hủy dopamine + serotonin TOÀN NÃO
   (khác COMT chỉ PFC-specific)

   LOW activity: dopamine + serotonin TỒN TẠI LÂU → mood STABLE
   HIGH activity: dopamine + serotonin CLEAR NHANH → mood SHIFTS

   🟢 Research: Shih et al. 1999

   KHÁC COMT Ở SCOPE:
     COMT = clear dopamine trong PFC (local, PFC-specific)
     MAO-A = clear dopamine + serotonin TOÀN NÃO (global)
     → 2 "nút chỉnh" KHÁC NHAU:
       COMT = PFC draft management (improviser/specialist)
       MAO-A = mood + energy overall (stable/volatile)

   Combinations:
     COMT nhanh + MAO-A chậm = improviser PFC + stable mood
     COMT chậm + MAO-A nhanh = specialist PFC + mood dao động

   CƠ CHẾ TÓM GỌN:
     IMPROVISER vs SPECIALIST = chủ yếu do COMT (PFC clear speed):
     → Cùng dopamine release → enzyme KHÁC → DURATION draft khác → behavior KHÁC
     → = Hardware quản lý DRAFT, không phải hardware quản lý REWARD

     KHÔNG phải:
       ❌ "Hormone biến động NHANH hơn" (fluctuation speed ≈ giống nhau)
       ❌ "Sướng ít hơn" (liking/opioid có thể giống nhau)
       ❌ "Cần nhiều dopamine" (narrative DRD4 có lỗ hổng logic)

     MÀ LÀ:
       ✅ Draft bị XÓA nhanh hay GIỮ lâu trong PFC workspace
       ✅ = Vấn đề DRAFT MANAGEMENT, không phải REWARD SENSITIVITY

   DISTRIBUTION ƯỚC LƯỢNG (đơn giản, không dùng DRD4):
     COMT Val/Val + MAO-A high: ~15-20% (improviser, switch nhanh)
     COMT Met/Met + MAO-A low:  ~60-70% (specialist, deep focus)
     Mixed:                     ~15-20% (T-shaped, context-dependent)
```

---

## §6 — NE α2/α1: PFC Circuit Breaker

```
NOREPINEPHRINE (NE) — TỪ LOCUS COERULEUS (LC):

  LC = nhóm nhỏ neurons ở THÂN NÃO (C zone — brainstem)
  → Hoạt động VÔ THỨC — PFC KHÔNG kiểm soát LC
  → LC nhận input từ: amygdala (threat), hypothalamus (arousal), body state
  → LC release NE → broadcast TOÀN NÃO (nhưng PFC đặc biệt nhạy)


NE có 2 LOẠI receptor TRÊN PFC:

  ┌──────────────┬──────────────────────────┬──────────────────────────┐
  │              │ α2 RECEPTORS             │ α1 RECEPTORS             │
  ├──────────────┼──────────────────────────┼──────────────────────────┤
  │ Affinity     │ CAO (bật ở NE thấp-vừa) │ THẤP (chỉ bật ở NE cao) │
  ├──────────────┼──────────────────────────┼──────────────────────────┤
  │ Khi active   │ TĂNG CƯỜNG PFC networks  │ DISCONNECT PFC networks  │
  │              │ → WM rõ, attention sharp │ → WM MẤT, PFC OFFLINE   │
  ├──────────────┼──────────────────────────┼──────────────────────────┤
  │ Khi nào      │ Bình thường, focused     │ Acute stress, emergency  │
  ├──────────────┼──────────────────────────┼──────────────────────────┤
  │ Verbal       │ "Tập trung, sáng suốt"  │ "Hoảng, rối, ko nghĩ đc"│
  └──────────────┴──────────────────────────┴──────────────────────────┘

  = CÙNG 1 hóa chất (NE), KHÁC receptor (α2 vs α1), NGƯỢC hiệu ứng
  = Yerkes-Dodson ở MỨC RECEPTOR


CHUỖI ACUTE THREAT (milliseconds):

  1. Amygdala detect threat (via "low road" — LeDoux 1996)
     → Sensory thalamus → Amygdala TRỰC TIẾP (bypass cortex)
     → ~12ms — TRƯỚC KHI PFC biết chuyện gì xảy ra

  2. Amygdala → signal LC → NE FLOOD

  3. NE cao → α1 receptors trên PFC KÍCH HOẠT
     → PFC network connections DISCONNECT
     → PFC OFFLINE (không phải "bận" — bị CẮT KẾT NỐI)

  4. ĐỒNG THỜI NE cao TĂNG CƯỜNG:
     → Amygdala (C zone — threat response mạnh hơn)
     → Basal ganglia (C zone — compiled responses sẵn sàng)
     → = Não CHUYỂN QUYỀN: A(PFC) → C(subcortical)

  5. Body respond: fight / flight / freeze (compiled, VÔ THỨC)
     → KHÔNG QUA PFC — vì PFC đã offline

  6. Threat pass → NE GIẢM dần
     → α1 deactivate → PFC reconnect → online lại
     → PFC evaluate SAU: "chuyện gì vừa xảy ra?"

  TOÀN BỘ chuỗi 1-5 = DESIGN FEATURE, không phải lỗi.
  → Recovery: seconds → PFC online lại.
  → ≠ cortisol damage (tuần-tháng, DAMAGE thật).
  → Chi tiết NE vs cortisol: Core-v7.8-Draft.md §4.3


INSIGHT CỐT LÕI:
  → PFC có α1 receptors = "circuit breaker" CÀI SẴN trên chính nó
  → Body (qua LC) có thể SHUTDOWN PFC bất kỳ lúc nào
  → PFC KHÔNG THỂ ngăn shutdown này (α1 = hardware level)
  → = PFC KHÔNG PHẢI "boss" — là TOOL mà body có thể TẮT

  Evolution logic:
    Emergency KHÔNG CẦN deliberation (PFC chậm, ~200ms+)
    Emergency CẦN compiled response (C subcortical nhanh, ~12ms)
    → α1 = evolutionary "circuit breaker" — 500 triệu năm optimization


🟢 GRADIENT THREAT DISTANCE (Mobbs et al. 2007):
  fMRI: virtual predator đuổi subjects:
    Threat XA: vmPFC ACTIVE (planning, strategy)
    Threat GẦN: vmPFC DEACTIVATED → PAG activated (panic, reflex)
    = GRADIENT, không phải switch ON/OFF
    = Càng gần nguy hiểm → PFC càng bị tắt → subcortical càng mạnh


PTSD IMPLICATION:
  → NE baseline CAO MÃN TÍNH (PTSD characteristic)
  → α1 active THƯỜNG XUYÊN → PFC impaired CHRONIC
  → "Không nghĩ được rõ" = PFC bị disconnect TRIỀN MIÊN
  → Không phải "yếu đuối" — là HARDWARE bị compromised
  → Treatment: giảm NE baseline → α1 deactivate → PFC reconnect
  → 🟢 PTSD + NE dysregulation = established (Southwick 1999)
```

🟢 Research: Arnsten 2009, 2015; LeDoux 1996; Mobbs 2007; Ramos & Arnsten 2007; Southwick 1999

---

## §7 — VTA Detection Loop (7 Bước)

```
🟡 HYPOTHESIS — logic consistent với research, chưa ai xác thực toàn bộ chain.
   Mỗi bước = established riêng lẻ. GOM LẠI thành flow = framework contribution.


BƯỚC 1 — B+C NEURONS FIRE LIÊN TỤC (24/7, kể cả ngủ):
  86 tỷ neurons fire → signal lan qua ~7000 neighbors mỗi neuron
  → Neurons THỬ đồng bộ → phần lớn FAIL → tan
  → Một số THÀNH → pattern hình thành = chunk
  → KHÔNG ai điều khiển — self-organizing

  ⭐ CORTISOL = CALIBRATION ENERGY:
  → Cortisol tăng → neurons fire MẠNH HƠN (arousal)
  → Chunks đang compiled bị RUNG LẮC → THỬ patterns MỚI
  → = Cortisol phục vụ B+C calibration, PFC là bên PHỤ được thông báo


BƯỚC 2 — VTA DETECT BIẾN ĐỘNG (delta, không absolute):
  VTA (~400,000 neurons, giữa não — C zone):
  → Vùng X fire ổn định → VTA QUEN → lờ đi
  → Vùng X bỗng fire KHÁC → VTA detect: "BIẾN ĐỘNG!" → fire
  → = VTA detect DELTA (thay đổi), không ABSOLUTE
  → Schema cũ compiled fire MẠNH nhưng ĐỀU → VTA quen → im
  → Pattern mới fire YẾU nhưng KHÁC → VTA detect → fire

  ⭐ KHÔNG CẦN "predict → compare → error" phức tạp (Schultz 1997)
  → CHỈ CẦN: "quen → khác quen → fire" (habituation + delta)
  → = Simpler mechanism, CÙNG observable result

  VTA fire → dopamine → broadcast: PFC, Nucleus Accumbens, Hippocampus


BƯỚC 3 — RECEPTOR FILTER (DRD4):
  Dopamine trong khe synapse → gắn DRD4 receptor trên PFC neuron
  → 7R (kém nhạy): cần NHIỀU dopamine → chỉ detect biến động LỚN
  → 4R (nhạy): ít dopamine cũng đủ → detect cả biến động NHỎ
  → PFC KHÔNG "chọn bỏ qua" — 7R THẬT SỰ KHÔNG BIẾT chunk nhỏ tồn tại
  → = HARDWARE filter, không SOFTWARE choice


BƯỚC 4 — PFC SPOTLIGHT (top-down):
  PFC neuron fire → gửi XUỐNG B cortical areas:
  → Boost NE + Acetylcholine tại vùng target
  → Neurons vùng target fire MẠNH HƠN = "spotlight"
  → PFC KHÔNG "bảo" B tính gì — chỉ TĂNG ÂM LƯỢNG
  → Spreading activation: boost vùng A → neighbors fire → chunks LIÊN QUAN

  Bất đối xứng:
    Lên: B+C → VTA (trung gian) → dopamine → PFC (indirect)
    Xuống: PFC → TRỰC TIẾP → B target (no middleman)

  🟢 Desimone & Duncan 1995, Miller & Cohen 2001


BƯỚC 5 — BODY-BASE CHECK:
  PFC nhận chunk → integrate vào workspace
  → Gửi xuống body-base: "giả lập → body feel gì?"
  → Chunk KHỚP body-need → opioid release → reward THẬT
  → Chunk KHÔNG khớp → body "meh" → discard
  → Dopamine = signal "có biến động" (chuông cửa)
  → Opioid = reward "có giá trị thật" (quà đằng sau cửa)


BƯỚC 6 — REINFORCE + LOOP:
  Body reward (opioid) → vùng đó REINFORCE:
  → Neurons fire MẠNH + kết nối CHẶT → pattern MỚI ỔN ĐỊNH
  → VTA habituate → PFC giảm attention
  → TRÊN NỀN ổn định mới → B+C THỬ TIẾP
  → Biến động MỚI → VTA detect → dopamine → PFC → body check → loop

  SAU NHIỀU VÒNG:
  → Pattern thô → nhiều vòng body check → tinh chỉnh
  → = Schema chất lượng cao = nhiều vòng body-check
  → = "Cùng nhạc cụ, cùng energy → melody đã khác"


BƯỚC 7 — DỌN DẸP (COMT clear):
  Dopamine trong khe synapse KHÔNG ở mãi:
    COMT enzyme (PFC-specific): Val/Val dọn NHANH, Met/Met dọn CHẬM
    DAT transporter (striatum-specific): PFC ÍT DAT → COMT là chính
  → Sau dọn: khe synapse SẠCH → sẵn sàng signal MỚI


TÓM GỌN VÒNG LẶP:
  ① B+C: neurons tự fire + tự đồng bộ → patterns hình thành
  ② VTA: detect BIẾN ĐỘNG (habituation) → fire → dopamine → PFC
  ③ Receptor: 4R nhận biến động nhỏ / 7R chỉ nhận lớn (HARDWARE filter)
  ④ PFC: spotlight XUỐNG B target → boost → B respond RÕ
  ⑤ Body-base: check chunk → reward (opioid) nếu khớp body-need
  ⑥ Reinforce: reward → pattern mạnh → ổn định → B+C thử tiếp → LOOP
  ⑦ COMT: dọn dopamine → clear speed → ảnh hưởng draft duration

  = Bottom-up (dopamine signal) ↔ Top-down (PFC spotlight)
  = KHÔNG AI điều khiển toàn bộ = self-organizing network
```

---

## §8 — 4 Receptor Systems Summary

```
  ┌──────────┬──────────────────┬──────────────────┬──────────────┐
  │ Receptor │ Hóa chất         │ Ảnh hưởng PFC    │ Timeframe    │
  ├──────────┼──────────────────┼──────────────────┼──────────────┤
  │ DRD4     │ Dopamine (VTA)   │ Chunk THRESHOLD  │ Per-event    │
  │          │                  │ "biến động nào   │ (ms)         │
  │          │                  │ đủ lớn để báo?"  │              │
  ├──────────┼──────────────────┼──────────────────┼──────────────┤
  │ COMT     │ Dopamine (PFC)   │ CLEAR SPEED      │ Per-draft    │
  │          │                  │ "draft ở bao lâu │ (seconds)    │
  │          │                  │ trước khi xóa?"  │              │
  ├──────────┼──────────────────┼──────────────────┼──────────────┤
  │ α2       │ NE (LC)          │ ENHANCE PFC      │ Continuous   │
  │          │                  │ "sharp, focused" │ (khi NE vừa) │
  ├──────────┼──────────────────┼──────────────────┼──────────────┤
  │ α1       │ NE (LC)          │ DISCONNECT PFC   │ Emergency    │
  │          │                  │ "offline, reflex"│ (ms, acute)  │
  └──────────┴──────────────────┴──────────────────┴──────────────┘

  = 4 receptor systems → 4 cách hardware ảnh hưởng PFC
  = MỖI người có VARIANT KHÁC NHAU ở mỗi receptor
  = "PFC profile" = tổ hợp DRD4 × COMT × α2/α1 sensitivity × PFC-Quality
```


### §8b — 4 Receptor Systems × 5 Reward Profiles (v1.1 new — Drill R8)

```
🟡 HARDWARE ẢNH HƯỞNG REWARD PROFILES KHÁC NHAU:

  §8 shows 4 receptor systems × PFC function (cognition).
  §8b extends: 4 systems + μ-opioid × 5 REWARD profiles:

  ┌──────────────┬──────────────┬──────────────┬──────────────┬─────────────┐
  │ Receptor     │ ① Sensory    │ ② Coherence  │ ③ Social     │ ④ Relief    │
  │ System       │   Reward     │   Reward     │   Reward     │   Reward    │
  ├──────────────┼──────────────┼──────────────┼──────────────┼─────────────┤
  │ COMT         │ Low impact   │ HIGH: clear  │ Moderate     │ Low impact  │
  │ (PFC clear   │ (sensory =   │ speed → ②    │ (social eval │ (cortisol   │
  │  speed)      │ below PFC)   │ develop speed│ = PFC-partly)│ system)     │
  ├──────────────┼──────────────┼──────────────┼──────────────┼─────────────┤
  │ DRD4         │ Low impact   │ HIGH: chunk  │ Moderate     │ Low impact  │
  │ (Hypothesis  │ (sensory not │ threshold →  │ (social cues │ (not VTA-   │
  │  D threshold)│ VTA-gated)   │ "AHA" vs "ồ" │ = VTA delta) │ gated)      │
  ├──────────────┼──────────────┼──────────────┼──────────────┼─────────────┤
  │ MAO-A        │ Moderate     │ Moderate     │ HIGH: mood   │ HIGH: base  │
  │ (mood global │ (sensory     │ (sustained   │ stability →  │ cortisol ↔  │
  │  stability)  │ valence)     │ affect mood) │ social resil.│ relief mag. │
  ├──────────────┼──────────────┼──────────────┼──────────────┼─────────────┤
  │ NE α2/α1     │ Low impact   │ HIGH: PFC    │ HIGH: threat │ HIGH: NE ↔  │
  │ (circuit     │              │ stability →  │ assessment → │ cortisol →  │
  │  breaker)    │              │ flow access  │ social threat│ relief sens.│
  ├──────────────┼──────────────┼──────────────┼──────────────┼─────────────┤
  │ μ-Opioid     │ HIGHEST      │ HIGH         │ HIGH         │ Moderate    │
  │ receptor     │ (A₀-A₃ all   │ (coherence   │ (social bond │ (relief =   │
  │ density      │ opioid)      │ → opioid)    │ opioid-aided)│ cortisol    │
  │              │              │              │              │ primarily)  │
  └──────────────┴──────────────┴──────────────┴──────────────┴─────────────┘

  ⭐ TYPE B (touch, warmth, exercise) = LESS affected by ALL receptor systems:
    → B = non-opioid, non-PFC, hardware-level pathways
    → B reward = MORE EGALITARIAN across individuals
    → Hardware individual differences = primarily TYPE A variation
    → B = evolution's EQUALIZER ("democratic reward")

  → Type A: μ-opioid density + COMT + DRD4 → HIGHLY variable
  → Type B: CT afferent density varies LESS across individuals
  → = WHY body-based reward (touch, exercise) is "democratic"

  ⚠️ μ-opioid receptor density = 🟡 consistent with pharmacological
  literature but individual variation poorly mapped.
  ⚠️ Table = framework synthesis, NOT established receptor-by-profile mapping.
  Source: Drill §3.22 ❷ (R8).
```


### §8c — 3-Variable Shorthand (v1.1 new — Drill R8)

```
🟡 PRACTICAL DESCRIPTION — 3-Variable Profile:

  Full model (5 profiles × 5 axes = 25 cells) = too complex for daily use.
  COMPRESSED DESCRIPTION uses 3 variables:

  ┌──────────────────────────────────────────────────────────┐
  │ ① A/B Ratio:   Where on Type A ↔ Type B spectrum        │
  │ ② Dom. Profile: Which of 5 profiles (①②③④⑤) STRONGEST  │
  │ ③ Breadth:      How many profiles ACTIVE (narrow ↔ broad)│
  └──────────────────────────────────────────────────────────┘

  EXAMPLES (illustrative, NOT measured):

    Nhà vật lý: High A (90/10), Dominant ②, Moderate breadth (②+③+④)
      → Intense coherence seeker, some social/relief, very little B

    Đầu bếp: Balanced A/B (60/40), Dominant ①, Narrow (①+④)
      → Sensory-driven, relief from completion, significant body reward

    Nhà trị liệu: Moderate A (55/45), Dominant ③, Broad (①②③④⑤)
      → Social reward primary, accesses ALL profiles

    Vận động viên: Low A (30/70), Dominant B+④, Narrow
      → Body-driven, relief from exertion, minimal coherence/social

  → "Personality" re: reward = this 3-variable profile
  → Simple "extrovert/introvert" = LOSSY COMPRESSION of 3 variables
  → = Framework alternative to trait psychology for reward description

  ⚠️ Cannot MEASURE precisely yet — organizing framework.
  ⚠️ Illustrative examples = framework reasoning, not clinical data.
  → Chi tiết reward profiles: Reward-Signal-Architecture.md §4
  → Chi tiết 5-axis model: Reward-Signal-Architecture.md §8.5
  Source: Drill §3.22 ❽ (R8).
```

---

## §9 — Honest Assessment

```
🟢 ESTABLISHED:
  WM ~4±1 items (Cowan 2001)
  COMT Val/Met effects on PFC (Egan 2001, well-replicated)
  DRD4-7R binding affinity thấp hơn 4R (Van Tol 1992)
  NE α2/α1 dual effect on PFC (Arnsten 2009, 2015)
  Amygdala low road ~12ms (LeDoux 1996)
  Threat gradient PFC→PAG (Mobbs 2007)
  Dopamine ≠ reward (Berridge 1998, 2003)
  VTA detect novelty/surprise (Schultz 1997)
  Top-down attention PFC→cortex (Desimone & Duncan 1995)
  Neural efficiency: giỏi fire ÍT (Haier 1992, Neubauer & Fink 2009)
  Brain size vs IQ: ~6% variance (Pietschnig 2015)
  PTSD + NE dysregulation (Southwick 1999)

🟡 FRAMEWORK SYNTHESIS:
  2-parameter model (Quality + Clear Speed) — novel organization
  Observed Capacity = 4-factor formula — novel, components established
  "Improviser/Specialist = COMT draft management" — novel framing
  VTA = delta detector (habituation) — prediction delta, không phải "prediction error" calculator
  PFC spotlight = tăng volume, không ra lệnh tính toán
  7-step VTA detection loop — novel integration
  COMT × Reward pattern (§3.4) — extension from cognition to reward domain (v1.1)
  COMT × Childhood trajectories (§3.5) — 4 combos, framework synthesis (v1.1)
  4 Receptor Systems × 5 Profiles (§8b) — cross-mapping, not established (v1.1)
  3-Variable Shorthand (§8c) — practical but lossy compression (v1.1)
  Type B "democratic reward" — less hardware-variable (v1.1)

🔴 NEEDS MORE RESEARCH:
  DRD4 Hypothesis D (chunk threshold) — testable, chưa ai test
  DRD4 Hypothesis A vs B vs C vs D — chưa settled
  MAO-A × COMT interaction — limited data
  Individual α2/α1 sensitivity variance — not well characterized
  Quantitative: bao nhiêu chunk size = vượt 7R threshold?
  COMT × DRD4 interaction patterns (§4.8) — framework 🔴×🔴, highly speculative (v1.1)
  DRD4 × Reward profiles (§4.7) — depends on Hypothesis D validity (v1.1)
  μ-opioid individual density variation — poorly mapped (v1.1)

🔴 TESTABLE PREDICTIONS (v1.1):
  P-R8a: COMT Val/Val → shorter flow, more domain-switches
    → Met/Met → longer flow, fewer domain switches
  P-R8b: Type B reward sensitivity has LOWER individual variance than Type A
    → B SD < A SD (B = hardware, A = compilation-dependent)
  P-R8d: Met/Met + 7R = HIGHEST variance in life satisfaction
    → BIMODAL: very high (right domain) OR very low (wrong domain)
```

---

## §10 — Cross-References

```
PFC FOLDER:
  PFC-Function.md v1.1 — 24 observable functions
  PFC-Configuration.md v1.0 — 6 dynamic modes, survival matrix (v1.1 NEW)
  PFC-Development.md — life stages + training
  PFC-Hold-Dimensions.md — tại sao ~4±1

PHYSICAL MAP:
  Neural-Architecture.md §2 — sub-regions, connectivity

REWARD (v1.1 NEW):
  Reward-Signal-Architecture.md v1.0 — Type A/B, 5 Profiles, A₀→A₃
    → §3.4 COMT×Reward maps to RSA §4 (profiles)
    → §8b Receptor×Profiles maps to RSA §8.5 (individual differences)
  03-Reward.md — H10 preconditions, 7-step VTA
  Dopamine-Reward-Rejection.md — Berridge, wanting ≠ liking
  Liking-Wanting.md — wanting × liking mechanisms

COMPILATION (v1.1 NEW):
  Compile-Taxonomy.md v1.0 §3 — 4 pathways → 4 P5 tag types
    → §3.5 COMT×Childhood maps to 4-Pathway × P5 Tag Model

BODY SYSTEMS:
  Cortisol-Baseline.md v2.0 — cortisol affects PFC function
  Body-Feedback.md — body signals + H10

CORE:
  Core-v7.8-Draft.md §6 — PFC trong cycle architecture
  Chunk.md v2.0 — chunks PFC operates on

DRILL SOURCE (v1.1):
  Drill-Reward-Feeling-Main.md v1.2 §3.22 (R8) — Individual Differences

OLD FILE (backup):
  PFC/Imagination/backup/PFC-Analysis-v1.1.md §8 — source content
```

---

> **PFC-Hardware.md v1.1**
>
> 4 receptor systems: DRD4 (threshold), COMT (clear speed), α2 (enhance), α1 (disconnect).
> PFC-Quality = resolution × filter × retrieval × compression (per-slot).
> Observed Capacity = Hardware × Chunks × Cortisol × Context.
> Improviser vs Specialist = COMT draft management, không phải reward sensitivity.
> v1.1: COMT×Reward, COMT×Childhood, DRD4×Reward, COMT×DRD4 interaction,
>   4 Receptors × 5 Profiles, 3-Variable Shorthand, Type B "democratic reward."
>
> Phiên bản: v1.1, 2026-05-10.
