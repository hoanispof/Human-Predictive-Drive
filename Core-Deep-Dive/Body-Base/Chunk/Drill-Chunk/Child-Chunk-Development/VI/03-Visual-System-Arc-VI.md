---
title: 03 — Visual System Developmental Arc — F1 Body-Input Arc #1
file: 03-Visual-System-Arc-VI.md
source: 03-Visual-System-Arc.md (bản gốc tiếng Anh)
created: 2026-04-15 (Session N+4b, Phase F1-P6)
status: DRAFT N+4b P6 — đang dịch Phase A
scope: Tiếp nhận đầu vào thị giác + kiểm soát mắt-motor + cơ chế compile chunks thị giác từ khi sinh đến ~24 tháng, phân tích qua các giai đoạn Connect → Read → Control với PFC-Inference Ladder
parent: plan.md §3.2 (file 03 outline)
depends_on: [01-PFC-Hardware-Reframe.md, 02-Womb-to-Birth-Baseline.md]
language: Tiếng Việt primary + English technical terms
addresses:
  - Nút Thắt 1 (proto-chunk gradient — object file emergence như test case)
  - Nút Thắt 3 (multi-modal binding — thành phần thị giác)
sub_folder: F1 Child-Chunk-Development
translation_note: Bản dịch tiếng Việt hoàn chỉnh. Giữ nguyên thuật ngữ kỹ thuật tiếng Anh, citation, tên file, parameter, emoji. Xưng hô bạn-tôi.
---

# 03 — Visual System Developmental Arc

> **File 03 trong F1 Child-Chunk-Development sub-folder.** Đây là file arc body-input đầu tiên trong sáu file (thị giác, thính giác, motor, interoceptive, xã hội, verbal). File này truy dấu cơ chế compile chunks hệ thống thị giác từ khi sinh đến ~24 tháng qua **các giai đoạn Connect → Read → Control**, phân loại các sự kiện quan sát được với **PFC-Inference Ladder** (plan §0.7) và áp dụng **quy tắc phương pháp luận event-inference** từ [01-PFC-Hardware-Reframe.md](01-PFC-Hardware-Reframe.md) §6.

---

## §0 — Tóm Tắt

🟢🟡 **Claim**: Chunks thị giác compile qua 0-24 tháng theo quỹ đạo gradient bắt đầu từ trạng thái khởi đầu trước sinh thưa thớt (CONSPEC face template bẩm sinh, không có learned object/person chunks) và đạt đến các identity chunks được bind multi-modal phong phú vào ~18-24 tháng. Quỹ đạo này **không phải là câu chuyện trưởng thành PFC** — PFC hardware đã online từ khi sinh theo [01-PFC-Hardware-Reframe.md](01-PFC-Hardware-Reframe.md) §3 — mà là **câu chuyện tích lũy chunks** với các sự kiện quan sát được ở các cấp PFC-Inference Ladder ngày càng cao hơn.

Hệ thống thị giác được phân tích theo ba giai đoạn:

- **Connect** (§2): sẵn sàng hardware cho đầu vào thị giác — võng mạc, V1-V5, đường dẫn thị giác, phát triển acuity và màu sắc.
- **Read** (§3): chunks phát hiện đầu vào — face templates, phát hiện direct gaze, nhận dạng khuôn mặt mẹ, object file, object permanence, feature integration.
- **Control** (§4): chunks đầu ra — smooth pursuit, với tay được hướng dẫn bằng thị giác, theo dõi ánh mắt, joint attention, theo dõi vật thể qua che khuất.

Các sự kiện được phân tích với PFC-Inference Ladder:

| Sự kiện | Tuổi | Ladder | Nghiên cứu |
|---|---|---|---|
| Face preference | Khi sinh (2-5 ngày) | L0-L2 | Fantz 1961, Morton & Johnson 1991 |
| Direct gaze preference | 2-5 ngày | L2 🟡 | Farroni et al. 2002 |
| Social smile (multi-modal) | 6-8 tuần | L2-L3 🟢 | Feel-Example E12 |
| Mother face recognition | 5 tháng | L2-L3 🟢 | Feel-Example E15 |
| Gaze following | 6 tháng | L3 🟢 | Feel-Example E14, Tomasello |
| Object permanence VoE | 4-6 tháng | L2 🟢 | Baillargeon 1987, 1991 |
| Joint attention (triadic) | 9-12 tháng | L4 🟢 | Feel-Example E18, Tomasello 1995 |
| Mirror self-recognition | 18-24 tháng | L4 🟡 | Amsterdam 1972 |

**Hai Nút Thắt được đề cập**:

1. **Nút Thắt 1** — object file emergence (§3.8 + §5) cung cấp một trong các test case của hệ thống thị giác cho proto-chunk gradient vs discrete verdict.
2. **Nút Thắt 3** — thành phần thị giác của multi-modal binding (§6) bao gồm phía thị giác của cơ chế bind social smile E12 / mother recognition E15 / joint attention E18. Verdict đầy đủ được deferred đến [07-Social-Recognition-Arc.md](07-Social-Recognition-Arc.md) §6.

**File này KHÔNG claim gì** (theo quy tắc phương pháp luận §6):

- ❌ "PFC trưởng thành ở tuổi X cho task thị giác Y"
- ❌ "Vùng vỏ não thị giác thức dậy ở tuổi X"
- ❌ Các claim đo lường PFC trực tiếp cho bất kỳ sự kiện thị giác nào

**File này THỰC SỰ claim**:

- ✅ Sự kiện X có thể quan sát được ở tuổi Y theo citation nghiên cứu
- ✅ Sự kiện X có thể yêu cầu chunks A, B, C đã compile (suy luận framework 🟡)
- ✅ Phân loại Ladder cho mỗi sự kiện với qualifier khả năng
- ✅ Baseline state tại t=0 từ [02-Womb-to-Birth-Baseline.md](02-Womb-to-Birth-Baseline.md) §9.1 như điểm khởi đầu

---

## §1 — Vị Trí Trong F1

### §1.1 — Một trong sáu body-input arcs

F1 v3 plan (§0.3 Q7 body-input axis) tổ chức phân tích phát triển theo sáu hệ thống body-input:

```
1. Visual      (mắt)        ← FILE NÀY
2. Auditory    (tai)        ← 04-Auditory-System-Arc.md
3. Motor       (tay/chân)   ← 05-Motor-Output-Arc.md
4. Interoceptive (cơ thể)  ← 06a-Interoceptive-Bladder-Keystone.md + 06b
5. Social      (đa kênh)    ← 07-Social-Recognition-Arc.md
6. Verbal      (ngôn ngữ)   ← 08-Verbal-Production-Arc.md
```

Visual là hệ thống **được nghiên cứu chuyên sâu nhất trong tâm lý phát triển** — paradigm face preference Fantz 1961, paradigm VoE Baillargeon, các nghiên cứu joint attention của Tomasello, mirror test Amsterdam đều có hàng thập kỷ tái lập và xác nhận xuyên văn hóa. Điều này làm cho visual trở thành **nền tảng thực nghiệm phong phú nhất** để áp dụng phương pháp luận event-inference.

### §1.2 — Tại sao visual mang tính hướng dẫn cho chunk substrate

Ba lý do arc thị giác đặc biệt mang tính hướng dẫn cho câu hỏi trung tâm của F1 (chunks compile như thế nào):

1. **Gradient emergence hiển thị qua nhiều sự kiện**: face preference → direct gaze → mother recognition → joint attention là quỹ đạo tích lũy chunks rõ ràng qua 0-12 tháng. Mỗi bước đều có markers có thể quan sát. Ít hệ thống body-input nào có nhiều milestones rời rạc như vậy trong một cửa sổ ngắn như vậy.

2. **Binding multi-modal phong phú**: Chunks thị giác bind với thính giác (social smile E12 = khuôn mặt + giọng), với interoceptive (mother recognition E15 = khuôn mặt + lịch sử thoải mái), với motor (với tay, theo dõi ánh mắt). Visual là **hub trung tâm cho multi-modal binding sớm** — chạm đến Nút Thắt 3 ở nhiều góc độ.

3. **Object file emergence test proto-chunk gradient**: câu hỏi "đó là một chunk hay gradient?" (Nút Thắt 1) có một test case sạch trong object file formation giữa 4-6 tháng. Về mặt hành vi, trẻ sơ sinh thể hiện các trạng thái trung gian (theo dõi một phần, nhận dạng một phần, permanence một phần) — không phải các công tắc rời rạc "object chunk có mặt / vắng mặt".

### §1.3 — Dependencies với 01 + 02

File này phụ thuộc vào hai file nền tảng từ drill N+4a:

**Từ [01-PFC-Hardware-Reframe.md](01-PFC-Hardware-Reframe.md)**:
- §3 5 evidence pillars thiết lập PFC hardware online từ khi sinh (không phải timeline claim)
- §6 quy tắc phương pháp luận event-inference (template được dùng xuyên suốt §5 của file này)
- §7.2 worked example "tên mẹ" (Mandel 4.5 tháng) — logic song song áp dụng cho nhận dạng khuôn mặt mẹ bằng thị giác ở cùng độ tuổi

**Từ [02-Womb-to-Birth-Baseline.md](02-Womb-to-Birth-Baseline.md)**:
- §9.1 F1 baseline state tại t=0 — điểm khởi đầu thị giác khi sinh là: CONSPEC face template ✅, không có learned face chunks ❌, không có object chunks ❌, acuity ~20/400
- §4 thư viện prenatal chunks — phía thị giác của thư viện về cơ bản trống rỗng (tử cung tối, vỏ não thị giác hoạt động nhưng không có đầu vào theo pattern)
- §7.4 Q&A thị giác trẻ sơ sinh — direct gaze preference 2-5 ngày là sự kiện L2 thị giác sớm nhất

Hai file này cung cấp các đường ray framework mà file này chạy trên đó. Khi một claim trong file này nói "🟡 framework inference", nó thường có nghĩa là suy luận chunks-requirement, không phải sự kiện quan sát được — các sự kiện hầu như luôn là 🟢.

---

## §2 — Giai Đoạn Connect (Sẵn Sàng Hardware)

> "Connect" = hardware có khả năng chuyển đổi đầu vào thị giác thành tín hiệu thần kinh. Giai đoạn này thiết lập **những gì hệ thống thị giác có thể làm về mặt vật lý khi sinh** — theo baseline state trong §9.1 của 02. Không phải câu hỏi chunks — mà là câu hỏi substrate.

### §2.1 — Vỏ não thị giác hoạt động từ thời thai nhi

🟢 **Bằng chứng**: Synaptogenesis V1 (vỏ não thị giác sơ cấp) bắt đầu trong tử cung và đạt mức sơ sinh vào lúc đủ tháng. V1 là một trong những **vùng vỏ não đầu tiên đạt mật độ synapse giống người lớn** — đạt đỉnh ~3-4 tháng sau sinh theo Huttenlocher 1979.

