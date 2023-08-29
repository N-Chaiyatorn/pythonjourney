# SQL Aggregation

## GROUP BY statement
- **GROUP BY** statement will allow us to aggregate data and apply aggregate functions per category
- **GROUP BY** must be right after FROM or WHERE statement

- If we have group by, in **SELECT** statement, columns must either get wrapped by aggregate function or be in the **GROUP BY** call
```
SELECT category_col, AGGREGATE_FUNCTION(data_col)
FROM table
GROUP BY category_col

SELECT category_col, AGGREGATE_FUNCTION(data_col)
FROM table
WHERE category_col != 'A'
GROUP BY category_col
```

- Categorical column is a column we choose to be a category and in the **GROUP BY** call, in below example image the categorical column is `category`
![](group_by_example_1.png)

- We can have more than 1 categorical columns
```
SELECT category_col_1, category_col_2, AGGREGATE_FUNCTION(data_col)
FROM table
GROUP BY category_col_1, category_col_2
```

- WHERE statements should not be use on aggregation results, we will learn to use HAVING to apply filter on those results later