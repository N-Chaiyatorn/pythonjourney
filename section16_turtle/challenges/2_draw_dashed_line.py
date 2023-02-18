# Example: https://replit.com/@appbrewery/day-18-2-end
from turtle import Turtle, Screen

def drawing_dotted_line():

    # Implement the class set into every object
    turtle = Turtle()
    screen = Screen()
    # drawing dotted line function
    def drawing_line():
        turtle.forward(10)
        turtle.penup()
        turtle.forward(10)
        turtle.pendown()

    for i in range(15):
        drawing_line()

    screen.exitonclick()

drawing_dotted_line()