
class Pizza():
    """Pizza calculates price and manages toppings"""
    def __init__(self):
        super(Pizza, self).__init__()

class Topping():
    """What goes on top of a pizza"""
    def __init__(self):
        super(Topping, self).__init__()

class Cart():
    """Cart is the shopping cart for the current user's order"""
    MENU_ITEMS = (
        "1: Add Toppings",
        "2: Remove Toppings",
        "3: Add Pizza to Cart",
        "0: Cancel",
    )

    current_pizza = Pizza()

    def __init__(self):
        super(Cart, self).__init__()

    def display_menu(self):
        while(True):
            print("\n\n")
            for menu_item in self.MENU_ITEMS:
                print(menu_item)

            menu_selection = input("\nPlease select an option from above? ")

            if menu_selection == "0":
                break

def main():
    """
    Main loop for the ordering application
    """
    MENU_ITEMS = (
        "1: Add Pizza",
        "2: Remove Pizza",
        "0: Exit",
    )

    cart = Cart()

    while(True):
        print("\n\n")
        for menu_item in MENU_ITEMS:
            print(menu_item)

        menu_selection = input("\nPlease select an option from above? ")

        if menu_selection == "0":
            break
        if menu_selection == "1":
            cart.display_menu()


main()