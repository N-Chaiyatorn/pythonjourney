"""
go here:
http://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json
"""

def turn_right():
    for i in range(0 , 3):
        turn_left()

while not at_goal():
    
    while front_is_clear() and not at_goal():
        move()
        
    if not at_goal():   
        turn_left()
        while wall_on_right():
            move()
        turn_right()
        move()
        
        turn_right()
        while front_is_clear():
            move()
        turn_left()    