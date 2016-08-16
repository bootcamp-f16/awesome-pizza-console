def add_to_order():
    """
    Prompts for adding pizza to an order.
    """

    ORDER_OPTIONS = (
        "1: Cheese Pizza",
        "2: Pepperoni Pizza",
        "0: Back to Main Menu",
    )
    
    while True:
        print("\n\n")
        for order_option in ORDER_OPTIONS:
            print(order_option)

        order_selection = input("\nWhich pizza would you like to order? ")

        if order_selection == "0":
            break
        elif order_selection == "1":
            return "Cheese Pizza"
            break
        elif order_selection == "2":
            return "Pepperoni Pizza"
            break

def display_order(order):
    if order is not None:
        print(order)
    else:
        print("You have not ordered anything yet.")

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


main()