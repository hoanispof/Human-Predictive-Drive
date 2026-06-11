---
title: Natural Language Architecture — Cấu trúc ngôn ngữ tự nhiên
created: 2026-04-16 (N+5 exploration session)
status: REFERENCE — tài liệu tham khảo, đọc nghiền ngẫm
scope: So sánh cấu trúc Tiếng Việt / English / 中文 Mandarin
purpose: Hiểu kiến trúc language thông thường trước khi phân tích external knowledge systems
parent: ../../plan.md (F3 Chunk-External-Development)
language: Tiếng Việt primary + English technical + 中文 với pinyin + dịch nghĩa
note: Mọi ví dụ tiếng Trung đều có phiên âm (pinyin) và dịch nghĩa tiếng Việt
---

# Natural Language Architecture — Cấu trúc ngôn ngữ tự nhiên

> **Mục đích**: Bạn dùng ngôn ngữ mỗi ngày, tuồn tuột không nghĩ. File này "mổ xẻ" cái bạn đang dùng — để thấy CẤU TRÚC bên trong. So sánh 3 ngôn ngữ: Tiếng Việt, English, 中文 (zhōngwén — tiếng Trung).
>
> **Cách đọc**: Không cần đọc 1 lần. Đọc từng phần, nghiền ngẫm, quay lại khi cần. Mỗi phần độc lập.
>
> **Quy ước tiếng Trung**: Mọi ví dụ tiếng Trung đều viết dạng: **汉字 (pīnyīn — dịch nghĩa)**. Ví dụ: 我吃饭 (wǒ chī fàn — tôi ăn cơm).

---

## MỤC LỤC

- §1 — Từ vựng: Các loại từ (Parts of Speech)
  - §1.1 Bảng tổng hợp 11 loại từ
  - §1.2 Classifier vs Article — khác biệt kiến trúc
  - §1.3 Đại từ — 3 hệ thống hoàn toàn khác
  - §1.4 Trợ từ — Vietnamese và Chinese có, English hầu như không
- §2 — Hình thái học: Từ thay đổi hình dạng thế nào (Morphology)
  - §2.1 Ba loại ngôn ngữ: Isolating vs Fusional
  - §2.2 So sánh: Thì (Tense)
  - §2.3 So sánh: Số nhiều (Plural)
  - §2.4 So sánh: So sánh hơn/nhất (Comparative/Superlative)
  - §2.5 Insight: Tiếng Việt là "lego blocks"
- §3 — Cú pháp: Cách ghép từ thành câu (Syntax)
  - §3.1 Trật tự cơ bản SVO
  - §3.2 Word order flexibility + Topic-Comment
  - §3.3 Cấu trúc cụm từ (Phrase Structure) — cây cú pháp
  - §3.4 Modifier order: Trước hay Sau danh từ
  - §3.5 Câu hỏi: 3 cách khác nhau
  - §3.6 Phủ định: Mỗi ngôn ngữ buộc phân biệt khác nhau
  - §3.7 Câu phức: Mệnh đề phụ + liên từ
- §4 — Đặc điểm riêng nổi bật
  - §4.1 Vietnamese: Classifier system chi tiết
  - §4.2 Chinese: Character = hình ảnh + nghĩa
  - §4.3 English: Phrasal verbs + idioms
  - §4.4 Vietnamese: Tone system 6 thanh
  - §4.5 Chinese: Thành ngữ 4 chữ (Chengyu)
- §5 — Tổng hợp so sánh
  - §5.1 Bảng so sánh toàn diện
  - §5.2 Mỗi ngôn ngữ BUỘC chunk gì
  - §5.3 Framework lens: Moderate Whorfian
- §6 — Verbal hierarchy: Từ → Cụm từ → Câu → Đoạn → Bài
- §7 — Construction Grammar: Tại sao word order quan trọng
- §8 — Câu hỏi mở + Liên kết framework

---

## §1 — Từ vựng: Các loại từ (Parts of Speech)

Mọi ngôn ngữ đều phân loại từ vựng thành **nhóm chức năng** — như linh kiện trong máy tính, mỗi loại có vai trò khác nhau. Ngôn ngữ học gọi là "parts of speech" (từ loại).

### §1.1 — Bảng tổng hợp 11 loại từ

| # | Loại từ | Vai trò | Tiếng Việt | English | 中文 (pinyin — nghĩa) |
|---|---|---|---|---|---|
| 1 | **Danh từ** (Noun) | Gọi tên sự vật, người, nơi chốn, khái niệm | chó, bàn, Hà Nội, tình yêu | dog, table, Hanoi, love | 狗 (gǒu — chó), 桌子 (zhuōzi — cái bàn), 爱 (ài — tình yêu) |
| 2 | **Động từ** (Verb) | Hành động hoặc trạng thái | chạy, ăn, nghĩ, là | run, eat, think, is | 跑 (pǎo — chạy), 吃 (chī — ăn), 想 (xiǎng — nghĩ), 是 (shì — là) |
| 3 | **Tính từ** (Adjective) | Mô tả tính chất của danh từ | đẹp, to, nhanh, buồn | beautiful, big, fast, sad | 美 (měi — đẹp), 大 (dà — to), 快 (kuài — nhanh), 悲 (bēi — buồn) |
| 4 | **Trạng từ** (Adverb) | Bổ nghĩa cho động từ, tính từ, hoặc cả câu | rất, nhanh, thường, không | very, quickly, often, not | 很 (hěn — rất), 常 (cháng — thường), 不 (bù — không) |
| 5 | **Đại từ** (Pronoun) | Thay thế danh từ | tôi, bạn, nó, chúng ta | I, you, he, she, we, they | 我 (wǒ — tôi), 你 (nǐ — bạn), 他 (tā — anh ấy), 她 (tā — cô ấy) |
| 6 | **Giới từ** (Preposition) | Chỉ quan hệ không gian, thời gian | ở, trong, trên, với, từ | in, on, at, with, from | 在 (zài — ở/tại), 从 (cóng — từ), 跟 (gēn — với) |
| 7 | **Liên từ** (Conjunction) | Nối từ hoặc nối câu | và, nhưng, hoặc, vì | and, but, or, because | 和 (hé — và), 但是 (dànshì — nhưng), 或 (huò — hoặc), 因为 (yīnwèi — vì) |
| 8 | **Thán từ** (Interjection) | Biểu cảm xúc, kêu gọi | ôi, trời ơi, ồ, chà | oh, wow, ouch, hey | 哦 (ó — ồ), 哇 (wā — woa), 哎 (āi — ôi) |
| 9 | **Mạo từ** (Article / Determiner) | Xác định danh từ (cụ thể hay chung chung) | ❌ KHÔNG CÓ trong tiếng Việt | a, an, the, this, that | ❌ KHÔNG CÓ mạo từ. Dùng 这 (zhè — này), 那 (nà — kia) thay thế |
| 10 | **Loại từ** (Classifier / Measure word) | Đếm và phân loại danh từ | con, cái, chiếc, quyển, tờ,... | ❌ Hầu như KHÔNG CÓ | 个 (gè — chung), 只 (zhī — con vật nhỏ), 条 (tiáo — dài), 本 (běn — quyển sách) |
| 11 | **Trợ từ** (Particle) | Ngữ pháp, ngữ khí, thể hiện thái độ | ạ, nhé, à, nhỉ, đã, đang, sẽ | (rất ít — "not", "'s") | 了 (le — hoàn thành), 的 (de — sở hữu), 吗 (ma — hỏi), 呢 (ne — nhỉ/thế) |

**Ghi chú cho người đọc**:
- Hầu hết ngôn ngữ đều có loại 1-8 (danh, động, tính, trạng, đại, giới, liên, thán)
- Loại 9-11 (mạo từ, loại từ, trợ từ) là chỗ ngôn ngữ KHÁC NHAU nhiều nhất
- Đây chính là nơi thấy rõ mỗi ngôn ngữ có "kiến trúc" riêng

---

### §1.2 — Classifier vs Article — Khác biệt kiến trúc quan trọng

Đây là sự khác biệt CỐT LÕI mà nhiều người không nhận ra:

**Tiếng Việt + Tiếng Trung: CÓ Loại từ (Classifier), KHÔNG CÓ Mạo từ**
**Tiếng Anh: CÓ Mạo từ (a/the), KHÔNG CÓ Loại từ**

Hãy xem cùng 1 câu nói "3 con chó" được encode thế nào:

```
TIẾNG VIỆT:   ba   CON   chó
              số   LOẠI   danh
              3    [animate] chó
              → Classifier "con" buộc phân loại: đây là SINH VẬT

TIẾNG TRUNG:  三   只     狗
              sān  zhī    gǒu
              (ba) (con-  (chó)
                   vật-
                   nhỏ)
              → Classifier "只" buộc phân loại: đây là CON VẬT NHỎ
              → Tiếng Trung classify CỤ THỂ HƠN Việt:
                只 (zhī) = con vật nhỏ
                头 (tóu) = con vật lớn (trâu, bò)
                条 (tiáo) = con dài (rắn, cá)

TIẾNG ANH:    three  dogs
              số     danh+s
              3      chó (số nhiều)
              → KHÔNG buộc phân loại gì. Chỉ đếm.
```

**Ngược lại, Tiếng Anh có Article — Việt và Trung không có:**

```
TIẾNG ANH:    THE dog          vs.    A dog
              [specific]               [any/general]
              "con chó ĐÓ cụ thể"    "một con chó BẤT KỲ"
              → Article "the/a" buộc phân biệt: CỤ THỂ hay CHUNG CHUNG?

TIẾNG VIỆT:   con chó           con chó ẤY / con chó NÀY
              (chung chung)      (cụ thể — nhưng OPTIONAL, không bắt buộc)
              → Tiếng Việt KHÔNG buộc phải nói rõ cụ thể hay chung

TIẾNG TRUNG:  狗 (gǒu)          那只狗 (nà zhī gǒu — con chó ĐÓ)
              (chung chung)      (cụ thể — dùng 那 "nà" = kia, OPTIONAL)
              → Tiếng Trung cũng KHÔNG buộc
```

