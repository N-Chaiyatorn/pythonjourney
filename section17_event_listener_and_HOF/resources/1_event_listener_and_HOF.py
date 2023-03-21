# https://docs.python.org/3/library/turtle.html#turtle.listen

from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()       # screen

# def move_forward():
#     tim.forward(10)

screen.listen()         # ตั้ง screen ไว้คอย listen 

# Higher Order Function (HOF)
# คือ function ที่มี อีก function ในค่า input ของ function
# screen.onkey(key="space", fun=move_forward)        # ข้อควรระวังไม่ควรใส่วงเล็บเข้าไปใน function ที่เรา nput เข้าไปเด็ดขาด     
# screen.exitonclick()


# Challenge
def move_forward():
    tim.forward(10)

def move_backward():
    tim.backward(10)

def turn_left():
    tim.left(10)

def turn_right():
    tim.right(10)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear)
screen.exitonclick()
