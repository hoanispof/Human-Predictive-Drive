---
title: Motor Output Developmental Arc — F1 Body-Input Arc #3 (Tay + Di chuyển)
file: 05-Motor-Output-Arc-VI.md
source: 05-Motor-Output-Arc.md (bản gốc tiếng Anh)
created: 2026-04-16 (Session N+4b, Phase F1-P8)
status: DRAFT N+4b P8 — bản dịch tiếng Việt hoàn chỉnh
scope: Hệ thống motor đầu ra (fine motor tay + locomotion cơ thể + giao tiếp gesture) từ khi sinh đến ~24 tháng, phân tích qua các giai đoạn Connect → Control với PFC-Inference Ladder. Giai đoạn Read hạn chế cho motor thuần túy.
parent: plan.md §3.2 (file 05 outline)
depends_on: [01-PFC-Hardware-Reframe.md, 02-Womb-to-Birth-Baseline.md, 03-Visual-System-Arc.md, 04-Auditory-System-Arc.md]
language: Tiếng Việt primary + English technical terms
addresses:
  - Nút Thắt 5 preview (H11 Receptive-Productive Asymmetry — phía productive gesture, phía verbal trong 08)
  - Nút Thắt 6 preview (labeling attachment — gesture như alternative handle cho verbal)
sub_folder: F1 Child-Chunk-Development
translation_note: Bản dịch tiếng Việt hoàn chỉnh. Giữ nguyên thuật ngữ kỹ thuật tiếng Anh, citation, tên file, parameter, emoji.
---

# 05 — Motor Output Developmental Arc

> **File 05 trong F1 Child-Chunk-Development sub-folder.** Đây là arc body-input thứ ba trong sáu file. File này truy dấu cơ chế compile chunks hệ thống motor đầu ra từ **các reflex sơ sinh** qua **đi bộ + giao tiếp gesture** ở ~24 tháng sau sinh. Không giống thính giác (04) nơi hệ thống thiên về receptive, motor là **output-dominant** — các chunks tạo ra hành động cơ thể thay vì phát hiện đầu vào. Điều này tạo ra một bất đối xứng đặc biệt mà file này khai thác.

---

## §0 — Tóm Tắt

🟢🟡 **Claim**: Motor chunks compile qua 0-24 tháng trong hai arc xen kẽ — **hand motor** (palmar reflex → proto-declarative pointing → tool use) và **locomotion** (head control → đi bộ). Cả hai arc đều dựa trên substrate chung (motor cortex + cerebellum + basal ganglia + spinal circuits) nhưng compile ở **các tỷ lệ khác nhau tùy thuộc vào khả dụng của visuomotor feedback**. Hand arc được coupled chặt chẽ hơn với visuomotor (visual feedback phong phú cho mỗi hành động); locomotion arc được coupled hơn với proprioceptive-vestibular (thị giác đóng vai trò hỗ trợ nhưng không phải chính cho cân bằng).

Hệ thống motor đặc biệt hướng dẫn cho F1 theo một cách cụ thể: **motor chunks bắc cầu giữa phía receptive và productive**. Hầu hết các milestones receptive F1 (thị giác, thính giác, interoceptive) xảy ra trước các đối tác sản xuất motor của chúng. **Khoảng cách giữa receptive và productive** — được formalize như H11 Receptive-Productive Asymmetry — biểu hiện rõ nhất khi các chunks motor đầu ra của một hệ thống cơ thể lag phía sau các chunks receptive tương ứng của nó. Giao tiếp gesture xuất hiện ở ~14 tháng (E25) với các chunks cụ thể need-to-gesture **trước** khi các nhãn verbal cho cùng nhu cầu xuất hiện ở ~18-22 tháng (E21, E22, E23). Điều này cho chúng ta một **khoảng cách gesture-verbal ~4-8 tháng trong cùng hệ thống motor productive** — một test sạch within-body-input của H11.

**Các sự kiện được phân tích (preview master table — đầy đủ trong §4)**:

| Sự kiện | Tuổi | Arc | Ladder | Nghiên cứu |
|---|---|---|---|---|
| Palmar grasp reflex (E7) | Khi sinh | Hand | L0 🟢 | Tiêu chuẩn nhi khoa |
| Rooting + sucking (E8) | Khi sinh | Miệng | L0 🟢 | Tiêu chuẩn nhi khoa |
| Head control | 2-4 tháng | Loco | L1-L2 🟢 | Bayley Scales |
| Hand-to-mouth chủ ý | 2-3 tháng | Hand | L1-L2 🟡 | Rochat 1989 |
| Vung vào vật thể | 3 tháng | Hand | L2 🟡 | von Hofsten 1982 |
| Lật người | 4-6 tháng | Loco | L2-L3 🟢 | Bayley Scales |
| Với tay có hướng dẫn thị giác | 4-5 tháng | Hand | L3 🟢 | von Hofsten 1979, 1984 |
| Nắm tay đầy đủ | 5-6 tháng | Hand | L3 🟢 | được ghi chép rộng rãi |
| Ngồi độc lập | 6-7 tháng | Loco | L3 🟢 | Bayley Scales |
| Bò | 7-9 tháng | Loco | L3 🟢 | được ghi chép rộng rãi |
| Pincer grasp | 9-10 tháng | Hand | L3-L4 🟢 | Halverson 1931 |
| Proto-imperative pointing | 9-10 tháng | Hand | L3 🟢 | Bates et al. 1975 |
| Kéo đứng | 9-10 tháng | Loco | L3 🟢 | Bayley Scales |
| Proto-declarative pointing | 12-14 tháng | Hand | L4 🟢 | Bates et al. 1975, Tomasello 1995 |
| Bước đi đầu tiên | 10-14 tháng | Loco | L3-L4 🟢 | được ghi chép rộng rãi |
| Đi bộ | 12-15 tháng | Loco | L4 🟢 | Bayley Scales |
| Gesture chủ ý cho nhu cầu (E25) | 12-14 tháng | Hand | L4 🟢 | Goodwyn et al. 2000 |
| Tool use / manipulation | 12-18 tháng | Hand | L4 🟢 | Piaget 1952, Bruner 1973 |
| Delayed imitation | 14-18 tháng | Hand+body | L4 🟢 | Meltzoff 1988 |
| Chạy | 18-24 tháng | Loco | L4 🟢 | Bayley Scales |

**Hai nút thắt preview**:

1. **Nút Thắt 5 preview** — phía productive gestural của H11 (§7). Verdict đầy đủ trong [08-Verbal-Production-Arc.md](08-Verbal-Production-Arc.md).
2. **Nút Thắt 6 preview** — alternative handle (gesture như chunk-label không cần lời) (§7.3). Verdict đầy đủ trong [08-Verbal-Production-Arc.md](08-Verbal-Production-Arc.md).

---

## §1 — Vị Trí Trong F1

### §1.1 — Motor là "action side" của F1

Sáu body-input arcs của F1 chia thành hệ thống thiên về receptive (thị giác, thính giác, interoceptive) và hệ thống thiên về production (motor, verbal). Xã hội là cross-cutting. Motor là **thuần productive nhất** trong các body-input arcs của F1 — các chunks của nó tạo ra hành động, không phát hiện đầu vào.

Điều này có hai hệ quả phương pháp luận:

1. **Phân loại Ladder lệch cao hơn**. Các sự kiện motor có liên quan đến hành động, vì vậy hầu hết đạt ít nhất L3 (hành động phối hợp thô). Các sự kiện motor L2 hiếm (pattern-match không có hành động theo định nghĩa nghĩa là không có motor output). Các sự kiện motor L0 là các reflex sơ sinh. Các sự kiện motor L1 là các chuyển động phản ứng post-hoc.

2. **Receptive-productive gap có thể nhìn thấy trong chính motor**. Em bé có thể có ý định với tay để lấy vật thể (phía nhận thức/thị giác) lâu trước khi việc với tay thành công (phía motor). Các chunks visuomotor mapping phải compile trước khi ý định được dịch thành hành động chính xác. Bất đối xứng within-motor này là phiên bản nhỏ hơn của bất đối xứng H11 Nút Thắt 5 rộng hơn.

### §1.2 — Hai arc với các milestones xen kẽ

Phát triển motor được hiểu tốt nhất như **hai arc song song** trên substrate chung:

**Hand arc**: fine motor, coupled visuomotor, thao tác, cuối cùng là giao tiếp (pointing, gesturing, tool use). Tích hợp nặng với visual chunks (03) + sau đó với verbal chunks (08).

**Locomotion arc**: gross motor, coupled proprioceptive-vestibular, driven bởi cân bằng, cuối cùng cho phép khám phá độc lập. Tích hợp nặng với interoceptive (cân bằng, nỗ lực) + environmental chunks.

**Tại sao phân biệt**: hai arc compile ở các tỷ lệ độc lập một phần. Một em bé có thể nâng cao về hand arc trong khi trung bình về locomotion arc (hoặc ngược lại). Đây là bằng chứng rằng **motor chunks đặc hiệu với từng bộ phận cơ thể**, không phải một trục "sự trưởng thành motor" duy nhất. Song song với Property 3 không đồng đều của plan §0.7.3.

