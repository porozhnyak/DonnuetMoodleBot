from aiogram import types
from aiogram.dispatcher import FSMContext
from utils import asyncres
from utils.buttons import buttons
from states.form_states import Form
import database
import asyncio
from states.activity_states import activity
from utils.some_loop import some_loop
from states.adminform import AdminForm

import sys
sys.setrecursionlimit(2000)

import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

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


async def get_password(message: types.Message, state: FSMContext):
    try:
        user_id = str(message.from_user.id)
        logger.info(f"User {user_id} is attempting to set a password.")
        
        async with state.proxy() as data:
            data['password'] = message.text
            user_login = data['login']
            user_password = data['password']
            logger.info(f"Retrieved login: {user_login} and password: {user_password} from state proxy.")

        profile_name = await asyncres.get_profile(user_login, user_password)
        logger.info(f"Profile name retrieved for user {user_id}: {profile_name}")
        
        async with state.proxy() as data:
            data['profile_name'] = profile_name
            data['user_id'] = user_id
            logger.info(f"State updated with profile_name: {profile_name} and user_id: {user_id}")

        await message.answer(f"Твой аккаунт {profile_name}?", reply_markup= await buttons.consent())
        await Form.verification.set()
        logger.info(f"User {user_id} moved to verification state.")

    except RecursionError as e:
        await message.answer("Произошла ошибка: превышена глубина рекурсии.")
        logger.error("RecursionError: Превышена глубина рекурсии.", exc_info=True)
    except Exception as e:
        await message.answer("Произошла неизвестная ошибка.")
        logger.error("Неизвестная ошибка.", exc_info=True)


async def get_login(message: types.Message, state: FSMContext):
    user_id = str(message.from_user.id)
    user = await database.get_user(user_id)
    
    async with state.proxy() as data:
        data['login'] = message.text
    await message.answer("Теперь введи свой пароль:")
    await Form.password.set()

async def confirm(message: types.Message, state: FSMContext):

    async with state.proxy() as data:
        profile_name = data.get('profile_name')
        user_id = data.get('user_id')
        user_login = data['login']
        user_password = data['password']

    if message.text == 'Да':

        if int(user_id) == 953420910:
            await message.answer("Вы определены как администратор.", reply_markup=buttons.adminmenu())
            await database.save_user(str(user_id), user_login, user_password, profile_name)
            await database.update_user_admin_status(user_id, 1)

            await AdminForm.adminmenu.set()
        else:
            await database.save_user(user_id, user_login, user_password, profile_name)
            # await database.update_user_active_status(user_id, 0)
            await message.answer("Профиль зарегистрирован.")

            await asyncio.sleep(1)
            await message.answer(f"Меню профиля: {profile_name} 👤", reply_markup=buttons.Mainmenu())

            await Form.mainmenu.set()
    if message.text == 'Нет':
        await message.answer("Возможно произошла ошибка авторизации. \nПовтори попытку командой /start", reply_markup=None)