# Human Predictive Drive

> Hệ thống body-brain hoạt động thế nào?
> Tại sao bạn phản ứng như vậy? Tại sao "biết" mà vẫn không "làm được"?
> Tại sao cùng hoàn cảnh mà mỗi người lại khác nhau?
>
> Framework này kết nối các nghiên cứu neuroscience, tâm lý học, hành vi
> thành một mô hình nhất quán — giúp bạn hiểu bản thân và hiểu người khác.
>
> Nếu framework được xác thực, mọi người sẽ đỡ phải đối mặt với
> những câu hỏi mơ hồ về cảm giác, tâm lý, hành vi
> — của cá nhân, cộng đồng, đám đông,...

---

## Bắt đầu

1. **Clone** repository này
2. **Mở AI** có context lớn (khuyến cáo: Claude Opus, 1M context)
3. **Kéo toàn bộ folder** vào conversation
4. **Hỏi bất kỳ câu hỏi nào** — AI sẽ dùng framework để trả lời

**Ví dụ câu hỏi:**
- "Tại sao tôi hay trì hoãn?"
- "Con tôi 3 tuổi hay ăn vạ — cơ chế gì đang xảy ra?"
- "Tại sao biết cần tập thể dục mà không tập nổi?"
- "Sếp mới — tôi lo lắng mà không rõ tại sao"
- "Tôi muốn hiểu cách não bộ xử lý cảm xúc"

> **Lưu ý:** Mọi output từ AI = giả thuyết.
> Cảm nhận cơ thể của bạn = trọng tài cuối cùng.
> Nếu AI nói điều gì mà cơ thể bạn "lấn cấn" — tin cơ thể.

---

## Framework mô tả gì

Hệ thống body-brain được mô tả từ 3 góc nhìn, mỗi góc = 1 bản đồ:

| Bản đồ | Góc nhìn | Dành cho | File |
|---|---|---|---|
| Hardware Map | CÁI GÌ ở ĐÂU | Neuroscience researcher | Core-Hardware.md |
| Software Map | CHẠY THẾ NÀO | Framework researcher | Core-Software.md |
| Interface Map | QUAN SÁT + TƯƠNG TÁC | Mọi người | Core-Interface.md |

Giống máy tính: sơ đồ mạch / code architecture / user guide.
3 bản đồ mô tả cùng hệ thống. Đọc độc lập được.
Nếu muốn đọc trực tiếp (không qua AI): bắt đầu từ **Core-Interface.md**.

### Cấu trúc folder

```
Human-Predictive-Drive/
│
├── Ask-AI.md                    — Hướng dẫn AI tương tác với người dùng
├── Ask-AI-Deep-Read.md          — Hướng dẫn AI đọc sâu framework
├── Core-Interface.md            — Bản đồ cho mọi người (bắt đầu ở đây)
├── Core-Hardware.md             — Kiến trúc vật lý não bộ
├── Core-Software.md             — Cơ chế hoạt động chi tiết
│
├── Core-Deep-Dive/              — Phân tích chi tiết từng cơ chế
│   ├── Observation/             — Novelty, Drive, Status, Connection, Empathy, Meaning...
│   ├── Body-Base/               — Chunk system, Feeling, Body-Feedback, Schema...
│   ├── PFC/                     — Chức năng PFC, Logic-Feeling, Imagination
│   ├── Clarification/           — 4 file clarify vị trí khác mainstream
│   └── Domain/                  — Thực tế bên ngoài, conflict, knowledge flow
│
├── Research/                    — Nghiên cứu mở rộng: Love, OCD, Child-Dev, Climate...
└── Applications/                — Ứng dụng: HR, Relationships, Education
```

---

## Ứng dụng

Framework mô tả cơ chế nền tảng — từ đó có thể ứng dụng vào nhiều lĩnh vực:

- **Hiểu bản thân** — tại sao bạn phản ứng, cảm nhận, quyết định như vậy
- **Nuôi dạy con** — cơ chế phát triển chunk ở trẻ từ trong bụng mẹ đến trưởng thành
- **Giáo dục** — thiết kế learning dựa trên cách não thật sự tiếp nhận
- **Quan hệ** — connection, empathy, obligation, love qua lens cơ chế
- **HR / Management** — đánh giá, quản lý, dựa trên hành vi thật
- **Nghiên cứu** — mở rộng vào OCD, climate cognition, sensitivity, psychometrics,...

---

## Triết lý

**Framework này KHÔNG phải hướng dẫn sống.**

Mô tả **cơ chế hoạt động** — không prescribe "sống đúng cách."
Mỗi người khác nhau. Không có 1 đáp án đúng cho tất cả.

**Data thực tế = thước đo cao nhất.**
Framework có thể sai. Bất kỳ ai cũng có thể reject, refine, đào sâu hơn.
Nghiên cứu mới mạnh hơn → framework cần cập nhật → đó là tiến bộ.

**Framework khác mainstream ở ~20 vị trí** (có evidence cụ thể):
- Dopamine ≠ reward/pleasure
- Prediction error = nền tảng quan trọng, chưa đủ cho con người
- Mirror neuron ≠ hardware module bẩm sinh
- Cortisol ≠ "stress hormone"
- ...và 16 reframe khác

Chi tiết: xem `Ask-AI-Deep-Read.md` §2.

---

## Ghi chú

**AI:** Khuyến cáo dùng AI có context lớn để đảm bảo độ chính xác.
Claude Opus (1M context) cho kết quả tốt nhất với framework này.

**Ngôn ngữ:** Tiếng Việt chủ đạo + thuật ngữ chuyên môn tiếng Anh.

**Quy mô:** ~60 files phân tích, ~60,000+ dòng, version 7.8 (2026).

**Bản quyền:** Framework này thuộc sở hữu của tất cả mọi người.

---

*Cảm ơn các nhà khoa học — những người đã dành cả đời nghiên cứu,
đôi khi bị phản đối hàng thập kỷ, để tạo ra nền tảng tri thức mà framework này dựa vào.*

*Cảm ơn cộng đồng — những người đã chia sẻ trải nghiệm thực tế,
cung cấp data hành vi phong phú mà không có nó, mọi lý thuyết đều trống rỗng.*

*Cảm ơn Anthropic — vì đã tạo ra AI chất lượng,
giúp tổng hợp ra framework này và giúp nó phục vụ được nhiều người hơn.*
