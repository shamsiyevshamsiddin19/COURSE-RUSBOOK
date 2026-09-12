"""1-dars — Я и русский язык."""

LESSON = {
    "number": 1,
    "title_ru": "Я И РУССКИЙ ЯЗЫК",
    "subtitle_ru": "«Я рассказываю о себе»",
    "subtitle_uz": "Men o‘zim haqimda gapiraman",
    "running": "Я И РУССКИЙ ЯЗЫК",

    "goal_intro": "Ushbu darsdan so‘ng o‘quvchi rus tilida o‘zi haqida oddiy va to‘liq ma’lumot bera oladi.",
    "goals": [],

    "phrases": [],
    "dialog": [],
    "dialog_note": "",

    # (ruscha savol, o'zbekcha tarjima, javob boshlanmasi, quyruq)
    "questions": [
        ("Как тебя зовут?", "Ismingiz nima?", "Мой ответ:", None),
        ("Сколько тебе лет?", "Yoshingiz nechida?", "Мне", "лет."),
        ("Откуда ты?", "Qayerdansiz?", "Я из", None),
        ("Где ты живёшь?", "Qayerda yashaysiz?", "Я живу в", None),
        ("В каком городе ты живёшь?", "Qaysi shaharda yashaysiz?", "Я живу в городе", None),
        ("Где ты работаешь?", "Qayerda ishlaysiz?", "Я работаю", None),
        ("Кем ты работаешь?", "Kim bo‘lib ishlaysiz?", "Я работаю", None),
        ("Где ты учишься?", "Qayerda o‘qiysiz?", "Я учусь в", None),
        ("На каком языке ты говоришь?", "Qaysi tilda gaplashasiz?", "Я говорю на", None),
        ("Ты знаешь русский язык?", "Rus tilini bilasizmi?", "Да, я", None),
        ("Почему ты изучаешь русский язык?", "Nima uchun rus tilini o‘rganyapsiz?",
         "Я изучаю русский язык, потому что", None),
        ("Тебе нравится русский язык?", "Rus tili sizga yoqadimi?", "Да, мне", None),
        ("Как давно ты изучаешь русский язык?", "Rus tilini qancha vaqtdan beri o‘rganyapsiz?",
         "Я изучаю русский язык", None),
        ("Что ты любишь делать?", "Nima qilishni yaxshi ko‘rasiz?", "Я люблю", None),
        ("Какое у тебя хобби?", "Hobbiyingiz nima?", "Моё хобби —", None),
        ("Ты любишь читать?", "Kitob o‘qishni yaxshi ko‘rasizmi?", "Да, я люблю", None),
        ("Ты любишь смотреть фильмы?", "Kino ko‘rishni yaxshi ko‘rasizmi?", "Да, я", None),
        ("Какую музыку ты любишь?", "Qanday musiqa yoqadi?", "Я люблю", None),
        ("Какой твой любимый цвет?", "Sevimli rangingiz qaysi?", "Мой любимый цвет —", None),
        ("Какое твоё любимое блюдо?", "Sevimli taomingiz nima?", "Моё любимое блюдо —", None),
        ("Ты любишь путешествовать?", "Sayohat qilishni yaxshi ko‘rasizmi?", "Да, я люблю", None),
        ("Куда ты хочешь поехать?", "Qayerga borishni xohlaysiz?", "Я хочу поехать", None),
        ("Что ты хочешь выучить на русском языке?", "Rus tilida nimani o‘rganishni xohlaysiz?",
         "Я хочу научиться", None),
        ("Какая у тебя мечта?", "Orzuingiz nima?", "Моя мечта —", None),
        ("Каким человеком ты хочешь стать?", "Qanday inson bo‘lishni xohlaysiz?", "Я хочу стать", None),
    ],

    "task_title": "МОЯ РЕЧЬ",
    "task_intro": "Endi yuqoridagi savollarga bergan javoblaringizdan foydalanib, "
                  "o‘zingiz haqingizda rus tilida 5–7 ta gap yozing.",
    "task_first_line": "Меня зовут",
    "task_blank_rows": 12,
    "task_dialog": [],

    "advice": [
        "Javoblarni yodlab olishga emas, tushunib gapirishga harakat qiling. "
        "Har bir savolga avval yozma javob bering, keyin javobingizni ovoz chiqarib 2–3 marta ayting.",
        "Shunda rus tilida gapirish asta-sekin osonlasha boshlaydi.",
    ],
    "advice_chain": [],

    "page_plan": [
        ["header", "goal", "questions:7"],
        ["questions:10"],
        ["questions:8"],
        ["task", "advice"],
    ],
}
