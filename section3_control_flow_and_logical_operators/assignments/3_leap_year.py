"""
Write a program that works out whether if a given year is a leap year. A normal year has 365 days, leap years have 366, with an extra day in February. The reason why we have leap years is really fascinating, this video does it more justice:

https://www.youtube.com/watch?v=xX96xng7sAE

This is how you work out whether if a particular year is a leap year.

on every year that is evenly divisible by 4 

**except** every year that is evenly divisible by 100 

**unless** the year is also evenly divisible by 400

e.g. The year 2000:

2000 ÷ 4 = 500 (Leap)

2000 ÷ 100 = 20 (Not Leap)

2000 ÷ 400 = 5 (Leap!)

So the year 2000 is a leap year.

But the year 2100 is not a leap year because:

2100 ÷ 4 = 525 (Leap)

2100 ÷ 100 = 21 (Not Leap)

2100 ÷ 400 = 5.25 (Not Leap)

### Example Input 1
```
2400
```
### Example Output 1
```
Leap year.
```
______________________
### Example Input 2
```
1989
```
### Example Output 2
```
Not leap year.
```
"""

years_requirement = int(input(""))                        

isdividedby4 = bool(years_requirement % 4)         #The checking of remainder of years divided by 4 and transform remainder into boolean data              
isdividedby100 = bool(years_requirement % 100)     #The checking of remainder of years divided by 100 and transform remainder into boolean data    
isdividedby400 = bool(years_requirement % 400)     #The checking of remainder of years divided by 400 and transform remainder into boolean data    

if not isdividedby4:
    if not isdividedby100:
        if not isdividedby400:
            print("Leap year.")           #If years requirement can be divided by 4,100 and 400 that year is leap years 
        else:
            print("Not leap year.")       #If years requirement can be divided by 4 and 100 but can't be divided by 400 that year is not leap years 
    else:
        print("Leap year")                #If years requirement can be divided by 4 but can't be divided by 100 and 400 that year is leap years 
else:
    print("Not leap year.")               #If years requirement can't be divided by 4,100 and 400 that year is not leap years       

    


