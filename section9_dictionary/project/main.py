from art import logo
import os

print(logo)
print("Welcome to secret auction program.")
is_finished = False
bidders = {}
greatest_bid = 0


while not is_finished:
    
    bidder_name = input("What is your name?: ").lower()                     
    individual_bid = int(input("What is you bid?: $"))
    bidders[bidder_name] = individual_bid                                               #Put each bidder and their bid into dictionaries name bidders 
    is_there_any_bidders = input("Are there other bidder? Type 'yes' or 'no'.\n").lower()             #Asking user to continous the auction or not. 
    # ?????????????????
    os.system('cls')
    
    if is_there_any_bidders == "yes":
        is_finished = False
    elif is_there_any_bidders == "no":
        is_ending = input("Are you sure that there are no one wants to join this blind auction else? Type 'yes' or 'no'.\n").lower()
        if is_ending == "yes":
            is_finished = True                                                                      #Clear the screen of program so next bidders will not allowed to see the previous bidders name and their bid.    
    else:
        print("Its seems you type wrong answer.")

    # Comparison of each bidders to find who is the winner of this blind
    if individual_bid > greatest_bid:
        greatest_bid = individual_bid
        highest_bidders = bidder_name


print(f"The winner is {highest_bidders} with a bid of ${greatest_bid}.")
 


