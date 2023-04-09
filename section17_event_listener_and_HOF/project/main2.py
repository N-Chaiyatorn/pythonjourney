from turtle import Turtle, Screen
import random
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class result_window():
    def checking_winner(self, user_ans, actual_winner):
        if actual_winner == user_ans:
            messagebox.showinfo(title = "result", message = f"Congraduation!!!, so your guess is {user_ans} and actual winner is {actual_winner}.")
        else:
            messagebox.showinfo(title = "result", message = f"You lose!!!, so your guess is {user_ans} and actual winner is {actual_winner}.")
    
def turn_off_program():
    question_window.destroy()
    define_every_turtle()
    screen.exitonclick()

def is_racing_still_go_on(turtle_dict):
    for color in turtle_dict:
        if turtle_dict[color].xcor() >= 250:
            return False
    return True

def checking_winner(turtle_dict):
    turtle_winner_pos = 0
    for color in turtle_dict:
        if turtle_dict[color].xcor() > turtle_winner_pos:
            turtle_winner_pos = turtle_dict[color].xcor()
            winner_color = color
    return winner_color

def define_every_turtle():
    turtle_number = 0
    for turtle in turtles_color:
        turtles_information[turtle] = {}
        turtles_information[turtle] = Turtle()
        turtles_information[turtle].shape("turtle")
        turtles_information[turtle].color(turtle)
        turtles_information[turtle].penup()
        turtles_information[turtle].setpos(-250, Y_POSITION[turtle_number])
        turtle_number += 1

def turtle_racing():
    user_ans = user_guess.get().lower()
    question_window.destroy()
    define_every_turtle()
    
    if user_ans != "":
        is_racing_not_end = True
        while is_racing_not_end:
            for turtle in turtles_color:
                turtles_information[turtle].speed(random.randint(0, 10))
                turtles_information[turtle].forward(random.randint(10, 20))
            is_racing_not_end = is_racing_still_go_on(turtle_dict = turtles_information)

        actual_winner = checking_winner(turtle_dict = turtles_information)
        result_screen = result_window()
        result_screen.checking_winner(user_ans, actual_winner)
    
    screen.exitonclick()

turtles_information = {}
screen = Screen()
Y_POSITION = [90, 60, 30, 0, -30, -60, -90]
turtles_color = ["purple","blue" ,"green" ,"yellow" ,"orange" ,"red"]

question_window = Tk()
question_window.geometry("300x70")

frame = ttk.Frame(master = question_window)
frame.grid(column = 0, row = 2)

question_window.title("Make your bet!!")
label = ttk.Label(master = question_window, text = "Which turtle is the winner in this race? Please answer:").grid(column = 0, row = 0)

user_guess = ttk.Entry(master = question_window, width = 45)
user_guess.grid(column = 0, row = 1)

okay_button = ttk.Button(master = frame, text = "Ok", command = turtle_racing).grid(column = 0, row = 0)
cancel_button = ttk.Button(master = frame, text = "Cancel", command = turn_off_program).grid(column = 1, row = 0)
question_window.protocol("WM_DELETE_WINDOW", turn_off_program)

question_window.mainloop()