**Tóm lại**:

| | Classifier (phân loại vật) | Article (phân loại xác định) |
|---|---|---|
| Tiếng Việt | ✅ BẮT BUỘC (con, cái, chiếc,...) | ❌ Không có |
| Tiếng Trung | ✅ BẮT BUỘC (个, 只, 条, 本,...) | ❌ Không có |
| Tiếng Anh | ❌ Không có | ✅ BẮT BUỘC (a, the) |

**Điều này có nghĩa**: Mỗi lần nói 1 câu có danh từ:
- Vietnamese/Chinese speaker **vô thức phân loại** vật đó thuộc nhóm nào (animate? flat? long? book?)
- English speaker **vô thức phân biệt** vật đó cụ thể hay chung chung (the dog hay a dog?)

---

### §1.3 — Đại từ — 3 hệ thống hoàn toàn khác

Đại từ (pronoun) = cách gọi "tôi", "bạn", "nó" — tưởng đơn giản nhưng 3 ngôn ngữ thiết kế KHÁC HOÀN TOÀN:

#### Tiếng Việt: Đại từ theo QUAN HỆ XÃ HỘI

```
"Tôi" có thể là:
  tôi    — chung, bình thường
  tớ     — thân mật, bạn bè
  mình   — thân mật hoặc chỉ bản thân
  em     — nói với người lớn hơn (kính trọng)
  anh    — nói với người nhỏ hơn (nam)
  chị    — nói với người nhỏ hơn (nữ)
  con    — nói với bố mẹ, thầy cô
  cháu   — nói với ông bà, người lớn tuổi
  bác    — nói với người nhỏ hơn mình nhiều tuổi

"Bạn" có thể là:
  bạn    — chung, bình thường
  cậu    — thân mật
  em     — gọi người nhỏ hơn
  anh    — gọi nam lớn hơn
  chị    — gọi nữ lớn hơn
  ông    — gọi người già (nam)
  bà     — gọi người già (nữ)
  thầy   — gọi giáo viên (nam)
  cô     — gọi giáo viên (nữ)
  con    — gọi con cái

→ MỖI CÂU tiếng Việt đều chứa thông tin VỀ QUAN HỆ XÃ HỘI
→ Nói "em đi ạ" vs "tôi đi" vs "con đi" — CÙNG Ý ("I go")
   nhưng encode KHÁC: em (kính trọng người nghe), tôi (trung lập), con (nói với bố mẹ)
```

#### Tiếng Anh: Đại từ theo NGÔI + GIỚI TÍNH

```
Ngôi 1: I (tôi)     / we (chúng tôi)
Ngôi 2: you (bạn)   / you (các bạn)   ← CÙNG 1 từ cho số ít và số nhiều!
Ngôi 3: he (anh ấy) / she (cô ấy) / it (nó) / they (họ)

→ English BẮT BUỘC phân biệt GIỚI TÍNH ở ngôi 3 (he vs she)
→ English KHÔNG phân biệt quan hệ xã hội qua đại từ
   (gọi tổng thống cũng "you", gọi bạn thân cũng "you")
→ English KHÔNG phân biệt "bạn" số ít vs số nhiều
   (1 người cũng "you", 10 người cũng "you")
```

#### Tiếng Trung: Đại từ theo NGÔI (đơn giản nhất)

```
我 (wǒ — tôi)          我们 (wǒmen — chúng tôi)
你 (nǐ — bạn)          你们 (nǐmen — các bạn)
您 (nín — bạn, kính)    → CHỈ CÓ 1 từ kính trọng (so Việt có hàng chục)
他 (tā — anh ấy)       他们 (tāmen — họ, nam)
她 (tā — cô ấy)        她们 (tāmen — họ, nữ)
它 (tā — nó, vật)       它们 (tāmen — chúng nó, vật)

⭐ ĐẶC BIỆT: 他, 她, 它 ĐỌC GIỐNG NHAU — đều là "tā"!
  → VIẾT thì phân biệt giới tính (他 nam / 她 nữ / 它 vật)
  → NÓI thì KHÔNG phân biệt — đều nghe là "tā"
  → Đây là lý do: nghe tiếng Trung thì không biết "he" hay "she"
     cho đến khi thấy context hoặc chữ viết
  → Khác với English: nghe "he" vs "she" biết ngay
```

**So sánh nhanh — cùng 1 tình huống: Học sinh nói với thầy giáo**:

```
Tiếng Việt:  "Thưa THẦY, CON không hiểu BÀI ạ"
             → 3 từ encode quan hệ: THẦY (kính), CON (hạ mình), ạ (kính ngữ cuối câu)

English:     "Teacher, I don't understand the lesson"
             → 1 từ "Teacher" (address), I = chung cho mọi TH. Không encode kính trọng.

Tiếng Trung: "老师 (lǎoshī — thầy)，我 (wǒ — tôi) 不 (bù — không)
              懂 (dǒng — hiểu) 这个 (zhège — cái này)
              课 (kè — bài học)"
             → 老师 (address) + 我 (chung). Kính trọng qua word choice, không qua pronoun.
```

---

### §1.4 — Trợ từ (Particles) — Vietnamese và Chinese có, English hầu như không

Trợ từ = những từ nhỏ xíu nhưng thay đổi NGHĨA CẢ CÂU hoặc thể hiện THÁI ĐỘ người nói.

**Tiếng Việt — Trợ từ cuối câu (ngữ khí từ):**

```
Bạn ăn cơm.      → Phát biểu bình thường
Bạn ăn cơm CHƯA? → Hỏi (trợ từ hỏi)
Bạn ăn cơm NHÉ.  → Đề nghị nhẹ nhàng, thân mật
Bạn ăn cơm ĐI.   → Khuyên / thúc giục
Bạn ăn cơm À?    → Hỏi xác nhận, hơi bất ngờ
Bạn ăn cơm Ạ.    → Kính trọng
Bạn ăn cơm NHỈ?  → Hỏi tìm đồng tình
Bạn ăn cơm HẢ?   → Hỏi ngạc nhiên
Bạn ăn cơm SAO?  → Hỏi lý do / ngạc nhiên
Bạn ăn cơm RỒI.  → Xác nhận đã xảy ra

→ CÙNG 1 câu, thay trợ từ cuối = ĐỔI HOÀN TOÀN thái độ + ý định
→ Tiếng Việt có ~15-20 trợ từ cuối câu thường dùng
```

**Tiếng Trung — Trợ từ (助词 zhùcí) rất phong phú:**

```
TRỢI TỪ CẤU TRÚC (structural particles):
  的 (de)  — sở hữu / bổ nghĩa danh từ
    我的书 (wǒ de shū — sách CỦA tôi)
    漂亮的花 (piàoliang de huā — hoa ĐẸP, "hoa MÀ đẹp")

  地 (de)  — bổ nghĩa động từ (trạng từ hóa)
    慢慢地走 (mànmàn de zǒu — CHẬM CHẬM MÀ đi)

  得 (de)  — kết quả / mức độ sau động từ
    跑得快 (pǎo de kuài — chạy NHANH, "chạy MÀ nhanh")

⭐ 3 chữ "de" — VIẾT KHÁC, ĐỌC GIỐNG, NGHĨA KHÁC:
  的 (bổ nghĩa danh từ) / 地 (bổ nghĩa động từ) / 得 (kết quả)
  → Đây là điểm KHÓ NHẤT cho người học tiếng Trung

TRỢI TỪ NGỮI KHÍ (modal particles — giống Việt):
  吗 (ma)  — biến câu thành câu hỏi yes/no
    你吃了吗？(nǐ chī le ma? — bạn ăn chưa?)

  呢 (ne)  — hỏi ngược / nhấn mạnh / "thế còn..."
    你呢？(nǐ ne? — thế còn bạn?)

  吧 (ba)  — đề nghị / suy đoán (giống "nhé/nhỉ" Việt)
    走吧 (zǒu ba — đi NHÉ / đi THÔI)
    是吧？(shì ba? — đúng KHÔNG NHỈ?)

  啊 (a/ā)  — cảm thán / nhấn mạnh (giống "à/ạ" Việt)
    好啊！(hǎo a! — tốt QUÁÁ!)

  了 (le)   — HOÀN THÀNH (aspect marker) — xem §2.2
    我吃了 (wǒ chī le — tôi ăn RỒI)

  过 (guò)  — KINH NGHIỆM (đã từng)
    我吃过 (wǒ chī guò — tôi đã TỪNG ăn)

  着 (zhe)  — ĐANG DIỄN RA (tiếp diễn)
    他看着书 (tā kàn zhe shū — anh ấy ĐANG nhìn sách / giữ nhìn sách)
```

**Tiếng Anh — hầu như KHÔNG CÓ trợ từ tương đương:**

```
English dùng:
  - Intonation (ngữ điệu) thay trợ từ ngữ khí
    "You ate?" (lên giọng cuối = hỏi) vs "You ate." (xuống = phát biểu)
  - Tag questions thay "nhỉ/nhé"
    "You ate, DIDN'T YOU?" ≈ "Bạn ăn rồi, ĐÚNG KHÔNG NHỈ?"
  - Auxiliary verbs thay trợ từ cấu trúc
    "I HAVE eaten" ≈ đã ăn (hoàn thành)
    "I WAS eating" ≈ đang ăn (tiếp diễn)

→ English KHÔNG có hệ thống trợ từ cuối câu phong phú như Việt/Trung
→ English bù bằng: auxiliary verbs + intonation + tag questions
```

---

## §2 — Hình thái học: Từ thay đổi hình dạng thế nào (Morphology)

### §2.1 — Ba loại ngôn ngữ: Isolating vs Fusional

Ngôn ngữ học phân loại ngôn ngữ theo cách xử lý hình dạng từ:

