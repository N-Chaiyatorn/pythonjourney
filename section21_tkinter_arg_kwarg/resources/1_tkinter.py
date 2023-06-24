# from tkinter import *

# window = Tk()
# window.title("first GUI Program")
# window.minsize(width=500, height=300)
# window.config(padx=20, pady=20)

# Label component
# my_label = Label(text="I'm a label", font=("Arial", 24, "bold"))

# pack the component to the window https://docs.python.org/3/library/tkinter.html#the-packer
# pack manual http://tcl.tk/man/tcl8.6/TkCmd/pack.htm
# my_label.pack()

# # Change component property
# my_label["text"] = "New Text"
# my_label.config(text="Jotaro")

# # Button
# def clicked():
#     print("Button get clicked")

# button = Button(text="Click here", command=clicked)
# button.pack()

# # Entry
# input = Entry()
# input_value = input.get()
# input.pack()

#######################################
### more tkinter components/widgets ###
#######################################

#Text
# text = Text(height=5, width=30)
# #Puts cursor in textbox.
# text.focus()
# #Adds some text to begin with.
# text.insert("1.0", "Example of multi-line text entry.\n")
# text.insert("2.0", "Spider-man.\n")
# text.insert("3.0", "Iron-man.")
# #Get's current value in textbox at line 1 to line 3 (not included), character 0
# print(text.get("1.0", "3.0"))
# text.pack()

# #Spinbox
# def spinbox_used():
#     #gets the current value in spinbox.
#     print(spinbox.get())
# spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
# spinbox.pack()

#Scale
#Called with current scale value.
# def scale_used(value):
#     print(value)
# scale = Scale(from_=0, to=100, command=scale_used)
# scale.pack()

#Checkbutton
# def checkbutton_used():
#     #Prints 1 if On button checked, otherwise 0.
#     print(checked_state.get())
# #variable to hold on to checked state, 0 is off, 1 is on.
# checked_state = IntVar()
# checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
# checked_state.get()
# checkbutton.pack()

#Radiobutton
# def radio_used():
#     print(radio_state.get())
# #Variable to hold on to which radio button value is checked.
# radio_state = IntVar()
# radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
# radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
# radiobutton1.pack()
# radiobutton2.pack()

#Listbox
# def listbox_used(event):
#     # Gets current selection from listbox
#     print(listbox.get(listbox.curselection()))

# listbox = Listbox(height=4)
# fruits = ["Apple", "Pear", "Orange", "Banana"]
# for item in fruits:
#     listbox.insert(fruits.index(item), item)
# listbox.bind("<<ListboxSelect>>", listbox_used)
# listbox.pack()

# Quiz
# Synchronous speed of electrical machine calculation
# With Synchronous speed equation is Ns = 120*f/P
# When Ns = Synchronous speed (rpm(round per minute)), f = frequency (Hz), P = The amount of pole in electrical machine

from tkinter import *

class Synchronous_Machine():
    def __init__(self):
        self.pole = 0
        self.frequency = 0
        self.synchronous_speed = 0

    def speed_converting(self):
        synchronous_speed_sec = (self.synchronous_speed * 2 * 3.1414) / 60 
        the_result_of_cal = Label(text = f"Synchronous speed (Ns) is {synchronous_speed_sec} rad/s when pole (P) is {self.pole} and frequency (f) is {self.frequency}", font=("Aerial", 10))
        the_result_of_cal.pack()
        
def synchronous_speed_cal():
    synchronous_machine = Synchronous_Machine()
    synchronous_machine.pole = int(pole_input.get())
    synchronous_machine.frequency = int(frequency_input.get())
    synchronous_machine.synchronous_speed = (120 * synchronous_machine.frequency) / synchronous_machine.pole
    the_result_of_cal = Label(text=f"Synchronous speed (Ns) is {synchronous_machine.synchronous_speed} rpm when pole (P) is {synchronous_machine.pole} and frequency (f) is {synchronous_machine.frequency}", font=("Aerial", 10))
    the_result_of_cal.pack()
    convert_button = Button(text = "convert speed to rad/s", command = synchronous_machine.speed_converting)
    convert_button.pack()

window = Tk()
window.title("Synchronous speed calculation program")
window.minsize(width = 600, height = 400)
window.config(padx = 10, pady = 10)

label = Label(text="Synchronous speed calculation", font=("Aerial", 25))
label.pack()

label = Label(text="type frequency in Hz", font=("Aerial", 10))
label.pack()
frequency_input = Entry()
frequency_input.pack()

label = Label(text="Type the amount of pole", font=("Aerial", 10))
label.pack()
pole_input = Entry()
pole_input.pack()


submit_button = Button(text = "Submit", command = synchronous_speed_cal)
submit_button.pack()

cancel_button = Button(text = "Cancel", command = window.destroy)
cancel_button.pack()

window.mainloop()