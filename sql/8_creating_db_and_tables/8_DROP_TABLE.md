# Creating databases and tables

## DROP statement
- DROP allows us to complete removal of a column in a table
- By default, we can't drop columns which are other tables's foreign key. We need to add CASCADE command to delete them.
- CASCADE will used to drop primary key column and undo foreign key refferences immediately.

Example
```
ALTER TABLE table_name
DROP COLUMN col_name

ALTER TABLE table_name
DROP COLUMN col_name CASCADE

-- Check before drop to avoid error
ALTER TABLE table_name
DROP COLUMN IF EXISTS col_name

-- Drop multiple columns
ALTER TABLE table_name
DROP COLUMN col1,
DROP COLUMN col2
```


## DROP Challenge
Try in pgAdmin
```
ALTER TABLE student
DROP COLUMN id CASCADE

```