```
ISOLATING (đơn lập)                    FUSIONAL (hòa kết)
Từ KHÔNG thay đổi hình dạng.          Từ BIẾN DẠNG để mang thêm nghĩa.
Muốn thêm nghĩa → thêm TỪ MỚI.      Muốn thêm nghĩa → thêm TIỀN TỐ/HẬU TỐ/BIẾN ÂM.

Tiếng Việt ◄────── Tiếng Trung ────────── Tiếng Anh ─────────► Latin/Russian/Arabic
(gần thuần đơn lập) (đơn lập, ít biến đổi) (fusional vừa)       (fusional nặng)

Ví dụ cực đoan:
  TIẾNG VIỆT:  "tôi đã ăn" = 3 từ riêng biệt, mỗi từ KHÔNG ĐỔI
  TIẾNG LATIN: "ēdī" = 1 từ = "tôi" + "ăn" + "quá khứ" gộp hết vào 1 từ biến dạng

Thêm ví dụ cực đoan: Tiếng Thổ Nhĩ Kỳ (agglutinative — kết dính):
  "evlerinizden" = ev + ler + iniz + den
                 = nhà + nhiều + của-các-bạn + từ
                 = "từ những ngôi nhà của các bạn" — 1 TỪ TIẾNG THỔ = 7 TỪ TIẾNG VIỆT
```

### §2.2 — So sánh: Thì (Tense) — Thời gian hành động

| | Quá khứ | Hiện tại | Tương lai |
|---|---|---|---|
| **Tiếng Việt** | tôi **đã** ăn | tôi ăn / tôi **đang** ăn | tôi **sẽ** ăn |
| Cách làm | THÊM TỪ "đã" trước verb | Không thêm / thêm "đang" | THÊM TỪ "sẽ" |
| Verb thay đổi? | ❌ "ăn" KHÔNG ĐỔI | ❌ "ăn" KHÔNG ĐỔI | ❌ "ăn" KHÔNG ĐỔI |
| | | | |
| **English** | I **ate** | I **eat** / I **am eating** | I **will eat** |
| Cách làm | Verb BIẾN DẠNG (eat→ate) | Verb nguyên / thêm be+-ing | THÊM TỪ "will" |
| Verb thay đổi? | ✅ eat → ate (bất quy tắc!) | ✅ eat → eating (-ing) | ❌ eat giữ nguyên |
| | | | |
| **Tiếng Trung** | 我吃**了** | 我吃 / 我**在**吃 | 我**会**吃 |
| Pinyin | wǒ chī **le** | wǒ chī / wǒ **zài** chī | wǒ **huì** chī |
| Nghĩa | tôi ăn **RỒI** | tôi ăn / tôi **ĐANG** ăn | tôi **SẼ** ăn |
| Cách làm | THÊM trợ từ "了" (le) SAU verb | Không thêm / thêm "在" (zài) trước | THÊM "会" (huì) trước |
| Verb thay đổi? | ❌ "吃" KHÔNG ĐỔI | ❌ "吃" KHÔNG ĐỔI | ❌ "吃" KHÔNG ĐỔI |

**English irregular verbs — đau đầu cho người học:**

```
go → went → gone        (đi — hoàn toàn KHÁC gốc)
eat → ate → eaten        (ăn — biến dạng bất quy tắc)
see → saw → seen         (thấy — biến dạng bất quy tắc)
think → thought → thought (nghĩ — biến dạng bất quy tắc)
run → ran → run          (chạy — biến dạng, rồi quay lại gốc!)
put → put → put          (đặt — KHÔNG đổi gì cả!)
be → was/were → been     (là — biến dạng PHỨC TẠP NHẤT)

→ Ước tính ~200 irregular verbs thường dùng trong English
→ Mỗi cái = 1 chunk phải học riêng (không suy luận được)
→ Vietnamese và Chinese: 0 irregular verbs (verb KHÔNG BAO GIỜ đổi)
```

### §2.3 — So sánh: Số nhiều (Plural)

| | Một | Nhiều |
|---|---|---|
| **Tiếng Việt** | con chó | **các** con chó / **những** con chó |
| Cách làm | (nguyên) | THÊM TỪ "các/những" TRƯỚC, danh từ KHÔNG ĐỔI |
| | | |
| **English** | dog | dog**s** |
| Cách làm | (nguyên) | THÊM -s/-es SAU danh từ. Nhưng CÓ NGOẠI LỆ: |
| Ngoại lệ | child → children, mouse → mice, foot → feet, person → people |
| | man → men, tooth → teeth, fish → fish (KHÔNG ĐỔI!) |
| | | |
| **Tiếng Trung** | 狗 (gǒu — chó) | 狗 (gǒu — chó) → KHÔNG ĐỔI GÌ CẢ |
| Cách làm | (nguyên) | Số nhiều hiểu từ context hoặc số đếm |
| Ngoại lệ | | 们 (men) chỉ dùng cho NGƯỜI: 他们 (tāmen — họ), 我们 (wǒmen — chúng tôi) |
| | | 朋友们 (péngyoumen — các bạn) — nhưng OPTIONAL |

**Tiếng Việt có 2 từ số nhiều khác nghĩa nhé:**

```
"CÁC" con chó  = TẤT CẢ con chó (definite — các con chó CỤ THỂ đó)
"NHỮNG" con chó = MỘT SỐ con chó (indefinite — vài con chó NÀO ĐÓ)

→ Tiếng Việt BẮT BUỘC phân biệt "tất cả nhóm" vs "một số trong nhóm"
→ English "dogs" = KHÔNG phân biệt (some dogs? all dogs? → hiểu từ context)
→ Chinese 狗 = KHÔNG phân biệt (1 hay nhiều? → hiểu từ context hoặc số đếm)
```

### §2.4 — So sánh: So sánh hơn/nhất (Comparative / Superlative)

| | Hơn | Nhất |
|---|---|---|
| **Tiếng Việt** | đẹp **hơn** | đẹp **nhất** |
| Cách làm | THÊM TỪ "hơn" SAU | THÊM TỪ "nhất" SAU |
| Tính từ đổi? | ❌ "đẹp" KHÔNG ĐỔI | ❌ "đẹp" KHÔNG ĐỔI |
| | | |
| **English** | bigg**er** / **more** beautiful | bigg**est** / **most** beautiful |
| Cách làm | Từ ngắn: thêm -er. Từ dài: thêm "more" | Từ ngắn: thêm -est. Từ dài: thêm "most" |
| Ngoại lệ | good → **better** (bất quy tắc!) | good → **best** |
| | bad → **worse** | bad → **worst** |
| | | |
| **Tiếng Trung** | **更** 大 | **最** 大 |
| Pinyin + nghĩa | **gèng** dà (CÒN-HƠN to) | **zuì** dà (NHẤT to) |
| Cách làm | THÊM TỪ "更" (gèng) TRƯỚC | THÊM TỪ "最" (zuì) TRƯỚC |
| Tính từ đổi? | ❌ "大" KHÔNG ĐỔI | ❌ "大" KHÔNG ĐỔI |

### §2.5 — Insight: Tiếng Việt là "lego blocks"

```
Tiếng Việt:    tôi  |  đã  |  ăn  |  cơm
               ───     ───    ───    ───
               block   block  block  block
               (ai)   (thì)  (hành  (cái
                              động)  gì)
               → Mỗi block GIỮ NGUYÊN hình dạng. Ghép blocks = ý nghĩa.

Tiếng Anh:     I    |  ate        |  rice
               ───     ─────────    ────
               block   BIẾN DẠNG    block
               (ai)   (eat → ate)   (cái gì)
               → Một số blocks phải BIẾN DẠNG tùy context.

Tiếng Trung:   我   |  吃  |  了   |  饭
               wǒ     chī    le     fàn
               (tôi)  (ăn)  (rồi)  (cơm)
               ───    ───    ───    ───
               block  block  block  block
               → Giống Vietnamese: blocks GIỮ NGUYÊN.
               → NHƯNG: mỗi block = 1 ký tự riêng biệt = 1 hình ảnh cố định

TRADE-OFF:
  Vietnamese/Chinese: Nhiều blocks nhỏ, mỗi block nhẹ, dễ ghép
  English:            Ít blocks hơn, mỗi block có thể biến dạng, pack nhiều info hơn per block

  Vietnamese:  "tôi  đã   không  ăn   cơm"     = 5 blocks
  English:     "I    didn't      eat  rice"     = 4 blocks (didn't = did+not gộp)
  Chinese:     "我   没          吃   饭"       = 4 blocks
               wǒ    méi         chī   fàn
               (tôi) (không-đã)  (ăn) (cơm)
```

---

## §3 — Cú pháp: Cách ghép từ thành câu (Syntax)

### §3.1 — Trật tự cơ bản: SVO (Subject — Verb — Object)

Cả 3 ngôn ngữ đều dùng trật tự SVO cơ bản:

```
         S (chủ ngữ)    V (động từ)    O (tân ngữ)
         ───────────    ──────────     ──────────
Việt:    Tôi            ăn              cơm
English: I              eat             rice
Trung:   我 (wǒ)        吃 (chī)        饭 (fàn)
         (tôi)          (ăn)            (cơm)
```

**Tham khảo**: Không phải mọi ngôn ngữ đều SVO:
- **SOV** (Subject-Object-Verb): Japanese, Korean, Turkish, Hindi, Latin
  - Nhật: 私は ご飯を 食べる (watashi wa gohan o taberu — "tôi cơm ăn")
- **VSO** (Verb-Subject-Object): Arabic, Welsh, Irish
  - Ả Rập: أكلتُ الأرز (akaltu al-aruz — "ăn tôi cơm")
- SVO chiếm ~42% ngôn ngữ thế giới, SOV chiếm ~45%

### §3.2 — Word order flexibility + Topic-Comment

**Tiếng Anh — STRICT SVO, ít linh hoạt:**

```
✅ "I eat rice."              SVO — câu chuẩn
✅ "Rice, I eat (it)."        OSV — nhấn mạnh "rice", literary, ít dùng
❌ "Rice eat I."              OVS — SAI (nghe như cơm ăn người)
❌ "Eat I rice."              VSO — SAI (trừ câu hỏi đảo ngữ)

→ English PHỤ THUỘC vào word order để biết ai làm gì cho ai
  "Dog bites man" ≠ "Man bites dog" — đảo trật tự = đảo nghĩa!
```

**Tiếng Việt — SVO nhưng CÓ Topic-Comment linh hoạt:**

