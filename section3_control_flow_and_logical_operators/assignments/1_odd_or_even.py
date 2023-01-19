"""
Write a program that works out whether if a given number is an odd or even number.

Even numbers can be divided by 2 with no remainder.

e.g. `86 is even` because 86 ÷ 2 = 43

43 does not have any decimal places. Therefore the division is clean.

e.g. `59 is odd` because 59 ÷ 2 = 29.5

there is a remainder of 0.5, so the division is not clean.

### Example Input 1

```
43
```
### Example Output 1
```
This is an odd number.
```

_____________________________

### Example Input 2
```
94
```
### Example Output 2
```
This is an even number.
```
"""


input_number = int(input(""))                
is_remainder = bool(input_number % 2)            #The transformation input number that the remainder of The divided of input number by 2 into boolean        

if is_remainder:
    print("This is an odd number.")             #If isremainder is true its mean that the input number cannot divided by 2 
else:
    print("This is an even number.")            #If isremainder is false its mean that the input number can divided by 2 