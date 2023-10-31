import sqlite3

def query_db(command_file, db_name="grades.db"):
    # читаємо файл зі скриптом для створення БД
    with open(command_file, 'r', encoding="utf8") as f:
        sql = f.read()

    # створюємо з'єднання з БД (якщо файлу з БД немає, він буде створений)
    with sqlite3.connect(db_name) as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


def print_results(results: []):
    if not results:
        print("Result is:", results)
        return
    for pos, el in enumerate(results):
        print(f"\t{pos+1}. {el}")

if __name__ == "__main__":
    db_name = "grades.db"
    task2sql_file = {
        "1. Знайти 5 студентів із найбільшим середнім балом з усіх предметів:": "query_1.sql",
        "2. Знайти студента із найвищим середнім балом з певного предмета (1):": "query_2.sql",
        "2. Знайти студента із найвищим середнім балом з певного предмета (2):": "query_2_2.sql",
        "3. Знайти середній бал у групах з певного предмета (general):": "query_3_general.sql",
        "3. Знайти середній бал у групах з певного предмета (specific):": "query_3.sql",
        "4. Знайти середній бал на потоці (по всій таблиці оцінок):": "query_4.sql",
        "5. Знайти які курси читає певний викладач (general):": "query_5_general.sql",
        "5. Знайти які курси читає певний викладач (specific):": "query_5.sql",
        "6. Знайти список студентів у певній групі (general):": "query_6_general.sql",
        "6. Знайти список студентів у певній групі (specific):": "query_6.sql",
        #"7. Знайти оцінки студентів у окремій групі з певного предмета (general):": "query_7_general.sql",
        "7. Знайти оцінки студентів у окремій групі з певного предмета (specific):": "query_7.sql",
        "8. Знайти середній бал, який ставить певний викладач зі своїх предметів (general):": "query_8_general.sql",
        "8. Знайти середній бал, який ставить певний викладач зі своїх предметів (specific):": "query_8.sql",
        "9. Знайти список курсів, які відвідує студент (specific):": "query_9.sql",
        "10. Список курсів, які певному студенту читає певний викладач (specific):": "query_10.sql",
        "11 (additional). Середній бал, який певний викладач ставить певному студентові (specific):": "query_11.sql",
        "12 (additional). Оцінки студентів у певній групі з певного предмета на останньому занятті (specific):": "query_12.sql"
    }
    for task, sql_file in task2sql_file.items():
        print(task)
        print_results(query_db(sql_file, db_name))
