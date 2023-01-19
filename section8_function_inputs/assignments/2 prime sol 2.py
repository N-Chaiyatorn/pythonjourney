"""
Prime numbers are numbers that can only be cleanly divided by themselves and 1.

https://en.wikipedia.org/wiki/Prime_number

You need to write a function that checks whether if the number passed into it is a prime number or not.

e.g. 2 is a prime number because it's only divisible by 1 and 2.

But 4 is not a prime number because you can divide it by 1, 2 or 4.


### Example Input 1
```
73
```
### Example Output 1
```
It's a prime number.
```
### Example Input 2
```
75
```
### Example Output 2
```
It's not a prime number.
```
"""
#Write your code below this line 👇
def prime_checker(number):
    not_a_prime = "It's not a prime number."
    a_prime = "It's a prime number."
    if number >= 2:
        can_divided_by = 0
        for each_number in range(1, number+1):
            if number%each_number == 0:
                can_divided_by+=1
        if can_divided_by <= 2:
            print(a_prime)
        elif can_divided_by > 2:
            print(not_a_prime)
    else:
        print(not_a_prime)

#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)