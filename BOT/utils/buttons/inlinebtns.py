from aiogram import types
from credit.config import admmenu_txt_btns, menu_txt_btns
import json



def all_groups(groups):
    keyboard = types.InlineKeyboardMarkup(row_width=4)
    for group in groups:
        button_text = f"{group}"
        button = types.InlineKeyboardButton(button_text, callback_data=group)
        keyboard.insert(button)
    return keyboard



def lessons_inline_buttons(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lessons = json.load(file)

    button_list = []
    for title, link in lessons.items():
        button = types.InlineKeyboardButton(title, url=link)
        button_list.append(button)

    inline_kb = types.InlineKeyboardMarkup(row_width=2)  # Устанавливаем row_width
    inline_kb.add(*button_list)  # Добавляем кнопки сразу



def donation_button():
    # Создание инлайн-кнопки с URL
    button = types.InlineKeyboardButton(text="Поддержать", url="https://www.tinkoff.ru/rm/rogovoy.dmitriy20/O3lyY1103")
    keyboard = types.InlineKeyboardMarkup().add(button)
    return keyboard
