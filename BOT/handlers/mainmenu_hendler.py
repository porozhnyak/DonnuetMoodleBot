from states.form_states import Form
from states.adminform import AdminForm
from aiogram import types
import database
import asyncio
from aiogram.dispatcher import FSMContext
from utils.some_loop import some_loop
from utils.buttons import buttons
from states.activity_states import activity
from aiogram.dispatcher.filters import Text
from utils.grades import all_grades_screen
import os
from aiogram.types import BotCommand, InputFile
from utils.gtlesgrp import parse_page
from credit.config import dp

import logging

# Создаем логгер
logger = logging.getLogger(__name__)


# В файле menu_handlers.py
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
# from credit.config import DONATE_LINK
import database

from credit.config import admmenu_txt_btns, menu_txt_btns

async def handle_main_menu(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    user = await database.get_user(user_id)
    leader = await database.get_user(user_id)
    admin = await database.get_user(user_id)

    
    profile_name = user[3]
    if user:
        command = message.text
        if command == menu_txt_btns[3]:
            await message.answer("Буду благодарен за поддержку.", reply_markup=buttons.donation_button())

            await Form.mainmenu.set()

        elif command == menu_txt_btns[2]:

            user_login = user[1]
            user_password = user[2]
            group = user[7]
            await message.answer("Функция в разработке, но вот все ваши предметы.")
            path = f"lessons_data/{group}.json"

            if os.path.exists(path):  # Проверяем, существует ли файл по указанному пути
                await message.answer(f"Курсы группы: {group}", reply_markup=buttons.lessons_inline_buttons(path))
            else:
                await parse_page(user_login, user_password)  # Парсим страницу и сохраняем данные
                await message.answer(f"Курсы группы: {group}", reply_markup=buttons.lessons_inline_buttons(path))
            await Form.mainmenu.set()
            
        elif command == menu_txt_btns[0]:
            # await handle_grades(message, state)

            await asyncio.sleep(2)
            await message.answer(f"Загружаю таблицу оценок пользователя: {profile_name}")

            user_id = str(message.from_user.id)
            user = await database.get_user(user_id)  
            if user:
                login, password = user[1], user[2]

                result = await all_grades_screen(login, password)
                if result.startswith('Таблица с оценками успешно сохранена'):
                    file = InputFile('grades_table.png')
                    await message.answer_photo(file)
                    os.remove('grades_table.png')
                else:
                    await message.answer(result)
                    
            await Form.mainmenu.set()

        elif command == menu_txt_btns[1]:
            is_active = user[4]
            await message.answer("Функция в разработке. Ошибки не критические.")
            await asyncio.sleep(2)
            if is_active == 1:
                await message.answer("Бот сейчас активен. Нажмите 'СТОП' для остановки активности.", reply_markup=buttons.stop())
                asyncio.create_task(some_loop(user_id))
            else:
                await message.answer("Бот статус не активен. Нажмите 'Старт' для начала активности.", reply_markup=buttons.start())
                await activity.waiting.set()

        elif command == menu_txt_btns[4]:
            await message.answer("Поддержка: @porozhnyack")
            await Form.mainmenu.set()
    else:
        await message.answer("Не удалось найти ваши данные для входа. Пожалуйста, авторизуйтесь заново. /start ")




async def handle_admin_commands(message: types.Message, state: FSMContext):
    command = message.text
    user_id = message.from_user.id

    user = await database.get_user(user_id)
    profile_name = user[3]

    if command == admmenu_txt_btns[0]:
        asyncio.sleep(2)
        await message.answer(f"Загружаю таблицу оценок пользователя: {profile_name}")

        user_id = str(message.from_user.id)
        user = await database.get_user(user_id)  # Предполагается, что есть функция для получения пользователя из БД
        if user:
            login, password = user[1], user[2]

            result = await all_grades_screen(login, password)
            if result.startswith('Таблица с оценками успешно сохранена'):
                file = InputFile('grades_table.png')
                await message.answer_photo(file)
                os.remove('grades_table.png')
            else:
                await message.answer(result)
        await AdminForm.adminmenu.set()

    elif command == admmenu_txt_btns[1]:
        is_active = user[4]
        if is_active == 1:
            await message.answer("Бот сейчас активен. Нажмите 'СТОП' для остановки активности.", reply_markup=buttons.stop())
            asyncio.create_task(some_loop(user_id))
        else:
            await message.answer("Бот статус не активен. Нажмите 'Старт' для начала активности.", reply_markup=buttons.start())
            await activity.waiting.set()

    elif command == admmenu_txt_btns[2]:
        # Логика для второй команды администратора

        user_login = user[1]
        user_password = user[2]
        group = user[7]
        await message.answer("Функция в разработке, но вот все ваши предметы.")
        path = f"lessons_data/{group}.json"

        if os.path.exists(path):  # Проверяем, существует ли файл по указанному пути
            await message.answer(f"Курсы группы: {group}", reply_markup=buttons.lessons_inline_buttons(path))
        else:
            await parse_page(user_login, user_password)  # Парсим страницу и сохраняем данные
            await message.answer(f"Курсы группы: {group}", reply_markup=buttons.lessons_inline_buttons(path))

        await AdminForm.adminmenu.set()

    elif command == admmenu_txt_btns[3]:
        try:
            groups = await database.get_unique_groups()
        
            keyboard = types.InlineKeyboardMarkup(row_width=1)
            for group in groups:
                button = types.InlineKeyboardButton(group, callback_data=f"group_{group}")
                keyboard.add(button)

            await message.answer("Выберите группу:", reply_markup=keyboard)


        except Exception as e:
            logger.exception("An error occurred in assign_leader_start function.")
            await message.answer("Произошла ошибка при попытке назначить старосту. Пожалуйста, попробуйте позже.")

        # groups = await database.get_unique_groups()
        # await message.answer("Функция в разработке. Но вот все зарегистрироанные группы.", reply_markup=buttons.all_groups(groups))
        # await AdminForm.adminmenu.set()

    elif command == admmenu_txt_btns[4]:

        await message.answer("Меню в разработке.")
        # await message.answer("Буду благодарен за поддержку.", reply_markup=buttons.donation_button())
        await AdminForm.adminmenu.set()

    else:
        await message.answer("Не удалось найти ваши данные для входа. Пожалуйста, авторизуйтесь заново. /start ")
    


