# https://docs.python.org/3/library/turtle.html#turtle.listen

from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()       # screen

# def move_forward():
#     tim.forward(10)

screen.listen()         # ตั้ง screen ไว้คอย listen 

# Higher Order Function (HOF)
# คือ function ที่มี อีก function ในค่า input ของ function
# screen.onkey(key="space", fun=move_forward)        # ข้อควรระวังไม่ควรใส่วงเล็บเข้าไปใน function ที่เรา input เข้าไปเด็ดขาด     
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
    

# screen.onkey(key="w", fun=move_forward)
# screen.onkey(key="s", fun=move_backward)
# screen.onkey(key="a", fun=turn_left)
# screen.onkey(key="d", fun=turn_right)
# screen.onkey(key="c", fun=clear)
# screen.exitonclick()


def typing_k():
    tim.pendown()
    tim.pencolor("red")
    tim.right(45)
    tim.forward(50)
    tim.backward(50)
    tim.left(90)
    tim.forward(50)
    tim.backward(50)
    tim.left(135)
    tim.forward(20)
    tim.right(90)
    tim.forward(50)
    tim.backward(100)
    tim.penup()
    tim.home()
    

def typing_e():
    tim.pendown()
    tim.pencolor("red")
    tim.forward(50)
    tim.backward(50)
    tim.left(90)
    tim.forward(50)
    tim.right(90)
    tim.forward(50)
    tim.backward(50)
    tim.right(90)
    tim.forward(100)
    tim.left(90)
    tim.forward(50)
    tim.penup()
    tim.home()

def typing_i():
    tim.pendown()
    tim.pencolor("red")
    tim.left(90)
    tim.forward(50)
    tim.penup()
    tim.forward(10)
    tim.pendown()
    tim.dot(5)
    tim.penup()
    tim.backward(10)
    tim.pendown()
    tim.backward(100)
    tim.penup()
    tim.home()

tim.pendown()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear)
screen.onkey(key="k", fun=typing_k)
screen.onkey(key="e", fun=typing_e)
screen.onkey(key="i", fun=typing_i)
screen.exitonclick()
