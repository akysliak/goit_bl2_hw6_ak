SELECT
    teachers.fullname,
    subjects.name
FROM teachers
JOIN subjects ON subjects.teacher_id = teachers.id
WHERE teachers.id = 3;