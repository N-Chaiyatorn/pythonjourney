# SQL CONDITIONAL EXPRESSION

## NULLIF
- **NULLIF** function takes in 2 inputs and returns null if both are equal, otherwise it returns the first argument passed
- Useful in cases where result could be something that we want to show it as null

Example

```
SELECT NULLIF(10, 0) -- return 10

SELECT NULLIF(0, 0) -- return null

SELECT NULLIF("HELLO", "") -- return HELLO

SELECT NULLIF("", "") -- return null
```
