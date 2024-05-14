import logging
import requests
from aiogram import Bot, Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ParseMode
from aiogram.contrib.fsm_storage.memory import MemoryStorage  # Импортируем MemoryStorage
from BOT.data_us import add_credentials
from BOT.response import get_main
from BOT.data_us import extract_code, add_credentials, save_data, add_data

logging.basicConfig(level=logging.INFO)

API_TOKEN = "6462661850:AAFt4eL23CpawQnzICuCz5tZS5_42k1OyNY"

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())  # Инициализируем Dispatcher с MemoryStorage

class FormStates(StatesGroup):
    WAITING_FOR_LOGIN = State()
    WAITING_FOR_PASSWORD = State()

@dp.message_handler(Command("start"), state="*")
async def send_welcome(message: types.Message, state: FSMContext):

    await state.finish()  # Очистка состояния FSM
    await state.reset_data()  # Очистка данных

    greeting = "Привет!\nЯ бот и я захожу за тебя на площадку Moodle.\nДля начала, давай установим твой логин от Moodle."
    await message.reply(greeting, parse_mode=ParseMode.HTML)
    await FormStates.WAITING_FOR_LOGIN.set()

@dp.message_handler(state=FormStates.WAITING_FOR_LOGIN)
async def handle_login(message: types.Message, state: FSMContext):
    await state.update_data(login=str(message.text))
    await FormStates.WAITING_FOR_PASSWORD.set()
    await message.reply("Отлично! Теперь введи свой пароль от Moodle.")

@dp.message_handler(state=FormStates.WAITING_FOR_PASSWORD)
async def handle_password(message: types.Message, state: FSMContext):
    data = await state.get_data()


    login = data.get("login")
    password = str(message.text)
    
    username = await check_moodle_login(login, password)
    
    group = extract_code(username)

    if username:
        await message.reply(f"Группа {group} зарегистрирована")
        await message.reply(f"Бот аккаунт {username} зарегистрирован")
        # add_data(group, login, password)
    else:
        await message.reply("Неверный логин или пароль. Повторите попытку. Нажми сюда /start")

async def check_moodle_login(login, password):
    return get_main(login, password)

if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)
