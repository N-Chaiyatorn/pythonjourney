# from turtle import Turtle, Screen

# timmy_the_turtle = Turtle()
# timmy_the_turtle.shape("turtle")        # ตั้งรูปร่างของเต่า
# timmy_the_turtle.color("#b14b7c")           # ตั้งสีของเต่า
# timmy_the_turtle.forward(100)           # เดินไปข้างหน้า 100
# timmy_the_turtle.right(45)              # หันไปทางขวา 45 องศา
# timmy_the_turtle.forward(100)


# screen = Screen()
# screen.exitonclick()

# Tuple and color random
# Tuple เป็นตัวเเปรที่ลักษณะคล้าย list เเต่ Tuple เป็นตัวเเปรที่ไม่สามารถเเก้ค่าข้างในได้เลย
# Tuple เหมือนเป็น list ที่ไม่สามารถเปลี่ยนค่าต่างๆ ข้างในได้เลย
# Ex. 
#           x = (1, 2, 3)
#           print(x[0])             ===> output:1
#           if define x[0] = 1
#           The result is  print(x[0]) ===> output:error
x = (1, 2, 3)

def random_color():
    r = random.ranint(0, 255)
    g = random.ranint(0, 255)
    b = random.ranint(0, 255)
    return (r, g, b)