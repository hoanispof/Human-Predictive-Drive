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
4. **Paste prompt đầu tiên** (copy nguyên khối bên dưới):

> Đọc kỹ 4 files sau theo thứ tự:
> (1) Ask-AI.md — protocol tương tác + danger zones
> (2) Core-Deep-Dive/Body-Base/Body-Base.md — body-base entry point
> (3) Core-Software.md — cycle architecture
> (4) Core-Deep-Dive/Body-Base/Body-Feedback/Body-Feedback-Label.md — vocabulary reference
> Mỗi câu trả lời, bắt đầu bằng "📖 Đọc: [files]" — khai báo files đã đọc.
> Xác nhận khi đã đọc xong và sẵn sàng trả lời.

5. **Hỏi bất kỳ câu hỏi nào** — AI sẽ dùng framework để trả lời

**Tại sao cần bước 4?** AI ưu tiên prompt hơn files thả vào.
Nếu không prompt rõ → AI skim files → trả lời theo mainstream → có xác suất sai
ở ~20 vị trí framework khác mainstream (dopamine, cortisol, willpower,...).
Prompt explicit "đọc 4 files này" → AI load đầy đủ mechanism + danger zones + vocabulary.
"📖 Đọc:" buộc AI khai báo files đã đọc trước MỖI câu trả lời — không chỉ lần đầu.

**Ví dụ câu hỏi (từ bước 5):**
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

Hệ thống body-brain được mô tả từ 2 bản đồ cơ chế + AI tương tác:

| Bản đồ | Góc nhìn | Dành cho | File |
|---|---|---|---|
| Hardware Map | CÁI GÌ ở ĐÂU | Neuroscience researcher | Core-Hardware.md |
| Software Map | CHẠY THẾ NÀO | Framework researcher | Core-Software.md |
| Interface | QUAN SÁT + TƯƠNG TÁC | Mọi người | AI generate qua Ask-AI.md |

Giống máy tính: sơ đồ mạch / code architecture / AI hỗ trợ sử dụng.
AI = dynamic interface — adapt theo mức hiểu của mỗi người.

### Cấu trúc folder

