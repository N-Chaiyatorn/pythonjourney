# SQL Functions

## Timestamp
PostgreSQL can hold date and time information
- TIME: Contains only time
- DATE: Contains only date
- TIMESTAMP: Contains date and time
- TIMESTAMPTZ: Contains date, time and timezone

These are some functions and operations related to the specific data types
- TIMEZONE
- NOW
- TIMEOFDAY
- CURRENT_TIME
- CURRENT_DATE

Try this in the pgAdmin
```
SELECT NOW(), TIMEOFDAY(), CURRENT_DATE()
```

## Extract
Let's explore extracting information from a time based data type using
- EXTRACT(YEAR FROM date_col): Allows you tto extract sub-component of a date value i.e. YEAR, MONTH, DAY, WEEK, QUARTER
- AGE(date_col): Calculate current age given a timestamp
- TO_CHAR(date_col, 'mm-dd-yyyy'): Convert to text, more details on https://www.postgresql.org/docs/12/functions-formatting.html

## Challenge
1. Which months did payments occur? Format your answer to return the full month name
2. How many payments occurred on Monday