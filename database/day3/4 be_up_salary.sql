-- backend up salary
SET SQL_SAFE_UPDATES = 0;
UPDATE employees SET salary = salary * 1.05 WHERE position = 'Backend';
SET SQL_SAFE_UPDATES = 1;
SELECT * FROM employees WHERE position = 'Backend';