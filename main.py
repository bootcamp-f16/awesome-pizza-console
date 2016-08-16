PIZZAS = (
            {
                "name" : "Cheese Pizza"
            },
            {
                "name" : "Pepperoni Pizza"
            }
        )

def add_to_order():
    """
    Prompts for adding pizza to an order.
    """
    
    while True:
        print("\n\n")
        for index, pizza_options in enumerate(PIZZAS):
            print("{}: {}".format(index + 1, pizza_options["name"]))

        print("0: Exit")
        pizza = input("\nWhich pizza would you like to order? ")

        if pizza == "0":
            break
        elif is_valid_pizza(pizza):
            return PIZZAS[int(pizza) - 1]


def display_order(order):
    if order is not None:
        print(order["name"])
    else:
        print("You have not ordered anything yet.")

def is_valid_pizza(pizza):
    return True if pizza.isdigit() and PIZZAS[int(pizza) - 1] is not None else False


def validate_options(menu_selection):
    if menu_selection.isdigit():
        print("\n{} is an invalid option, please try again".format(menu_selection))
    else:
        print("\n{} is not a number, please enter a number from the menu above".format(menu_selection))


def main():
    """
    Main loop for the ordering application
    """
    MENU_ITEMS = (
        "1: Order Pizza",
        "2: Display Order",
        "0: Exit",
    )

    order = None

    while(True):
        print("\n\n")
        for menu_item in MENU_ITEMS:
            print(menu_item)

        menu_selection = input("\nPlease select an option from above? ")

        if menu_selection == "0":
            break
        elif menu_selection == "1":
            order = add_to_order()
        elif menu_selection == "2":
            display_order(order)
        else:
            validate_options(menu_selection)


main()
