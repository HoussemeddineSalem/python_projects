from ingredients import MENU, resources


def ask_for_choice():
    return input('What would you like ? (espresso/latte/cappuccino)')


def resources_checking(choice):
    for order in MENU:
        if choice.lower() == order:
            choice_lowercase = choice.lower()
            resources["water"] -= MENU[choice_lowercase]["ingredients"]["water"]
            if "milk" in MENU[choice_lowercase]["ingredients"]:
                resources["milk"] -= MENU[choice_lowercase]["ingredients"]["milk"]
            resources["coffee"] -= MENU[choice_lowercase]["ingredients"]["coffee"]
            resources["money"] = MENU[choice_lowercase]["cost"]


def paying(choice_price):
    quarters = input('how many quarters')
    dimes = input('how many dimes')
    nickels = input('how many nickels')
    pennies = input('how many pennies')
    payment = float(quarters)*0.25 + float(dimes)*0.1 + float(nickels)*0.05 + float(pennies)*0.01
    if float(choice_price) > payment:
        print("Sorry that's not enough money. Money refunded.")
    elif float(choice_price) < payment:
        print('here is your drink')
        change = round(payment-choice_price,2)
        print(f'here is your change {change}')
    else:
        print('here is your drink')


def coffee_machine():
    off = False
    while not off:
        choice = ask_for_choice()
        if choice.lower() == "off":
            off = True
        elif choice.lower() == "report":
            for key, values in resources.items():
                print(key, ':', values)
        elif choice.lower() in MENU:
            choice_lowercase = choice.lower()
            # print(MENU[choice_lowercase]["ingredients"]["water"])
            # print(resources["water"])
            if MENU[choice_lowercase]["ingredients"]["water"] > resources["water"]:
                print("Sorry, we don't have enough water")
            elif "milk" in MENU[choice_lowercase]["ingredients"] and\
                 MENU[choice_lowercase]["ingredients"]["milk"] > resources["milk"]:
                print("Sorry, we don't have enough milk")
            elif MENU[choice_lowercase]["ingredients"]["coffee"] > resources["coffee"]:
                print("Sorry, we don't have enough coffee")
            else:
                # print(f'Please wait, your {choice} will be ready in a second')
                resources_checking(choice_lowercase)
                # print(resources)
                paying(MENU[choice_lowercase]["cost"])
        else:
            print('Please enter a valid choice')


coffee_machine()


