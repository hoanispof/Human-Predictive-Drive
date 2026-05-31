# Plan: Final Abbreviation Cleanup

**Ngày tạo**: 2026-05-31
**Mục tiêu**: Rà soát và sửa TẤT CẢ viết tắt tự tạo còn sót trong production files.
**Phương pháp**: Tìm → Ghi nhận → Fix → Tìm thêm → Fix → Re-scan toàn bộ.

---

## §1 — QUY ƯỚC (nhắc lại)

KHÔNG viết tắt bất kỳ concept nào.
Ngoại lệ DUY NHẤT: thuật ngữ học thuật mainstream (PFC, VTA, vmPFC, DRN, fMRI, EEG, HRV, COMT, HPA, SNC, GABA, LTP, ACC, OFC, DLPFC, NAcc, mOFC, VTC, DAT, DRD4, DMN, TBW, EF, WM, SCR, SE, PTSD, OCD, ADHD, DNA, RNA, TPJ, FFG) + labels (M1-M4, H1-H12, §1-§7, GD-Q1-Q8).

---

## §2 — DANH SÁCH VIẾT TẮT TÌM THẤY

### Đợt 1 (2026-05-31, scan 5 phase)

| # | Viết tắt | Tên đầy đủ | File | Dòng | Status |
|---|----------|-----------|------|------|--------|
| 1 | RSA | Reward-Signal-Architecture | Body-Feedback-Precondition.md | 103 | ✅ |
| 2 | RSA | Reward-Signal-Architecture | Body-Feedback-Precondition.md | 119 | ✅ |
| 3 | RSA | Reward-Signal-Architecture | Body-Feedback-Precondition.md | 186 | ✅ |
| 4 | RSA | Reward-Signal-Architecture | Body-Feedback-Precondition.md | 515 | ✅ |
| 5 | RSA | Reward-Signal-Architecture | Body-Feedback-Precondition.md | 788 | ✅ |
| 6 | RSA | Reward-Signal-Architecture | Body-Feedback-Precondition.md | 1328 | ✅ |
| 7 | BFM | Body-Feedback-Mechanism | Body-Feedback-Precondition.md | 104 | ✅ |
| 8 | BFM | Body-Feedback-Mechanism | Body-Feedback-Precondition.md | 121 | ✅ |
| 9 | BFM | Body-Feedback-Mechanism | Body-Feedback-Precondition.md | 1339 | ✅ |
| 10 | BF | Body-Feedback | Body-Feedback-Precondition.md | 105 | ✅ |
| 11 | DSA | Dissonance-Signal-Architecture | Body-Feedback-Precondition.md | 106 | ✅ |
| 12 | DSA | Dissonance-Signal-Architecture | Body-Feedback-Precondition.md | 120 | ✅ |
| 13 | DSA | Dissonance-Signal-Architecture | Body-Feedback-Precondition.md | 1254 | ✅ |
| 14 | DSA | Dissonance-Signal-Architecture | Body-Feedback-Precondition.md | 1280 | ✅ |
| 15 | UV | Uncanny-Valley | Human-AI-Future.md | 290 | ✅ |
| 16 | UV | Uncanny-Valley | Human-AI-Future.md | 783 | ✅ |
| 17 | UV | Uncanny-Valley | Human-AI-Future.md | 787 | ✅ |
| 18 | UV | Uncanny-Valley | Human-AI-Future.md | 791 | ✅ |
| 19 | UV | Uncanny-Valley | Human-AI-Future.md | 798 | ✅ |
| 20 | UV | Uncanny-Valley | Uncanny-Valley.md | 207 | ✅ |
| 21 | BF-Mech | Body-Feedback-Mechanism | Uncanny-Valley.md | 1295 | ✅ |
| 22 | UV | Uncanny-Valley | Research/01-File-Index.md | 22 | ✅ |
| 23 | CSP | Collective-Schema-Pressure | Gap-Distribution-Profile.md | 1220 | ✅ |
| 24 | GD-Profile | Gap-Distribution-Profile | Coordination-Node.md | 672 | ✅ |
| 25 | FLT | Feeling-Literacy-Training | 02-Cross-Network-Transfer.md | 1270 | ✅ |
| 26 | DKM | Domain-Knowledge-Map | html-page/global-index.json | 3427 | ✅ |

**Tổng đợt 1: 26 instances, 9 viết tắt, 8 files**

### Đợt 2+ (thêm khi phát hiện mới)

_(chưa có)_

---

## §3 — TIẾN TRÌNH

### Phase A: Fix đợt 1 — ✅✅ ALL DONE (2026-05-31)
- ✅ File 1: Body-Feedback-Precondition.md (14 instances: RSA×6, BFM×3, BF×1, DSA×4)
- ✅ File 2: Human-AI-Future.md (5 instances: UV×5) — bảng box-drawing mở rộng cột 4
- ✅ File 3: Uncanny-Valley.md (2 instances: UV×1, BF-Mech×1) — UV→"uncanny valley", BF-Mech split 2 dòng
- ✅ File 4: Research/01-File-Index.md (1 instance: UV×1)
- ✅ File 5: Gap-Distribution-Profile.md (1 instance: CSP×1)
- ✅ File 6: Coordination-Node.md (1 instance: GD-Profile×1)
- ✅ File 7: 02-Cross-Network-Transfer.md (1 instance: FLT×1)
- ✅ File 8: html-page/global-index.json (1 instance: DKM×1)

### Phase B: Tìm thêm — ✅✅ ALL CLEAN (2026-05-31)
- ✅ Scan 14 patterns (10 đã biết + 4 bổ sung: BFP, GBN, RPE, SE-as-Simulation-Engine)
- ✅ Kết quả: 0 framework abbreviation trong production files
- ✅ 1 false positive OK: BF = Basal Forebrain (neuroscience) trong Neural-Processing-Flow.md
- ✅ Không có đợt 2 — không tìm thấy viết tắt mới

### Phase C: Re-scan toàn bộ
- ⬜ Scan lại toàn bộ framework với pattern rộng: `[A-Z]{2,5} §` + standalone abbreviations
- ⬜ Cross-check danh sách 30+ viết tắt đã cleanup trước đây (SPM, BPGR, EVD, BFL, HAF, ASM, AM, EA, EC, VP, SE, IF, PR, EAE, EAC, CB, RS, BA, BS, BP, BB, BC, LW, IBM, SAL + 9 mới)
- ⬜ Xác nhận 0 viết tắt framework trong production files

---

## §4 — ĐÃ XÁC NHẬN SẠCH (từ scan 2026-05-31)

Các viết tắt sau đã verify = 0 instances trong production files:
SPM, BPGR, EVD, BFL, HAF, ASM, AM, EA, EC, VP, SE, IF, PR, EAE, EAC, CB, RS, BA, BS, BP, BB, BC, LW, IBM, SAL

---

## §5 — GHI CHÚ

- Scope: production files ONLY (loại trừ backup/, _backup/, plan-*, rename_backup/)
- False positives cần giữ nguyên: VP(Ventral Pallidum), EC(Entorhinal Cortex), BA(Vietnamese "ba"/Bachelor), BS(Vietnamese "bác sĩ"), CN(Vietnamese), BC(historical dates), SE(Somatic Experiencing), GDP(economics), AM(English "am"), PR(Pull Request), SCR(Skin Conductance Response)
- RSA: collision với neuroscience "respiratory sinus arrhythmia" → thêm lý do phải viết đầy đủ
