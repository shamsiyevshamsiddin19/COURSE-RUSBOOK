#!/usr/bin/env python3
"""Kitobni yig'adi: darslarni lessons/ dan o'qib, index.html ni yangilaydi.

    python3 build.py

Har bir dars bir xil qolipda quriladi:
    sarlavha -> DARS MAQSADI -> ENG KERAKLI IBORALAR -> DIALOG
    -> SAVOL-JAVOB -> AMALIY VAZIFA -> USTOZDAN MASLAHAT
Bo'sh bo'limlar tashlab ketiladi, lekin tartib hech qachon o'zgarmaydi.

Sahifa raqamlari, yuqoridagi kolontitul, reja va navigatsiya ro'yxati
shu yerdan avtomatik hisoblanadi.
"""
import html
import importlib.util
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).parent
E = html.escape

# 1-sahifa muqova, 2-4 reja, 5 muallifdan; darslar 6-sahifadan boshlanadi
FIRST_LESSON_PAGE = 6

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


def load_lessons():
    out = []
    for path in sorted((ROOT / "lessons").glob("lesson*.py")):
        spec = importlib.util.spec_from_file_location(path.stem, path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        out.append(mod.LESSON)
    return out


# ---------------------------------------------------------------- bo'limlar

def sec_header(L):
    parts = [f'        <div class="lesson-eyebrow">УРОК {L["number"]}</div>',
             f'        <h1 class="page-title">{E(L["title_ru"])}</h1>']
    if L.get("subtitle_ru"):
        parts.append(f'        <div class="lesson-sub-ru">{E(L["subtitle_ru"])}</div>')
    if L.get("subtitle_uz"):
        parts.append(f'        <div class="lesson-sub-uz">{E(L["subtitle_uz"])}</div>')
    return "\n".join(parts)


def sec_goal(L):
    rows = [f'          <div class="goal-text">{E(L["goal_intro"])}</div>']
    if L.get("goals"):
        items = "\n".join(f"            <li>{E(g)}</li>" for g in L["goals"])
        rows.append(f'          <ul class="goal-list">\n{items}\n          </ul>')
    body = "\n".join(rows)
    return ('        <div class="goal-box">\n'
            '          <div class="goal-title">DARS MAQSADI</div>\n'
            f'{body}\n'
            '        </div>')


def sec_phrases(L):
    if not L.get("phrases"):
        return None
    rows = "\n".join(
        f'          <div class="phrase-row"><div class="phrase-ru">{E(ru)}</div>'
        f'<div class="phrase-uz">{E(uz)}</div></div>' for ru, uz in L["phrases"])
    return ('        <div class="badge-tag">ENG KERAKLI IBORALAR</div>\n'
            f'        <div class="phrase-table">\n{rows}\n        </div>')


def sec_dialog(L):
    if not L.get("dialog"):
        return None
    lines = "\n".join(
        f'          <div class="dialog-line"><span class="dash">—</span>{E(t)}</div>'
        for t in L["dialog"])
    out = ('        <div class="badge-tag">DIALOG</div>\n'
           f'        <div class="dialog-box">\n{lines}\n        </div>')
    if L.get("dialog_note"):
        out += (f'\n        <p class="body-text-sm" style="margin:6px 0 10px;">'
                f'{E(L["dialog_note"])}</p>')
    return out


def q_html(n, q):
    ru, uz, stem, tail = q
    if tail:
        ans = (f'<span>{E(stem)}</span><span class="write-line short"></span>'
               f'<span>{E(tail)}</span>')
    elif stem:
        ans = f'<span>{E(stem)}</span><span class="write-line"></span>'
    else:
        ans = '<span class="write-line"></span>'
    uz_line = f'\n              <div class="q-uz">{E(uz)}</div>' if uz else ""
    return (f'          <div class="q-item">\n'
            f'            <div class="q-num">{n}</div>\n'
            f'            <div class="q-body">\n'
            f'              <div class="q-ru">{E(ru)}</div>{uz_line}\n'
            f'              <div class="q-answer">{ans}</div>\n'
            f'            </div>\n'
            f'          </div>')


def sec_task(L):
    if not (L.get("task_blank_rows") or L.get("task_dialog")):
        return None
    parts = [f'        <div class="badge-tag">{E(L["task_title"])}</div>']
    if L.get("task_intro"):
        parts.append(f'        <p class="body-text-sm" style="margin-bottom:4px;">{E(L["task_intro"])}</p>')
    if L.get("task_first_line"):
        parts.append(f'        <div class="q-answer" style="margin-top:10px;">'
                     f'<span>{E(L["task_first_line"])}</span><span class="write-line"></span></div>')
    if L.get("task_blank_rows"):
        rows = "\n".join('          <div class="write-line"></div>'
                         for _ in range(L["task_blank_rows"]))
        parts.append(f'        <div class="write-rows">\n{rows}\n        </div>')
    if L.get("task_dialog"):
        rows = []
        for text in L["task_dialog"]:
            label = f'<span>{E(text)}</span>' if text else ""
            rows.append('          <div class="q-answer task-line"><span class="dash">—</span>'
                        f'{label}<span class="write-line"></span></div>')
        parts.append('        <div class="task-dialog">\n' + "\n".join(rows) + '\n        </div>')
    return "\n".join(parts)


def sec_advice(L):
    if not L.get("advice"):
        return None
    parts = ['        <div class="advice-box">',
             '          <div class="advice-title">USTOZDAN MASLAHAT</div>']
    texts = list(L["advice"])
    parts.append(f'          <p class="body-text-sm">{E(texts[0])}</p>')
    if L.get("advice_chain"):
        chain = '<span class="arrow">→</span>'.join(
            f'<span class="chip">{E(c)}</span>' for c in L["advice_chain"])
        parts.append(f'          <div class="chain">{chain}</div>')
    for t in texts[1:]:
        parts.append(f'          <p class="body-text-sm">{E(t)}</p>')
    parts.append('        </div>')
    return "\n".join(parts)


# ---------------------------------------------------------------- sahifalash

def lesson_pages(L):
    """page_plan bo'yicha darsni sahifalarga bo'ladi.

    page_plan — har bir sahifa uchun bo'limlar ro'yxati, masalan:
        [["header", "goal", "phrases"],
         ["dialog", "questions:7"],
         ["questions:13"],
         ["questions:5", "task", "advice"]]
    """
    builders = {
        "header": sec_header,
        "goal": sec_goal,
        "phrases": sec_phrases,
        "dialog": sec_dialog,
        "task": sec_task,
        "advice": sec_advice,
    }
    qs = L["questions"]
    plan = L["page_plan"]

    planned = sum(int(item.split(":")[1]) for page in plan for item in page
                  if item.startswith("questions:"))
    assert planned == len(qs), \
        f"{L['number']}-dars: rejada {planned} ta savol, aslida {len(qs)} ta"

    pages, idx, badge_done = [], 0, False
    for page in plan:
        block = []
        for item in page:
            if item.startswith("questions:"):
                n = int(item.split(":")[1])
                if not badge_done:
                    block.append('        <div class="badge-tag">SAVOL-JAVOB</div>')
                    badge_done = True
                block += [q_html(i + 1, qs[i]) for i in range(idx, idx + n)]
                idx += n
            else:
                sec = builders[item](L)
                if sec:
                    block.append(sec)
        pages.append(block)
    return pages


def render_page(pid, num, parts, running):
    side = "right" if pid % 2 else "left"
    facet = RIGHT_FACET if side == "right" else LEFT_FACET
    head = f'        <div class="running-head">{E(running)}</div>\n\n' if running else ""
    body = "\n\n".join(parts)
    return (f'      <section class="page {side}-page" id="page-{pid}">\n'
            f'{head}{body}\n\n'
            f'        <div class="page-number">{num:02d}</div>\n\n'
            f'{facet}\n'
            f'      </section>')


def build_lessons(lessons):
    """HTML va har bir dars boshlanadigan sahifa raqamini qaytaradi."""
    pid = FIRST_LESSON_PAGE
    rendered, starts = [], {}

    for L in lessons:
        starts[L["number"]] = pid
        for k, parts in enumerate(lesson_pages(L)):
            # birinchi sahifada katta sarlavha bor — kolontitul kerak emas
            running = "" if k == 0 else f'УРОК {L["number"]} · {L["running"]}'
            rendered.append(render_page(pid, pid, parts, running))
            pid += 1

    # sahifalarni ikkitadan yoyilmaga joylash
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

    return "\n\n".join(blocks), starts, pid


# ---------------------------------------------------------------- index.html

def splice(html_text, lessons_html):
    a = html_text.index("    <!-- LESSONS:START -->")
    b = html_text.index("    <!-- LESSONS:END -->")
    return (html_text[:a] + "    <!-- LESSONS:START -->\n"
            + lessons_html + "    <!-- LESSONS:END -->" + html_text[b + len("    <!-- LESSONS:END -->"):])


def set_back_cover(html_text, page_no):
    html_text = re.sub(r'         PAGE \d+: BACK COVER', f'         PAGE {page_no}: BACK COVER', html_text)
    return re.sub(r'(<section class="page page-cover left-page" id=")page-\d+(">)',
                  rf'\1page-{page_no}\2', html_text)


def update_reja(html_text, starts):
    """Reja ro'yxatidagi darslarga haqiqiy sahifa raqamini qo'yadi."""
    def repl(m):
        prefix, num = m.group(1), int(m.group(2))
        page = starts.get(num)
        tag = f'<span class="toc2-page">{page}</span>' if page else ""
        return f'{prefix}{tag}</div>'

    html_text = re.sub(r'<span class="toc2-page">\d+</span>', "", html_text)
    return re.sub(
        r'(<div class="toc2-lesson"><span class="l-n">Урок (\d+)\.</span>.*?)</div>',
        repl, html_text)


def update_nav(html_text, lessons, starts, total):
    rows = ["01. Front Cover", "02. Reja (1-3-modul)", "03. Reja (4-6-modul)",
            "04. Reja (7-8-modul)", "05. Muallifdan"]
    for L in lessons:
        first = starts[L["number"]]
        count = len(lesson_pages(L))
        for k in range(count):
            rows.append(f'{first + k:02d}. Урок {L["number"]} — {L["running"].capitalize()}')
    rows.append(f"{total:02d}. Back Cover")

    new = "".join(f'        <option value="page-{i + 1}">{r}</option>\n'
                  for i, r in enumerate(rows))
    old = re.search(r'        <option value="page-1">.*?</option>\n(?:        <option.*?</option>\n)+',
                    html_text, re.S).group(0)
    html_text = html_text.replace(old, new)
    html_text = re.sub(r'A5 Format \(\d+ Pages\)', f'A5 Format ({total} Pages)', html_text)
    return re.sub(r'Kurs Kitobi — \d+ Sahifa', f'Kurs Kitobi — {total} Sahifa', html_text)


def main():
    lessons = load_lessons()
    lessons_html, starts, next_page = build_lessons(lessons)
    total = next_page  # orqa muqova

    p = ROOT / "index.html"
    s = p.read_text(encoding="utf-8")
    s = splice(s, lessons_html)
    s = set_back_cover(s, total)
    s = update_reja(s, starts)
    s = update_nav(s, lessons, starts, total)
    p.write_text(s, encoding="utf-8")

    print(f"{len(lessons)} ta dars yig‘ildi, jami {total} sahifa")
    for L in lessons:
        print(f"  Урок {L['number']}: {starts[L['number']]}-sahifadan, "
              f"{len(lesson_pages(L))} sahifa")
    if total % 4:
        print(f"\nESLATMA: chop etish uchun sahifa soni 4 ga karrali bo‘lishi kerak "
              f"(hozir {total}, {4 - total % 4} ta yetishmaydi).")


if __name__ == "__main__":
    sys.exit(main())
