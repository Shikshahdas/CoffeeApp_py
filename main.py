MENU = {
    "Espresso": {"ingredients": {"water": 50, "coffee": 18}, "cost": 50},
    "Latte": {"ingredients": {"water": 200, "milk": 150, "coffee": 24}, "cost": 100},
    "Cappuccino": {"ingredients": {"water": 250, "milk": 100, "coffee": 24}, "cost": 120},
    "Cold Coffee":{"ingredients":{"water":250, "milk":100, "coffee": 30, "ice cubes":5}, "cost": 150}
}

resources = {"water": 1000, "milk": 700, "coffee": 500}
profit = 0


def is_resource_sufficient(order_ingredients):
    """Checks if resources are enough to make the drink."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"❌ Sorry, not enough {item}.")
            return False
    return True


def process_payment(cost):
    """Simulates payment and checks if enough money is provided."""
    print(f"💰 Please insert money (Cost: ₹{cost})")
    total = int(input("Enter amount: ₹"))
    if total < cost:
        print("❌ Not enough money. Refunded.")
        return False
    elif total > cost:
        change = total - cost
        print(f"✅ Payment successful! Here’s ₹{change} change.")
    else:
        print("✅ Payment successful!")
    return True


def make_coffee(drink_name, order_ingredients):
    """Deduct resources and make coffee."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"☕ Here is your {drink_name}! Enjoy!")


def coffee_machine():
    global profit
    is_on = True
    while is_on:
        choice = input("\nWhat would you like? (espresso/latte/cappuccino/report/exit): ").lower()
        if choice == "exit":
            is_on = False
            print("👋 Turning off the coffee machine. Goodbye!")
        elif choice == "report":
            print(f"Water: {resources['water']}ml")
            print(f"Milk: {resources['milk']}ml")
            print(f"Coffee: {resources['coffee']}g")
            print(f"Profit: ₹{profit}")
        elif choice in MENU:
            drink = MENU[choice]
            if is_resource_sufficient(drink["ingredients"]):
                if process_payment(drink["cost"]):
                    make_coffee(choice, drink["ingredients"])
                    profit += drink["cost"]
        else:

            print("Invalid option, please try again.")



