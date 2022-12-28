"""
go here:
https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%202&url=worlds%2Ftutorial_en%2Fhurdle2.json
"""

def turn_right():
    for i in range(0 , 3):
        turn_left()
def amplitude():
    turn_right()
    move()
def movement():
    move()
    turn_left()
    move()
    amplitude()
    amplitude()
    turn_left()
    
    

while not at_goal():
    movement()
    

        
    
    
  
    