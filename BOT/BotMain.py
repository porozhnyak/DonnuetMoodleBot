import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from credit.config_adm import TOKEN
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncres
from buttons import buttons



storage = MemoryStorage()

bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=storage)

user_states = {}
user_credentials = {}
# user_id = message.from_user.id

class Form(StatesGroup):
    login = State()
    password = State()

@dp.message_handler(commands=['start'])
async def start(message: types.Message):

    await message.answer("Привет! Я бот для площадки moodle.")
    await asyncio.sleep(2)
    await message.answer("Что бы начать работу давай авторизуемся.\nВведи свой логин от Moodle")

    await Form.login.set()

    # await message.answer(response.get_profile(user_login, user_password), reply_markup=keyboard)

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

    # Perform login and get profile
    response_message =  await asyncres.get_profile(user_login, user_password)

    await message.answer(response_message, reply_markup=buttons.consent())
    await state.finish()
    
    # await dp.register_message_handler(get_password, state="waiting_for_password", user_id=user_id)


gets = False

@dp.message_handler(lambda message: message.text in ['Да', 'Нет'])
async def handle_response(message: types.Message):

    if message.text == 'Да':
        await message.answer("Хорошо, начинаю работу.")
        await asyncio.sleep(1)
        await message.answer("Если произойдёт ошибка, то нажми кнопку 'СТОП'.", reply_markup=buttons.stop())

        await asyncio.sleep(2)

        chat_id = message.chat.id
        global gets
        gets = True
        # Запускаем цикл в асинхронной функции
        await some_loop(chat_id)

    if message.text == 'Нет':
        await message.answer("Ну нет, так нет.", reply_markup=None)
        return


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


async def some_loop(chat_id):
    global gets
    counter = 0
    while gets:
        counter += 1
        # Выводим определенные сообщения
        await bot.send_message(chat_id, await asyncres.ressles())
        await asyncio.sleep(30)  # Ждем 30 секунд перед отправкой следующего сообщения

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)