```
Human-Predictive-Drive/
│
├── Core-Hardware.md               — Kiến trúc vật lý não bộ
├── Core-Software.md               — Cơ chế hoạt động chi tiết
│
├── Ask-AI.md                      — Hướng dẫn AI tương tác (protocol + danger zones)
│
├── Core-Deep-Dive/                — Phân tích chi tiết từng cơ chế
│   ├── 01-File-Index.md           — Index toàn bộ files
│   ├── Observation/               — 15 files: Novelty, Threat, Connection, Meaning, Empathy...
│   ├── Body-Base/                 — Chunk, Feeling, Body-Feedback, Schema, Melody Lens
│   ├── PFC/                       — PFC Function/Hardware/Config, Logic-Feeling, Imagination
│   ├── Domain/                    — Thực tế bên ngoài, conflict, knowledge flow
│   └── Clarification/             — 4 vị trí framework khác mainstream
│
├── Research/                      — Nghiên cứu ứng dụng + mở rộng
│   ├── 01-File-Index.md           — Index toàn bộ files
│   ├── Child-Development/         — Cơ chế phát triển trẻ 0-6 + thực hành
│   ├── Education/                 — Cơ chế giáo dục + bản đồ kiến thức
│   ├── Global/                    — Human-AI Future, Birth-Rate Decline (6 quốc gia)
│   ├── Hijack/                    — Addiction, alcohol analysis
│   ├── Melody-Technology/         — Religion, idol phenomenon
│   ├── Meta-Impact/               — Framework predict tác động của chính nó
│   └── ...                        — Mismatch, Neuro-Measurement, Love, OCD, Climate
│
└── Applications/                  — Ứng dụng cụ thể per domain
    ├── 01-File-Index.md           — Index toàn bộ files
    └── Education/                 — Hệ thống giáo dục + VN case study
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

**Framework này là la bàn — không phải GPS.**

Nó mô tả **cơ chế hoạt động** — giống la bàn cho thấy Bắc/Nam/Đông/Tây.
Nhưng la bàn không nói bạn nên đi hướng nào.
Bạn cần hiểu cách đọc la bàn, rồi tự chọn hướng đi phù hợp với mình.

Framework cũng vậy — hiểu mechanism, rồi tự calibrate.
Mỗi người khác nhau. Không có 1 đáp án đúng cho tất cả.

**Data thực tế = thước đo cao nhất.**
Framework có thể sai. Bất kỳ ai cũng có thể validate, falsify, hoặc refine.
Nghiên cứu mới mạnh hơn → framework cần cập nhật → đó là tiến bộ.

**Framework khác mainstream ở ~20 vị trí** (có evidence cụ thể):
- Dopamine ≠ reward/pleasure
- Prediction error = nền tảng quan trọng, chưa đủ cho con người
- Mirror neuron ≠ hardware module bẩm sinh
- Cortisol ≠ "stress hormone"
- ...và 16 reframe khác

Chi tiết: xem `Ask-AI.md` §3.

---

## Contribute

This framework is a hypothesis — not established science.
It connects well-supported findings into a unified model,
but the connections themselves are new and unvalidated.

**Why this matters:**

We built the most powerful external tool in history — AI.
Now we need to understand the internal system that wields it.

1. **Old calibration systems are failing.**
   For hundreds of thousands of years, society auto-calibrated individuals
   through 7 functions (direction, push, pull, repair, check, identity,
   connection). Modernity, technology, and AI are breaking all 7
   simultaneously — for the first time in history.
   Self-calibration is becoming a necessary skill — but it requires
   understanding our own mechanisms.
   → Deep analysis: [`Social-Calibration.md`](Research/Global/Social-Calibration.md)

2. **AI amplifies whatever self-model we operate on.**
   Wrong model + AI = amplified mistakes.
   Right model + AI = amplified growth.
   As technology moves closer to the body (brain-computer interfaces,
   neural implants), understanding the system before augmenting it
   becomes essential.
   → Deep analysis: [`AI-Self-Model.md`](Research/Global/AI-Self-Model.md)

3. **We need to evolve intentionally.**
   Before AI, society pushed adaptation through competition and norms.
   In the AI era, we increasingly drive our own growth —
   which requires knowing how motivation, learning, and behavior
   actually work, not folk models ("just try harder", "dopamine = reward").
   → Deep analysis: [`Human-AI-Future.md`](Research/Global/Human-AI-Future.md)

If the framework is largely correct, it provides a mechanism-based compass
for this self-understanding. If parts are wrong, finding them early
benefits everyone. We all gain from knowing which parts hold up.

**Current stage: Verify or Falsify.**

The framework needs critical examination, not adoption.
Challenge the mechanisms. Test the predictions. Find what breaks.
Every falsification = progress. Every verification = confidence.

**How you can participate (by current impact):**

① **Neuroscience researcher** — Verify the biological mechanisms.
   Do the claimed pathways hold up? Where does the evidence diverge?
   Key claims to test: dopamine as salience signal (not reward),
   cortisol as change-readiness amplifier (not "stress hormone"),
   mirror neuron rejection, body-base as primary behavioral driver.

② **Psychologist / Therapist** — Test the behavioral predictions.
   Do the patterns match clinical observation?
   Key prediction: "knowing but not doing" = two-system architecture
   (PFC ≠ compiled body-base), not willpower failure.

③ **Philosopher of Science** — Evaluate the epistemological position.
   Are the claims properly falsifiable?
   Is the unified model overreaching or well-constrained?

④ **Educator / Parent** — Test the learning and development principles.
   Does the chunk-based learning model match
   actual child development and classroom observations?

⑤ **Anyone** — Use the framework, test it against your experience.
   Your body is the final arbiter. Report what doesn't match.

---

## Ghi chú

**AI:** Khuyến cáo dùng AI có context lớn để đảm bảo độ chính xác.
Claude Opus (1M context) cho kết quả tốt nhất với framework này.

**Ngôn ngữ:** Tiếng Việt chủ đạo + thuật ngữ chuyên môn tiếng Anh.

**Quy mô:** ~170 files phân tích, ~120,000+ dòng, version 7.8 (2026).

**Privacy:** This framework is entirely text — no software, no code execution,
no data collection or storage of any kind.
However, when you use AI to ask personal questions,
your data is processed by the AI service you choose.
Use reputable AI services and review their privacy policies.

**License:** [CC0 1.0 — Public Domain.](LICENSE)
Use, share, adapt freely. No permission needed. No credit required.

---

## Keywords

**Framework** · `unified theory of human behavior` · `predictive processing framework` · `body-brain interaction` · `behavioral neuroscience model`

**Science** · `embodied cognition` · `interoception` · `incentive salience` · `affective neuroscience` · `developmental neuroscience` · `dopamine is not reward` · `somatic marker hypothesis` · `social cognition` · `prediction error` · `neuroscience of education` · `neuroscience of motivation` · `addiction mechanisms` · `emotional regulation` · `behavioral science`

**Understanding** · `understanding human behavior` · `why we feel what we feel` · `body mind connection` · `self-understanding` · `how the brain works` · `child brain development` · `why knowing is not doing` · `emotional intelligence` · `brain-based parenting` · `human motivation`