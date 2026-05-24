# Neuro-Measurement — Mục tiêu & Phương pháp đo lường

> **Status**: Sơ lược. Chưa drill.
> **Version**: v0.2
> **Created**: 2026-05-10
> **Position**: Research/ — ứng dụng framework vào đo lường trạng thái não trong môi trường làm việc

---

## §1. Bối cảnh

Não xử lý theo nhiều kiểu activation khác nhau:

| Kiểu | Số vùng sáng | Temporal | Phù hợp task | Ví dụ |
|---|---|---|---|---|
| Gọn-ổn định | Ít (1-2) | Rất ổn | Routine expert | Coder viết code quen |
| Rộng-ổn định | Nhiều (3-5) | Ổn, đồng bộ | Novel trong domain quen | Architect thiết kế system |
| Rộng-nhảy | Nhiều (5+) | Thay đổi liên tục | Cross-domain discovery | Pattern jump, brainstorm |
| Overload | Nhiều | Hỗn loạn | Không phù hợp task nào | "Loạn hết cả đầu" |

Mỗi kiểu có ưu nhược riêng. Không kiểu nào "tốt hơn" — chỉ có phù hợp hay không phù hợp với task hiện tại.

**Vấn đề hiện tại**: Không ai biết mình đang ở trạng thái nào → không tối ưu được → làm việc sai trạng thái (ép creative khi đang overload, ép focus khi đang creative flow).

**Câu hỏi core**: Có thể đo lường trạng thái não real-time, rẻ, trong môi trường làm việc thật — đủ tin cậy để hành động theo không?

---

## §2. Mục tiêu

### 2.1 Đo lường trạng thái cá nhân (real-time)
- Khi nào đang focused (chain logic, nên tiếp tục)
- Khi nào đang creative flow (pattern jump hiệu quả — để yên, đừng disturb)
- Khi nào đang eustress (căng thẳng tích cực — approach motivation, nên cố thêm)
- Khi nào đang distress (căng thẳng tiêu cực — avoidance, gần overload, nên giảm)
- Khi nào đang fatigue nhưng chưa tự nhận ra
- Khi nào đang neural wear (kiệt sức kéo dài, cần nghỉ dài hạn)

### 2.2 Feedback loop với kết quả thực tế
- Kết hợp measurement data với analytics: user retention, A/B test results, gameplay quality metrics
- Tìm correlation: trạng thái não nào → output có giá trị nhất
- Phân biệt: "sáng tạo thật" (output verified tốt) vs "tưởng sáng tạo" (output kém)
- Calibrate cá nhân: mỗi người có pattern riêng, baseline riêng

### 2.3 Ứng dụng team (game dev)
- Tool hỗ trợ **tự nhận biết**, KHÔNG phải tool giám sát
- Mỗi người tự thấy trạng thái bản thân → tự quyết khi nào nghỉ/tiếp
- Tối ưu team workflow: ai đang creative thì đừng kéo vào meeting
- Track neural wear theo thời gian → phát hiện burnout sớm

---

## §3. Phương pháp đo lường

### 3.1 EEG (điện não đồ) — Quantitative, real-time

**Đo được (khá tốt):**

| Trạng thái | EEG Signal | Ghi chú |
|---|---|---|
| Focused bình thường | Beta (13-30Hz) vừa phải, alpha thấp | Tin cậy cao |
| Creative flow | Alpha-theta crossover (8-12Hz giao 4-8Hz) | Khá, nhưng cần phân biệt với drowsy |
| Eustress (căng tích cực) | Beta vừa + **frontal trái > phải** (approach) | Frontal asymmetry = key signal |
| Distress (căng tiêu cực) | High-beta + **frontal phải > trái** (avoidance) | Frontal asymmetry = key signal |
| Buồn ngủ / mất tập trung | Theta tăng trong task cần beta | Tin cậy cao |

**Đo kém:**

| Trạng thái | Vì sao kém | Cần bổ sung gì |
|---|---|---|
| Neural wear (kiệt sức mãn tính) | EEG chỉ snapshot, wear là trạng thái kéo dài | HRV theo dõi nhiều ngày |
| Burnout vs mệt thường | EEG thấy giống nhau (theta cao) | HRV + cortisol + self-report |
| Vùng não cụ thể nào sáng | Consumer EEG spatial resolution kém | fMRI (đắt, không practical) |

**Ưu điểm**: Real-time, quantifiable, đeo được khi làm việc.
**Nhược điểm**: Cần calibrate cá nhân, consumer-grade có noise, đeo lâu có thể khó chịu.

### 3.2 HRV + Wearable — Quantitative, passive

Heart Rate Variability = chỉ số biến thiên nhịp tim. Phản ánh trạng thái autonomic nervous system.

| Trạng thái | HRV Signal |
|---|---|
| Thư giãn, recovery | HRV cao (parasympathetic dominant) |
| Stress (cả eustress và distress) | HRV giảm (sympathetic dominant) |
| Neural wear / burnout | HRV baseline giảm dần qua nhiều ngày/tuần |
| Overtraining | HRV sáng thức dậy thấp bất thường |

**Thiết bị**: Apple Watch, Oura Ring, Whoop, Garmin — đã có sẵn, rẻ, đeo 24/7.
**Ưu điểm**: Passive (không cần nghĩ tới), track dài hạn, phát hiện wear/burnout.
**Nhược điểm**: Không phân biệt được eustress vs distress (chỉ thấy "stress"), không real-time cho cognitive state.

