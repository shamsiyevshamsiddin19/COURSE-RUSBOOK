# Fayoza · Рус тили — kurs kitobi (kitob-4)

Bu papka — loyihaning **asosiy ishi**. `kitob-1`, `kitob2`, `kitob3` eski
urinishlar; ular tarix uchun saqlanib turibdi, lekin ishlanmaydi.

Hozirgi holat: **28 sahifa** — muqova, reja, muallifdan, foydalanish
qo'llanmasi, rus alifbosi (2 sahifa), **1-dars**, **2-dars**, orqa muqova.

---

## Ishga tushirish

```bash
python3 build.py          # darslarni yig'ib, index.html ni quradi
python3 check_pages.py    # matn sahifadan chiqib ketganini tekshiradi
node generate_pdf.js      # o'qish uchun PDF (A4, 210x297)
node generate_pdf.js --print   # bosmaxona uchun PDF (216x303, 3mm bleed)
```

Odatdagi tartib: `build.py` → `check_pages.py` → tuzatish → yana
`build.py` → `generate_pdf.js`.

`index.html` — **yig'iladigan fayl, uni qo'lda tahrirlamang**. O'zgartirish
kerak bo'lsa `template.html` yoki `lessons/lessonNN.py` ga tegiladi.

---

## Fayllar

