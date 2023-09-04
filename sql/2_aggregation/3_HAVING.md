# SQL Aggregation

## HAVING statement
- We can't use **WHERE** to filter based off of aggregate results. because those **aggregations happen after a WHERE is executure**
- **HAVING** statement allow us to use the aggregate result as a filter along with **GROUP BY**

```
SELECT company, SUM(sales)
FROM finance_table
WHERE company != 'Google'
GROUP BY category_col
HAVING SUM(sales) > 1000
```

## HAVING Challenge
- We are launching a platinum service for our most loyal customer. We will assign platinum status to customers that have had 40 or more transaction payments. What customer_id are eligible for platinum status
    - use the payment table
- What are the customer ids of customers who have spent more than 100 USD in payment transactions with our staff_id member 2
    - use the payment table