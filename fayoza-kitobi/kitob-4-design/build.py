#!/usr/bin/env python3
"""Kitobni yig'adi: darslarni lessons/ dan o'qib, index.html ni quradi.

    python3 build.py

Har bir dars — bloklar ro'yxati (lessons/lessonNN.py ichida BLOCKS).
Blok — bu lug'at, ichida "type" kaliti bor. Sahifani uzish uchun
ro'yxatga oddiy "PAGE" satri qo'yiladi:

    BLOCKS = [
        {"type": "title", ...},
        {"type": "sec", "ru": "ДИАЛОГ", "uz": "Suhbat"},
        {"type": "dialog", ...},
        "PAGE",
        ...
    ]

Shu tariqa matn sahifaga sig'masa, shrift kichraytirilmaydi va
"(davomi)" yozilmaydi — oddiygina yangi "PAGE" qo'yiladi.

Sahifa raqamlari, kolontitul, reja va navigatsiya ro'yxati shu
yerdan avtomatik hisoblanadi.
"""
import html
import importlib.util
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).parent
E = html.escape

# 1 muqova, 2-3 reja, 4 muallifdan, 5 qo‘llanma, 6-7 alifbo — darslar 8-sahifadan
FIRST_LESSON_PAGE = 8

LEFT_FACET = """        <svg class="bottom-facet" viewBox="0 0 340 80" preserveAspectRatio="none">
          <polygon points="0,80 180,80 340,25 0,80" fill="#eaebee"/>
          <polygon points="120,80 340,80 340,0" fill="#e03538"/>
          <polygon points="120,80 230,80 340,0" fill="#ca282c"/>
        </svg>"""

RIGHT_FACET = """        <svg class="bottom-facet" viewBox="0 0 340 80" preserveAspectRatio="none">
          <polygon points="0,0 0,80 220,80" fill="#e03538"/>
          <polygon points="0,0 110,80 220,80" fill="#ca282c"/>
          <polygon points="0,25 160,80 340,80" fill="#eaebee"/>
        </svg>"""

I = "        "  # bloklarning asosiy chekinishi


