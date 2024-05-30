import re
import aiosqlite
import asyncio
import logging
from utils.parse_utils.group_name import extract_group

# Настройка логгера
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

async def init_db():
    async with aiosqlite.connect('BOT/credit/moodlebot.db') as db:
        await db.execute('''CREATE TABLE IF NOT EXISTS users (
                            user_id INTEGER PRIMARY KEY,
                            login TEXT NOT NULL,
                            password TEXT NOT NULL,
                            profile_name TEXT NOT NULL,
                            is_active INTEGER DEFAULT 0,
                            is_representative INTEGER DEFAULT 0,
                            is_admin INTEGER DEFAULT 0,
                            group_name TEXT NOT NULL
                            )''')
        await db.commit()
        logger.info("Database initialized.")

async def save_user(user_id, login, password, profile_name):
    try:
        user = await get_user(user_id)
        group_name = await extract_group(profile_name)
        
        if user is None or user[1] != login:
            async with aiosqlite.connect('BOT/credit/moodlebot.db') as db:
                await db.execute('''INSERT INTO users (user_id, login, password, profile_name, group_name) 
                                    VALUES (?, ?, ?, ?, ?)''',
                                (user_id, login, password, profile_name, group_name))
                await db.commit()
                logger.info(f"User {user_id} saved with profile name {profile_name}.")
        else:
            logger.info(f"User {user_id} already exists with the same login.")
    except Exception as e:
        logger.error(f"Error saving user {user_id}: {e}")

async def get_user(user_id):
    try:
        async with aiosqlite.connect('BOT/credit/moodlebot.db') as db:
            cursor = await db.execute('''SELECT * FROM users WHERE user_id = ?''', (user_id,))
            user = await cursor.fetchone()
            if user:
                logger.info(f"User {user_id} found: {user}.")
                return user
            else:
                logger.warning(f"User with id {user_id} not found.")
                return None
    except Exception as e:
        logger.error(f"Error getting user {user_id}: {e}")
        return None

async def get_users_by_group(group_name):
    try:
        async with aiosqlite.connect('BOT/credit/moodlebot.db') as db:
            cursor = await db.execute('''SELECT * FROM users WHERE group_name = ?''', (group_name,))
            users = await cursor.fetchall()
            if users:
                logger.info(f"Users found in group {group_name}: {users}.")
                return users
            else:
                logger.warning(f"No users found in group {group_name}.")
                return []
    except Exception as e:
        logger.error(f"Error getting users by group {group_name}: {e}")
        return []

async def update_user_active_status(user_id, is_active):
    try:
        async with aiosqlite.connect('BOT/credit/moodlebot.db') as db:
            await db.execute('''UPDATE users SET is_active = ? WHERE user_id = ?''', (is_active, user_id))
            await db.commit()
            logger.info(f"User {user_id} active status updated to {is_active}.")
    except Exception as e:
        logger.error(f"Error updating user active status {user_id}: {e}")

async def update_user_representative_status(user_id, is_representative):
    try:
        async with aiosqlite.connect('BOT/credit/moodlebot.db') as db:
            await db.execute('''UPDATE users SET is_representative = ? WHERE user_id = ?''', (is_representative, user_id))
            await db.commit()
            logger.info(f"User {user_id} representative status updated to {is_representative}.")
    except Exception as e:
        logger.error(f"Error updating user representative status {user_id}: {e}")

async def update_user_admin_status(user_id, is_admin):
    try:
        async with aiosqlite.connect('BOT/credit/moodlebot.db') as db:
            await db.execute('''UPDATE users SET is_admin = ? WHERE user_id = ?''', (is_admin, user_id))
            await db.commit()
            logger.info(f"User {user_id} admin status updated to {is_admin}.")
    except Exception as e:
        logger.error(f"Error updating user admin status {user_id}: {e}")

# # Пример использования функций
# async def main():
#     await init_db()
#     await save_user(1, "user_login1", "user_password1", "Анна КШИ-22-А Хорошилова")
#     await save_user(2, "user_login2", "user_password2", "Иван КШИ-22-А Иванов")
#     await save_user(3, "user_login3", "user_password3", "Олег МО-23-А Петров")
    
#     user = await get_user(1)
#     if user:
#         print(user)  # Выводит информацию о пользователе

#     users_in_group = await get_users_by_group("КШИ-22-А")
#     if users_in_group:
#         print(users_in_group)  # Выводит информацию о пользователях в группе "КШИ-22-А"
#     else:
#         print("No users found in the specified group.")

# asyncio.run(main())

    
# # Примеры использования новых функций
# async def set_user_as_representative(user_id):
#     await update_user_representative_status(user_id, 1)

# async def unset_user_as_representative(user_id):
#     await update_user_representative_status(user_id, 0)

# async def set_user_as_admin(user_id):
#     await update_user_admin_status(user_id, 1)

# async def unset_user_as_admin(user_id):
#     await update_user_admin_status(user_id, 0)


# Пример использования фильтра всех пользователей по группе
# await get_users_by_group("КШИ-22-А")

