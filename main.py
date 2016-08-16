order = None

def add_to_order():
    """
    Prompts for adding pizza to an order.
    """
    
    ORDER_OPTIONS = (
        "1: Cheese pizza",
        "2: Pepperoni pizza",
        "0: Back to main menu",
    )
    
    while True:
        for order_option in ORDER_OPTIONS:
            print(order_option)

        order_selection = input("Which pizza would you like to order? ")

        if order_selection == "0":
            break



def main():
    """
    Main loop for the ordering application
    """
    MENU_ITEMS = (
        "1: Order Pizza",
        "0: Exit",
    )

    while(True):
        for menu_item in MENU_ITEMS:
            print(menu_item)

        menu_selection = input("Please select an option from above? ")

        if menu_selection == "0":
            break
        elif menu_selection == "1":
            add_to_order()


main()