```
✅ "Tôi ăn cơm rồi."               SVO — câu chuẩn
✅ "Cơm, tôi ăn rồi."              Topic-Comment: cơm = topic
✅ "Ăn cơm chưa?"                   Bỏ subject (hiểu ngầm "bạn")
✅ "Cơm thì tôi ăn rồi,            Topic-Comment chuỗi:
    canh thì chưa."                  2 topics, 2 comments
❌ "Cơm ăn tôi."                    Semantic violation (cơm không biết ăn)

Topic-Comment = cấu trúc "A thì B":
  "Cái áo này, (thì) tôi mua hôm qua."
  → "Cái áo này" = TOPIC (đề tài đang nói)
  → "tôi mua hôm qua" = COMMENT (nói gì về topic)
  → Topic KHÔNG CẦN là subject — nó là "cái đang được nói tới"
```

**Tiếng Trung — Topic-Comment MẠNH NHẤT trong 3 ngôn ngữ:**

```
✅ 我吃饭。(wǒ chī fàn — tôi ăn cơm)                    SVO chuẩn
✅ 饭，我吃了。(fàn, wǒ chī le — cơm, tôi ăn rồi)        Topic-Comment
✅ 吃饭了吗？(chī fàn le ma? — ăn cơm chưa?)               Bỏ subject
✅ 这本书我看过了。                                         Topic-Comment phức tạp
   (zhè běn shū wǒ kàn guò le)
   (cuốn sách NÀY, tôi đọc RỒI)
   → 这本书 (cuốn sách này) = TOPIC, KHÔNG phải subject
   → 我 (tôi) = subject, nằm SAU topic

✅ 他，人很好。
   (tā, rén hěn hǎo)
   (anh ấy, người rất tốt = "anh ấy, là người tốt")
   → Cấu trúc "A, B" — topic = 他 (anh ấy), comment = 人很好 (người rất tốt)

→ Tiếng Trung KHÔNG CẦN subject rõ ràng
→ Topic có thể là BẤT CỨ DANH TỪ NÀO kéo lên đầu câu
→ Đây là điểm giống tiếng Việt, KHÁC tiếng Anh
```

### §3.3 — Cấu trúc cụm từ (Phrase Structure) — Cây cú pháp

Câu KHÔNG phải flat (từ + từ + từ + từ). Câu có **cấu trúc cây** — từ nhóm thành cụm, cụm nhóm thành câu:

```
CÂU TIẾNG VIỆT: "Con chó đen lớn của tôi đang chạy nhanh trong công viên"

[CÂU]
├── [Cụm danh từ — CHỦ NGỮ]
│   ├── [Loại từ] con
│   ├── [Danh từ] chó
│   ├── [Tính từ] đen
│   ├── [Tính từ] lớn
│   └── [Cụm sở hữu]
│       ├── [Giới từ] của
│       └── [Đại từ] tôi
│
├── [Cụm động từ — VỊ NGỮ]
│   ├── [Trợ từ thì] đang
│   ├── [Động từ] chạy
│   ├── [Trạng từ] nhanh
│   │
│   └── [Cụm giới từ — NƠI CHỐN]
│       ├── [Giới từ] trong
│       └── [Cụm danh từ]
│           └── [Danh từ] công viên
```

```
CÂU ENGLISH: "My big black dog is running fast in the park"

[SENTENCE]
├── [Noun Phrase — SUBJECT]
│   ├── [Possessive] My              ← VỊ TRÍ: TRƯỚC noun (khác Việt: SAU)
│   ├── [Adjective] big
│   ├── [Adjective] black
│   └── [Noun] dog
│
├── [Verb Phrase — PREDICATE]
│   ├── [Auxiliary] is               ← Auxiliary verb (Việt: không cần)
│   ├── [Verb -ing] running          ← -ing form (Việt: "đang" thay thế)
│   ├── [Adverb] fast
│   │
│   └── [Prepositional Phrase — LOCATION]
│       ├── [Preposition] in
│       └── [Noun Phrase]
│           ├── [Article] the        ← Article (Việt: không có)
│           └── [Noun] park
```

```
CÂU TIẾNG TRUNG: "我的大黑狗正在公园里快跑"
(wǒ de dà hēi gǒu zhèngzài gōngyuán lǐ kuài pǎo)
(của-tôi to đen chó đang-ở công-viên trong nhanh chạy)
= "Con chó đen lớn của tôi đang chạy nhanh trong công viên"

[句子 — CÂU]
├── [名词短语 — CỤM DANH TỪ, CHỦ NGỮ]
│   ├── [所有格] 我的 (wǒ de — của tôi)     ← VỊ TRÍ: TRƯỚC noun (giống Anh, khác Việt)
│   ├── [形容词] 大 (dà — to)
│   ├── [形容词] 黑 (hēi — đen)
│   └── [名词] 狗 (gǒu — chó)
│
├── [动词短语 — CỤM ĐỘNG TỪ, VỊ NGỮ]
│   ├── [副词] 正在 (zhèngzài — đang)
│   │
│   ├── [地点短语 — NƠI CHỐN]
│   │   ├── [名词] 公园 (gōngyuán — công viên)
│   │   └── [方位词] 里 (lǐ — trong/bên trong)    ← "trong" ĐI SAU danh từ (khác Việt/Anh)
│   │
│   ├── [副词] 快 (kuài — nhanh)
│   └── [动词] 跑 (pǎo — chạy)
```

### §3.4 — Modifier order: Trước hay Sau danh từ?

Đây là khác biệt CẤU TRÚC giữa 3 ngôn ngữ:

```
TIẾNG VIỆT: HEAD-FIRST — Danh từ TRƯỚC, bổ nghĩa SAU
            con chó  ĐEN LỚN CỦA TÔI
                 ↑    ↑↑↑↑↑↑↑↑↑↑↑↑↑↑
                HEAD  modifiers đi SAU

TIẾNG ANH:  HEAD-LAST — Bổ nghĩa TRƯỚC, danh từ SAU
            MY BIG BLACK  dog
            ↑↑↑↑↑↑↑↑↑↑↑   ↑
            modifiers      HEAD

TIẾNG TRUNG: HEAD-LAST — Giống Anh: bổ nghĩa TRƯỚC + 的 + danh từ
             我的  大  黑  狗
             wǒ de dà hēi gǒu
             (của-tôi to đen chó)
             ↑↑↑↑↑↑↑↑↑↑↑↑  ↑
             modifiers      HEAD
```

**HỆ QUẢ QUAN TRỌNG CHO CÁCH NGHĩ:**

```
Nghe câu Việt:  "Con chó..." → BIẾT NGAY đang nói về con chó
                → Rồi mới nghe chi tiết: "...đen lớn của tôi"
                → Chunk "chó" ACTIVATE TRƯỚC, chi tiết bổ sung SAU

Nghe câu Anh:   "My big black..." → CHƯA BIẾT nói về cái gì!
                → Phải ĐỢI: "...dog" cuối cùng mới biết
                → Chi tiết tích lũy TRƯỚC, chunk chính activate SAU

Nghe câu Trung:  "我的大黑..." → CHƯA BIẾT nói về cái gì (giống Anh)
                 → Phải đợi: "...狗" cuối cùng
                 → Giống Anh: chi tiết trước, chunk chính sau

→ Vietnamese KHÁC vì chunk trung tâm NGHE TRƯỚC
→ English + Chinese chunk trung tâm NGHE SAU
→ Đây là sự khác biệt TIMING khi activate chunks
```

### §3.5 — Câu hỏi: 3 cách hoàn toàn khác

**Câu hỏi Yes/No (hỏi xác nhận):**

```
TIẾNG VIỆT — Giữ nguyên trật tự, thêm từ hỏi:
  Bạn ăn cơm.     → Bạn ăn cơm CHƯA?    (hỏi bằng "chưa" cuối câu)
  Bạn ăn cơm.     → Bạn CÓ ăn cơm KHÔNG? (hỏi bằng "có...không" bao quanh verb)

TIẾNG ANH — ĐẢO trật tự, thêm auxiliary:
  You eat rice.    → DO you eat rice?      (thêm "do" + đảo lên trước subject)
  You ate rice.    → DID you eat rice?     (thêm "did" + verb quay về nguyên)
  You are eating.  → ARE you eating?       (đảo "are" lên trước subject)

TIẾNG TRUNG — Giữ nguyên trật tự, thêm 吗 (ma) cuối câu:
  你吃饭。         → 你吃饭吗？
  (nǐ chī fàn)      (nǐ chī fàn ma?)
  (bạn ăn cơm)      (bạn ăn cơm KHÔNG?)
  → Chỉ cần thêm "吗" cuối câu = biến thành câu hỏi. CỰC ĐƠN GIẢN.

HOẶC — Tiếng Trung còn cách hỏi KHÁC (verb-not-verb):
  你吃不吃？(nǐ chī bù chī? — bạn ăn-KHÔNG-ăn? = bạn ăn không?)
  你是不是学生？(nǐ shì bù shì xuéshēng? — bạn là-KHÔNG-là học sinh?)
  → Cấu trúc "V-不-V" = hỏi bằng cách đưa ra cả "có" lẫn "không"
```

**Câu hỏi Wh- (hỏi thông tin):**