| Fayl | Nima qiladi |
|---|---|
| `template.html` | O'zgarmas qism: muqova, reja, muallifdan, alifbo, orqa muqova |
| `lessons/lessonNN.py` | Bitta darsning butun mazmuni |
| `build.py` | Darslarni HTML ga aylantirib, `template.html` ichiga joylaydi |
| `check_pages.py` | Chrome orqali o'lchab, sig'magan sahifani topadi |
| `generate_pdf.js` | Chrome headless bilan PDF chiqaradi |
| `styles/booklet.css` | Barcha uslublar (raqamlangan bo'limlar bilan) |
| `styles/noto.css` | Matn fonti — Noto Sans |
| `styles/fonts.css` | Sarlavha fonti — Montserrat |

---

## Dars qanday yoziladi

Dars — bu bloklar ro'yxati. Har bir blok — lug'at, ichida `"type"` bor.
Sahifani uzish uchun ro'yxatga oddiy `"PAGE"` satri qo'yiladi:

```python
LESSON = {
    "number": 3,
    "running": "Моя семья",
    "blocks": [
        {"type": "title", "number": 3, "ru": "МОЯ СЕМЬЯ", "uz": "Oilam"},
        {"type": "cando", "items": ["...", "..."]},
        {"type": "sec", "ru": "ДИАЛОГ", "uz": "Suhbat"},
        {"type": "dialog", "n": 1, "scene": "...", "lines": [
            ("Аза́мат:", "Э́то моя́ семья́.", "Bu mening oilam."),
        ]},
        "PAGE",
        ...
    ],
}
```

### Mavjud blok turlari

| `type` | Nima uchun | Asosiy kalitlar |
|---|---|---|
| `title` | Dars sarlavhasi | `number`, `ru`, `uz` |
| `cando` | «Bu darsdan so'ng qila olasiz» | `items` |
| `sec` | Bo'lim sarlavhasi | `ru`, `uz` |
| `text` | Oddiy xatboshi | `p`, `class` |
| `dialog` | Suhbat | `n`, `scene`, `lines` |
| `vocab` | Lug'at jadvali | `words` — `(so'z, talaffuz, ma'no, izoh)` |
| `pron` | Talaffuz qutisi (sariq) | `title`, `p`, `rows` |
| `keyphrases` | Asosiy iboralar (qizil) | `sub`, `rows` |
| `gram` | Grammatika qutisi (ko'k) | `title`, `p`, `pairs`, `tables`, `note` |
| `ex` | Mashq | `n`, `task`, `items`, `match`, `model`, `cards`, `rows` |
| `roleplay` | Rolli o'yin, ikki ustun | `cols` |
| `model` | Namuna suhbat | `lines` |
| `read` | O'qish matni (monolog) | `items` |
| `cards` | Vizitka / jadval kabi haqiqiy material | `items` |
| `write` | Yozish uchun chiziqlar | `rows` |
| `culture` | Madaniyat qutisi (yashil) | `title`, `p`, `note` |
| `advice` | Ustozdan maslahat | `title`, `p`, `chain`, `after` |
| `selfcheck` | O'zini tekshirish ro'yxati | `items` |

### Matn ichidagi belgilar

| Belgi | Natija |
|---|---|
| `*matn*` | **qalin** |
| `_matn_` | _kursiv_ |
| `~` | qisqa yozuv chizig'i |
| `~~` | o'rtacha chiziq |
| `~~~` | uzun chiziq |

---

## Qat'iy qoidalar

**1. Urg'u belgisi har doim qo'yiladi.** Har bir ruscha so'zda urg'uli
unli ustiga `U+0301` (combining acute) qo'yiladi: `Здра́вствуйте`,
`Москва́`. `ё` har doim urg'uli, shuning uchun unga belgi qo'yilmaydi.

**2. Inter fonti ishlatilmaydi.** Uning Google Fonts subseti urg'u
belgisini unliga biriktirmaydi — urg'u keyingi harf ustiga tushib
qoladi (`Ша́хло` o'rniga `Шах́ло`). Shuning uchun matn fonti
**Noto Sans** (kerakli belgilargacha qisqartirilib, `assets/fonts/`
ichiga joylangan, jami ~120 KB). Boshqa fontga o'tishdan oldin albatta
urg'uli so'zni sinab ko'ring.

**3. Matn sig'masa — shrift kichraytirilmaydi.** «(davomi)» ham
yozilmaydi. Sig'masa `lessonNN.py` ga yangi `"PAGE"` qo'yiladi.
Qayerda va qanchaga sig'magani `check_pages.py` da ko'rinadi:

```bash
python3 check_pages.py -b    # har bir blokning balandligi bilan
```

**4. Sahifa soni 4 ga karrali bo'lishi kerak.** Bosmaxona qog'ozni
to'rttadan buklaydi. `build.py` karrali bo'lmasa ogohlantiradi.

---

## Dars tuzilishi

Har bir dars bir xil yo'ldan boradi — bu tartib ataylab tanlangan:
avval **eshitadi va ko'radi**, keyin **tushunadi**, oxirida **o'zi
qo'llaydi**.

```
ДИАЛОГ      jonli suhbat, tarjimasi bilan
СЛОВА       lug'at — dialogda uchragan tartibda, talaffuzi bilan
ПРОИЗНОШЕНИЕ  aynan o'zbek tilida so'zlashuvchilar qiynaladigan tovushlar
ЗАПОМНИТЕ   asosiy iboralar — grammatikaga o'tishdan oldin
ГРАММАТИКА  qoida — dialogda ko'rgan narsa tushuntiriladi
УПРАЖНЕНИЯ  mashqlar — oson dan qiyin ga
ГОВОРИТЕ!   rolli o'yin, guruh o'yini
ЧИТАЙТЕ!    o'qish matni va haqiqiy material (vizitka, jadval)
ПРОВЕРЬ СЕБЯ  o'z-o'zini tekshirish ro'yxati
```

Andoza: Ruslan Russian 1 (A1, John Langran) va RKI metodikasidagi
dars bosqichlari.

---

## Keyingi qadamlar

- 3–50-darslar (`lessons/lesson03.py` va hokazo). Reja `template.html`
  ichidagi mundarijada turibdi; yozilmagan darslar `pending` sinfi
  bilan belgilangan va sahifa raqami o'rniga «—» ko'rsatadi.
- Audio: hozir dialoglarda raqam bor, lekin yozuv yo'q. QR kod yoki
  havola qo'shilsa, `dialog` blokiga bitta kalit qo'shish yetadi.
- Javoblar kaliti (ключи) — kitob oxirida alohida bo'lim.
