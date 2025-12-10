# texts.py

TEXTS = {

    # ------------------------------
    # Welcome / Start messages
    # ------------------------------
    "start": {
        "en": (
        "Hello!\n\n"
        "I am your English Map bot — and your learning journey starts right here. 🌍\n\n"
        "Before we begin, let’s find out your current English level.\n"
        "To continue, please subscribe to our main channel first."
        ),
        "ru": (
        "Здравствуйте!\n\n"
        "Я бот English Map — и ваше путешествие в изучении английского начинается прямо здесь. 🌍\n\n"
        "Прежде чем мы начнём, давайте узнаем ваш текущий уровень английского.\n"
        "Чтобы продолжить, пожалуйста, подпишитесь на наш основной канал."
        ),
        "uz": (
        "Salom!\n\n"
        "Men English Map botiman — va sizning ingliz tili bo‘yicha sayohatingiz aynan shu yerda boshlanadi. 🌍\n\n"
        "Boshlashdan oldin, keling, hozirgi ingliz tili darajangizni aniqlab olaylik.\n"
        "Davom etish uchun iltimos, asosiy kanalimizga obuna bo‘ling."
        ),
},

    # ------------------------------
    # Subscription check + language selection
    # ------------------------------
    "choose_language": {
        "en": "🎉 You are subscribed!\n\n🌍 Please choose your language:",
        "ru": "🎉 Вы подписаны!\n\n🌍 Пожалуйста, выберите язык:",
        "uz": "🎉 Siz obuna bo'lgansiz!\n\n🌍 Iltimos, tilni tanlang:"
    },

    "language_saved": {
        "en": "Great — language saved! ✅\nPress the button below to start the test.",
        "ru": "Отлично — язык сохранён! ✅\nНажмите кнопку ниже, чтобы начать тест.",
        "uz": "Ajoyib — til saqlandi! ✅\nTestni boshlash uchun pastdagi tugmani bosing."
    },

    "start_test_button": {
        "en": "Start test ▶️",
        "ru": "Начать тест ▶️",
        "uz": "Testni boshlash ▶️"
    },

    # ------------------------------
    # Test start message
    # ------------------------------
    "test_start": {
        "en": "🧪 Your English test is about to begin.\nYou’ll receive 20 questions one by one.\nDo your best — and good luck! 🍀",
        "ru": "🧪 Ваш тест по английскому начинается.\nВы получите 20 вопросов по одному.\nУдачи! 🍀",
        "uz": "🧪 Ingliz tili testi boshlanmoqda.\nSizga 20 ta savol navbatma-navbat beriladi.\nOmad! 🍀"
    },

    # ------------------------------
    # Test finished / results
    # ------------------------------
    "test_finished": {
        "en": "🎉 Test finished!\nYour score: {score} / 20\n📘 Your English level: *{level}*",
        "ru": "🎉 Тест завершён!\nВаш результат: {score} / 20\n📘 Ваш уровень английского: *{level}*",
        "uz": "🎉 Test tugadi!\nNatijangiz: {score} / 20\n📘 Ingliz tili darajangiz: *{level}*"
    },

    # ------------------------------
    # Profile section
    # ------------------------------
    "profile_title": {
        "en": "👤 Your Profile",
        "ru": "👤 Ваш профиль",
        "uz": "👤 Profilingiz"
    },

    "profile_level_not_tested": {
        "en": "Not tested yet ❔",
        "ru": "Тест ещё не проходили ❔",
        "uz": "Hali test topshirilmagan ❔"
    },

    "profile_text": {
        "en": (
            "👤 *Your Profile*\n"
            "━━━━━━━━━━━━━━\n"
            "🙋‍♂️ Name: {name}\n"
            "📘 Current English level: *{level}*\n\n"
            "✨ Keep learning and improving step by step!"
        ),
        "ru": (
            "👤 *Ваш профиль*\n"
            "━━━━━━━━━━━━━━\n"
            "🙋‍♂️ Имя: {name}\n"
            "📘 Текущий уровень английского: *{level}*\n\n"
            "✨ Продолжайте учиться и улучшать свои навыки!"
        ),
        "uz": (
            "👤 *Profilingiz*\n"
            "━━━━━━━━━━━━━━\n"
            "🙋‍♂️ Ism: {name}\n"
            "📘 Ingliz tili darajasi: *{level}*\n\n"
            "✨ O‘rganishda davom eting!"
        ),
    },

    # ------------------------------
    # Help command
    # ------------------------------
    "help": {
        "en": (
            "Here are the available commands:\n\n"
            "/start — restart the bot\n"
            "/channel — open the English Map channel\n"
            "/profile — view your information\n"
            "/help — list all commands\n"
            "/test — check your English level\n"
        ),
        "ru": (
            "Доступные команды:\n\n"
            "/start — перезапустить бота\n"
            "/channel — открыть канал English Map\n"
            "/profile — ваша информация\n"
            "/help — список команд\n"
            "/test — пройти тест на уровень английского\n"
        ),
        "uz": (
            "Mavjud buyruqlar:\n\n"
            "/start — botni qayta ishga tushirish\n"
            "/channel — English Map kanaliga o‘tish\n"
            "/profile — profilingiz\n"
            "/help — buyruqlar ro‘yxati\n"
            "/test — ingliz tili darajasini aniqlash\n"
        )
    },
    "profile_name": {
        "en": "Name",
        "ru": "Имя",
        "uz": "Ism"
    },

    "profile_level": {
        "en": "Current English level",
        "ru": "Текущий уровень английского",
        "uz": "Ingliz tili darajangiz"
    },

    "profile_footer": {
        "en": "✨ Keep learning and improving step by step!",
        "ru": "✨ Продолжайте учиться и улучшать свой уровень!",
        "uz": "✨ O‘rganishda davom eting va o‘sishda davom eting!"
    },
    "help": {
        "en": (
            "💡 *Help Menu*\n\n"
            "/start — restart the bot\n"
            "/channel — view our main channel\n"
            "/profile — see your progress\n"
            "/help — list all commands\n"
            "/test — start level test\n\n"
            "Need more help? Just ask! 😊\n"
            "If necessary, you can message the owner: @Abdulkayumov."
        ),
        "ru": (
            "💡 *Меню помощи*\n\n"
            "/start — перезапустить бота\n"
            "/channel — открыть основной канал\n"
            "/profile — посмотреть ваш прогресс\n"
            "/help — список команд\n"
            "/test — пройти тест уровня\n\n"
            "Нужна помощь? Просто напишите! 😊\n"
            "При необходимости вы можете написать владельцу: @Abdulkayumov."
        ),
        "uz": (
            "💡 *Yordam menyusi*\n\n"
            "/start — botni qayta ishga tushirish\n"
            "/channel — asosiy kanal\n"
            "/profile — profilingizni ko‘rish\n"
            "/help — buyruqlar ro‘yxati\n"
            "/test — daraja testini boshlash\n\n"
            "Yordam kerakmi? Marhamat, so‘rang! 😊\n"
            "Zarur bo‘lsa, bot egasi bilan bog‘lanishingiz mumkin: @Abdulkayumov."
        )
    },
    "channel": {
        "en": (
            "📘 *Welcome to English Map!*\n\n"
            "Follow your fluency and learn step by step.\n"
            "We help you understand and use English with confidence! ✨\n\n"
            "Owner: @Abdulkayumov"
        ),
        "ru": (
            "📘 *Добро пожаловать в English Map!*\n\n"
            "Следуйте своему пути изучения.\n"
            "Мы помогаем осваивать английский уверенно! ✨\n\n"
            "Owner: @Abdulkayumov"
        ),
        "uz": (
            "📘 *English Map kanaliga xush kelibsiz!*\n\n"
            "Til o‘rganish yo‘lingizni biz bilan davom ettiring.\n"
            "Ingliz tilini ishonch bilan o‘rganing! ✨\n\n"
            "Owner: @Abdulkayumov"
        )
    },
    "choose_language": {
        "en": "🌍 Please choose your language:",
        "ru": "🌍 Пожалуйста, выберите язык:",
        "uz": "🌍 Iltimos, tilni tanlang:"
    },
    "language_updated": {
        "en": "✅ Language updated!",
        "ru": "✅ Язык обновлён!",
        "uz": "✅ Til o‘zgartirildi!"
    },



}
