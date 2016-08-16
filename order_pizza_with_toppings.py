
class Cart():
    """Cart is the shopping cart for the current user's order"""
    def __init__(self):
        super(Cart, self).__init__()

class Pizza():
    """Pizza calculates price and manages toppings"""
    def __init__(self):
        super(Pizza, self).__init__()

class Topping():
    """What goes on top of a pizza"""
    def __init__(self):
        super(Topping, self).__init__()

def main():
    """
    Main loop for the ordering application
    """
    MENU_ITEMS = (
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


main()