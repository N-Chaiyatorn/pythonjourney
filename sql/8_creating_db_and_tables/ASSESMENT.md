# Assessment Test

This will test your knowledge of the previous section, focused on creating databases and table operations. This test will actually consist of a more open-ended assignment below:

### Complete the following task:

Create a new database called "School" this database should have two tables: __teachers__ and __students__.

The __students__ table should have columns for student_id, first_name,last_name, homeroom_number, phone,email, and graduation year.

The __teachers__ table should have columns for teacher_id, first_name, last_name,

homeroom_number, department, email, and phone.

The constraints are mostly up to you, but your table constraints do have to consider the following:

1. We must have a phone number to contact students in case of an emergency.

2. We must have ids as the primary key of the tables

3. Phone numbers and emails must be unique to the individual.

Once you've made the tables, insert a student named Mark Watney (student_id=1) who has a phone number of 777-555-1234 and doesn't have an email. He graduates in 2035 and has 5 as a homeroom number.

Then insert a teacher names Jonas Salk (teacher_id = 1) who as a homeroom number of 5 and is from the Biology department. His contact info is: jsalk@school.org and a phone number of 777-555-4321.

__Keep in mind that these insert tasks may affect your constraints!__
# Each teacher can only take care only one homeroom or  less.
```
# Create teachers table
CREATE TABLE teachers(
	teacher_id SERIAL PRIMARY KEY,
	first_name VARCHAR(40) NOT NULL,
	last_name VARCHAR(40) NOT NULL,
	homeroom_number INTEGER UNIQUE,
	department VARCHAR(40),
	email VARCHAR(40),
	phone VARCHAR(40) NOT NULL,
	UNIQUE(email), 
    UNIQUE(phone)
)

# Create students table
CREATE TABLE students(
	student_id SERIAL PRIMARY KEY,
	first_name VARCHAR(40) NOT NULL,
	last_name VARCHAR(40) NOT NULL,
	homeroom_number INTEGER REFERENCES teachers(homeroom_number) NOT NULL,
	phone VARCHAR(40) NOT NULL,
	email VARCHAR(40),
	graduation_year INTEGER NOT NULL,
	
	UNIQUE(phone), 
    UNIQUE(email)
)

# Insert teachers first

INSERT INTO 
	teachers(first_name, last_name, 
			homeroom_number, department, phone, email)
VALUES 
	('Jonas', 'Salk', 5, 'Biology department', '777-555-4321', 'jsalk@school.org')

# Insert student, so student will come from defined homeroom_number from table only.
INSERT INTO 
	students(first_name, last_name, 
			homeroom_number, phone, email, 
			graduation_year)
VALUES 
	('Mark', 'Watney', 5, '777-555-1234', NULL, 2035)





```
## Results after insert tables.
### Students table
![](students_table_result.png)
### Teachers table
![](teachers_table_result.png)