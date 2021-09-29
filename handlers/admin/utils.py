from functools import wraps

from aiogram import types

from data.config import ADMINS


def admin_requires(f):
    @wraps(f)
    async def wrapped(message: types.Message, *args, **kwargs):
        if not ADMINS or message.from_user.id not in ADMINS:
            await message.bot.delete_message(
                chat_id=message.chat.id,
                message_id=message.message_id
            )
            return None
        else:
            return await f(message, *args, **kwargs)

    return wrapped
