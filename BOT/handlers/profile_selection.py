from states.form_states import Form
from aiogram import types
import database
import asyncio
from aiogram.dispatcher import FSMContext
from utils.buttons import buttons
from states.adminform import AdminForm

async def profile_selection(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    user = await database.get_user(user_id)
    if user:
        profile_name = user[3]
        if message.text == profile_name:

            if user[6] == 1:
                await message.answer(f"Вы вошли как Администратор: {profile_name}", reply_markup=buttons.adminmenu())
                await AdminForm.adminmenu.set()
            elif user[5] == 1:
                await message.answer(f"Вы вошли как Староста: {profile_name}", reply_markup=buttons.leadermenu())
                await AdminForm.adminmenu.set()
            else:
                await message.answer(f"Вы вошли как {profile_name}", reply_markup=buttons.Mainmenu())
                await asyncio.sleep(1)
                await Form.mainmenu.set()
        elif message.text == "Другой профиль":
            await message.answer("Введите новый логин:")
            await Form.login.set()