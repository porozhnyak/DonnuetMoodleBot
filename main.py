import requests
from fake_useragent import UserAgent
import time
from bs4 import BeautifulSoup
import datetime
import os


try:
    from config_act import user_login, user_password
    with open('config_act.py', 'r', encoding='utf8') as f:
        user, password = f.readlines()
except:
    user = input('Введите логин - ')
    password = input('Введите пароль - ')
    with open('config_act.py', 'w', encoding='utf8') as f:
        f.write(f'user_login = "{user}"\nuser_password = "{password}"')
    print("Эта процедура запускается один раз. Если ты ввёл неправильные данные, то просто удали из папки main файл config_act")
    
finally:
    from config_act import user_login, user_password


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


def login():
    session.headers.update(headers)

    res = session.get(log_url)
    soup = BeautifulSoup(res.content, 'html.parser')

    data = {
        'anchor': '',
        'logintoken': soup.find('input', {"name": "logintoken"}).get("value"),
        "username" : user_login,
        "password" : user_password,
    }
    
    time.sleep(5)
    
    loging = session.post(log_url, data=data, headers=headers)

    time.sleep(5)

def profile():

    cookies_dict = [
        {"domain": key.domain, "name": key.name, "path": key.path, "value": key.value}
        for key in session.cookies
    ]


    for cookies in cookies_dict:
        session2.cookies.set(**cookies)

    profile = session2.get(profile_link, headers=headers)


    # f = open('results.html', 'w', encoding='utf8')
    # f.write(profile.text)
    # f.close()

    return profile



