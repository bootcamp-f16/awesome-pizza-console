class Topping():
    """What goes on top of a pizza"""
    def __init__(self, name):
        super(Topping, self).__init__()
        self.name = name

    def __str__(self):
        return self.name

class Pizza():
    """Pizza calculates price and manages toppings"""

    MENU_ITEMS = (
        "1: Add Toppings",
        "2: Display Toppings",
        "3: Remove Toppings",
        "4: Add Pizza to Cart",
        "0: Cancel",
    )

    AVAILABLE_TOPPINGS = (
        Topping(name="Cheese"),
        Topping(name="Pepperoni"),
        Topping(name="Sausage"),
    )

    toppings = []

    def __init__(self):
        super(Pizza, self).__init__()

    def is_valid_topping(self, selection):
        return (selection.isdigit() and
            (int(selection) - 1) >= 0 and
            (int(selection) - 1) < len(self.AVAILABLE_TOPPINGS))

    def display_menu(self):
        while True:
            print("\n\n")
            for menu_item in self.MENU_ITEMS:
                print(menu_item)

            menu_selection = input("\nPlease select an option from above? ")

            if menu_selection == "0":
                break
            elif menu_selection == "1":
                self.add_toppings()
            elif menu_selection == "2":
                self.display_toppings()

    def add_toppings(self):
        while(True):
            print("\n\n")
            for index, topping in enumerate(self.AVAILABLE_TOPPINGS):
                print("{}: {}".format(index + 1, topping))
            print("0: Exit")

            menu_selection = input("\nPlease select a topping from above? ")

            if menu_selection == "0":
                break
            elif self.is_valid_topping(menu_selection):
                topping = self.AVAILABLE_TOPPINGS[int(menu_selection) - 1]
                self.toppings.append(topping)
                print("\n{} added to the pizza!".format(topping))
            else:
                print("\n{} is an invalid option, please try again".format(menu_selection))

class Cart():
    """Cart is the shopping cart for the current user's order"""


    MENU_ITEMS = (
        "1: Add Pizza",
        "2: Remove Pizza",
        "0: Exit",
    )

    current_pizza = Pizza()
    pizzas = []

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
            if menu_selection == "1":
                self.current_pizza.display_menu()
                self.pizzas.append(self.current_pizza)

def main():
    """
    Main loop for the ordering application
    """


    cart = Cart()

    while(True):
        cart.display_menu()


main()