def load_lessons():
    out = []
    for path in sorted((ROOT / "lessons").glob("lesson*.py")):
        spec = importlib.util.spec_from_file_location(path.stem, path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        out.append(mod.LESSON)
    return out


# ------------------------------------------------------- yordamchilar

def rich(s):
    """Matnni xavfsiz qiladi, lekin bir nechta oddiy belgini qoldiradi.

    *qalin*  -> <b>qalin</b>
    _kursiv_ -> <i>kursiv</i>
    ~bo'sh~  -> yozish uchun chiziq
    """
    s = E(s)
    s = re.sub(r"\*([^*]+)\*", r"<b>\1</b>", s)
    s = re.sub(r"_([^_]+)_", r"<i>\1</i>", s)
    s = s.replace("~~~", '<span class="gap lg"></span>')
    s = s.replace("~~", '<span class="gap"></span>')
    s = s.replace("~", '<span class="gap sm"></span>')
    return s


def attr(d, key, default=""):
    return d.get(key, default)


# ------------------------------------------------------------ bloklar

def b_title(b):
    out = [f'{I}<div class="lesson-eyebrow">УРОК {b["number"]}</div>',
           f'{I}<h1 class="lesson-title">{E(b["ru"])}</h1>']
    if b.get("uz"):
        out.append(f'{I}<div class="lesson-title-uz">{E(b["uz"])}</div>')
    return "\n".join(out)


def b_cando(b):
    items = "\n".join(f'{I}    <li>{rich(t)}</li>' for t in b["items"])
    title = attr(b, "title", "BU DARSDAN SO‘NG SIZ QILA OLASIZ")
    return (f'{I}<div class="cando">\n'
            f'{I}  <div class="cando-title">{E(title)}</div>\n'
            f'{I}  <ul class="cando-list">\n{items}\n{I}  </ul>\n'
            f'{I}</div>')


def b_sec(b):
    uz = f'\n{I}  <span class="sec-uz">{E(b["uz"])}</span>' if b.get("uz") else ""
    return (f'{I}<div class="sec">\n'
            f'{I}  <span class="sec-ru">{E(b["ru"])}</span>{uz}\n'
            f'{I}  <span class="sec-line"></span>\n'
            f'{I}</div>')


def b_text(b):
    cls = attr(b, "class", "body-text")
    return "\n".join(f'{I}<p class="{cls}">{rich(t)}</p>' for t in b["p"])


def b_dialog(b):
    out = [f'{I}<div class="dlg">']
    if b.get("scene"):
        n = f'<span class="dlg-scene-n">{b["n"]}</span>' if b.get("n") else ""
        out.append(f'{I}  <div class="dlg-scene">{n}<span>{E(b["scene"])}</span></div>')
    out.append(f'{I}  <div class="dlg-body">')
    for line in b["lines"]:
        who, text = line[0], line[1]
        tr = line[2] if len(line) > 2 else ""
        tr_html = f'<span class="dlg-tr">{E(tr)}</span>' if tr else ""
        out.append(f'{I}    <div class="dlg-line">'
                   f'<span class="dlg-who">{E(who)}</span>'
                   f'<span class="dlg-text">{E(text)}{tr_html}</span></div>')
    out.append(f'{I}  </div>')
    out.append(f'{I}</div>')
    return "\n".join(out)


def b_vocab(b):
    heads = attr(b, "heads", ("So‘z", "Talaffuz", "Ma’nosi"))
    rows = []
    for w in b["words"]:
        ru, tr, uz = w[0], w[1], w[2]
        note = f' <span class="v-note">{E(w[3])}</span>' if len(w) > 3 and w[3] else ""
        rows.append(f'{I}    <tr><td class="v-ru">{E(ru)}</td>'
                    f'<td class="v-tr">{E(tr)}</td>'
                    f'<td class="v-uz">{E(uz)}{note}</td></tr>')
    body = "\n".join(rows)
    return (f'{I}<table class="vocab">\n'
            f'{I}  <thead><tr>'
            f'<th>{E(heads[0])}</th><th>{E(heads[1])}</th><th>{E(heads[2])}</th>'
            f'</tr></thead>\n'
            f'{I}  <tbody>\n{body}\n{I}  </tbody>\n'
            f'{I}</table>')


def _pairs(rows):
    body = "\n".join(
        f'{I}    <tr><td class="p-ru">{rich(ru)}</td>'
        f'<td class="p-uz">{rich(uz)}</td></tr>' for ru, uz in rows)
    return f'{I}  <table class="pair">\n{body}\n{I}  </table>'


def _gtable(t):
    head = "".join(f"<th>{E(h)}</th>" for h in t["head"])
    rows = []
    for r in t["rows"]:
        cells = []
        for j, c in enumerate(r):
            cls = "k" if j == 0 else ""
            if isinstance(c, tuple):
                c, cls = c[0], c[1]
            cls = f' class="{cls}"' if cls else ""
            cells.append(f"<td{cls}>{rich(str(c))}</td>")
        rows.append(f'{I}    <tr>{"".join(cells)}</tr>')
    body = "\n".join(rows)
    return (f'{I}  <table class="gtable">\n'
            f'{I}    <thead><tr>{head}</tr></thead>\n'
            f'{body}\n{I}  </table>')


def _box(b, cls, title_cls, default_title):
    out = [f'{I}<div class="{cls}">']
    title = attr(b, "title", default_title)
    if title:
        out.append(f'{I}  <div class="{title_cls}">{E(title)}</div>')
    for t in attr(b, "p", []):
        out.append(f'{I}  <p>{rich(t)}</p>')
    if b.get("pairs"):
        out.append(_pairs(b["pairs"]))
    for t in attr(b, "tables", []):
        out.append(_gtable(t))
    if b.get("chain"):
        chain = '<span class="arrow">→</span>'.join(
            f'<span class="chip">{E(c)}</span>' for c in b["chain"])
        out.append(f'{I}  <div class="chain">{chain}</div>')
    for t in attr(b, "after", []):
        out.append(f'{I}  <p>{rich(t)}</p>')
    if b.get("note"):
        out.append(f'{I}  <div class="gram-note">{rich(b["note"])}</div>')
    out.append(f'{I}</div>')
    return "\n".join(out)


def b_gram(b):
    return _box(b, "gram", "gram-title", "")


def b_culture(b):
    return _box(b, "culture", "culture-title", "ЭТО ИНТЕРЕСНО · Bilib qo‘ying")


def b_advice(b):
    return _box(b, "advice", "advice-title", "USTOZDAN MASLAHAT")


def b_pron(b):
    out = [f'{I}<div class="pron">']
    out.append(f'{I}  <div class="pron-title">{E(attr(b, "title", "ТАЛАФФУЗ"))}</div>')
    for t in attr(b, "p", []):
        out.append(f'{I}  <p>{rich(t)}</p>')
    for r in attr(b, "rows", []):
        out.append(f'{I}  <div class="pron-row">'
                   f'<span class="pron-ru">{E(r[0])}</span>'
                   f'<span class="pron-say">{E(r[1])}</span>'
                   f'<span class="pron-why">{rich(r[2])}</span></div>')
    out.append(f'{I}</div>')
    return "\n".join(out)


# o'zbek alifbosidagi rus harflari — mashq bandlari uchun
LETTERS = list("абвгдежзиклмнопрст")


def b_ex(b):
    out = [f'{I}<div class="ex">']
    hint = f' <span class="hint">{E(b["hint"])}</span>' if b.get("hint") else ""
    out.append(f'{I}  <div class="ex-head">'
               f'<span class="ex-n">{b["n"]}</span>'
               f'<span class="ex-task">{rich(b["task"])}{hint}</span></div>')

    if b.get("model"):
        lines = "".join(f'<span class="m-line"><span class="dash">—</span>{rich(m)}</span>'
                        for m in b["model"])
        out.append(f'{I}  <div class="model">{lines}</div>')

    if b.get("cards"):
        out.append(b_cards({"items": b["cards"]}))

    if b.get("items"):
        out.append(f'{I}  <div class="ex-items">')
        for k, it in enumerate(b["items"]):
            text = it[0] if isinstance(it, tuple) else it
            opts = (f'<span class="ex-opts">{E(it[1])}</span>'
                    if isinstance(it, tuple) and len(it) > 1 and it[1] else "")
            out.append(f'{I}    <div class="ex-item">'
                       f'<span class="ex-let">{LETTERS[k]})</span>'
                       f'<span class="ex-body">{rich(text)}</span>{opts}</div>')
        out.append(f'{I}  </div>')

    if b.get("match"):
        left, right = b["match"]
        lc = "\n".join(f'{I}      <div class="match-row">'
                       f'<span class="ex-let">{LETTERS[k]})</span>'
                       f'<span>{rich(t)}</span></div>' for k, t in enumerate(left))
        rc = "\n".join(f'{I}      <div class="match-row">'
                       f'<span class="ex-let">{k + 1}.</span>'
                       f'<span>{rich(t)}</span></div>' for k, t in enumerate(right))
        out.append(f'{I}  <div class="match">\n'
                   f'{I}    <div class="match-col">\n{lc}\n{I}    </div>\n'
                   f'{I}    <div class="match-col">\n{rc}\n{I}    </div>\n'
                   f'{I}  </div>')

    if b.get("choice"):
        opts = "".join(f'<span class="choice-opt">'
                       f'<span class="choice-box"></span>{rich(o)}</span>'
                       for o in b["choice"])
        out.append(f'{I}  <div class="choice">{opts}</div>')

    if b.get("rows"):
        cls = " tight" if b.get("tight") else ""
        rows = "\n".join(f'{I}    <div class="row"></div>' for _ in range(b["rows"]))
        out.append(f'{I}  <div class="write-rows{cls}">\n{rows}\n{I}  </div>')

    out.append(f'{I}</div>')
    return "\n".join(out)


def b_roleplay(b):
    cols = []
    for col in b["cols"]:
        steps = "\n".join(f'{I}    <div class="role-step">{rich(s)}</div>'
                          for s in col["steps"])
        cols.append(f'{I}  <div class="role-col">\n'
                    f'{I}    <div class="role-head">{E(col["head"])}</div>\n'
                    f'{steps}\n{I}  </div>')
    return f'{I}<div class="roleplay">\n' + "\n".join(cols) + f'\n{I}</div>'


def b_model(b):
    lines = "".join(f'<span class="m-line"><span class="dash">—</span>{rich(m)}</span>'
                    for m in b["lines"])
    return f'{I}<div class="model">{lines}</div>'


def b_write(b):
    cls = " tight" if b.get("tight") else ""
    rows = "\n".join(f'{I}  <div class="row"></div>' for _ in range(b["rows"]))
    return f'{I}<div class="write-rows{cls}">\n{rows}\n{I}</div>'


def b_read(b):
    """O'qish uchun matn — monolog, dialog emas (tirecha qo'yilmaydi)."""
    out = [f'{I}<div class="read">']
    for k, t in enumerate(b["items"]):
        n = f'<span class="read-n">{k + 1}.</span>' if b.get("numbered", True) else ""
        out.append(f'{I}  <div class="read-item">{n}<span>{rich(t)}</span></div>')
    out.append(f'{I}</div>')
    return "\n".join(out)


def b_cards(b):
    """Vizitka / hujjat ko'rinishidagi haqiqiy material."""
    out = [f'{I}<div class="cards">']
    for c in b["items"]:
        out.append(f'{I}  <div class="card">\n'
                   f'{I}    <div class="card-name">{rich(c[0]).replace(chr(10), "<br>")}</div>\n'
                   f'{I}    <div class="card-role">{rich(c[1])}</div>\n'
                   f'{I}    <div class="card-foot">{rich(c[2])}</div>\n'
                   f'{I}  </div>')
    out.append(f'{I}</div>')
    return "\n".join(out)


def b_keyphrases(b):
    """Darsning asosiy iboralari — tez qaraladigan ro'yxat."""
    title = attr(b, "title", "ЗАПОМНИТЕ · Yodda tuting")
    out = [f'{I}<div class="keyph">',
           f'{I}  <div class="keyph-title">{E(title)}</div>']
    if b.get("sub"):
        out.append(f'{I}  <div class="keyph-sub">{rich(b["sub"])}</div>')
    for ru, uz in b["rows"]:
        out.append(f'{I}  <div class="keyph-row">'
                   f'<span class="keyph-ru">{E(ru)}</span>'
                   f'<span class="keyph-uz">{E(uz)}</span></div>')
    out.append(f'{I}</div>')
    return "\n".join(out)


def b_selfcheck(b):
    title = attr(b, "title", "ПРОВЕРЬ СЕБЯ · O‘ZINGIZNI TEKSHIRING")
    sub = attr(b, "sub", "Quyidagilarni bemalol qila olsangiz, keyingi darsga o‘ting.")
    rows = "\n".join(f'{I}  <div class="selfcheck-row">'
                     f'<span class="selfcheck-box"></span>'
                     f'<span class="t">{rich(t)}</span></div>' for t in b["items"])
    return (f'{I}<div class="selfcheck">\n'
            f'{I}  <div class="selfcheck-title">{E(title)}</div>\n'
            f'{I}  <div class="selfcheck-sub">{E(sub)}</div>\n'
            f'{rows}\n'
            f'{I}</div>')


BUILDERS = {
    "title": b_title,
    "cando": b_cando,
    "sec": b_sec,
    "text": b_text,
    "dialog": b_dialog,
    "vocab": b_vocab,
    "gram": b_gram,
    "pron": b_pron,
    "ex": b_ex,
    "roleplay": b_roleplay,
    "model": b_model,
    "write": b_write,
    "culture": b_culture,
    "advice": b_advice,
    "read": b_read,
    "cards": b_cards,
    "keyphrases": b_keyphrases,
    "selfcheck": b_selfcheck,
}


# ----------------------------------------------------------- sahifalash

def lesson_pages(L):
    """BLOCKS ro'yxatini "PAGE" belgisi bo'yicha sahifalarga bo'ladi."""
    pages, cur = [], []
    for blk in L["blocks"]:
        if blk == "PAGE":
            pages.append(cur)
            cur = []
            continue
        kind = blk["type"]
        if kind not in BUILDERS:
            raise KeyError(f'{L["number"]}-dars: "{kind}" nomli blok turi yo‘q')
        cur.append(BUILDERS[kind](blk))
    if cur:
        pages.append(cur)
    return pages


def check_exercise_numbers(L):
    """Mashqlar 1 dan boshlab uzluksiz raqamlanganini tekshiradi."""
    nums = [b["n"] for b in L["blocks"]
            if isinstance(b, dict) and b["type"] == "ex"]
    want = list(range(1, len(nums) + 1))
    if nums != want:
        raise AssertionError(
            f'{L["number"]}-dars: mashq raqamlari {nums}, kutilgani {want}')


def render_page(pid, parts, running):
    side = "right" if pid % 2 else "left"
    facet = RIGHT_FACET if side == "right" else LEFT_FACET
    head = f'{I}<div class="running-head">{E(running)}</div>\n\n' if running else ""
    body = "\n\n".join(parts)
    return (f'      <section class="page {side}-page" id="page-{pid}">\n'
            f'{head}{body}\n\n'
            f'{I}<div class="page-number">{pid:02d}</div>\n\n'
            f'{facet}\n'
            f'      </section>')


def build_lessons(lessons):
    pid = FIRST_LESSON_PAGE
    rendered, starts, nav = [], {}, []

    for L in lessons:
        check_exercise_numbers(L)
        starts[L["number"]] = pid
        pages = lesson_pages(L)
        for k, parts in enumerate(pages):
            # birinchi sahifada katta sarlavha bor — kolontitul ortiqcha
            running = "" if k == 0 else f'УРОК {L["number"]} · {L["running"]}'
            rendered.append(render_page(pid, parts, running))
            nav.append((pid, f'Урок {L["number"]} — {L["running"]}'))
            pid += 1

    blocks, i = [], 0
    while i < len(rendered):
        pair = rendered[i:i + 2]
        n = FIRST_LESSON_PAGE + i
        label = f"PAGE {n}" + (f" & PAGE {n + 1}" if len(pair) == 2 else "")
        body = "\n\n".join(pair)
        blocks.append(
            "    <!-- ==========================================================\n"
            f"         {label}\n"
            "         ========================================================== -->\n"
            f'    <div class="spread-wrapper">\n{body}\n    </div>\n')
        i += 2

    return "\n\n".join(blocks), starts, nav, pid


# ------------------------------------------------------------ index.html

def splice(text, mark, payload):
    """START va END belgilari orasidagi hamma narsani payload bilan almashtiradi.

    Belgilar oldidagi bo'shliq qanday bo'lsa ham ishlaydi.
    """
    pat = re.compile(rf"(?s)([ \t]*<!-- {mark}:START -->\n).*?([ \t]*<!-- {mark}:END -->)")
    m = pat.search(text)
    if not m:
        raise ValueError(f"template.html ichida <!-- {mark}:START/END --> belgisi yo‘q")
    return text[:m.start()] + m.group(1) + payload + m.group(2) + text[m.end():]


def update_toc(text, starts):
    """Reja ro'yxatidagi darslarga haqiqiy sahifa raqamini qo'yadi."""
    def repl(m):
        head, num = m.group(1), int(m.group(2))
        page = starts.get(num)
        if page:
            return (f'{head}<span class="toc-dots"></span>'
                    f'<span class="toc-row-p">{page}</span></div>')
        return (f'{head}<span class="toc-dots"></span>'
                f'<span class="toc-row-p">—</span></div>')

    text = re.sub(r'<span class="toc-dots"></span><span class="toc-row-p">[^<]*</span>',
                  "", text)
    return re.sub(
        r'(<div class="toc-row(?: pending)?"><span class="toc-row-n">(\d+)\.</span>.*?)</div>',
        repl, text)


def update_nav(text, nav, total):
    rows = ["01. Muqova", "02. Reja (1–4-modul)", "03. Reja (5–8-modul)",
            "04. Muallifdan", "05. Kitobdan qanday foydalanish",
            "06. Rus alifbosi", "07. Rus alifbosi — uchta guruh"]
    rows += [f"{p:02d}. {name}" for p, name in nav]
    rows.append(f"{total:02d}. Orqa muqova")
    opts = "".join(f'    <option value="page-{i + 1}">{E(r)}</option>\n'
                   for i, r in enumerate(rows))
    pat = re.compile(r'(?s)(<select id="pageSelect"[^>]*>\n).*?([ \t]*</select>)')
    if not pat.search(text):
        raise ValueError("template.html ichida <select id=\"pageSelect\"> topilmadi")
    text = pat.sub(lambda m: m.group(1) + opts + m.group(2), text, count=1)
    text = re.sub(r'A4 · \d+ sahifa', f'A4 · {total} sahifa', text)
    return text


def set_back_cover(text, page_no):
    text = re.sub(r'PAGE \d+: ORQA MUQOVA', f'PAGE {page_no}: ORQA MUQOVA', text)
    return re.sub(r'(<section class="page back-cover-page[^"]*" id=")page-\d+(")',
                  rf'\1page-{page_no}\2', text)


def main():
    lessons = load_lessons()
    lessons_html, starts, nav, next_page = build_lessons(lessons)
    total = next_page  # orqa muqova shu raqamni oladi

    p = ROOT / "index.html"
    s = (ROOT / "template.html").read_text(encoding="utf-8")
    s = splice(s, "LESSONS", lessons_html)
    s = set_back_cover(s, total)
    s = update_toc(s, starts)
    s = update_nav(s, nav, total)
    p.write_text(s, encoding="utf-8")

    print(f"{len(lessons)} ta dars yig‘ildi, jami {total} sahifa")
    for L in lessons:
        n = len(lesson_pages(L))
        exs = sum(1 for b in L["blocks"] if isinstance(b, dict) and b["type"] == "ex")
        words = sum(len(b["words"]) for b in L["blocks"]
                    if isinstance(b, dict) and b["type"] == "vocab")
        print(f"  Урок {L['number']}: {starts[L['number']]}-sahifadan, "
              f"{n} sahifa · {words} so‘z · {exs} mashq")
    if total % 4:
        need = 4 - total % 4
        print(f"\nESLATMA: bosmaxona uchun sahifa soni 4 ga karrali bo‘lishi kerak "
              f"(hozir {total}, yana {need} ta kerak).")


if __name__ == "__main__":
    sys.exit(main())
