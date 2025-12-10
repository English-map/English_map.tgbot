# start_bot.py

import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, CommandStart
from aiogram.types import (
    Message,
    CallbackQuery,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)

from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import FSInputFile
# LOCAL MODULES
from texts import TEXTS
from storage import (
    user_data,
    get_user_lang,
    set_user_lang,
    get_user_level,
    set_user_level
)
from test_logic import TestStates, start_test, process_answer
from test_logic import generate_test
import html


# -----------------------------
# BOT CONFIG
# -----------------------------
TOKEN = "Token"
CHANNEL_USERNAME = "@the_english_map"

bot = Bot(token=TOKEN)
dp = Dispatcher(storage=MemoryStorage())


# -------------------------
# Subscription & language helpers / handlers
# -------------------------

async def is_user_subscribed(user_id: int) -> bool:
    try:
        member = await bot.get_chat_member(CHANNEL_USERNAME, user_id)
        return member.status in ["member", "administrator", "creator"]
    except Exception:
        return False


async def block_if_not_subscribed(message: Message) -> bool:
    """
    Blocks user from using protected commands if they are not subscribed.
    Uses user's saved language if available.
    """
    user_id = int(message.from_user.id)
    lang = get_user_lang(user_id)

    # Always allow /start
    if message.text and message.text.startswith("/start"):
        return True

    subscribed = await is_user_subscribed(user_id)
    if not subscribed:
        keyboard = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="English Map 🌍", url=f"https://t.me/{CHANNEL_USERNAME.lstrip('@')}")],
                [InlineKeyboardButton(text="Check subscription ✔️", callback_data="check_sub")]
            ]
        )

        # localized "please subscribe" short messages (fallback)
        must_subscribe = {
            "en": "❗ Please subscribe to our channel to continue.\n\nClick the button below, join the channel, then press Check subscription ✔️.",
            "ru": "❗ Пожалуйста, подпишитесь на наш канал, чтобы продолжить.\n\nНажмите кнопку ниже, подпишитесь, затем нажмите «Проверить подписку ✔️».",
            "uz": "❗ Davom etish uchun kanalga obuna bo‘ling.\n\nQuyidagi tugmani bosing, kanalga obuna bo‘ling, so‘ngra «Obunani tekshirish ✔️» tugmasini bosing."
        }

        await message.answer(must_subscribe.get(lang, must_subscribe["en"]), reply_markup=keyboard)
        return False

    return True


# -------------------------------
# /start handler
# -------------------------------

@dp.message(CommandStart())
async def start(message: Message):
    user_id = int(message.from_user.id)
    lang = get_user_lang(user_id)

    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="English Map 🌍", url=f"https://t.me/{CHANNEL_USERNAME.lstrip('@')}")],
            [InlineKeyboardButton(text="Check subscription ✔️", callback_data="check_sub")]
        ]
    )

    # Use centralized TEXTS start entry (fallback to English if missing)
    start_text = TEXTS.get("start", {}).get(lang, TEXTS.get("start", {}).get("en", "Welcome!"))

    await message.answer(start_text, reply_markup=keyboard)


# -------------------------------
# Check subscription callback
# -------------------------------

@dp.callback_query(F.data == "check_sub")
async def check_subscription(callback: CallbackQuery):
    user_id = int(callback.from_user.id)
    lang = get_user_lang(user_id)

    subscribed = await is_user_subscribed(user_id)
    if subscribed:

        # TRY TO DELETE the previous welcome message
        try:
            await callback.message.delete()
        except:
            pass  # if message already deleted – ignore

        # Show language selection prompt (localized)
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="🇬🇧 English", callback_data="lang_en")],
            [InlineKeyboardButton(text="🇷🇺 Русский", callback_data="lang_ru")],
            [InlineKeyboardButton(text="🇺🇿 O‘zbek", callback_data="lang_uz")]
        ])

        choose_text = TEXTS.get("choose_language", {}).get(lang, TEXTS.get("choose_language", {}).get("en"))
        await callback.message.answer(choose_text, reply_markup=keyboard)
        await callback.answer()
    else:
        not_sub_msg = {
            "en": "❗ You are not subscribed yet. Please join our channel and then press Check subscription ✔️.",
            "ru": "❗ Вы ещё не подписаны. Пожалуйста, присоединитесь к нашему каналу и затем нажмите «Проверить подписку ✔️».",
            "uz": "❗ Siz hali obuna bo‘lmagansiz. Iltimos kanalga qo‘shiling va keyin «Obunani tekshirish ✔️» tugmasini bosing."
        }
        await callback.message.answer(not_sub_msg.get(lang, not_sub_msg["en"]))
        await callback.answer()


# -------------------------------
# /language command (open language menu anytime)
# -------------------------------

@dp.message(Command("language"))
async def language_command(message: Message):
    user_id = int(message.from_user.id)
    lang = get_user_lang(user_id)

    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🇬🇧 English", callback_data="lang_en")],
        [InlineKeyboardButton(text="🇷🇺 Русский", callback_data="lang_ru")],
        [InlineKeyboardButton(text="🇺🇿 O‘zbek", callback_data="lang_uz")]
    ])

    # Reuse choose_language text
    choose_text = TEXTS.get("choose_language", {}).get(lang, TEXTS.get("choose_language", {}).get("en"))
    await message.answer(choose_text, reply_markup=keyboard)


