import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.utils import executor
import response
from config_act import user_login, user_password
from credit.TOKEN import TOKEN


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

user_states = {}
# user_id = message.from_user.id

@dp.message_handler(commands=['start'])
async def start(message: types.Message):


    # dp.message_handlers.clear()
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(types.KeyboardButton(text="Да"))
    keyboard.add(types.KeyboardButton(text="Нет"))
    # Запускаем цикл в асинхронной функции

    await message.answer("Привет! Я бот для площадки moodle.")
    await message.answer(response.get_profile(user_login, user_password), reply_markup=keyboard)


gets = False

@dp.message_handler(lambda message: message.text in ['Да', 'Нет'])
async def handle_response(message: types.Message):

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(types.KeyboardButton(text="СТОП"))

    if message.text == 'Да':
        await message.answer("Хорошо, начинаю работу.")
        await asyncio.sleep(1)
        await message.answer("Если произойдёт ошибка, то нажми кнопку 'СТОП'.", reply_markup=keyboard)

        await asyncio.sleep(2)


        global gets
        gets = True
        # Запускаем цикл в асинхронной функции
        await some_loop(message.chat.id)

    if message.text == 'Нет':
        await message.answer("Ну нет, так нет.", reply_markup=None)
        return


@dp.message_handler(lambda message: message.text in ['СТОП'])
async def stop_res(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(types.KeyboardButton(text="Старт"))

    if message.text == "СТОП":
        global gets
        gets = False
        await message.answer("Бот приостановлен", reply_markup=keyboard)


@dp.message_handler(lambda message: message.text in ['Старт'])
async def stop_res(message: types.Message):

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(types.KeyboardButton(text="СТОП"))

    if message.text == "Старт":
        global gets
        gets = True
        await message.answer("Работа бота возоблена", reply_markup=keyboard)
        await some_loop(message.chat.id)


async def some_loop(chat_id):
    global gets
    counter = 0
    while gets:
        counter += 1
        # Выводим определенные сообщения
        await bot.send_message(chat_id, response.resless())
        await asyncio.sleep(30)  # Ждем 30 секунд перед отправкой следующего сообщения

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)



