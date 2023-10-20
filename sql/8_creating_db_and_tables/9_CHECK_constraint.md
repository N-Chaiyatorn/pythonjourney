# Creating databases and tables

## CHECK statement
- CHECK constraint allows us to create more customized constraints

Example
```
CREATE TABLE adults (
    id SERIAL PRIMARY KEY,
    age SMALLINT CHECK(age > 20)
    parent_age SMALLINT CHECK(parent_age > age)
)
```
## CHECK Challenge
Crate your own table and columns with CHECK constraints then try to insert the data which doesn't satisfy your condition
```
CREATE TABLE total_income(
	id SERIAL PRIMARY KEY,
	first_name VARCHAR(20) NOT NULL,
	surname VARCHAR(20) NOT NULL,
	income_date TIMESTAMP NOT NULL,
	income MONEY CHECK(income <= CAST(70000 AS MONEY))
)

SELECT * FROM total_income
INSERT INTO total_income(first_name, surname, income_date, income)
VALUES
	('Peter', 'Anderson', TO_TIMESTAMP('2023-02-01, 00:00:00', 'YYYY-MM-DD HH24:MI:SS'), 85000)
```