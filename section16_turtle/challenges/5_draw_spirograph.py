# Example: https://replit.com/@appbrewery/day-18-5-end
# Change color every sequence 

from turtle import Turtle, Screen
import random

turtle = Turtle()
screen = Screen()
screen.colormode(255)

def drawing_spirograph():
    cir_num = 0
    while cir_num < 36:
        turtle.speed(4)
        turtle.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        turtle.circle(100)
        cir_num += 1
        turtle.left(10)

drawing_spirograph()
screen.exitonclick()
       