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
users_hand_sign = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
hand_sign = [rock, paper, scissors]
hand_sign_character = ["rock" , "paper", "scissors"]
computer_hand_sign = random.randint(0, 2)
print(f"\nYour hand sign is {hand_sign_character[users_hand_sign]}\n{hand_sign[users_hand_sign]}\nvs\n\nYour opponent hand sign is {hand_sign_character[computer_hand_sign]}\n{hand_sign[computer_hand_sign]}")

if not bool(users_hand_sign):
    if not bool(computer_hand_sign):
        print(f"Your hand sign is {hand_sign_character[users_hand_sign]} and your opponent hand sign is also {hand_sign_character[computer_hand_sign]}.")
        print("You are draw with you opponent.")
    else:
        if computer_hand_sign == 1:
            print(f"Your hand sign is {hand_sign_character[users_hand_sign]} and your opponent hand sign is {hand_sign_character[computer_hand_sign]}.")
            print("You lose.")
        else:
            print(f"Your hand sign is {hand_sign_character[users_hand_sign]} and your opponent hand sign is {hand_sign_character[computer_hand_sign]}.")
            print("You win.")
elif users_hand_sign == 1:
    if not bool(computer_hand_sign):
        print(f"Your hand sign is {hand_sign_character[users_hand_sign]} and your opponent hand sign is {hand_sign_character[computer_hand_sign]}.")
        print("You win.")
    else:
        if computer_hand_sign == 1:
            print(f"Your hand sign is {hand_sign_character[users_hand_sign]} and your opponent hand sign is also {hand_sign_character[computer_hand_sign]}.")
            print("You are draw with you opponent.")
        else:
            print(f"Your hand sign is {hand_sign_character[users_hand_sign]} and your opponent hand sign is {hand_sign_character[computer_hand_sign]}.")
            print("You lose.")
else:
    if not bool(computer_hand_sign):
        print(f"Your hand sign is {hand_sign_character[users_hand_sign]} and your opponent hand sign is {hand_sign_character[computer_hand_sign]}.")
        print("You lose.")
    else:
        if computer_hand_sign == 1:
            print(f"Your hand sign is {hand_sign_character[users_hand_sign]} and your opponent hand sign is {hand_sign_character[computer_hand_sign]}.")
            print("You win.")
        else:
            print(f"Your hand sign is {hand_sign_character[users_hand_sign]} and your opponent hand sign is also {hand_sign_character[computer_hand_sign]}.")
            print("You are draw with you opponent.")



