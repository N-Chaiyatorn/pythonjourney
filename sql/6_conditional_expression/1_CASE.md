# SQL CONDITIONAL EXPRESSION

## CASE
- **CASE** statement allow us to get columns based on our conditions, which is similar to IF/ELSE statement in programming languages

Example

```
SELECT CASE
        WHEN condition1 THEN result1
        WHEN condition2 THEN result2
        ELSE other_result
       END
FROM table


SELECT a,
       CASE
          WHEN a = 1 THEN 'one'
          WHEN a = 2 THEN 'two'
          ELSE 'unknown'
       END AS string_name
FROM table


SELECT customer_id
       ,CASE
          WHEN customer_id <= 100 THEN 'Premium'
          WHEN customer_id BETWEEN 100 and 200 THEN 'PLUS'
          ELSE 'Normal'
        END AS customer_status
FROM customer
```


## CASE Challenge
- We want to know and compare the various amounts of films we have per movie rating
- use CASE and the dvdrental database to re-create this table below

![](CASE_challenge.png)
