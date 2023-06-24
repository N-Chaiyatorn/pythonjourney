# https://docs.python.org/3/library/datetime.html

import datetime as dt

now = dt.datetime.now()

year = now.year
month = now.month
day_of_week = now.weekday

date = dt.datetime(year=1998, month=12, day=15)