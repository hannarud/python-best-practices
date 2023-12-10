SELECT *
  FROM employee
 WHERE reports_to=1;


SELECT employee_id, last_name, first_name, title, reports_to, hire_date
  FROM employee
 WHERE NOT SUBSTRING(hire_date,1,4) = '2016'; -- We compare strings with strings

SELECT employee_id, last_name, first_name
  FROM employee
 WHERE LENGTH(first_name) > LENGTH(last_name);

SELECT *
  FROM employee
 WHERE 1=1;

SELECT first_name, last_name, title, birthdate
  FROM employee
 WHERE first_name = 'Nancy'
       OR first_name = 'Steve';

SELECT *
  FROM employee
 WHERE NOT SUBSTRING(first_name, 1, 1) = 'M'
       AND SUBSTRING(hire_date, 1, 4) = '2016';

SELECT last_name, first_name, hire_date, city
  FROM employee
 WHERE (SUBSTRING(hire_date, 1, 4) = '2016'
        AND SUBSTRING(first_name, 1, 1) = 'M'
       )
       OR NOT city='Calgary';

SELECT *
  FROM employee
 WHERE (LENGTH(first_name) = 5
        OR LENGTH(first_name) = 6
       )
       AND SUBSTRING(hire_date, 1, 4)='2017'
 LIMIT 2;

SELECT name AS name_longer_than_2h
  FROM track
 WHERE (CAST(milliseconds AS REAL) / 1000) / 60 > 60;

SELECT name AS name_between_17_and_19_min, (CAST(milliseconds AS REAL) / 1000) / 60 AS duration_minutes
  FROM track
 WHERE duration_minutes BETWEEN 17 AND 19;
