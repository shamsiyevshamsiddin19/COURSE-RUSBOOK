#!/usr/bin/env python3
"""Sahifalarni tekshiradi: matn sahifadan chiqib ketmaganini aniqlaydi.

    python3 check_pages.py

Chrome'ni headless rejimda ishga tushirib, har bir .page ichidagi
oxirgi blok sahifa chegarasidan qanchaga oshib ketganini o'lchaydi.

Nega kerak: shrift kichraytirilmaydi va "(davomi)" yozilmaydi — matn
sig'masa, lessonNN.py ichiga yangi "PAGE" qo'yiladi. Buning uchun
avval qayerda va qanchaga oshib ketganini aniq bilish kerak.

Chiqish kodi: hammasi joyida bo'lsa 0, oshib ketgan sahifa bo'lsa 1.
"""
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile

ROOT = pathlib.Path(__file__).parent

MEASURE = r"""
<script>
window.addEventListener('load', function () {
  var out = [];
  document.querySelectorAll('.page').forEach(function (page) {
    var pr = page.getBoundingClientRect();
    var cs = getComputedStyle(page);
    var padBottom = parseFloat(cs.paddingBottom);
    var limit = pr.bottom - padBottom;

    var worst = 0, tail = 0, kids = [];
    page.querySelectorAll(':scope > *').forEach(function (el) {
      if (el.classList.contains('page-number')) return;
      if (el.classList.contains('bottom-facet')) return;
      if (el.classList.contains('running-head')) return;
      if (el.classList.contains('cover-rule-field')) return;
      var r = el.getBoundingClientRect();
      if (r.height === 0) return;
      worst = Math.max(worst, r.bottom - limit);
      tail = Math.max(tail, r.bottom);
      var name = el.className.split(' ')[0] || el.tagName.toLowerCase();
      kids.push(name + ':' + r.height.toFixed(0));
    });
    var free = limit - tail;
    out.push(page.id + '|' + worst.toFixed(1) + '|' + free.toFixed(1)
             + '|' + kids.join(','));
  });
  document.title = 'MEASURE:' + out.join(';');
});
</script>
"""


def find_chrome():
    for b in ("google-chrome", "google-chrome-stable", "chromium", "chromium-browser"):
        if shutil.which(b):
            return b
    sys.exit("Chrome/Chromium topilmadi.")


def px_to_mm(px):
    return px / 96.0 * 25.4


def main():
    src = ROOT / "index.html"
    if not src.exists():
        sys.exit("index.html yo‘q. Avval: python3 build.py")

    html = src.read_text(encoding="utf-8").replace("</head>", MEASURE + "</head>")
    tmp = ROOT / ".check-build.html"
    tmp.write_text(html, encoding="utf-8")

    try:
        with tempfile.TemporaryDirectory() as profile:
            dom = subprocess.run(
                [find_chrome(), "--headless", "--disable-gpu", "--no-sandbox",
                 f"--user-data-dir={profile}",
                 "--virtual-time-budget=15000", "--dump-dom", f"file://{tmp}"],
                capture_output=True, text=True, timeout=120).stdout
    finally:
        tmp.unlink(missing_ok=True)

    m = re.search(r"<title>MEASURE:(.*?)</title>", dom, re.S)
    if not m:
        sys.exit("O‘lchash natijasi olinmadi — Chrome sahifani yuklay olmadi.")

    bad, tight, rows = [], [], []
    for rec in m.group(1).split(";"):
        if not rec:
            continue
        pid, over, free, kids = rec.split("|")
        over, free = float(over), float(free)
        rows.append((pid, over, free, kids))
        if over > 1:
            bad.append((pid, over))
        elif free > 190:  # ~50 mm dan ko'p bo'sh joy
            tight.append((pid, free))

    print(f"{len(rows)} ta sahifa tekshirildi\n")

    show_blocks = "-b" in sys.argv or "--blocks" in sys.argv
    print("  sahifa      holat")
    for pid, over, free, kids in rows:
        if over > 1:
            state = f"OSHDI  +{px_to_mm(over):5.1f} mm"
        else:
            state = f"bo‘sh  -{px_to_mm(free):5.1f} mm"
        print(f"  {pid:10}  {state}")
        if show_blocks and kids:
            for k in kids.split(","):
                name, h = k.rsplit(":", 1)
                print(f"      {name:16} {px_to_mm(float(h)):6.1f} mm")
    print()

    if bad:
        print("SAHIFADAN CHIQIB KETGAN:")
        for pid, over in bad:
            print(f"  {pid:10} {px_to_mm(over):6.1f} mm oshib ketdi "
                  f"— lessonNN.py ga yangi \"PAGE\" qo‘ying")
        print()

    if tight:
        print("JUDA BO‘SH (ixtiyoriy — blok ko‘chirish mumkin):")
        for pid, free in tight:
            print(f"  {pid:10} {px_to_mm(free):6.1f} mm bo‘sh qoldi")
        print()

    if not bad:
        print("Hamma sahifa joyiga sig‘di.")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
