from aiogram import types

def create_profile_button():
    button = types.KeyboardButton(text="Мой профиль")
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(button)
    return keyboard

async def consent():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(types.KeyboardButton(text="Да")),
    keyboard.add(types.KeyboardButton(text="Нет"))
    return keyboard

def stop():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(types.KeyboardButton(text="СТОП"))
    return keyboard

def start():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(types.KeyboardButton(text="Продолжить активность"))
    keyboard.add(types.KeyboardButton(text="Меню"))
    return keyboard

def authorization(name):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(types.KeyboardButton(text=f"{name}"))
    keyboard.add(types.KeyboardButton(text="Другой профиль"))
    return keyboard

def Mainmenu():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.row(
        types.KeyboardButton(text="Оценки 📖"),
        types.KeyboardButton(text="Активность 🖊")
    )
    keyboard.row(
        types.KeyboardButton(text="Курсы 📅"),
        types.KeyboardButton(text="Поддержать 💸")
    )
    keyboard.add(types.KeyboardButton(text="Помощь 🆘"))
    return keyboard

def donation_button():
    # Создание инлайн-кнопки с URL
    button = types.InlineKeyboardButton(text="Поддержать", url="https://www.tinkoff.ru/rm/rogovoy.dmitriy20/O3lyY1103")
    keyboard = types.InlineKeyboardMarkup().add(button)
    return keyboard

def leadermenu():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=2)
    keyboard.row(
        types.KeyboardButton(text="Оценки 📖"),
        types.KeyboardButton(text="Активность 🖊")
    )
    keyboard.row(
        types.KeyboardButton(text="Расписание 📅"),
        types.KeyboardButton(text="Поддержать 💸")
    )
    # keyboard.add(types.KeyboardButton(text="FAQ"))
    return keyboard

def adminmenu():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.row(
        types.KeyboardButton(text="Оценки 📖"),
        types.KeyboardButton(text="Активность 🖊")
    )
    keyboard.row(
        types.KeyboardButton(text="Расписание 📅"),
        types.KeyboardButton(text="Назначить старосту 👤")
    )
    keyboard.add(types.KeyboardButton(text="Поддержать 💸"))
    # keyboard.add(types.KeyboardButton(text="FAQ"))
    return keyboard

import json

def lessons_inline_buttons(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lessons = json.load(file)

    button_list = []
    for title, link in lessons.items():
        button = types.InlineKeyboardButton(title, url=link)
        button_list.append(button)

    inline_kb = types.InlineKeyboardMarkup(row_width=2)  # Устанавливаем row_width
    inline_kb.add(*button_list)  # Добавляем кнопки сразу

    return inline_kb

def all_groups(groups):
    keyboard = types.InlineKeyboardMarkup(row_width=4)
    for group in groups:
        button_text = f"{group}"
        button = types.InlineKeyboardButton(button_text, callback_data="ignore")
        keyboard.insert(button)
    return keyboard










