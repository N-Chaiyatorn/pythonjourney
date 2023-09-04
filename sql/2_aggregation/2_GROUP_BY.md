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

(Group by:จะทำหน้าที่เเยกประเภทเเละจัดประเภทของข้อมูลตามค่าต่างๆที่เป็นไปได้ใน col ที่กำหนด โดยที่สามารถใช้งานร่วมกับ aggregation function ต่างๆ ได้ เช่น count, avg โดยที่ aggregation func จะทำการดำเนินการไปทีละ categories ข้อมูล เช่น ข้อมูล A ที่ไม่ได้จัดประเภท เวลาใช้ count(*) มันก็จะนับ จน เเถวทั้งหมดของข้อมูล A อย่างเดียว โดยที่ถ้า ข้อมูล B มีการ group by เเละเเยกข้อมูลเป็น 2 ประเภท คือ B.1 เเละ B.2
ดังนั้นเวลาใช้ count มันก็จะนับ จน เเถวทั้งหมดของข้อมูล B.1 เเละ return มาเป็นเเถวเเรก เเละ ต่อมาจะนับข้อมูลของเเถวใน B.2 เเละ return กลับมาในเเถวที่สอง)


- WHERE statements should not be use on aggregation results, we will learn to use HAVING to apply filter on those results later

## GROUP BY Challenge
- We have two staff members, with staff IDs 1 and 2. We want to give a bonus to the staff member that handled the most payments. Most in terms of number of payments processed, not total dollar amount. How many payments did each staff member handle and who gets the bonus?
    - use the payment table
```
SELECT staff_id, count(payment_id)
FROM payment

GROUP BY staff_id;
```
Staff id 2 will get bonus.
- Corporate HQ is conducting a study on the relationship between replacement cost and a movie MPAA rating (e.g. G, PG, R, etc.) What is the average replacement cost per MPAA rating?
    - use the film table
### solution 1: By not rounding replacement cost
```
SELECT AVG(replacement_cost),rating
FROM film 

GROUP BY rating
```
### solution 2: By rounding replacement cost
```
SELECT ROUND(AVG(replacement_cost)) AVG,rating
FROM film 

GROUP BY rating
```

- We are running a promotion to reward our top 5 customers with coupons. What are the customer ids of the top 5 customers by total spend?
    - use the payment table
    - use order by
```
SELECT customer_id, SUM(amount) total_spend
FROM payment

GROUP BY customer_id
ORDER BY total_spend DESC

LIMIT 5
```