# TODO: import libraries

from data import MENU, resources


# TODO: Define functions
# (1) report function

def report(water, milk, coffee, money):
    print(f"Water: {water}ml\nMilk:{milk}ml\nCoffee: {coffee}g\nMoney: ${money}\n")


# (2) Check resources function

def check_resources(water, milk, coffee, choice):
    if choice == "espresso":
        required_milk = 0
    else:
        required_milk = MENU[choice]["ingredients"]["milk"]

    required_water = MENU[choice]["ingredients"]["water"]
    required_coffee = MENU[choice]["ingredients"]["coffee"]

    if water < required_water:
        return "False", "water"
    elif milk < required_milk:
        return "False", "milk"
    elif coffee < required_coffee:
        return "False", "coffee"
    else:
        return "True"

# Calculate total money given
def calculate_money(quarter, dimes, nickles, pennies):
    '''Return total money collected from user'''
    total_money = quarter * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01

    return total_money

# Updating resources
def update(water, milk, coffee, money, choice):

    if choice == "espresso":
        required_milk = 0
    else:
        required_milk = MENU[choice]["ingredients"]["milk"]

    required_water = MENU[choice]["ingredients"]["water"]
    required_coffee = MENU[choice]["ingredients"]["coffee"]
    required_money = MENU[choice]["cost"]

    water -= required_water
    milk -= required_milk
    coffee -= required_coffee
    money += required_money

    return(water, milk, coffee, money)

# TODO: Declare variables


running = True


# TODO: Writing main function
def coffee_machine():

    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    money = 0

    while running:

        drink_choice = input("What would you like? (espresso/latte/cappuccino):")

        if drink_choice == "off":
            break

        elif drink_choice == "report":
            report(water, milk, coffee, money)
            continue

        result = check_resources(water, milk, coffee, drink_choice)
        is_sufficient = result[0]
        if is_sufficient == "False":
            is_sufficient = False
        else:
            is_sufficient = True
        missing_ingredient = result[1]

        if is_sufficient:
            print("Please insert coins.\n")
            quarters = int(input("How many quaters?: \n"))
            dimes = int(input("How many dimes?: \n"))
            nickles = int(input("How many nickles?: \n"))
            pennies = int(input("How many pennies?: \n"))

            # Calculate change
            required_money = MENU[drink_choice]["cost"]
            total_money = calculate_money(quarters, dimes, nickles, pennies)
            change = round(total_money - required_money, 2)

            if change < 0:
                print("Sorry that's not enough money. Money refunded\n")
            else:
                print(f"Here is ${change} in change. \n")
                print(f"Here is your {drink_choice} ☕ Enjoy!\n")
                # Update ingredients and money
                outcome = update(water, milk, coffee, money, drink_choice)
                water = outcome[0]
                milk = outcome[1]
                coffee = outcome[2]
                money = outcome[3]

        else:
            print(f"Sorry there is not enough {missing_ingredient} \n")


coffee_machine()
