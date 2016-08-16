class Topping():
    """What goes on top of a pizza"""
    def __init__(self, name):
        super(Topping, self).__init__()
        self.name = name

    def __str__(self):
        return self.name

class Pizza():
    """Pizza calculates price and manages toppings"""
    AVAILABLE_TOPPINGS = (
        Topping(name="Cheese"),
        Topping(name="Pepperoni"),
        Topping(name="Sausage"),
    )

    def __init__(self):
        super(Pizza, self).__init__()

    def add_topping(self):
        while(True):
            print("\n\n")
            for index, topping in enumerate(self.AVAILABLE_TOPPINGS):
                print("{}: {}".format(index + 1, topping))
            print("0: Exit")

            menu_selection = input("\nPlease select a topping from above? ")

            if menu_selection == "0":
                break


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
            elif menu_selection == "1":
                self.current_pizza.add_topping()

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