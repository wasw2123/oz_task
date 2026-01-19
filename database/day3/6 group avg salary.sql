-- group avg salary
SELECT position, AVG(salary) 
FROM employees
GROUP BY position;