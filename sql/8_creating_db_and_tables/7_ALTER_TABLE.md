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
```

- more details https://www.postgresql.org/docs/current/sql-altertable.html

## ALTER TABLE Challenge
Try in pgAdmin