from art import logo
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]    
iswanttoplay = True
player_information = {}
print(logo)
print("Welcome to blackjack game.")

def checking_point(card_list):
    total_point = 0
    for each_card in card_list:
        total_point+=each_card

    return total_point


while iswanttoplay:
    ask_wanted_play = input("Do you want to play blackjack? Type 'y' or 'no': ")
    if ask_wanted_play == 'y':
        iswanttoplay == True
        
        player_information["player"] = random.sample(cards, k=2)
        player_information["computer"] = random.sample(cards, k=2)
        ismorecard = True
        while ismorecard:
            player_point = checking_point(card_list=player_information["player"])

            print(f"You card is {player_information['player']}, you current score is {player_point}")
            print(f"You rival first card is {player_information['computer'][0]}")
            ask_more_card = input("Do you want more card? if you want type 'y' if you don't type 'n': ")
            if ask_more_card == 'y':
                ismorecard = True
                player_information["player"] = player_information["player"].append(new_card)
                
                                                                    
    elif ask_wanted_play == 'n':
        iswanttoplay == False