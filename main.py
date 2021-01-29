from data import MENU, resources


def get_report():
    """Print the machine's current resources in a readable format."""
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print("Money: ${:0.2f}".format(money))


def is_enough_resources(required_ing):
    """Return whether there are enough resources to make the user's drink."""
    for item in required_ing:
        if req_ing[item] > resources[item]:
            print(f"Sorry, there is not enough {item}")
            return False
    return True


def get_money():
    """"Prompt the user to insert coins and return the total value."""
    print("Please insert coins.")
    total_amount = int(input("How many quarters?: ")) * 0.25
    total_amount += int(input("How many dimes?: ")) * 0.10
    total_amount += int(input("How many nickels?: ")) * 0.05
    total_amount += int(input("How many pennies?: ")) * 0.01
    return total_amount


def is_enough_money(total_money, total_cost):
    """"Return whether the user has entered enough money."""
    if total_money < total_cost:
        # If there is not enough money, inform the user and start over
        print("Sorry that's not enough money. Money refunded.")
        return False
    # If the user entered more than needed for the drink, offer change
    elif total > cost:
        change = total - cost
        print('Here is ${:0.2f} in change'.format(change))
    return True


money = 0
is_on = True
# Repeat until the machine is turned off
while is_on:
    # Prompt the user to choose a drink
    request = input("What would you like? (espresso/latte/cappuccino): ").lower()
    # Turn off machine to exit
    if request == 'off':
        is_on = False
        print("Powering off...")
    elif request == 'report':
        get_report()
    else:
        drink = MENU[request]
        req_ing = drink["ingredients"]
        # Check if there are enough resources to complete user's request
        if is_enough_resources(req_ing):
            total = get_money()
            cost = drink["cost"]
            # Check if the user inserted enough money for their drink
            if is_enough_money(total, cost):
                # Add the cost of the drink to the machine's total money
                money += cost
                # Deduct the required resources to make the user's drink from the machine's total resources
                for ingredient in req_ing:
                    resources[ingredient] -= req_ing[ingredient]
                # Dispense the user's drink and start over
                print(f"Enjoy your {request}!")
