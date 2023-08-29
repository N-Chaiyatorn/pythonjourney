# SQL Aggregation

## Aggregate functions
- **GROUP BY** Operator will allow us to aggregate data and apply functions to better understand how data look like per category
- The main idea behind aggregation is to take multiple inputs (from each row's column value) and return a single output
- To aggregate data, we need **aggregate functions** to get the output we want. For example 
    - AVG(column)   - returns a float with many decimal places e.g. 1.64598, we can use ROUND() to specify the precision
    - COUNT(column) - we can use COUNT(*) to check the number of rows
    - MAX(column)
    - MIN(column)
    - SUM(column)
- see more functions here [https://www.postgresql.org/docs/current/functions-aggregate.html]


Example: 

```
SELECT AVG(replacement_cost), MAX(replacement_cost), MIN(replacement_cost)
FROM film
```
