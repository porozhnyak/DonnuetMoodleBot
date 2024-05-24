import database
import asyncio
from utils import asyncres
from credit.config import bot


async def some_loop(user_id):
    counter = 0
    while True:
        user = await database.get_user(user_id)
        if user:
            is_active = user[4]  # Индекс 4 соответствует столбцу is_active в базе данных
            if is_active == 1:
                counter += 1
                user_login, user_password = user[1], user[2]
                await bot.send_message(user_id, await asyncres.ressles(user_login, user_password))
                await asyncio.sleep(30)  # Ждем 30 секунд перед отправкой следующего сообщения
            else:
                break  # Прерываем цикл, если is_active равно 0
        else:
            await bot.send_message(user_id, "Не удалось найти данные пользователя.")
            break  # Прерываем цикл, если не удалось найти пользователя