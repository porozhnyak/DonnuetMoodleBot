etica = "https://distant.donnuet.ru/course/view.php?id=4371"
fizra = "https://distant.donnuet.ru/course/view.php?id=6344"
pravo = "https://distant.donnuet.ru/course/view.php?id=289"
zdorovoe_pitanie = "https://distant.donnuet.ru/course/view.php?id=1602"
estetica = "https://distant.donnuet.ru/course/view.php?id=7433"
marketing = "https://distant.donnuet.ru/course/view.php?id=3442"
organizacia = "https://distant.donnuet.ru/course/view.php?id=3446"
servicnaya_deyat = "https://distant.donnuet.ru/course/view.php?id=3448"
servisologia = "https://distant.donnuet.ru/course/view.php?id=5322"
rabota_predpriatia = "https://distant.donnuet.ru/course/view.php?id=6547"

import datetime
import time


global today, TimeNow

today = str(datetime.datetime.today().isoweekday())# Выводит номер дня недели (1-Понедельник ... 7-Воскресенье)
TimeNow = str(datetime.datetime.today().strftime('%H:%M'))


Lessons_lib = {
    "1": {
        "08:30":organizacia,
        "08:31":fizra,
        "09:00":organizacia,
        "09:01":fizra,
        "09:30":organizacia,
        "09:31":fizra,
        #Конец первой пары
        "10:15":servicnaya_deyat,
        "10:45":servicnaya_deyat,
        "11:15":servicnaya_deyat,
        "11:45":servicnaya_deyat,
        #конец второй пары
        "12:15":rabota_predpriatia,
        "12:45":rabota_predpriatia,
        "12:15":rabota_predpriatia
    },
    "2": {
        "08:30":marketing,
        "08:31":marketing,
        "09:00":marketing,
        "09:01":marketing,
        "09:30":marketing,
        "09:31":marketing,
        #Конец первой пары
        "10:15":zdorovoe_pitanie,
        "10:16":estetica,
        "10:45":zdorovoe_pitanie,
        "10:46":estetica,
        "11:15":zdorovoe_pitanie,
        "11:16":estetica,
        "11:45":zdorovoe_pitanie,
        "11:45":estetica,
        #конец второй пары
    
    },   
    "3": {
        "08:30":organizacia,
        "08:31":estetica,
        "09:00":organizacia,
        "09:01":estetica,
        "09:30":organizacia,
        "09:31":estetica,
        #конец первой пары
        "10:15":fizra,
        "10:16":etica,
        "10:45":fizra,
        "10:46":etica,
        "11:15":fizra,
        "11:16":etica,
        "11:45":fizra,
        "11:46":etica,
        # конец второй пары
        "12:15":pravo,
        "12:16": etica,
        "12:45": pravo,
        "12:46": etica,
        "13:15": pravo,
        "13:16": etica,
        "13:45": pravo,
        "13:46": etica,
        #конец третьей пары
    },
    "4": {
        "8:30": servicnaya_deyat,
        "9:00": servicnaya_deyat,
        "9:30": servicnaya_deyat,
        "10:00": servicnaya_deyat,
        "10:15": marketing,
        "10:45": marketing,
        "11:15": marketing,
        "11:45": marketing,
        "12:15": fizra,
        "12:45": fizra,
        "13:15": fizra,
        "13:45": fizra,
    },
    "5": {
        "8:30": rabota_predpriatia,
        "9:00": rabota_predpriatia,
        "9:30": rabota_predpriatia,
        "10:00": rabota_predpriatia,
        "10:15": zdorovoe_pitanie,
        "10:45": zdorovoe_pitanie,
        "11:15": zdorovoe_pitanie,
        "11:45": zdorovoe_pitanie,
        "12:15": pravo,
        "12:45": pravo,
        "13:15": pravo,
        "13:45": pravo,
    },
    # "7": {
    #     TimeNow: "Это тестовое сообщение! Завтра бот должен начать работу."
    # },
    today:{
        TimeNow :estetica,
    }
}


# while True:
    # today = str(datetime.datetime.today().isoweekday())# Выводит номер дня недели (1-Понедельник ... 7-Воскресенье)
    # TimeNow = datetime.datetime.today().strftime('%H:%M')
    # print(Lessons_lib[today][TimeNow])
    # time.sleep(10)