from aiogram.utils import executor
from credit.config import TOKEN, dp, storage
from aiogram.dispatcher.filters import Text

import database
from states.form_states import Form
from states.activity_states import activity

from handlers.profile_selection import profile_selection
from handlers.startstop_hendler import startstop
from handlers.reg_hendler import get_password, get_login, confirm
from handlers.start_hendler import start
from handlers.mainmenu_hendler import handle_main_menu

async def on_startup(dp):
    # Инициализация базы данных при запуске бота
    await database.init_db()

dp.register_message_handler(start, commands=['start'], state="*")

dp.register_message_handler(handle_main_menu,Text(equals=["Оценки 📖", "Активность 🖊", "Поддержать 💸"], ignore_case=True), state=Form.mainmenu)

dp.register_message_handler(profile_selection)

dp.register_message_handler(get_login, state=Form.login)

dp.register_message_handler(get_password, state=Form.password)

dp.register_message_handler(confirm, state=Form.verification)

dp.register_message_handler(startstop, lambda message: message.text in ['СТОП', 'Продолжить активность', 'Меню'], state=activity.waiting)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)



