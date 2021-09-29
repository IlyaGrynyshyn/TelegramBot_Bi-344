from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

keyboard_about = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Назад")
        ]
    ],
    resize_keyboard=True
)
