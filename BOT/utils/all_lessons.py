from bs4 import BeautifulSoup
import aiohttp
from parse_utils import getpage
import asyncres

import asyncio

url = "https://distant.donnuet.ru/my/"

async def list_lessons(url):

    log = await asyncres.login(user_login="10.rdo", user_password="Stud_2021")

    page = await getpage(log, url)

    return page

asyncio.run(print(list_lessons))