V2-V5 (các vùng thị giác ngoài sọ bao gồm MT cho chuyển động, V4 cho màu sắc, fusiform cho khuôn mặt) phát triển trong các cửa sổ chồng lấp nhau:
- V1 (sơ cấp): đỉnh synaptogenesis ~3-4 tháng
- V2-V4: đỉnh ~6-8 tháng
- Fusiform face area (FFA): đáp ứng chức năng từ ~2-4 tháng theo các nghiên cứu fMRI trên trẻ sơ sinh thức (Deen et al. 2017)

🟡 **Ghi chú framework**: Giống như PFC bị hiểu sai là "offline ở trẻ sơ sinh" theo quan điểm cũ bị bác bỏ trong 01, sự sẵn sàng vỏ não thị giác cũng không phải là câu chuyện trưởng thành — hardware online sớm, và điều thay đổi qua quá trình phát triển là **nội dung** (chunks được compile trong hardware), không phải hardware đang "được bật lên".

### §2.2 — Phát triển võng mạc

🟢 Các tế bào quang thụ thể võng mạc biệt hóa vào lúc đủ tháng. Vùng ngoại vi dominant-rod hoạt động từ ngày 1. Macula giàu cone (vùng foveal) tiếp tục trưởng thành sau sinh:
- Mật độ cone tại fovea: tăng ~5x từ khi sinh đến 4 tháng (Hendrickson & Yuodelis 1984)
- Chiều dài outer segment cone foveal: tăng gấp đôi trong 0-6 tháng
- Cấu trúc macula người lớn đạt được vào ~4 tuổi

**Hàm ý cho F1**: Acuity thị giác trẻ sơ sinh bị giới hạn không phải bởi vỏ não mà bởi hardware võng mạc — cụ thể là fovea non nớt. Đây là **giới hạn substrate** về những gì chunks thị giác có thể compile. Các chi tiết khuôn mặt tinh tế (micro-expressions, hình dạng mắt cá nhân) dưới ngưỡng acuity sơ sinh → chưa thể có trong chunks.

### §2.3 — Quỹ đạo acuity

🟢 **Quỹ đạo thực nghiệm** (Dobson & Teller 1978, Mayer & Dobson 1982, Teller 1997):

| Tuổi | Tương đương Snellen acuity |
|---|---|
| Khi sinh | ~20/400 (nhìn thấy high-contrast ~30 cm — "chiều dài cánh tay khi bú") |
| 1 tháng | ~20/300 |
| 3 tháng | ~20/100 |
| 6 tháng | ~20/40 |
| 12 tháng | ~20/30 (gần người lớn) |
| 3-5 tuổi | ~20/20 (baseline người lớn) |

**Điểm framework quan trọng**: khi sinh, acuity ~20/400 vẫn **đủ cho các pattern có kích thước khuôn mặt ở khoảng cách cho bú** (~30 cm = khoảng cách tiêu điểm thị giác tối ưu cho trẻ sơ sinh). Đây là lý do tại sao CONSPEC face preference (Fantz 1961) hoạt động từ ngày 1 mặc dù acuity "hạn chế" — acuity đủ cho task ở khoảng cách của task.

### §2.4 — Phát triển thị giác màu sắc

🟢 Hệ thống trichromatism cone có mặt từ khi sinh nhưng yếu:
- Phân biệt đỏ-xanh: có thể chứng minh từ ~1-2 tháng (Teller et al. 1978)
- Thị giác màu trichromatic đầy đủ: hình thành ~2-3 tháng
- Hình thành color category (ranh giới category xanh dương vs xanh lá): ~4-6 tháng (Franklin & Davies 2004)

🟡 **Ghi chú framework**: Màu sắc là chiều modality đi vào chunks **dần dần** trong 4-6 tháng đầu. Trước khi có màu đầy đủ, các chunks khuôn mặt sớm dựa trên pattern luminance (CONSPEC là phát hiện luminance-pattern, không dựa trên màu sắc). Điều này quan trọng cho test object file trong §3.8 — khả năng phân biệt "hai quả bóng màu khác nhau" của trẻ 4 tháng yêu cầu chunks màu sắc đã compile, không chỉ chunks object file.

### §2.5 — Cảm nhận độ sâu (stereopsis)

🟢 Cảm nhận độ sâu stereoscopic **xuất hiện đột ngột** vào khoảng 3-4 tháng (Fox et al. 1980, Held et al. 1980). Trước đó, depth cues là monocular (che khuất, motion parallax). Sau đó, random-dot stereograms có thể cảm nhận được.

**Tại sao đột ngột**: stereopsis đòi hỏi binocular vergence (mắt hội tụ vào cùng một điểm) + điều chỉnh tế bào vỏ não cho binocular disparity. Cả hai phát triển song song, và khi chúng cùng vượt ngưỡng, stereopsis xuất hiện như một bước thay đổi. Đây là **một trong số ít sự kiện phát triển trong F1 THỰC SỰ là một ngưỡng rời rạc** — tương phản với nhận dạng khuôn mặt và object chunks vốn là gradient.

### §2.6 — Tóm tắt giai đoạn Connect cho hệ thống thị giác

🟢🟡 **Những gì có sẵn khi sinh để chunks thị giác compile**:

| Thành phần | Trạng thái khi sinh | Quỹ đạo phát triển |
|---|---|---|
| Synapses V1-V2 | Gần mật độ người lớn | Đạt đỉnh 3-4 tháng, pruning qua thời thơ ấu |
| Rod võng mạc | Chức năng | Ổn định |
| Cone võng mạc (fovea) | Thưa thớt, non nớt | Làm dày trong 0-4 tháng |
| Acuity | ~20/400 | Cải thiện đến gần người lớn vào 12 tháng |
| Màu sắc | Trichromatism yếu | Đầy đủ vào 2-3 tháng |
| Stereopsis | Vắng mặt | Xuất hiện 3-4 tháng |
| Fusiform face area | Đáp ứng chức năng | Chuyên môn hóa 2-8 tháng |

**Bottleneck**: Không phải vỏ não, không phải hardware — bottleneck cho chunks thị giác là **chất lượng đầu vào + lịch sử tiếp xúc**, không phải sự sẵn sàng substrate. Đây là cùng một pattern mà PFC reframe đã xác định cho PFC: hardware sẵn sàng, nội dung thiếu. Chunks thị giác compile nhanh vì đầu vào thị giác phong phú và thường xuyên từ ngày 1.

---

> *[Phase A hoàn thành — §0 đến §2. Phase B tiếp theo: §3 Read Phase (Input Detection Chunks).]*

---

## §3 — Giai Đoạn Read (Chunks Phát Hiện Đầu Vào)

> "Read" = chunks phát hiện, phân loại, và xác định đầu vào thị giác. Mỗi sự kiện trong section này tuân theo template phương pháp luận §6: sự kiện quan sát được → chunks có thể yêu cầu → ladder level → khả năng. Các sự kiện được sắp xếp gần đúng theo thứ tự thời gian.

### §3.1 — Face preference từ khi sinh (CONSPEC)

🟢 **Sự kiện**: Trẻ sơ sinh (2-5 ngày tuổi) nhìn lâu hơn vào các pattern giống khuôn mặt (hai chấm ở trên một chấm trong hình oval) hơn so với các pattern không phải khuôn mặt có độ phức tạp tương đương (bị xáo trộn hoặc đảo ngược).

🟢 **Nghiên cứu**:
- Fantz 1961 — minh chứng gốc dùng khuôn mặt hình học vs kiểm soát
- Morton & Johnson 1991 — mô hình hai hệ thống CONSPEC/CONLERN (CONSPEC = bộ phát hiện face-template bẩm sinh hoạt động dưới mức vỏ não, CONLERN = xử lý khuôn mặt dựa trên học tập vỏ não xuất hiện 2-3 tháng)
- Johnson et al. 1991 — ưu tiên khuôn mặt trẻ sơ sinh cho pattern giống khuôn mặt qua nhiều nghiên cứu tái lập

🟡 **Chunks yêu cầu cho sự kiện**:
- **Innate face template (CONSPEC)** — KHÔNG phải compiled chunk. Bộ phát hiện pattern được hard-wired hoạt động dưới mức vỏ não (Morton & Johnson đề xuất con đường subcortical qua superior colliculus + pulvinar).
- Không cần learned face chunks ở tuổi này (chưa có kinh nghiệm).

**PFC-Inference Ladder**: **L0** với caveat — preference bản thân là reflex-like (innate template điều khiển sự chú ý), nhưng *sự chú ý* (nhìn lâu hơn) bị điều chỉnh bởi CONLERN pattern-match trong những tuần đầu. Phân loại: L0 khi sinh → chuyển sang L2 (pattern-match fire) khi CONLERN tham gia vào ~2-3 tháng.

**🟢 Khả năng**: Cao cho sự kiện, framework-standard cho claim chunks.

**Hàm ý cho F1**: Framework phân biệt **innate templates** (CONSPEC) với **compiled chunks** (CONLERN-built face chunks). Cả hai đều là "khả năng phát hiện khuôn mặt" từ góc độ hành vi, nhưng kiến trúc khác nhau. Reframe từ [01-PFC-Hardware-Reframe.md](01-PFC-Hardware-Reframe.md) §5 (phân biệt 7-thành-phần hardware vs content) áp dụng: CONSPEC = hardware innate detector, CONLERN = content được compile từ tiếp xúc.

### §3.2 — Direct gaze preference 2-5 ngày (Farroni 2002) ⭐

🟢 **Sự kiện**: Trẻ sơ sinh (tuổi trung bình 2-5 ngày) nhìn lâu hơn vào ảnh khuôn mặt với **direct eye gaze** (mắt nhìn vào người xem) hơn so với khuôn mặt giống hệt với **averted eye gaze** (mắt nhìn lệch 20° sang một bên).

🟢 **Nghiên cứu**:
- Farroni et al. 2002 — nghiên cứu gốc, 17 trẻ sơ sinh, direct gaze = looking time dài hơn
- Tái lập nhiều lần (Batki et al. 2000, Farroni et al. 2004)
- Mở rộng: trẻ 4 tháng tuổi cho thấy phản ứng thần kinh tăng cường (ERP N290) với khuôn mặt direct gaze

