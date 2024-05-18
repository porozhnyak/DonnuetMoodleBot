
import datetime
import time
import LessonsLink 
import asyncio


# today = datetime.datetime.today().isoweekday()# Выводит номер дня недели (1-Понедельник ... 7-Воскресенье)
# TimeNow = datetime.datetime.today().strftime('%H:%M')


async def GetLessonsLink(today, TimeNow):

    # today = 4
    # TimeNow = "02:36"
    # num = Lessons_lib.items()

    try:
        print(today, TimeNow)
        return LessonsLink.Lessons_lib[str(today)][TimeNow]
    except KeyError:
        pass

# print(GetLessonsLink(today, TimeNow))
