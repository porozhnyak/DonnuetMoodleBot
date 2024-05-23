import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from credit.config import TOKEN
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncres
from buttons import buttons
import database



storage = MemoryStorage()

bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=storage)

user_states = {}
user_credentials = {}
# user_id = message.from_user.id

class Form(StatesGroup):
    start = State()
    login = State()
    password = State()
    verification = State()

async def on_startup(dp):
    # Инициализация базы данных при запуске бота
    await database.init_db()

@dp.message_handler(commands=['start'], state="*")
async def start(message: types.Message, state: FSMContext):

    await state.finish()

    user_id = message.from_user.id
    user = await database.get_user(user_id)

    if user:
        login, password, profile_name = user[1], user[2], user[3]
        await message.answer(f"Привет! Выбери действие: ", reply_markup=buttons.authorization(profile_name))
        # код в разработке
    else:
        await message.answer("Привет! Я бот для площадки moodle.")
        await asyncio.sleep(2)
        await message.answer("Что бы начать работу давай авторизуемся.")
        await asyncio.sleep(2)
        await message.answer("Введи свой логин от Moodle")
        await Form.login.set()

@dp.message_handler(state=Form.login)
async def get_login(message: types.Message, state: FSMContext):
    user_id = str(message.from_user.id)

    async with state.proxy() as data:
        data['login'] = message.text

    await message.answer("Теперь введи свой пароль:")
    await Form.next()

@dp.message_handler(state=Form.password)
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

    await message.answer(f"Твой аккаунт {profile_name}?", reply_markup=buttons.consent())

    await Form.verification.set()

gets = False

# @dp.message_handler(lambda message: message.text in ['Да', 'Нет'])
@dp.message_handler(state=Form.verification)
async def handle_response(message: types.Message, state: FSMContext):

    async with state.proxy() as data:
        profile_name = data.get('profile_name')
        user_id = data.get('user_id')
        user_login = data['login']
        user_password = data['password']
    if message.text == 'Да':
        
        await database.save_user(user_id, user_login, user_password, profile_name)
        await message.answer("Хорошо, начинаю работу.")
        await asyncio.sleep(1)
        await message.answer("Если произойдёт ошибка, то нажми кнопку 'СТОП'.", reply_markup=buttons.stop())

        chat_id = message.chat.id
        global gets
        gets = True
        # Запускаем цикл в асинхронной функции
        await some_loop(chat_id)

    if message.text == 'Нет':
        await message.answer("Возможно произошла ошибка авторизации. \nПовтори попытку командой /start", reply_markup=None)
    


@dp.message_handler(lambda message: message.text in ['СТОП'])
async def stop_res(message: types.Message):

    if message.text == "СТОП":
        global gets
        gets = False
        await message.answer("Бот приостановлен", reply_markup=buttons.start())


@dp.message_handler(lambda message: message.text in ['Старт'])
async def stop_res(message: types.Message):

    if message.text == "Старт":
        global gets
        gets = True
        await message.answer("Работа бота возоблена", reply_markup=buttons.stop())
        await some_loop(message.chat.id)


async def some_loop(user_id):
    global gets
    counter = 0
    while gets:
        counter += 1
        # Получаем учетные данные пользователя из базы данных
        user = await database.get_user(user_id)
        if user:
            user_login, user_password = user[1], user[2]
            # Выводим определенные сообщения
            await bot.send_message(user_id, await asyncres.ressles(user_login, user_password))
        else:
            await bot.send_message(user_id, "Не удалось найти данные пользователя.")
        
        await asyncio.sleep(30)  # Ждем 30 секунд перед отправкой следующего сообщения


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)



