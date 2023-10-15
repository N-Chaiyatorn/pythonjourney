# Creating databases and tables

## Constraints
- Constraints are the rules enforced on data columns on table
- It prevents invalid data to enter the database, thus ensure the accuracy and reliability of the data
- Divided into two main categories
    - Column Constraints: apply to a column
    - Table Constraints: apply to the entire table

### Example column constraints
- NOT NULL: Ensure a column can't contain NULL
- UNIQUE: Ensure a column are different
- PRIMARY KEY: Unique key used to identify the row in the table
- FOREIGN KEY: Constrains data based on column in other tables
- CHECK: Ensure value in a column satisfy certain condition
- REFERENCES: constrain the value stored in the column that must exist in a column in another table

## Example table constraints
- UNIQUE(column_list)
- PRIMARY KEY(column_list)
- CHECK(condition)
