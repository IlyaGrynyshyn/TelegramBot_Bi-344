from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Сьогодні"),
            KeyboardButton(text="Завтра")
        ],
        [
            KeyboardButton(text="Розклад"),
            KeyboardButton(text="Розклад дзвінків")
        ],
        [
            KeyboardButton(text= "Номер неділі"),
            KeyboardButton(text='Про бота')
        ]
    ],
    resize_keyboard=True
)