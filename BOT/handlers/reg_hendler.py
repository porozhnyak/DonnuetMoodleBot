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

async def get_password(message: types.Message, state: FSMContext):
    
    user_id = str(message.from_user.id)
    async with state.proxy() as data:
        data['password'] = message.text
    user_login = data['login']
    user_password = data['password']
    profile_name = await asyncres.get_profile(user_login, user_password)
    async with state.proxy() as data:
        data['profile_name'] = profile_name
        data['user_id'] = user_id

    # user = await database.get_user(user_id)
    # chek_login = user[2]

    await message.answer(f"Твой аккаунт {profile_name}?", reply_markup=buttons.consent())
    await Form.verification.set()


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

        # chat_id = message.chat.id

        # # await some_loop(chat_id)
        # await database.update_user_active_status(user_id, is_active=1)
        # asyncio.create_task(some_loop(user_id))

        # await activity.waiting.set()
    if message.text == 'Нет':
        await message.answer("Возможно произошла ошибка авторизации. \nПовтори попытку командой /start", reply_markup=None)