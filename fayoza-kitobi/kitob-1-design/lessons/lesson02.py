"""2-dars — Знакомство.

Savollarning o'zbekcha tarjimasi: 1-10, 14, 15 — muallifning o'z so'zlari
(1-darsdan va shu darsning ibora ro'yxatidan olingan). Qolganlari tarjima
qilingan, muallif tekshirishi kerak.
"""

LESSON = {
    "number": 2,
    "title_ru": "ЗНАКОМСТВО",
    "subtitle_ru": "",
    "subtitle_uz": "Tanishish va tanishtirish",
    "running": "ЗНАКОМСТВО",

    "goal_intro": "Bu darsdan so‘ng siz:",
    "goals": [
        "o‘zingizni tanishtira olasiz;",
        "boshqa insonning ismini, yoshini, qayerdanligini so‘ray olasiz;",
        "suhbatni boshlab, davom ettira olasiz;",
        "yangi tanishgan inson bilan oddiy dialog qura olasiz.",
    ],

    "phrases": [
        ("Здравствуйте!", "Assalomu alaykum! / Salom!"),
        ("Привет!", "Salom!"),
        ("Как вас зовут?", "Ismingiz nima?"),
        ("Как тебя зовут?", "Isming nima?"),
        ("Меня зовут Фаёза.", "Mening ismim Fayoza."),
        ("Очень приятно!", "Tanishganimdan xursandman!"),
        ("Мне тоже приятно.", "Men ham xursandman."),
        ("Откуда вы?", "Qayerdansiz?"),
        ("Откуда ты?", "Qayerdansan?"),
        ("Я из Узбекистана.", "Men O‘zbekistondanman."),
        ("Где вы живёте?", "Qayerda yashaysiz?"),
        ("Я живу в Ташкенте.", "Men Toshkentda yashayman."),
        ("До свидания!", "Xayr!"),
        ("До встречи!", "Ko‘rishguncha!"),
    ],

    "dialog": [
        "Здравствуйте! Как вас зовут?",
        "Здравствуйте! Меня зовут Малика. А вас?",
        "Меня зовут Фаёза. Очень приятно!",
        "Мне тоже приятно!",
        "Откуда вы?",
        "Я из Узбекистана. А вы?",
        "Я тоже из Узбекистана.",
        "Где вы живёте?",
        "Я живу в Ташкенте.",
    ],
    "dialog_note": "Endi dialogni o‘zingizning ma’lumotlaringiz bilan qayta yozing.",

    "questions": [
        ("Как тебя зовут?", "Isming nima?", "Мой ответ:", None),
        ("Как вас зовут?", "Ismingiz nima?", "Мой ответ:", None),
        ("Сколько тебе лет?", "Yoshingiz nechida?", "Мне", "лет."),
        ("Откуда ты?", "Qayerdansan?", "Я из", None),
        ("Где ты живёшь?", "Qayerda yashaysiz?", "Я живу в", None),
        ("В каком городе ты живёшь?", "Qaysi shaharda yashaysiz?", "Я живу в", None),
        ("Где ты учишься?", "Qayerda o‘qiysiz?", "Я учусь", None),
        ("Где ты работаешь?", "Qayerda ishlaysiz?", "Я работаю", None),
        ("Кем ты работаешь?", "Kim bo‘lib ishlaysiz?", "Я работаю", None),
        ("На каком языке ты говоришь?", "Qaysi tilda gaplashasiz?", "Я говорю на", None),
        ("Ты из Узбекистана?", "O‘zbekistondanmisiz?", "Да,", None),
        ("Ты говоришь по-русски?", "Rus tilida gaplashasizmi?", "Да, я", None),
        ("Ты изучаешь русский язык?", "Rus tilini o‘rganyapsizmi?", "Да, я", None),
        ("Как давно ты изучаешь русский язык?", "Rus tilini qancha vaqtdan beri o‘rganyapsiz?",
         "Я изучаю русский язык", None),
        ("Тебе нравится русский язык?", "Rus tili sizga yoqadimi?", "Да,", None),
        ("Ты студент / студентка?", "Talabamisiz?", "Да, я", None),
        ("Ты работаешь или учишься?", "Ishlaysizmi yoki o‘qiysizmi?", "Я", None),
        ("Ты живёшь один / одна?", "Yolg‘iz yashaysizmi?", "Я", None),
        ("У тебя есть друзья?", "Do‘stlaringiz bormi?", "Да, у меня", None),
        ("Ты любишь знакомиться с новыми людьми?", "Yangi insonlar bilan tanishishni yaxshi ko‘rasizmi?",
         "Да, я", None),
        ("Что ты обычно говоришь при знакомстве?", "Tanishganda odatda nima deysiz?", "Я говорю:", None),
        ("Что можно сказать после знакомства?", "Tanishgandan keyin nima deyish mumkin?", "", None),
        ("Как попрощаться с новым знакомым?", "Yangi tanishingiz bilan qanday xayrlashasiz?", "", None),
        ("Как спросить имя человека?", "Insonning ismini qanday so‘raysiz?", "", None),
        ("Как спросить, откуда человек?", "Insonning qayerdanligini qanday so‘raysiz?", "", None),
    ],

    "task_title": "AMALIY VAZIFA",
    "task_intro": "Tasavvur qiling: siz yangi inson bilan birinchi marta uchrashdingiz. "
                  "Rus tilida kichik dialog tuzing.",
    "task_first_line": "",
    "task_blank_rows": 0,
    # dialog skeleti: matn bo'lsa yoziladi, bo'sh bo'lsa faqat chiziq
    "task_dialog": ["Здравствуйте!", "", "", "", "", "Очень приятно!"],

    "advice": [
        "Tanishish paytida eng muhimi — mukammal gapirish emas. Oddiy gaplardan boshlang:",
        "Shu 5 ta iborani yaxshi o‘zlashtirsangiz, rus tilida suhbatni boshlash ancha osonlashadi.",
    ],
    "advice_chain": ["Здравствуйте!", "Как вас зовут?", "Откуда вы?", "Где вы живёте?", "Очень приятно!"],

    "page_plan": [
        ["header", "goal", "phrases"],
        ["dialog", "questions:7"],
        ["questions:13"],
        ["questions:5", "task", "advice"],
    ],
}
