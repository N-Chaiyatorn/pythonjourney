# Creating databases and tables

## ALTER TABLE statement
ALTER TABLE allows us to change existing table structure such as
- Add, drop, rename columns
- Change columns data type
- Set default value for columns
- Add check constaints
- Rename table


Example
```
-- Basic syntax
ALTER TABLE table_name action

-- Adding columns
ALTER TABLE table_name
ADD COLUMN new_column TYPE

-- Removing Columns
ALTER TABLE table_name
DROP COLUMN column_name

-- Alter constraints
ALTER TABLE table_name
ALTER COLUMN col_name
SET DEFAULT value --or SET NOT NULL or ADD CONSTAINT constaint_name

Example for changing column attributes:
-- Add foreign_key constrain

ALTER TABLE table_a
ADD CONSTRAINT fk_new_col FOREIGN KEY (col_a) REFFERENCES table_b(col_a)

-- Add new constraint
ALTER TABLE table_name
ADD CONSTRIANT constraint_name CONSTRAIANT

-- Drop constraint
ALTER TABLE table_name
DROP constraint_name

-- Change column name
ALTER TABLE table_name
RENAME old_name TO new_name

-- Show every contain constraints in each schema
SELECT *
FROM information_schema.table_constraints 
```

- more details https://www.postgresql.org/docs/current/sql-altertable.html

## ALTER TABLE Challenge
Try in pgAdmin
Ex1:
```
ALTER TABLE game_list
ADD COLUMN description VARCHAR(100),
ADD COLUMN is_discount BOOL 
```
Ex2:
```
ALTER TABLE student 
DROP COLUMN age,
ADD COLUMN city VARCHAR(15),
ADD COLUMN email VARCHAR(15)
```
Ex3:
```
ALTER TABLE student 
ADD CONSTRAINT unique_city UNIQUE(city)
```
Ex4:
```
ALTER TABLE student 
DROP CONSTRAINT unique_city
```