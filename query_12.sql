WITH LastDate AS (
    SELECT
        s.id AS student_id,
        g.subject_id AS subject_id,
        MAX(g.grade_date) AS last_grade_date
    FROM grades g
    JOIN students s on s.id = g.student_id
    GROUP BY s.id, g.subject_id
    )
SELECT
    g.name,
    s.name,
    st.fullname,
    grades.grade,
    grades.grade_date
FROM groups g
JOIN students st ON st.group_id = g.id
JOIN grades ON grades.student_id = st.id
JOIN subjects s ON s.id = grades.subject_id
JOIN LastDate ON LastDate.student_id = grades.student_id
            AND LastDate.subject_id = grades.subject_id
            AND LastDate.last_grade_date = grades.grade_date
WHERE g.id = 3 AND s.id = 6
;