from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import InputFile
import os
import database
from states.form_states import Form
from utils.grades import all_grades_screen

# @dp.message_handler(state=Form.grades_url)
async def handle_grades(message: types.Message, state: FSMContext):
    user_id = str(message.from_user.id)
    
    user = await database.get_user(user_id)
    if user:
        login, password = user[1], user[2]

        # Выгрузка таблицы в виде скриншота
        result = await all_grades_screen(login, password)

        if result.startswith('Таблица с оценками успешно сохранена'):
            file = InputFile('grades_table.png')
            await message.answer_document(file)
            os.remove('grades_table.png')
        else:
            await message.answer(result)
    else:
        await message.answer("Не удалось найти ваши данные для входа.")
    
    await state.finish()
