from art import logo
import random
import os

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
after_ten_cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
iswanttoplay = True
player_information = {}               # Define player_information as the dictionary that store every player cards     
print("Welcome to blackjack game.")
win = "Congraduation!,you win ^_^"


# Each player calculating function and return the result of total point in current cards
def checking_point(card_list):
    '''
    Calculate the total point of all cards in list that input into this function
    '''
    total_point = 0
    for each_card in card_list:
        total_point += each_card

    return total_point

# Printing the result of game and show user about the point that user and computer have recieved
def final_score():
    '''
    The result of each match
    '''
    print(f"You card is {player_information['player']}, you final score is {player_point}")
    print(f"You rival final hand is {player_information['computer']}, final score is {computer_point}")

# Ace checking is the function that going to check that if player draw a card and they get Ace card if total point is greater than 21 (including Ace card)
# Ace card point that they have draw will changes to 1
def ace_checking(point):
    '''
    Ace point checking function
    '''
    if point < 11:
        new_card = random.choice(cards)
    else:
        new_card = random.choice(after_ten_cards)
    
    return new_card


# Starting game
while iswanttoplay:

    ask_wanted_play = input("Do you want to play blackjack? Type 'y' or 'n': ")             
    os.system("cls")              # Clearing screen in this game   
    
    if ask_wanted_play == 'y':
        print(logo)
        player_information["player"] = random.sample(cards, k=2)        # Player starter cards     
        player_information["computer"] = random.sample(cards, k=2)      # Computer starter cards     
        ismorecard = True

        while ismorecard:
            player_point = checking_point(card_list=player_information["player"])     # Calculating player point       
            if player_point <= 21:
                print(f"You card is {player_information['player']}, you current score is {player_point}")
                print(f"You rival first card is {player_information['computer'][0]}")
                ask_more_card = input("Do you want more card? if you want type 'y' if you don't type 'n': ")
                if ask_more_card == 'y':
                    ismorecard = True
                    player_information["player"].append(ace_checking(point = player_point))
                elif ask_more_card == 'n':
                    ismorecard = False
            else:
                break                   #If your current point is more than 21 then you will lose this match automatically 

        isbotdraw = True

        # Computer gameplay loop
        while isbotdraw:
            computer_point = checking_point(card_list = player_information["computer"])
            # If computer total point is greater than 21 computer will stop drawing new card
            if computer_point >= 21:
                break
            
            isbotdraw = bool(random.randint(0, 1))
            if isbotdraw:
                player_information["computer"].append(ace_checking(point = computer_point))

        final_score()
        if player_point <= 21:
            if computer_point <= 21:
                if computer_point > player_point:
                    print("you lose T_T")
                elif computer_point == player_point:
                    print("You are draw with you rival -_-.")
                else:
                    print("Congraduation!,you win ^_^")
            else:
                print("Congraduation!,you win ^_^")
        else:
            print(f"You went over, you lose T_T")

    elif ask_wanted_play == 'n':
        iswanttoplay = False