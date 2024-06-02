import aiohttp
import asyncio
from bs4 import BeautifulSoup
import json

async def login(user_login, user_password, log_url):
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
                    print("Logged in successfully")
                    return session.cookie_jar.filter_cookies(log_url)  # Вернуть куки
                else:
                    print("Failed to log in")
                    return None

async def get_page(log, url):
    try:
        async with aiohttp.ClientSession(cookies=log) as session:
            async with session.get(url) as profile_response:
                if profile_response.status != 200:
                    print(f"Error fetching profile page: {profile_response.status}")
                    return None

                return await profile_response.text()
    except Exception as e:
        print(f"Error in profile function: {e}")
        return None


async def parse_page(user_login, user_password, log_url, url):
    cookies = await login(user_login, user_password, log_url)
    if cookies:
        page_content = await get_page(cookies, url)
        if page_content:
            soup = BeautifulSoup(page_content, 'html.parser')
            lesson_dict = {}
            for card in soup.find_all('li'):
                lesson_title_element = card.find('span', class_='media-body')
                lesson_link_element = card.find('a', class_='list-group-item list-group-item-action')
                if lesson_title_element and lesson_link_element:
                    lesson_title = lesson_title_element.get_text(strip=True)
                    if lesson_title not in ['Личный кабинет', 'В начало', 'Календарь', 'Личные файлы']:
                        lesson_link = lesson_link_element['href']
                        lesson_dict[lesson_title] = lesson_link


            with open('lessons.json', 'w', encoding='utf-8') as file:
                json.dump(lesson_dict, file, ensure_ascii=False, indent=4)
            return lesson_dict
        else:
            print("Ошибка получения контента страницы")
            return None
    else:
        print("Ошибка аутентификации")
        return None




# Пример использования
async def main():
    url = 'https://distant.donnuet.ru/?redirect=0'
    user_login = ""
    user_password = ""
    log_url = 'https://distant.donnuet.ru/login/index.php'
    
    lessons = await parse_page(user_login, user_password, log_url, url)
    if lessons:
        print("Успешно получены данные:")
        for title, link in lessons.items():
            print(f"Название урока: {title}, Ссылка: {link}")
    else:
        print("Не удалось получить данные")

# Запуск асинхронного кода
asyncio.run(main())

