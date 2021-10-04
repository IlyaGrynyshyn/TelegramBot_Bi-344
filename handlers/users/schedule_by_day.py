import datetime
import json

from aiogram.types import Message
from aiogram.utils.emoji import emojize
from aiogram.utils.exceptions import MessageTextIsEmpty

from keyboards.default.about_bot_key import keyboard_about
from keyboards.default.main_menu import main_menu
from loader import dp
from utils.misc import rate_limit
from keyboards.default.schedule_by_day import schedule_by_day
from aiogram.types import Message

with open("schedule/ФККПІ/244/Перша підгрупа.json", "r", encoding='utf-8') as json_file:
    date = json.load(json_file)

lessons_time = {
    '1': "8:00-9:35",
    '2': "9:50-11:25",
    '3': "11:40-13:15",
    '4': "13:30-15:05",
    '5': "15:20-16:55",
    '6': "17:10-18:45",
    '7': "19:00-20:35"

}

@dp.message_handler(text='Розклад')
async def schedue(message: Message):
    text = (
        'Розклад')
    await message.answer(text, reply_markup=schedule_by_day)


@dp.message_handler(text='1.Пнд')
async def first_monday(message: Message):
    day = '1.Пнд'
    num_of_lessons = ([x[-1] for x in date['schedule'].keys() if f"{day}" in x])
    text = ""
    for i in num_of_lessons:
        t = (
            f'{emojize(":bell:")} {i} пари\n'
            f'{emojize(":clock7:")} ({lessons_time[i]})\n'
            f'{emojize(":book:")} {date["schedule"][f"{day}.{i}"]["discipline"]}\n'
            f'{emojize(":office:")} ({date["schedule"][f"{day}.{i}"]["classroom"]})\n'
            f'{emojize(":hear_no_evil:")} {date["schedule"][f"{day}.{i}"]["teacher"]}\n\n'
        )
        text += t
    await message.answer(text=text)


@dp.message_handler(text='1.Втр')
async def first_tuesday(message: Message):
    day = '1.Втр'
    num_of_lessons = ([x[-1] for x in date['schedule'].keys() if f'{day}' in x])
    text = ""
    for i in num_of_lessons:
        t = (
            f'{emojize(":bell:")} {i} пари\n'
            f'{emojize(":clock7:")} ({lessons_time[i]})\n'
            f'{emojize(":book:")} {date["schedule"][f"{day}.{i}"]["discipline"]}\n'
            f'{emojize(":office:")} ({date["schedule"][f"{day}.{i}"]["classroom"]})\n'
            f'{emojize(":hear_no_evil:")} {date["schedule"][f"{day}.{i}"]["teacher"]}\n\n'
        )
        text += t
    await message.answer(text=text)


@dp.message_handler(text='1.Срд')
async def first_wednesday(message: Message):
    day = '1.Срд'
    num_of_lessons = ([x[-1] for x in date['schedule'].keys() if f'{day}' in x])
    text = ""
    for i in num_of_lessons:
        t = (
            f'{emojize(":bell:")} {i} пари\n'
            f'{emojize(":clock7:")} ({lessons_time[i]})\n'
            f'{emojize(":book:")} {date["schedule"][f"{day}.{i}"]["discipline"]}\n'
            f'{emojize(":office:")} ({date["schedule"][f"{day}.{i}"]["classroom"]})\n'
            f'{emojize(":hear_no_evil:")} {date["schedule"][f"{day}.{i}"]["teacher"]}\n\n'
        )
        text += t
    await message.answer(text=text)


@dp.message_handler(text='1.Чтв')
async def first_thursday(message: Message):
    day = '1.Чтв'
    num_of_lessons = ([x[-1] for x in date['schedule'].keys() if f'{day}' in x])
    text = ""
    for i in num_of_lessons:
        t = (
            f'{emojize(":bell:")} {i} пари\n'
            f'{emojize(":clock7:")} ({lessons_time[i]})\n'
            f'{emojize(":book:")} {date["schedule"][f"{day}.{i}"]["discipline"]}\n'
            f'{emojize(":office:")} ({date["schedule"][f"{day}.{i}"]["classroom"]})\n'
            f'{emojize(":hear_no_evil:")} {date["schedule"][f"{day}.{i}"]["teacher"]}\n\n'
        )
        text += t
    await message.answer(text=text)


