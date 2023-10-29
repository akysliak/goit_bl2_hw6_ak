import logging
import sqlite3

from faker import Faker
from random import randint

from create_tables import create_db

NUMBER_STUDENTS_PER_GROUP = 15
NUMBER_GROUPS = 3
NUMBER_TEACHERS = 5
NUMBER_SUBJECTS_PER_TEACHER = 2
NUMBER_GRADES_PER_SUBJECT = 10

fake = Faker()


def execute_query(sql: str, db_name: str) -> list:
    with sqlite3.connect(db_name) as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()

# Підключення до бази даних
def execute_queries(sqls: [str], db_name) -> list:
    if not sqls:
        return
    with sqlite3.connect(db_name) as con:
        cur = con.cursor()
        for sql in sqls:
            cur.execute(sql)
        return cur.fetchall()


# Додавання груп
def generate_sql_add_groups(number_groups=NUMBER_GROUPS):
    res = []
    for _ in range(number_groups):
        res.append(f"INSERT INTO groups (name) VALUES ('{fake.word().title()}')") #("INSERT INTO groups (name) VALUES (%s)", (fake.word().title(),))
    return res


# Додавання викладачів
def generate_sql_add_teachers(number_teachers=NUMBER_TEACHERS):
    res = []
    for _ in range(number_teachers):
        res.append(f"INSERT INTO teachers (fullname) VALUES ('{fake.name()}')")
    return res


# Додавання предметів із вказівкою викладача
def generate_sql_add_subjects(number_subjects_per_teacher=NUMBER_SUBJECTS_PER_TEACHER,
                              number_teachers=NUMBER_TEACHERS):
    res = []
    for teacher_id in range(1, number_teachers+1):
        for _ in range(number_subjects_per_teacher):
            res.append(f"INSERT INTO subjects (name, teacher_id) VALUES ('{fake.word().title()}', '{teacher_id}')")
    return res


# Додавання студентів і оцінок
def add_students_and_grades(db_name, number_subjects=NUMBER_SUBJECTS_PER_TEACHER*NUMBER_TEACHERS,
                              number_groups=NUMBER_GROUPS,
                              number_students_per_group=NUMBER_STUDENTS_PER_GROUP,
                              number_grades_per_subject=NUMBER_GRADES_PER_SUBJECT):
    with sqlite3.connect(db_name) as con:
        cur = con.cursor()
        for group_id in range(1, number_groups+1):
            for _ in range(number_students_per_group):
                cur.execute(f"INSERT INTO students (fullname, group_id) VALUES ('{fake.name()}', '{group_id}') RETURNING id")
                student_id = cur.fetchone()[0]
                for subject_id in range(1, number_subjects+1):
                    for _ in range(number_grades_per_subject):
                        cur.execute(f"INSERT INTO grades (student_id, subject_id, grade, grade_date) VALUES "
                                    f"('{student_id}', '{subject_id}', '{randint(0, 100)}', '{fake.date_this_decade()}')")

if __name__ == "__main__":
    command_file = 'create_tables_sqlite_commands.sql'
    db_name = "grades.db"
    create_db(command_file, db_name)
    sqls = generate_sql_add_groups()
    sqls += generate_sql_add_teachers()
    sqls += generate_sql_add_subjects()
    execute_queries(sqls, db_name)
    add_students_and_grades(db_name)

'''
try:
    # Збереження змін
    conn.commit()
except DatabaseError as e:
    logging.error(e)
    conn.rollback()
finally:
    # Закриття підключення
    cur.close()
    conn.close()
'''

