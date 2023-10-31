SELECT
    g.name,
    s.fullname
FROM groups g
JOIN students s ON s.group_id = g.id;