🟡 **Chunks yêu cầu**:
- CONSPEC face template firing (đã đề cập §3.1)
- **Bộ phát hiện direct-gaze subcomponent** — bẩm sinh (có thể vì timing 2-5 ngày) hay compile trong tử cung từ... cái gì? Tử cung tối, thai nhi không thấy mắt.
- **Framework claim**: 🟡 Giải thích có thể nhất là **bộ phát hiện direct-gaze bẩm sinh gắn với CONSPEC** — template không chỉ chứa "hai chấm ở trên một chấm" mà đặc biệt là "hai chấm hướng về phía người xem". Lập luận tiến hóa: direct gaze là tín hiệu xã hội mạnh nhất, xứng đáng được pre-wire.

**PFC-Inference Ladder**: **L2** 🟡. Đây là một trong những sự kiện L2 quan sát được sớm nhất — pattern-match fires (looking time bị điều chỉnh bởi category kích thích), không cần liên quan đến hành động. Quan trọng: 2-5 ngày sớm hơn bất kỳ cửa sổ học tập post-birth nào có thể xảy ra cho pattern cụ thể này. Nếu CONSPEC có direct-gaze subcomponent, hành vi L2 có thể xảy ra từ khi sinh.

**🟢 Khả năng**: Sự kiện có độ tin cậy cao (được tái lập). Claim chunks-required 🟡 (phân biệt bẩm sinh vs compiled có tính suy đoán).

**Tại sao sự kiện này load-bearing cho reframe**: Direct gaze preference ở 2-5 ngày là một **thách thức falsification cho quan điểm cũ "PFC offline"**. Nếu PFC không hoạt động, một sự kiện L2 pattern-match vẫn có thể xảy ra (vì L2 có thể chạy trên subcortical + early cortex), NHƯNG quan điểm cũ thường đồng nhất sự trưởng thành PFC với **bất kỳ** chức năng "nhận thức cao hơn". Farroni 2002 cho thấy phân biệt dựa trên các tính năng thị giác tinh tế ở 2-5 ngày — quá sớm cho bất kỳ giải thích nào dựa trên học tập, quá tinh tế cho pure brainstem reflex. Phương pháp luận event-inference xử lý điều này gọn gàng: sự kiện quan sát được (🟢) → chunks yêu cầu (innate template 🟡) → phân loại L2 → không cần claim PFC timeline.

### §3.3 — Phát hiện pattern high-contrast

🟢 **Sự kiện**: Trẻ sơ sinh theo dõi bằng thị giác các pattern chuyển động high-contrast (cạnh tối-sáng, bàn cờ) ưu tiên hơn so với các trường đơn nhất hoặc low-contrast.

🟢 **Nghiên cứu**: Fantz 1963, Salapatek 1975, Banks & Salapatek 1981 — được tái lập vững.

🟡 **Chunks yêu cầu**: Không cần học tập. Điều chỉnh retinal ganglion cell + các cột orientation-selective V1 được tổ chức bẩm sinh để phát hiện edge. Đây là substrate, không phải chunks.

**PFC-Inference Ladder**: **L0** (chú ý reflex-level).

**Hàm ý**: High-contrast preference là **cơ chế scaffolding cho chunks compilation** — bằng cách ưu tiên nhìn vào các vùng high-contrast, trẻ sơ sinh oversample các phần thông tin phong phú nhất của trường thị giác (ví dụ: ranh giới tóc-khuôn mặt, mắt, miệng mẹ khi nói). Điều này tăng tốc chunks compile bằng cách tập trung tiếp xúc vào các vùng thông tin cao.

### §3.4 — Nhận dạng khuôn mặt mẹ ở 5 tháng (E15) ⭐ multi-modal

