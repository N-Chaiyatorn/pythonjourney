"""
# Tip Calculator Project


If the bill was $150.00, split between 5 people, with 12% tip.

Each person should pay (150.00 / 5) * 1.12 = 33.6

Format the result to 2 decimal places = 33.60

Thus everyone's share of the total bill is $30.00 plus a $3.60 tip.

Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪


### Example Input
```
Welcome to the tip calculator!
What was the total bill? $124.56
How much tip would you like to give? 10, 12, or 15? 12
How many people to split the bill? 7
```

### Example Output
```
Each person should pay: $19.93
```

"""
print("Welcome to the tip calculator!")
total_bill = input("What was the total bill? $")
percent_of_tip = input("How much tip would you like to give? 10, 12, or 15? ")
amount_of_people = input("How many people to split the bill? ")

total_bill_calculation = float(total_bill)
percent_of_tip_calculation = ((float(percent_of_tip))/100) + 1
amount_of_people_calculation = int(amount_of_people)
each_person_payment = (total_bill_calculation/amount_of_people_calculation)*percent_of_tip_calculation

print("Each person should pay: ${:0.2f}".format(each_person_payment))