**→ Bổ sung tốt cho EEG**: EEG đo cognitive state real-time, HRV đo physiological load dài hạn.

### 3.3 Giao tiếp trò chuyện — Qualitative, high-bandwidth

Trò chuyện vu vơ trong team = đo lường qualitative tự nhiên nhất.

**Detect tốt:**
- Neural wear mãn tính → giọng nói, năng lượng, cách phản ứng thay đổi
- Emotional state → micro-expression, pattern giao tiếp
- Motivation shift → cách nói về work thay đổi (hứng thú vs nghĩa vụ)
- Context mà thiết bị không capture được (vấn đề cá nhân, team dynamics)

**Detect kém:**
- Người giỏi che giấu → vẫn rò rỉ nhưng cần người quan sát tinh
- Không quantify được → "thấy mệt" nhưng mệt bao nhiêu?
- Người tự không biết mình overload → quen rồi nên báo "ổn"
- Không track được trend dài hạn

**→ Không thay thế thiết bị, nhưng thiết bị cũng không thay thế giao tiếp. Bổ sung nhau.**

### 3.4 Behavioral metrics — Quantitative, passive

Đo gián tiếp qua hành vi làm việc:

| Metric | Có thể reflect | Hạn chế |
|---|---|---|
| Keystroke dynamics (tốc độ, pattern gõ) | Fatigue, cognitive load | Cần baseline cá nhân |
| Mouse movement patterns | Attention, hesitation | Noise nhiều |
| Commit frequency / code quality | Productive state | Lag time (đo sau, không real-time) |
| Break patterns (tự nghỉ khi nào) | Self-regulation | Bị ảnh hưởng bởi deadline |

**Ưu điểm**: Hoàn toàn passive, không cần đeo gì, data có sẵn.
**Nhược điểm**: Indirect — correlation chứ không phải causation. Cần lượng data lớn mới thấy pattern.

---

## §4. So sánh tổng hợp

| Phương pháp | Real-time | Dài hạn | Eustress vs Distress | Neural wear | Cost | Invasiveness |
|---|---|---|---|---|---|---|
| EEG | ✅ | ❌ | ✅ (frontal asymmetry) | ❌ | $250-1000 | Trung bình (đeo headband) |
| HRV wearable | ⚠️ (chậm) | ✅ | ❌ | ✅ | $100-400 | Thấp (đồng hồ/nhẫn) |
| Giao tiếp | ✅ | ⚠️ (không quantify) | ✅ (nếu tinh) | ✅ (nếu quan sát lâu) | Free | Không |
| Behavioral | ❌ | ✅ | ❌ | ⚠️ | Free | Không |

**Kết luận sơ bộ**: Không phương pháp nào đủ một mình. Combo tối ưu có thể là:
- **EEG** cho real-time cognitive state (focus/creative/stress type)
- **HRV** cho long-term physiological load (wear/burnout detection)
- **Giao tiếp** cho context và nuance mà thiết bị không capture
- **Behavioral + Analytics** cho correlation với output thực tế

---

## §5. Liên kết framework

- **Neural efficiency** (Neubauer & Fink, 2009): Expert = ít activation hơn → EEG có thể track skill development?
- **4 kiểu activation**: Gọn-ổn / rộng-ổn / rộng-nhảy / overload → EEG temporal stability phân biệt được
- **Frontal asymmetry**: Left (approach) vs Right (avoidance) → trực tiếp map vào eustress vs distress
- **Evaluative reward** (pattern match) vs implementation cost → alpha-theta crossover = Evaluative moment?
- **Body-base feedback**: Thiết bị = "externalize" cái mà body đã biết nhưng chưa articulate
- **PFC Configuration**: 6 modes → liệu EEG signature khác nhau giữa các config?
- **COMT genotype**: Val/Val vs Met/Met → EEG baseline pattern khác nhau? (cần drill)

---

## §6. Câu hỏi mở (chưa drill)

1. **Frontal asymmetry trên consumer EEG**: Muse 2 channels đủ detect không? Hay cần Emotiv 5+?
2. **Creative vs drowsy**: Alpha-theta crossover giống nhau — phân biệt bằng cách nào?
3. **Individual calibration**: Bao lâu để có baseline cá nhân đủ tin cậy?
4. **Framework mapping**: EEG signatures có map được vào PFC Configuration modes không?
5. **Wear detection combo**: EEG snapshot + HRV trend → algorithm nào phát hiện wear sớm?
6. **Giao tiếp structured**: Có framework câu hỏi nào giúp detect state qua trò chuyện không?

---

## §7. Cross-References

- Core-Deep-Dive/PFC/PFC-Hardware.md — COMT, DRD4, working memory hardware
- Core-Deep-Dive/PFC/PFC-Configuration.md — 6 config modes, control spectrum
- Core-Deep-Dive/PFC/PFC-Function.md — 24 functions, sub-region mapping
- Core-Deep-Dive/Body-Base/Body-Feedback/Reward-Signal-Architecture.md — Evaluative/Direct-State reward
- Core-Deep-Dive/Body-Base/Body-Feedback/Body-Feedback-Mechanism.md — body signal processing
- Core-Deep-Dive/Body-Base/Body-Feedback/Cortisol-Baseline.md — stress physiology
