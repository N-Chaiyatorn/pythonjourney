# https://replit.com/@appbrewery/oop-coffee-machine-final

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

def coffee_machine():
    # First of all, define the significant objects
    coffee_maker = CoffeeMaker()
    menu = Menu()
    money_machine = MoneyMachine()
    while True: 
        # Input user order
        order_name = input(f"Welocome!!! what would you like today? {menu.get_items()}: ")
        # Define Every required information of user order
        ordered_coffee = menu.find_drink(order_name)
        # Check the resource if there are some resource left the program will make a coffee and change the money to user
        if coffee_maker.is_resource_sufficient(drink = ordered_coffee):
            if money_machine.make_payment(cost = ordered_coffee.cost):
                coffee_maker.make_coffee(order = ordered_coffee)

coffee_machine()                 
    

        

    
    
