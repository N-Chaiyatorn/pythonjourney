# https://docs.python.org/3/library/datetime.html

# เรื่องที่เกี่ยวกับการจับเวลา
import datetime as dt

now = dt.datetime.now() # dt= module, datetime = class, now() = method ที่ใช้ในการดีงข้อมูลของเวลา ณ ปัจจุบัน
print(now)  # now เป็นข้อมูลวันเวลาปัจจุบัน เเต่ไม่ใช่ str

year = now.year
month = now.month
day_of_week = now.weekday()
print(day_of_week)

date = dt.datetime(year=1998, month=12, day=15)     # เป็นการประกาศ object ที่เอาไว้เก็บข้อมูลเวลา ณ เวลาที่เรากำหนดเองเลย
print(date)