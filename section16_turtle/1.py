from turtle import Turtle, Screen

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("red")
timmy_the_turtle.forward(100)
timmy_the_turtle.right(45)
timmy_the_turtle.forward(100)


screen = Screen()
screen.exitonclick()

# Tuple and color random
x = (1, 2, 3)

def random_color():
    r = random.ranint(0, 255)
    g = random.ranint(0, 255)
    b = random.ranint(0, 255)
    return (r, g, b)