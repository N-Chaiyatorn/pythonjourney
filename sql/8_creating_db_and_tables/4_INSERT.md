# Creating databases and tables

## INSERT statement
- INSERT allow you to add rows to a table

Example
```
INSERT INTO table (column_1, column_2, ...)
VALUES
    (value1, value2, ...),
    (value1, value2, ...),
```

- you can also insert the values referenced from another table

Example
```
INSERT INTO table(column1, column2, ...)
SELECT column1, column2, ...
FROM another table
WHERE condition

For example:

INSERT INTO student(id, age, user_name)
SELECT player_id, age, username
FROM players
WHERE age >= (SELECT AVG(age) FROM players)

## The code above will get the row that players have age greater than average age and then insert that selected rows into student table.


```

### Note
- Keep in mind, the inserted row values must match the table's columns, including constraints
- SERIAL columns don't need to be provided a value
```
Serial columns คือ col ที่มี data type เป็น serial ซึ่งเป็น data type ของลำดับเลขตั้งเเต่ 1 - 147483647 ที่ไม่มีค่าซ้ำกันเเละจะเป็น col ที่เเต่ละเเถวจะมีค่าเรียงกันมักใช้กับ primary key เเละเป็นการเรียงลำดับตัวเลข ดังนั้นตอน insert row ก็ไม่จำเป็นต้องระบุ col ที่เป็น serial col ก็ได้เพราะ เมื่อ insert เเถวใหม่เเล้ว serial col จะทำการเพิ่ม col ล่าสุดโดยอัตโนมัติโดยอิงจากค่าของเเถวก่อนหน้า

เช่น 
CREATE TABLE Dog_name(
    id SERIAL PRIMARY KEY,
    name VARCHAR(20) NOT NULL
)

INSERT TABLE Dog_name(name)
VALUES  ("Timmy"),
        ("James"),
        ("Tom")

If you execute SELECT * FROM Dog_name
result will be 
id  |   name
1   |   Timmy
2   |   James
3   |   Tom

```

## INSERT Challenge
Try INSERT in pgAdmin 
    - Try to use function like CURRENT_TIMESTAMP as a value in TIMESTAMP data type column

```
INSERT INTO players(player_id, age, username, created_time)
VALUES 
	(4, 11, 'Kira', CURRENT_TIMESTAMP),
	(5, 17, 'Diavolo', CURRENT_TIMESTAMP),
	(6, 11, 'Jotaro', CURRENT_TIMESTAMP)
    
```