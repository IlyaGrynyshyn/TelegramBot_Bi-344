from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp
from aiogram.types import ReplyKeyboardRemove

from loader import dp
from utils.misc import rate_limit

@rate_limit(10, 'help')
@dp.message_handler(CommandHelp(),state=None)
async def bot_help(message: types.Message):
    text = ("Список команд: ",
            "/start - Для початку спілкування з ботом",
            "/help - Допомога по командам бота",
            '/about - Інформація про бота',
            '/change_query - Змінити запит')

    
    await message.answer("\n".join(text),reply_markup=ReplyKeyboardRemove())
