from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Запустити бота"),
            types.BotCommand("help", "Вивести справку"),
            types.BotCommand("about",'Вивести інформацію про бота'),
            types.BotCommand("change_query",'Змінити запит')
        ]
    )
