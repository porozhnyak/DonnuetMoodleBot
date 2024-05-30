from bs4 import BeautifulSoup
import aiohttp
import re
import asyncio

async def extract_group(profile_name):
    # Регулярное выражение для поиска группы, учитывающее нижнее подчеркивание
    pattern = re.compile(r'\b[A-Za-zА-Яа-я]{1,9}-\d{2}(?:-\w+)?(?:-?\d{0,2})?\b')
    match = pattern.search(profile_name.replace('_', ' '))
    return match.group() if match else None