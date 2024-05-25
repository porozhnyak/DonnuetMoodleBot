
import datetime
import time
import LessonsLink 
import asyncio
import logging


async def GetLessonsLink(today, TimeNow):
    try:
        print(f"День: {today}, Время: {TimeNow}")
        return LessonsLink.Lessons_lib[today][TimeNow]
    except KeyError:
        pass
# while True:
#     today = str(datetime.datetime.today().isoweekday())# Выводит номер дня недели (1-Понедельник ... 7-Воскресенье)
#     TimeNow = datetime.datetime.today().strftime('%H:%M')

#     asyncio.run(GetLessonsLink(today, TimeNow))
#     time.sleep(10)
