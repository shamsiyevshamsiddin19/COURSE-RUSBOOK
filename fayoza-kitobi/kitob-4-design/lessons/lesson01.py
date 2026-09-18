# -*- coding: utf-8 -*-
"""1-dars — Я и русский язык.

Grammatik o'zak:  rus tilida hozirgi zamonda «bo'lmoq» fe'li yo'q;
                  меня зовут; shaxs olmoshlari; ты/вы; ohang bilan savol.
Talaffuz o'zagi:  «ы» tovushi, urg'usiz «о» -> «а», «щ», yumshatuvchi «ь».

Sahifa tartibi ataylab shunday: DIALOG -> SO'ZLAR -> TALAFFUZ ->
GRAMMATIKA -> MASHQLAR -> NUTQ -> O'QISH -> YAKUN. Ya'ni avval
eshitadi va ko'radi, keyin tushunadi, oxirida o'zi qo'llaydi.
"""

LESSON = {
    "number": 1,
    "running": "Я и русский язык",
    "blocks": [

        # ------------------------------------------------ 1-sahifa
        {"type": "title",
         "number": 1,
         "ru": "Я И РУССКИЙ ЯЗЫК",
         "uz": "Men va rus tili — o‘zingiz haqingizda gapirish"},

        {"type": "cando", "items": [
            "Salomlashib, o‘z ismingizni ayta olasiz va suhbatdoshingizning ismini so‘raysiz",
            "Qayerdan ekaningizni va qayerda yashashingizni ayta olasiz",
            "Kimligingizni ayta olasiz: talaba, o‘qituvchi, shifokor",
            "Nega rus tilini o‘rganayotganingizni tushuntira olasiz",
            "«sen» va «siz» ni qachon ishlatishni bilasiz",
        ]},

        {"type": "sec", "ru": "ДИАЛОГ", "uz": "Suhbat"},

        {"type": "text", "class": "body-text-sm", "p": [
            "Avval faqat ruscha qismini o‘qing — pastdagi tarjimaga qaramang. "
            "Keyin ovoz chiqarib, rollarga bo‘lib o‘qing.",
        ]},

        {"type": "dialog", "n": 1,
         "scene": "Til markazida. Fayoza yangi o‘quvchi bilan tanishmoqda.",
         "lines": [
             ("Фаёза:", "Здра́вствуйте!", "Assalomu alaykum!"),
             ("Ша́хло:", "Здра́вствуйте!", "Assalomu alaykum!"),
             ("Фаёза:", "Меня́ зову́т Фаёза. Я преподава́тель. А как вас зову́т?",
              "Mening ismim Fayoza. Men o‘qituvchiman. Sizning ismingiz nima?"),
             ("Ша́хло:", "Меня́ зову́т Ша́хло.", "Mening ismim Shahlo."),
             ("Фаёза:", "О́чень прия́тно, Ша́хло!", "Tanishganimdan juda xursandman, Shahlo!"),
             ("Ша́хло:", "Мне то́же о́чень прия́тно.", "Men ham tanishganimdan xursandman."),
         ]},

        {"type": "dialog", "n": 2,
         "scene": "Guruhda. Shahlo yonidagi yigit bilan gaplashmoqda.",
         "lines": [
             ("Аза́мат:", "Извини́те, вы студе́нтка?", "Kechirasiz, siz talabamisiz?"),
             ("Ша́хло:", "Да, я студе́нтка. А вы?", "Ha, men talabaman. Sizchi?"),
             ("Аза́мат:", "Я то́же студе́нт. Меня́ зову́т Аза́мат.",
              "Men ham talabaman. Mening ismim Azamat."),
             ("Ша́хло:", "Ша́хло. Вы отку́да?", "Shahlo. Siz qayerdansiz?"),
             ("Аза́мат:", "Я из Самарка́нда. А вы?", "Men Samarqanddanman. Sizchi?"),
             ("Ша́хло:", "Я из Ташке́нта. Я живу́ в Чилонзо́ре.",
              "Men Toshkentdanman. Chilonzorda yashayman."),
         ]},

        "PAGE",

        # ------------------------------------------------ 2-sahifa
        {"type": "dialog", "n": 3,
         "scene": "Darsning oxirida. Fayoza sababini so‘raydi.",
         "lines": [
             ("Фаёза:", "Ша́хло, почему́ вы изуча́ете ру́сский язы́к?",
              "Shahlo, nega siz rus tilini o‘rganyapsiz?"),
             ("Ша́хло:", "Я рабо́таю в больни́це. Там мно́го ру́сских паци́ентов.",
              "Men kasalxonada ishlayman. U yerda rus bemorlar ko‘p."),
             ("Фаёза:", "Поня́тно. А вы, Аза́мат?", "Tushunarli. Sizchi, Azamat?"),
             ("Аза́мат:", "Я хочу́ рабо́тать в Росси́и. И ещё мне нра́вится ру́сский язы́к.",
              "Men Rossiyada ishlamoqchiman. Yana menga rus tili yoqadi."),
             ("Фаёза:", "Отли́чно! Тогда́ начина́ем.", "Ajoyib! Unda boshladik."),
         ]},

        {"type": "sec", "ru": "СЛОВА", "uz": "Yangi so‘zlar"},

        {"type": "vocab", "words": [
            ("здра́вствуйте", "zdra-stvuy-te", "assalomu alaykum", "hurmat bilan"),
            ("меня́ зову́т", "mi-nya za-vut", "mening ismim…"),
            ("преподава́тель", "pri-pa-da-va-tel", "o‘qituvchi"),
            ("а", "a", "-chi; esa"),
            ("как", "kak", "qanday, qanaqa"),
            ("вас", "vas", "sizni"),
            ("о́чень", "o-chin", "juda"),
            ("прия́тно", "pri-yat-na", "yoqimli"),
            ("о́чень прия́тно", "", "tanishganimdan xursandman"),
            ("мне", "mne", "menga"),
            ("то́же", "to-je", "ham"),
            ("извини́те", "iz-vi-ni-te", "kechirasiz"),
            ("вы", "vi", "siz"),
            ("студе́нт / студе́нтка", "stu-dent / stu-dent-ka", "talaba", "o‘g‘il / qiz"),
            ("да", "da", "ha"),
            ("нет", "net", "yo‘q"),
            ("я", "ya", "men"),
            ("ты", "ti", "sen"),
            ("отку́да", "at-ku-da", "qayerdan"),
            ("из", "iz", "-dan"),
            ("живу́ (жить)", "ji-vu", "yashayman (yashamoq)"),
        ]},

        "PAGE",

        # ------------------------------------------------ 3-sahifa
        {"type": "vocab", "words": [
            ("в", "v", "-da, -ga"),
            ("почему́", "pa-chi-mu", "nega"),
            ("изуча́ю (изуча́ть)", "i-zu-cha-yu", "o‘rganaman (o‘rganmoq)"),
            ("ру́сский язы́к", "rus-kiy ya-zik", "rus tili"),
            ("рабо́таю (рабо́тать)", "ra-bo-ta-yu", "ishlayman (ishlamoq)"),
            ("больни́ца", "bal-ni-tsa", "kasalxona"),
            ("там", "tam", "u yerda"),
            ("мно́го", "mno-ga", "ko‘p"),
            ("паци́ент", "pa-tsi-yent", "bemor"),
            ("поня́тно", "pa-nyat-na", "tushunarli"),
            ("хочу́ (хоте́ть)", "xa-chu", "xohlayman (xohlamoq)"),
            ("Росси́я", "Ra-si-ya", "Rossiya"),
            ("ещё", "yi-sho", "yana, hali"),
            ("нра́вится", "nra-vit-sa", "yoqadi"),
            ("отли́чно", "at-lich-na", "a’lo, ajoyib"),
            ("тогда́", "tag-da", "unda, u holda"),
            ("начина́ем", "na-chi-na-yem", "boshlaymiz"),
        ]},

        {"type": "sec", "ru": "ПРОИЗНОШЕНИЕ", "uz": "Talaffuz"},

        {"type": "pron",
         "title": "Uchta tovush — o‘zbek tilida umuman yo‘q",
         "p": ["Bu uchtasi eng ko‘p xato qilinadigan joy. Har birini ovoz chiqarib, "
               "oynaga qarab mashq qiling — og‘iz shakli muhim."],
         "rows": [
             ("ты · вы · мы · язы́к", "tı · vı · mı",
              "*«ы»* — «и» ham, «у» ham emas, ikkisining orasi. Lablarni yoymang, "
              "tilingizni orqaga torting. «ты» ni «ти» deb aytsangiz — boshqa so‘z bo‘ladi."),
             ("ещё · това́рищ · борщ", "yi-sho · ta-va-rish · borsh",
              "*«щ»* — uzun va yumshoq *«ш»*. Oddiy «ш» dan uzunroq va yumshoqroq "
              "talaffuz qilinadi."),
             ("учи́тель · день · сколько", "u-chi-tel · den · skolka",
              "*«ь»* tovush emas — u oldingi undoshni yumshatadi. Tilning o‘rtasini "
              "tanglayga yaqinlashtiring, xuddi undoshdan keyin juda qisqa «y» "
              "aytmoqchi bo‘lgandek."),
         ]},

        "PAGE",

        # ------------------------------------------------ 4-sahifa
        {"type": "pron",
         "title": "Ikkita qoida — yozilgani boshqa, o‘qilgani boshqa",
         "rows": [
             ("Москва́ · хорошо́ · молоко́", "Masqva · xarasho · malako",
              "Urg‘u tushmagan *«о»* har doim *«а»* kabi o‘qiladi. «хорошо́» da uchta «о» "
              "bor, lekin faqat oxirgisi urg‘uli — shuning uchun faqat u «о» bo‘lib qoladi."),
             ("здра́вствуйте · со́лнце", "zdra-stvuy-te · sontse",
              "Ba’zi undoshlar umuman o‘qilmaydi: «здравствуйте» dagi birinchi *«в»*, "
              "«солнце» dagi *«л»*. So‘zni bo‘g‘inlarga bo‘lib mashq qiling: "
              "здра / ствуй / те."),
         ],
         "after": ["*«ё»* harfi esa har doim urg‘uli — shuning uchun unga urg‘u belgisi "
                   "qo‘yilmaydi: *ещё*, *её*, *живёт*."]},

        {"type": "keyphrases",
         "sub": "Grammatikaga o‘tishdan oldin — shu yettita ibora bilan siz allaqachon "
                "oddiy tanishuvni o‘tkaza olasiz. Ularni yod oling.",
         "rows": [
             ("Здра́вствуйте!", "Assalomu alaykum!"),
             ("Меня́ зову́т…", "Mening ismim…"),
             ("Как вас зову́т?", "Ismingiz nima?"),
             ("О́чень прия́тно.", "Tanishganimdan xursandman."),
             ("Вы отку́да?", "Siz qayerdansiz?"),
             ("Я из Ташке́нта.", "Men Toshkentdanman."),
             ("Извини́те…", "Kechirasiz…"),
         ]},

        {"type": "sec", "ru": "ГРАММАТИКА", "uz": "Qoida"},

        {"type": "gram",
         "title": "1. Rus tilida «bo‘lmoq» fe’li ishlatilmaydi",
         "p": ["O‘zbek tilida biz «Men talaba*man*» deymiz — oxiridagi qo‘shimcha "
               "«bo‘lmoq» vazifasini bajaradi. Rus tilida hozirgi zamonda bunday "
               "qo‘shimcha ham, fe’l ham yo‘q. Gap shunchaki ikki so‘zdan iborat bo‘ladi:"],
         "pairs": [
             ("Я студе́нт.", "Men talabaman."),
             ("Она́ преподава́тель.", "U o‘qituvchi."),
             ("Он врач.", "U shifokor."),
             ("Я из Ташке́нта.", "Men Toshkentdanman."),
             ("Э́то Москва́.", "Bu Moskva."),
         ],
         "note": "Shuning uchun olmoshni (*я, ты, он*) tushirib qoldirib bo‘lmaydi. "
                 "O‘zbek tilida «Talabaman» deyish mumkin, rus tilida esa «Студе́нт» "
                 "deyish g‘alati eshitiladi — albatta *«Я студе́нт»* deyiladi."},

        "PAGE",

        # ------------------------------------------------ 5-sahifa
        {"type": "gram",
         "title": "2. Меня́ зову́т… — ismni aytish",
         "p": ["Ism aytishning tayyor qolipi. So‘zma-so‘z u «meni chaqirishadi» degani, "
               "shuning uchun ism oxirida keladi:"],
         "tables": [{
             "head": ["Qolip", "Ma’nosi", "Misol"],
             "rows": [
                 ("Меня́ зову́т…", "Mening ismim…", "Меня́ зову́т Ша́хло."),
                 ("Тебя́ зову́т…", "Sening isming…", "Тебя́ зову́т Аза́мат?"),
                 ("Вас зову́т…", "Sizning ismingiz…", "Как вас зову́т?"),
                 ("Его́ зову́т…", "Uning ismi… (erkak)", "Его́ зову́т Ди́лшод."),
                 ("Её зову́т…", "Uning ismi… (ayol)", "Её зову́т Ди́лноза."),
             ]}],
         "note": "«Как вас зову́т?» — «Ismingiz nima?». So‘zma-so‘z «Sizni qanday "
                 "chaqirishadi?». Javob ham shu qolipda beriladi."},

        {"type": "gram",
         "title": "3. Shaxs olmoshlari",
         "tables": [{
             "head": ["Birlik", "Ma’nosi", "Ko‘plik", "Ma’nosi"],
             "rows": [
                 ("я", "men", "мы", "biz"),
                 ("ты", "sen", "вы", "siz / sizlar"),
                 ("он", "u (erkak)", "они́", "ular"),
                 ("она́", "u (ayol)", "", ""),
                 ("оно́", "u (o‘rta rod)", "", ""),
             ]}],
         "note": "Rus tilida jonsiz narsalar ham «он» yoki «она́» bo‘ladi: "
                 "*кни́га — она́* (kitob), *стол — он* (stol). Buni 9-darsda "
                 "batafsil ko‘ramiz."},

        "PAGE",

        # ------------------------------------------------ 6-sahifa
        {"type": "gram",
         "title": "4. «ты» yoki «вы»? — eng muhim tanlov",
         "p": ["O‘zbek tilidagidek rus tilida ham ikki xil murojaat bor. Lekin chegara "
               "biroz boshqacha — buni xato qilish suhbatdoshni xafa qilishi mumkin."],
         "tables": [{
             "head": ["ты — sen", "вы — siz"],
             "rows": [
                 ("do‘stlar, tengdoshlar", "notanish odam"),
                 ("oila a’zolari", "o‘zingizdan katta yoshdagi kishi"),
                 ("bolalar", "o‘qituvchi, rahbar, mijoz"),
                 ("o‘zaro kelishilgan hamkasblar", "rasmiy vaziyat, ish yozishmasi"),
             ]}],
         "note": "Muhim farq: rus tilida *notanish tengdoshingizga ham* «вы» deyiladi. "
                 "Ko‘chada yoshi o‘zingizdek odamga «ты» desangiz — qo‘pol eshitiladi. "
                 "Avval «вы» bilan boshlang; kerak bo‘lsa, suhbatdosh o‘zi "
                 "«Дава́й на ты» (kel, «sen»ga o‘tamiz) deydi."},

        {"type": "gram",
         "title": "5. Savolni ohang bilan yasash",
         "p": ["Rus tilida oddiy savolni yasash uchun so‘z tartibini o‘zgartirish ham, "
               "hech qanday yordamchi so‘z qo‘shish ham shart emas. Faqat ohang o‘zgaradi:"],
         "pairs": [
             ("Вы студе́нт. ↘", "Siz talabasiz. _(ovoz pasayadi)_"),
             ("Вы студе́нт? ↗", "Siz talabamisiz? _(ovoz ko‘tariladi)_"),
             ("Она́ из Бухары́. ↘", "U Buxorodan. _(ovoz pasayadi)_"),
             ("Она́ из Бухары́? ↗", "U Buxorodanmi? _(ovoz ko‘tariladi)_"),
         ],
         "note": "O‘zbek tilidagi *-mi* qo‘shimchasining o‘rnini rus tilida ohang "
                 "bajaradi. Ovozni ko‘tarish kerak bo‘lgan so‘z — siz so‘rayotgan so‘z."},

        {"type": "sec", "ru": "УПРАЖНЕНИЯ", "uz": "Mashqlar"},

        {"type": "ex", "n": 1,
         "task": "Mos olmoshni qo‘ying.",
         "hint": "я · ты · он · она́ · вы",
         "items": [
             ("~ студе́нт. Меня́ зову́т Аза́мат.", "я / он"),
             ("Извини́те, ~ преподава́тель?", "ты / вы"),
             ("Э́то Ша́хло. ~ из Ташке́нта.", "он / она́"),
             ("Э́то Аза́мат. ~ из Самарка́нда.", "он / она́"),
             ("~ рабо́таю в больни́це.", "я / вы"),
             ("Ди́лшод, ~ изуча́ешь ру́сский язы́к?", "ты / она́"),
         ]},

        "PAGE",

        # ------------------------------------------------ 7-sahifa
        {"type": "ex", "n": 2,
         "task": "Savol va javobni moslashtiring.",
         "hint": "chiziq bilan bog‘lang",
         "match": [
             ["Здра́вствуйте!", "Как вас зову́т?", "Вы отку́да?",
              "Вы студе́нт?", "О́чень прия́тно."],
             ["Да, я студе́нт.", "Мне то́же о́чень прия́тно.",
              "Здра́вствуйте!", "Я из Бухары́.", "Меня́ зову́т Ди́лноза."],
         ]},

        {"type": "ex", "n": 3,
         "task": "«ты» yoki «вы»? Kerakli variantni belgilang.",
         "items": [
             ("Rus tili o‘qituvchingizga", "ты / вы"),
             ("Yoningizdagi o‘n yoshli bolaga", "ты / вы"),
             ("Do‘kondagi notanish sotuvchiga", "ты / вы"),
             ("Kichik ukangizga", "ты / вы"),
             ("Ish beruvchingiz bilan suhbatda", "ты / вы"),
             ("Ko‘chada yo‘l so‘rayotgan tengdoshingizga", "ты / вы"),
         ]},

        {"type": "ex", "n": 4,
         "task": "Gapni savolga aylantiring. So‘z tartibi o‘zgarmaydi — faqat ohang.",
         "model": ["Он врач. → Он врач?"],
         "items": [
             "Она́ студе́нтка. → ~~~",
             "Вы из Ташке́нта. → ~~~",
             "Аза́мат рабо́тает в больни́це. → ~~~",
             "Тебя́ зову́т Ди́лшод. → ~~~",
         ]},

        {"type": "ex", "n": 5,
         "task": "Rus tiliga tarjima qiling.",
         "items": [
             "Men talabaman. ~~~",
             "Mening ismim Dilnoza. ~~~",
             "Men Buxorodanman. ~~~",
             "Siz o‘qituvchimisiz? ~~~",
             "Tanishganimdan juda xursandman. ~~~",
             "U shifokor. U Samarqandda yashaydi. ~~~",
         ]},

        {"type": "ex", "n": 6,
         "task": "Suhbatdagi bo‘sh joylarni to‘ldiring.",
         "items": [
             "— Здра́вствуйте! Меня́ ~~ Ка́мола. А как ~~ зову́т?",
             "— Меня́ зову́т Ти́мур. О́чень ~~.",
             "— Мне то́же. Вы ~~? — Я из Нама́нгана.",
             "— Почему́ вы ~~ ру́сский язы́к? — Я ~~ рабо́тать в Росси́и.",
         ]},

        "PAGE",

        # ------------------------------------------------ 8-sahifa
        {"type": "ex", "n": 7,
         "task": "O‘zingiz haqingizda yozing.",
         "hint": "gaplarni to‘liq yozing",
         "items": [
             "Меня́ зову́т ~~~",
             "Я из ~~~",
             "Я живу́ в ~~~",
             "Я ~~~ (студе́нт / преподава́тель / врач …)",
             "Я изуча́ю ру́сский язы́к, потому́ что ~~~",
         ]},

        {"type": "sec", "ru": "ГОВОРИТЕ!", "uz": "Gapiring"},

        {"type": "ex", "n": 8,
         "task": "Juftlikda ishlang. Navbat bilan ikkala rolni ham bajaring.",
         "hint": "yolg‘iz o‘qiyotgan bo‘lsangiz, ikkalasini ham ovoz chiqarib o‘qing"},

        {"type": "roleplay", "cols": [
            {"head": "A — yangi o‘quvchi", "steps": [
                "Salomlashing.",
                "Ismingizni ayting va suhbatdoshning ismini so‘rang.",
                "Tanishganingizdan xursand ekaningizni bildiring.",
                "Qayerdan ekaningizni ayting va undan ham so‘rang.",
                "Nega rus tilini o‘rganayotganingizni tushuntiring.",
            ]},
            {"head": "B — o‘qituvchi", "steps": [
                "Salomga javob bering.",
                "O‘z ismingizni ayting, kasbingizni qo‘shing.",
                "Siz ham xursand ekaningizni ayting.",
                "Javob bering, keyin qayerda yashashini so‘rang.",
                "«Отли́чно! Тогда́ начина́ем» deb darsni boshlang.",
            ]},
        ]},


        {"type": "ex", "n": 9,
         "task": "Guruh bilan o‘yin: *«Найди́ колле́гу»* — hamkasbingizni toping.",
         "hint": "faqat rus tilida gaplashing"},

        {"type": "text", "class": "body-text-sm", "p": [
            "Har bir o‘quvchi quyidagi kasblardan bittasini yashirincha tanlaydi. "
            "Keyin hamma turib, bir-biridan so‘raydi va o‘zi bilan bir xil kasbni "
            "tanlagan odamlarni topadi. O‘zbekcha bitta so‘z ham ishlatilmaydi.",
        ]},

        {"type": "keyphrases",
         "title": "ПРОФЕССИИ · Kasblar",
         "rows": [
             ("врач", "shifokor"),
             ("учи́тель", "o‘qituvchi"),
             ("инжене́р", "muhandis"),
             ("води́тель", "haydovchi"),
             ("программи́ст", "dasturchi"),
             ("продаве́ц", "sotuvchi"),
         ]},

        {"type": "model", "lines": [
            "Извини́те, вы врач?",
            "Нет, я учи́тель. А вы?",
            "Я то́же учи́тель! О́чень прия́тно.",
        ]},
        "PAGE",

        # ------------------------------------------------ 9-sahifa
        {"type": "sec", "ru": "ЧИТАЙТЕ!", "uz": "O‘qing"},

        {"type": "text", "class": "body-text-sm", "p": [
            "Quyida uch kishi o‘zi haqida yozgan. O‘qing va pastdagi savollarga javob bering.",
        ]},

        {"type": "read", "items": [
            "Меня́ зову́т Ди́лноза. Я из Бухары́, но живу́ в Ташке́нте. Я студе́нтка. "
            "Я изуча́ю ру́сский язы́к, потому́ что хочу́ рабо́тать в тури́зме.",
            "Меня́ зову́т Ти́мур. Я из Нама́нгана. Я води́тель. Я не студе́нт. "
            "Ру́сский язы́к мне ну́жен для рабо́ты.",
            "Меня́ зову́т Ка́мола Раши́довна. Я преподава́тель. Я живу́ в Самарка́нде. "
            "Я о́чень люблю́ ру́сскую литерату́ру.",
        ]},

        {"type": "ex", "n": 10,
         "task": "Matnga qarab javob bering. To‘liq gap bilan yozing.",
         "items": [
             "Кто из Бухары́? ~~~",
             "Кто не студе́нт? ~~~",
             "Кто живёт в Самарка́нде? ~~~",
             "Почему́ Ди́лноза изуча́ет ру́сский язы́к? ~~~",
         ]},

        {"type": "culture",
         "title": "ЭТО ИНТЕРЕСНО · Ruscha ismlar",
         "p": ["Rus ismi uch qismdan iborat: *и́мя* (ism), *о́тчество* (otasining ismidan "
               "yasalgan qism) va *фами́лия* (familiya). Masalan: *Ива́н Петро́вич Смирно́в*.",
               "Rasmiy vaziyatda odamga *ism + otchestvo* bilan murojaat qilinadi: "
               "*«Здра́вствуйте, Ива́н Петро́вич!»* — bu eng hurmatli shakl. Familiya "
               "bilan murojaat qilish (*«Смирно́в!»*) esa qo‘pol yoki maktabdagi kabi "
               "eshitiladi."],
         "note": "O‘zbekistonda ham shu odat saqlanib qolgan: *Камо́ла Раши́довна*, "
                 "*Фаёза Алише́ровна*. Agar rus tilida gaplashayotgan hamkasbingiz "
                 "o‘zini shunday tanishtirsa — siz ham unga aynan shunday murojaat qiling."},


        {"type": "ex", "n": 11,
         "task": "Vizitkalarni o‘qing va savollarga javob bering.",
         "hint": "yuqoridagi qoidaga qarang",
         "cards": [
             ("Соколо́ва\nИри́на Никола́евна", "врач", "Городска́я больни́ца №7 · Москва́"),
             ("Усма́нов\nТи́мур Бахтия́рович", "инжене́р", "«Узбекнефтега́з» · Ташке́нт"),
             ("Петро́в\nСерге́й Ива́нович", "программи́ст", "IT-центр «Ба́рс» · Каза́нь"),
         ],
         "items": [
             "Как зову́т врача́? ~~~",
             "Кто из Ташке́нта? ~~~",
             "Как вы обрати́тесь к Петро́ву на рабо́те? ~~~",
         ]},

        "PAGE",

        # ------------------------------------------------ 10-sahifa
        {"type": "ex", "n": 12,
         "task": "Yodda qolganini tekshiring. Ruschasini urg‘u belgisi bilan yozing.",
         "hint": "kitobga qaramasdan urinib ko‘ring",
         "items": [
             "assalomu alaykum ~~~",
             "kechirasiz ~~~",
             "o‘qituvchi ~~~",
             "qayerdan ~~~",
             "nega ~~~",
             "men kasalxonada ishlayman ~~~",
             "rus tili ~~~",
             "tushunarli ~~~",
             "tanishganimdan juda xursandman ~~~",
             "unda boshladik ~~~",
         ]},

        {"type": "advice",
         "title": "USTOZDAN MASLAHAT",
         "p": ["Birinchi darsdanoq bitta odat qiling: yangi so‘zni yozib olayotganda "
               "*urg‘u belgisini ham* qo‘ying. Urg‘usiz yodlangan so‘z — yarim yodlangan "
               "so‘z. Rus tilida urg‘u joyi o‘zgarsa, ma’no ham o‘zgarib ketadi: "
               "*за́мок* (qal’a) va *замо́к* (qulf) — bir xil harflar, boshqa so‘zlar."],
         "chain": ["So‘zni ko‘rdim", "urg‘uni belgiladim", "ovoz chiqarib aytdim", "esda qoldi"],
         "after": ["Va yana: birinchi kundan «Здра́вствуйте» ni mukammal aytishga harakat "
                   "qiling. Bu — suhbatdoshingiz eshitadigan birinchi so‘z, undan sizning "
                   "darajangiz haqida birinchi taassurot tug‘iladi."]},

        {"type": "selfcheck", "items": [
            "Salomlashib, ismimni ayta olaman: «Здра́вствуйте! Меня́ зову́т…»",
            "Suhbatdoshning ismini so‘ray olaman: «Как вас зову́т?»",
            "Qayerdan ekanimni ayta olaman: «Я из…»",
            "Rus tilida hozirgi zamonda «bo‘lmoq» fe’li yo‘qligini bilaman",
            "«ты» va «вы» ni qachon ishlatishni bilaman",
            "«ы» tovushini «и» dan ajratib ayta olaman",
            "Urg‘usiz «о» ni «а» kabi o‘qiyman: Москва́ — «Masqva»",
        ]},

    ],
}
