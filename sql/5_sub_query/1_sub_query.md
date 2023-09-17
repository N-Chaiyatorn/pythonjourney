# Sub Query
- A sub query allows you to construct complex queries, performing a query on the results of another query
- The syntax involves at least two **SELECT** statements. Example
```
SELECT student, grade
FROM test_scores
WHERE grade > (SELECT AVG(grade) FROM test_scores)
```
- The sub query is performed first since it's inside the parenthesis
- We can also use **IN** operator in conjunction with a sub query to check against multiple results. Example
```
SELECT student, grade
FROM test_scores
WHERE student IN (SELECT student FROM some_table)
```

## EXISTS operator
- Used to test for the existence of rows in a sub query
- Typically a sub query is passed in the **EXISTS** operator to check if any rows are returned with the subquery
```
SELECT column
FROM table
WHERE EXISTS (SELECT column FROM table WHERE condition)
```

________

### Try these example in the pgAdmin
```
SELECT title, rental_rate
FROM film
WHERE rental_rate > (SELECT AVG(rental_rate) FROM film)



SELECT film_id, title
FROM film
WHERE film_id IN (
    SELECT iv.film_id
    FROM rental rt
    INNER JOIN inventory iv ON iv.inventory_id = rt.inventory_id
    WHERE return_date BETWEEN '2005-05-29' AND '2005-05-30'
)
ORDER BY film_id



SELECT first_name, last_name
FROM customer c
WHERE EXISTS (
    SELECT *
    FROM payment p
    WHERE p.customer_id  = c.customer_id
        AND amount > 11
)
```