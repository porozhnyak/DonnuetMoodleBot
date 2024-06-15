
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
