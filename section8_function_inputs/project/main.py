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
    if number >= 2:
        divided_by_other = 0
        # Counting the amount of number that can divide given number
        for each_number in range(2, number):
            if number%each_number == 0:
                divided_by_other+=1
        # checking if there are the number other than 1 and themselve can divide given number so that is not a prime number
        if divided_by_other > 0:
            print(not_a_prime)
        else:
            print("It's a prime number.")
                
    else:
        print(not_a_prime)

#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)