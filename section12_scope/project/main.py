#Number Guessing Game Objectives:

# Include an ASCII art logo. you may get from here http://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random
from logoart import logo

def turn_decrease(current_turns):
    '''
    When player guess is wrong their turns will be decreased
    '''
    
    current_turns -= 1
    return current_turns

def higher_or_lower():
    '''
    Checking player answer and tell player that their answer is lower or higher
    '''
    if player_guess > correct_ans:
        print("Too high.")
    elif player_guess < correct_ans:
        print("Too Low.")

print(logo)
print("Welcome to guess number game.")
diff_level = input("What's the level do you want to play,please type 'easy' or 'hard' : ").lower()
isremainturn = True
correct_ans = random.randint(1, 100)        # Gets the actual answer

# Determine player turn remaining
if diff_level == 'easy':
    player_turns = 10
elif diff_level == 'hard':
    player_turns = 5            
else:
    print("Error! its seems you type wrong direction.")

while isremainturn:
    print(f"You have {player_turns} remaining before game over.")
    player_guess = int(input("Type your guess number: "))

    # The comparison between player guess and actual answer 
    if player_guess == correct_ans:
        isremainturn = False
        print(f"Congraduation!, your guess is correct!,so the answer is {correct_ans}")
    elif player_guess != correct_ans:
        player_turns = turn_decrease(current_turns = player_turns)
        if player_turns > 0:
            isremainturn = True
            higher_or_lower()            
        elif player_turns == 0:
            isremainturn = False
            print("Game over!,You run out of turns.")
