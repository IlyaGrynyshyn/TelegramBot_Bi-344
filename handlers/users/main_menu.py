import datetime
import json

from aiogram.types import Message

from keyboards.default.about_bot_key import keyboard_about
from keyboards.default.main_menu import main_menu
from loader import dp
from utils.misc import rate_limit


@dp.message_handler(text="Назад")
async def main_page(message: Message):
    await message.answer(text='Головне меню', reply_markup=main_menu)


@dp.message_handler(text='Сьогодні')
async def schedule_today(message: Message):
    global week_days, text
    global num_of_week

    today = int(datetime.date.today().weekday())
    with open("schedule/ФККПІ/244/Перша підгрупа.json", "r", encoding='utf-8') as json_file:
        date = json.load(json_file)

    week = list(str(datetime.date.today()).replace('-', ' ').split(' '))
    week_now = datetime.date(int(week[0]), int(week[1]), int(week[2])).isocalendar()[1]
    if week_now % 2 == 0:
        num_of_week = '2'
    else:
        num_of_week = '1'
    if today == 0:
        week_days = 'Пнд'

    if today == 1:
        week_days = 'Втр'

    if today == 2:
        week_days = 'Срд'

    if today == 3:
        week_days = 'Чтв'

    if today == 4:
        week_days = 'Птн'

    if today == 5:
        week_days = 'Сбт'

    if today == 6:
        week_days = 'Нд'



    num_of_lessons = ([x[-1] for x in date['schedule'].keys() if f"{num_of_week}.{week_days}" in x])
    # a = 1
    # b = 0
    # while a <= len(num_of_lessons):
    #     text = (
    #             f'Предмет: {date["schedule"][f"{num_of_week}.{week_days}.{num_of_lessons[b]}"]["discipline"]}\n'
    #             f'Аудиторія:  {date["schedule"][f"{num_of_week}.{week_days}.{num_of_lessons[b]}"]["classroom"]}'
    #
    #         )
    #
    #
    #     a = a + 1
    #     b = b + 1
    t = ''
    for i in num_of_lessons:
        text = (
                f'{emojize(":bell:")} {i} пара\n'
                f'{emojize(":clock7:")} Часи пари\n'
                f'{emojize(":book:")} {date["schedule"][f"{num_of_week}.{week_days}.{i}"]["discipline"]}\n'
                f'{emojize(":office:")} ({date["schedule"][f"{num_of_week}.{week_days}.{i}"]["classroom"]})\n'
                f'{emojize(":hear_no_evil:")} {date["schedule"][f"{num_of_week}.{week_days}.{i}"]["teacher"]}\n\n'
        )
        t += text
    await message.answer(text = t)



@rate_limit(20, 'Завтра')
@dp.message_handler(text="Завтра")
async def schedule_tomorrow(message: Message):
    today = int(datetime.date.today().weekday())
    tomorrow = int(today) + 1
    if tomorrow == 0:
        text = 'Завтра понеділок'
        return await message.answer(text=text)
    if tomorrow == 1:
        text = 'Завтра вівторок'
        return await message.answer(text=text)
    if tomorrow == 2:
        text = 'Завтра середа'
        return await message.answer(text=text)
    if tomorrow == 3:
        text = 'Завтра четверг'
        return await message.answer(text=text)
    if tomorrow == 4:
        text = 'Завтра пятниця'
        return await message.answer(text=text)
    if tomorrow == 5:
        text = 'Завтра субота'
        return await message.answer(text=text)
    if tomorrow == 6:
        text = 'Завтра неділя'
        return await message.answer(text=text)


from aiogram.types import Message
from aiogram.utils.emoji import emojize


@rate_limit(20, 'Розклад')
@dp.message_handler(text='Розклад')
async def schedue(message: Message):
    text = (
        'Розклад')
    await message.answer(text)


@dp.message_handler(text='Розклад дзвінків')
async def serch_schedue(message: Message):
    text = (
        f'{emojize(":bell:")} 1 пара\n{emojize(":eight-thirty:")} 8:00 - 9:35 \n\n'
        f'{emojize(":bell:")} 2 пара\n{emojize(":nine_o’clock:")} 9:50-11:25 \n\n'
        f'{emojize(":bell:")} 3 пара\n{emojize(":twelve_o’clock:")} 11:40 - 13:15\n\n'
        f'{emojize(":bell:")} 4 пара\n{emojize(":one-thirty:")} 13:30-15:05 \n\n'
        f'{emojize(":bell:")} 5 пара\n{emojize(":three-thirty:")} 15:20-16:55 \n\n'
        f'{emojize(":bell:")} 6 пара\n{emojize(":five_o’clock:")} 17:10-18:45 \n\n'
        f'{emojize(":bell:")} 7 пара\n{emojize(":seven_o’clock:")} 19:00-20:35')
    await message.answer(text)


# functional to know num of week
@rate_limit(20, 'Номер неділі')
@dp.message_handler(text="Номер неділі")
async def num_week(message: Message):
    import datetime
    today = str(datetime.date.today())
    week = list(today.replace('-', ' ').split(' '))
    week_now = datetime.date(int(week[0]), int(week[1]), int(week[2])).isocalendar()[1]
    if week_now % 2 == 0:
        await message.answer('Тиждень №2')
    else:
        await message.answer("Тиждень №1")


@rate_limit(20, 'Про бота')
@dp.message_handler(text="Про бота")
async def about(message: Message):
    about = (
        (
            f"Бот, який створений, щоб спростити життя"
            f" студентам і не тільки {emojize(':wink:')}"

            f"\n\nБільше не потрібно використовувати застарілий і незрозумілий сайт, "
            f"щоб дізнатись, чи є завтра пари, доки можна поспати, а, можливо,"
            f" й прогуляти {emojize(':see_no_evil:')}"

            f"\n\nЩось не працює, "
            f"або знаєш як покращити мене?{emojize(':sunglasses:')}"
            f"\nНе соромся, пиши мені [ @falex03 ]."

        )
    )
    await message.answer(text=about, reply_markup=keyboard_about)
