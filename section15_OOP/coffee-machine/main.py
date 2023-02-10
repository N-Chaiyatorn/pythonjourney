# https://replit.com/@appbrewery/oop-coffee-machine-final

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

def coffee_machine():
    # First of all, define the significant objects
    coffeemaker = CoffeeMaker()
    menu = Menu()
    moneymachine = MoneyMachine()
    while True: 
        # Input user order
        order_name = input(f"Welocome!!! what would you like today? {menu.get_items()}: ")
        # Define Every required information of user order
        orderinformation = menu.find_drink(order_name)
        # Check the resource if there are some resource left the program will make a coffee and change the money to user
        can_make = coffeemaker.is_resource_sufficient(drink = orderinformation)
        if can_make:
            is_there_enough_money = moneymachine.make_payment(cost = orderinformation.cost)
            if is_there_enough_money:
                # 
                coffeemaker.make_coffee(order = orderinformation)

coffee_machine()                 
    

        

    
    
