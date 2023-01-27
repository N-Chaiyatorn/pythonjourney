# checkout real game here http://www.higherlowergame.com/
# checkout our version here https://replit.com/@appbrewery/higher-lower-final#main.py

import random
from game_data import data
from art import logo, vs
import os

# First of all define function names 'higherlowergame()'
def higherlowergame():
    # Define player_point = 0
    player_point = 0
    # From the start you will print 'logo' ascii art
    isgamecontinous = True
    randomaly_data = random.sample(data, k=len(data))
    sequence = 0
    # In higherlowergame() have loop while so if player answer right question loop while will working continouslly
    while isgamecontinous:
        # random person B
        if sequence == len(data):
            print("All of yor answer is correct, We have nothing to beat you down from now.")
        
        # print logo
        

    
        person_a = randomaly_data[sequence]
        person_b = randomaly_data[sequence + 1]
        
        player_ans = battle_screen(person_a, person_b)
        # Clear screen
        os.system('cls')
        print(logo)
        isgamecontinous = check_ans(player_ans, person_a, person_b)
       
        if isgamecontinous:
            player_point += 1
            sequence += 1
            print(f"You answer is correct, your current point is {player_point}.")
        elif not isgamecontinous:
            print(f"You answer is incorrect, your final point is {player_point}.")
        else:
            print("Person A and B have equal follower_counts.")
        
#Create function names "battle_screen(A, B) so A and B is input dictionaries and this function will print person A and person B information to compare each other" 
def battle_screen(person_a, person_b):
    # print person A information from directories without showing their follower_counts
    print(f"Compare A, {person_a['name']}, {person_a['description']}, from {person_a['country']}.")
    # print 'vs' ascii art
    print(vs)
    print(f"And B, {person_b['name']}, {person_b['description']}, from {person_b['country']}.")
    # Input player answer 
    return input("What do you thing? ,Who have more follower_count, 'A' or 'B' : ")


# Create function names 'check_ans(guess, A, B)' ,in this function will check about player guess if their answer is correct so the function will return True, if the answer is incorrect then the function will return False
def check_ans(guess, person_a, person_b):   
    if guess == 'A':
        if person_a['follower_count'] > person_b['follower_count']:
            return True
        elif person_a['follower_count'] < person_b['follower_count']:
            return False
        else:
            return 
    elif guess == 'B':
        if person_a['follower_count'] > person_b['follower_count']:
            return False
        elif person_a['follower_count'] < person_b['follower_count']:
            return True
        else:
            return 
            
    
# Create function names 'compare(guess)' ,in this function will check about player guess if their answer is correct so you are going to add 1 point to player_point, tell them current point and return their current point 
# then you are going to the beginning of loop again
# If the answer is incorrect then tell them the final score and stop the loop

print(logo)
higherlowergame()

