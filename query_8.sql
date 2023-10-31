SELECT
    t.fullname,
    ROUND(AVG(g.grade), 2) AS average_grade
FROM teachers t
JOIN subjects s ON s.teacher_id = t.id
JOIN grades g ON g.subject_id = s.id
WHERE t.id=2
GROUP BY t.id;