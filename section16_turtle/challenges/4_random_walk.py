# Example: https://replit.com/@appbrewery/day-18-4-end

# Define every ... meter the turtle will change direction randomaly and change color randomaly
from turtle import Turtle, Screen
import random

turning_angle = ("forward", "right", "left")
def turn_around(turning_dir):
    if turning_dir == "right":
        turtle_pen.right(90)
    elif turning_dir == "left":
        turtle_pen.left(90)
    else:
        turtle_pen.right(0)
    

def move_and_turn():
    for sequence in range(random.randint(2, 100)):
        turtle_pen.speed(0)
        turtle_pen.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        turtle_pen.forward(100)
        turning_dir = random.choice(turning_angle)
        turn_around(turning_dir)
        
    
turtle_pen = Turtle()
turtle_pen.pensize(20)
screen = Screen()
screen.colormode(255)

move_and_turn()
screen.exitonclick()