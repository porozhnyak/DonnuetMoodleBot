import requests
from fake_useragent import UserAgent
import time
from bs4 import BeautifulSoup
import datetime

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



def login(moodle_login,moodle_password):
    session.headers.update(headers)

    res = session.get(log_url)
    soup = BeautifulSoup(res.content, 'html.parser')

    data = {
        'anchor': '',
        'logintoken': soup.find('input', {"name": "logintoken"}).get("value"),
        "username" : moodle_login,
        "password" : moodle_password,
    }
    
    loging = session.post(log_url, data=data, headers=headers)

 

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

def get_main(moodle_login, moodle_password):



    global login
    login = login(moodle_login, moodle_password)
    prof = profile()
    
    soup = BeautifulSoup(prof.text, 'html.parser')
    unlog = soup.find('span', class_ = 'login') #Переменная отвечающая за вход в систему, если есть, то бот не вошёл в систему
    log = soup.find('span', class_ = "usertext mr-1").text

    while True:
        if unlog:
            print("Идёт авторизация")
            login
            continue
        else:  
            return log
            
    

    # return (f"Бот {log} вошёл в систему!")

# if __name__ == "__main__":
#     main()