```
TIẾNG VIỆT — Từ hỏi ở VỊ TRÍ CÂU TRẢ LỜI:
  Bạn ăn GÌ?        (gì = ở vị trí O → câu trả lời "cơm" cũng ở vị trí O)
  AI ăn cơm?         (ai = ở vị trí S)
  Bạn ăn Ở ĐÂU?     (ở đâu = ở vị trí nơi chốn)
  Bạn ăn KHI NÀO?    (khi nào = ở vị trí thời gian)

TIẾNG ANH — Từ hỏi CHẠY LÊN ĐẦU CÂU + đảo auxiliary:
  WHAT do you eat?    (what = chạy lên đầu, dù answer "rice" ở cuối)
  WHO eats rice?      (who = đầu câu, NHƯNG không cần đảo vì who = subject)
  WHERE do you eat?   (where = đầu câu + đảo "do")
  WHEN do you eat?    (when = đầu câu + đảo "do")

TIẾNG TRUNG — Giống Việt: từ hỏi ở VỊ TRÍ CÂU TRẢ LỜI:
  你吃什么？(nǐ chī shénme? — bạn ăn GÌ?)         什么 ở vị trí O
  谁吃饭？  (shéi chī fàn? — AI ăn cơm?)           谁 ở vị trí S
  你在哪里吃？(nǐ zài nǎlǐ chī? — bạn Ở ĐÂU ăn?)  哪里 ở vị trí nơi chốn
  你什么时候吃？(nǐ shénme shíhòu chī?              什么时候 ở vị trí thời gian
                — bạn KHI NÀO ăn?)

→ Việt + Trung: từ hỏi "ở yên" tại vị trí câu trả lời. TRẬT TỰ KHÔNG ĐỔI.
→ Anh: từ hỏi "nhảy" lên đầu câu + đảo auxiliary. TRẬT TỰ ĐỔI.
→ Đây là lý do Vietnamese/Chinese speakers hay quên đảo ngữ khi nói English:
   *"You eat what?" (Việt-hóa) thay vì "What do you eat?" (English chuẩn)
```

### §3.6 — Phủ định: Mỗi ngôn ngữ buộc phân biệt khác nhau

```
TIẾNG VIỆT — "không" vs "chưa":
  Tôi KHÔNG ăn.    = phủ định TUYỆT ĐỐI (tôi không ăn, point.)
  Tôi CHƯA ăn.     = phủ định TẠM THỜI (chưa ăn nhưng có thể sẽ ăn)

  → Vietnamese BẮT BUỘC phân biệt "vĩnh viễn" vs "tạm thời"
  → Nói "tôi không ăn" ≠ "tôi chưa ăn" — nghĩa RẤT KHÁC

  Thêm: CHẲNG (nhấn mạnh phủ định), CHƯA BAO GIỜ (quá khứ phủ định hoàn toàn)

TIẾNG ANH — "not" chung cho mọi trường hợp:
  I don't eat.          = phủ định (chung)
  I haven't eaten yet.  = phủ định tạm thời (phải thêm "yet" = tự thêm, KHÔNG bắt buộc)
  I never eat.          = phủ định vĩnh viễn (phải thêm "never")

  → English CÓ THỂ phân biệt nhưng KHÔNG BẮT BUỘC
  → "I don't eat" = CHƯA RÕ là "không" hay "chưa" cho đến khi có context

TIẾNG TRUNG — "不" (bù) vs "没" (méi):
  我不吃。  (wǒ bù chī — tôi KHÔNG ăn)   = phủ định Ý CHÍ (tôi không MUỐN ăn)
  我没吃。  (wǒ méi chī — tôi CHƯA ăn)   = phủ định SỰ KIỆN (việc ăn chưa xảy ra)

  → Chinese BẮT BUỘC phân biệt "ý chí" vs "sự kiện"
  → 我不去 (wǒ bù qù — tôi không đi) = tôi không MUỐN đi
  → 我没去 (wǒ méi qù — tôi chưa đi) = tôi chưa ĐI (sự kiện chưa xảy ra)

  Ví dụ rõ hơn:
  "Bạn có ăn cơm không?" → trả lời:
    不吃 (bù chī) = không ăn (từ chối, ý chí)
    没吃 (méi chī) = chưa ăn (chưa xảy ra, có thể sẽ ăn)

SO SÁNH 3 HỆ THỐNG PHỦ ĐỊNH:
  ┌─────────────────────────────────────────────────────────────┐
  │ Tiếng Việt: KHÔNG (vĩnh viễn) vs CHƯA (tạm thời)         │
  │ Tiếng Trung: 不 bù (ý chí)    vs 没 méi (sự kiện)        │
  │ Tiếng Anh:   NOT (chung)       → context quyết định       │
  │                                                             │
  │ → Cùng 1 tình huống "chưa ăn":                            │
  │   Việt bắt buộc nói "CHƯA" (phân biệt khỏi "không")      │
  │   Trung bắt buộc nói "没" méi (phân biệt khỏi "不" bù)   │
  │   Anh có thể nói "I didn't eat" hoặc "I haven't eaten"    │
  │   → English PHỨC TẠP hơn ở thì (didn't vs haven't),       │
  │     nhưng KHÔNG bắt buộc phân biệt ý chí vs sự kiện       │
  └─────────────────────────────────────────────────────────────┘
```

### §3.7 — Câu phức: Mệnh đề phụ + liên từ

Khi câu có nhiều hơn 1 ý (mệnh đề chính + mệnh đề phụ):

```
NGUYÊN NHÂN-KẾT QUẢ:

  Việt:  VÌ trời mưa, (NÊN) tôi ở nhà.
         → Liên từ: vì...nên (pair)
         → Mệnh đề nguyên nhân TRƯỚC, kết quả SAU (hoặc ngược)

  Anh:   BECAUSE it rained, I stayed home.
         I stayed home BECAUSE it rained.
         → Liên từ: because
         → Cả 2 thứ tự đều OK

  Trung:  因为下雨，(所以) 我在家。
          (yīnwèi xià yǔ, suǒyǐ wǒ zài jiā)
          (VÌ     mưa,    NÊN   tôi ở nhà)
          → Liên từ: 因为...所以 (yīnwèi...suǒyǐ = vì...nên), pair giống Việt

MỆnh ĐỀ QUAN HỆ (relative clause) — NƠI 3 ngôn ngữ KHÁC NHẤT:

  Việt:  Con chó  MÀ  tôi nuôi
         ↓ HEAD    ↓   ↓ relative clause
         → HEAD TRƯỚC + "mà" + clause SAU

  Anh:   The dog  THAT  I raise
         ↓ HEAD    ↓     ↓ relative clause
         → HEAD TRƯỚC + "that/which/who" + clause SAU

  Trung:  我养的     狗
          wǒ yǎng de gǒu
          (tôi nuôi 的 chó)
          ↓ relative clause ↓ HEAD
          → Clause TRƯỚC + 的 (de) + HEAD SAU !!! NGƯỢC với Việt + Anh

  → Tiếng Trung đặt mệnh đề quan hệ TRƯỚC danh từ (pre-nominal)
  → Tiếng Việt và Anh đặt SAU danh từ (post-nominal)
  → Đây là khác biệt CẤU TRÚC quan trọng

  Ví dụ phức tạp hơn:
  Việt:  "Cuốn sách MÀ bạn tôi mua hôm qua ĐÃ bán hết rồi"
  Anh:   "The book THAT my friend bought yesterday IS sold out"
  Trung:  "我朋友昨天买的书已经卖完了"
          (wǒ péngyou zuótiān mǎi de shū yǐjīng mài wán le)
          (tôi bạn     hôm-qua mua 的 sách đã    bán hết  rồi)
          → "我朋友昨天买的" = relative clause TRƯỚC "书" (sách)
```

---

## §4 — Đặc điểm riêng nổi bật

### §4.1 — Vietnamese: Classifier system chi tiết

Vietnamese có hệ thống loại từ (classifier) phong phú. Mỗi khi đếm hoặc chỉ định danh từ, PHẢI chọn loại từ phù hợp:

```
CLASSIFIER CHÍNH — phân loại theo ĐẶC TÍNH:

  con   → SINH VẬT (animate) + một số mở rộng metaphor
          con chó, con mèo, con người, con kiến, con cá
          con sông (sông "sống"/chảy — metaphor animate)
          con dao (dao "nguy hiểm" — historical metaphor)
          con đường (đường "trải dài" — metaphor animate)
          con mắt (mắt "sống" — metaphor)
          → "con" là classifier RỘNG NHẤT, nhiều mở rộng metaphor nhất

  cái   → ĐỒ VẬT thông dụng (inanimate objects)
          cái bàn, cái ghế, cái bút, cái áo, cái ly, cái nồi
          cái miệng, cái mũi (bộ phận cơ thể = "vật thuộc cơ thể")
          → "cái" cũng dùng làm từ chỉ chung: "cái gì?" = "what?"

  chiếc → CÁ THỂ, thường là 1 trong cặp hoặc 1 đơn vị
          chiếc giày (1 chiếc, ko phải đôi), chiếc xe, chiếc nhẫn
          chiếc lá, chiếc thuyền
          → Nhấn mạnh sự ĐƠN LẺ, CÁ THỂ

CLASSIFIER CHUYÊN DỤNG — phân loại theo HÌNH DẠNG/LOẠI:

  quyển / cuốn → đồ ĐÓNG GÁY (sách, vở, tập, album)
  tờ           → đồ PHẲNG MỎNG (giấy, báo, tiền giấy)
  bức          → đồ TREO/TRƯNG BÀY (tranh, ảnh, thư, tường)
  tấm          → đồ PHẲNG RỘNG (ảnh, gương, thảm, ván)
  cây          → đồ DÀI THẲNG (bút, cờ, tre, nến, cầu)
  quả / trái   → đồ TRÒN (cam, táo, bóng, đồi, tim, bom!)
  ngôi         → NHÀ, SAO, MỘ (ngôi nhà, ngôi sao, ngôi mộ)
  bài          → TÁC PHẨM ngắn (bài thơ, bài hát, bài báo, bài tập)
  bộ           → TẬP HỢP (bộ quần áo, bộ phim, bộ sách)
  đôi          → CẶP (đôi giày, đôi mắt, đôi bạn)
  bữa          → BỮA ĂN/TIỆC (bữa cơm, bữa tiệc)
  giọt         → GIỌT (giọt nước, giọt mồ hôi, giọt máu)

CLASSIFIER XÃ HỘI — phân loại theo THÁI ĐỘ đối với NGƯỜI:

  vị    → KÍNH TRỌNG (vị khách, vị giáo sư, vị tổng thống)
  ngài  → RẤT KÍNH TRỌNG (ngài đại sứ, ngài tổng thống)
  ông   → NAM, KÍNH/TRUNG LẬP (ông Nguyễn, ông ấy)
  bà    → NỮ, KÍNH/TRUNG LẬP (bà Trần, bà ấy)
  anh   → NAM TRẺ (anh Minh, anh ấy)
  chị   → NỮ TRẺ (chị Lan, chị ấy)
  cô    → NỮ TRẺ/GIÁO VIÊN (cô giáo, cô ấy)
  chú   → NAM TRUNG NIÊN (chú ấy)
  thằng → NAM, THÂN MẬT hoặc TIÊU CỰC (thằng Tí, thằng ăn trộm)
  con   → TRẺ EM hoặc HẠ THẤP (con bé, con nhà ai đó)
  tên   → TIÊU CỰC (tên trộm, tên lưu manh)
  gã    → TIÊU CỰC/XA LẠ NAM (gã đàn ông, gã lái xe)

→ ⭐ Hệ thống classifier Vietnamese = BUỘC phân loại:
  1. Animate hay inanimate? (con vs cái)
  2. Hình dạng? (tờ phẳng, cây dài, quả tròn,...)
  3. Thái độ xã hội? (vị kính trọng, tên tiêu cực,...)
→ MỖI CÂU có danh từ = 1 act phân loại VÔ THỨC
```

