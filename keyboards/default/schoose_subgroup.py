from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

schoose_subgroup = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="1"),
            KeyboardButton(text="2")
        ]
    ],
    resize_keyboard=True
)