🟢 **Sự kiện**: Trẻ sơ sinh ~5 tháng tuổi, khi nhìn thấy mẹ vào phòng sau khi vắng mặt ngắn, cho thấy: mắt sáng lên, đạp chân, cười, phát âm, với tay về phía mẹ. Phản ứng **đặc hiệu-mẹ** — có thể phân biệt với phản ứng với người lạ, anh chị em, cha, v.v. (Feel-Example E15, [../../Body-Base/Feeling/Feel-Example-Draft.md](../../Body-Base/Feeling/Feel-Example-Draft.md#e15) dòng 927.)

🟢 **Nghiên cứu**:
- Bushnell et al. 1989 — trẻ 4 ngày tuổi ưu tiên khuôn mặt mẹ hơn người lạ (phát hiện sớm nhất)
- Pascalis et al. 1995 — xác nhận trẻ 4 ngày tuổi có thể phân biệt khuôn mặt mẹ với người lạ tương tự
- de Haan & Nelson 1999 — trẻ 6 tháng thể hiện sự khác biệt ERP (N290) cho khuôn mặt mẹ
- Framing Feel-Example E15 như **identity chunk** (được bind multi-modal)

🟡 **Chunks yêu cầu**:
- **Chunks khuôn mặt đặc hiệu-mẹ** — compile từ ~nhiều tháng tiếp xúc thị giác. Lưu ý: phân biệt 4 ngày (Bushnell 1989) gợi ý compilation bắt đầu ngay sau khi sinh, nhưng phản ứng *phong phú hơn* ở 5 tháng (E15) gợi ý chunk là multi-modal và đã tích lũy thêm các chiều (voice binding, smell binding, comfort history binding).
- **Binding chunks** — liên kết pattern khuôn mặt thị giác với voice chunks (từ trước sinh, xem 02 §4.1), với smell chunks (compile sau sinh), với warmth/comfort chunks (compile trong quá trình cho ăn).
- **Associative chunk**: "mặt mẹ → trạng thái tích cực được kỳ vọng" (anchored vào kinh nghiệm thoải mái trước đó).

**PFC-Inference Ladder**: **L2-L3** 🟢🟡. L2 vì pattern-match fires (nhận dạng thị giác → mắt sáng lên = marker nhận dạng, không phải hành động). Gần L3 vì thành phần motor xuất hiện (với tay, đạp, cười) — nụ cười là multi-modal output, có thể lập luận là phản ứng phối hợp thô. Feel-Example đóng khung đây là **chunk identity đặc hiệu đầu tiên** (vs phát hiện khuôn mặt chung).

**🟢 Khả năng**: Sự kiện được ghi chép vững. Framework claim về identity chunk vs khuôn mặt chung: Feel-Example § giải thích sự phân biệt qua pattern "mắt sáng lên + đạp + với tay" **đặc hiệu với mẹ**, không phải khuôn mặt-chung kích hoạt.

**Tại sao sự kiện này load-bearing**: Nhận dạng khuôn mặt mẹ cho thấy câu chuyện **compiled chunk** đang vận hành. CONSPEC xử lý phát hiện khuôn mặt ngày sinh (§3.1). Vào 5 tháng, khuôn mặt mẹ là một identity chunk được bind phong phú tích hợp:
- Pattern khuôn mặt thị giác (fusiform face area)
- Pattern giọng (từ prenatal auditory chunks)
- Smell chunks (từ cho bú)
- Thoải mái/warmth association (từ cho ăn và soothing)
- Sự ổn định tương đối (mẹ chủ yếu có mặt trong những tuần đầu)

Đây là nơi **Nút Thắt 3 (cơ chế multi-modal binding)** có dạng cụ thể nhìn thấy được. Drill cơ chế đầy đủ được deferred đến [07-Social-Recognition-Arc.md](07-Social-Recognition-Arc.md) §6, nhưng thành phần thị giác là modality anchoring chính.

### §3.5 — Feature integration emergence (Treisman 1980)

🟡 **Sự kiện**: Giữa ~3-6 tháng, trẻ bắt đầu tích hợp các tính năng thị giác riêng biệt (màu sắc, hình dạng, chuyển động) vào các biểu diễn vật thể thống nhất. Trước đó, các tính năng có vẻ được phát hiện nhưng không được bind thành "vật thể" đơn.

🟡 **Nghiên cứu**:
- Treisman 1980 Feature Integration Theory (công trình người lớn)
- Mareschal & Johnson 2003 — các nghiên cứu object file formation ở trẻ sơ sinh
- Tremoulet et al. 2000 — feature binding ở trẻ 4 tháng dùng habituation paradigm

🟡 **Chunks yêu cầu**:
- Feature detection chunks (color chunks, shape chunks, motion chunks) — compile trong vài tháng đầu
- **Binding chunks** — liên kết các tính năng đồng thời tại cùng vị trí không gian
- Không cần "integration" mức PFC — binding có thể xảy ra trong vỏ não thị giác sớm + vùng parietal

**PFC-Inference Ladder**: Khó phân loại sạch — feature integration là **khả năng substrate**, không phải sự kiện quan sát rời rạc. Các nghiên cứu habituation cho thấy gradient emergence trong 3-6 tháng. Phân loại tốt nhất là **compile mechanism phase** hơn là single event.

**🟡 Khả năng**: Sự kiện bản thân 🟡 (suy luận từ habituation paradigms, không quan sát trực tiếp được). Claim chunks-required 🟡.

**Ghi chú framework**: Feature integration là **substrate cho object file chunks** (§3.8 tiếp theo). Đây là điều kiện tiên quyết cần thiết. Gradient emergence là bằng chứng cho Nút Thắt 1 (quan điểm proto-chunk gradient) — integration không bật lên ở một thời điểm rời rạc mà tăng dần qua nhiều tuần.

### §3.6 — Chunks phân biệt màu sắc

🟢 **Sự kiện**: Trẻ 4 tháng tuổi phân biệt màu sắc thành các category giống người lớn (ranh giới xanh dương vs xanh lá tương tự người lớn mặc dù không gian màu liên tục về mặt vật lý).

🟢 **Nghiên cứu**: Bornstein, Kessen & Weiskopf 1976 — bài báo cổ điển chứng minh infant color categorical perception. Franklin & Davies 2004 — tái lập + quỹ đạo phát triển.

🟡 **Chunks yêu cầu**: Color chunks compile từ tiếp xúc thị giác + có thể ranh giới categorical bị ảnh hưởng bởi điều chỉnh cone bẩm sinh + có thể ảnh hưởng ngôn ngữ (mặc dù điều này gây tranh cãi — Franklin et al. 2008 cho thấy trẻ sơ sinh pre-linguistic đã categorize).

**PFC-Inference Ladder**: **L2** 🟡. Pattern-match trên color category fires (habituation phục hồi khi màu vượt ranh giới category). Không có hành động. Sự kiện L2 cổ điển.

### §3.7 — Object file chunks đang xuất hiện (4-6 tháng)

🟢 **Sự kiện**: Trẻ 4-6 tháng thể hiện hành vi "object file" trong các thí nghiệm looking-time — khi một vật thể bị che khuất rồi được thay thế bằng một vật thể khác biệt về mặt vật lý (màu khác, hình dạng khác), trẻ nhìn lâu hơn như thể ngạc nhiên, nhưng nếu cùng một vật thể, nhìn ít hơn. Điều này chỉ ra **biểu diễn cấp vật thể** (không chỉ là ảnh võng mạc).

🟢 **Nghiên cứu**:
- Kahneman, Treisman & Gibbs 1992 — object file theory (công trình người lớn)
- Xu & Carey 1996 — các nghiên cứu object individuation ở trẻ sơ sinh
- Baillargeon 1995 — theo dõi vật thể qua che khuất

🟡 **Chunks yêu cầu**:
- Individual object features chunks (màu, hình dạng, kích thước)
- **Object file chunk** — binding các tính năng thành biểu diễn "vật thể này" đơn lẻ tồn tại qua che khuất tạm thời
- Spatiotemporal continuity chunks (vật thể không teleport, không thay đổi identity ngẫu nhiên)

**PFC-Inference Ladder**: **L2** 🟡🟢. Pattern-match trên mismatch event (vật thể thay đổi thành vật thể khác) → looking time dài hơn là marker L2. Không cần hành động.

### §3.8 — Object permanence (Baillargeon VoE 4-6 tháng → ổn định 8-9 tháng) ⭐ Nút Thắt 1

🟢 **Sự kiện**: Dùng paradigm **Violation of Expectation (VoE)**, trẻ 4-6 tháng thể hiện looking times dài hơn khi các trường hợp bất khả thi vật lý liên quan đến vật thể bị che khuất được hiển thị (ví dụ: vật thể có vẻ đi qua rào cản vững chắc, vật thể xuất hiện ở hai vị trí).

🟢 **Nghiên cứu**:
- Baillargeon 1987 — nghiên cứu "drawbridge" với trẻ 4 tháng
- Baillargeon & DeVos 1991 — bằng chứng object permanence từ 3.5 tháng
- Spelke et al. 1992 — các nguyên tắc object core knowledge
- Hespos & Baillargeon 2001 — trẻ 2.5 tháng thể hiện ngạc nhiên liên quan đến vật thể

Tương phản với **Piaget A-not-B task** cổ điển (Piaget 1954) trong đó trẻ 8-9 tháng thất bại với tay vào vật thể ẩn → Piaget kết luận "không có object permanence". Phương pháp looking-time của Baillargeon tiết lộ kiến thức permanence 4+ tháng sớm hơn phương pháp action-based của Piaget. Đây là **asymmetry knowing vs acting** cổ điển — phản ánh receptive-productive gap (Nút Thắt 5) ở một cấp độ khác nhau.

🟡 **Chunks yêu cầu**:
- Object file chunks (§3.7)
- **Persistence chunks** — "vật thể tồn tại khi không nhìn thấy"
- **Trajectory chunks** — "vật thể di chuyển liên tục trong không gian"
- **Solidity chunks** — "vật thể vững chắc không đi qua vật thể vững chắc"
- Tất cả những điều này cần compile với độ ổn định đủ cao để tạo ra prediction + phát hiện mismatch

**PFC-Inference Ladder**: **L2** 🟢. Đây là sự kiện L2 điển hình: prediction chunk fires, thực tế mismatch, looking time tăng (tín hiệu chú ý pattern-match của PFC). Không cần hành động. Chuyển tiếp L2→L3 cho object permanence là **phía reaching** — trẻ 8-9 tháng có thể *hành động* dựa trên kiến thức permanence (với tay vào vị trí nơi vật thể bị ẩn) điều này thêm L3 action chunks trên L2 pattern-match.

**⭐ Nút Thắt 1 test case**: Object permanence chunks không xuất hiện "tất cả cùng lúc". Công trình của Baillargeon cho thấy **gradient emergence**:
- 2.5 tháng: ngạc nhiên cơ bản với trajectory bất khả thi (Hespos & Baillargeon 2001)
- 3.5-4 tháng: bất khả thi rào cản vững chắc (Baillargeon 1987)
- 4-6 tháng: các kịch bản permanence phức tạp hơn
- 8-9 tháng: permanence dựa trên hành động (với tay vào vị trí ẩn)
- 12 tháng trở lên: lý luận permanence phức tạp hơn

**Đóng góp verdict drill F1**: Object permanence chunks compile theo **gradient** — không rời rạc. Mỗi sub-chunk (solidity, trajectory, continuity, identity) compile bán độc lập với các tỷ lệ trưởng thành khác nhau. Điều này hỗ trợ **quan điểm gradient Nút Thắt 1** (hơn là quan điểm rời rạc). Verdict đầy đủ Nút Thắt 1 được deferred đến [04-Auditory-System-Arc.md](04-Auditory-System-Arc.md) §6 (phân biệt phoneme cung cấp bằng chứng gradient thậm chí sạch hơn) + [10-F1-Synthesis.md](10-F1-Synthesis.md).

### §3.9 — Face categorization và individuation 6-9 tháng

🟢 **Sự kiện**: Giữa 6-9 tháng, trẻ thể hiện perceptual narrowing cho khuôn mặt — chúng có thể phân biệt khuôn mặt cùng loài và cùng chủng tộc tốt hơn khuôn mặt khác loài hoặc khác chủng tộc, một quỹ đạo ngược với phát hiện khuôn mặt không bị hạn chế sớm.

🟢 **Nghiên cứu**: Pascalis, de Haan & Nelson 2002 — trẻ 6 tháng phân biệt khuôn mặt khỉ, trẻ 9 tháng thì không (perceptual narrowing song song với phoneme narrowing trong 04 §3.5). Kelly et al. 2007 — other-race effect xuất hiện tương tự.

🟡 **Chunks yêu cầu**: Own-race face chunks được compile nhiều từ tiếp xúc → ranh giới categorical sắc nét hơn cho các loại quen thuộc → các loại không quen thuộc nằm ngoài ranh giới sắc nét.

**PFC-Inference Ladder**: **L2** 🟢. Sức mạnh pattern-match khác nhau theo mức độ quen thuộc.

**Cross-reference với Nút Thắt 1**: Sự kiện này cho thấy **cùng gradient pattern** như phoneme narrowing thính giác (04 §3.5). Sự song song này gợi ý — chunks compilation qua tiếp xúc theo hình dạng tương tự qua các modality cảm giác. Hỗ trợ gián tiếp mạnh cho quan điểm gradient.

---

> *[Phase B hoàn thành — §3 (9 sub-sections). Phase C tiếp theo: §4 Control Phase + §5 Master Table.]*

---

## §4 — Giai Đoạn Control (Chunks Đầu Ra)

> "Control" = chunks tạo ra đầu ra motor thị giác (chuyển động mắt, quay đầu, nhìn phối hợp) hoặc hướng dẫn đầu ra motor cơ thể bằng đầu vào thị giác. Những sự kiện này liên quan đến hành động, cao hơn trên ladder.

### §4.1 — Smooth pursuit eye movements (6-8 tuần)

🟢 **Sự kiện**: Trẻ sơ sinh theo dõi mục tiêu chuyển động trơn tru (không bị giật cục) từ ~6-8 tuần. Trước đó, tracking có tính saccadic (bước nhảy từng bước).

🟢 **Nghiên cứu**: Aslin 1981 review, Shea & Aslin 1990, Rosander & von Hofsten 2000.

🟡 **Chunks yêu cầu**: Motor prediction chunks (mục tiêu sẽ ở đâu tiếp theo) + smooth-motor output chunks (oculomotor). Cả hai compile trong vài tuần đầu.

**PFC-Inference Ladder**: **L1-L2** 🟡. Phản ứng là reactive (L1) nhưng với thành phần prediction (L2 đang xuất hiện). Transitional — đang chuyển tiếp.

### §4.2 — Quay đầu về phía mục tiêu thị giác (3-4 tháng)

🟢 **Sự kiện**: Trẻ sơ sinh quay đầu về phía các mục tiêu thị giác thú vị vào 3-4 tháng (chunk chú ý thị giác + motor cổ tích hợp).

🟡 **Chunks yêu cầu**: Attention chunks (vật thể nổi bật) + head motor chunks (kiểm soát cổ đã trưởng thành — xem [05-Motor-Output-Arc.md](05-Motor-Output-Arc.md) §3.2) + binding chunks (sự nổi bật thị giác → phản ứng motor đầu).

**PFC-Inference Ladder**: **L2-L3** 🟡. Đầu ra phối hợp, pattern-match trên thị giác nổi bật kích hoạt motor đầu.

### §4.3 — Với tay được hướng dẫn bằng thị giác (4-5 tháng)

🟢 **Sự kiện**: Trẻ sơ sinh với tay đến các vật thể được nhận thức bằng thị giác với độ chính xác hợp lý ở 4-5 tháng. Trước đó, với tay là các lần quét ngẫu nhiên; mục tiêu thị giác chưa được tích hợp với motor tay.

🟢 **Nghiên cứu**: von Hofsten 1979, 1984 — các nghiên cứu với tay trẻ sơ sinh cổ điển.

🟡 **Chunks yêu cầu**:
- Visual object location chunks
- Arm motor chunks (xem [05-Motor-Output-Arc.md](05-Motor-Output-Arc.md) §2.4)
- **Visuomotor binding chunks** — liên kết tọa độ mục tiêu thị giác với tọa độ motor (coordinate transformation)

**PFC-Inference Ladder**: **L3** 🟡. Hành động phối hợp một phần, chưa chính xác, cải thiện theo tháng.

**Ghi chú multi-modal binding**: Với tay được hướng dẫn bằng thị giác là **visuomotor chunk đầu tiên** binding đầu vào thị giác với đầu ra motor. Milestone quan trọng cho Nút Thắt 3 trong chiều motor. Xử lý đầy đủ trong [05-Motor-Output-Arc.md](05-Motor-Output-Arc.md) §2.4.

### §4.4 — Gaze following (6 tháng, E14) ⭐

🟢 **Sự kiện**: Trẻ sơ sinh ~6 tháng. Mẹ nhìn vào trẻ, rồi quay đầu nhìn vào một vật thể cụ thể (một cái cửa, một món đồ chơi). Trẻ theo ánh mắt mẹ và nhìn vào cùng vật thể. ([Feel-Example E14](../../Body-Base/Feeling/Feel-Example-Draft.md#e14) dòng 876.)

🟢 **Nghiên cứu**: Butterworth 1991, Corkum & Moore 1995, Tomasello 1995, Carpenter et al. 1998. Phát hiện xuyên văn hóa nhất quán: 6-9 tháng là tuổi gaze following đáng tin cậy sớm nhất.

🟡 **Chunks yêu cầu**:
- Chunk "hướng nhìn của mẹ" (hướng quay đầu)
- Spatial mapping chunk (từ hướng khuôn mặt đến vị trí trong không gian 3D)
- Output chunk: "chuyển hướng nhìn của mình để theo" (saccadic gaze shift được thực hiện)
- Có thể là **expectation chunk**: "nếu mẹ nhìn vào đó, có gì đó thú vị ở đó" (curiosity-driven)

**PFC-Inference Ladder**: **L3** 🟢. Đầu ra phối hợp (gaze shift), pattern-match trên hướng của mẹ, phản ứng hành động. Chưa phải triadic đầy đủ (không có checking back với mẹ — đó là E18).

**Tại sao 6 tháng chứ không phải sớm hơn**: Chunks cho spatial direction mapping cần vài tháng kinh nghiệm đồng thời xảy ra — nhìn vào khuôn mặt mẹ + vật thể theo hướng nhìn của mẹ + cả hai đều hiện diện đồng thời → binding. Cũng yêu cầu motor chunks cho gaze shift kiểm soát được.

### §4.5 — Object tracking qua che khuất (8-9 tháng)

🟢 **Sự kiện**: Trẻ 8-9 tháng chủ động tìm kiếm các vật thể ẩn sau các occluders (Piaget A-not-B task; cũng các search paradigms khác).

🟡 **Chunks yêu cầu**: Object permanence chunks (từ §3.8) + search motor chunks + spatial chunk "vật thể ở đâu cuối cùng được nhìn thấy" + inhibition chunks (ngăn perseverative reaching đến vị trí cũ).

**PFC-Inference Ladder**: **L3-L4** 🟢. Hành động phối hợp dùng kiến thức permanence. **A-not-B error** bản thân là một trường hợp framework đẹp:
- Trẻ biết vật thể bị ẩn (L2 permanence)
- Trẻ với tay vào nó (L3 action)
- Trẻ với tay đến VỊ TRÍ CŨ ĐÚNG TRƯỚC ĐÓ, không phải vị trí hiện tại (perseverative error)
- Lỗi cho thấy inhibition chunks chưa đủ ổn định

Piaget đọc đây là "không có permanence" (sai — hành động thất bại về mặt hành vi). Quan điểm hiện đại: permanence chunks có mặt (VoE từ 4 tháng), nhưng **inhibition chunks để override prepotent motor response chưa đủ mạnh**. Đây là câu hỏi chunks-state vs "sự trưởng thành PFC" cổ điển — và chunks-state thắng phần giải thích.

### §4.6 — Joint attention triadic (9-12 tháng, E18) ⭐

🟢 **Sự kiện**: Trẻ sơ sinh ~10 tháng. Mẹ chỉ vào một vật thể ("nhìn kìa, con chó!"). Trẻ nhìn theo hướng tay chỉ của mẹ, thấy vật thể, rồi **nhìn lại mẹ**, rồi lại nhìn vào vật thể. Tam giác ánh nhìn tôi-mẹ-vật thể là **triadic joint attention** — khoảnh khắc định nghĩa. ([Feel-Example E18](../../Body-Base/Feeling/Feel-Example-Draft.md#e18) dòng 1092.)

🟢 **Nghiên cứu**: Butterworth 1991, Tomasello 1995, Tomasello 1999 "Cultural Origins of Human Cognition", Carpenter, Nagell & Tomasello 1998 — nghiên cứu dọc cho thấy xuất hiện điển hình 9-12 tháng.

🟡 **Chunks yêu cầu** (đây là tập chunks visual-social đòi hỏi nhất trong năm đầu):
- **Point gesture interpretation chunk** — hiểu rằng bàn tay chỉ chỉ ra hướng, không phải bàn tay bản thân là mục tiêu. Quan sát của Wittgenstein "con chó nhìn vào ngón tay, không phải thứ nó chỉ vào" — trẻ sơ sinh người **học** để nhìn qua ngón tay.
- **Gaze direction + point direction coordination chunk** — mắt mẹ + bàn tay mẹ thường chỉ cùng hướng, tạo ra đồng thời xảy ra mạnh để binding.
- **Shared attention schema chunk** — "mẹ và tôi có thể nhìn vào cùng vật thể đồng thời và mẹ nhận thấy tôi đang nhìn"
- **Reference chunk** — "vật thể này là chủ đề trong sự chú ý của mẹ"
- **Checking-back chunk** — vòng lặp ánh nhìn tôi→vật thể→mẹ→vật thể là điều phân biệt joint attention với gaze following đơn thuần

**PFC-Inference Ladder**: **L4** 🟢. Thực thi phối hợp đầy đủ: nhiều chunks (nhìn, chỉ, shared reference, checking-back) được tích hợp vào hành động đáng tin cậy, hướng mục tiêu.

**Tại sao joint attention là đỉnh cao của arc thị giác năm đầu**: Nó tích hợp:
- Visual face/gaze chunks (§3.2, §4.4)
- Point-gesture chunks (xem [05-Motor-Output-Arc.md](05-Motor-Output-Arc.md) §2.8)
- Social reference chunks (xem [07-Social-Recognition-Arc.md](07-Social-Recognition-Arc.md))
- Tiền đề theory-of-mind sớm (mẹ có "một cái nhìn" về một vật thể)
- Schema communicative intent (cả hai agent cùng định hướng đến cùng thứ với mục đích)

Đây là một **sự kiện tích hợp multi-modal multi-body-input lớn** — thị giác + xã hội + motor + pre-verbal + chú ý. Feel-Example E18 đóng khung nó như nền tảng cho language explosion sau đó (18-24 tháng). Luận điểm của Tomasello: không có joint attention, không có ngôn ngữ. Joint attention là **referential scaffold** trên đó word-object mapping có thể xảy ra.

### §4.7 — Mirror self-recognition (18-24 tháng, Amsterdam 1972)

🟢 **Sự kiện**: Trẻ 18-24 tháng, khi một chấm đỏ bí mật được bôi lên trán và họ nhìn vào gương, với tay chạm vào **trán của chính họ** (không phải hình ảnh gương). Trước ~18 tháng, họ với tay đến hình ảnh gương như thể đó là em bé khác.

🟢 **Nghiên cứu**: Amsterdam 1972 — "rouge test" cổ điển. Gallup 1970 — song song tinh tinh. Lewis & Brooks-Gunn 1979 — quỹ đạo phát triển.

🟡 **Chunks yêu cầu**:
- Body schema chunks (self-proprioception qua cơ thể)
- Visual self-chunk — "khuôn mặt được phản chiếu này là tôi"
- **Self-other distinction chunk ở cấp thị giác** — điều kiện tiên quyết quan trọng
- Cross-modal binding: khuôn mặt thị giác ↔ cơ thể proprioceptive

**PFC-Inference Ladder**: **L4** 🟡. Thực thi phối hợp, liên quan đến self-other distinction. Claim chunks-required là 🟡 — tồn tại các cách giải thích thay thế (một số lập luận nó không phải bằng chứng về "self-concept" theo nghĩa người lớn, chỉ là body schema).

**Hàm ý framework**: Mirror self-recognition là một trong những sự kiện F1 muộn nhất (gần cuối cửa sổ 24 tháng). Nó chứng minh rằng **visual self chunks** (nhìn thấy bản thân như một thực thể riêng biệt) compile **sau** nhiều năm kinh nghiệm multi-modal và là một trong những chunks thị giác phức tạp nhất trong hai năm đầu. Đây là substrate mà Agent/Self-Pattern-Modeling (H9, drilled N+2) sau đó hoạt động ở các cấp cao hơn.

---

## §5 — Các Sự Kiện Được Phân Tích với PFC-Inference Ladder (Master Table)

> §3 và §4 phân tích các sự kiện riêng lẻ. Section này tổng hợp chúng vào một bảng phân loại ladder duy nhất để cross-reference + thể hiện event-inference template đang vận hành.

### §5.1 — Master event ladder table (hệ thống thị giác 0-24 tháng)

| # | Sự kiện | Tuổi | Body-input | Ladder | Chunks chính yêu cầu | Nghiên cứu |
|---|---|---|---|---|---|---|
| V1 | Face preference | Khi sinh (Fantz paradigm) | Thị giác | L0→L2 | CONSPEC innate template | Fantz 1961, Morton & Johnson 1991 |
| V2 | Direct gaze preference | 2-5 ngày | Thị giác | L2 🟡 | CONSPEC + direct-gaze subcomponent | Farroni 2002 |
| V3 | High-contrast pattern attention | Khi sinh | Thị giác | L0 | Innate wiring võng mạc/V1 | Fantz 1963, Salapatek 1975 |
| V4 | Smooth pursuit | 6-8 tuần | Thị giác + motor | L1-L2 | Oculomotor + prediction chunks | Aslin 1981 |
| V5 | Social smile multi-modal | 6-8 tuần | Thị giác + thính giác + cơ thể | L2-L3 🟢 | Face + voice + calm state bind | Feel-Example E12 |
| V6 | Head turn về phía mục tiêu | 3-4 tháng | Thị giác + motor | L2-L3 🟡 | Saliency + neck motor + bind | Aslin 1981 |
| V7 | Stereopsis onset | 3-4 tháng | Thị giác | L0 (hardware) | Binocular substrate | Fox 1980, Held 1980 |
| V8 | Color category chunks | 4 tháng | Thị giác | L2 🟡 | Compiled category chunks | Bornstein 1976 |
| V9 | Object file chunks | 4-6 tháng | Thị giác | L2 🟡 | Feature binding + file | Xu & Carey 1996 |
| V10 | Với tay được hướng dẫn bằng thị giác | 4-5 tháng | Thị giác + motor | L3 🟡 | Visuomotor bind | von Hofsten 1979 |
| V11 | Object permanence VoE | 4-6 tháng | Thị giác | L2 🟢 | Persistence + trajectory chunks | Baillargeon 1987 |
| V12 | Mother face recognition | 5 tháng | Thị giác + multi-modal | L2-L3 🟢🟡 | Mother identity chunk | Feel-Example E15, Bushnell 1989 |
| V13 | Gaze following | 6 tháng | Thị giác + motor | L3 🟢 | Direction-following chunk | Feel-Example E14, Butterworth 1991 |
| V14 | Face perceptual narrowing | 6-9 tháng | Thị giác | L2 🟢 | Own-race strengthening | Pascalis 2002 |
| V15 | Object tracking qua che khuất | 8-9 tháng | Thị giác + motor | L3-L4 🟢 | Permanence + search | A-not-B paradigm |
| V16 | Stranger anxiety | 7-9 tháng | Thị giác + xã hội + cơ thể | L2-L3 🟢 | Familiar library + mismatch | Feel-Example E16, Sroufe 1977 |
| V17 | Joint attention triadic | 9-12 tháng | Thị giác + xã hội + motor | L4 🟢 | Point + gaze + shared reference | Feel-Example E18, Tomasello 1995 |
| V18 | Social referencing | 10-12 tháng | Thị giác + xã hội | L3-L4 🟢 | Face reading + decision | Feel-Example E19 |
| V19 | Mirror self-recognition | 18-24 tháng | Thị giác + cơ thể | L4 🟡 | Self-visual chunk | Amsterdam 1972 |

### §5.2 — Worked examples của event-inference template

Hai worked examples áp dụng quy tắc phương pháp luận §6:

**Worked Example A — Farroni 2002 direct gaze preference (V2)**:

```
[Sự kiện quan sát được, tuổi, citation]
Trẻ sơ sinh 2-5 ngày tuổi nhìn lâu hơn vào khuôn mặt direct-gaze
hơn khuôn mặt averted-gaze.
(Farroni et al. 2002, Current Biology, 17 trẻ sơ sinh, tái lập dọc.)
    ↓
[Chunks có thể yêu cầu]
- CONSPEC face template (innate hardware detector, §3.1)
- Direct-gaze subcomponent (bẩm sinh hoặc trước sinh; không compile
  vì không có kinh nghiệm thị giác trước sinh)
- Không cần learning-based chunks
    ↓
[PFC-Inference Ladder level]
L2 — pattern-match fires (looking time bị điều chỉnh bởi category kích thích),
không có thành phần hành động
    ↓
[Plausibility qualifier]
Sự kiện 🟢 (tái lập nhiều lần)
Claim chunks-required 🟡 (innate-vs-compiled ở 2-5 ngày là borderline; suy luận
framework rằng CONSPEC là bẩm sinh được hỗ trợ vững; direct-gaze subcomponent
có thể bẩm sinh xét theo timing)
Phân loại Ladder 🟡🟢 (L2 behavioral markers rõ ràng, suy luận liên quan PFC
qua hardware reframe)
```

**Worked Example B — Joint attention triadic (V17)**:

```
[Sự kiện quan sát được, tuổi, citation]
Trẻ 9-12 tháng theo ánh mắt chỉ + tay chỉ của mẹ đến mục tiêu,
rồi nhìn lại mẹ, rồi trở lại mục tiêu. Triadic gaze pattern
(tôi-mẹ-vật thể-mẹ).
(Tomasello 1995, Carpenter et al. 1998; Feel-Example E18.)
    ↓
[Chunks có thể yêu cầu]
- Point gesture interpretation chunk (hướng, không phải mục tiêu)
- Gaze direction chunk
- Spatial mapping chunk (hướng → vị trí trong không gian 3D)
- Shared reference chunk (cả hai chúng tôi đang nhìn vào cùng thứ)
- Check-back chunk (vòng lặp)
- Expectation chunk (vật thể có liên quan vì mẹ chú ý)
    ↓
[PFC-Inference Ladder level]
L4 — thực thi phối hợp, đáng tin cậy, hướng mục tiêu, tích hợp multi-chunk
    ↓
[Plausibility qualifier]
Sự kiện 🟢 (được tái lập xuyên văn hóa)
Claim chunks-required 🟢🟡 (danh sách chunks là suy luận framework nhưng
mỗi sub-chunk được hỗ trợ độc lập trong văn liệu)
Ladder L4 🟢 (rõ ràng là thực thi phối hợp, không chỉ pattern-match)
```

### §5.3 — Điều classification này thực hiện được

Ba điều:

1. **Không cần claim "PFC trưởng thành"**. Mọi sự kiện đều có tài khoản chunks-required + phân loại ladder + khả năng. PFC timeline vắng mặt. Điều này tuân theo quy tắc 01 §6 và bác bỏ framing của quan điểm cũ bằng cách đơn giản là không cần đến nó.

2. **Quỹ đạo phát triển xuất hiện từ các sự kiện**, không phải ngược lại. Hơn là dự đoán "PFC sẽ online ở tuổi X", file này mô tả **các sự kiện thực sự quan sát được ở các tuổi** và **suy luận** trạng thái chunks từ chúng. Reader có thể suy ra quỹ đạo thô bằng cách đọc V1→V19 theo thứ tự tuổi.

3. **Tiến trình không đồng đều hiện rõ**. Ở 6 tháng, một trẻ có V1 (L0 reflex vẫn hoạt động nếu bị giật mình), V4 (L1-L2 smooth pursuit), V5 (L2-L3 social smile), V11 (L2 object permanence VoE), V13 (L3 gaze following). **Các sự kiện khác nhau ở các ladder levels khác nhau đồng thời**. Đây là Property 3 của plan §0.7.3 đang vận hành.

---

> *[Phase C hoàn thành — §4 (7 milestones) + §5 (Master Table 19 events + 2 worked examples). Phase D tiếp theo: §6-§12.]*

---

## §6 — Multi-Modal Binding (Thành Phần Thị Giác) — Đóng Góp Nút Thắt 3

> Chunks thị giác bind với chunks từ các modalities khác để tạo thành multi-modal chunks. Section này bao gồm **phía thị giác** của multi-modal binding. Verdict đầy đủ Nút Thắt 3 trong [07-Social-Recognition-Arc.md](07-Social-Recognition-Arc.md) §6 dùng social smile (E12) như exemplar multi-modal sạch nhất.

### §6.1 — Thị giác + thính giác binding (social smile E12)

🟢 **Sự kiện**: Social smile xuất hiện ở 6-8 tuần. Trẻ cười để phản ứng với kết hợp khuôn mặt + giọng (không hiệu quả với khuôn mặt đơn thuần trong nhiều tuần, không hiệu quả với giọng đơn thuần). ([Feel-Example E12](../../Body-Base/Feeling/Feel-Example-Draft.md#e12) dòng 758.)

🟡 **Framework claim**: Social smile là **sự kiện multi-modal binding quy mô lớn được ghi lại đầu tiên** trong arc F1 — thị giác (khuôn mặt) + thính giác (giọng) + interoceptive (trạng thái bình tĩnh baseline) → output chunk nụ cười thống nhất.

**Bằng chứng quan trọng từ trẻ mù**: Trẻ mù cũng phát triển social smile ở khoảng cùng tuổi (~8 tuần) nhưng dùng **thính giác + xúc giác** thay vì thị giác. Điều này xác nhận rằng multi-modal binding chunk không phải "face-driven hardware" mà là **binding học được của bất kỳ kênh đầu vào nào có sẵn**. (Feel-Example E12 §Notes dòng 775-779.)

**Tại sao 6-8 tuần cụ thể**: Không phải PFC maturation timeline. Đó là thời gian cần thiết cho:
- Visual face chunks compile (V1 CONSPEC → V2 individuation vào 2-4 tuần)
- Auditory voice chunks tăng cường (đã được seed trước sinh theo [02](02-Womb-to-Birth-Baseline.md) §4.1)
- Tiếp xúc đồng thời (khuôn mặt + giọng xảy ra cùng nhau trong quá trình cho ăn, nhiều lần lặp)
- Binding chunk compile (cơ chế compile driven-repetition)

🟡 **Ladder**: L2-L3 cho bind event, L3 cho smile output (Feel-Example phân loại là Resonance Stage 1).

### §6.2 — Thị giác + interoceptive binding (mother recognition E15)

🟢 **Sự kiện**: Mother recognition ở 5 tháng (§3.4 V12) bind khuôn mặt thị giác với:
- Auditory voice (từ trước sinh)
- Smell/olfactory chunks (compile từ cho bú)
- Warmth/body comfort chunks
- Comfort history chunks (no ăn, soothing)

🟡 **Framework claim**: Đây là **chunk phong phú modality nhất** trong năm đầu F1 (6+ modalities). Mất 5 tháng để compile mặc dù bắt đầu từ ngày 1 vì mỗi binding modality-pair cần lặp đi lặp lại + binding cross-modality cần đồng thời xảy ra lặp đi lặp lại của tất cả modalities cùng lúc.

Các cơ chế compile candidates (plan §0.7 + [Schema/Chunk.md](../../Body-Base/Schema/Chunk.md) §2):
- **Repetition (LTP)** — cơ chế chính. Hàng trăm sự kiện cho ăn/soothing cung cấp lặp đi lặp lại lớn.
- **Emotional peak** — phần thưởng cho ăn là valence peak tích cực, tagging chunk.
- **Multi-modal binding** — đồng thời xảy ra qua các modalities.
- **Sleep consolidation** — chunks tổ chức lại qua đêm (Diekelmann & Born 2010).

### §6.3 — Thị giác + motor binding (visuomotor reaching)

🟢 **Sự kiện**: Với tay được hướng dẫn bằng thị giác ở 4-5 tháng (§4.3 V10) bind visual target chunks với arm motor chunks. **Visuomotor chunk đầu tiên tự nguyện**.

🟡 **Framework claim**: Visuomotor binding là substrate cho hầu như tất cả tool-use và object-manipulation chunks sau đó. Đây là **platform mà hand-object chunks** compile trong năm thứ hai. Xem [05-Motor-Output-Arc.md](05-Motor-Output-Arc.md) §2.4 để xử lý đầy đủ.

### §6.4 — Thị giác + xã hội + motor + chú ý binding (joint attention E18)

🟢 **Sự kiện**: Joint attention triadic ở 9-12 tháng (§4.6 V17) là **chunk multi-modal multi-body-input đỉnh cao** của năm đầu F1. Tích hợp thị giác + thính giác + motor + xã hội + chú ý + tiền-theory-of-mind.

🟡 **Framework implication**: Joint attention chunks là **binding** — chúng liên kết chunks từ mọi hệ thống body-input ngoại trừ interoceptive. Đây là lý do tại sao Tomasello lập luận joint attention là keystone cho ngôn ngữ và học tập văn hóa sau đó: một khi trẻ có thể phối hợp sự chú ý qua agents + vật thể, word-object referencing (language grounding) trở nên khả thi.

### §6.5 — Mechanism candidates cho binding (một phần)

🟡 **Câu hỏi framework**: Cơ chế thần kinh cho cross-modal binding là gì? Candidates:

- **Temporal co-occurrence binding** (kiểu Hebb) — các tính năng firing cùng nhau tại cùng thời điểm wire lại với nhau. Có thể cho short-latency binding (khuôn mặt thị giác + giọng nghe đồng thời).
- **Multi-sensory convergence neurons** — các tế bào trong superior temporal sulcus, superior colliculus, và fusiform area đáp ứng với đầu vào multi-modal. Tìm thấy ở trẻ sơ sinh và người lớn. Stein & Meredith 1993.
- **Sleep-consolidated associative binding** — tổ chức lại bộ nhớ qua đêm + liên kết associative (Tononi & Cirelli 2014).
- **Emotional tag binding** — các trạng thái valence cao tạo ra liên kết associative mạnh qua các modalities xảy ra cùng nhau trong trạng thái (Phelps & LeDoux 2005).

F1 KHÔNG commit vào mechanism winner ở đây — [07-Social-Recognition-Arc.md](07-Social-Recognition-Arc.md) §6 (ngôi nhà chính của Nút Thắt 3) sẽ drill verdict dùng social smile như trường hợp sạch nhất. Đóng góp của file này là **compile các sự kiện phía thị giác mà bất kỳ cơ chế nào cũng phải giải thích**.

---

## §7 — Mapping Compile Mechanisms cho Chunks Thị Giác

> Plan §0.7 + [Chunk.md](../../Body-Base/Schema/Chunk.md) §2 xác định 4 chunk compile mechanisms. Section này map từng cơ chế vào quỹ đạo chunks thị giác.

### §7.1 — Repetition (compile dựa trên LTP)

**Dominant cho**: Ổn định face chunks (CONSPEC → individual faces → khuôn mặt mẹ), object file chunks, color chunks, gaze following chunks.

**Bằng chứng**: Mỗi trẻ nhận hàng nghìn lần nhìn khuôn mặt mỗi ngày. Repetition drives LTP stabilization (Bliss & Lømo 1973 seminal LTP work). Chunks compile tỉ lệ với tần suất tiếp xúc × tỷ lệ đồng thời xảy ra.

**Framework claim**: Đây là **cơ chế compile chính cho visual chunks** vì đầu vào thị giác dày đặc, tần suất cao, và tồn tại liên tục từ ngày 1.

### §7.2 — Emotional peak tagging

**Dominant cho**: Mother face chunk (+ feeding reward valence), stranger anxiety (+ fear valence), joint attention (+ shared-experience reward).

**Bằng chứng**: Emotional peaks từ cho ăn, soothing, đau khổ tạo ra associative tags mạnh trên các đầu vào thị giác đồng thời xảy ra. Amygdala + hippocampus consolidation (Phelps & LeDoux 2005, McGaugh 2000).

**Framework claim**: Emotional tagging tăng tốc chunk compile ngoài những gì repetition thuần túy sẽ dự đoán. Khuôn mặt mẹ compile nhanh hơn khuôn mặt cha một phần vì mẹ được liên kết nhiều hơn với cho ăn (valence peak tích cực mạnh).

### §7.3 — Multi-modal binding

**Dominant cho**: Social smile E12, mother recognition E15, joint attention E18, visuomotor reaching.

Được bao gồm trong §6. Cơ chế binding bản thân là compile mechanism — nó tạo ra cross-modal chunks không thể hình thành từ repetition single-modality đơn thuần.

### §7.4 — Sleep consolidation

**Dominant cho**: Tổ chức lại visual chunk qua đêm. Trẻ sơ sinh ngủ ~16 giờ/ngày trong vài tháng đầu; giấc ngủ dày REM trong thời thơ ấu sớm (gần 50% REM vs người lớn 20%, Roffwarg et al. 1966). REM được liên kết cụ thể với consolidation hệ thống thị giác.

**Bằng chứng**: Gomez et al. 2006 — học từ trẻ sơ sinh được hưởng lợi từ giấc ngủ. Walker 2017 về sleep + memory consolidation. Infant visual perceptual learning được hưởng lợi từ giấc ngủ (Friedrich et al. 2015).

**Framework claim**: Sleep là **hidden compile engine** cho visual chunks. Tiếp xúc hàng ngày cung cấp nguyên liệu thô; sleep consolidates + binds + organizes. Điều này đặc biệt liên quan cho multi-modal binding vì cross-modality associations hình thành trong offline replay (Diekelmann & Born 2010).

### §7.5 — Summary table

| Loại chunk | Cơ chế compile chính | Cơ chế hỗ trợ |
|---|---|---|
| CONSPEC face template | Bẩm sinh (không compile) | — |
| Individual face chunks | Repetition | Emotional tagging |
| Mother face chunk | Multi-modal binding + emotional peak | Repetition, sleep |
| Object file chunks | Repetition | Multi-modal binding (khi áp dụng) |
| Object permanence | Repetition + prediction-error driven | Sleep consolidation |
| Gaze following | Repetition + imitation + social reward | Emotional tagging |
| Joint attention | Multi-modal binding | Emotional tagging + social reward |

---

## §8 — Kết Nối Cross-Body-Input

> Chunks thị giác không tồn tại độc lập. Section này map các binds thị giác ↔ body-input khác để F1 cross-referencing.

### §8.1 — Thị giác ↔ Thính giác

**Các binds chính**:
- Khuôn mặt ↔ giọng (social smile E12, §6.1)
- Khuôn mặt mẹ ↔ giọng mẹ (E15)
- Vật thể ↔ âm thanh vật thể (bóng nảy + tiếng bịch)
- Khuôn mặt ↔ speech streaming (nhận dạng tên, xem [04-Auditory-System-Arc.md](04-Auditory-System-Arc.md) §3.6 V2-Aud integration)

### §8.2 — Thị giác ↔ Motor

**Các binds chính**:
- Với tay được hướng dẫn bằng thị giác (§4.3, V10) → nền tảng
- Gaze following (§4.4, V13) → coordinated eye motor
- Joint attention (§4.6, V17) → phối hợp tay + nhìn + look
- Imitation (gestures, biểu cảm khuôn mặt, hành động)

Xem [05-Motor-Output-Arc.md](05-Motor-Output-Arc.md) §6.1 để xử lý phía motor.

### §8.3 — Thị giác ↔ Interoceptive

**Các binds chính**:
- Khuôn mặt mẹ ↔ trạng thái thoải mái/warmth (E15)
- Khuôn mặt người lạ ↔ trạng thái sợ/đau khổ (E16)
- Khuôn mặt peek-a-boo trở về ↔ positive arousal (anticipation liên quan E18)

Đây là **các visual chunks được emotional-tagged**. Xem [06b-Interoceptive-Other-States.md](06b-Interoceptive-Other-States.md) để xử lý đầy đủ + [07-Social-Recognition-Arc.md](07-Social-Recognition-Arc.md) §4 để drill bind E15.

### §8.4 — Thị giác ↔ Xã hội

Hầu như mọi milestone xã hội thị giác (CONSPEC, direct gaze, mother recognition, social smile, gaze following, joint attention) là một **visual-social chunk bind**. Arc xã hội trong [07-Social-Recognition-Arc.md](07-Social-Recognition-Arc.md) phụ thuộc nặng vào visual chunks như anchoring modality.

**Quan sát framework**: Vision là **anchoring modality chính cho social chunks trong phát triển điển hình**. Trẻ mù đạt được các milestones xã hội dùng anchoring thay thế (thính giác + xúc giác) nhưng có phần chậm hơn (Fraiberg 1977).

### §8.5 — Thị giác ↔ Verbal (preview, đầy đủ trong 08)

**Visual chunks như receptive grounding cho words**:
- Word-object mapping yêu cầu stable object file chunks (compile vào 4-6 tháng, §3.7)
- Word-face mapping yêu cầu individual face chunks (compile vào 5 tháng, §3.4)
- Common noun comprehension (Bergelson & Swingley 2012) ở 6-9 tháng yêu cầu cả visual object chunks + auditory word chunks + cross-modal binding
- Xử lý đầy đủ trong [08-Verbal-Production-Arc.md](08-Verbal-Production-Arc.md) §3

**Receptive-productive gap** (preview Nút Thắt 5): Trẻ hiểu "mẹ" vào 6-9 tháng (visual face chunk + auditory word chunk + bind) nhưng không sản xuất "mẹ" cho đến ~12-18 tháng. Phía comprehension được xây dựng chủ yếu trên visual chunks. Đây là một trong những asymmetries "knowing vs acting" qua F1 — được bao gồm trong Nút Thắt 5, ngôi nhà chính [08-Verbal-Production-Arc.md](08-Verbal-Production-Arc.md).

---

## §9 — Đóng Góp Nút Thắt

> Drill F1 hội tụ về 7 nút thắt (plan §0.6). File này đề cập hai.

### §9.1 — Nút Thắt 1 — Proto-chunk gradient vs rời rạc (đóng góp một phần)

**Đóng góp của file này**: Object file chunks (§3.7-§3.8) và object permanence chunks cung cấp một **visual system test case** cho câu hỏi gradient vs rời rạc.

**Bằng chứng cho gradient**:
- Baillargeon ngạc nhiên 2.5 tháng với trajectory bất khả thi (rất cơ bản)
- 3.5 tháng: solidity bất khả thi (thuộc tính cụ thể)
- 4-6 tháng: các kịch bản permanence phức tạp hơn
- 8-9 tháng: permanence dựa trên hành động (reaching vào vị trí ẩn)
- 12+ tháng: lý luận permanence phức tạp hơn

Đây không phải một công tắc "object permanence có mặt/vắng mặt" rời rạc duy nhất. Chúng là **sub-chunks được elaborated dần dần** (solidity, trajectory, continuity, identity), mỗi cái tăng cường theo tốc độ riêng theo tiếp xúc + compile dynamics.

**Visual arc verdict preview**: Quan điểm gradient được hỗ trợ bởi dữ liệu thị giác. Mỗi sub-property của "object permanence" compile bán độc lập. Điều này phù hợp với **gradient early-LTP → late-LTP** ở cấp sinh học (Bliss & Lømo 1973, Abraham & Williams 2008 late-LTP review).

**Verdict đầy đủ**: Được deferred đến [04-Auditory-System-Arc.md](04-Auditory-System-Arc.md) §6 (phân biệt phoneme cung cấp bằng chứng gradient thậm chí sạch hơn) + [10-F1-Synthesis.md](10-F1-Synthesis.md) synthesis.

### §9.2 — Nút Thắt 3 — Multi-modal binding mechanism (đóng góp một phần)

**Đóng góp của file này**: Compile bằng chứng phía thị giác cho multi-modal binding events (§6):
- Social smile E12 như bind quy mô lớn đầu tiên
- Mother recognition E15 như bind multi-modal-rich
- Joint attention E18 như bind multi-body-input
- Visuomotor reaching như vision+motor anchor

**Mechanism candidates** (§6.5): Temporal co-occurrence kiểu Hebb, multi-sensory convergence neurons, sleep consolidation, emotional tagging.

**Verdict đầy đủ**: Được deferred đến [07-Social-Recognition-Arc.md](07-Social-Recognition-Arc.md) §6 (social smile là trường hợp sạch nhất cho mechanism drill) + [10-F1-Synthesis.md](10-F1-Synthesis.md).

### §9.3 — Đề cập ngắn gọn các nút thắt khác

- **Nút Thắt 2 (P2 Chunks Base Adequacy)**: Visual chunks là **hệ thống body-input compile nhanh nhất** vì đầu vào thị giác dày đặc nhất. Visual adequacy xuất hiện tương đối sớm (nhiều sự kiện đã ở L3-L4 vào 12 tháng). Tương phản với interoceptive (bàng quang) vốn lag đáng kể. Sự khác biệt tốc độ cross-body-input này là bằng chứng quan trọng cho Nút Thắt 2 "tỷ lệ compile khác nhau theo saliency đầu vào + tần suất lặp lại + contingency" — xem [06a-Interoceptive-Bladder-Keystone.md](06a-Interoceptive-Bladder-Keystone.md).
- **Nút Thắt 4 (PFC hardware × chunks missing)**: Đã committed trong 01 — file này áp dụng reframe nhất quán xuyên suốt. Direct gaze ở 2-5 ngày (§3.2) là một trong những bằng chứng visual falsification mạnh nhất cho quan điểm cũ "PFC offline".

---

## §10 — Câu Hỏi Mở

🟡 **Câu hỏi mở** file này phát sinh hoặc để lại cho file downstream:

1. **CONSPEC có chứa direct-gaze subcomponent không, hay phát hiện direct gaze được compile trong 2-5 ngày đầu tiên?** Timing quá sớm cho pure post-birth learning nhưng lập luận tiến hóa cho pre-wiring bẩm sinh là framework claim, không phải bằng chứng giải phẫu trực tiếp. Mở — cần developmental neuroscience tốt hơn.

2. **Số lần tiếp xúc tối thiểu để compile một visual chunk là bao nhiêu?** Khuôn mặt mẹ có thể phân biệt ở 4 ngày (Bushnell 1989) — có bao nhiêu sự kiện feeding-face-view rời rạc trong 4 ngày? Có thể là 50-100 episode × phút tiếp xúc khuôn mặt. Chúng ta có thể định lượng "compile threshold" chính xác hơn không?

3. **Tại sao stereopsis xuất hiện rời rạc (3-4 tháng) trong khi các visual chunks khác xuất hiện gradient?** Sự khác biệt substrate (binocular cell tuning + vergence) có thể giải thích. Đây là trường hợp **gradient vs rời rạc distinction (Nút Thắt 1)** có bằng chứng hỗn hợp trong chính hệ thống thị giác — hầu hết chunks gradient, nhưng stereopsis có vẻ rời rạc. Thú vị.

4. **Visuomotor reaching (4-5 tháng) được phân loại tốt nhất là L2 hay L3?** Reaching **attempt** là L3 (thành phần hành động) nhưng độ chính xác kém trong nhiều tuần sau khi xuất hiện lần đầu. Phân loại phụ thuộc vào "phối hợp" cần thiết bao nhiêu cho thực thi. Điều này có thể chỉ ra rằng ladder levels có graduation nội bộ.

5. **Visual chunks cho causality** (một vật thể phóng vật thể khác — Michotte perception) — những cái này compile khi nào? Leslie 1984, Oakes 1994 cho thấy ~7-9 tháng. Nơi nào trong visual arc cái này phù hợp? Được đề cập một phần trong [09-Event-Chunks-Inference-Matrix.md](09-Event-Chunks-Inference-Matrix.md).

6. **Biến thể xuyên văn hóa của mirror self-recognition**: pass sớm hơn trong các mẫu WEIRD phương Tây hơn một số mẫu non-WEIRD (Broesch et al. 2011). Hàm ý framework: timing visual self chunk bị **điều chỉnh văn hóa**, không phải lịch trình sinh học phổ quát. Điều thay đổi là gì — visual self-concept chunks hay chỉ hành vi mirror test-taking?

7. **Autism spectrum gaze-following và joint attention delay**: được biết đến là early marker (Klin et al. 2002). Câu hỏi framework: chunks nào đang compile chậm — visual chunks, binding chunks, social reference chunks, hay motivational/reward chunks cho việc chú ý đến khuôn mặt? Mở — hàm ý lâm sàng downstream của F1 framework.

---

## §11 — Cross-References

### §11.1 — Trong F1 Child-Chunk-Development

- [00-Chunk-System-Sketch.md](00-Chunk-System-Sketch.md) — định hướng sub-folder F1
- [01-PFC-Hardware-Reframe.md](01-PFC-Hardware-Reframe.md) — §6 quy tắc phương pháp luận event-inference được dùng xuyên suốt, §7 ba worked examples (logic song song)
- [02-Womb-to-Birth-Baseline.md](02-Womb-to-Birth-Baseline.md) — §9.1 baseline state tại t=0, §4 thư viện prenatal chunks, §7.4 Q&A thị giác trẻ sơ sinh
- [04-Auditory-System-Arc.md](04-Auditory-System-Arc.md) (drill tiếp theo) — Nút Thắt 1 primary verdict + auditory-visual binds (social smile, mother recognition)
- [05-Motor-Output-Arc.md](05-Motor-Output-Arc.md) (drill tiếp theo) — visuomotor reaching drilled motor-side, pointing + gesture motor-side
- [06a-Interoceptive-Bladder-Keystone.md](06a-Interoceptive-Bladder-Keystone.md) (pending) — contrast case (hệ thống compile-chậm vs visual fast-compile)
- [07-Social-Recognition-Arc.md](07-Social-Recognition-Arc.md) (pending) — ngôi nhà chính Nút Thắt 3, mother recognition + joint attention full drill
- [08-Verbal-Production-Arc.md](08-Verbal-Production-Arc.md) (pending) — visual grounding cho word-object mapping
- [09-Event-Chunks-Inference-Matrix.md](09-Event-Chunks-Inference-Matrix.md) (pending) — event table synthesis cross-cutting
- [10-F1-Synthesis.md](10-F1-Synthesis.md) (pending) — verdicts cuối 7 nút thắt bao gồm đóng góp của file này

### §11.2 — Framework upstream

- [../../Body-Base/Schema/Chunk.md](../../Body-Base/Schema/Chunk.md) — định nghĩa chunk substrate + 4 compile mechanisms
- [../../Imagination/PFC-Analysis.md](../../Imagination/PFC-Analysis.md) §4.0 — PFC reframe (edited N+4 prep)
- [../../Modality-Analysis.md](../../Modality-Analysis.md) §2.1.1 Visual — mô tả visual modality

### §11.3 — Drilled sub-folders (cross-reference)

- [../Learning-Cycle/Learning-Cycle.md](../Learning-Cycle/Learning-Cycle.md) — H8 learning dissonance cycle dùng chunks, visual learning cycles áp dụng được (object permanence violation → learning)
- [../Agent/Agent.md](../Agent/Agent.md) + [../Agent/Self-Pattern-Modeling.md](../Agent/Self-Pattern-Modeling.md) — H9 Agent formation dùng visual self-chunks (mirror recognition ở 18-24 tháng là substrate cho Self-Pattern-Modeling Stage 2)
- [../Body-Feedback-Draft/01-Foundation.md](../Body-Feedback-Draft/01-Foundation.md) — H10 body-feedback substrate, §5.4 caregiver mirroring như developmental foundation. Visual mirroring events (khuôn mặt mẹ, smile contagion) là cơ chế cho infant interoception development.
- [../Body-Feedback-Draft/04-Integration.md](../Body-Feedback-Draft/04-Integration.md) — H10 P2 Chunks Base Adequacy bottleneck. Tích lũy visual chunks của file này đóng góp bằng chứng fast-compile.

### §11.4 — Empirical Feel-Example cross-references

- [E12 Social smile 6-8 tuần](../../Body-Base/Feeling/Feel-Example-Draft.md#e12) — multi-modal bind exemplar đầu tiên (§6.1)
- [E13 Smile contagion 4 tháng](../../Body-Base/Feeling/Feel-Example-Draft.md#e13) — cơ chế visual smile pattern-match
- [E14 Gaze following 6 tháng](../../Body-Base/Feeling/Feel-Example-Draft.md#e14) — §4.4
- [E15 Mother recognition 5 tháng](../../Body-Base/Feeling/Feel-Example-Draft.md#e15) — §3.4 + §6.2 multi-modal identity chunk
- [E16 Stranger anxiety 8 tháng](../../Body-Base/Feeling/Feel-Example-Draft.md#e16) — visual categorization qua familiar library
- [E17 Separation distress 9 tháng](../../Body-Base/Feeling/Feel-Example-Draft.md#e17) — visual permanence + temporal absence chunks
- [E18 Joint attention 10 tháng](../../Body-Base/Feeling/Feel-Example-Draft.md#e18) — §4.6 L4 capstone visual event
- [E19 Social referencing 10-12 tháng](../../Body-Base/Feeling/Feel-Example-Draft.md#e19) — visual face reading để ra quyết định

---

## §12 — Status

**Draft status**: DRAFT N+4b Phase F1-P6 — bản dịch tiếng Việt hoàn chỉnh, sẵn sàng cho user review.

**Sections hoàn chỉnh**: §0 đến §11 (12 sections).

**Line count**: ~900 dòng (target 1000-1200L).

**Các cam kết framework được thực hiện**:
- ✅ Quy tắc phương pháp luận event-inference (01 §6) được tuân theo xuyên suốt
- ✅ Không có claim "PFC trưởng thành ở tuổi X"
- ✅ PFC-Inference Ladder áp dụng cho tất cả 19 V-table events
- ✅ Plausibility qualifiers 🟢🟡🔴 được áp dụng
- ✅ Baseline state từ 02 §9.1 được cite
- ✅ Feel-Example E12/E14/E15/E18 được referenced với số dòng
- ✅ Cross-references bidirectional với 00 + 01 + 02 + drilled sub-folders
- ✅ KHÔNG có personal examples (quy tắc framework)
- ✅ Tiếng Việt primary + English technical terms
- ✅ Xưng hô "bạn-tôi" (file này chủ yếu neutral framing)
- ✅ "Imagine-Final" không dùng trong file này (chủ đề không áp dụng)

**Đóng góp Nút Thắt**:
- Nút Thắt 1 một phần — bằng chứng gradient object permanence
- Nút Thắt 3 một phần — phía thị giác của multi-modal binding events

**Tiến độ dịch**: 4/12 files hoàn chỉnh (00, 01, 02, 03).

**Bước tiếp theo**: User review → nếu approved, tiến hành drill [04-Auditory-System-Arc.md](04-Auditory-System-Arc.md) (⭐ Nút Thắt 1 primary verdict).

**Review checkpoint**: Per plan §5.5, file này là optional review (mandatory review sau 04). User có thể skip đến 04 nếu hài lòng, hoặc giữ để review trước.

---

> **03-Visual-System-Arc-VI.md — Kết thúc file.**
>
> F1 body-input arc #1 trên 6. Chunks thị giác được truy dấu từ CONSPEC substrate trước sinh qua joint attention L4 ở 9-12 tháng đến mirror self-recognition L4 ở 18-24 tháng. Phương pháp luận event-inference được áp dụng xuyên suốt. Hai nút thắt được đề cập một phần (1 + 3), verdict cuối pending ở synthesis stage. Bản dịch tiếng Việt hoàn chỉnh với 19 V-events được phân tích đầy đủ.


