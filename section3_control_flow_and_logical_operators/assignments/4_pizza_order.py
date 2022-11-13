"""
Congratulations, you've got a job at Python Pizza. Your first job is to build an automatic pizza order program.

Based on a user's order, work out their final bill.

Small Pizza: $15

Medium Pizza: $20

Large Pizza: $25

Pepperoni for Small Pizza: +$2

Pepperoni for Medium or Large Pizza: +$3

Extra cheese for any size pizza: + $1

### Example Input
```
size = "L"
add_pepperoni = "Y"
extra_cheese = "N"
```
### Example Output
```
Your final bill is: $28.
```
"""

pizza_size_user = input("size = ")                         #Pizza size requirement      
pepperoni_add_user = input("add_pepperoni = ")             #The additional of pepperoni
extra_cheese_user = input("extra_cheese = ")               #The additional of cheese
if pizza_size_user == '"S"': 
    ispizzasmall = True
    ispizzamedium = False
    ispizzalarge = False
elif pizza_size_user == '"M"': 
    ispizzasmall = False
    ispizzamedium = True
    ispizzalarge = False
elif pizza_size_user == '"L"': 
    ispizzasmall = False
    ispizzamedium = False
    ispizzalarge = True
else:
    ispizzasmall = False
    ispizzamedium = False
    ispizzalarge = False
if pepperoni_add_user == '"Y"':
    ispepperoniaddy = True
    ispepperoniaddn = False
elif pepperoni_add_user == '"N"':
    ispepperoniaddy = False
    ispepperoniaddn = True
else:
    ispepperoniaddy = False
    ispepperoniaddn = False
if extra_cheese_user == '"Y"':
    ischeeseaddy = True
    ischeeseaddn = True
elif extra_cheese_user == '"N"':
    ischeeseaddy = False
    ischeeseaddn = True
else:
    ischeeseaddy = False
    ischeeseaddn = False

            
if ispizzasmall:
    pizza_price = 15
    if ispepperoniaddy:
        pizza_price += 2
        if ischeeseaddy:
            pizza_price += 1
            print(f"Your final bill is: ${pizza_price}.")           #The price of pizza that you have to pay if you has ordered pizza size small and add some pepporoni and cheese
        elif ischeeseaddn:
            print(f"Your final bill is: ${pizza_price}.")           #The price of pizza that you have to pay if you has ordered pizza size small and add some pepporoni but didn't add any cheese
        else:
            print("Error!! please check your input again.")
            
    elif ispepperoniaddn:
        if ischeeseaddy:
            pizza_price += 1
            print(f"Your final bill is: ${pizza_price}.")               #The price of pizza that you have to pay if you has ordered pizza size small and add some cheese but didn't add any pepporoni 
        elif ischeeseaddn:
            print(f"Your final bill is: ${pizza_price}.")               #The price of pizza that you have to pay if you has ordered pizza size small and didn't add any cheese and pepporoni 
        else:
            print("Error!! please check your input again.")
    else:
        print("Error!! please check your input again.")
      
        
elif ispizzamedium:
    pizza_price = 20
    if ispepperoniaddy:
        pizza_price += 3
        if ischeeseaddy:
            pizza_price += 1
            print(f"Your final bill is: ${pizza_price}.")                              #The price of pizza that you have to pay if you has ordered pizza size medium and add some pepporoni and cheese
        elif ischeeseaddn:
            print(f"Your final bill is: ${pizza_price}.")                              #The price of pizza that you have to pay if you has ordered pizza size medium and add some pepporoni but didn't add any cheese
        else:
            print("Error!! please check your input again.")
            
    elif ispepperoniaddn:
        if ischeeseaddy:
            pizza_price += 1
            print(f"Your final bill is: ${pizza_price}.")                               #The price of pizza that you have to pay if you has ordered pizza size medium and add some cheese but didn't add any pepporoni 
        elif ischeeseaddn:
            print(f"Your final bill is: ${pizza_price}.")                               #The price of pizza that you have to pay if you has ordered pizza size medium and didn't add any cheese and pepporoni
        else:
            print("Error!! please check your input again.")
    else:
        print("Error!! please check your input again.")
        

elif ispizzalarge:
    pizza_price = 25
    if ispepperoniaddy:
        pizza_price += 3
        if ischeeseaddy:
            pizza_price += 1
            print(f"Your final bill is: ${pizza_price}.")            #The price of pizza that you have to pay if you has ordered pizza size large and add some pepporoni and cheese 
        elif ischeeseaddn:
            print(f"Your final bill is: ${pizza_price}.")           #The price of pizza that you have to pay if you has ordered pizza size large and add some pepporoni but didn't add any cheese
        else:
            print("Error!! please check your input again.")
            
    elif ispepperoniaddn:
        if ischeeseaddy:
            pizza_price += 1
            print(f"Your final bill is: ${pizza_price}.")           #The price of pizza that you have to pay if you has ordered pizza size large and add some cheese but didn't add any pepporoni 
        elif ischeeseaddn:
            print(f"Your final bill is: ${pizza_price}.")        #The price of pizza that you have to pay if you has ordered pizza size large and didn't add any cheese and pepporoni
        else:
            print("Error!! please check your input again.")
    else:
        print("Error!! please check your input again.")
            
else:
    print("Error!! please check your input again.")
        

    

