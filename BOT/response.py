import requests
from fake_useragent import UserAgent
import time
from bs4 import BeautifulSoup
import datetime
import GetLessonsLink

import aiohttp

import asyncio

# user_login = "10.rdo"
# user_password = "Stud_2021"

URL = "https://distant.donnuet.ru" 
log_url = URL+"/login/index.php"
profile_link = "https://distant.donnuet.ru/my/"


#Заголовки
ua = UserAgent()
rand_ua = ua.random
headers = {
    "User-Agent": rand_ua
}


session = requests.Session()
session2 = requests.Session()

# today = datetime.datetime.today().isoweekday()# Выводит номер дня недели (1-Понедельник ... 7-Воскресенье)
# TimeNow = datetime.datetime.today().strftime('%H:%M')

async def login(user_login, user_password):
    session.headers.update(headers)

    res = session.get(log_url)
    soup = BeautifulSoup(res.content, 'html.parser')

    data = {
        'anchor': '',
        'logintoken': soup.find('input', {"name": "logintoken"}).get("value"),
        "username" : user_login,
        "password" : user_password,
    }
    
    session.post(log_url, data=data, headers=headers)
    

 

async def profile():

    cookies_dict = [
        {"domain": key.domain, "name": key.name, "path": key.path, "value": key.value}
        for key in session.cookies
    ]

    for cookies in cookies_dict:
        session2.cookies.set(**cookies)

    profile_response = session2.get(profile_link, headers=headers)


    # f = open('results.html', 'w', encoding='utf8')
    # f.write(profile.text)
    # f.close()

    return profile_response

async def get_profile(user_login, user_password):
    try:
        
        session = await login(user_login, user_password)
        # prof = profile()
        profile_response = await profile()
        
        soup = BeautifulSoup(profile_response.text, 'html.parser')
        unlog = soup.find('span', class_ = 'login') #Переменная отвечающая за вход в систему, если есть, то бот не вошёл в систему
        log = soup.find('span', class_ = "usertext mr-1").text


        return f"Твой аккаунт {log}?"
    except Exception as e:
        return f"Ошибка логина: {e}"
            
async def resless(): #запросы на уроки
    try:


        link = await GetLessonsLink.GetLessonsLink(today, TimeNow)
        if link is None:
            print("Ссылка None")

        res =  session2.get(link, headers=headers)
        if res is None:
            print("Запрос none")
        else: 
            res

        soup = BeautifulSoup(res.text, 'html.parser')
        name_course = soup.find('div', class_ = 'page-header-headings').text
        name_user = soup.find('span', class_ = 'usertext mr-1').text


 
        return f"Бот-аккаунт {name_user} на курсе : {name_course} "
        # return name_user
    except Exception as e:
        return f"Ошибка запроса урока {e}"
    # except Exception as e:
    #     if e is not None:
    #         return f'Ошибка: {e}'
    #     else:   
    #         pass

    




# async def req_answ():


#     global today, TimeNow   
#     today = datetime.datetime.today().isoweekday()# Выводит номер дня недели (1-Понедельник ... 7-Воскресенье)
#     TimeNow = datetime.datetime.today().strftime('%H:%M')
#     while True:
#         await get_profile(user_login, user_password)
#         print( await resless())

#         time.sleep(5)

# asyncio.run(req_answ())