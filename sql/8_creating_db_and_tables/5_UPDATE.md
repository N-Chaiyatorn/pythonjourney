# Creating databases and tables

## UPDATE statement
- UPDATE allows you to change the value of the columns in a table

Example
```
UPDATE table
SET column1 = value1,
    column2 = value2, ...
WHERE condition

UPDATE account
SET last_login = CURRENT_TIMESTAMP
WHERE last_login is NULL

-- Update based on another column within a table
UPDATE account
SET last_login = created_on

-- Use another table's values to update
UPDATE tableA
SET original_col = tableB.new_col
FROM tableB
WHERE tableA.id = tableB.id

-- Return affected rows
UPDATE account
SET last_login = created_on
RETURNING account_id, last_login
```

## UPDATE Challenge
Try above query in pgAdmin. Use your custom table or existing table
Ex1:
```
UPDATE payment 
SET amount = 0
WHERE amount is NULL

```
Ex2:
```
## If the players id is exist in student table then their vip status is True.

UPDATE players p
SET is_vip = True
FROM student s
WHERE p.id = s.id

RETURNING p.id, p.age, p.username, p.is_vip
```
Ex3:Using update with case when.
```
UPDATE test_1 t1
SET grade = g.grade
FROM (SELECT CASE 
WHEN score >= 80 THEN 'A'
WHEN score >= 75 THEN 'B+'
WHEN score >= 70 THEN 'B'
WHEN score >= 65 THEN 'C+'
WHEN score >= 60 THEN 'C'
WHEN score >= 55 THEN 'D+'
WHEN score >= 50 THEN 'D'
	ELSE 'F'
	END AS grade, id
FROM test_1 ) g

WHERE g.id = t1.id

```