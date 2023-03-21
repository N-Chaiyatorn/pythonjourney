
# ในการใช้ method ถ้ามีค่าต่างๆ ของ attribute ที่เปลี่ยนไปใน method ถึงเเม้ว่าจะจบ method นั้นเเล้ว
# เเต่ ค่า attribute นั้นก็จะอิงค่าล่าสุดที่เปลี่ยนไปใน method เลยโดยที่ไม่จำเป็นต้อง return ตราบใดที่ method กับ attribute ที่เปลี่ยนไปนั้นมันอยู่ใน class เดียวกัน

# Ex.1 
# class test1():
#     def __init__(self):
#         self.attribute1 = 0
#         self.attribute2 = 1

#     def add(self, f):
#         f += 2
#         self.attribute1 += 1
# f = 1
# t1 = test1()
# t1.add(f)
# print(t1.attribute1)                 =====>The answer is 1
# print(f)                             =====>The answer is 1
# 
# Ex.2 
# class test1():
#      def __init__(self):
#          self.attribute1 = 0
#          self.attribute2 = 1

#      def add(self, f, t2):
#          f += 2
#          self.attribute1 += 1
#          t2.attribute1 += 1

# class test2():
#      def __init__(self):
#          self.attribute1 = 0
#          self.attribute2 = 1

#      def add(self, f):
#          f += 2
#          self.attribute1 += 1

# def add():
#     t2.attribute1 += 1

# f = 1
# t1 = test1()
# t2 = test2()
# t1.add(f, t2)
# add()
# print(t1.attribute1)              =====>The answer is 1             
# print(t2.attribute1)              =====>The answer is 2
# print(f)                          =====>The answer is 1

        