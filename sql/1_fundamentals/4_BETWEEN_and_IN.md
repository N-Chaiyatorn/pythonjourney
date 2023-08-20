# SQL Fundamentals - Syntax

## BETWEEN statement
**BETWEEN** operator can be used to match a value against a range of values. These two are the same 

```
column >= low_value AND column <= high_value
column between low_value and high_value
```

We can also combined **BETWEEN** with **NOT**

```
column NOT BETWEEN low_value AND high_value
```

Lastly, BETWEEN can also apply with dates but you need to format to YYYY-MM-DD format and timestamp also matters
Example: 

```
SELECT *
FROM payment
WHERE payment_date BETWEEN '2007-02-01' AND '2007-02-14'
```

## IN statement
**IN** operator can be used to check multiple values.

```
value IN (value_1, value_2)
```

Lastly, BETWEEN can also apply with dates but you need to format to YYYY-MM-DD format and timestamp also matters
Example: 

```
SELECT color
FROM color_table
WHERE color IN ('red', 'green')
```

### Challenge
research on LIKE and ILIKE statements