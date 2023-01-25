"""
You are going to write a program that calculates the average student height from a List of heights.

e.g. ```student_heights = [180, 124, 165, 173, 189, 169, 146]```

The average height can be calculated by adding all the heights together and dividing by the total number of heights.

e.g.

180 + 124 + 165 + 173 + 189 + 169 + 146 = 1146

There are a total of 7 heights in ```student_heights```

1146 ÷ 7 = __163.71428571428572__

Average height rounded to the nearest whole number = 164

___Important___: You should not use the ```sum()``` or ```len()``` functions in your answer. You should try to replicate their functionality using what you have learnt about for loops.

### Example Input
```
156 178 165 171 187
```
In this case, student_heights would be a list that looks like: `[156, 178, 165, 171, 187]`

### Example Output
```
171
```
"""

# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

total_height = 0
amount_of_student = 0
#Write your code below this row 👇
for student_height in student_heights:
  total_height += student_height
  amount_of_student += 1
  
print(round(total_height/amount_of_student))




