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
from handlers.choose_handlers.foradmins_handlers import process_group_choice, process_user_choice


from credit.config import admmenu_txt_btns
from credit.config import menu_txt_btns


dp.middleware.setup(LoggingMiddleware())

async def on_startup(dp):
    # Инициализация базы данных при запуске бота
    await database.init_db()

dp.register_message_handler(start, commands=['start'], state="*")
dp.register_message_handler(handle_main_menu,Text(equals=menu_txt_btns, ignore_case=True), state=Form.mainmenu)
dp.register_message_handler(handle_admin_commands, Text(equals=admmenu_txt_btns, ignore_case=True), state=AdminForm.adminmenu)
dp.register_message_handler(profile_selection)
dp.register_message_handler(get_login, state=Form.login)
dp.register_message_handler(get_password, state=Form.password)
dp.register_message_handler(confirm, state=Form.verification)

dp.register_message_handler(startstop, lambda message: message.text in ['СТОП', 'Продолжить активность', 'Меню'], state=activity.waiting)

# dp.register_message_handler(handle_admin_commands)
dp.register_callback_query_handler(process_group_choice, state=AdminForm.choose_group)
dp.register_callback_query_handler(process_user_choice, state=AdminForm.choose_leader)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)



