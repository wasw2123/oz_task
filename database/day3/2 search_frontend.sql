-- search name and salaly data
-- frontend and salary 90000
SELECT name, salary
FROM employees 
WHERE position = 'Frontend' AND salary <= 90000;