@dp.message_handler(text='1.Птн')
async def first_friday(message: Message):
    day = '1.Птн'
    num_of_lessons = ([x[-1] for x in date['schedule'].keys() if f'{day}' in x])
    text = ""
    for i in num_of_lessons:
        t = (
            f'{emojize(":bell:")} {i} пари\n'
            f'{emojize(":clock7:")} ({lessons_time[i]})\n'
            f'{emojize(":book:")} {date["schedule"][f"{day}.{i}"]["discipline"]}\n'
            f'{emojize(":office:")} ({date["schedule"][f"{day}.{i}"]["classroom"]})\n'
            f'{emojize(":hear_no_evil:")} {date["schedule"][f"{day}.{i}"]["teacher"]}\n\n'
        )
        text += t
    await message.answer(text=text)


""" 
Розклад другого тижня
"""


@dp.message_handler(text='2.Пнд')
async def first_monday(message: Message):
    day = '2.Пнд'
    num_of_lessons = ([x[-1] for x in date['schedule'].keys() if f"{day}" in x])
    text = ""
    for i in num_of_lessons:
        t = (
            f'{emojize(":bell:")} {i} пари\n'
            f'{emojize(":clock7:")} ({lessons_time[i]})\n'
            f'{emojize(":book:")} {date["schedule"][f"{day}.{i}"]["discipline"]}\n'
            f'{emojize(":office:")} ({date["schedule"][f"{day}.{i}"]["classroom"]})\n'
            f'{emojize(":hear_no_evil:")} {date["schedule"][f"{day}.{i}"]["teacher"]}\n\n'
        )
        text += t
    await message.answer(text=text)


@dp.message_handler(text='2.Втр')
async def first_tuesday(message: Message):
    day = '2.Втр'
    num_of_lessons = ([x[-1] for x in date['schedule'].keys() if f'{day}' in x])
    text = ""
    for i in num_of_lessons:
        t = (
            f'{emojize(":bell:")} {i} пари\n'
            f'{emojize(":clock7:")} ({lessons_time[i]})\n'
            f'{emojize(":book:")} {date["schedule"][f"{day}.{i}"]["discipline"]}\n'
            f'{emojize(":office:")} ({date["schedule"][f"{day}.{i}"]["classroom"]})\n'
            f'{emojize(":hear_no_evil:")} {date["schedule"][f"{day}.{i}"]["teacher"]}\n\n'
        )
        text += t
    await message.answer(text=text)


@dp.message_handler(text='2.Срд')
async def first_wednesday(message: Message):
    day = '2.Срд'
    num_of_lessons = ([x[-1] for x in date['schedule'].keys() if f'{day}' in x])
    text = ""
    for i in num_of_lessons:
        t = (
            f'{emojize(":bell:")} {i} пари\n'
            f'{emojize(":clock7:")} ({lessons_time[i]})\n'
            f'{emojize(":book:")} {date["schedule"][f"{day}.{i}"]["discipline"]}\n'
            f'{emojize(":office:")} ({date["schedule"][f"{day}.{i}"]["classroom"]})\n'
            f'{emojize(":hear_no_evil:")} {date["schedule"][f"{day}.{i}"]["teacher"]}\n\n'
        )
        text += t
    await message.answer(text=text)


@dp.message_handler(text='2.Чтв')
async def first_thursday(message: Message):
    day = '2.Чтв'
    num_of_lessons = ([x[-1] for x in date['schedule'].keys() if f'{day}' in x])
    text = ""
    for i in num_of_lessons:
        t = (
            f'{emojize(":bell:")} {i} пари\n'
            f'{emojize(":clock7:")} ({lessons_time[i]})\n'
            f'{emojize(":book:")} {date["schedule"][f"{day}.{i}"]["discipline"]}\n'
            f'{emojize(":office:")} ({date["schedule"][f"{day}.{i}"]["classroom"]})\n'
            f'{emojize(":hear_no_evil:")} {date["schedule"][f"{day}.{i}"]["teacher"]}\n\n'
        )
        text += t
    await message.answer(text=text)


@dp.message_handler(text='2.Птн')
async def first_friday(message: Message):
    day = '2.Птн'
    num_of_lessons = ([x[-1] for x in date['schedule'].keys() if f'{day}' in x])
    text = ""
    for i in num_of_lessons:
        t = (
            f'{emojize(":bell:")} {i} пари\n'
            f'{emojize(":clock7:")} ({lessons_time[i]})\n'
            f'{emojize(":book:")} {date["schedule"][f"{day}.{i}"]["discipline"]}\n'
            f'{emojize(":office:")} ({date["schedule"][f"{day}.{i}"]["classroom"]})\n'
            f'{emojize(":hear_no_evil:")} {date["schedule"][f"{day}.{i}"]["teacher"]}\n\n'
        )
        text += t
    await message.answer(text=text)
