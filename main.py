from data import MENU, resources
# TODO 1. Prompt the user to choose a drink
request = input("What would you like? (espresso/latte/cappuccino): ").lower()
# TODO 2. Decide what to do next based on the user's input
# TODO 3. Turn off machine to exit
# TODO 4. Print report of current resources
water = resources["water"]
milk = resources["milk"]
coffee = resources["coffee"]
money = 0

if request == 'report':
    print(f"Water: {water}ml")
    print(f"Milk: {milk}ml")
    print(f"Coffee: {coffee}g")
    print(f"Money: ${money}")

# TODO 5. Check if there are enough resources to complete user's request
else:
    drink = MENU[request]
    req_ing = drink["ingredients"]
    if req_ing > resources:
        print("")
# TODO 6. If there are not enough resources, inform the user and start over
# TODO 7. Prompt the user to insert coins
print("Please insert coins.")
quarters = int(input("How many quarters?: "))
dimes = int(input("How many dimes?: "))
nickels = int(input("How many nickels?: "))
pennies = int(input("How many pennies?: "))

# TODO 8. Calculate the total value of the coins inserted
total = round(quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01, 2)
print(total)
# TODO 9. Check if the user inserted enough money for their drink
# TODO 10. If there is not enough money, inform the user and start over
# TODO 11. Add the cost of the drink to the machine's total money
# TODO 12. If the user entered more than needed for the drink, offer change
# TODO 13. Deduct the required resources to make the user's drink from the machine's total resources
# TODO 14. Dispense the user's drink and start over
