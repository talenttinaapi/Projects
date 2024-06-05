
SELECT employee_id, device_id
FROM employees;

SELECT *
FROM employees;

SELECT customerid, city, country
FROM customers
ORDER BY city;

SELECT*
FROM log_in_attempts
WHERE country = 'RSA';

SELECT*
FROM log_in_attempts
WHERE country LIKE 'SA%';

SELECT*
FROM log_in_attempts
WHERE time > '18:00';

SELECT*
FROM machines
WHERE OS_patch_date BETWEEN '2023-03-01' AND '2023-07-31';

SELECT*
FROM machines
WHERE operating_system = 'OS 1' AND email_client = 'Email client 1';

SELECT*
FROM machines
WHERE operating_system = 'OS 1' OR operating_system = 'OS 3';

SELECT*
FROM machines
WHERE NOT operating_system = 'OS 3';


SELECT*
FROM machines
WHERE operating_system IN ('OS 1', 'OS 3');
OUTER JOIN
SELECT*
=======
SELECT employee_id, device_id
FROM employees;

SELECT *
FROM employees;

SELECT customerid, city, country
FROM customers
ORDER BY city;

SELECT*
FROM log_in_attempts
WHERE country = 'RSA';

SELECT*
FROM log_in_attempts
WHERE country LIKE 'SA%';

SELECT*
FROM log_in_attempts
WHERE time > '18:00';

SELECT*
FROM machines
WHERE OS_patch_date BETWEEN '2023-03-01' AND '2023-07-31';

SELECT*
FROM machines
WHERE operating_system = 'OS 1' AND email_client = 'Email client 1';

SELECT*
FROM machines
WHERE operating_system = 'OS 1' OR operating_system = 'OS 3';

SELECT*
FROM machines
WHERE NOT operating_system = 'OS 3';

SELECT*
INNERT JOIN employees


