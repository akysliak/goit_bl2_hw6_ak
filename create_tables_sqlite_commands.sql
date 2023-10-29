-- Таблиця груп
DROP TABLE IF EXISTS groups;
CREATE TABLE groups (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name VARCHAR(50) NOT NULL
);

-- Таблиця студентів
DROP TABLE IF EXISTS students;
CREATE TABLE students (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  fullname VARCHAR(150) NOT NULL,
  group_id INTEGER,
  FOREIGN KEY (group_id) REFERENCES groups(id)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);

-- Таблиця викладачів
DROP TABLE IF EXISTS teachers;
CREATE TABLE teachers (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  fullname VARCHAR(150) NOT NULL
);

-- Таблиця предметів
DROP TABLE IF EXISTS subjects;
CREATE TABLE subjects (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name VARCHAR(175) NOT NULL,
  teacher_id INTEGER,
  FOREIGN KEY (teacher_id) REFERENCES teachers(id)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);

-- Таблиця оцінок
DROP TABLE IF EXISTS grades;
CREATE TABLE grades (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  student_id INTEGER,
  subject_id INTEGER,
  grade INTEGER CHECK (grade >= 0 AND grade <= 100),
  grade_date DATE NOT NULL,
  FOREIGN KEY (student_id) REFERENCES students(id)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  FOREIGN KEY (subject_id) REFERENCES subjects(id)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);

