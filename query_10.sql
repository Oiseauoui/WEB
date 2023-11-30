-- 10. Список курсів, які читає певний викладач для конкретного студента.
SELECT DISTINCT students.fullname, disciplines.name, teachers.fullname
FROM disciplines
JOIN teachers ON disciplines.teacher_id = teachers.id
JOIN groups ON disciplines.group_id = groups.id
JOIN students ON groups.id = students.group_id
WHERE students.fullname = 'Cory Walker' AND teachers.fullname = 'Catherine Moran';
