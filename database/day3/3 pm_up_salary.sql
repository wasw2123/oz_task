-- pm up salary
SET SQL_SAFE_UPDATES = 0;
UPDATE employees SET salary = salary * 1.1 WHERE position = 'PM';
SET SQL_SAFE_UPDATES = 1;
SELECT * FROM employees WHERE position = 'PM';