### §1.3 — Dependencies với các file trước

**Từ [01-PFC-Hardware-Reframe.md](01-PFC-Hardware-Reframe.md)**:
- §6 quy tắc phương pháp luận event-inference — được tuân theo xuyên suốt §4 master table
- §7.3 worked example "giao tiếp bình thường" — file này mở rộng phân tích gesture-verbal gap

**Từ [02-Womb-to-Birth-Baseline.md](02-Womb-to-Birth-Baseline.md)**:
- §9.1 baseline state tại t=0 — "motor chunks cho môi trường chịu trọng lực ❌" khi sinh là điểm xuất phát mà file này biện minh sự mở rộng từ đó
- §3.3 hoạt động motor trước sinh — thai nhi có các pattern motor trong tử cung (đá, mút ngón tay, tiểu tiện thai nhi 10-14 tuần); arc sau sinh bắt đầu từ các hạt giống motor trước sinh này

**Từ [03-Visual-System-Arc.md](03-Visual-System-Arc.md)**:
- §4.3 visually guided reaching — phía motor được xử lý ở đây (§2.4 dưới đây)
- §4.4 gaze following + §4.6 joint attention — phía motor cho pointing + gaze coordination
- §6.3 visuomotor binding — tham chiếu cơ chế

**Từ [04-Auditory-System-Arc.md](04-Auditory-System-Arc.md)**:
- §9 receptive-productive asymmetry preview — file này mở rộng bất đối xứng sang phía productive gestural

---

## §2 — Hand Motor Arc

> Hand arc = chunks fine motor cho kiểm soát tay, với, nắm, thao tác, chỉ, gesture, dùng công cụ. Được sắp xếp theo thứ tự xấp xỉ theo tuổi xuất hiện.

### §2.1 — Palmar grasp reflex khi sinh (E7, L0)

