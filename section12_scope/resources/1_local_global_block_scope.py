# Local Scope
# def local_scope():
#     y = 2
#     print(y)                  ===> result is 2
# local_scope()
# print(y)                       ===> result is error


# Global Scope
# a = 1 (global scope)
# def global_scope():
#     b = 2
#     print(a)   (local scope)                 ===> result is 2
# global_scope()


# Block scope   ====>ในภาษาอื่น คือ {}    เเต่ python ไม่มี block scope
# def block_scope():
#     a = 1
#     if True:
#         b = a
#     print(b)
# block_scope()


# Extra: modify global scope
# a = 1
# def modify_global_scope():
#     global a                      
#     a += 2
#     print(a)
# modify_global_scope()
# print(a)              ====> result is 3

# Global constant    ====> ค่าคงที่ที่ไม่ควรจะเปลี่ยนเเปลงเลย เราควรจะประกาศชื่อตัวเเปรให้เป็นตัวพิมพ์ใหญ่ทั้งหมด
# PI = 3.14159
# GOOGLE_URL = "www.google.com"
