# Thompson & Spencer 1966 — Habituation: Model Phenomenon

> **Full Citation:** Thompson RF, Spencer WA. "Habituation: A model phenomenon for the study of neuronal substrates of behavior." *Psychological Review* 73(1):16–43, 1966. DOI: 10.1037/h0022681. PMID: 5324565
> **Cited in:** PE-Sensitivity.md §4 (③ Habituation Rate)
> **Framework confidence tag:** 🟡 (suy luận từ 🟢 này)

---

## What the Framework Claims

PE-Sensitivity.md §4, dòng 119:
> "🟡 (suy luận từ 🟢 Thompson & Spencer 1966 — habituation; synaptic plasticity research)"

Framework dùng study này để support concept ③ Habituation Rate:
> "= Tốc độ update prediction model → PE BIẾN MẤT khi model đã cập nhật. Sau khi chunk mới hình thành, bao lâu nó trở thành 'đã biết' (PE → 0)?"

---

## Original Study

### Context & Question
Field đang cố hiểu cách kết nối behavioral changes với neuronal mechanisms. Vấn đề: thí nghiệm intact-animal không thể phân tích ở mức neuronal; simplified preparations (như spinal reflex) không rõ có liên quan đến behavior phức tạp không.

**Đề xuất của Thompson & Spencer:** Habituation là hiện tượng lý tưởng làm cầu nối — xảy ra cả ở intact organism lẫn simplified preparations, có thể so sánh 2 mức trực tiếp.

**Câu hỏi:** Habituation của spinal flexion reflex có tuân theo cùng 9 parametric rules như behavioral habituation ở intact organism không?

### Method
- **Species:** Mèo (*Felis catus*)
- **Preparation:** **Acute spinal cat** — cắt tủy sống (spinal transection), isolate khỏi brain. Đây là preparation đơn giản hóa để loại bỏ supraspinal influences
- **Response:** Hindlimb flexion reflex — reflex tủy sống khi kích thích da chân sau
- **Neural recording:** Extracellular recordings từ spinal interneurons + ventral root recordings
- **Approach:** (1) Review toàn bộ behavioral habituation literature + (2) Original spinal cat data → so sánh

### Key Findings — 9 Parametric Characteristics của Habituation

Thompson & Spencer review literature và tổng hợp thành **9 đặc tính định nghĩa habituation**:

1. Lặp lại stimulus → response giảm dần (habituation). Thường là negative exponential function
2. Nếu stimulus ngừng → response phục hồi theo thời gian (spontaneous recovery)
3. Nhiều chu kỳ habituation-recovery → habituation xảy ra ngày càng nhanh hơn (potentiation)
4. Stimulus càng nhanh → habituation càng nhanh/mạnh
5. **Stimulus càng yếu → habituation càng nhanh. Stimulus mạnh có thể không habituate đáng kể**
6. Habituation có thể xảy ra "below zero" — training sau khi response biến mất → recovery chậm hơn
7. Habituation của một stimulus → generalize sang stimuli khác (stimulus generalization)
8. Một stimulus khác (thường mạnh) → phục hồi response đã habituate (dishabituation)
9. Lặp lại stimulus gây dishabituation → dishabituation giảm dần (habituation of dishabituation)

**Phát hiện về dishabituation:** Dishabituation KHÔNG phải là đảo ngược habituation. Đây là quá trình **superimposed sensitization** độc lập — "facilitatory afterdischarge." Habituation vẫn còn đó bên dưới.

**Neural mechanism đề xuất:**
- Habituation = polysynaptic low-frequency depression (synaptic efficacy giảm ở interneurons)
- Dishabituation = superimposed facilitatory afterdischarge
- Long-term habituation = membrane desensitization thêm vào

### Authors' Conclusions
Spinal flexion reflex habituate theo đúng 9 parametric characteristics như behavioral habituation → spinal cord là viable model system. 9 characteristics này có thể serve như "operational definition of habituation."

Tuy nhiên, authors **explicit** gọi neural mechanism proposals là "working hypothesis" — không phải kết luận xác định.

---

## Verification Assessment

### Framework dùng đúng không?
**PARTIALLY — concept đúng, nhưng có mismatch quan trọng về scope**

### Alignment Details

**Điều framework lấy đúng:**
- Habituation là real neurological phenomenon với clear characteristics
- Người khác nhau có thể có habituation rate khác nhau (có biological basis)

**Mismatch 1 — Level of analysis:**
Thompson & Spencer study **spinal reflex ở mèo** — reflexes cơ bản của tủy sống, không phải cognitive processes hay reward learning.

Framework áp dụng concept vào **cognitive PE processing** — "chunk mới hình thành, bao lâu nó trở thành 'đã biết'." Đây là level phức tạp hơn nhiều, xảy ra ở cortex, không phải spinal cord.

**Mismatch 2 — Mechanism claim:**
Framework nói habituation rate được quyết định bởi "synaptic plasticity rate — BDNF, NMDA receptor." Thompson & Spencer nói về "polysynaptic low-frequency depression" ở spinal interneurons — cơ chế khác với long-term synaptic plasticity (LTP/LTD) mà BDNF/NMDA liên quan.

**Mismatch 3 — Individual differences:**
Paper này không study individual differences trong habituation rate. 9 characteristics là universal properties của habituation — không nói ai habituate nhanh hơn ai.

**Điều framework bỏ sót từ paper:**
- **Characteristic 5** quan trọng: stimulus yếu → habituate nhanh, stimulus mạnh → ít/không habituate. Điều này directly liên quan đến Threshold trong framework (chunk lớn = strong stimulus = ít habituate) nhưng framework không kết nối điểm này
- **Stimulus generalization** (characteristic 7) = precursor của ④ Generalization Scope trong framework — nhưng không được cite ở đó

### What the Study Does NOT Say
- Không study habituation ở cognitive/reward domain — chỉ spinal reflex
- Không measure individual differences trong habituation rate
- Không liên quan đến BDNF hay NMDA receptor trực tiếp
- Không study habituation của "chunks" hay "prediction errors" — đây là framework concept không có trong paper
- Neural mechanism proposals là explicitly "speculative" và "working hypothesis"
- Species: mèo, preparation: acute spinal — không trực tiếp generalize đến human cognitive processing

---

## Related References
- [Feldman-Friston-2010-precision-weighting.md](Feldman-Friston-2010-precision-weighting.md) — ② Precision: cùng chủ đề tốc độ update

---

## Notes

**Insight quan trọng bị bỏ sót trong framework:**

Characteristic 5 của Thompson & Spencer: **"The weaker the stimulus, the more rapid and/or more pronounced is habituation. Strong stimuli may yield no significant habituation."**

Trong ngôn ngữ HPD: chunk có PE lớn (strong stimulus) → habituate chậm hơn chunk PE nhỏ. Điều này có nghĩa: **Threshold cao** tự nhiên chọn lọc các chunk PE lớn để process → các chunk đó habituate chậm hơn → **Threshold cao vô tình slow down habituation** của những gì được processed.

Đây là interaction Threshold × Habituation mà framework chưa model rõ.

**Về 9 characteristics:** Đây là empirical taxonomy của habituation, không phải mechanistic explanation. Framework dùng nó như neurochemical basis — không hoàn toàn chính xác. Thompson & Spencer xác lập *phenomenology*, không phải *mechanism*.
