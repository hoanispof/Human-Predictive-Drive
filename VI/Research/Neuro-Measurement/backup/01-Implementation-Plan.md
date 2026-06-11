# Neuro-Measurement — Kế hoạch triển khai

> **Status**: Sơ lược. Chưa drill.
> **Version**: v0.1
> **Created**: 2026-05-10
> **Position**: Research/Neuro-Measurement/ — practical implementation roadmap
> **Depends on**: 00-Goals.md

---

## §1. Nguyên tắc triển khai

1. **Tự mình trước, team sau** — không deploy tool chưa tự validate
2. **Rẻ trước, đắt sau** — bắt đầu với thiết bị rẻ nhất có thể, upgrade khi có evidence
3. **Hỗ trợ, không giám sát** — data thuộc về cá nhân, không phải manager
4. **Correlation trước, causation sau** — tìm pattern trước, giải thích sau
5. **Body-base vẫn là primary** — thiết bị bổ sung, không thay thế tự cảm nhận

---

## §2. Thiết bị chi tiết (cần drill thêm)

### 2.1 EEG

| Thiết bị | Giá | Channels | Frontal Asymmetry? | SDK/API | Đeo lâu được? | Ghi chú |
|---|---|---|---|---|---|---|
| Muse 2 | ~$250 | 4 (2 frontal + 2 temporal) | Sơ bộ (2 frontal) | Có (Muse SDK, third-party) | Khá (headband nhẹ) | Entry-level tốt nhất |
| Muse S | ~$400 | 4 | Tương tự Muse 2 | Tương tự | Tốt hơn (mềm hơn) | Sleep tracking thêm |
| Emotiv Insight | ~$500 | 5 | Tốt hơn (5 positions) | Emotiv SDK (có free tier) | Trung bình | Cân bằng giá/chất |
| Emotiv Epoc X | ~$900 | 14 | Tốt (nhiều channels) | Emotiv SDK | Kém hơn (nặng hơn) | Research-grade |
| OpenBCI Cyton | ~$500-1000 | 8-16 | Tùy setup | Open-source (Python/JS) | Kém (DIY mount) | Tùy biến cao nhưng cần kỹ thuật |

**Recommendation sơ bộ**: Bắt đầu Muse 2 ($250). Nếu frontal asymmetry không đủ → upgrade Emotiv Insight ($500).

### 2.2 HRV

| Thiết bị | Giá | HRV accuracy | Đeo 24/7? | Ghi chú |
|---|---|---|---|---|
| Oura Ring (Gen 3) | ~$300 + $6/tháng | Tốt | Có (nhẹ, kín đáo) | Best cho passive tracking |
| Apple Watch | ~$400+ | Khá | Có (quen rồi) | Nếu đã có thì dùng luôn |
| Whoop 4.0 | ~$30/tháng (subscription) | Rất tốt | Có | Tốt nhất cho HRV nhưng subscription |
| Garmin (mid-range) | ~$200-400 | Khá | Có | Rẻ, bền |

**Recommendation sơ bộ**: Dùng đồng hồ/nhẫn đã có. Nếu chưa có → Oura Ring (kín đáo nhất, HRV tốt).

---

## §3. Prototype Phases

### Phase 0: Preparation (1 tuần)
- [ ] Chọn và mua thiết bị EEG (recommend: Muse 2)
- [ ] Setup app/SDK, test kết nối
- [ ] Thiết kế log sheet đơn giản: timestamp + trạng thái EEG + đang làm gì + self-report cảm giác
- [ ] Xác định output metrics sẵn có (analytics nào track được?)

### Phase 1: Self-measurement (2-4 tuần)
- [ ] Đeo EEG khi làm việc, log liên tục
- [ ] Cuối mỗi ngày: ghi nhận output (code commits, gameplay changes, ideas generated)
- [ ] Cuối mỗi ngày: self-report (1-5: energy, creativity, satisfaction)
- [ ] Song song: HRV tracking 24/7 nếu có wearable

**Output Phase 1**: Raw data + cảm nhận sơ bộ: "EEG có match với cảm giác thật không?"

