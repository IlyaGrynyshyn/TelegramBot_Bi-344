import asyncpg
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.utils.emoji import emojize
from keyboards import default
from loader import dp
from utils.db_api import quick_commands as commands
from utils.misc import rate_limit


@rate_limit(10, 'start')
@dp.message_handler(CommandStart())
async def bot_start(message: types.Message, state: FSMContext):
    name = message.from_user.full_name
    welcome_text = (
        f"Привіт! {emojize(':wave:')}"
        "\nЯ — твоя права рука під час навчального року,"
        " адже в мене ти завжди можеш дізнатись, які в тебе пари протягом тижня"
        f"{emojize(':smiling_imp:')}"
        f"\n\nПотрібна допомога з командами? Просто відправ мені /help"
        f"\n\nХочеш більше дізнатися про бота?"
        f" Знаєш як його покращити?"
        f" Щось пішло не так?"
        f"\nВсю потрібну інформацію ти знайдеш натиснувши /about"

        f"\n\nДля початку, скажи мені хто ти{emojize(':smirk_cat:')}:"
    )

    try:
        await commands.add_user(id=message.from_user.id,
                                name=name)
    except asyncpg.exceptions.UniqueViolationError:
        pass

    await message.answer(welcome_text,reply_markup=default.main_menu)


