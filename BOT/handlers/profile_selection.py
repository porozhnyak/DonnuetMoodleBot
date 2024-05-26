from states.form_states import Form
from aiogram import types
import database
import asyncio
from aiogram.dispatcher import FSMContext
from utils.some_loop import some_loop
from utils.buttons import buttons
from states.activity_states import activity


async def profile_selection(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    user = await database.get_user(user_id)
    if user:
        profile_name = user[3]
        if message.text == profile_name:
            await message.answer(f"Вы вошли как {profile_name}", reply_markup=buttons.Mainmenu())

            await asyncio.sleep(1)

            await Form.mainmenu.set()
            # if user[4] == 0:
            #     await database.update_user_active_status(user_id, 1)
            #     await message.answer("Бот аккаунт активирован.")
            #     await asyncio.sleep(2)
            #     await message.answer("Если произойдёт ошибка, то нажми кнопку 'СТОП'.")
                
            #     asyncio.create_task(some_loop(user_id))
            # else:
            #     await message.answer("Продолжаю работу.")
            #     asyncio.create_task(some_loop(user_id))
            # await activity.waiting.set()
        elif message.text == "Другой профиль":
            await message.answer("Введите новый логин:")
            await Form.login.set()