# -------------------------------
# Language selection callback (global)
# -------------------------------

@dp.callback_query(F.data.startswith("lang_"))
async def set_language(callback: CallbackQuery):
    user_id = int(callback.from_user.id)
    lang = callback.data.split("_")[1]

    # Save language globally
    set_user_lang(user_id, lang)

    # Delete the language selection message
    try:
        await callback.message.delete()
    except:
        pass  # in case message is already deleted

    # Prepare Start Test button in user's language
    start_label = TEXTS.get("start_test_button", {}).get(lang, TEXTS.get("start_test_button", {}).get("en", "Start test ▶️"))
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=start_label, callback_data="start_test")]
    ])

    saved_text = TEXTS.get("language_saved", {}).get(lang, TEXTS.get("language_saved", {}).get("en", "Language saved."))
    await callback.message.answer(saved_text, reply_markup=keyboard)
    await callback.answer()


# ------------------------------ START TEST ---------------------------------

@dp.callback_query(F.data == "start_test")
async def begin_test(callback: CallbackQuery, state: FSMContext):
    # Delete the "Language saved" message (with button)
    try:
        await callback.message.delete()
    except Exception:
        pass
    # Start test
    await callback.answer()
    await start_test(callback, state)

# ------------------------------ /CHANNEL -----------------------------------

@dp.message(Command("channel"))
async def channel(message: Message):

    if not await block_if_not_subscribed(message):
        return

    user_id = int(message.from_user.id)
    lang = get_user_lang(user_id)

    photo = FSInputFile("c:\\My vc\\Телеграмбот\\english_map_logo.jpg")

    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="English Map 🌍", url="https://t.me/the_english_map")]
        ]
    )

    await message.answer_photo(
        photo=photo,
        caption=TEXTS["channel"][lang],
        parse_mode="Markdown",
        reply_markup=keyboard
    )



# ------------------------------ /PROFILE -----------------------------------

@dp.message(Command("profile"))
async def profile(message: Message):
    if not await block_if_not_subscribed(message):
        return

    user = message.from_user
    user_id = int(user.id)

    lang = get_user_lang(user_id)

    # Load stored level (string or None)
    level = get_user_level(user_id)

    # If no test taken
    if not level:
        level_text = TEXTS["profile_level_not_tested"][lang]
    else:
        level_text = level

    # Make name clickable (always works, even without @username)
    safe_name = html.escape(user.full_name or "User")
    mention_link = f'<a href="tg://user?id={user_id}">{safe_name}</a>'

    # Build localized profile message
    text = (
        f"{TEXTS['profile_title'][lang]}\n"
        f"━━━━━━━━━━━━━━\n"
        f"🙋‍♂️ {TEXTS['profile_name'][lang]}: {mention_link}\n"
        f"📘 {TEXTS['profile_level'][lang]}: <b>{html.escape(str(level_text))}</b>\n\n"
        f"{TEXTS['profile_footer'][lang]}"
    )

    await message.answer(text, parse_mode="HTML")



# ------------------------------ /HELP --------------------------------------

@dp.message(Command("help"))
async def help_cmd(message: Message):

    if not await block_if_not_subscribed(message):
        return

    user_id = int(message.from_user.id)
    lang = get_user_lang(user_id)

    await message.answer(TEXTS["help"][lang], parse_mode="Markdown")




# ------------------------------ /LANGUAGE ----------------------------------

@dp.message(Command("language"))
async def language(message: Message):

    user_id = int(message.from_user.id)
    lang = get_user_lang(user_id)

    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="🇬🇧 English", callback_data="lang_en")],
            [InlineKeyboardButton(text="🇷🇺 Русский", callback_data="lang_ru")],
            [InlineKeyboardButton(text="🇺🇿 O‘zbek", callback_data="lang_uz")]
        ]
    )

    await message.answer(
        TEXTS["choose_language"][lang],
        reply_markup=keyboard
    )

@dp.callback_query(F.data.startswith("lang_"))
async def set_language(callback: CallbackQuery):
    lang = callback.data.split("_")[1]
    user_id = int(callback.from_user.id)

    set_user_lang(user_id, lang)

    await callback.answer()
    await callback.message.answer(TEXTS["language_updated"][lang])


# ------------------------------ /TEST --------------------------------------

@dp.message(Command("test"))
async def test_command(message: Message, state: FSMContext):
    if not await block_if_not_subscribed(message):
        return

    await start_test(message, state)


# ------------------------------ ANSWERS -------------------------------------

@dp.callback_query(F.data.startswith("ans_"))
async def answer_handler(callback: CallbackQuery, state: FSMContext):
    """
    A single clean handler for processing all answer buttons.
    """
    current_state = await state.get_state()

    # If the user isn't in waiting_for_answer state, ignore the tap
    if current_state != TestStates.waiting_for_answer.state:
        await callback.answer()
        return

    from test_logic import process_answer
    await process_answer(callback, state)


# ------------------------------ RUN BOT -------------------------------------

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())