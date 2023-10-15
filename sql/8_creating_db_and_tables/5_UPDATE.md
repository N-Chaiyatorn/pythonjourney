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