# SQL CONDITIONAL EXPRESSION

## CAST
- **CAST** operator convert one data type to another
- Keep in mind not every instance of a data type can cast to another. Like 'Hello' can't be casted to INTEGER

Example

```
SELECT CAST('5' AS INTEGER), CAST(date as TIMESTAMP)


SELECT '5'::INTEGER -- PostgreSQL special syntax
```
