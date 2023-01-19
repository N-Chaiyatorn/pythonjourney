""" 
Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.

It will take your current age as the input and output a message with our time left in this format:

You have x days, y weeks, and z months left.

Where x, y and z are replaced with the actual calculated numbers.

Warning: your output should match the Example Output format exactly, even the positions of the commas and full stops.


### Example Input
```
56
```

### Example Output
```
You have 12410 days, 1768 weeks, and 408 months left.
```

"""


user_age = input("")                            #Write your ages
user_age_number = int(user_age)                 #The transformation of user's ages to integer data
remainingg_years = 90 - user_age_number           #User's remaining ages
fou = 365 * remainng_years            #User's remaining days
remainng_weeks = 52 * remainng_years            #User's remaining weeks
remainng_months = 12 * remainng_years           #User's remaining years
print(f"You have {fou} days, {remainng_weeks} weeks, and {remainng_months} months left.")         #The result of user's times left 
