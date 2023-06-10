import turtle
import pandas
from turtle import Turtle

answerd_state = []
def type_new_state(user_correct_state_guess):
    '''Typing new correct state guess in U.S state map'''
    correct_state_list = user_correct_state_guess.values.tolist()
    text.setposition(correct_state_list[0][1], correct_state_list[0][2])
    text.write(correct_state_list[0][0], True, align="center")

def text_class_setup(text):
    text.penup()
    text.hideturtle()
    text.speed(0)

text = Turtle()
text_class_setup(text)
# Create turtle screen
screen = turtle.Screen()
screen.title("U.S. States Game")
# Insert image from 'blank_states_img.gif'
image_path = "/Gittest/Python study/pythonjourney/section19_directories/project_us_states_game/blank_states_img.gif"
screen.addshape(image_path)
turtle.shape(image_path)
# Import every U.S states from csv file named '50_states.csv'
states_data = pandas.read_csv("/Gittest/Python study/pythonjourney/section19_directories/project_us_states_game/50_states.csv")

def get_mouse_click_coord(x, y):
    print(x, y)
turtle.onscreenclick(get_mouse_click_coord)

total_guess_correct = 0
# States guess game.
while True:
    # Input user guess answer.
    answer_state = screen.textinput(title=f"{total_guess_correct}/50 Guess the State", prompt="What's another state's name?")
    # If user have clicked cancel or exit button, answer_state will be none and ending the game immediately.
    if answer_state == None:
        break
    # Filtering the answer_state compared to states_data
    user_correct_state_guess = states_data[states_data.state == answer_state]

    if not user_correct_state_guess.empty and answer_state not in answerd_state:
        type_new_state(user_correct_state_guess)
        answerd_state.append(answer_state)
        total_guess_correct += 1

turtle.bye()
turtle.mainloop()