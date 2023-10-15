# Creating databases and tables

## DELETE statement
- DELETE allows us to remove rows from a table

Example
```
-- Use unique identifier to delete
DELETE FROM table
WHERE row__id = 1

-- Delete based on their presence in other tables
DELETE FROM tableA
USING tableB
WHERE tableA.id = tableB.id

-- Delete all rows
DELETE FROM table
```

- Similar to UPDATE command, you can also add RETURNING to return rows those were removed

## DELETE Challenge
Try in pgAdmin