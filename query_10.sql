SELECT DISTINCT
    st.fullname,
    t.fullname,
    sb.name
FROM students st
JOIN grades g ON g.student_id = st.id
JOIN subjects sb ON g.subject_id = sb.id
JOIN teachers t ON t.id = sb.teacher_id
WHERE st.id = 15 AND t.id = 2;