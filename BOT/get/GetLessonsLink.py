import site.LessonsLink as LessonsLink
import datetime
import time
from site.LessonsLink import Lessons_lib


# today = datetime.datetime.today().isoweekday()# Выводит номер дня недели (1-Понедельник ... 7-Воскресенье)
# TimeNow = datetime.datetime.today().strftime('%H:%M')
def GetLessonsLink():

    today = 4
    TimeNow = "02:36"
    num = LessonsLink.Lessons_lib.items()

    try:
        return Lessons_lib[str(today)][TimeNow]
    except KeyError:
        pass

print(GetLessonsLink())
