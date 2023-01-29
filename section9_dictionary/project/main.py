from art import logo
import os

print(logo)
print("Welcome to secret auction program.")
is_finished = False
bidders = {}
greatest_bid = 0

def is_want_to_finished():
    is_there_any_bidders = input("Are there other bidder? Type 'yes' or 'no'.\n").lower()
    while True:
        if is_there_any_bidders == "yes":
            return False
        elif is_there_any_bidders == "no":
            return True  
        else:
            is_there_any_bidders = input("Its seems you type wrong answer, please type 'yes' to continous this auction or type 'no': ").lower()
    



while not is_finished:
    
    bidder_name = input("What is your name?: ").lower()                     
    individual_bid = int(input("What is you bid?: $"))
    bidders[bidder_name] = individual_bid                                                                         
    is_finished = is_want_to_finished()
    
    #Clear the screen of program so next bidders will not allowed to see the previous bidders name and their bid.
    os.system('cls')
    
    # Comparison of each bidders to find who is the winner of this blind
    if individual_bid > greatest_bid:
        greatest_bid = individual_bid
        highest_bidders = bidder_name


print(f"The winner is {highest_bidders} with a bid of ${greatest_bid}.")
 


