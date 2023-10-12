MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}


profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

change = 0

def checking(drink_wants):
    if drink_wants == "espresso" :
        if resources["water"] >= MENU["espresso"]["ingredients"]["water"] and resources["coffee"] >= MENU["espresso"]["ingredients"]["coffee"]:
            quarters, dimes, nickles, pennies = money_checking()
            user_total_money = float(format((quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01),".2f"))
            if user_total_money >= MENU["espresso"]["cost"]:
                global  change
                change = user_total_money - MENU["espresso"]["cost"]
                if change > 0 :
                    print(f"Here is your change : ${change}")
                resources["water"] -= MENU["espresso"]["ingredients"]["water"]
                resources["coffee"] -= MENU["espresso"]["ingredients"]["coffee"]
                print("Here is your espresso")
                global profit
                profit += MENU["espresso"]["cost"]
                # print(profit)
            else:
                print("You dont have enough money for latte! Choose Something else please.")
                return "no money"
        else:
            return False


    elif drink_wants == "latte" :
        if resources["water"] >= MENU["latte"]["ingredients"]["water"] and resources["coffee"] >= MENU["latte"]["ingredients"]["coffee"]  and resources["milk"] >= MENU["latte"]["ingredients"]["milk"]:
            quarters, dimes, nickles, pennies = money_checking()
            user_total_money = float(format((quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01),".2f"))
            if user_total_money >= MENU["latte"]["cost"]:

                change = user_total_money - MENU["latte"]["cost"]
                if change > 0:
                    print(f"Here is your change : ${change}")
                resources["water"] -= MENU["latte"]["ingredients"]["water"]
                resources["coffee"] -= MENU["latte"]["ingredients"]["coffee"]
                resources["milk"] -= MENU["latte"]["ingredients"]["milk"]
                print("Here is your latte")

                profit += MENU["latte"]["cost"]
                # print(profit)

            else:
                print("You dont have enough money for latte! Choose Something else please.")

        else:
            return False


    if drink_wants == "cappuccino" :
        if resources["water"] >= MENU["cappuccino"]["ingredients"]["water"] and resources["coffee"] >= MENU["cappuccino"]["ingredients"]["coffee"]  and resources["milk"] >= MENU["cappuccino"]["ingredients"]["milk"]:
            quarters, dimes, nickles, pennies = money_checking()
            user_total_money = float(format((quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01),".2f"))
            if user_total_money >= MENU["cappuccino"]["cost"]:
                change = user_total_money - MENU["cappuccino"]["cost"]
                if change > 0:
                    print(f"Here is your change : ${change}")
                resources["water"] -= MENU["espresso"]["ingredients"]["water"]
                resources["coffee"] -= MENU["cappuccino"]["ingredients"]["coffee"]
                resources["milk"] -= MENU["cappuccino"]["ingredients"]["milk"]
                print("Here is your espresso")

                profit += MENU["cappuccino"]["cost"]
                # print(profit)

            else:
                print("You dont have enough money for cappuccino! Choose Something else please.")

        else:
            return False
def money_checking():
    print("Please insert coins :")
    quarters = int(input("How many quarters? :"))
    dimes = int(input("How many dimes? :"))
    nickles = int(input("How many nickles? :"))
    pennies = int(input("How many pennies? :"))
    return quarters , dimes , nickles , pennies



# money = 0
repeat = True
while repeat :
    user_input = input("What would you like espresso/latte/cappuccino: ").lower()
    if user_input == "report":
        print(f'water : {resources["water"]}ml')
        print(f'milk : {resources["milk"]}ml')
        print(f'coffee : {resources["coffee"]}g')
        print(f'profit : ${profit}')
    elif user_input == "espresso":
        availability = checking(user_input)
        if availability == False:
            print("Sorry ! There is no enough ingredients Choose some other drink.")


    elif user_input == "latte":
        availability = checking(user_input)
        if availability == False:
            print("Sorry ! There is no enough ingredients Choose some other drink.")

    elif user_input == "cappuccino":
        availability = checking(user_input)
        if availability == False:
            print("Sorry ! There is no enough ingredients Choose some other drink.")
    else:
        print("Please enter Correct input!")