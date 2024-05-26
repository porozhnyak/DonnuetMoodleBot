from aiogram import types
import database
from utils.some_loop import some_loop
from utils.buttons import buttons
import asyncio
from states.form_states import Form

async def startstop(message: types.Message):

    if message.text == "СТОП":
        user_id=message.from_user.id
        await database.update_user_active_status(user_id, 0)
        await message.answer("Бот приостановлен", reply_markup=buttons.start())


    if message.text == "Продолжить активность":
        user_id = str(message.from_user.id)
        # Устанавливаем статус is_active в True при возобновлении цикла
        await database.update_user_active_status(user_id, is_active=1)

        await message.answer("Работа бота возоблена", reply_markup=buttons.stop())
        asyncio.create_task(some_loop(user_id))

    if message.text == "Меню":
        user_id = str(message.from_user.id)
        user = await database.get_user(user_id)
        profile_name = user[3]


        await message.answer(f"Меню профиля: {profile_name} 👤", reply_markup=buttons.Mainmenu())
        await Form.mainmenu.set()