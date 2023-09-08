import sqlite3
from aiogram.types import Message


def run_connection():
    try:
        db = sqlite3.connect('bot.db')
        db_cursor = db.cursor()
        return db, db_cursor
    except Exception as e:
        print(f'Ошибка: {e}')


async def db_start():
    db, db_cursor = run_connection()
    try:
        db_cursor.execute('CREATE TABLE IF NOT EXISTS users('
                          'id INTEGER PRIMARY KEY AUTOINCREMENT,'
                          'user_id TEXT,'
                          'username TEXT,'
                          'balance INTEGER,'
                          'cart_id TEXT)')
        db_cursor.execute('CREATE TABLE IF NOT EXISTS categories('
                          'category_id INTEGER PRIMARY KEY AUTOINCREMENT,'
                          'category_name TEXT)')
        db_cursor.execute('CREATE TABLE IF NOT EXISTS items ('
                          'id INTEGER PRIMARY KEY AUTOINCREMENT,'
                          'category_id INTEGER,'
                          'item_name TEXT,'
                          'item_description TEXT,'
                          'item_price TEXT,'
                          'item_photo TEXT,'
                          'FOREIGN KEY(category_id) REFERENCES categories(category_id))'
                          )
        db.commit()  # Сохраняем изменения в базе данных
    except sqlite3.Error as e:
        print("Ошибка SQLite:", e)
    finally:
        if db_cursor:
            db_cursor.close()
        if db:
            db.close()


async def cmd_start_db(message: Message):
    db, db_cursor = run_connection()
    try:
        user = db_cursor.execute(
            "SELECT * FROM users WHERE user_id == '{key}'".format(key=message.from_user.id)).fetchone()
        if not user:
            db_cursor.execute("INSERT INTO users (user_id, username, balance, cart_id) VALUES (?, ?, ?, ?)",
                              (message.from_user.id, message.from_user.username, 0, '0'))
            db.commit()
    except sqlite3.Error as e:
        print("Ошибка SQLite:", e)
    finally:
        if db_cursor:
            db_cursor.close()
        if db:
            db.close()


if __name__ == '__main__':
    db_start()
