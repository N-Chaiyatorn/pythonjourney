# # List comprehension
# list = [1,2,3]
# new_list = [n + 1 for n in list]      # [ตัวที่อยากได้ for ตัวเเต่ละตัวใน list in list]
# # [n + 1 for n in list] == for n in list:
# print(new_list)     # [2, 3, 4]  

# new_list_2 = [n for n in list if n == 2]
# print(new_list_2)                   # output is [2] 

# exercise_list_1 = [1,2,3,4,5,6,7,8,9]
# exercise_list_2 = ["Angela", "David", "Conley", "James"]

# # square the number in exercise_list_1 
# new_list_1 = [number**2 for number in exercise_list_1]
# print(new_list_1)

# # Filter even number in exercise_list_1
# new_list_2 = [number for number in exercise_list_1 if number%2 == 0]
# print(new_list_2)

# # make the name in exercise_list_2 which longer than 5 characters to be uppercase(ตัวพิมพ์ใหญ่)
# new_list_3 = [name.upper() for name in exercise_list_2 if len(name) > 5]
# print(new_list_3)

# filter file_1.txt and file_2.txt overlapped number



# Dictionary comprehension
names = ["Pan", "Jean"]
import random
student_scores = {student:random.randint(1, 100) for student in names}   # เป้นการไล่ loop for โดยการ    
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

weather_f = {day:round((celcius * 9/5) + 32, 2) for (day, celcius) in weather_c.items()}
print(weather_f)