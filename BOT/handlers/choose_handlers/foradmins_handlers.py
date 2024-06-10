from states.adminform import AdminForm
from aiogram import types
import database
from utils.buttons import buttons
from aiogram.dispatcher import FSMContext

from credit.config import dp

import logging

# Создаем логгер
logger = logging.getLogger(__name__)

# Шаг 2: Обработка выбора группы
@dp.callback_query_handler(state=AdminForm.choose_group)
async def process_group_choice(callback_query: types.CallbackQuery, state: FSMContext):
    try:
        group_name = callback_query.data
        logger.info(f"Group selected: {group_name}")
        await state.update_data(chosen_group=group_name)
        
        users = await database.get_users_by_group(group_name)
        logger.info(f"Users in group {group_name}: {users}")
        
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        for user in users:
            button = types.InlineKeyboardButton(user[3], callback_data=f"user_{user[0]}")
            keyboard.add(button)
        
        await callback_query.message.edit_text("Выберите старосту из списка пользователей:", reply_markup=keyboard)
        await AdminForm.choose_leader.set()
    except Exception as e:
        logger.exception("An error occurred in process_group_choice function.")
        await callback_query.message.answer("Произошла ошибка при обработке выбора группы. Пожалуйста, попробуйте позже.")

# Шаг 3: Обработка выбора пользователя
@dp.callback_query_handler(state=AdminForm.choose_leader)
async def process_user_choice(callback_query: types.CallbackQuery, state: FSMContext):
    try:
        user_id = callback_query.data
        data = await state.get_data()
        group_name = data.get('chosen_group')
        
        logger.info(f"User selected: {user_id} for group: {group_name}")
        await database.assign_leader(user_id, group_name)
        await callback_query.message.edit_text("Староста успешно назначен!")
        await AdminForm.adminmenu.set()
    except Exception as e:
        logger.exception("An error occurred in process_user_choice function.")
        await callback_query.message.answer("Произошла ошибка при обработке выбора пользователя. Пожалуйста, попробуйте позже.")
        await state.finish()