# ให้วาดสี่เหลี่ยมความยาวด้านละ 500 สีอะไรก็ได้
from turtle import Turtle, Screen
def draw_one_side():
    ben_ten.forward(100)
    ben_ten.right(90)

ben_ten = Turtle()
ben_ten.shape("arrow")
ben_ten.color("blue")

for i in range(4):
    draw_one_side()



screen = Screen()
screen.exitonclick()