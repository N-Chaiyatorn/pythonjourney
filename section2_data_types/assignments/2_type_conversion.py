""" 
Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8

Warning: Do not change the code on lines 1-3. Your program should work for different inputs. e.g. any two-digit number.


### Example input
```
39
```

### Example Output
```
3 + 9 = 12
12
```

"""

# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

two_digit_number_integer = int(two_digit_number)                                    #The transformation of input number into integer variable    
first_digit_main_unit = two_digit_number_integer%10                                 #The fraction of input number
second_digit = two_digit_number_integer//10                                         #The digit of tens
The_additional_of_two_digit = first_digit_main_unit + second_digit                  #The additional of two digits number

print(f"{second_digit} + {first_digit_main_unit} = {The_additional_of_two_digit}")  #Print the additional of two digits  
print(first_digit_main_unit + second_digit)                                         #The result of two digits additional