🟢 **Sự kiện**: Trẻ sơ sinh, khi lòng bàn tay được chạm hoặc một vật được đặt vào tay, phản xạ đóng ngón tay quanh nó. Lực nắm có thể đủ mạnh để giữ ngắn tạm thời trọng lượng cơ thể trẻ sơ sinh. Có mặt từ khi sinh, thường biến mất ~3-4 tháng. ([Feel-Example E7](../../Body-Base/Feeling/Feel-Example-Draft.md#e7) dòng 391.)

🟢 **Nghiên cứu**: Khám thần kinh nhi khoa tiêu chuẩn. Peiper 1963, Prechtl & Beintema 1964, Twitchell 1970 các nghiên cứu cổ điển về reflex trẻ sơ sinh.

🟡 **Chunks yêu cầu**: Không có gì học. Mạch reflex tủy sống + dưới vỏ (primitive motor pattern).

**PFC-Inference Ladder**: **L0** 🟢. Pure reflex.

**Ghi chú framework**: Palmar grasp reflex **không phải là cùng hệ thống motor như việc nắm chủ ý sau này**. Nắm chủ ý (§2.5 dưới đây) xuất hiện khi reflex mờ đi và kiểm soát motor vỏ não tiếp quản. Reflex là **spinal/subcortical pattern**, nắm chủ ý là **compiled chunk được kiểm soát bởi vỏ não**. Cả hai đều trông giống nhau về mặt hành vi (bàn tay đóng quanh vật thể) nhưng khác biệt về cơ chế.

### §2.2 — Rooting + sucking reflex khi sinh (E8, L0)

🟢 **Sự kiện**: Trẻ sơ sinh, khi má được chạm, quay đầu về phía chỗ chạm và há miệng để mút. Có mặt từ khi sinh, tồn tại biến đổi qua các tháng đầu. ([Feel-Example E8](../../Body-Base/Feeling/Feel-Example-Draft.md#e8) dòng 427.)

🟡 **Chunks yêu cầu**: Không có gì học. Brainstem reflex cho định hướng cho ăn.

**PFC-Inference Ladder**: **L0** 🟢.

**Tại sao đưa vào**: Rooting + sucking là **miệng motor** reflex sau này trở thành substrate cho **articulatory motor chunks** (babbling, sản xuất từ). Miệng là một trong những hệ thống motor sớm nhất có kiểm soát vỏ não xuất hiện — full vocal production arc trong [08-Verbal-Production-Arc.md](08-Verbal-Production-Arc.md).

### §2.3 — Hand-to-mouth chủ ý (2-3 tháng)

🟢 **Sự kiện**: Vào 2-3 tháng, trẻ cố ý đưa tay lên miệng — không phải như reflex mà như hành động chủ ý lặp lại, thường để tự an ủi hoặc khám phá.

🟢 **Nghiên cứu**: Rochat 1989 "Self-perception and action in infancy" — mô tả hand-to-mouth như hành động được hướng dẫn proprioceptively đang xuất hiện.

🟡 **Chunks yêu cầu**:
- Chunks body-schema proprioceptive (biết bàn tay ở đâu)
- Chunks arm motor (phối hợp vai + khuỷu tay + cổ tay)
- Mouth-target motor chunk (hướng tay đến mặt)
- Repetition compile từ nhiều episode hàng ngày

**PFC-Inference Ladder**: **L1-L2** 🟡. Pattern-match trên trạng thái proprioceptive → motor output. Sự kiện chuyển tiếp — kiểm soát chủ ý đang xuất hiện.

**Tầm quan trọng framework**: Hand-to-mouth ở 2-3 tháng có thể là **motor chunk chủ ý đầu tiên** trong phát triển sau sinh — chunk đầu tiên liên kết nhận thức proprioceptive với motor output chủ ý. Đây là một mốc nhỏ nhưng quan trọng — substrate cho tất cả các motor chunks chủ ý tiếp theo.

### §2.4 — Với tay có hướng dẫn thị giác (4-5 tháng) ⭐ visuomotor bind

🟢 **Sự kiện**: Trẻ 4-5 tháng với tay đến các mục tiêu nhìn thấy với độ chính xác hợp lý. Trước 4 tháng, với tay là "pre-reaching" — các vung không phối hợp không hướng rõ ràng bởi vị trí mục tiêu thị giác.

🟢 **Nghiên cứu**:
- von Hofsten 1979 — chứng minh đầu tiên về với tay có chủ ý ở trẻ nhỏ
- von Hofsten 1982, 1984 — quỹ đạo phát triển với tay
- Clifton et al. 1993 — với tay xảy ra ngay cả trong bóng tối nếu trẻ có thông tin mục tiêu thính giác/proprioceptive, cho thấy với tay không phụ thuộc hoàn toàn vào thị giác
- Berthier & Keen 2006 — phân tích quỹ đạo với tay

🟡 **Chunks yêu cầu** (stack đáng kể):
- **Visual object location chunk** (tọa độ không gian 3D từ visual field)
- **Arm motor chunks** (các primitive phối hợp vai, khuỷu tay, cổ tay)
- ⭐ **Visuomotor binding chunk** — **coordinate transformation** từ tọa độ thị giác (retinal/3D) sang tọa độ motor (joint-angle/muscle). Đây là một trong những binding chunks then chốt trong F1.
- Hand-shape chunk (pre-shaping tay cho nắm khi cánh tay tiếp cận vật thể)
- Feedback-driven correction chunks (online error correction trong khi với tay)

**PFC-Inference Ladder**: **L3** 🟢. Hành động phối hợp, hướng mục tiêu, nhưng chưa đáng tin cậy hoàn toàn (độ chính xác cải thiện qua nhiều tháng sau khi xuất hiện đầu tiên).

**⭐ Tại sao visuomotor binding là load-bearing cho F1**:

1. **Binding quy mô lớn đầu tiên của visual + motor chunks**. Trước visuomotor reaching, thị giác và motor là các hệ thống riêng biệt — visual chunks compile độc lập (03 §3), motor chunks compile độc lập (reflexes + voluntary sớm §2.3). Ở 4-5 tháng, **binding** giữa chúng trở nên chức năng và em bé có thể hành động trên những gì họ thấy.

2. **Đóng góp visual-motor Nút Thắt 3**: đây là phía visual-motor của cơ chế multi-modal binding. Mechanism candidates: Hebbian temporal co-occurrence (với tay trong khi visual fixation tạo ra co-firing), sleep consolidation của visuomotor mappings, error-driven learning từ các lần với tay thất bại.

3. **Substrate cho tool use + manipulation**. Mọi hand-based chunk từ đây trở đi (nắm, pincer, pointing, tool use, gesturing) đều dựa trên visuomotor binding được thiết lập ở 4-5 tháng. Không có bind này, không có hand-object chunks nào có thể compile.

### §2.5 — Nắm tay đầy đủ (5-6 tháng)

🟢 **Sự kiện**: Trẻ 5-6 tháng nắm đồ vật bằng tay đầy đủ (palmar grasp, scooping bằng cả bàn tay — chưa phải pincer). Nắm chủ ý, hướng mục tiêu thay thế palmar reflex nguyên thủy (§2.1) hiện đã biến mất.

🟡 **Chunks yêu cầu**: Visuomotor reach chunks (§2.4) + grasp motor chunks (uốn cong ngón tay) + điều chỉnh grip strength + release chunks.

**PFC-Inference Ladder**: **L3** 🟢.

### §2.6 — Khám phá vật thể qua tay (5-9 tháng)

🟢 **Sự kiện**: Giữa 5 và 9 tháng, trẻ khám phá vật thể bằng cách nắm, mút, đập, chuyển tay-sang-tay, xoay, kiểm tra. Đây là **motor substrate để compile object chunks** — các visual object file chunks (03 §3.7) được làm giàu với hand-motor interaction chunks tạo ra multi-modal object chunks.

🟡 **Framework claim**: Giai đoạn này là **cửa sổ compile hiệu quả nhất** cho kiến thức vật thể hand-based. Mỗi episode tương tác vật thể compile: visual chunks (ngoại hình) + motor chunks (cách nắm) + tactile chunks (kết cấu, trọng lượng) + đôi khi auditory chunks (âm thanh từ đập) + outcome chunks (điều gì xảy ra khi bạn thao tác).

### §2.7 — Pincer grasp (9-10 tháng) — fine motor precision

🟢 **Sự kiện**: Trẻ 9-10 tháng nhặt các vật thể nhỏ (nho khô, vòng ngũ cốc) bằng cách đối lập ngón cái + ngón trỏ (pincer grasp). Đây là **fine motor precision** thay thế scooping bằng cả bàn tay cho các mục tiêu nhỏ.

🟢 **Nghiên cứu**: Halverson 1931 — taxonomi nắm cổ điển, vẫn được cite rộng rãi. Corbetta & Bojczyk 2002 — quỹ đạo phát triển.

🟡 **Chunks yêu cầu**: Visuomotor chunks cho mục tiêu nhỏ + finger-specific motor chunks (đối lập ngón cái-trỏ) + điều chỉnh grip force cho vật thể nhỏ/dễ vỡ.

**PFC-Inference Ladder**: **L3-L4** 🟢. Độ chính xác tinh hơn yêu cầu stack chunks phối hợp hơn.

**Ghi chú framework**: Tuổi pincer grasp đáng chú ý gần với tuổi proto-imperative pointing (§2.8) và xấp xỉ khi joint attention xuất hiện (03 §4.6). Các **phát triển hội tụ ở 9-12 tháng** này không phải ngẫu nhiên — chúng dựa trên cùng substrate của fine motor chunks được tinh chỉnh + social-cognitive chunks trưởng thành cùng nhau.

### §2.8 — Proto-imperative pointing (9-10 tháng)

🟢 **Sự kiện**: Trẻ 9-10 tháng bắt đầu dùng pointing ngón tay duỗi ra **để yêu cầu vật thể**. "Proto-imperative" vì nó chức năng như một yêu cầu ("cho tôi cái đó") — một speech act imperative ở dạng gestural.

🟢 **Nghiên cứu**: Bates, Camaioni & Volterra 1975 "The acquisition of performatives prior to speech" — typology cổ điển của proto-imperative vs proto-declarative pointing.

🟡 **Chunks yêu cầu**:
- Finger-extension motor chunk (hand shape: tất cả ngón cong trừ ngón trỏ duỗi)
- Arm-orientation chunk (directing cánh tay về phía mục tiêu)
- Target-identification chunk (visual chunks cho vật thể được mong muốn)
- **Adult-as-agent chunk** — hiểu rằng người lớn có thể lấy vật thể, vì vậy pointing đến người lớn mang lại vật thể
- Communicative intention chunk (làm gesture với mục đích)

**PFC-Inference Ladder**: **L3** 🟢. Hành động hướng mục tiêu phối hợp với thành phần xã hội.

### §2.9 — Proto-declarative pointing (12-14 tháng) ⭐

🟢 **Sự kiện**: Trẻ 12-14 tháng bắt đầu pointing **để chia sẻ chú ý** với người lớn về một vật thể — "nhìn vào đó" thay vì "đưa cho tôi cái đó". Đây là dạng declarative gesture. Thường đi kèm với check-back đến người lớn (E18-style triadic gaze, xem [03-Visual-System-Arc.md](03-Visual-System-Arc.md) §4.6).

🟢 **Nghiên cứu**: Bates et al. 1975, Tomasello 1995, Liszkowski, Carpenter & Tomasello 2007 — proto-declarative pointing như bằng chứng của shared intentionality.

🟡 **Chunks yêu cầu** (nhiều hơn proto-imperative):
- Tất cả proto-imperative chunks (§2.8) ở trên
- **Shared attention schema chunk** — coi chú ý như một thứ mà hai agents có thể cùng giữ trên một vật thể
- **Communicative purpose chunk** cho non-request (chia sẻ khác với yêu cầu)
- **Check-back chunk** — vòng lặp gaze xác nhận shared attention

**PFC-Inference Ladder**: **L4** 🟢. Thực thi phối hợp đầy đủ, tích hợp multi-chunk, mục tiêu là non-instrumental (chia sẻ, không phải yêu cầu).

**Tầm quan trọng framework**: Proto-declarative pointing là **phiên bản gestural của joint attention initiation**. Nó tích hợp hand motor chunks + social chunks + pre-theory-of-mind chunks. Tomasello lập luận đây là tiền thân gestural của ngôn ngữ — khả năng tham chiếu đến một thứ gì đó vì lợi ích của agent khác là nền tảng của tham chiếu ngôn ngữ. Xem [08-Verbal-Production-Arc.md](08-Verbal-Production-Arc.md) §3 để xử lý phía verbal.

### §2.10 — Tool use + object manipulation (12-18 tháng)

🟢 **Sự kiện**: Trẻ 12-18 tháng bắt đầu dùng vật thể như công cụ — thìa để ăn, cốc để uống, que để với, container để đựng. Thao tác ngày càng thành thục.

🟢 **Nghiên cứu**: Piaget 1952 — "tertiary circular reactions" substage 5 cổ điển mô tả tool use xuất hiện. Bruner 1973 — học kỹ năng qua tinh chỉnh dần dần. Want & Harris 2001 — học xã hội về tool use.

🟡 **Chunks yêu cầu**: Object-function chunks + hand-tool coordination chunks + goal-sequence chunks + đôi khi imitation chunks (từ việc xem người lớn).

**PFC-Inference Ladder**: **L4** 🟢. Phối hợp, hướng mục tiêu, tích hợp multi-chunk.

### §2.11 — Intentional gesture for need (E25, 14 tháng) ⭐ bằng chứng H11

🟢 **Sự kiện**: Em bé ~14 tháng (chưa nói được). Há miệng + pointing đến tủ lạnh = "muốn ăn". Giơ cả hai tay = "bế em lên". Đẩy tay người khác đi = "không, không muốn". Mỗi gesture có ý nghĩa cụ thể và nhất quán. ([Feel-Example E25](../../Body-Base/Feeling/Feel-Example-Draft.md#e25) dòng 1680.)

🟢 **Nghiên cứu**: Goodwyn, Acredolo & Brown 2000 "Impact of symbolic gesturing on early language development" — cho thấy trẻ sơ sinh có được các nhãn gestural sớm hơn các nhãn lời nói cho cùng khái niệm. Nghiên cứu ngôn ngữ ký hiệu cho em bé có literature đáng kể về giao tiếp gestural sớm.

🟡 **Chunks yêu cầu**:
- Interoceptive/need state chunk (đói, mong muốn được bế, muốn từ chối)
- Gesture-specific motor chunk (một cái cho mỗi nhu cầu)
- **Need-to-gesture binding chunk** — liên kết trạng thái nhu cầu cụ thể với gesture output cụ thể
- Social intention chunk (người lớn sẽ hiểu và phản hồi)

**PFC-Inference Ladder**: **L4** 🟢. Thực thi phối hợp với mapping need-to-output phân biệt.

**⭐ Bằng chứng H11 Receptive-Productive Asymmetry**: E25 ở 14 tháng là **motor productive** cho các trạng thái nhu cầu cụ thể. Productive verbal cho cùng nhu cầu xuất hiện ở ~18-22 tháng (E21 "đói", E22 "đau chân", E23 "buồn đái"). Khoảng cách = ~4-8 tháng.

**Quan sát framework quan trọng**: E25 cho thấy rằng **receptive-productive gap là một phần là motor-system gap**, không phải thuần túy là gap nhận thức. Em bé ở 14 tháng:
- Có need-detection chunk (interoceptive, phía receptive)
- Có specific-gesture chunk (hand motor, phía productive)
- Có thể liên kết chúng đáng tin cậy

Ở 14 tháng, em bé **chưa có**:
- Articulation chunks cho các nhãn verbal tương ứng (phối hợp mouth motor cho "đói", "bế", v.v.)
- Hoặc có thể: verbal label chunk bản thân đang compile nhưng articulation motor chunks đang lag

Khoảng cách 4-8 tháng từ E25 đến E21/E22/E23 là bằng chứng rằng **articulation motor chunks cụ thể lag phía sau hand motor chunks** cho communicative output. Đây là một trong những demonstrations within-motor-system sạch nhất của H11 — và sẽ được drill sâu hơn trong [08-Verbal-Production-Arc.md](08-Verbal-Production-Arc.md) §5.

**Hàm ý từ Feel-Example E25 Notes**: Feel-Example explicitly states "chunks có thể được 'labeled' bằng gesture trước khi labeled bằng words. Output channel cho chunks không nhất thiết phải verbal." Đây là **đóng góp Nút Thắt 6** — labeling attachment có thể dùng gestural handles như alternative cho verbal handles. Xem §7.3 + §8.2 dưới đây.

### §2.12 — Delayed imitation (14-18 tháng, Meltzoff 1988)

🟢 **Sự kiện**: Trẻ 14-18 tháng có thể bắt chước một hành động họ quan sát nhiều giờ hoặc nhiều ngày trước đó — chứng minh delayed recall + motor reproduction.

🟢 **Nghiên cứu**: Meltzoff 1988 — demonstration cổ điển về delayed imitation ở trẻ 14 tháng quan sát một hành động với đồ chơi mới, được test sau 24 giờ. Meltzoff & Moore 1994 — công trình imitation sơ sinh (neonatal) trước đó.

🟡 **Chunks yêu cầu**: Observed-action chunks + motor-reproduction chunks + action-sequence chunks + delayed recall (chunks tồn tại qua các chu kỳ ngủ/thức).

**PFC-Inference Ladder**: **L4** 🟢.

**Tầm quan trọng framework**: Delayed imitation cho thấy motor chunks **bền vững qua sleep consolidation**. Điều này kết nối với §5.4 cơ chế sleep consolidation cho motor learning.

---

> *[Phase A hoàn thành — Header + §0 + §1 + §2 (Hand Motor Arc, 12 sub-sections). Phase B tiếp theo: §3 Locomotion Arc + §4 Master Table.]*

---

## §3 — Locomotion Arc

> Locomotion arc = chunks gross motor cho kiểm soát cơ thể, cân bằng, di chuyển qua không gian. Thiên proprioceptive-vestibular hơn là hướng thị giác (mặc dù thị giác đóng góp).

### §3.1 — Postural reflexes khi sinh

🟢 **Sự kiện**: Trẻ sơ sinh cho thấy nhiều postural reflexes khác nhau (Moro, stepping reflex, asymmetric tonic neck reflex, Galant reflex). Đây là **các primitive patterns được driven bởi brainstem**, không phải chunks học được.

🟡 **Chunks yêu cầu**: Không có. Pattern generators ở cấp tủy sống + brainstem.

**PFC-Inference Ladder**: **L0** 🟢.

**Ghi chú framework**: Một số reflexes tồn tại ngắn như substrate cho voluntary motor chunks sau đó (stepping reflex cuối cùng trở thành đi bộ), nhưng hầu hết biến mất khi kiểm soát motor vỏ não tiếp quản. Sự biến mất của primitive reflexes là một **marker phát triển nhi khoa** — duy trì quá tuổi dự kiến gợi ý lo ngại phát triển.

### §3.2 — Head control (2-4 tháng)

🟢 **Sự kiện**: Vào 2-4 tháng, trẻ giữ đầu khi nằm sấp, nâng đầu chống lại trọng lực, quay đầu để theo dõi các mục tiêu thị giác hoặc thính giác.

🟢 **Nghiên cứu**: Bayley Scales of Infant Development — đánh giá nhi khoa tiêu chuẩn.

🟡 **Chunks yêu cầu**: Neck motor chunks + proprioceptive chunks (đầu tương đối với cơ thể) + gravity compensation chunks.

**PFC-Inference Ladder**: **L1-L2** 🟡. Kiểm soát chủ ý đang xuất hiện.

### §3.3 — Lật người (4-6 tháng)

🟢 **Sự kiện**: 4-6 tháng, trẻ lật từ ngửa sang nghiêng, rồi nghiêng sang sấp, rồi sấp sang ngửa. Thứ tự thường là sấp-sang-ngửa trước (dễ hơn).

🟡 **Chunks yêu cầu**: Torso rotation motor chunks + body-schema chunks + effort coordination chunks.

**PFC-Inference Ladder**: **L2-L3** 🟢.

### §3.4 — Ngồi độc lập (6-7 tháng)

🟢 **Sự kiện**: 6-7 tháng, em bé có thể ngồi không cần hỗ trợ trong thời gian dài, duy trì cân bằng chống lại trọng lực và các rung động nhỏ.

🟡 **Chunks yêu cầu**: Postural control chunks (trunk motor + proprioception + vestibular) + balance recovery chunks (phản ứng với việc ngả người).

**PFC-Inference Ladder**: **L3** 🟢. Motor output phối hợp liên tục.

**Quan sát framework**: Ngồi độc lập là **milestone chức năng lớn** vì nó giải phóng tay để thao tác trong khi em bé ở thẳng đứng. Trước khi ngồi, sử dụng tay trong tư thế thẳng đứng yêu cầu hỗ trợ người lớn. Sau khi ngồi, tay tự do → tỷ lệ compile hand-motor tăng. Đây là một trong những trường hợp **phát triển locomotion arc tạo điều kiện cho phát triển hand arc** qua thay đổi ngữ cảnh.

### §3.5 — Bò (7-9 tháng)

🟢 **Sự kiện**: 7-9 tháng, trẻ bắt đầu bò — di chuyển trên tay và đầu gối (hoặc kiểu commando bằng bụng trước). Tạo ra **locomotion độc lập** đầu tiên → khám phá môi trường vượt ra ngoài tầm tay người lớn.

🟡 **Chunks yêu cầu**: Limb coordination chunks (cross-pattern: tay trái với gối phải, tay phải với gối trái) + forward-motion motor chunks + balance-in-motion chunks.

**PFC-Inference Ladder**: **L3** 🟢.

**Quan sát framework**: Bò cho phép **tự khám phá có định hướng**. Trước khi bò, thế giới của em bé là những gì người lớn mang đến cho chúng. Sau khi bò, em bé có thể theo đuổi các mục tiêu thị giác, điều tra, tiếp cận. Điều này **tăng mạnh tỷ lệ compile cho visual + object chunks** vì em bé giờ tạo ra cơ hội học tập thị giác của riêng mình. Campos et al. 2000 "Travel broadens the mind" xem xét các hệ quả nhận thức của khởi đầu bò — nhận thức không gian, object permanence, cảm xúc, social referencing đều thay đổi tính chất sau khi bò bắt đầu.

### §3.6 — Kéo đứng (9-10 tháng)

🟢 **Sự kiện**: 9-10 tháng, trẻ kéo mình lên tư thế đứng sử dụng đồ nội thất hoặc người lớn để hỗ trợ. Chưa đứng độc lập.

🟡 **Chunks yêu cầu**: Leg extension motor chunks + standing postural chunks + grip chunks (để giữ hỗ trợ).

**PFC-Inference Ladder**: **L3** 🟢.

### §3.7 — Bước đi độc lập đầu tiên (10-14 tháng)

🟢 **Sự kiện**: Giữa 10 và 14 tháng, trẻ bước đi độc lập đầu tiên — thả khỏi hỗ trợ và đi 2-5 bước trước khi ngã hoặc bắt hỗ trợ. Khoảng rộng (10-15 tháng điển hình, đuôi dài hơn trong biến thể cá nhân).

🟢 **Nghiên cứu**: Milestones nhi khoa tiêu chuẩn; biến thể cross-cultural được ghi chép (Super 1976 về trẻ Đông Phi đi sớm hơn do thực hành người chăm sóc; Karasik et al. 2010 — review cross-cultural).

🟡 **Chunks yêu cầu**: Upright balance chunks + stepping pattern chunks + weight transfer chunks + fall recovery chunks.

**PFC-Inference Ladder**: **L3-L4** 🟢.

### §3.8 — Đi bộ (12-15 tháng)

🟢 **Sự kiện**: Vào 12-15 tháng, trẻ đi bộ độc lập với ngày càng ít chao đảo, chuỗi dài hơn, và hướng có mục đích.

🟡 **Chunks yêu cầu**: Walking cycle chunks (luân phiên trái-phải-trái) + direction control chunks + balance-in-motion chunks + obstacle-avoidance chunks.

**PFC-Inference Ladder**: **L4** 🟢. Thực thi phối hợp đầy đủ, hướng mục tiêu, đáng tin cậy.

**Tầm quan trọng framework**: Đi bộ là **đỉnh cao của locomotion arc trong năm đầu**. Nó chuyển đổi thế giới của em bé một lần nữa (như bò đã làm, nhưng hơn thế). Đi bộ + nói chuyện cùng nhau đánh dấu sự chuyển tiếp từ "infant" sang "toddler" — khoảnh khắc khi hầu hết các hệ thống cơ thể đạt ngưỡng hoạt động đầu tiên cho chức năng độc lập.

### §3.9 — Chạy (18-24 tháng)

🟢 **Sự kiện**: 18-24 tháng, trẻ nhỏ bắt đầu chạy — dáng đi nhanh hơn với giai đoạn ngắn trên không.

🟡 **Chunks yêu cầu**: Walking chunks + faster-cycle execution + airborne balance chunks + energy management chunks.

**PFC-Inference Ladder**: **L4** 🟢.

### §3.10 — Tóm tắt locomotion arc

🟢 Locomotion arc là **tương đối tuyến tính** — mỗi milestone xây dựng trên cái trước, với ít track song song. Head control → lật → ngồi → bò → kéo đứng → bước đầu tiên → đi bộ → chạy là một chuỗi sạch. Biến thể cá nhân tồn tại về timing (một số em bé bỏ qua bò, đi thẳng từ ngồi đến kéo đứng và đi bộ), nhưng ordering chung ổn định.

Tương phản với hand arc có **các track song song** (manipulation, pointing, gesturing, tool use có thể tiến bộ bán độc lập). Tính tuyến tính của locomotion phản ánh tính thống nhất của "di chuyển cơ thể qua không gian" như một task cơ thể cấp đơn.

---

## §4 — Các Sự Kiện Được Phân Tích với PFC-Inference Ladder (Master Table)

### §4.1 — Master event table (motor arcs 0-24 tháng)

| # | Sự kiện | Tuổi | Arc | Ladder | Chunks chính yêu cầu | Nghiên cứu |
|---|---|---|---|---|---|---|
| M1 | Palmar grasp reflex (E7) | Khi sinh | Hand | L0 🟢 | Không (reflex) | Peiper 1963 |
| M2 | Rooting + sucking (E8) | Khi sinh | Miệng | L0 🟢 | Không (reflex) | Peiper 1963 |
| M3 | Moro reflex (E6) | Khi sinh | Cơ thể | L0 🟢 | Không (reflex) | Tiêu chuẩn nhi khoa |
| M4 | Stepping reflex | Khi sinh | Loco | L0 🟢 | Không (reflex, biến mất) | Thelen 1986 |
| M5 | Hand-to-mouth chủ ý | 2-3 tháng | Hand | L1-L2 🟡 | Proprioceptive + arm motor | Rochat 1989 |
| M6 | Head control | 2-4 tháng | Loco | L1-L2 🟢 | Neck motor + proprioception | Bayley Scales |
| M7 | Smooth pursuit (eye motor) | 6-8 tuần | Eye | L1-L2 🟡 | Oculomotor + prediction | Aslin 1981 (từ 03) |
| M8 | Vung vào vật thể | 3 tháng | Hand | L2 🟡 | Target + motor, kém chính xác | von Hofsten 1982 |
| M9 | Với tay có hướng dẫn thị giác | 4-5 tháng | Hand | L3 🟢 | Visuomotor bind ⭐ | von Hofsten 1979, 1984 |
| M10 | Lật người | 4-6 tháng | Loco | L2-L3 🟢 | Torso rotation + body schema | Bayley Scales |
| M11 | Nắm tay đầy đủ | 5-6 tháng | Hand | L3 🟢 | Reach + finger flexion | Halverson 1931 |
| M12 | Khám phá vật thể (mút, đập) | 5-9 tháng | Hand | L3 🟢 | Manipulation + object chunks | Piaget 1952 |
| M13 | Ngồi độc lập | 6-7 tháng | Loco | L3 🟢 | Postural + balance recovery | Bayley Scales |
| M14 | Chuyển tay-sang-tay | 6-8 tháng | Hand | L3 🟢 | Bilateral coordination | được ghi chép rộng rãi |
| M15 | Bò | 7-9 tháng | Loco | L3 🟢 | Cross-pattern limb coordination | Bayley Scales |
| M16 | Pincer grasp | 9-10 tháng | Hand | L3-L4 🟢 | Fine motor precision | Halverson 1931 |
| M17 | Proto-imperative pointing | 9-10 tháng | Hand | L3 🟢 | Finger extension + target + adult-as-agent | Bates et al. 1975 |
| M18 | Kéo đứng | 9-10 tháng | Loco | L3 🟢 | Leg extension + standing postural | Bayley Scales |
| M19 | Bước đi độc lập đầu tiên | 10-14 tháng | Loco | L3-L4 🟢 | Upright balance + stepping + recovery | Bayley Scales |
| M20 | Đi bộ | 12-15 tháng | Loco | L4 🟢 | Full walking cycle + direction + obstacle | Bayley Scales |
| M21 | Proto-declarative pointing | 12-14 tháng | Hand | L4 🟢 | Proto-imperative + shared attention + check-back | Bates 1975, Tomasello 1995 |
| M22 | Intentional gesture for need (E25) ⭐ | 14 tháng | Hand | L4 🟢 | Need + gesture + binding | Goodwyn 2000 |
| M23 | Tool use / manipulation | 12-18 tháng | Hand | L4 🟢 | Object-function + coordination | Piaget 1952, Bruner 1973 |
| M24 | Delayed imitation | 14-18 tháng | Hand+body | L4 🟢 | Observed action + reproduction | Meltzoff 1988 |
| M25 | Chạy | 18-24 tháng | Loco | L4 🟢 | Fast gait + airborne balance | Bayley Scales |

### §4.2 — Worked example — Với tay có hướng dẫn thị giác (M9)

Tuân theo template 01 §6.3:

```
[Sự kiện quan sát được, tuổi, citation]
Trẻ 4-5 tháng với tay đến các mục tiêu nhìn thấy với độ chính xác hợp lý.
Trước 4 tháng, với tay là các vung không phối hợp.
(von Hofsten 1979 Developmental Psychology 15:257-261; được tái lập rộng rãi.)
    ↓
[Chunks có thể yêu cầu]
- Visual object location chunk (tọa độ không gian 3D)
- Arm motor chunks (các primitive vai, khuỷu tay, cổ tay)
- ⭐ Visuomotor binding chunk (coordinate transformation visual → motor)
- Hand pre-shape chunk (tay phù hợp với hình dạng mục tiêu trước khi tiếp xúc)
- Online correction chunks (điều chỉnh với tay driven bởi feedback)
    ↓
[PFC-Inference Ladder level]
L3 — hành động phối hợp, hướng mục tiêu, nhưng độ chính xác cải thiện trong những tháng tiếp theo
    ↓
[Plausibility qualifier]
Sự kiện 🟢 (được tái lập rộng rãi)
Chunks-required 🟢🟡 (chunks list được hỗ trợ tốt, visuomotor bind là
claim trung tâm framework cho đóng góp Nút Thắt 3)
Ladder L3 🟢
```

### §4.3 — Worked example — E25 gestural communication (M22)

```
[Sự kiện quan sát được, tuổi, citation]
Trẻ 14 tháng dùng các gestures cụ thể cho các nhu cầu cụ thể: há miệng + point đến
tủ lạnh = muốn ăn; giơ tay = bế em lên; đẩy tay đi = từ chối.
(Feel-Example E25; Goodwyn, Acredolo & Brown 2000 cho cơ sở nghiên cứu.)
    ↓
[Chunks có thể yêu cầu]
- Interoceptive need detection chunks (đói, mong muốn được bế, từ chối)
- Hand motor chunks cho mỗi gesture cụ thể
- Need-to-gesture binding chunks (một binding cho mỗi cặp need-gesture)
- Social communicative intention chunk (người lớn sẽ hiểu)
- Expectation chunk (người lớn sẽ phản ứng phù hợp)
    ↓
[PFC-Inference Ladder level]
L4 — thực thi phối hợp, outputs phân biệt theo nhu cầu, đáng tin cậy
    ↓
[Plausibility qualifier]
Sự kiện 🟢 (được ghi chép rõ ràng qua nhiều em bé)
Chunks-required 🟢🟡 (chunks stack là framework inference, binding là
claim trung tâm)
Ladder L4 🟢
    ↓
[⭐ H11 Receptive-Productive gap test]
Gestural productive cho trạng thái nhu cầu: 14 tháng (E25)
Verbal productive cho cùng nhu cầu: 18-22 tháng (E21/E22/E23)
Khoảng cách: ~4-8 tháng
Diễn giải: Articulation motor chunks lag phía sau hand motor chunks cho
communicative output. Need-detection chunk + communicative intention chunk đã
được compile ở 14 tháng — chỉ có OUTPUT CHANNEL là khác.
```

---

> *[Phase B hoàn thành — §3 Locomotion Arc (10 sub-sections) + §4 Master Table (25 M-events + 2 worked examples). Phase C tiếp theo: §5 Compile Mechanisms + §6 Cross-Body-Input + §7 ⭐ Pre-verbal Gestural Production.]*

---

## §5 — Compile Mechanisms cho Motor Chunks

> Motor chunks compile qua cùng 4 cơ chế nhưng với **các trọng số khác nhau** so với chunks receptive (thị giác/thính giác).

### §5.1 — Repetition (LTP) — dominant

**Dominant cho**: Về cơ bản tất cả motor chunks. Motor learning theo cổ điển là repetition-driven (Thorndike's law of exercise, nghiên cứu motor learning hiện đại).

**Bằng chứng**: Mỗi sự kiện motor chunks trong §2-§3 xuất hiện qua hàng trăm đến hàng nghìn lần thử. Hand-to-mouth (§2.3) được thực hành hàng chục lần/ngày. Với tay (§2.4) được thực hành với độ chính xác cải thiện dần qua nhiều tuần. Số bước đi bộ: ~2,400 bước/giờ × giờ thực hành (Adolph et al. 2012 "How do you learn to walk? Thousands of steps and dozens of falls per day").

**Framework claim**: Repetition là **cơ chế compile chính không thể chối cãi cho motor**. Điều này tương phản với thính giác chunks nơi receptive có thể compile từ passive exposure; motor **phải liên quan đến thực hành chủ động** để compile.

### §5.2 — Multi-modal binding — rất quan trọng

**Dominant cho**: Visuomotor chunks (với tay, pointing, gaze following), audio-motor chunks (quay đầu về phía âm thanh), proprioceptive-motor chunks (cân bằng, body schema).

**Bằng chứng**: Hầu hết motor chunks trên L1 đều là multi-modal — chúng bind motor output với sensory input của một loại nào đó. Pure motor-only chunks (không có sensory binding) hiếm ngoài các reflexes.

**Framework claim**: Motor arc là **intrinsically multi-modal** vì hành động yêu cầu sensory feedback để tinh chỉnh. Đây là sự khác biệt then chốt so với chunks receptive có thể compile mà không cần hành động.

### §5.3 — Emotional peak tagging — ít liên quan hơn cho motor

**Áp dụng cho**: Pain-associated motor chunks (rút lui khỏi nóng), comfort-associated motor chunks (với tay đến caregiver), reward-associated motor chunks (các hành động lặp lại mang lại kết quả mong muốn).

**Framework claim**: Emotional tagging là **ít trung tâm hơn** cho hầu hết motor chunks so với chunks receptive. Hầu hết motor chunks (đi bộ, nắm, pointing) compile qua thực hành không có emotional peaks mạnh. Nhưng reward-associated motor chunks (imitation learning, intentional actions) có nhận emotional tagging. Đây là **compile-mechanism asymmetry qua các body-inputs** — một phát hiện mà file này đóng góp cho F1 synthesis.

### §5.4 — Sleep consolidation — quan trọng

**Dominant cho**: Motor skill consolidation, độ bền của motor memory.

**Bằng chứng**:
- Walker 2003, 2017 — sleep + motor learning literature rộng rãi
- Stickgold 2005 — sleep-dependent motor memory consolidation
- Gomez et al. 2006 — học tập trẻ sơ sinh được hưởng lợi từ nap (có thể mở rộng cho motor tasks)
- Friedrich et al. 2015 — consolidation memory trẻ sơ sinh trong khi ngủ

**Framework claim**: Trẻ sơ sinh ngủ 14-17 giờ/ngày trong các tháng đầu, nhiều trong REM-rich sleep. Đây là **môi trường consolidation lý tưởng** cho motor chunks được có được trong giờ thức. Các cải thiện motor ấn tượng thường thấy sau một giấc ngủ ngắn hoặc qua đêm phản ánh **offline consolidation**, không phải thực hành ý thức.

### §5.5 — Tương tác của các cơ chế

Quỹ đạo compile motor chunk điển hình:

1. **Lần thử đầu tiên** — khám phá ngẫu nhiên (ví dụ vung đầu tiên không phối hợp vào vật thể)
2. **Tinh chỉnh driven bởi feedback** — visual + proprioceptive feedback trong khi thử
3. **Repetition** — nhiều lần thử qua nhiều giờ/ngày
4. **Sleep consolidation** — tổ chức lại qua đêm tăng cường các pattern hữu ích, prune các pattern thất bại
5. **Chunk ổn định** — thực thi đáng tin cậy, cần ít chú ý ý thức tối thiểu

Mỗi motor chunk đi qua quỹ đạo này ở tỷ lệ riêng của nó. Chunks compile nhanh (hand-to-mouth, head turn đến âm thanh) mất vài ngày-tuần. Chunks compile chậm (đi bộ, tool use) mất nhiều tuần-tháng. Sự biến đổi phụ thuộc vào **độ phức tạp của chunks stack yêu cầu** — chunks primitive đơn giản compile nhanh hơn các hành vi tích hợp multi-chunk.

---

## §6 — Các Kết Nối Cross-Body-Input

### §6.1 — Motor ↔ Thị giác (visuomotor)

**Được bao gồm trong**: §2.4 (với tay), §2.8-§2.9 (pointing), §3.5 (bò + khám phá thị giác).

**Bind then chốt**: Visuomotor coordinate transformation — substrate cho hầu như tất cả hành động hướng mục tiêu hand-based. Xem [03-Visual-System-Arc.md](03-Visual-System-Arc.md) §6.3.

### §6.2 — Motor ↔ Thính giác

**Primary binds**: Head turn đến âm thanh ([04](04-Auditory-System-Arc.md) §4.1), vocal production (mouth motor + auditory feedback, [08](08-Verbal-Production-Arc.md)), rhythm-based motor entrainment (nhảy xuất hiện 18-24 tháng).

### §6.3 — Motor ↔ Interoceptive

**Primary binds**: Body-effort chunks (đi bộ nỗ lực, với tay nỗ lực), self-soothing motor chunks (mút ngón tay), need-to-action motor chunks (§2.11 E25 gesture for need).

**Quan sát framework**: Interoceptive-motor bind là load-bearing cho danh mục **response-to-body-state** của hành động. Em bé với tay về phía mẹ khi lạnh bind interoceptive (cold chunk) với motor (reach chunk). Xem [06a-Interoceptive-Bladder-Keystone.md](06a-Interoceptive-Bladder-Keystone.md) + [06b-Interoceptive-Other-States.md](06b-Interoceptive-Other-States.md) để xử lý phía interoceptive.

### §6.4 — Motor ↔ Xã hội

**Primary binds**: Pointing (§2.8-§2.9), với tay đến caregiver (social-motor), imitation (§2.12), các thành phần motor joint attention (gaze + head turn + pointing).

Xem [07-Social-Recognition-Arc.md](07-Social-Recognition-Arc.md) để xử lý phía xã hội.

### §6.5 — Motor ↔ Verbal (preview, đầy đủ trong 08)

**Primary binds**: Articulation motor (mouth motor cho lời nói), gesture-as-language-substitute (E25 intentional gesture), co-speech gestures sau trong những năm toddler.

**Bất đối xứng then chốt**: Hand motor chunks compile nhanh hơn articulation motor chunks (§2.11 phân tích E25). Bất đối xứng này là bằng chứng phía motor cho H11 (Nút Thắt 5). Xem §7 dưới đây + [08-Verbal-Production-Arc.md](08-Verbal-Production-Arc.md) §5.

---

## §7 — Sản Xuất Gestural Tiền-Verbal như Proto-Communication (Preview Nút Thắt 5+6)

> Section này là phân tích tập trung về giao tiếp gestural trong cửa sổ 9-18 tháng — bằng chứng sạch nhất trong F1 cho H11 và Nút Thắt 6.

### §7.1 — Khoảng cách 4 tháng từ gesture đến verbal

🟢 **Thực tế thực nghiệm**: Intentional gesture for needs (E25) xuất hiện đáng tin cậy ~14 tháng. Các nhãn verbal đầu tiên cho nhu cầu (E21 "đói", E22 "đau chân", E23 "buồn đái") xuất hiện ~18-22 tháng. Khoảng cách = ~4-8 tháng.

🟡 **Framework claim**: Khoảng cách KHÔNG phải vì em bé ở 14 tháng thiếu:
- ❌ Need-detection chunk — em bé rõ ràng phát hiện nhu cầu (được chứng minh bởi gesture phù hợp)
- ❌ Communicative intention chunk — em bé rõ ràng có ý định giao tiếp (được chứng minh bởi gesture hướng đến người lớn + chờ phản hồi)
- ❌ Binding chunk — em bé rõ ràng bind trạng thái nhu cầu với communicative output (được chứng minh bởi gesture cụ thể cho mỗi nhu cầu)
- ❌ Vốn từ vựng receptive cho các từ liên quan — vào 14 tháng em bé thường hiểu "đói", "ăn", "bế" v.v. (nhất quán với Bergelson & Swingley 2012 common noun comprehension 6-9 tháng)

🟡 **Framework claim**: Khoảng cách LÀ vì em bé ở 14 tháng thiếu:
- ✅ **Articulation motor chunks** — các mouth motor chunks cụ thể để sản xuất các nhãn verbal đáng tin cậy
- ✅ Có thể: **verbal label chunk bản thân ở dạng productive** — dạng mà retrieving + orchestrating articulation để output

**Bằng chứng cho framing articulation-bottleneck**: Các em bé được dạy ngôn ngữ ký hiệu cho em bé cho thấy rằng **phía receptive + binding + intention** đã sẵn sàng sớm hơn — chúng sản xuất ký hiệu cho nhu cầu nhiều tháng trước khi chúng sản xuất các từ nói tương ứng. Goodwyn et al. 2000 là citation then chốt. Thứ DUY NHẤT được thêm khi trẻ cuối cùng sử dụng các từ nói là kênh output articulation motor.

### §7.2 — Within-child test của H11

🟢 Gesture-to-verbal gap là **within-child test** của H11 Receptive-Productive Asymmetry:

- Điều kiện kiểm soát: cùng em bé, cùng trạng thái nhu cầu, cùng communicative intent, cùng khán giả người lớn
- Variable: output motor channel (tay vs miệng)
- Kết quả: hand motor chunks compile 4-8 tháng sớm hơn mouth motor chunks cho communicative outputs tương đương

Điều này cô lập **sự khác biệt tỷ lệ compile motor-channel** khỏi các yếu tố phát triển khác. Đây là bằng chứng within-subjects mạnh cho H11, mà bằng chứng cross-modality rộng hơn (Mandel 1995 name gap 13.5 tháng trong [04](04-Auditory-System-Arc.md) §9.3) bổ sung.

**H11 formalization đầy đủ**: [08-Verbal-Production-Arc.md](08-Verbal-Production-Arc.md) §5. Đóng góp của file này là bằng chứng within-child đặc hiệu motor.

### §7.3 — Preview Nút Thắt 6 — gesture như alternative handle

🟡 **Framework claim**: Nút Thắt 6 hỏi liệu chunks có luôn cần verbal labels để hoạt động không, hay các hệ thống labeling thay thế (gestures, actions, images) có thể phục vụ cùng vai trò chunk-handle không.

**Bằng chứng từ E25 và giao tiếp gesture**:
- Chunks cho các trạng thái nhu cầu ở 14 tháng hoạt động đầy đủ mà không có verbal labels
- Gestural label đủ cho referential communication + retrieval + action
- Người lớn giải thích gesture và phản hồi phù hợp = chunk được "labeled" trong một hệ thống không-verbal
- Khi verbal labels sau đó compile (18-22 tháng), chúng thường **thay thế** gestures cho cùng chunks, nhưng các chunks tồn tại trước verbal

**Framework implication**: Verbal labeling là **một trong số các hệ thống labeling**, không phải hệ thống duy nhất. Chunks có thể được "handled" qua:
- Gestural labels (E25, baby sign language, deaf sign language)
- Action labels (các chuỗi hành động thói quen trở thành label của riêng chúng)
- Visual labels (nhận dạng dựa trên hình ảnh)
- Verbal labels (dominant trong các nền văn hóa người lớn)
- Internal-only labels (felt sense không có external output, Feel-Example notes)

**⭐ Đóng góp Feel-Example** (từ [E25 Notes](../../Body-Base/Feeling/Feel-Example-Draft.md#e25) dòng 1720-1734): "chunks có thể được 'labeled' bằng gesture trước khi labeled bằng words. Output channel cho chunks không nhất thiết phải verbal. ... Tất cả đều là valid forms của 'feeling expressed'. Sự ưu tiên cho verbal output trong văn hóa dominant có thể bias chúng ta nghĩ 'feeling = verbal' — nhưng đó là confusion giữa output channel và chunk itself."

Đây là **framework commitment** mà file này kế thừa và operationalize cho preview Nút Thắt 6. Verdict đầy đủ trong [08-Verbal-Production-Arc.md](08-Verbal-Production-Arc.md).

---

> *[Phase C hoàn thành — §5 Compile Mechanisms + §6 Cross-Body-Input + §7 ⭐ Pre-verbal Gestural Production. Phase D tiếp theo: §8-§11.]*

---

## §8 — Đóng Góp Nút Thắt

### §8.1 — Nút Thắt 5 (Receptive-Productive Asymmetry) — đóng góp preview

**Đóng góp của file này**: Bằng chứng motor-channel within-child (§7.1-§7.2). Gesture ở 14 tháng vs verbal ở 18-22 tháng chứng minh articulation-motor-specific lag trong một so sánh trong-cá-nhân có kiểm soát.

**Điểm dừng tiếp theo**: [08-Verbal-Production-Arc.md](08-Verbal-Production-Arc.md) §5 ngôi nhà chính cho H11 formalization đầy đủ.

### §8.2 — Nút Thắt 6 (Alternative labeling handles) — đóng góp preview

**Đóng góp của file này**: Demonstration gestural labeling qua E25 + framework theoretical commitment Feel-Example. Chunks có thể được handled bởi các nhãn không-verbal.

**Điểm dừng tiếp theo**: [08-Verbal-Production-Arc.md](08-Verbal-Production-Arc.md) để formalization chính.

### §8.3 — Nút Thắt 3 (Multi-modal binding) — đóng góp một phần qua visuomotor

**Đóng góp của file này**: Visually guided reaching (§2.4) như phía motor của visual-motor bind. Visuomotor coordinate transformation là một trong những sự kiện multi-modal binding rõ ràng nhất trong F1 năm đầu.

### §8.4 — Nút Thắt 1 (Proto-chunk gradient) — bằng chứng thứ cấp

**Đóng góp của file này**: Motor learning cho thấy **kỹ năng xuất hiện gradient** qua tất cả các milestones. Với tay đi từ vung không phối hợp → với tay ngày càng chính xác qua nhiều tuần. Đi bộ đi từ các lần thử 2 bước không ổn định → đi bộ ổn định qua nhiều tuần. Đây là bằng chứng thêm cho quan điểm gradient đã committed trong [04-Auditory-System-Arc.md](04-Auditory-System-Arc.md) §6.4.

### §8.5 — Nút Thắt 4 (PFC hardware × chunks missing)

Đã committed trong [01-PFC-Hardware-Reframe.md](01-PFC-Hardware-Reframe.md). File này áp dụng reframe xuyên suốt bằng cách xử lý motor chunks như **content missing** thay vì "motor cortex trưởng thành".

---

## §9 — Câu Hỏi Mở

1. **Tại sao hand motor lead articulation motor 4+ tháng?** Nhiều giả thuyết:
   - Hand motor có visual feedback trực tiếp hơn (bạn thấy tay mình di chuyển)
   - Mouth motor feedback là proprioceptive + auditory (ít nổi bật hơn)
   - Hand motor cortex có representation vỏ não lớn hơn
   - Hand motor cũ hơn về mặt tiến hóa
   Không cái nào được test dứt khoát như nguyên nhân của khoảng cách. Câu hỏi framework-empirical mở.

2. **Biến thể cá nhân trong bước đầu tiên — điều gì dự đoán timing?** Khoảng từ 9-18 tháng qua các em bé điển hình. Các yếu tố môi trường (thực hành người chăm sóc, loại bề mặt), sinh lý học (khối lượng cơ chân, tỷ lệ cơ thể), thần kinh (sự trưởng thành motor). Bao nhiêu là tỷ lệ compile chunks vs hạn chế vật lý?

3. **Em bé bỏ qua bò — hệ quả nhận thức là gì?** Một số em bé bỏ qua bò và đi từ ngồi → kéo đứng → đi bộ. Campos et al. 2000 lập luận bò có lợi ích nhận thức (nhận thức không gian, điều tiết cảm xúc, social referencing). Các em bé bỏ qua có bị bất lợi không, hay họ bắt kịp qua các cơ chế thay thế?

4. **Xuất hiện intentional gesture E25 — có prerequisite receptive không?** Em bé có cần thấy gestures được dùng giao tiếp (ở caregivers, trẻ khác) trước khi chúng có thể sản xuất chúng không? Hay motor + intention đến trước và mô hình môi trường là icing? Trẻ điếc của cha mẹ ký hiệu phát triển giao tiếp gestural theo đúng timeline mặc dù không có mô hình verbal — gợi ý motor + intention là primary.

5. **Delayed imitation (Meltzoff 1988) — nó có yêu cầu ngôn ngữ không?** Trẻ 14-18 tháng bắt chước hành động từ nhiều ngày trước đó. Liệu delayed recall này có được mediated bởi verbal rehearsal nội bộ (không có khả năng ở em bé tiền-verbal), bởi visual memory, bởi motor imagery, hay bởi một cơ chế khác không? Câu hỏi framework về cơ chế persistence chunks.

6. **Sleep consolidation trong motor learning — chúng ta có thể định lượng sự cải thiện không?** Motor learning người lớn cho thấy cải thiện ~20-30% sau khi ngủ vs các điều kiện không ngủ. Motor learning trẻ sơ sinh nên cho thấy hiệu ứng tương tự hoặc lớn hơn (ngủ nhiều hơn, REM nhiều hơn). Các nghiên cứu so sánh trực tiếp sẽ tăng cường claim cơ chế compile.

7. **Biến thể cross-cultural trong motor milestones** — Super 1976 trẻ Đông Phi đi sớm hơn (thực hành caregiver giữ thẳng đứng). Karasik et al. 2010 review tìm thấy biến thể cross-cultural đáng kể. F1 framework dự đoán gì về cách thực hành caregiver thay đổi tỷ lệ compile chunks trong các motor arcs cụ thể?

---

## §10 — Cross-References

### §10.1 — Trong F1 Child-Chunk-Development

- [00-Chunk-System-Sketch.md](00-Chunk-System-Sketch.md) — định hướng F1 sub-folder
- [01-PFC-Hardware-Reframe.md](01-PFC-Hardware-Reframe.md) — §6 quy tắc phương pháp luận được dùng xuyên suốt
- [02-Womb-to-Birth-Baseline.md](02-Womb-to-Birth-Baseline.md) — §9.1 baseline (motor chunks vắng mặt khi sinh trừ reflexes + prenatal seeds)
- [03-Visual-System-Arc.md](03-Visual-System-Arc.md) — §4.3 phía thị giác của visually guided reaching, §4.4 gaze following, §4.6 joint attention
- [04-Auditory-System-Arc.md](04-Auditory-System-Arc.md) — §9 receptive-productive preview, §4 auditory motor interface
- [06a-Interoceptive-Bladder-Keystone.md](06a-Interoceptive-Bladder-Keystone.md) — interoceptive-motor binds, buồn đái motor-response lag
- [06b-Interoceptive-Other-States.md](06b-Interoceptive-Other-States.md) — interoceptive-motor cho các trạng thái khác (đói, đau)
- [07-Social-Recognition-Arc.md](07-Social-Recognition-Arc.md) — các sự kiện social-motor (pointing, joint attention, imitation)
- [08-Verbal-Production-Arc.md](08-Verbal-Production-Arc.md) — **ngôi nhà chính cho Nút Thắt 5 + 6**, H11 formalization, articulation-motor deep drill
- [09-Event-Chunks-Inference-Matrix.md](09-Event-Chunks-Inference-Matrix.md) — event table cross-cutting
- [10-F1-Synthesis.md](10-F1-Synthesis.md) — 7 nút thắt final verdicts

### §10.2 — Upstream framework

- [../../Body-Base/Schema/Chunk.md](../../Body-Base/Schema/Chunk.md) — chunk substrate + compile mechanisms
- [../../Modality-Analysis.md](../../Modality-Analysis.md) §2.1.4 Motor — đặc trưng modality motor

### §10.3 — Drilled sub-folders

- [../Learning-Cycle/Learning-Cycle.md](../Learning-Cycle/Learning-Cycle.md) — H8 learning cycle. Motor learning qua error → correction → repetition là một instance của learning cycle, với error signal là "với tay lỡ mục tiêu" v.v.
- [../Agent/Agent.md](../Agent/Agent.md) — H9 Agent operations trên motor chunks cho phép hành động hướng mục tiêu (Self-Pattern-Match dùng motor chunks).
- [../Body-Feedback-Draft/01-Foundation.md](../Body-Feedback-Draft/01-Foundation.md) — H10 body-feedback substrate. Motor chunks là downstream của body-feedback L1-L2 raw signals (proprioception, nỗ lực, đau).

### §10.4 — Feel-Example cross-references thực nghiệm

- [E6 Moro reflex](../../Body-Base/Feeling/Feel-Example-Draft.md#e6) — tham chiếu L0
- [E7 Palmar grasp](../../Body-Base/Feeling/Feel-Example-Draft.md#e7) — §2.1 L0 hand reflex
- [E8 Rooting + sucking](../../Body-Base/Feeling/Feel-Example-Draft.md#e8) — §2.2 L0 mouth reflex
- [E25 Intentional gesture for need](../../Body-Base/Feeling/Feel-Example-Draft.md#e25) — §2.11 ⭐ bằng chứng H11 within-child + §7 preview Nút Thắt 5+6
- [E26 Comfort object](../../Body-Base/Feeling/Feel-Example-Draft.md#e26) — motor + social cross-bind
- [E29 Imitation of household tasks](../../Body-Base/Feeling/Feel-Example-Draft.md#e29) — cross-ref delayed imitation
- [E31 "Không" autonomy](../../Body-Base/Feeling/Feel-Example-Draft.md#e31) — verbal + motor ở ~18-24 tháng

### §10.5 — Cơ sở dữ liệu citation nghiên cứu

Motor arc literature:
- **Peiper 1963** — infant reflexes cổ điển
- **Prechtl & Beintema 1964** — khám thần kinh sơ sinh
- **Twitchell 1970** — phát triển grasp
- **Bayley Scales of Infant Development** — motor milestones nhi khoa tiêu chuẩn
- **Halverson 1931** — grasp taxonomy
- **von Hofsten 1979** *Developmental Psychology* 15:257-261 — bài báo nền tảng infant reaching
- **von Hofsten 1982, 1984** — quỹ đạo phát triển reaching
- **Clifton et al. 1993** — reaching trong bóng tối
- **Rochat 1989** — self-perception và action trong infancy
- **Thelen 1986** — stepping reflex dynamics
- **Bates, Camaioni & Volterra 1975** — proto-imperative / proto-declarative
- **Tomasello 1995** — nền tảng joint attention
- **Liszkowski, Carpenter & Tomasello 2007** — bằng chứng proto-declarative pointing
- **Goodwyn, Acredolo & Brown 2000** ⭐ — symbolic gesturing + phát triển ngôn ngữ
- **Meltzoff 1988** ⭐ — delayed imitation ở 14 tháng
- **Meltzoff & Moore 1994** — neonatal imitation
- **Piaget 1952** — tool use + tertiary circular reactions substage 5
- **Bruner 1973** — học kỹ năng
- **Campos et al. 2000** — bò + hệ quả nhận thức
- **Adolph et al. 2012** — hàng nghìn bước mỗi ngày trong motor learning đi bộ
- **Super 1976** — motor milestones cross-cultural Đông Phi
- **Karasik et al. 2010** — review motor cross-cultural
- **Walker 2003, 2017** — sleep + motor learning
- **Stickgold 2005** — sleep-dependent motor memory
- **Gomez, Bootzin & Nadel 2006** — nap-enhanced learning
- **Friedrich, Wilhelm, Born & Friederici 2015** — infant memory sleep
- **Corbetta & Bojczyk 2002** — quỹ đạo phát triển pincer grasp
- **Berthier & Keen 2006** — phân tích quỹ đạo reaching
- **Bliss & Lømo 1973** — LTP foundational mechanism (motor learning)

---

## §11 — Status

**Draft status**: DRAFT N+4b Phase F1-P8 — bản dịch tiếng Việt hoàn chỉnh, sẵn sàng cho user review.

**Sections hoàn chỉnh**: §0 đến §10 (12 sections).

**Các cam kết framework được thực hiện**:
- ✅ Quy tắc phương pháp luận event-inference được tuân theo xuyên suốt
- ✅ Không có claim "PFC trưởng thành ở tuổi X"
- ✅ PFC-Inference Ladder áp dụng cho tất cả 25 M-table events
- ✅ Plausibility qualifiers 🟢🟡🔴 được áp dụng
- ✅ Baseline state từ 02 §9.1 được cite
- ✅ Hai arc (hand + locomotion) được giữ phân biệt với phân tích cross-rate
- ✅ ⭐ Bằng chứng within-child cho H11 qua E25 vs E21/E22/E23 gap (§7)
- ✅ Preview Nút Thắt 6 qua Feel-Example E25 theoretical commitment
- ✅ Cross-references bidirectional với 00-04 + drilled sub-folders
- ✅ KHÔNG có personal examples (quy tắc framework)
- ✅ Tiếng Việt primary + English technical terms
- ✅ Citations nghiên cứu toàn diện

**Đóng góp Nút Thắt**:
- **Nút Thắt 5 preview** — within-child gesture vs verbal khoảng cách 4-8 tháng (§7.1-§7.2)
- **Nút Thắt 6 preview** — alternative handles qua gesture (§7.3)
- Nút Thắt 3 một phần — bằng chứng cơ chế visuomotor binding (§2.4)
- Nút Thắt 1 thứ cấp — bằng chứng gradient từ motor skill emergence (§8.4)
- Nút Thắt 4 được áp dụng — PFC reframe được dùng xuyên suốt

**Tiến độ dịch**: 6/12 files hoàn chỉnh (00, 01, 02, 03, 04, 05).

**Bước tiếp theo**: User review → nếu được approve, tiến hành Phase F1-P9 (06a + 06b Interoceptive).

---

> **05-Motor-Output-Arc-VI.md — Kết thúc file.**
>
> F1 body-input arc #3 trong 6. Motor output được truy dấu qua hai arc (hand + locomotion) từ birth reflexes qua đi bộ + gestural communication ở 18-24 tháng. Nút Thắt 5 + 6 được preview qua bằng chứng gesture-verbal gap within-child (E25 vs E21/E22/E23). Compile mechanism asymmetry (repetition dominant, emotional tagging ít quan trọng hơn) được ghi chép như phát hiện F1 synthesis. Bản dịch tiếng Việt hoàn chỉnh với 25 M-events được phân tích đầy đủ.
