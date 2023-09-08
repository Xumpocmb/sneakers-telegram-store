import sqlite3


async def db_start():
    try:
        db = sqlite3.connect('bot.db')
        db_cursor = db.cursor()

        db_cursor.execute('CREATE TABLE IF NOT EXISTS users('
                          'id INTEGER PRIMARY KEY AUTOINCREMENT,'
                          'user_id TEXT,'
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


if __name__ == '__main__':
    db_start()