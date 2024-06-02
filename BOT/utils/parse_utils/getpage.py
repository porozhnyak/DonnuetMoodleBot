import logging
import aiohttp

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('response')

async def get_page(log, url):
    try:
        async with aiohttp.ClientSession(cookies=log) as session:
            async with session.get(url) as profile_response:
                if profile_response.status != 200:
                    logger.error(f"Error fetching profile page: {profile_response.status}")
                    return None

                return await profile_response.text()
    except Exception as e:
        logger.error(f"Error in profile function: {e}")
        return None