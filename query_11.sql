SELECT
    t.fullname,
    s.fullname,
    ROUND(AVG(g.grade), 2) AS average_grade
FROM teachers t
JOIN subjects sb ON sb.teacher_id = t.id
JOIN grades g ON g.subject_id = sb.id
JOIN students s ON g.student_id = s.id
WHERE t.id = 4 AND s.id = 20;