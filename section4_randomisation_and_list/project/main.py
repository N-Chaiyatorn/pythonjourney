rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇 
import random 
print("Welcome to Rock Paper Scissors game.")
users_hand_sign = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))                           #Input user hand sign   

if 0 <= users_hand_sign <= 2:
    hand_sign = [rock, paper, scissors]                                                                                             #The image of hand signs
    hand_sign_character = ["rock" , "paper", "scissors"]                                                                            #The string of hand signs in every case
    player_hand_sign = hand_sign_character[users_hand_sign]
    computer_hand_sign = random.randint(0, 2)
    opponent_hand_sign = hand_sign_character[computer_hand_sign]

    draw = "You are draw with you opponent."
    lose = "You lose."
    win = "You win"

    def youaredraw():
        print(f"Your hand sign is {player_hand_sign} and your opponent hand sign is also {opponent_hand_sign}.")
        print(draw)

    def youwin():
        print(f"Your hand sign is {player_hand_sign} and your opponent hand sign is {opponent_hand_sign}.")
        print(win)

    def youlose():
        print(f"Your hand sign is {player_hand_sign} and your opponent hand sign is {opponent_hand_sign}.")
        print(lose)  

    print(f"\nYour hand sign is {player_hand_sign}\n{hand_sign[users_hand_sign]}\nvs\n\nYour opponent hand sign is {opponent_hand_sign}\n{hand_sign[computer_hand_sign]}")
    if player_hand_sign == "rock":
        if opponent_hand_sign == "rock":
            youaredraw()
        elif opponent_hand_sign == "paper":
            youlose()
        elif opponent_hand_sign == "scissors":
            youwin()
    elif player_hand_sign == "paper":
        if opponent_hand_sign == "rock":
            youwin()
        elif opponent_hand_sign == "paper":
            youaredraw()
        elif opponent_hand_sign == "scissors":
            youlose()
    elif player_hand_sign == "scissors":
        if opponent_hand_sign == "rock":
            youlose()
        elif opponent_hand_sign == "paper":
            youwin()
        elif opponent_hand_sign == "scissors":
            youaredraw()
else:
    print("Your input is invalid please run and type again.")









