SELECT CEIL(AVG(Salary) - AVG(CAST(REPLACE(Salary, 0, "") AS DECIMAL)))
FROM EMPLOYEES;