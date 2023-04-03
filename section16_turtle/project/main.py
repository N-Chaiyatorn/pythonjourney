import colorgram
from turtle import Turtle, Screen
import random
# วาดรูป 10 เเถวเเถวละ 10 จุด 

def set_new_line(y_position):
    turtle.speed(0)
    turtle.penup()
    turtle.setx(-285)
    turtle.sety(y_position)

def drawing_circle(colors_list):
    turtle.pendown()
    randomaly_circle_color = random.choice(colors_list)
    turtle.color(randomaly_circle_color, randomaly_circle_color)
    turtle.begin_fill()
    turtle.circle(20)
    turtle.end_fill()

rgb_colors = []
colors = colorgram.extract('section16_turtle/project/image.jpg', 30)       #         

for color in colors:
    color_position = (color.rgb.r, color.rgb.g, color.rgb.b)
    rgb_colors.append(color_position)

screen = Screen()
screen.colormode(255)
turtle = Turtle()
current_y_position = 195
for circle_row in range(10):
    set_new_line(y_position = current_y_position)
    for circle_column in range(10):
        drawing_circle(colors_list = rgb_colors)
        turtle.penup()
        turtle.forward(70)
    
    current_y_position -= 50

screen.exitonclick()

