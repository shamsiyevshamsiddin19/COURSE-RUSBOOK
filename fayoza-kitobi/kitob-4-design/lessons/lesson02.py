# -*- coding: utf-8 -*-
"""2-dars — Знакомство.

1-darsda o'quvchi o'zi haqida gapirishni o'rgandi. Bu darsda u
suhbatni boshlash va tugatishni, holini so'rashni va uchinchi
odamni tanishtirishni o'rganadi.

Grammatik o'zak:  vaqtga qarab salomlashish; «Как дела?» va javoblar;
                  мой / моя (rodning birinchi tanishuvi); kasblarning
                  erkak va ayol shakli; rasmiy va do'stona xayrlashish.
Talaffuz o'zagi:  жи/ши doim qattiq; -ого/-его -> «-ova/-eva»;
                  so'z oxiridagi jarangli undoshning jarangsizlanishi.
"""

LESSON = {
    "number": 2,
    "running": "Знакомство",
    "blocks": [

        # ------------------------------------------------ 1-sahifa
        {"type": "title",
         "number": 2,
         "ru": "ЗНАКОМСТВО",
         "uz": "Tanishuv — suhbatni boshlash va tugatish"},

        {"type": "cando", "items": [
            "Kunning qaysi qismi ekaniga qarab to‘g‘ri salomlasha olasiz",
            "«Как дела́?» deb so‘ray olasiz va bu savolga javob bera olasiz",
            "Do‘stingizni yoki hamkasbingizni boshqa odamga tanishtira olasiz",
            "Kimning kasbi nima ekanini so‘ray olasiz va ayta olasiz",
            "Rasmiy va do‘stona xayrlashuvni farqlay olasiz",
        ]},

        {"type": "sec", "ru": "ДИАЛОГ", "uz": "Suhbat"},

        {"type": "dialog", "n": 1,
         "scene": "Ertalab, til markazining yo‘lagida.",
         "lines": [
             ("Фаёза:", "До́брое у́тро, Аза́мат!", "Xayrli tong, Azamat!"),
             ("Аза́мат:", "До́брое у́тро, Фаёза Алише́ровна!",
              "Xayrli tong, Fayoza Alisherovna!"),
             ("Фаёза:", "Как дела́?", "Ishlaringiz qalay?"),
             ("Аза́мат:", "Хорошо́, спаси́бо. А у вас?", "Yaxshi, rahmat. Sizchi?"),
             ("Фаёза:", "То́же хорошо́. Проходи́те, пожа́луйста.",
              "Men ham yaxshi. Kiravering."),
         ]},

        {"type": "dialog", "n": 2,
         "scene": "Tanaffusda. Shahlo dugonasini olib keldi.",
         "lines": [
             ("Ша́хло:", "Аза́мат, познако́мьтесь! Э́то моя́ подру́га Ди́лноза.",
              "Azamat, tanishing! Bu mening dugonam Dilnoza."),
             ("Аза́мат:", "О́чень прия́тно. Аза́мат.", "Juda yoqimli. Azamat."),
             ("Ди́лноза:", "Ди́лноза. О́чень прия́тно.", "Dilnoza. Juda yoqimli."),
             ("Аза́мат:", "Ди́лноза, кто вы по профе́ссии?",
              "Dilnoza, kasbingiz nima?"),
             ("Ди́лноза:", "Я медсестра́. А вы?", "Men hamshiraman. Sizchi?"),
             ("Аза́мат:", "Я инжене́р. Рабо́таю в Ташке́нте.",
              "Men muhandisman. Toshkentda ishlayman."),
         ]},

        "PAGE",

        # ------------------------------------------------ 2-sahifa
        {"type": "dialog", "n": 3,
         "scene": "Dars tugadi. Hamma tarqalmoqda.",
         "lines": [
             ("Фаёза:", "Уро́к око́нчен. До свида́ния!", "Dars tugadi. Xayr!"),
             ("Ша́хло:", "До свида́ния, Фаёза Алише́ровна!",
              "Xayr, Fayoza Alisherovna!"),
             ("Аза́мат:", "До за́втра!", "Ertagacha!"),
             ("Ди́лноза:", "Пока́! Всего́ хоро́шего!", "Xayr! Hammasi yaxshi bo‘lsin!"),
             ("Фаёза:", "Пока́! Хоро́шего дня!", "Xayr! Kuningiz yaxshi o‘tsin!"),
         ]},

        {"type": "sec", "ru": "СЛОВА", "uz": "Yangi so‘zlar"},

        {"type": "vocab", "words": [
            ("до́брое у́тро", "dob-ra-ye ut-ra", "xayrli tong", "04:00–11:00"),
            ("до́брый день", "dob-riy den", "xayrli kun", "11:00–17:00"),
            ("до́брый ве́чер", "dob-riy ve-chir", "xayrli kech", "17:00–23:00"),
            ("споко́йной но́чи", "spa-koy-nay no-chi", "xayrli tun", "uxlashdan oldin"),
            ("приве́т", "pri-vet", "salom", "do‘stona"),
            ("здра́вствуй", "zdra-stvuy", "salom", "«sen» shakli"),
            ("как дела́?", "kak di-la", "ishlar qalay?"),
            ("хорошо́", "xa-ra-sho", "yaxshi"),
            ("отли́чно", "at-lich-na", "a’lo"),
            ("норма́льно", "nar-mal-na", "durustgina"),
            ("не о́чень", "ni o-chin", "unchalik emas"),
            ("пло́хо", "plo-xa", "yomon"),
            ("спаси́бо", "spa-si-ba", "rahmat"),
            ("пожа́луйста", "pa-ja-lus-ta", "marhamat; iltimos"),
            ("проходи́те", "pra-xa-di-te", "kiravering"),
            ("познако́мьтесь", "paz-na-kom-tes", "tanishing"),
            ("э́то", "e-ta", "bu"),
            ("мой / моя́", "moy / ma-ya", "mening", "erkak / ayol"),
            ("друг / подру́га", "drug / pad-ru-ga", "do‘st", "o‘g‘il / qiz"),
        ]},

        "PAGE",

        # ------------------------------------------------ 3-sahifa
        {"type": "vocab", "words": [
            ("кто", "kto", "kim"),
            ("по профе́ссии", "pa pra-fe-si-i", "kasbi bo‘yicha"),
            ("медсестра́", "mit-sist-ra", "hamshira"),
            ("инжене́р", "in-ji-ner", "muhandis"),
            ("учи́тель / учи́тельница", "u-chi-tel / u-chi-tel-ni-tsa", "o‘qituvchi"),
            ("врач", "vrach", "shifokor", "erkak ham, ayol ham"),
            ("продаве́ц / продавщи́ца", "pra-da-vets / pra-dav-shi-tsa", "sotuvchi"),
            ("води́тель", "va-di-tel", "haydovchi"),
            ("бухга́лтер", "bu-gal-tir", "buxgalter"),
            ("рабо́та", "ra-bo-ta", "ish"),
            ("уро́к", "u-rok", "dars"),
            ("око́нчен", "a-kon-chin", "tugadi"),
            ("до свида́ния", "da svi-da-ni-ya", "xayr", "rasmiy"),
            ("до за́втра", "da zaf-tra", "ertagacha"),
            ("пока́", "pa-ka", "xayr", "do‘stona"),
            ("всего́ хоро́шего", "fsi-vo xa-ro-shi-va", "hammasi yaxshi bo‘lsin"),
            ("хоро́шего дня", "xa-ro-shi-va dnya", "kuningiz yaxshi o‘tsin"),
            ("то́же", "to-je", "ham"),
        ]},

        {"type": "sec", "ru": "ПРОИЗНОШЕНИЕ", "uz": "Talaffuz"},

        {"type": "pron",
         "title": "Yozilgani boshqa, o‘qilgani boshqa — uchta qoida",
         "rows": [
             ("всего́ хоро́шего · его́", "fsi-vo · xa-ro-shi-va · yi-vo",
              "Sifat va olmoshlardagi *-ого / -его* qo‘shimchasi hech qachon "
              "«-ogo» deb o‘qilmaydi — doim *«-ova / -eva»*. Bu rus tilining eng "
              "mashhur «tuzoq»laridan biri."),
             ("маши́на · жизнь · цирк", "ma-shi-na · jizn · tsirk",
              "*ж, ш, ц* harflari har doim qattiq. Ulardan keyingi *«и»* aslida "
              "*«ы»* kabi o‘qiladi: «маши́на» — «mashına», «жизнь» — «jızn»."),
             ("до свида́ния", "da-svi-da-ni-ya",
              "Bu ikki so‘z nutqda bitta so‘zdek aytiladi va «до» dagi «о» "
              "urg‘usiz — «а» bo‘lib ketadi. Sekin emas, bir tekis ayting."),
         ]},

        "PAGE",

        # ------------------------------------------------ 4-sahifa
        {"type": "pron",
         "title": "So‘z oxiridagi undosh — jarangsizlanadi",
         "p": ["Rus tilida jarangli undosh so‘z oxirida kelsa, o‘zining jarangsiz "
               "juftiga aylanadi. O‘zbek tilida bunday emas, shuning uchun bu "
               "odatlanishni talab qiladi."],
         "rows": [
             ("Ивано́в · друг · зуб", "I-va-nof · druk · zup",
              "*в → ф*, *г → к*, *б → п*. «Иванов» hech qachon «Ivanov» deb "
              "tugamaydi — «Ivanof»."),
             ("хле́б · го́род · муж", "xlep · go-rat · mush",
              "*б → п*, *д → т*, *ж → ш*. Lekin so‘z o‘zgarganda jarang qaytadi: "
              "«го́род» — «garat», ammo «города́» — «garada»."),
         ]},

        {"type": "keyphrases",
         "sub": "Shu o‘n ibora bilan siz kunning istalgan paytida suhbatni "
                "boshlab, tugata olasiz.",
         "rows": [
             ("До́брое у́тро!", "Xayrli tong!"),
             ("До́брый день!", "Xayrli kun!"),
             ("До́брый ве́чер!", "Xayrli kech!"),
             ("Как дела́?", "Ishlar qalay?"),
             ("Хорошо́, спаси́бо. А у вас?", "Yaxshi, rahmat. Sizchi?"),
             ("Познако́мьтесь! Э́то…", "Tanishing! Bu…"),
             ("Кто вы по профе́ссии?", "Kasbingiz nima?"),
             ("До свида́ния!", "Xayr! (rasmiy)"),
             ("Пока́!", "Xayr! (do‘stona)"),
             ("Всего́ хоро́шего!", "Hammasi yaxshi bo‘lsin!"),
         ]},

        {"type": "advice",
         "title": "USTOZDAN MASLAHAT",
         "p": ["Salomlashish va xayrlashish — o‘ylab o‘tirmaydigan darajada "
               "avtomatik bo‘lishi kerak. Buning eng oson yo‘li: bir hafta "
               "davomida *o‘zingiz bilan o‘zingiz* ruscha salomlashing. "
               "Ertalab ko‘zingizni ochganingizda — *«До́брое у́тро»*. Tushda "
               "ovqatga o‘tirganda — *«До́брый день»*. Yotishdan oldin — "
               "*«Споко́йной но́чи»*."],
         "chain": ["Ertalab", "До́брое у́тро", "Tushda", "До́брый день", "Kechqurun",
                   "До́брый ве́чер"],
         "after": ["Bir haftadan keyin bu iboralar o‘ylamasdan chiqadigan bo‘ladi — "
                   "va aynan shu narsa sizni «kitobdan o‘rgangan» odamdan "
                   "«gapiradigan» odamga aylantiradi.",
                   "Va yana bitta narsa: *«Всего́ хоро́шего»* ni «fsivo xaroshiva» "
                   "deb aytishni mashq qiling. Uni to‘g‘ri aytsangiz, suhbatdoshingiz "
                   "sizning darajangizni birdaniga yuqori baholaydi."]},

        "PAGE",

        # ------------------------------------------------ 5-sahifa
        {"type": "sec", "ru": "ГРАММАТИКА", "uz": "Qoida"},

        {"type": "gram",
         "title": "1. Salomlashish — soatga qarab tanlanadi",
         "p": ["O‘zbek tilida «assalomu alaykum» kun bo‘yi ishlaydi. Rus tilida esa "
               "salom kunning qaysi qismi ekaniga bog‘liq:"],
         "tables": [{
             "head": ["Vaqt", "Salom", "Qachon ishlatiladi"],
             "rows": [
                 ("04:00 – 11:00", "До́брое у́тро!", "ertalab"),
                 ("11:00 – 17:00", "До́брый день!", "kunduzi"),
                 ("17:00 – 23:00", "До́брый ве́чер!", "kechqurun"),
                 ("uxlashdan oldin", ("Споко́йной но́чи!", "hl"),
                  "salom emas — xayrlashuv!"),
             ]}],
         "note": "Diqqat: *«Споко́йной но́чи»* bilan salomlashib bo‘lmaydi — u faqat "
                 "uxlashdan oldin aytiladigan xayrlashuv. Kechasi uchrashganda ham "
                 "*«До́брый ве́чер»* deyiladi. Vaqtdan qat’i nazar ishlaydigan "
                 "universal salom — *«Здра́вствуйте!»*"},

        {"type": "gram",
         "title": "2. «Как дела́?» va unga javoblar",
         "p": ["Javoblar yaxshidan yomonga qarab shunday joylashadi:"],
         "tables": [{
             "head": ["Javob", "Ma’nosi", "Qachon"],
             "rows": [
                 (("Отли́чно!", "hl"), "A’lo!", "hammasi juda yaxshi"),
                 ("Хорошо́, спаси́бо.", "Yaxshi, rahmat.", "odatdagi javob"),
                 ("Норма́льно.", "Durustgina.", "yomon ham emas, yaxshi ham"),
                 ("Не о́чень.", "Unchalik emas.", "biroz noxush"),
                 ("Пло́хо.", "Yomon.", "haqiqatan yomon"),
             ]}],
         "note": "Savolni qaytarish uchun *«А у вас?»* (siz bilan) yoki *«А у тебя́?»* "
                 "(sen bilan) deyiladi. Javobsiz qoldirmang — bu qo‘pol hisoblanadi."},

        "PAGE",

        # ------------------------------------------------ 6-sahifa
        {"type": "gram",
         "title": "3. мой yoki моя́? — rod bilan birinchi tanishuv",
         "p": ["Rus tilida har bir ot erkak (он) yoki ayol (она́) rodiga tegishli. "
               "«Mening» so‘zi shu rodga moslashadi. Rodni odatda so‘zning oxirgi "
               "harfidan bilib olish mumkin:"],
         "tables": [{
             "head": ["Rod", "So‘z qanday tugaydi", "«Mening»", "Misol"],
             "rows": [
                 ("erkak — он", "undosh yoki -й", ("мой", "hl"),
                  "мой друг, мой брат, мой уро́к"),
                 ("ayol — она́", "-а yoki -я", ("моя́", "hl"),
                  "моя́ подру́га, моя́ сестра́, моя́ рабо́та"),
             ]}],
         "note": "*друг* undosh bilan tugaydi → *мой друг*. *подру́га* «-а» bilan "
                 "tugaydi → *моя́ подру́га*. Shu bitta qoida bilan darsdagi "
                 "so‘zlarning deyarli hammasini to‘g‘ri ishlatasiz. To‘liq "
                 "qoidani 9- va 11-darslarda ko‘ramiz."},

        {"type": "gram",
         "title": "4. Kasblarning erkak va ayol shakli",
         "tables": [{
             "head": ["Erkak", "Ayol", "Ma’nosi"],
             "rows": [
                 ("студе́нт", "студе́нтка", "talaba"),
                 ("учи́тель", "учи́тельница", "o‘qituvchi"),
                 ("продаве́ц", "продавщи́ца", "sotuvchi"),
                 ("перево́дчик", "перево́дчица", "tarjimon"),
                 ("врач", ("врач", "hl"), "shifokor — shakli o‘zgarmaydi"),
                 ("инжене́р", ("инжене́р", "hl"), "muhandis — shakli o‘zgarmaydi"),
             ]}],
         "note": "Ba’zi kasblarning ayol shakli yo‘q: ayol shifokor haqida ham "
                 "*«Она́ врач»* deyiladi. Aksincha, *медсестра́* (hamshira) — "
                 "faqat ayol shakli; erkak uchun *медбра́т* ishlatiladi."},

        {"type": "gram",
         "title": "5. Xayrlashish — rasmiy va do‘stona",
         "tables": [{
             "head": ["Rasmiy — «вы»", "Do‘stona — «ты»", "Ma’nosi"],
             "rows": [
                 ("До свида́ния!", "Пока́!", "Xayr!"),
                 ("Всего́ хоро́шего!", "Дава́й!", "Hammasi yaxshi bo‘lsin!"),
                 ("До за́втра!", "До за́втра!", "Ertagacha!"),
                 ("Споко́йной но́чи!", "Споко́йной но́чи!", "Xayrli tun!"),
             ]}],
         "note": "*«Пока́»* — faqat yaqin odamlarga. O‘qituvchiga, rahbaringizga yoki "
                 "notanish odamga *«Пока́»* desangiz — xuddi o‘zbekchada ustozingizga "
                 "«ketdim» degandek eshitiladi. Shubhalansangiz — *«До свида́ния»*."},

        "PAGE",

        # ------------------------------------------------ 7-sahifa
        {"type": "sec", "ru": "УПРАЖНЕНИЯ", "uz": "Mashqlar"},

        {"type": "ex", "n": 1,
         "task": "Soatga qarang va to‘g‘ri salomni yozing.",
         "items": [
             "07:30 — ~~~",
             "14:00 — ~~~",
             "19:45 — ~~~",
             "23:00, uxlashdan oldin — ~~~",
         ]},

        {"type": "ex", "n": 2,
         "task": "«мой» yoki «моя́»? To‘g‘risini tanlang.",
         "items": [
             ("~ друг Аза́мат.", "мой / моя́"),
             ("~ подру́га Ди́лноза.", "мой / моя́"),
             ("~ сестра́ — медсестра́.", "мой / моя́"),
             ("~ брат — инжене́р.", "мой / моя́"),
             ("~ рабо́та в больни́це.", "мой / моя́"),
             ("~ уро́к в два часа́.", "мой / моя́"),
         ]},

        {"type": "ex", "n": 3,
         "task": "Kasbni ayol shakliga o‘tkazing. O‘zgarmasa, xuddi shunday yozing.",
         "model": ["Он студе́нт. → Она́ студе́нтка."],
         "items": [
             "Он учи́тель. → ~~~",
             "Он продаве́ц. → ~~~",
             "Он врач. → ~~~",
             "Он перево́дчик. → ~~~",
             "Он инжене́р. → ~~~",
         ]},

        {"type": "ex", "n": 4,
         "task": "Suhbatdagi bo‘sh joylarni to‘ldiring.",
         "items": [
             "— До́брое ~~! Как ~~? — Хорошо́, ~~. А у вас?",
             "— Познако́мьтесь! Э́то ~~ подру́га Ка́мола.",
             "— Ка́мола, кто вы ~~ профе́ссии? — Я ~~.",
             "— Уро́к око́нчен. До ~~! — ~~! Всего́ хоро́шего!",
         ]},

        "PAGE",

        # ------------------------------------------------ 8-sahifa
        {"type": "ex", "n": 5,
         "task": "Rus tiliga tarjima qiling.",
         "items": [
             "Xayrli kun! Ishlaringiz qalay? ~~~",
             "Yaxshi, rahmat. Sizchi? ~~~",
             "Tanishing! Bu mening do‘stim Timur. ~~~",
             "U kasbi bo‘yicha kim? — U buxgalter. ~~~",
             "Xayr! Ertagacha! ~~~",
         ]},

        {"type": "ex", "n": 6,
         "task": "Rasmiymi yoki do‘stonami? Har bir vaziyat uchun to‘g‘ri "
                 "xayrlashuvni belgilang.",
         "items": [
             ("Rus tili o‘qituvchingiz bilan dars oxirida", "До свида́ния / Пока́"),
             ("Yaqin do‘stingiz bilan kafedan chiqayotib", "До свида́ния / Пока́"),
             ("Ish suhbatidan keyin rahbar bilan", "До свида́ния / Пока́"),
             ("Ukangiz bilan uyda, yotishdan oldin", "Споко́йной но́чи / До свида́ния"),
         ]},

        {"type": "ex", "n": 7,
         "task": "Til markazining dars jadvali. Har bir dars boshida o‘qituvchi "
                 "qanday salomlashadi?",
         "cards": [
             ("Группа A-1\n08:30 – 10:00", "у́тро", "salom: ~~~"),
             ("Группа B-2\n13:00 – 14:30", "день", "salom: ~~~"),
             ("Группа C-1\n18:30 – 20:00", "ве́чер", "salom: ~~~"),
         ]},

        {"type": "sec", "ru": "ГОВОРИТЕ!", "uz": "Gapiring"},

        {"type": "ex", "n": 8,
         "task": "Uch kishi bo‘lib ishlang: A o‘z do‘sti B ni C ga tanishtiradi.",
         "hint": "yolg‘iz bo‘lsangiz, uchala rolni ham ovoz chiqarib o‘qing"},

        {"type": "roleplay", "cols": [
            {"head": "A — tanishtiruvchi", "steps": [
                "Kunning vaqtiga qarab salomlashing.",
                "«Познако́мьтесь!» deb B ni tanishtiring.",
                "B ning kasbini ayting.",
                "Suhbat oxirida ikkalasi bilan xayrlashing.",
            ]},
            {"head": "B va C — tanishayotganlar", "steps": [
                "Salomga javob bering.",
                "Ismingizni ayting: «О́чень прия́тно, …»",
                "Bir-biringizdan kasbni so‘rang.",
                "Do‘stona yoki rasmiy xayrlashuvni tanlang.",
            ]},
        ]},

        "PAGE",

        # ------------------------------------------------ 9-sahifa
        {"type": "ex", "n": 9,
         "task": "Zanjir o‘yini: *«Как дела́?»* — guruh bo‘ylab.",
         "hint": "har kim boshqacha javob berishi kerak"},

        {"type": "model", "lines": [
            "Ша́хло, как дела́?",
            "Отли́чно! А у тебя́, Аза́мат?",
            "Норма́льно. Ди́лноза, а у тебя́?",
        ]},

        {"type": "sec", "ru": "ЧИТАЙТЕ!", "uz": "O‘qing"},

        {"type": "text", "class": "body-text-sm", "p": [
            "Uchta qisqa xabar. O‘qing va pastdagi savollarga javob bering.",
        ]},

        {"type": "read", "items": [
            "До́брое у́тро, Ди́лноза! Как дела́? У меня́ всё хорошо́. Сего́дня "
            "уро́к в два часа́. До встре́чи! Ша́хло",
            "Приве́т, Аза́мат! Э́то мой брат Ти́мур. Он води́тель, рабо́тает в "
            "Нама́нгане. Он то́же изуча́ет ру́сский язы́к. Пока́!",
            "До́брый ве́чер, Фаёза Алише́ровна! Извини́те, за́втра я не могу́. "
            "У меня́ рабо́та. До свида́ния! Ди́лноза",
        ]},

        {"type": "ex", "n": 10,
         "task": "Matnga qarab javob bering.",
         "items": [
             "Кто написа́л пе́рвое сообще́ние? ~~~",
             "Кто брат Ти́мура? Кто он по профе́ссии? ~~~",
             "Почему́ Ди́лноза не мо́жет за́втра? ~~~",
             "Како́е сообще́ние са́мое официа́льное? Почему́? ~~~",
         ]},

        {"type": "culture",
         "title": "ЭТО ИНТЕРЕСНО · «Как дела́?» — bu shunchaki odob emas",
         "p": ["Ingliz tilidagi «How are you?» dan farqli o‘laroq, ruslar "
               "*«Как дела́?»* deb so‘raganda haqiqatan javob kutishadi. "
               "Agar ishlaringiz yomon bo‘lsa — *«Не о́чень»* yoki *«Пло́хо»* "
               "deyish mumkin, va bu g‘alati emas.",
               "Aksincha, har doim *«Отли́чно!»* deb javob berish ba’zan "
               "samimiy emasdek tuyuladi. Rus muomalasida holatni ochiq "
               "aytish odatiy hol."],
         "note": "Notanish odam bilan esa *«Как дела́?»* deyilmaydi — u faqat "
                 "tanish odamlarga. Notanishga *«Здра́вствуйте»* yetarli."},

        "PAGE",

        # ------------------------------------------------ 10-sahifa
        {"type": "ex", "n": 11,
         "task": "O‘z do‘stingizni yozma tanishtiring. Kamida to‘rt gap yozing.",
         "hint": "ism, kasb, qayerdan, nega rus tilini o‘rganadi"},

        {"type": "write", "rows": 5},

        {"type": "ex", "n": 12,
         "task": "Yodda qolganini tekshiring. Ruschasini urg‘u belgisi bilan yozing.",
         "hint": "kitobga qaramasdan urinib ko‘ring",
         "items": [
             "xayrli tong ~~~",
             "ishlar qalay? ~~~",
             "yaxshi, rahmat ~~~",
             "tanishing! ~~~",
             "mening dugonam ~~~",
             "kasbingiz nima? ~~~",
             "hamshira ~~~",
             "xayr (rasmiy) ~~~",
             "hammasi yaxshi bo‘lsin ~~~",
         ]},

        {"type": "selfcheck", "items": [
            "Soatga qarab to‘g‘ri salomni tanlay olaman",
            "«Как дела́?» deb so‘ray olaman va beshta xil javob bera olaman",
            "«Познако́мьтесь! Э́то…» bilan odamni tanishtira olaman",
            "«мой» va «моя́» ni to‘g‘ri qo‘ya olaman",
            "Kasbning ayol shaklini yasay olaman: студе́нт — студе́нтка",
            "«До свида́ния» va «Пока́» ni qachon ishlatishni bilaman",
            "«всего́ хоро́шего» ni «fsivo xaroshiva» deb o‘qiyman",
            "«маши́на» dagi «ши» ni «шы» kabi aytaman",
        ]},

    ],
}
