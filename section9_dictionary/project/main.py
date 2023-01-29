from art import logo
import os

print(logo)
print("Welcome to secret auction program.")
is_there_bidders = True
bidders = {}
greatest_bid = 0


while is_there_bidders:
    
    bidder_name = input("What is your name?: ").lower()                     
    individual_bid = int(input("What is you bid?: $"))
    bidders[bidder_name] = individual_bid                                               #Put each bidder and their bid into dictionaries name bidders 
    isthereanybidders = input("Are there other bidder? Type 'yes' or 'no'.\n").lower()             #Asking user to continous the auction or not. 
    os.system('cls')
    
    if isthereanybidders == "yes":
        istherebidders = True
    elif isthereanybidders == "no":
        istherebidders = False                                                                      #Clear the screen of program so next bidders will not allowed to see the previous bidders name and their bid.    
    else:
        print("Its seems you type wrong answer.")

    # Comparison of each bidders to find who is the winner of this blind
    if individual_bid > greatest_bid:
        greatest_bid = individual_bid


print(f"The winner is {bidders[greatest_bid]} with a bid of ${greatest_bid}.")
 


