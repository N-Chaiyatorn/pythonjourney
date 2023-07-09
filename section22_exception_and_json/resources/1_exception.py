# #FileNotFound
# with open("x.txt") as x:
#     x.read()

# #KeyError
# dictionary = {"key":"value"}
# value = dictionary["test"]

# #IndexError
# list_a = [1,2,3]
# list[3]

# #TypeError
# text = "test"
# print(text + 5)

# พวกชื่อ error ต่างๆเหล่านี้ เช่น TypeError IndexError KeyError FileNotFound จะเป็น class อย่างนึง

# Syntax for error(exception) catching
# 
"""
try     = Code that might cause an exception (เป็นรูปเเบบคำสั่งที่หลังตัวที่ประกาศ try คือ code หลักที่เราเอาไว้ทำงาน)
except  = Do this part if there is any exception (เป็นรูปเเบบคำสั่งที่จะทำงานก็ต่อเมื่อเกิด error ขึ้นใน code หลัก (เกิด error ใน code ภายในคำสั่ง try))
else    = Do this part if there is no exception (เป็นรูปเเบบคำสั่งที่จะทำงานหลังจากที่เรา run code หลักใน try เเล้วไม่เกิด error ใดๆ)
finally = Do this regardless
"""
# try:
#     file = open("a_file.txt")
#     dictionary = {"key":"value"}
#     print(dictionary["test"])
# except + type of error
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("")
# except KeyError as err:
#     print("Key error", err)
# else:
#     content = file.read()
#     print(content)
# finally:
#     file.close()
#     print("closed file")

# code ด้านบนมีลำดับการทำงานคือ ทำ try ก่อนจากนั้นทำ file = open("a_file.txt")
# จากนั้นเกิด FileNotFoundError ดังนั้นจึงไปทำ except FileNotFoundError ต่อ จากนั้นก็จะไปทำ finnally ต่อ
# จากนั้นเมื่อ run อีกรอบ ก็จะทำ file = open("a_file.txt") เเต่ไม่ FileNotFoundError เเล้วเเต่จะเกิด KeyError ต่อ


# custom exception (การสร้างรูปเเบบ error ขึ้น (โดย error ก็คือ classๆ นึง)โดยเราตั้งเงื่อนไขขึ้นมาเอง)
# height = float(input("height: "))

# if height >= 3:
#     raise ValueError("Invalid height input")            


# Quiz - Modify below code to sum the likes of each dict in the list without error, ignore dict without 'Likes' key
facebook_posts = [
    {'Likes': 21, 'Comments': 2}, 
    {'Likes': 13, 'Comments': 2, 'Shares': 1}, 
    {'Likes': 33, 'Comments': 8, 'Shares': 3}, 
    {'Comments': 4, 'Shares': 2}, 
    {'Comments': 1, 'Shares': 1}, 
    {'Likes': 19, 'Comments': 3}
]


total_likes = 0
for post in facebook_posts:
    try:
        total_likes = total_likes + post['Likes']
    except KeyError:
        pass

print(total_likes)