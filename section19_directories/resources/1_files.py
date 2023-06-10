file = open("/Gittest/Python study/pythonjourney/section19_directories/resources/hi.txt")           # function ที่เอาไว้เปิดไฟล์ที่ต้องการ (เเค่เปิดขึ้นมาเเละเอาทั้งไฟล์ใส่ไปในตัวเเปร file เฉยๆ ยังดูเนื้อหาไฟล์ไม่ได้)
print(file)
# contents = file.read()
# print(contents)
# file.close()            # ทุกๆครั้งที่เปิดไฟล์มาทำ จะต้องปิดไฟล์ทุกครั้งหลังจากทำงานหรือใช้งานอะไรกับไฟล์เสร็จเเล้ว  

# read file using "with"
# with open("hi.txt") as file คือหมายถึงว่า file = open("hi.txt")
# with open("hi.txt") as file:              (if you didnt define any mode in open function its mean your mode will be mode = 'r' automically)
#     contents = file.read()
#     print(contents)

# overwrite file
# with open("hi.txt", mode="w") as file:          # Open file with mode ="w" its mean you open file with write only
#     file.write("New text")

# with open("hi2.txt", mode="w") as file:          # Open file with mode ="w" its mean you open file with write only
#     file.write("New text")

# with open("hi3.txt", mode="r") as file:          # Open file with mode ="w" its mean you open file with write only
#     file.read("New text")


# append file
# with open("hi.txt", mode="a") as file:
#     file.write("New text")