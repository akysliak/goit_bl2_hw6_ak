import sqlite3

def query_db(command_file='query_db_sqlite_commands.sql', db_name="grades.db"):
    # читаємо файл зі скриптом для створення БД
    with open(command_file, 'r', encoding="utf8") as f:
        sql = f.read()

    # створюємо з'єднання з БД (якщо файлу з БД немає, він буде створений)
    with sqlite3.connect(db_name) as con:
        cur = con.cursor()
        cur.executescript(sql)
        print(cur.fetchall())


def execute_query(sql: str, db_name: str) -> list:
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
    sql = """
        SELECT
            s.id,
            s.fullname,
            ROUND(AVG(g.grade), 2) AS average_grade
        FROM students s
        JOIN grades g ON s.id = g.student_id
        GROUP BY s.id
        ORDER BY average_grade DESC
        LIMIT 5;
    """
    print("1. Знайти 5 студентів із найбільшим середнім балом з усіх предметів:")
    print_results(execute_query(sql, db_name))

    sql = """
        WITH StudentGrades AS (
            SELECT
                s.id,
                s.fullname,
                ROUND(AVG(g.grade)) as average_grade
            FROM students s
            JOIN grades g ON s.id = g.student_id
            WHERE g.subject_id = 1  -- Предмет, з якого ви хочете знайти середній бал
            GROUP BY s.id
        )
        SELECT
            id,
            fullname,
            average_grade
        FROM StudentGrades
        ORDER BY average_grade DESC
        LIMIT 1;
    """
    print("2. Знайти студента із найвищим середнім балом з певного предмета (1):")
    print_results(execute_query(sql, db_name))

    sql = """
        SELECT
            s.id,
            s.fullname,
            ROUND(AVG(g.grade), 2) AS average_grade
        FROM grades g
        JOIN students s ON s.id = g.student_id
        where g.subject_id = 1
        GROUP BY s.id
        ORDER BY average_grade DESC
        LIMIT 1;
    """
    print("2. Знайти студента із найвищим середнім балом з певного предмета (2):")
    print_results(execute_query(sql, db_name))

    print("3. Знайти середній бал у групах з певного предмета:")
    sql = """
    SELECT
        groups.name,
        subjects.name,
        ROUND(AVG(g.grade), 2) AS average_grade
    FROM students s
    JOIN grades g ON s.id = g.student_id
    JOIN subjects ON g.subject_id = subjects.id
    JOIN groups ON s.group_id = groups.id
    GROUP BY g.subject_id, s.group_id
    ORDER BY s.group_id, subjects.name ASC;
    """
    print_results(execute_query(sql, db_name))

    #print("4. Знайти середній бал на потоці (по всій таблиці оцінок):")

    #print("5. Знайти які курси читає певний викладач:")

    #print("6. Знайти список студентів у певній групі:")

    #print("7. Знайти оцінки студентів у окремій групі з певного предмета:")

    #print("8. Знайти середній бал, який ставить певний викладач зі своїх предметів:")

    #print("9. Знайти список курсів, які відвідує студент:")

    #print("10. Список курсів, які певному студенту читає певний викладач:")
