import logging
import sqlite3

async def db_connect():
    return sqlite3.connect('credit/users.db')


async def check_user_exists(user_id):
    conn = await db_connect()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE user_id = ?', (user_id,))
    user = cursor.fetchone()
    conn.close()
    return user

async def save_user(user_id, login, password):
    conn = await db_connect()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users (user_id, login, password) VALUES (?, ?, ?)', (user_id, login, password))
    conn.commit()
    conn.close()