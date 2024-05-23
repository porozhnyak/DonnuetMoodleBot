from aiogram import types

def create_profile_button():
    button = types.KeyboardButton(text="Мой профиль")
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(button)
    return keyboard

def consent():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(types.KeyboardButton(text="Да"))
    keyboard.add(types.KeyboardButton(text="Нет"))
    return keyboard

def stop():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(types.KeyboardButton(text="СТОП"))
    return keyboard

def start():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(types.KeyboardButton(text="Старт"))
    return keyboard

def authorization(name):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(types.KeyboardButton(text=f"{name}"))
    keyboard.add(types.KeyboardButton(text="Другой профиль"))
    return keyboard



