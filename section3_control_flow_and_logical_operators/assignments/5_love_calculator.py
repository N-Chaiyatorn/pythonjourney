"""
You are going to write a program that tests the compatibility between two people.

To work out the love score between two people:

Take both people's names and check for the number of times the letters in the word TRUE occurs. 

Then check for the number of times the letters in the word LOVE occurs. 

Then combine these numbers to make a 2 digit number.

## For Love Scores less than 10 or greater than 90, the message should be:
```
"Your score is **x**, you go together like coke and mentos."
```
## For Love Scores between 40 and 50, the message should be:
```
"Your score is **y**, you are alright together."
```

## Otherwise, the message will just be their score. e.g.:
```
"Your score is **z**."
```

### Example
```
name1 = "Angela Yu"
name2 = "Jack Bauer"
```
T occurs 0 times
R occurs 1 time
U occurs 2 times
E occurs 2 times
Total = 5

L occurs 1 time
O occurs 0 times
V occurs 0 times
E occurs 2 times
Total = 3

Love Score = 53

Print: `"Your score is 53."`

### Example Input 1
```
name1 = "Kanye West"
name2 = "Kim Kardashian"
```
### Example Output 1
```
Your score is 42, you are alright together.
```
_____________________
### Example Input 2
```
name1 = "Brad Pitt"
name2 = "Jennifer Aniston"
```
### Example Output 2
```
Your score is 73.
```
"""

name1 = input("name1 = ")
name2 = input("name2 = ")

counting_T = name1.count("T") + name1.count("t") + name2.count("T") + name2.count("t")
counting_R = name1.count("R") + name1.count("r") + name2.count("R") + name2.count("r")
counting_U = name1.count("U") + name1.count("u") + name2.count("U") + name2.count("u")
counting_E = name1.count("E") + name1.count("e") + name2.count("E") + name2.count("e")
total_counting_of_TRUE = counting_T + counting_R + counting_U + counting_E                  #The amount of TRUE character in name1 and name2           

counting_L = name1.count("L") + name1.count("l") + name2.count("L") + name2.count("l")
counting_O = name1.count("O") + name1.count("o") + name2.count("O") + name2.count("o")
counting_V = name1.count("V") + name1.count("v") + name2.count("V") + name2.count("v")
counting_E = name1.count("E") + name1.count("e") + name2.count("E") + name2.count("e")
total_counting_of_LOVE = counting_L + counting_O + counting_V + counting_E                  #The amount of LOVE character in name1 and name2                 

total_love_score = (total_counting_of_TRUE * 10) + total_counting_of_LOVE                   #The calculation of love score       

if total_love_score < 10 or total_love_score > 90:
    print(f"Your score is {total_love_score}, you go together like coke and mentos.")
elif 40 < total_love_score < 50:
    print(f"Your score is {total_love_score}, you are alright together.")  
else:
    print(f"Your score is {total_love_score}.")  












