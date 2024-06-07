from aiogram.utils import executor
from credit.config import TOKEN, dp, storage
from aiogram.dispatcher.filters import Text
from aiogram.contrib.middlewares.logging import LoggingMiddleware

import database
from states.form_states import Form
from states.activity_states import activity
from states.adminform import AdminForm

from handlers.profile_selection import profile_selection
from handlers.startstop_hendler import startstop
from handlers.reg_hendler import get_password, get_login, confirm
from handlers.start_hendler import start
from handlers.mainmenu_hendler import handle_main_menu, handle_admin_commands

import sys
sys.setrecursionlimit(2000)


import logging

# Настройка логгера для записи в файл
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(name)s %(levelname)s:%(message)s',
    handlers=[
        logging.FileHandler("app.log", mode='w'),  # Перезаписываем лог при каждом запуске
        logging.StreamHandler()
    ]
)

def get_logger(name: str):
    return logging.getLogger(name)


dp.middleware.setup(LoggingMiddleware())

async def on_startup(dp):
    # Инициализация базы данных при запуске бота
    await database.init_db()

dp.register_message_handler(start, commands=['start'], state="*")
dp.register_message_handler(handle_main_menu,Text(equals=["Оценки 📖", "Активность 🖊", "Курсы 📅", "Поддержать 💸", "Помощь 🆘"], ignore_case=True), state=Form.mainmenu)
dp.register_message_handler(handle_admin_commands, Text(equals=["Оценки 📖", "Назначить старосту 👤", "Расписание 📅", "Активность 🖊", "Поддержать 💸"],ignore_case=True), state=AdminForm.adminmenu)
dp.register_message_handler(profile_selection)
dp.register_message_handler(get_login, state=Form.login)
dp.register_message_handler(get_password, state=Form.password)
dp.register_message_handler(confirm, state=Form.verification)
dp.register_message_handler(startstop, lambda message: message.text in ['СТОП', 'Продолжить активность', 'Меню'], state=activity.waiting)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)



