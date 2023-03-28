import turtle

screen = turtle.Screen()
screen.title("U.S. States Game")

image_path = "blank_states_img.gif"
screen.addshape(image_path)
turtle.shape(image_path)

def get_mouse_click_coord(x, y):
    print(x, y)
turtle.onscreenclick(get_mouse_click_coord)

answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?")

turtle.mainloop()