### Phase 2: Pattern Analysis (1-2 tuần)
- [ ] Phân tích correlation: EEG states × output quality
- [ ] Phân tích: HRV trend × productive days vs burnout days
- [ ] Tìm: có signal nào predict "ngày mai sẽ mệt" không?
- [ ] Tìm: alpha-theta crossover có correlate với output sáng tạo thật không?
- [ ] Honest assessment: EEG consumer-grade có đủ signal hay toàn noise?

**Output Phase 2**: Report: "Có đáng tiếp không? Signal gì đáng tin? Cái gì noise?"

### Phase 3: Pilot with 2-3 người (2-4 tuần, NẾU Phase 2 positive)
- [ ] Mời 2-3 team member tự nguyện
- [ ] Mỗi người calibrate baseline riêng (1-2 ngày)
- [ ] So sánh patterns giữa các người: giống/khác thế nào?
- [ ] Test: recommendation engine đơn giản ("nên nghỉ" / "đang flow, đừng disturb")
- [ ] Thu feedback: helpful hay annoying?

**Output Phase 3**: "Tool này có giá trị cho team không? Hay chỉ novelty?"

### Phase 4: Team workflow (NẾU Phase 3 positive)
- [ ] Design dashboard cá nhân (mỗi người chỉ thấy data của mình)
- [ ] Integration với work schedule (optional: "focus hours" dựa trên EEG pattern)
- [ ] Long-term: combine EEG + HRV + analytics → personal productivity profile
- [ ] Iterate based on feedback

---

## §4. Rủi ro & Mitigation

| Rủi ro | Xác suất | Impact | Mitigation |
|---|---|---|---|
| Consumer EEG toàn noise, không có signal | Trung bình | Cao — dừng project | Phase 1-2 validate trước khi invest thêm |
| Team thấy bị giám sát | Cao nếu design sai | Cao — mất trust | Data thuộc cá nhân, opt-in, no manager access |
| Novelty effect (hứng 2 tuần rồi bỏ) | Cao | Trung bình | Design để passive, không cần effort hàng ngày |
| Overthink data, quên làm việc | Trung bình | Thấp | Set rule: check EEG 2 lần/ngày max, không liên tục |
| Thiết bị khó chịu, đeo lâu mỏi | Trung bình | Trung bình | Test comfort Phase 1 trước |

---

## §5. Metrics đánh giá thành công

**Phase 1-2 thành công nếu:**
- Phân biệt được ít nhất 3 trạng thái (focus / creative / fatigue) với accuracy > 70%
- EEG data correlate (r > 0.3) với self-report hoặc output quality
- Bản thân thấy useful (body-base check: "biết thêm cái này có thay đổi hành vi không?")

**Phase 3-4 thành công nếu:**
- >50% pilot members tiếp tục dùng sau 2 tuần (không phải novelty)
- Ít nhất 1 case: phát hiện overload/wear mà bản thân chưa tự nhận ra
- Team workflow cải thiện measurable (ít interrupt creative flow hơn)

---

## §6. Câu hỏi drill cho sessions sau

1. **EEG signal processing**: SDK nào dễ dùng nhất? Python libraries? Real-time streaming?
2. **Frontal asymmetry algorithm**: Tính thế nào từ raw EEG? Threshold bao nhiêu?
3. **HRV × EEG fusion**: Combine 2 nguồn data thế nào? Existing research?
4. **Privacy-first design**: Architecture nào đảm bảo data không leak? Local-only processing?
5. **Comfort test**: Review thực tế từ người đeo Muse/Emotiv 8h/ngày?
6. **Game dev specific**: Có research nào về EEG × creative work (không chỉ coding)?

---

## §7. Cross-References

- 00-Goals.md — mục tiêu và phương pháp đo lường
- Core-Deep-Dive/PFC/PFC-Hardware.md — COMT baseline → EEG baseline?
- Core-Deep-Dive/Body-Base/Body-Feedback/Cortisol-Baseline.md — stress physiology × HRV
- Research/Health-Conditions/Hijack/Addiction-Analysis.md — dopamine loop awareness (tránh gamify measurement)
