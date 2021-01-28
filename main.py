from data import MENU, resources
money = 0


def get_report():
    # TODO 4. Print report of current resources
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    print(f"Water: {water}ml")
    print(f"Milk: {milk}ml")
    print(f"Coffee: {coffee}g")
    print(f"Money: ${money}")


def check_resources(req_ing):
    for ingredient in req_ing:
        if req_ing[ingredient] > resources[ingredient]:
            print(f"Sorry, there is not enough {ingredient}")
            coffee_machine()


def get_money():
    # TODO 7. Prompt the user to insert coins
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))

    # TODO 8. Calculate the total value of the coins inserted
    return quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01


def check_money(total, cost, profit):
    if total < cost:
        # TODO 10. If there is not enough money, inform the user and start over
        print("Sorry that's not enough money. Money refunded.")
        coffee_machine()

    # TODO 12. If the user entered more than needed for the drink, offer change
    if total > cost:
        change = total - cost
        print('Here is ${:0.2f} in change'.format(change))

    # TODO 11. Add the cost of the drink to the machine's total money
    return profit + cost


def coffee_machine():
    global money
    # TODO 1. Prompt the user to choose a drink
    request = ""
    valid_requests = ['espresso', 'latte', 'cappuccino', 'report', 'off']
    while request not in valid_requests:
        request = input("What would you like? (espresso/latte/cappuccino): ").lower()
    # TODO 2. Decide what to do next based on the user's input
    # TODO 3. Turn off machine to exit
    if request == 'off':
        print("Powering off...")
        return
    elif request == 'report':
        get_report()
        coffee_machine()
    else:
        # TODO 5. Check if there are enough resources to complete user's request
        drink = MENU[request]
        req_ing = drink["ingredients"]
        # TODO 6. If there are not enough resources, inform the user and start over
        check_resources(req_ing)

        # TODO 9. Check if the user inserted enough money for their drink
        total = get_money()
        cost = drink["cost"]
        money = check_money(total, cost, money)

        # TODO 13. Deduct the required resources to make the user's drink from the machine's total resources
        for ingredient in req_ing:
            resources[ingredient] -= req_ing[ingredient]

        # TODO 14. Dispense the user's drink and start over
        print(f"Enjoy your {request}!")
        coffee_machine()


coffee_machine()