### §4.2 — Chinese: Character = hình ảnh + nghĩa

Hệ thống chữ Trung Quốc KHÁC CĂN BẢN so với alphabetic (Việt/Anh):

```
ALPHABETIC (Việt, Anh):
  Chữ cái → encode ÂM THANH → não giải mã âm → tìm nghĩa
  "c-h-ó" → /tʃɔ/ (âm "chó") → nghĩa: con chó
  → Đường đi: CHỮ → ÂM → NGHĨA (2 bước)

LOGOGRAPHIC (Trung):
  Ký tự → encode NGHĨA TRỰC TIẾP (+ đôi khi gợi ý âm)
  狗 → (nhìn thấy) → nghĩa: con chó, âm: gǒu
  → Đường đi: CHỮ → NGHĨA (1 bước, có thể skip âm)
```

**Cách ký tự Trung được cấu tạo:**

```
1. TƯỢNG HÌNH (Pictographic) — ký tự VẼ GIỐNG vật thật (cổ nhất):
   日 (rì — mặt trời)     ← hình vẽ mặt trời cổ: ☉
   月 (yuè — mặt trăng)   ← hình vẽ trăng khuyết
   山 (shān — núi)         ← hình vẽ 3 đỉnh núi
   水 (shuǐ — nước)        ← hình vẽ dòng chảy
   木 (mù — cây)           ← hình vẽ cây có rễ + cành
   人 (rén — người)         ← hình vẽ người đứng nghiêng
   口 (kǒu — miệng)        ← hình vẽ miệng mở

2. CHỈ SỰ (Indicative) — ký hiệu TRỪU TƯỢNG:
   一 (yī — một)            ← 1 nét ngang = 1
   二 (èr — hai)            ← 2 nét ngang = 2
   三 (sān — ba)            ← 3 nét ngang = 3
   上 (shàng — trên)        ← nét phía trên đường cơ sở
   下 (xià — dưới)          ← nét phía dưới đường cơ sở

3. HỘI Ý (Compound ideographic) — GHÉP hình = nghĩa MỚI:
   日 + 月 = 明 (míng — sáng)           "mặt trời + mặt trăng = SÁNG"
   木 + 木 = 林 (lín — rừng nhỏ)        "cây + cây = RỪNG"
   木 + 木 + 木 = 森 (sēn — rừng rậm)   "cây + cây + cây = RỪNG RẬM"
   人 + 人 = 从 (cóng — đi theo)         "người + người = ĐI THEO"
   人 + 人 + 人 = 众 (zhòng — đám đông)  "người × 3 = ĐÁM ĐÔNG"
   女 + 子 = 好 (hǎo — tốt/đẹp)         "phụ nữ + con = TỐT" (có con = tốt)
   田 + 力 = 男 (nán — nam)              "ruộng + sức = NAM" (người cày ruộng)
   女 + 女 + 女 = 姦 (jiān — gian dối)   "ba phụ nữ = GIAN" ← nhận xét: sexist cổ đại!
   不 + 好 = 孬 (nāo — hèn/yếu)          "không + tốt = HÈN"

4. HÌNH THANH (Phono-semantic) — phần GỢI NGHĨA + phần GỢI ÂM (~90% chữ Trung):
   Cấu trúc: [bộ thủ nghĩa] + [thành phần gợi âm]

   氵(bộ nước) + 可 (kě) = 河 (hé — sông)
     → 氵 gợi nghĩa: liên quan NƯỚC
     → 可 gợi âm: hé gần giống kě

   氵(bộ nước) + 每 (měi) = 海 (hǎi — biển)
     → 氵 gợi nghĩa: liên quan NƯỚC
     → 每 gợi âm: hǎi gần giống měi

   木 (bộ cây) + 寸 (cùn) = 村 (cūn — làng)
     → 木 gợi nghĩa: liên quan CÂY/NÔNG THÔN
     → 寸 gợi âm: cūn gần giống cùn

   亻(bộ người) + 本 (běn) = 体 (tǐ — thân thể)
     → 亻 gợi nghĩa: liên quan NGƯỜI
     → → gợi âm: tǐ (gần giống běn? — âm đã drift qua lịch sử)

BỘ THỦ (Radicals) — "linh kiện" cơ bản (~214 bộ thủ):
   氵= nước (sông, biển, hồ, mưa, rượu...)
   火/灬 = lửa (nấu, nóng, đốt, đèn...)
   木 = cây (rừng, bàn, ghế, cây cối...)
   金/钅= kim loại (sắt, đồng, tiền...)
   亻= người (anh ấy, bạn, làm, ngồi...)
   女 = nữ (mẹ, chị, đẹp, cưới...)
   口 = miệng (ăn, hát, gọi, uống...)
   心/忄= tim/tâm (yêu, ghét, nghĩ, lo...)
   手/扌= tay (cầm, đánh, kéo, vẽ...)
   目 = mắt (nhìn, xem, mù, ngủ...)

→ ⭐ Ký tự Trung = VISUAL CHUNK SYSTEM
  Mỗi ký tự = 1 đơn vị hình ảnh encode nghĩa
  Nhìn 氵→ NÃO TỰ ĐỘNG activate "liên quan nước"
  → Reader Trung Quốc nhìn chữ LẠ cũng ĐOÁN ĐƯỢC nghĩa gần đúng từ bộ thủ
  → Alphabetic reader (Việt/Anh) nhìn chữ lạ → KHÔNG đoán được nghĩa (chỉ đoán được âm)
```

**Số lượng ký tự cần biết:**

```
  Biết đọc báo:        ~2,000-3,000 ký tự
  Tốt nghiệp phổ thông: ~3,500 ký tự
  Người có học:          ~5,000-8,000 ký tự
  Từ điển đầy đủ:       ~50,000+ ký tự (nhưng phần lớn cổ/hiếm)

  So sánh:
  Vietnamese alphabet:  29 chữ cái + dấu thanh
  English alphabet:     26 chữ cái
  Chinese "alphabet":   ~3,500 ký tự thường dùng (mỗi cái = 1 "chữ cái" riêng)

  → Trẻ em Trung Quốc mất ~6 năm tiểu học để học đủ ký tự đọc báo
  → Trẻ em Việt/Anh mất ~1-2 năm để học alphabet + ghép vần
  → TRADE-OFF: Chinese mất lâu hơn nhưng sau đó đọc NHANH hơn (visual → meaning trực tiếp)
```

### §4.3 — English: Phrasal verbs + idioms

English có hệ thống phrasal verbs — khi verb kết hợp với preposition/particle, tạo ra nghĩa MỚI không suy luận được:

```
PHRASAL VERBS — nghĩa KHÔNG suy luận được từ từng phần:

  give up        = bỏ cuộc        (≠ "cho" + "lên")
  give in        = nhượng bộ      (≠ "cho" + "vào")
  give away      = cho đi/tiết lộ (≠ "cho" + "đi")

  look up        = tra cứu        (≠ "nhìn" + "lên")
  look up to     = ngưỡng mộ      (≠ "nhìn" + "lên" + "tới")
  look down on   = coi thường     (≠ "nhìn" + "xuống" + "lên")
  look after     = chăm sóc       (≠ "nhìn" + "sau")
  look forward to = mong đợi      (≠ "nhìn" + "phía trước" + "tới")
  look into      = điều tra       (≠ "nhìn" + "vào")
  look out       = cẩn thận       (≠ "nhìn" + "ra")

  break down     = hỏng / sụp đổ  (≠ "phá" + "xuống")
  break up       = chia tay        (≠ "phá" + "lên")
  break in       = đột nhập        (≠ "phá" + "vào")
  break out      = bùng nổ         (≠ "phá" + "ra")
  break through  = đột phá         (≠ "phá" + "xuyên qua")

  come up with   = nghĩ ra         (≠ "đến" + "lên" + "với")
  figure out     = tìm hiểu/giải   (≠ "hình" + "ra")
  put up with    = chịu đựng       (≠ "đặt" + "lên" + "với")
  run out of     = hết             (≠ "chạy" + "ra" + "của")
  get along with = hòa thuận       (≠ "nhận" + "dọc" + "với")
  turn out       = hóa ra          (≠ "quay" + "ra")
  work out       = tập thể dục / giải quyết (≠ "làm" + "ra")

→ Ước tính: ~5,000 phrasal verbs thường gặp trong English
→ MỖI phrasal verb = 1 CHUNK phải compile riêng (không suy luận được)
→ Đây là RÀO CẢN LỚN NHẤT cho English L2 learners

SO SÁNH:
  Vietnamese KHÔNG CÓ phrasal verbs (mỗi từ giữ nghĩa riêng)
  Chinese KHÔNG CÓ phrasal verbs (verb + complement nhưng nghĩa suy luận được hơn)
  → English phrasal verb = đặc thù English, phải học từng cái
```

### §4.4 — Vietnamese: Tone system 6 thanh

