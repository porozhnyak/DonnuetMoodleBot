from bs4 import BeautifulSoup
import aiohttp
import re
import asyncio



async def extract_group(profile_name):
    # Регулярное выражение для поиска группы, учитывающее нижнее подчеркивание
    pattern = re.compile(r'\b[A-ZА-Я]{2,}(?:-\d{2,})+(?:-[A-ZА-Я]+)?\b')
    match = pattern.search(profile_name.replace('_', ' '))
    return match.group() if match else None



