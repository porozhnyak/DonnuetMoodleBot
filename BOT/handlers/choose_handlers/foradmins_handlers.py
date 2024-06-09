from states.adminform import AdminForm
from aiogram import types
import database
from utils.buttons import buttons
from aiogram.dispatcher import FSMContext

from credit.config import dp

import logging

# Создаем логгер
logger = logging.getLogger(__name__)

@dp.callback_query_handler(lambda callback_query: callback_query.data.startswith('group_'))
async def process_group_choice(callback_query: types.CallbackQuery):
    try:
        group_name = callback_query.data.split('_')[1]
        users = await database.get_users_by_group(group_name)
        
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        for user in users:
            button = types.InlineKeyboardButton(user[3], callback_data=f"user_{user[0]}")
            keyboard.add(button)
        
        await callback_query.message.edit_text("Выберите старосту из списка пользователей:", reply_markup=keyboard)

    except Exception as e:
        logger.exception("An error occurred in process_group_choice function.")
        await callback_query.message.answer("Произошла ошибка при обработке выбора группы. Пожалуйста, попробуйте позже.")


# Шаг 3: Обработка выбора пользователя
@dp.callback_query_handler(lambda callback_query: callback_query.data.startswith('user_'))
async def process_user_choice(callback_query: types.CallbackQuery):
    try:
        user_id = callback_query.data.split('_')[1]
        group_name = (await dp.bot.get_chat(callback_query.message.chat.id)).title
        await database.assign_leader(user_id, group_name)
        await callback_query.message.edit_text("Староста успешно назначен!")
    except Exception as e:
        logger.exception("An error occurred in process_user_choice function.")
        await callback_query.message.answer("Произошла ошибка при обработке выбора пользователя. Пожалуйста, попробуйте позже.")

    await AdminForm.adminmenu.set()