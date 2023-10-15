# Creating databases and tables

## CREATE TABLE statement
- 

```
CREATE TABLE table_name (
    column_name1 TYPE COLUMN_CONSTRAINT,
    column_name2 TYPE COLUMN_CONSTRAINT,
    TABLE_CONSTAINT TABLE_CONSTAINT
) INHERITS existing_table_name

CREATE TABLE players (
    player_id SERIAL PRIMARY KEY,
    age SMALLINT NOT NULL,
    username VARCHAR(50) UNIQUE NOT NULL
    created_time TIMESTAMP NOT NULL
)
```

## CREATE Challenge
Try above query in pgAdmin