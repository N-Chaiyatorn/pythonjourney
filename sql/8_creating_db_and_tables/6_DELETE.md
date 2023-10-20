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
Ex1:
```
# We want to delete every rows that prices column is null.
DELETE FROM game_list
WHERE prices IS NULL
```
Ex2: Delete reffernce from another table.:
```
# The table vip_student have every grade student here!!(Grade:F-A), so in table vip_student we only want every students that have grade 'A' only but in table vip_student don't have any grade column to be compared so we going to use 'using'
statement to get student table student and compare what id that have grade 'A'.

DELETE FROM vip_student vs
USING student s
WHERE vs.id(FK refference to s.id) = s.id(PK) AND s.grade != 'A' 

```