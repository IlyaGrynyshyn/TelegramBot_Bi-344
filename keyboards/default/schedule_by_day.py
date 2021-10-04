from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

schedule_by_day = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="1.Пнд"),
            KeyboardButton(text="1.Втр"),
            KeyboardButton(text='1.Срд'),
            KeyboardButton(text='1.Чтв'),
            KeyboardButton(text='1.Птн'),

        ],
        [
            KeyboardButton(text="2.Пнд"),
            KeyboardButton(text="2.Втр"),
            KeyboardButton(text='2.Срд'),
            KeyboardButton(text='2.Чтв'),
            KeyboardButton(text='2.Птн'),
        ],
        [
            KeyboardButton(text='Назад')
        ]
    ],
    resize_keyboard=True
)