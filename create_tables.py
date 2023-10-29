import sqlite3

def create_db(command_file='create_tables_sqlite_commands.sql', db_name="grades.db"):
    # читаємо файл зі скриптом для створення БД
    with open(command_file, 'r', encoding="utf8") as f:
        sql = f.read()

    # створюємо з'єднання з БД (якщо файлу з БД немає, він буде створений)
    with sqlite3.connect(db_name) as con:
        cur = con.cursor()
        # виконуємо скрипт із файлу, який створить таблиці в БД
        cur.executescript(sql)


if __name__ == "__main__":
    create_db()