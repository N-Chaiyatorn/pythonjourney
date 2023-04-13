# List comprehension
list = [1,2,3]
new_list = [n + 1 for n in list]
print(new_list)

new_list_2 = [n for n in list if n == 2]
print(new_list_2)

exercise_list_1 = [1,2,3,4,5,6,7,8,9]
exercise_list_2 = ["Angela", "David", "Conley", "James"]

# square the number in exercise_list_1 

# Filter even number in exercise_list_1

# make the name in exercise_list_2 which longer than 5 characters to be uppercase

# filter file_1.txt and file_2.txt overlapped number



# Dictionary comprehension
names = ["Pan", "Jean"]
import random
student_scores = {student:random.randint(1, 100) for student in names}
passed_student = {student:score for (student, score) in student_scores.items() if score >= 60}


weather_c = {
    "Sunday": 20.7,
    "Monday": 25.1,
    "Tuesday": 26.2,
    "Wednesday": 26.0,
    "Thursday":24.9,
    "Friday":23.7,
    "Saturday":24.3
}

# make weather_c to be in farenheit