def get_lesson():

    today = datetime.datetime.today().isoweekday()
    
    def course_req(today):
        if today == 1: #Понедельник
            time.sleep(6300) # Секунд ожидания, если нет 1 пары (Пара 5400 сек.)

            k = 0
            w = 0

            while k < 9: #Первая Пара
                try:
                    res =  session2.get("https://distant.donnuet.ru/course/view.php?id=1630", headers=headers) #Гостиничный сервис
                    k += 1
                    soup = BeautifulSoup(res.text, 'html.parser')
                    name_course = soup.find('div', class_ = 'page-header-headings').get_text()
                    name_user = soup.find('span', class_ = 'usertext mr-1').get_text()
                    print(f"Бот-аккаунт ({name_user}) на курсе : {name_course} ")
                    time.sleep(600)
                except requests.exceptions.ConnectionError:
                    print(f": Переподключение...")
                    k += 1
                    pass
                    time.sleep(600)
            print("Пара закончена!") 
            print("Следующая пара через 15 минут")     

            time.sleep(900)

            while w < 9: # Вторая пара
                try:
                    res =  session2.get("https://distant.donnuet.ru/course/view.php?id=1907", headers=headers)
                    w += 1
                    soup = BeautifulSoup(res.text, 'html.parser')
                    name_course = soup.find('div', class_ = 'page-header-headings').get_text()
                    name_user = soup.find('span', class_ = 'usertext mr-1').get_text()
                    print(f"Бот-аккаунт ({name_user}) на курсе : {name_course} ")
                    time.sleep(600)
                except requests.exceptions.ConnectionError:
                    print("Переподключение...")
                    w += 1
                    pass
                    time.sleep(600)

            print("Бот закончил работу")

        if today == 2: #Вторник
            time.sleep(6300) # Секунд ожидания, если нет 1 пары (Пара 5400 сек.)
            a = 0
            b = 0
            c = 0
            d = 0
            while a < 9: #Первая Пара
                try:
                    res =  session2.get("https://distant.donnuet.ru/course/view.php?id=1426", headers=headers) #Естественнонаучная картина мира
                    a += 1
                    soup = BeautifulSoup(res.text, 'html.parser')
                    name_course = soup.find('div', class_ = 'page-header-headings').get_text()
                    name_user = soup.find('span', class_ = 'usertext mr-1').get_text()
                    print(f"Бот-аккаунт ({name_user}) на курсе : {name_course} ")
                    time.sleep(600)
                except requests.exceptions.ConnectionError:
                    print(f": Переподключение...")
                    a += 1
                    pass
                    time.sleep(600)
            print("Пара закончена!") 
            print("Следующая пара через 15 минут")     

            time.sleep(900)

            while b < 9: # Вторая пара
                try:
                    res1 = session2.get("https://distant.donnuet.ru/course/view.php?id=1462", headers=headers) #Музееведение
                    res2 = session2.get("https://distant.donnuet.ru/course/view.php?id=4170", headers=headers) #Психодиагностика
                    b += 1
                    soup1 = BeautifulSoup(res1.text,'html.parser')
                    soup2 = BeautifulSoup(res2.text,'html.parser')

                    name_course1 = soup1.find('div', class_ = 'page-header-headings').get_text()
                    name_course2 = soup2.find('div', class_ = 'page-header-headings').get_text()

                    name_user = soup1.find('span', class_ = 'usertext mr-1').get_text()
                    print(f"Бот-аккаунт ({name_user}) на курсе : {name_course1} и {name_course2} ")

                    time.sleep(600)
                except requests.exceptions.ConnectionError:
                    print("Переподключение...")
                    b += 1
                    pass
                    time.sleep(600)

            print("Пара закончена!") 
            print("Следующая пара через 15 минут")     

            time.sleep(900)

            while c < 9: # Третья пара
                try:
                    res1 = session2.get("https://distant.donnuet.ru/course/view.php?id=1589", headers=headers) #Русский
                    res2 = session2.get("https://distant.donnuet.ru/course/view.php?id=1534", headers=headers) #Анализ хоз. деят.
                    c += 1
                    soup1 = BeautifulSoup(res1.text,'html.parser')
                    soup2 = BeautifulSoup(res2.text,'html.parser')

                    name_course1 = soup1.find('div', class_ = 'page-header-headings').get_text()
                    name_course2 = soup2.find('div', class_ = 'page-header-headings').get_text()

                    name_user = soup1.find('span', class_ = 'usertext mr-1').get_text()
                    print(f"Бот-аккаунт ({name_user}) на курсе : {name_course1} и {name_course2} ")

                    time.sleep(600)
                except requests.exceptions.ConnectionError:
                    print("Переподключение...")
                    c += 1
                    pass
                    time.sleep(600)

            print("Пара закончена!") 
            print("Следующая пара через 15 минут")     

            time.sleep(900)

            while d < 9: # Четвёртая пара
                try:
                    res1 = session2.get("https://distant.donnuet.ru/course/view.php?id=6342", headers=headers) #Физра
                    res2 = session2.get("https://distant.donnuet.ru/course/view.php?id=1534", headers=headers) #Анализ хоз. деят.
                    d += 1
                    soup1 = BeautifulSoup(res1.text,'html.parser')
                    soup2 = BeautifulSoup(res2.text,'html.parser')

                    name_course1 = soup1.find('div', class_ = 'page-header-headings').get_text()
                    name_course2 = soup2.find('div', class_ = 'page-header-headings').get_text()

                    name_user = soup1.find('span', class_ = 'usertext mr-1').get_text()
                    print(f"Бот-аккаунт ({name_user}) на курсе : {name_course1} и {name_course2} ")

                    time.sleep(600)
                except requests.exceptions.ConnectionError:
                    print("Переподключение...")
                    d += 1
                    pass
                    time.sleep(600)
                    
            print("Бот закончил работу")       

        if today == 3: #Среда
            a = 0
            b = 0
            c = 0
            d = 0
            while a < 9: #Первая Пара
                try:
                    res =  session2.get("https://distant.donnuet.ru/course/view.php?id=3979", headers=headers) #Английский
                    a += 1
                    soup = BeautifulSoup(res.text, 'html.parser')
                    name_course = soup.find('div', class_ = 'page-header-headings').get_text()
                    name_user = soup.find('span', class_ = 'usertext mr-1').get_text()
                    print(f"Бот-аккаунт ({name_user}) на курсе : {name_course} ")
                    time.sleep(600)
                except requests.exceptions.ConnectionError:
                    print(f": Переподключение...")
                    a += 1
                    pass
                    time.sleep(600)
            
            print("Пара закончена!") 
            print("Следующая пара через 15 минут")

            time.sleep(900)

            while b < 9: # Вторая пара
                try:
                    res1 = session2.get("https://distant.donnuet.ru/course/view.php?id=4170", headers=headers) #Психодиагностика
                    
                    b += 1
                    soup1 = BeautifulSoup(res1.text,'html.parser')
                    name_course1 = soup1.find('div', class_ = 'page-header-headings').get_text()
                    name_user = soup1.find('span', class_ = 'usertext mr-1').get_text()
                    print(f"Бот-аккаунт ({name_user}) на курсе : {name_course1}")
                    time.sleep(600)
                except requests.exceptions.ConnectionError:
                    print("Переподключение...")
                    b += 1
                    pass
                    time.sleep(600)

            print("Пара закончена!") 
            print("Следующая пара через 15 минут")

            time.sleep(900)

            while c < 9: #Третья пара
                try:
                    res1 = session2.get("https://distant.donnuet.ru/course/view.php?id=1534", headers=headers) #Анализ. хоз деятельности
                    
                    c += 1
                    soup1 = BeautifulSoup(res1.text,'html.parser')
                    name_course1 = soup1.find('div', class_ = 'page-header-headings').get_text()
                    name_user = soup1.find('span', class_ = 'usertext mr-1').get_text()
                    print(f"Бот-аккаунт ({name_user}) на курсе : {name_course1}")
                    time.sleep(600)
                except requests.exceptions.ConnectionError:
                    print("Переподключение...")
                    c += 1
                    pass
                    time.sleep(600)

        if today == 4: #Четверг
            a = 0
            b = 0
            c = 0

            while a < 9: #Первая Пара
                try:
                    res1 = session2.get("https://distant.donnuet.ru/course/view.php?id=1604", headers=headers) #Английский
                    res2 = session2.get("https://distant.donnuet.ru/course/view.php?id=1426", headers=headers) #Картина блять
                    a += 1
                    soup1 = BeautifulSoup(res1.text,'html.parser')
                    soup2 = BeautifulSoup(res2.text,'html.parser')

                    name_course1 = soup1.find('div', class_ = 'page-header-headings').get_text()
                    name_course2 = soup2.find('div', class_ = 'page-header-headings').get_text()

                    name_user = soup1.find('span', class_ = 'usertext mr-1').get_text()
                    print(f"Бот-аккаунт ({name_user}) на курсе : {name_course1} и {name_course2} ")

                    time.sleep(600)
                except requests.exceptions.ConnectionError:
                    print("Переподключение...")
                    a += 1
                    pass
                    time.sleep(600)
            print("Пара закончена!") 
            print("Следующая пара через 15 минут")

            time.sleep(900)

            while b < 9: #Вторая пара
                try:
                    res1 = session2.get("https://distant.donnuet.ru/course/view.php?id=1630", headers=headers) #Гостиничный сервис
                    
                    b += 1
                    soup1 = BeautifulSoup(res1.text,'html.parser')
                    

                    name_course1 = soup1.find('div', class_ = 'page-header-headings').get_text()
                    

                    name_user = soup1.find('span', class_ = 'usertext mr-1').get_text()
                    print(f"Бот-аккаунт ({name_user}) на курсе : {name_course1}")

                    time.sleep(600)
                except requests.exceptions.ConnectionError:
                    print("Переподключение...")
                    b += 1
                    pass
                    time.sleep(600)
    
            print("Пара закончена!") 
            print("Следующая пара через 1,5 часа и 15 минут")

            time.sleep(6300)

            login()
            profile()

            while c < 9: # Третья пара
                try:
                    res1 = session2.get("https://distant.donnuet.ru/course/view.php?id=1462", headers=headers) #Музееведение
                    
                    c += 1
                    soup1 = BeautifulSoup(res1.text,'html.parser')
                    soup2 = BeautifulSoup(res2.text,'html.parser')

                    name_course1 = soup1.find('div', class_ = 'page-header-headings').get_text()
                    name_course2 = soup2.find('div', class_ = 'page-header-headings').get_text()

                    name_user = soup1.find('span', class_ = 'usertext mr-1').get_text()
                    print(f"Бот-аккаунт ({name_user}) на курсе : {name_course1}")

                    time.sleep(600)
                except requests.exceptions.ConnectionError:
                    print("Переподключение...")
                    c += 1
                    pass
                    time.sleep(600)

        if today == 5: #Пятница
            a = 0
            b = 0
            c = 0
            d = 0
            while a < 9: # Первая пара
                try:
                    res1 = session2.get("https://distant.donnuet.ru/course/view.php?id=4170", headers=headers) #Психодиагностика
                    res2 = session2.get("https://distant.donnuet.ru/course/view.php?id=6342", headers=headers) #Физра
                    a += 1
                    soup1 = BeautifulSoup(res1.text,'html.parser')
                    soup2 = BeautifulSoup(res2.text,'html.parser')

                    name_course1 = soup1.find('div', class_ = 'page-header-headings').get_text()
                    name_course2 = soup2.find('div', class_ = 'page-header-headings').get_text()

                    name_user = soup1.find('span', class_ = 'usertext mr-1').get_text()
                    print(f"Бот-аккаунт ({name_user}) на курсе : {name_course1} и {name_course2} ")

                    time.sleep(600)
                except requests.exceptions.ConnectionError:
                    print("Переподключение...")
                    a += 1
                    pass
                    time.sleep(600)

            print("Пара закончена!") 
            print("Следующая пара через 15 минут")

            time.sleep(900)
            
            while b < 9: #Вторая пара
                try:
                    res1 = session2.get("https://distant.donnuet.ru/course/view.php?id=1907", headers=headers) #Экономика предпр. сервиса.
                    res2 = session2.get("https://distant.donnuet.ru/course/view.php?id=1589", headers=headers) #Русский
                    b += 1
                    soup1 = BeautifulSoup(res1.text,'html.parser')
                    soup2 = BeautifulSoup(res2.text,'html.parser')

                    name_course1 = soup1.find('div', class_ = 'page-header-headings').get_text()
                    name_course2 = soup2.find('div', class_ = 'page-header-headings').get_text()

                    name_user = soup1.find('span', class_ = 'usertext mr-1').get_text()
                    print(f"Бот-аккаунт ({name_user}) на курсе : {name_course1} и {name_course2} ")

                    time.sleep(600)
                except requests.exceptions.ConnectionError:
                    print("Переподключение...")
                    b += 1
                    pass
                    time.sleep(600)

            print("Пара закончена!") 
            print("Следующая пара через 15 минут")

            time.sleep(900)

            while c < 9: # Третья пара
                try:
                    res1 = session2.get("https://distant.donnuet.ru/course/view.php?id=1589", headers=headers) #Русский
                    
                    c += 1
                    soup1 = BeautifulSoup(res1.text,'html.parser')
                    name_course1 = soup1.find('div', class_ = 'page-header-headings').get_text()
                    name_user = soup1.find('span', class_ = 'usertext mr-1').get_text()
                    print(f"Бот-аккаунт ({name_user}) на курсе : {name_course1}")

                    time.sleep(600)
                except requests.exceptions.ConnectionError:
                    print("Переподключение...")
                    c += 1
                    pass
                    time.sleep(600)

            print("Пара закончена!") 
            print("Следующая пара через 15 минут")

            time.sleep(900) 

            while d < 9: # Четвёртая пара
                try:
                    res1 = session2.get("https://distant.donnuet.ru/course/view.php?id=6342", headers=headers) #Физра                   
                    d += 1
                    soup1 = BeautifulSoup(res1.text,'html.parser')
                    name_course1 = soup1.find('div', class_ = 'page-header-headings').get_text()
                    name_user = soup1.find('span', class_ = 'usertext mr-1').get_text()
                    print(f"Бот-аккаунт ({name_user}) на курсе : {name_course1}")
                    time.sleep(600)
                except requests.exceptions.ConnectionError:
                    print("Переподключение...")
                    d += 1
                    pass
                    time.sleep(600)

        if today == 7: #Воскресенье
            print("Завтра пары. ВАЖНО ЧТОБЫ В 8:30 У ТЕБЯ БЫЛ ИНТЕРНЕТ, иначе бот работать не будет")

    course_req(today)

def main():



    global login
    login = login()
    prof = profile()
    
    soup = BeautifulSoup(prof.text, 'html.parser')
    unlog = soup.find('span', class_ = 'login') #Переменная отвечающая за вход в систему, если есть, то бот не вошёл в систему


    while True:
        if unlog:
            print("Идёт авторизация")
            login
            continue
        else:  
            print("Бот вошёл в систему!")
            break
    

    time.sleep(5)

    global get_lesson
    get_lesson = get_lesson()

    time.sleep(10)

    

if __name__ == "__main__":
    main()