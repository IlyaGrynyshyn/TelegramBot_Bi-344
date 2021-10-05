from aiogram import types
from aiogram.utils.exceptions import MessageCantBeDeleted, MessageToDeleteNotFound

from keyboards.default.schoose_subgroup import schoose_subgroup
from loader import dp
from states.botStates import StatesOfBot


@dp.message_handler(text='/change_query', state='*')
async def cmd_change_query(message: types.Message):
    """
    Change query type
    """
    await message.answer(
        text="Вибери з якої ти підгрупи",
        reply_markup=schoose_subgroup,
        parse_mode='HTML'
    )
    await StatesOfBot.start_state.set()
    try:
        await message.delete()
    except (MessageCantBeDeleted, MessageToDeleteNotFound):
        pass


# @dp.message_handler()
# async def empty(message: types.Message):
#     await message.answer(text='Нічого не вдалось знайти, спробуй ще раз')
