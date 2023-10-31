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