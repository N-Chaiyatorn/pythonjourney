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
    """
    When player guess is wrong their turns will be decreased
    """
    
    current_turns -= 1
    return current_turns

def print_higher_or_lower(guess):
    """
    Checking player answer and tell player that their answer is lower or higher than correct answer.
    """
    if guess > CORRECT_ANS:
        print("Too high.")
    elif guess < CORRECT_ANS:
        print("Too Low.")

def define_player_turn(game_level):
    while True:
        if game_level == 'easy':
            return 10
        elif game_level == 'hard':
            return 5            
        else:
            game_level = input("Error! its seems you type wrong direction, please type the difficult level again: ").lower()


CORRECT_ANS = random.randint(1, 100) 
def guess_number_game():
    print(logo)
    print("Welcome to guess number game.")
    diff_level = input("What's the level do you want to play, please type 'easy' or 'hard' : ").lower()
    is_not_finished = True

       

    # Determine player turn remaining
    player_turns = define_player_turn(game_level = diff_level)

    while is_not_finished:
        print(f"You have {player_turns} remaining before game over.")
        player_guess = int(input("Type your guess number: "))

        # The comparison between player guess and actual answer 
        if player_guess == CORRECT_ANS:
            is_not_finished = False
            print(f"Congraduation!, your guess is correct!,so the answer is {CORRECT_ANS}")
        elif player_guess != CORRECT_ANS:
            player_turns = turn_decrease(current_turns = player_turns)
            if player_turns > 0:
                is_not_finished = True
                print_higher_or_lower(guess = player_guess)            
            elif player_turns == 0:
                is_not_finished = False
                print("Game over!, You run out of turns.")

guess_number_game()
