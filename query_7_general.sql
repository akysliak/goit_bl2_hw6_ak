SELECT
    g.name,
    s.name,
    grades.grade
FROM groups g
LEFT JOIN students st ON st.group_id = g.id
LEFT JOIN grades ON st.id = grades.student_id
LEFT JOIN subjects s ON s.id = grades.subject_id;