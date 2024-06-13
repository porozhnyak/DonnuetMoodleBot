from aiogram import types
from credit.config import admmenu_txt_btns, menu_txt_btns

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
        types.KeyboardButton(text=menu_txt_btns[0]),
        types.KeyboardButton(text=menu_txt_btns[1])
    )
    keyboard.row(
        types.KeyboardButton(text=menu_txt_btns[2]),
        types.KeyboardButton(text=menu_txt_btns[3])
    )
    keyboard.add(types.KeyboardButton(text=menu_txt_btns[4]))
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
        types.KeyboardButton(text=admmenu_txt_btns[0]),
        types.KeyboardButton(text=admmenu_txt_btns[1])
    )
    keyboard.row(
        types.KeyboardButton(text=admmenu_txt_btns[2]),
        types.KeyboardButton(text=admmenu_txt_btns[3])
    )
    keyboard.add(types.KeyboardButton(text=admmenu_txt_btns[4]))
    # keyboard.add(types.KeyboardButton(text="FAQ"))
    return keyboard














