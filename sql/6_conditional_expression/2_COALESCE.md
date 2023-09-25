# SQL CONDITIONAL EXPRESSION

## COALESCE
- **COALESCE** function retturns the first argument that is not null. If all arguments are null, then it returns null.
- Accepts unlimited number of arguments

Example

```
SELECT COALESCE(column1, column2, column3)
FROM table


SELECT COALESCE(1, 2, 3) -- this return 1
FROM table


SELECT COALESCE(null, 2, 3) -- this return 2
FROM table


SELECT COALESCE(null, null, 3) -- this return 3
FROM table
```
