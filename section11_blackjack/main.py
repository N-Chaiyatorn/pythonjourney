from art import logo
import random
import os



cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_information = {}               # Define player_information as the dictionary that store every player cards     

# Each player calculating function and return the result of total point in current cards
def cards_point_calculation(card_list):
    """
    Calculate the total point of all cards in list that input into this function
    """
    total_point = 0
    for each_card in card_list:
        total_point += each_card

    return total_point

# Printing the result of game and show user about the point that user and computer have recieved
def final_score_print(player_information, player_point, computer_point):
    """
    The result of each match
    """
    print(f"You card is {player_information['player']}, you final score is {player_point}")
    print(f"You rival final hand is {player_information['computer']}, final score is {computer_point}")

# Ace checking is the function that going to check that if player draw a card and they get Ace card if total point is greater than 21 (including Ace card)
# Ace card point that they have draw will changes to 1
def define_ace_point(point):
    """
    Ace point checking function
    """
    if point < 11:
        return 11
    else:
        return 1

def drawing_new_card(cards):
    new_cards = random.choice(cards)
    return new_cards

def print_result_of_game(player_score, computer_score):
    if player_score > 21:
        print(f"You went over, you lose T_T")
    elif computer_score > 21:
        print("Congraduation!,you win ^_^")
    elif computer_score < player_score:
        print("Congraduation!,you win ^_^")
    elif computer_score > player_score:
        print("you lose T_T")
    else:
        print("You are draw with you rival -_-.")
        
            
    
def black_jack_game(cards_list, everyone_information):
    while True:

        player_ans_input = input("Do you want to play blackjack? Type 'y' or 'n': ")             
        os.system("cls")              # Clearing screen in this game   
    
        if player_ans_input == 'y':
            print(logo)
            player_information["player"] = random.sample(cards, k=2)        # Player starter cards     
            player_information["computer"] = random.sample(cards, k=2)      # Computer starter cards     
        
            while True:
                player_point = cards_point_calculation(card_list = player_information["player"])     # Calculating player point       
                if player_point > 21:
                    break
                print(f"You card is {player_information['player']}, you current score is {player_point}")
                print(f"You rival first card is {player_information['computer'][0]}")
                is_player_draw = input("Do you want more card? if you want type 'y' if you don't type 'n': ")
                if is_player_draw == 'y':
                    new_card = drawing_new_card(cards = cards)
                    if new_card == 11:
                        new_card = define_ace_point(point = player_point)
                    player_information["player"].append(new_card)
                elif is_player_draw == 'n':
                    break
                                 #If your current point is more than 21 then you will lose this match automatically 

        # Computer gameplay loop
            while True:
                computer_point = cards_point_calculation(card_list = player_information["computer"])
            # If computer total point is greater than 21 computer will stop drawing new card
                if computer_point >= 21:
                    break
                
                is_bot_draw = bool(random.randint(0, 1))
                if is_bot_draw:
                    new_card = drawing_new_card(cards)
                    if new_card == 11:
                        new_card = define_ace_point(point = player_point)
                    player_information["computer"].append(new_card)

            final_score_print(player_information, player_point, computer_point)
            print_result_of_game(player_score = player_point, computer_score = computer_point)

        elif player_ans_input == 'n':
            break

        else:
            player_ans_input = input("Its seems you type wrong way, please type 'y' to play blackjack or 'n': ")

print("Welcome to blackjack game.")
black_jack_game(cards_list = cards, everyone_information = player_information)