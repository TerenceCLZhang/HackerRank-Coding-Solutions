SELECT name
FROM Students
WHERE marks > 75
ORDER BY RIGHT(name, 3) ASC, ID ASC;