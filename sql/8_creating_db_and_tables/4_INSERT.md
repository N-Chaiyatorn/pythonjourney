# Creating databases and tables

## INSERT statement
- INSERT allow you to add rows to a table

Example
```
INSERT INTO table (column_1, column_2, ...)
VALUES
    (value1, value2, ...),
    (value1, value2, ...),
```

- you can also insert the values referenced from another table

Example
```
INSERT INTO table(column1, column2, ...)
SELECT column1, column2, ...
FROM another table
WHERE condition
```

### Note
- Keep in mind, the inserted row values must match the table's columns, including constraints
- SERIAL columns don't need to be provided a value

## INSERT Challenge
Try INSERT in pgAdmin 
    - Try to use function like CURRENT_TIMESTAMP as a value in TIMESTAMP data type column