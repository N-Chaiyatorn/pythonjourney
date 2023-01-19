""" Type Conversion """

# Type Error
# len(100)
# "Hello" + 10  ====>ทำไม่ได้เนื่องจาก hello กับ 10 เป็น string กับ int ซึ่งบวกกันไม่ได้
# 10 + "Hello" 

# Type Check
print(type(100))
print(type(15.123))
print(type("Hello"))
print(type(True))

# Function type เป็นฟังก์ชั่นที่ใช้เช็คประเภทของตัวเเปรที่อยู่ใน func

# Type Conversion คือ การเปลี่ยน type จาก type หนึ่ง เป็นอีก type หนึ่ง
print(type(str(100)))     #str(100)   คือเปลี่ยนจาก 100 ที่เป็น int ให้เป็น string คือ "100"
print(type(str("1.2345")))      #str("1.2345") เปลี่ยนจาก "1.2345"  เป็น "1.2345"
print(type(int("1")))
print(type(float("1.123")))         #float("1.123") เปลี่ยนจาก "1.2345"  เป็น 1.2345
# print(type(int("1.123")))           int("1.123") จะไม่สามารถเปลี่ยน 1.123 เป็นตัวเเปรเเบบ int ได้
# สรุปคือ เปลี่ยน int เป็น float ได้ เเต่ไม่สามารถเปลี่ยนจาก float เป็น int ได้  
# print(type(int("asdqw")))
print(type(float("4")))         #float("4") เปลี่ยนจาก "4"  เป็น 4.0

