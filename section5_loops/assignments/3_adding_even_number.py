"""
You are going to write a program that calculates the sum of all the even numbers from 1 to 100. Thus, the first even number would be 2 and the last one is 100:

i.e. 2 + 4 + 6 + 8 +10 ... + 98 + 100

__Important__: there should only be 1 print statement in your console output. It should just print the final total and not every step of the calculation.
"""

#Write your code below this row 👇
total_calculation = 0
for even_number in range(101):
    if even_number % 2 == 0:
        total_calculation += even_number       #The summation of even number       
        test = even_number

print(f"The summation of even number from 2 to {test} is {total_calculation}")    #The result of calculation 

