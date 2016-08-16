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
            return None
        elif is_valid_pizza(pizza, PIZZAS):
            return PIZZAS[int(pizza) - 1]

def remove_from_order(order):
    for index, pizza in enumerate(order):
        print("{}: {}".format(index + 1, pizza["name"]))
    print("0: Exit")

    remove_choice = input("\nWhich pizza would you like to remove? ")
    if remove_choice == "0":
        return
    elif is_valid_pizza(remove_choice, order):
        del order[int(remove_choice)-1]


def display_order(order):
    if len(order) == 0:
        print("You have not ordered anything yet.")
    else: 
        for item in order:
            print(item["name"])

def is_valid_pizza(pizza, pizza_list):
    return True if pizza.isdigit() and pizza_list[int(pizza) - 1] is not None else False


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
        "1: Add Pizza to Order",
        "2: Remove Pizza from Order",
        "3: Display Order",
        "0: Exit",
    )

    order = []

    while(True):
        print("\n\n")
        for menu_item in MENU_ITEMS:
            print(menu_item)

        menu_selection = input("\nPlease select an option from above? ")

        if menu_selection == "0":
            break
        elif menu_selection == "1":
            order_selection = add_to_order()
            if order_selection is not None:
                order.append(order_selection)

        elif menu_selection == "2":
            remove_from_order(order)
        elif menu_selection == "3":
            display_order(order)
        else:
            validate_options(menu_selection)


main()
