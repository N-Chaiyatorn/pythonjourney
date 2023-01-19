"""
Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.

It should tell them the interpretation of their BMI based on the BMI value.

Under 18.5 they are underweight
Over 18.5 but below 25 they have a normal weight
Over 25 but below 30 they are slightly overweight
Over 30 but below 35 they are obese
Above 35 they are clinically obese.

### Example Input
```
weight = 85
height = 1.75
```
### Example Output
```
85 ÷ (1.75 x 1.75) = 27.755102040816325
Your BMI is 28, you are slightly overweight.
```
"""

user_weight = input("weight = ")
user_height = input("height = ")

user_weight_cal = float(user_weight)
user_height_cal = float(user_height)

#The calculation of BMI     
actual_bmi = user_weight_cal / (user_height_cal ** 2)              
#The rounding of BMI result   
approximate_bmi = round(actual_bmi)                                          

print(f"{user_weight} ÷ ({user_height} x {user_height}) = {actual_bmi}")

if approximate_bmi < 18.5 :
    print(f"Your BMI is {approximate_bmi}, you are underweight.")             
elif approximate_bmi < 25 :
    print(f"Your BMI is {approximate_bmi}, you have a normal weight.")
elif approximate_bmi < 30 :
    print(f"Your BMI is {approximate_bmi}, you are slightly overweight.")
elif approximate_bmi < 35 :
    print(f"Your BMI is {approximate_bmi}, you are obese.")
else:
    print(f"Your BMI is {approximate_bmi}, you are clinically obese.")