```
Vietnamese có 6 THANH — cùng 1 âm, KHÁC THANH = KHÁC NGHĨA HOÀN TOÀN:

  ma  (thanh ngang)   = ghost (ma)
  mà  (thanh huyền)   = but/which (liên từ, mệnh đề quan hệ)
  mả  (thanh hỏi)     = grave (mộ)
  mã  (thanh ngã)     = horse (ngựa, Hán-Việt) / code (mã số)
  má  (thanh sắc)     = mother (mẹ, phương ngữ Nam) / cheek (má)
  mạ  (thanh nặng)    = rice seedling (mạ lúa) / gold plating (mạ vàng)

  → 6 từ hoàn toàn khác nghĩa, chỉ khác THANH (pitch pattern)
  → Người nước ngoài hay nói sai thanh → nói sai NGHĨA hoàn toàn
  → Ví dụ kinh điển: "mấy bà đi chợ" nếu sai thanh có thể thành... khác!

TIẾNG TRUNG (Mandarin) có 4 thanh:
  mā (thanh 1: cao bằng)     = 妈 (mẹ)
  má (thanh 2: lên)           = 麻 (gai/tê)
  mǎ (thanh 3: xuống lên)    = 马 (ngựa)
  mà (thanh 4: xuống)         = 骂 (mắng/chửi)
  (+ thanh nhẹ: ma)           = 吗 (trợ từ hỏi)

  → Câu kinh điển: "妈妈骑马，马慢，妈妈骂马"
    (māma qí mǎ, mǎ màn, māma mà mǎ)
    (mẹ cưỡi ngựa, ngựa chậm, mẹ mắng ngựa)
    → TẤT CẢ là âm "ma" với 4 thanh khác nhau!

TIẾNG ANH: KHÔNG CÓ thanh (tone)
  → English dùng intonation (ngữ điệu câu) chứ không dùng tone (thanh từ)
  → Lên giọng cuối câu = hỏi. Xuống = khẳng định.
  → NHƯNG: lên/xuống giọng KHÔNG đổi nghĩa TỪ (chỉ đổi ý định CÂU)
```

### §4.5 — Chinese: Thành ngữ 4 chữ (Chengyu 成语)

```
Tiếng Trung có hệ thống THÀNH NGỮ 4 CHỮ (成语 chéngyǔ) cực kỳ phong phú:
  → ~5,000 thành ngữ thường dùng, tổng ~20,000+
  → Mỗi thành ngữ = 4 ký tự = 1 câu chuyện/triết lý nén gọn

Ví dụ:
  一石二鸟 (yì shí èr niǎo — một đá hai chim) = "một công đôi việc"
  画蛇添足 (huà shé tiān zú — vẽ rắn thêm chân) = "thêm thắt không cần thiết"
  守株待兔 (shǒu zhū dài tù — giữ gốc cây đợi thỏ) = "thụ động chờ may mắn"
    → Câu chuyện: nông dân thấy thỏ đâm vào gốc cây chết, 
       từ đó ngồi đợi bên gốc cây thay vì đi săn
  对牛弹琴 (duì niú tán qín — đánh đàn cho bò nghe) = "nói chuyện với người không hiểu"
  塞翁失马 (sài wēng shī mǎ — ông già biên giới mất ngựa) = "trong họa có phúc"
    → Câu chuyện dài: mất ngựa → ngựa dẫn thêm ngựa về → 
       con cưỡi ngựa bị gãy chân → không phải đi lính → sống sót

  → Mỗi chéngyǔ = 1 meta-chunk cực nén: 4 ký tự pack nghĩa CẢ CÂU CHUYỆN
  → Người Trung Quốc dùng chéngyǔ trong conversation hàng ngày
  → Tương đương Vietnamese: tục ngữ/thành ngữ nhưng Trung Quốc NHIỀU HƠN RẤT NHIỀU
     và có format cố định 4 chữ
```

---

## §5 — Tổng hợp so sánh

### §5.1 — Bảng so sánh toàn diện

| Đặc điểm | Tiếng Việt | English | 中文 Mandarin |
|---|---|---|---|
| **Morphology type** | Isolating (từ không đổi) | Fusional (từ biến dạng) | Isolating (từ không đổi) |
| **Word order cơ bản** | SVO | SVO (strict) | SVO |
| **Topic-Comment** | ✅ Mạnh | 🟡 Yếu (literary) | ✅ Rất mạnh |
| **Thì (Tense)** | Trợ từ: đã/đang/sẽ | Biến dạng verb: eat/ate + auxiliary | Trợ từ: 了/在/会 |
| **Số nhiều** | Từ: các/những | Hậu tố: -s/-es + bất quy tắc | Không bắt buộc mark |
| **Classifier** | ⭐ BẮT BUỘC (con/cái/chiếc...) | ❌ Không có | ⭐ BẮT BUỘC (个/只/条...) |
| **Article** | ❌ Không có | ⭐ BẮT BUỘC (a/the) | ❌ Không có |
| **Pronoun system** | ⭐ Social-relational (hàng chục) | Person-based (I/you/he/she) | Person-based (我/你/他/她) |
| **Câu hỏi** | Thêm từ, giữ trật tự | ĐẢO trật tự + auxiliary | Thêm 吗 (ma), giữ trật tự |
| **Phủ định** | không/chưa (vĩnh viễn/tạm thời) | not (chung) | 不/没 (ý chí/sự kiện) |
| **Writing system** | Alphabetic (chữ cái Latin + dấu) | Alphabetic (chữ cái Latin) | Logographic (~3,500 ký tự thường) |
| **Modifier order** | HEAD-FIRST (chó đen) | HEAD-LAST (black dog) | HEAD-LAST (黑狗) |
| **Tone** | ⭐ 6 thanh | ❌ Không | ⭐ 4 thanh |
| **Relative clause** | Post-nominal (chó MÀ tôi nuôi) | Post-nominal (dog THAT I raise) | Pre-nominal (我养的狗) |
| **Trợ từ cuối câu** | ⭐ Phong phú (nhé/nhỉ/ạ/à...) | ❌ Hầu như không | ⭐ Phong phú (吗/呢/吧/啊...) |
| **Irregular forms** | ❌ Gần như 0 | ⭐ Nhiều (~200 irregular verbs) | ❌ Gần như 0 |
| **Phrasal verbs** | ❌ Không có | ⭐ ~5,000 | ❌ Không có |
| **Thành ngữ 4 chữ** | Có nhưng ít | Có idioms nhưng length khác nhau | ⭐ ~5,000+ chéngyǔ (format cố định 4 chữ) |

### §5.2 — Mỗi ngôn ngữ BUỘC phải chunk gì (mỗi câu, vô thức)

```
VIETNAMESE SPEAKER — mỗi câu NÓI phải xử lý vô thức:
  ✅ Classifier: animate hay inanimate? hình dạng? (con/cái/chiếc/tờ/quyển...)
  ✅ Social pronoun: ai nói với ai? quan hệ gì? (em/anh/con/bạn/thầy...)
  ✅ Negation type: tạm thời hay vĩnh viễn? (chưa vs không)
  ✅ Tone: 6 thanh phải đúng (ma ≠ mà ≠ mả ≠ mã ≠ má ≠ mạ)
  ✅ Sentence-final particle: thái độ gì? (nhé/nhỉ/ạ/à/hả/sao...)

ENGLISH SPEAKER — mỗi câu NÓI phải xử lý vô thức:
  ✅ Article: specific hay general? (the vs a)
  ✅ Verb form: thì gì? (eat/ate/eaten/eating/eats)
  ✅ 3rd person gender: he hay she?
  ✅ Question inversion: phải đảo auxiliary (do you...? are you...?)
  ✅ Irregular forms: nhớ từng verb bất quy tắc
  ✅ Phrasal verb: chọn đúng combination

CHINESE SPEAKER — mỗi câu NÓI phải xử lý vô thức:
  ✅ Classifier: loại gì? (个/只/条/本/张/把/件... chi tiết hơn Việt)
  ✅ Negation type: ý chí hay sự kiện? (不 bù vs 没 méi)
  ✅ Aspect particle: hoàn thành? kinh nghiệm? đang? (了/过/着)
  ✅ Tone: 4 thanh phải đúng
  ✅ Character: nhớ hình dạng ký tự (khi viết)
  ✅ 3 loại "de": 的/地/得 (khi viết — nói thì giống nhau)
```

### §5.3 — Framework lens: Moderate Whorfian

Từ bảng §5.2, thấy rõ: **mỗi ngôn ngữ BUỘC speaker attention đến CÁC KHÍA CẠNH KHÁC NHAU** của cùng 1 tình huống.

```
CÙNG 1 TÌNH HUỐNG: "Tôi chưa ăn cơm trưa"

Vietnamese speaker VÔ THỨC xử lý:
  - "chưa" (tạm thời, chưa nhưng sẽ ăn)
  - "tôi" (quan hệ xã hội với người nghe)
  - "cơm trưa" (không cần classifier vì không đếm)

English speaker VÔ THỨC xử lý:
  - "haven't eaten" (present perfect tense marking)
  - "I" (không cần xử lý social)
  - "lunch" (không cần classifier, nhưng cần article? "the lunch" hay "lunch"?)

Chinese speaker VÔ THỨC xử lý:
  - "没吃" méi chī (没 = sự kiện chưa xảy ra, khác "không muốn ăn")
  - "午饭" wǔfàn (cơm trưa — không cần classifier vì không đếm)
  - 4 thanh điệu phải chính xác

→ MODERATE WHORFIAN: Mỗi ngôn ngữ shape ATTENTION khác nhau
  Vietnamese: attention đến social relationship + temporality
  English: attention đến tense precision + specificity (the/a)
  Chinese: attention đến intention vs fact + visual character form

→ NHƯNG: underlying CHUNK (cảm giác đói, plan ăn trưa) LÀ GIỐNG NHAU
  → Ngôn ngữ shape HANDLE/ACCESS, không shape SUBSTRATE
```

---

## §6 — Verbal hierarchy: Từ → Cụm từ → Câu → Đoạn → Bài

