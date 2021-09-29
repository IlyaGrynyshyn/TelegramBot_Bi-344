from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.utils.emoji import emojize

from keyboards.default import keyboard_about
from loader import dp


# Хендрел виводить інформацію /about

@dp.message_handler(Command('about'))
async def bot_about(message: types.Message):
    about_bot = (
        f"Бот, який створений, щоб спростити життя"
        f" студентам і не тільки {emojize(':wink:')}"

        f"\n\nБільше не потрібно використовувати застарілий і незрозумілий сайт, "
        f"щоб дізнатись, чи є завтра пари, доки можна поспати, а, можливо,"
        f" й прогуляти {emojize(':see_no_evil:')}"

        f"\n\nЩось не працює, "
        f"або знаєш як покращити мене?{emojize(':sunglasses:')}"
        f"\nНе соромся, пиши мені [ @falex03 ]."

    )
    await message.answer(about_bot, reply_markup=keyboard_about)
