# Draw trangle, square, pentagon, hexagon, heptagon, octagon, nonagon and decagon
# Draw with different color for each shape
# Each side length is 100
# Example: https://replit.com/@appbrewery/day-18-3-end

# hint:Every shape the total angle will be 360 

from turtle import Turtle, Screen
import random

# Determine class called 'Drawing_Shape_Process' to implement and drawing every side of shape
class Drawing_Shape_Process:
    def __init__(self):
        self.total_degree = 0
        self.total_shape = 3
    
    def drawing_each_shape_side(self):
        drawing_format.forward(100)
        drawing_format.right(180 - (self.total_degree / self.total_shape))

    def drawing_each_shape(self):
        self.total_degree += 180
        for each_side_drawing in range(self.total_shape):
            self.drawing_each_shape_side()
        self.total_shape += 1

    def is_still_drawing(self):
        return self.total_shape <= 10

# Define every object
drawing_format = Turtle()
screen = Screen()
drawing_shape_process = Drawing_Shape_Process()

while drawing_shape_process.is_still_drawing():
    screen.colormode(255)
    drawing_format.color((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
    drawing_shape_process.drawing_each_shape()

screen.exitonclick()


