"""
go here:
https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json"""

def turn_around():
    turn_left()
    turn_left()
    
def turn_right():
    
    turn_around()
    turn_left()
    
while not at_goal():
    
    turn_left()
    if wall_in_front():
        wall_on_left = True
    else:
        wall_on_left = False
    turn_right()
    if wall_in_front():
        if wall_on_right() and wall_on_left:
            turn_around()
            move()
        elif wall_on_right():
            turn_left()
            move()
        elif wall_on_left:
            turn_right()
            move()
        else:
            turn_right()
            move()
    else:
        if wall_on_right() and wall_on_left:
            move()
        elif wall_on_right():
            move()
        elif wall_on_left:
            turn_right()
            move()
        else:
            turn_right()
            move()