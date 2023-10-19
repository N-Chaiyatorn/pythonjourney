# Creating databases and tables

## SQL Basic Data types
- Boolean: True, False
- Character: CHAR (ตัวอักษรตัวเดียว), VARCHAR (ตัวอักษรเเบบจำกัด จน. EX:VARCHAR(200)), TEXT (str ยาวๆ )
## Difference between VARCHAR(20) vs VARCHAR(200)
VARCHAR(max_size):In gennerally the size of data that storaged in database is depend on max_size if you define high max_size the data that you have storaged in each row will be high , even if you characters in each row didn't reach max_size therfore max_size will also define the maximum characters in each row.
### Example
```
VARCHAR(20) ===> 'Hello' ===> data_size is 20 
VARCHAR(200) ===> 'Hello' ===> data_size is 200
```
- Numeric (ข้อมูลประเภทตัวเลข): INTEGER, FLOAT, DECIMAL
### Example
```
CREATE TABLE test(
    col1 NUMERIC(total_len_of_num(including decimal part), total_decimal_part)
    (You also can use DECIMAL(num_len, decimal_len).)
)
```
```
CREATE TABLE test(
    col1 NUMERIC(5, 2) ===> total digits part is 5, total decimal part is 2
)
(which means the col1 will only have two number in decimal part)
ex. INSERT INTO test (col1)
    VALUES (323.5891)

result will be:

col1
(5, 2)
______
323.59
```
- Temporal: date, time, timestamp, interval
- UUID: Universally Unique Identifier
- Array
- JSON
- Other special types: Network Address, Geometric data
- see more at postgresql.org/docs/current/datatype.html

### Challenge
Which data type is suit for these data?
- Username 
ans: VARCHAR
- User status (VIP or non-VIP) 
ans: BOOL (col_name:is_vip)
- Latitude and Longtitude of user
ans: point
- Phone number
ans: VARCHAR
