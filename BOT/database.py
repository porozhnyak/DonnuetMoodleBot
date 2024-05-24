import aiosqlite

async def init_db():
    async with aiosqlite.connect('BOT/credit/moodlebot.db') as db:
        await db.execute('''CREATE TABLE IF NOT EXISTS users (
                            user_id INTEGER PRIMARY KEY,
                            login TEXT NOT NULL,
                            password TEXT NOT NULL,
                            profile_name TEXT NOT NULL,
                            is_active INTEGER DEFAULT 0
                            )''')
        await db.commit()

async def save_user(user_id, login, password, profile_name):
    async with aiosqlite.connect('BOT/credit/moodlebot.db') as db:
        await db.execute('''INSERT INTO users (user_id, login, password, profile_name) VALUES (?, ?, ?, ?)''',
                        (user_id, login, password, profile_name))
        await db.commit()

async def get_user(user_id):
    async with aiosqlite.connect('BOT/credit/moodlebot.db') as db:
        cursor = await db.execute('''SELECT * FROM users WHERE user_id = ?''', (user_id,))
        return await cursor.fetchone()

async def update_user_active_status(user_id, is_active):
    async with aiosqlite.connect('BOT/credit/moodlebot.db') as db:
        await db.execute('''UPDATE users SET is_active = ? WHERE user_id = ?''', (is_active, user_id))
        await db.commit()
