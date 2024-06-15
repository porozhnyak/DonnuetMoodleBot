import aiohttp
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import datetime
import GetLessonsLink
from credit.config import log_url, profile_link
import asyncio
import datetime
import logging

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('response')

#Заголовки
ua = UserAgent()
rand_ua = ua.random
headers = {
    "User-Agent": rand_ua
}

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('response')

async def login(user_login, user_password):
    async with aiohttp.ClientSession() as session:
        async with session.get(log_url) as res:
            soup = BeautifulSoup(await res.text(), 'html.parser')
            logintoken = soup.find('input', {"name": "logintoken"}).get("value")

            data = {
                'anchor': '',
                'logintoken': logintoken,
                'username': user_login,
                'password': user_password,
            }

            async with session.post(log_url, data=data) as log_res:
                if log_res.status == 200:
                    logger.info("Logged in successfully")
                    return session.cookie_jar.filter_cookies(log_url)  # Вернуть куки
                else:
                    logger.error("Failed to log in")
                    return None

async def profile(cookies):
    try:
        async with aiohttp.ClientSession(cookies=cookies) as session:
            async with session.get(profile_link) as profile_response:
                if profile_response.status != 200:
                    logger.error(f"Error fetching profile page: {profile_response.status}")
                    return None

                return await profile_response.text()
    except Exception as e:
        logger.error(f"Error in profile function: {e}")
        return None

async def get_profile(user_login, user_password):
    try:
        cookies = await login(user_login, user_password)
        if cookies:
            profile_data = await profile(cookies)
            if profile_data:
                soup = BeautifulSoup(profile_data, 'html.parser')
                unlog = soup.find('span', class_='login')
                if unlog:
                    logger.error("User is not logged in")
                    return "Ошибка логина: Пользователь не вошел в систему"
                log = soup.find('span', class_="usertext mr-1").text
                return f"{log}"
            else:
                logger.error("Failed to fetch profile data")
                return "Ошибка логина: Не удалось получить данные профиля"
        else:
            logger.error("Login failed")
            return "Ошибка логина: Не удалось войти в систему"
    except Exception as e:
        logger.error(f"Error in get_profile: {e}")
        return f"Ошибка логина: {e}"

async def ressles(user_login, user_password):
    try:
        today = str(datetime.datetime.today().isoweekday())# Выводит номер дня недели (1-Понедельник ... 7-Воскресенье)
        TimeNow = str(datetime.datetime.today().strftime('%H:%M'))
        lessons_link = await GetLessonsLink.GetLessonsLink(today, TimeNow)
        cookies = await login(user_login, user_password)

        if lessons_link is None:
            logger.error("No lessons link found for the given day and time.")
            return 

        if cookies:
            async with aiohttp.ClientSession(cookies=cookies) as session:
                async with session.get(lessons_link) as res:
                    if res.status != 200:
                        logger.error(f"Error fetching lessons page: {res.status}")
                        return None

                    soup = BeautifulSoup(await res.text(), 'html.parser')
                    name_course = soup.find('div', class_='page-header-headings').text
                    name_user = soup.find('span', class_='usertext mr-1').text

                    return f"Бот-аккаунт {name_user} на курсе: {name_course}"
        else:
            logger.error("Login failed")
            return "Ошибка логина: Не удалось войти в систему"
    except Exception as e:
        logger.error(f"Error in ressles function: {e}")
        return f"Ошибка запроса урока: {e}"