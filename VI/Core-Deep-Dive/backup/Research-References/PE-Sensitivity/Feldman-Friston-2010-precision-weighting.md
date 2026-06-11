# Feldman & Friston 2010 — Attention, Uncertainty, Precision Weighting

> **Full Citation:** Feldman H, Friston KJ. "Attention, uncertainty, and free-energy." *Frontiers in Human Neuroscience* 4: article 215, 2010. DOI: 10.3389/fnhum.2010.00215. PMCID: PMC3001758
> **Cited in:** PE-Sensitivity.md §3 (② Precision Weighting)
> **Framework confidence tag:** 🟡 (suy luận từ 🟢 này)

---

## What the Framework Claims

PE-Sensitivity.md §3, dòng 91:
> "🟡 (suy luận từ 🟢 Feldman & Friston 2010 — precision weighting trong predictive coding)"

Framework dùng study này để support concept: não **đánh giá PE đáng tin cỡ nào** trước khi "thưởng" — gán trọng số (precision) cho prediction error. Người khác nhau gán precision khác nhau → DA fire nhanh/chậm → explore vs. deepen.

---

## Original Study

### Context & Question
Paper hỏi: **Attention có thể được giải thích trong khuôn khổ Bayesian inference không?** Thay vì coi attention là một module riêng, liệu nó có phải là hệ quả tự nhiên của một cơ chế tổng quát hơn — cụ thể là việc tối ưu hóa **precision** (độ tin cậy, nghịch đảo của variance) của sensory signals?

### Method
**Đây là paper lý thuyết và computational — không có participants hay empirical data.**

Framework được dùng:
- **Free-energy principle** (Karl Friston): não minimize free energy = một bound on surprise/log-evidence → perception = variational Bayesian inference
- **Hierarchical generative models với state-dependent noise:** precision của sensory signal có thể được infer, không chỉ assumed cố định
- **Neuronal simulations** của Posner spatial cueing paradigm (valid cue vs. invalid cue reaction times)
- **Biased competition simulation:** 2 stimuli cạnh tranh → mô hình tự nhiên reproduces winner-take-all
- Model inversion bằng gradient descent trên free energy

### Key Claims và Findings

1. **Attention = precision optimization:**
   > "Attention is the process of optimizing synaptic gain to represent the precision of sensory information (prediction error) during hierarchical inference."

2. **Precision được encode bởi synaptic gain:** Precision của prediction error tại mỗi level của cortical hierarchy = gain (amplification) của neurons signal prediction error. Attend một channel = tăng gain của units đó.

3. **State-dependent noise là cơ chế chính:** Khi states của world (ví dụ: cue spatial) thay đổi precision của sensory data → tối ưu hóa free energy tự nhiên tạo ra attentional phenomena — không cần attention mechanism riêng biệt.

4. **Simulation results:**
   - Valid cue: phản ứng nhanh hơn ~20ms, suppressed prediction error
   - Invalid cue: enhanced late components (analogous P3) — context-updating prediction error
   - Biased competition: emerges naturally, không cần lateral inhibition riêng

### Authors' Conclusions
Framework "unifies psychological constructs of attention with neurophysiological mechanisms." Attention "is more concerned with optimizing the uncertainty or precision of probabilistic representations, rather than what is being represented." Attention là direct consequence của Bayesian inference, không phải independent module.

---

## Verification Assessment

### Framework dùng đúng không?
**PARTIALLY — concept đúng, nhưng scope khác**

### Alignment Details

**Điều framework lấy từ paper:**
Concept **precision weighting** = không phải mọi PE đều được xử lý như nhau. Não gán trọng số tin cậy cho mỗi PE trước khi update model. Đây là **concept trực tiếp từ paper**, dùng đúng.

**Điều framework extend thêm (không trong paper):**
Paper nói về **attention** — cơ chế não ưu tiên sensory channel nào. Framework transplant concept này sang **individual differences** trong PE Sensitivity: một số người gán precision nhanh/tin ngay, người khác cẩn thận hơn.

Paper **không** study individual differences trong precision weighting. Paper model là về cơ chế chung — không phân biệt tại sao người A gán precision nhanh hơn người B.

**Tức là:** Framework lấy concept precision weighting (đúng) và extrapolate nó thành inter-individual parameter (chưa có evidence từ paper này).

### What the Study Does NOT Say
- Không đo người thật — chỉ là computational model
- Không study individual differences trong precision weighting
- Không address learning: "we will focus on perceptual inference and return to learning in a later paper"
- Không model spatial receptive fields
- Không provide empirical validation — chỉ tạo predictions
- Scope: directed spatial attention trong Posner paradigm — không general hơn
- Không liên quan đến reward/dopamine trực tiếp — framework là về sensory attention, không PE trong nghĩa reward

---

## Related References
- [Thompson-Spencer-1966-habituation.md](Thompson-Spencer-1966-habituation.md) — ③ Habituation: cùng chủ đề "tốc độ update model"

---

## Notes

**Đây là paper quan trọng nhất cần phân biệt rõ:**

Feldman & Friston nói về **precision weighting trong attention** — cụ thể là cách não ưu tiên sensory channel nào khi có nhiều signals cạnh tranh. Đây là cơ chế **trong-một-người**.

Framework HPD extrapolate thành **khác biệt giữa người** — người A vs. người B có precision weighting rate khác nhau. Đây là leap không có trong paper gốc.

Leap này có thể hợp lý về mặt logic (nếu cơ chế tồn tại, tại sao không có variation?), nhưng paper không support nó trực tiếp. Framework cần tag phần này là 🔴 thay vì 🟡.

Ngoài ra, paper không liên quan đến **dopamine** (DA) — framework dùng nó để nói về DA firing patterns, nhưng Feldman & Friston là computational framework, không phải neurochemistry study.
