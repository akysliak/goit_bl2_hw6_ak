SELECT DISTINCT
    st.fullname,
    sb.name
FROM students st
JOIN grades g ON g.student_id = st.id
JOIN subjects sb ON g.subject_id = sb.id
WHERE st.id = 15;