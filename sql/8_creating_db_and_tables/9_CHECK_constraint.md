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