```
LEVEL 1 — TỪ (Word) = CHUNK đơn lẻ
  "xe"                      = 1 chunk phonological, link tới network chunks ngữ nghĩa
  → Active khi nghe/đọc: retrieve associated chunks

LEVEL 2 — CỤM TỪ (Phrase) = CHUNK compound
  "xe máy"                  = 2 chunks kết hợp → 1 compound unit
  "con chó đen lớn"         = 4 chunks kết hợp → 1 noun phrase
  → Modifier constrain: "đen lớn" thu hẹp "chó" về subset cụ thể

LEVEL 3 — CÂU (Sentence) = CHUNK CHAIN theo template
  "Tôi đi xe máy"          = 3 chunks chain theo SVO template
  → Grammar template constrain: ai (S) làm gì (V) với gì (O)
  → Template = Construction Grammar (Goldberg 1995): learned chunk-chain patterns

LEVEL 4 — ĐOẠN VĂN (Paragraph) = SCHEMA (organized chunk chains, có purpose)
  "Hôm nay tôi đi xe máy ra chợ. Mua được nhiều đồ tươi.
   Về nhà nấu cơm cho cả nhà. Ai cũng khen ngon."
  → 4 câu liên kết: timeline + causality + evaluation
  → Có PURPOSE: kể chuyện đi chợ + kết quả

LEVEL 5 — BÀI VĂN / VĂN BẢN (Text) = PLAN (nested schemas, có goal structure)
  Bài luận, báo cáo, truyện ngắn, email, tin nhắn dài,...
  → Nhiều đoạn liên kết: intro → body → conclusion
  → Có GOAL: thuyết phục, thông tin, giải trí, yêu cầu,...

MAPPING VÀO FRAMEWORK:
  Level 1 Từ        ↔ Chunk (atom)
  Level 2 Cụm từ    ↔ Chunk compound (small molecule)
  Level 3 Câu       ↔ Chunk chain (schema đơn giản)
  Level 4 Đoạn      ↔ Schema (organized, có purpose)
  Level 5 Bài       ↔ Plan (goal-directed, nested schemas)
```

---

## §7 — Construction Grammar: Tại sao word order quan trọng

**Construction Grammar** (Goldberg 1995, 2006) — lý thuyết cho rằng:
Grammar = bộ sưu tập **TEMPLATES** (constructions) mà speaker đã compile.

```
Mỗi Construction = 1 compiled chunk-chain template có SLOTS:

CONSTRUCTION 1: [S] [V] [O]                     = SVO cơ bản
  Slot S = ai?  Slot V = làm gì?  Slot O = cái gì?
  "Tôi ăn cơm" → S=tôi, V=ăn, O=cơm ✅

CONSTRUCTION 2: [S] [V] [O1] [O2]              = Ditransitive (cho ai cái gì)
  "Tôi cho bạn quyển sách" → S=tôi, V=cho, O1=bạn, O2=quyển sách ✅

CONSTRUCTION 3: [S] [V] [O] [Result]            = Resultative
  "She painted the wall blue" → S=she, V=painted, O=wall, Result=blue
  "Cô ấy sơn tường màu xanh" → S=cô ấy, V=sơn, O=tường, Result=màu xanh

CONSTRUCTION 4: [Topic], [S] [V] [O]            = Topic-Comment (Việt + Trung)
  "Cơm, tôi ăn rồi" → Topic=cơm, S=tôi, V=ăn, ...
  "这本书，我看过了" → Topic=这本书, S=我, V=看, ...

CONSTRUCTION 5: [câu hỏi] — mỗi ngôn ngữ KHÁC template:
  Việt: [S] [V] [question word]?         "Bạn ăn GÌ?"
  Anh:  [Wh] [aux] [S] [V]?             "WHAT DO you EAT?"
  Trung: [S] [V] [question word]?        "你吃什么 (nǐ chī shénme)?"

TẠI SAO "tôi xe đi" SAI:
  → PFC cố match "tôi xe đi" vào MỌI construction templates đã compile
  → Không match được template nào:
    - Không phải SVO (V ở đâu? "xe" là noun, không phải verb)
    - Không phải Topic-Comment (thiếu dấu phẩy/pause sau topic)
    - Không phải câu hỏi
  → PFC báo MISMATCH → body signal "sao sao ấy"
  → Đây là cơ chế: cảm giác "sai ngữ pháp" = PFC TEMPLATE MISMATCH

TẠI SAO "xe máy tôi đi" HỢP LỆ (dù sao sao):
  → Match Topic-Comment template: Topic="xe máy", Comment="tôi đi"
  → Nghĩa: "Về cái xe máy ấy, tôi đi rồi"
  → "Sao sao" vì THIẾU context marker (comma, "thì", "ấy")
  → Thêm marker = hoàn toàn chuẩn: "Xe máy ẤY, tôi đi rồi" ✅

CONSTRUCTION GRAMMAR INSIGHT:
  → Trẻ em KHÔNG học "quy tắc ngữ pháp" abstract trước
  → Trẻ em học TỪNG construction cụ thể qua repetition:
    - Nghe "mẹ ăn cơm", "bé ăn cơm", "bố ăn cơm" → compile template [S] ăn [O]
    - Nghe "cho mẹ", "cho bé", "cho bạn" → compile template cho [O]
    - DẦN DẦN generalize: [S] [V] [O] (từ nhiều instances cụ thể)
  → Giống cách compile chunk: repetition → pattern extract → generalized template
  → Tomasello 2003: "Usage-based" acquisition = learn from instances, not rules
```

---

## §8 — Câu hỏi mở + Liên kết framework

### §8.1 — Câu hỏi mở từ phân tích trên

1. **Classifier system Vietnamese có THỰC SỰ giúp phân loại nhanh hơn?** Prediction: Vietnamese speakers phân loại animate/inanimate nhanh hơn English speakers trong reaction time experiments. (Imai & Mazuka 2007 có evidence cho Japanese classifiers.)

2. **Chinese visual encoding có giúp đọc nhanh hơn?** Prediction: Expert Chinese readers đọc passage cùng content nhanh hơn English readers vì visual→meaning skip auditory. (DeLuca et al. có evidence cho deaf readers.)

3. **Vietnamese social pronoun system có giúp social modeling tốt hơn?** Prediction: Vietnamese speakers habitual attention đến social hierarchy → nhanh hơn trong social reasoning tasks? (Chưa có evidence rõ.)

4. **Phrasal verb system English có CHẬM HƠN cho L2 learner?** Yes — extensive evidence. Phrasal verbs là barrier #1 cho intermediate→advanced English (Laufer & Eliasson 1993).

5. **Topic-Comment flexibility (Việt + Trung) có giúp pragmatic communication tốt hơn?** Prediction: Topic-Comment speakers dễ dàng hơn trong organizing information for listener. (Chưa có evidence so sánh.)

6. **Construction Grammar vs Chomsky Universal Grammar**: Trẻ em HỌC constructions từ input (Tomasello) hay CÓ SẴN grammar capacity bẩm sinh (Chomsky)? Framework position: neural substrate bẩm sinh (Broca sequence processing) + specific constructions learned (Construction Grammar). Moderate reconciliation.

### §8.2 — Liên kết framework

- **Moderate Whorfian claim** (F1 08 §5.6): Mỗi ngôn ngữ shape HANDLES (attention patterns), không shape SUBSTRATE (underlying chunks). Phân tích trên = evidence chi tiết cho claim này.

- **NT6 Verbal-as-handle** (F1 08 §5.4): Verbal labels = retrieval paths + symbolic compression, NOT 5th modality. Phân tích trên cho thấy: verbal structure (grammar, word order, constructions) = cách tổ chức retrieval paths, không phải cách tổ chức chunks.

- **Communication Modality** (Modality-Analysis.md §2): Verbal là 1 FORMAT trong Communication Modality. Phân tích trên = deep drill FORMAT "verbal" (1 trong nhiều formats).

- **Processing Layers model** (session N+5 discussion): Verbal = L2 Encoding layer. Grammar templates = L2 compiled patterns. Word order violation detection = L1→L2 mismatch signal.

- **Construction Grammar** ↔ **Schema/Chunk.md**: Constructions = compiled chunk-chain templates. Learning grammar = compiling templates via repetition (same mechanism as chunk compile).

---

## §9 — Tham khảo (References)

| Tác giả | Năm | Công trình | Confidence |
|---|---|---|---|
| Goldberg, A. | 1995, 2006 | Construction Grammar | 🟢 |
| Tomasello, M. | 2003 | Usage-based language acquisition | 🟢 |
| Chomsky, N. | 1957, 1965 | Universal Grammar, generative linguistics | 🟡 (counter-hypothesis) |
| Slobin, D. | 1996 | Thinking for Speaking | 🟢 |
| Boroditsky, L. | 2001 | Mandarin vs English time metaphors | 🟢 |
| Winawer, J. et al. | 2007 | Russian blue (синий/голубой) | 🟢 |
| Imai, M. & Mazuka, R. | 2007 | Classifier cognitive effects | 🟢 |
| Collins, A. & Loftus, E. | 1975 | Spreading Activation model | 🟢 |
| Miller, G. | 1956 | Magical number 7±2, chunking | 🟢 |
| Laufer, B. & Eliasson, S. | 1993 | Phrasal verb acquisition difficulty | 🟢 |
| DeLuca, V. et al. | — | Chinese deaf reading advantage | 🟡 |
| Kay, P. & Kempton, W. | 1984 | Color terms and perception | 🟢 |
| Comrie, B. | 1989 | Language Universals and Linguistic Typology | 🟢 |
| Dryer, M. & Haspelmath, M. | 2013 | World Atlas of Language Structures (WALS) | 🟢 |
| Li, C. & Thompson, S. | 1981 | Mandarin Chinese: A Functional Reference Grammar | 🟢 |
| Emeneau, M. | 1951 | Vietnamese linguistic typology | 🟢 |

---

> **01-Natural-Language-Architecture.md — End of file.**
>
> Tài liệu tham khảo cho exploration session N+5. Đọc nghiền ngẫm, không cần hiểu hết 1 lần. Mỗi phần independent, có thể đọc riêng.
>
> Phiên bản: v1.0, 2026-04-16. Sẽ update nếu drill thêm phát hiện mới.
