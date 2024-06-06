import aiohttp
import asyncio
from bs4 import BeautifulSoup
import json
from utils.parse_utils import group_name
import os
from utils import asyncres
from utils.parse_utils import getpage
from credit.config import log_url, main_link
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def parse_page(user_login, user_password):
    cookies = await asyncres.login(user_login, user_password)
    if cookies:
        page_content = await getpage.get_page(cookies, main_link)
        if page_content:
            soup = BeautifulSoup(page_content, 'html.parser')
            lesson_dict = {}
            profile_name = soup.find('span', class_ = 'usertext mr-1').get_text(strip=True)
            for card in soup.find_all('li'):
                lesson_title_element = card.find('span', class_='media-body')
                lesson_link_element = card.find('a', class_='list-group-item list-group-item-action')
                if lesson_title_element and lesson_link_element:
                    lesson_title = lesson_title_element.get_text(strip=True)
                    if lesson_title not in ['Личный кабинет', 'В начало', 'Календарь', 'Личные файлы']:
                        lesson_link = lesson_link_element['href']
                        lesson_dict[lesson_title] = lesson_link

            if lesson_dict:
                last_key = list(lesson_dict.keys())[-1]
                lesson_dict.pop(last_key)

            folder_name = 'lessons_data'
            if not os.path.exists(folder_name):
                os.makedirs(folder_name)

            # Сохранение в файл
            
            file_path = os.path.join(folder_name, f"{await group_name.extract_group(profile_name)}.json")
            with open(file_path, 'w', encoding='utf-8') as file:
                json.dump(lesson_dict, file, ensure_ascii=False, indent=4)
            logger.info(f"Lesson data saved to {file_path}")
            return lesson_dict


        #     with open(f'lessons_data/lessons {await group_name.extract_group(profile_name)}.json', 'w', encoding='utf-8') as file:
        #         json.dump(lesson_dict, file, ensure_ascii=False, indent=4)
        #     return lesson_dict
        # else:
        logger.error("Ошибка получения контента страницы")
        return None
    else:
        logger.error("Ошибка аутентификации")
        return None




# Пример использования
# async def main():
#     url = 'https://distant.donnuet.ru/?redirect=0'
#     user_login = ""
#     user_password = ""
#     log_url = 'https://distant.donnuet.ru/login/index.php'
    
#     lessons = await parse_page(user_login, user_password, log_url, url)
#     if lessons:
#         print("Успешно получены данные:")
#         for title, link in lessons.items():
#             print(f"Название урока: {title}, Ссылка: {link}")
#     else:
#         print("Не удалось получить данные")

# # Запуск асинхронного кода
# asyncio.run(main())

