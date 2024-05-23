# database.py

import sqlite3

DATABASE_PATH = 'BOT/credit/moodlebot.db'

async def init_db():
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            login TEXT,
            password TEXT,
            profile_name TEXT
        )
    ''')
    conn.commit()
    conn.close()

async def save_user(user_id, login, password, profile_name):
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users (user_id, login, password, profile_name) VALUES (?, ?, ?, ?)', (user_id, login, password, profile_name))
    conn.commit()
    conn.close()

async def get_user(user_id):
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE user_id = ?', (user_id,))
    user = cursor.fetchone()
    conn.close()
    return user
