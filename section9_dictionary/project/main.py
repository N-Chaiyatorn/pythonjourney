from art import logo
import os

istherebidders = "yes"
bidders = {}
greatest_bid = 0


while istherebidders == "yes":
    print(logo) 
    print("Welcome to secret auction program.")
    bidder_name = input("What is your name?: ").lower()                     
    individual_bid = int(input("What is you bid?: $"))
    bidders[individual_bid] = bidder_name                                               #Put each bidder and their bid into dictionaries name bidders 
    istherebidders = input("Are there other bidder? Type 'yes' or 'no'.\n").lower()             #Asking user to continous the auction or not. 
    os.system('cls')                                                                    #Clear the screen of program so next bidders will not allowed to see the previous bidders name and their bid.    

    # Comparison of each bidders to find who is the winner of this blind
    if individual_bid>greatest_bid:
        greatest_bid = individual_bid

print(logo)
print(f"The winner is {bidders[greatest_bid]} with a bid of ${greatest_bid}.")
 


