<!-- Select Queries -->
SELECT *                
FROM users;

SELECT * 
FROM faves;

SELECT *  
FROM follows;
<!-- SELECT W/Conditionals -->
SELECT first_name
FROM users
WHERE id = 2;

SELECT last_name
FROM users
WHERE id = 2 OR id = 3;

SELECT *
FROM users
WHERE id > 2;

SELECT * 
FROM users
WHERE first_name LIKE "%e";

SELECT * 
FROM users
WHERE first_name NOT LIKE "K%";
<!-- SELECT W/ Sorting -->

SELECT *
FROM users
ORDER BY birthday DESC;

SELECT *
FROM users
ORDER BY birthday ASC;

SELECT *
FROM users
WHERE first_name LIKE "%e"
ORDER BY birthday DESC;

SELECT first_name
FROM users
ORDER BY first_name;

<!-- SELECT w/ Limit and Offset -->

<!-- What query would you run to get the first 3 users? -->
SELECT *
FROM users
LIMIT 3;
<!-- What query would you run to get user records 3-5? -->
SELECT *
FROM users
LIMIT 3
OFFSET 2;
<!-- You could also combine LIMIT and OFFSET like this: -->
SELECT *
FROM users
LIMIT 2,3;



