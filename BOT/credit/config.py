from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from dotenv import load_dotenv
import os


log_url = "https://distant.donnuet.ru/login/index.php"
profile_link = "https://distant.donnuet.ru/my/"
grade_link = "https://distant.donnuet.ru/grade/report/overview/index.php"
main_link = "https://distant.donnuet.ru/?redirect=0"

agreement = "https://telegra.ph/Polzovatelskoe-soglashenie-MoodleBot-06-07"

storage = MemoryStorage()

load_dotenv()
TOKEN = os.getenv("TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=storage)

admmenu_txt_btns = ["Оценки 📖", "Активность 🖊", "Курсы 📅", "Назначить старосту 👤", "Меню администратора 🔑"]
menu_txt_btns = ["Оценки 📖", "Активность 🖊", "Курсы 📅", "Поддержать 💸", "Помощь 🆘"]