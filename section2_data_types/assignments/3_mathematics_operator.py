"""
Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.

The BMI is a measure of someone's weight taking into account their height. e.g. If a tall person and a short person both weigh the same amount, the short person is usually more overweight.

The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):


Warning you should convert the result to a whole number.


### Example Input
```
weight = 80
height = 1.75
```

### Example Output
```
80 ÷ (1.75 x 1.75) = 26.122448979591837
26
```

"""
user_weight = input("weight = ")       #user's weight input      
user_height = input("height = ")       #user's height input  

user_weight_number = float(user_weight)               #The transformation of turning weight input into integer data
user_height_number = float(user_height)             #The transformation of turning height input into float data
user_total_BMI = user_weight_number/user_height_number**2       #The calculation of BMI

print(f"{user_weight} ÷ ({user_height} x {user_height}) = {user_total_BMI}")       #Print BMI solution
print(round(user_total_BMI))        #The total result of BMI in integer digits


