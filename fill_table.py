from datetime import datetime
import faker
from random import randint, choice
from datetime import datetime
import sqlite3


NUMBER_STUDENTS = 50
NUMBER_GROUPS = 3
NUMBER_TEACHERS = 5
NUMBER_SUBJECTS = NUMBER_TEACHERS*2
NUMBER_GRADES = 10


def generate_fake_data(number_students, number_groups, number_teachers, number_subjects, number_grades):
    fake_student_names = []
    fake_group_names = []
    fake_teacher_names = []
    fake_subject_names = []
    fake_grades = []
    fake_grade_dates = []

    '''Візьмемо три компанії з faker і помістимо їх у потрібну змінну'''
    fake_data = faker.Faker()

    for _ in range(number_students):
        fake_student_names.append(fake_data.name())

    for _ in range(number_teachers):
        fake_teacher_names.append(fake_data.name())

    for _ in range(number_groups):
        fake_group_names.append(fake_data.word().title())

    for _ in range(NUMBER_SUBJECTS):
        fake_subject_names.append(fake_data.word().title())

    for _ in range(number_students*number_subjects*number_grades):
        fake_grades.append(randint(0, 100))
        fake_grade_dates.append(str(fake_data.date_between_dates(date_start=datetime(2015,1,1), date_end=datetime(2023,10,31))))

    return fake_student_names, fake_teacher_names, fake_group_names, fake_subject_names, fake_grades, fake_grade_dates

if __name__ == "__main__":
    res = generate_fake_data(NUMBER_STUDENTS, NUMBER_GROUPS, NUMBER_TEACHERS, NUMBER_SUBJECTS, NUMBER_GRADES)
    for el in res:
        print(el)