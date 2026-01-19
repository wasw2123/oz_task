-- del min
SET SQL_SAFE_UPDATES = 0;
DELETE FROM employees WHERE name = '민혁';
SET SQL_SAFE_UPDATES = 1;
SELECT * FROM employees;