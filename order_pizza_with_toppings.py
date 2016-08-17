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

    @classmethod
    def make_pizza(cls):
        pizza = cls()
        while True:
            print("\n\n")
            for menu_item in pizza.MENU_ITEMS:
                print(menu_item)

            menu_selection = input("\nPlease select an option from above? ")

            if menu_selection == "0":
                return None
            elif menu_selection == "1":
                pizza.add_toppings()
            elif menu_selection == "2":
                pizza.display_toppings()
            elif menu_selection == "3":
                pizza.remove_toppings()
            elif menu_selection == "4":
                return pizza

    def __init__(self):
        super(Pizza, self).__init__()
        self.toppings = []

    def is_valid_topping(self, selection, toppings=AVAILABLE_TOPPINGS):
        return (selection.isdigit() and
            (int(selection) - 1) >= 0 and
            (int(selection) - 1) < len(toppings))


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

    def display_toppings(self, heading="Toppings", topping_format="{index}: {topping}"):
        if len(self.toppings) == 0:
            print("There are no toppings on the pizza yet")
        else:
            if heading is not None:
                print(heading)
            for index, topping in enumerate(self.toppings):
                print(topping_format.format(index=index+1, topping=topping))

    def remove_toppings(self):
        while True:
            self.display_toppings()
            print("0: Exit")

            menu_selection = input("\nPlease select a topping to remove? ")

            if menu_selection == "0":
                break
            elif self.is_valid_topping(menu_selection, self.toppings):
                topping = self.toppings[int(menu_selection) -1]
                self.toppings.remove(topping)
                print("\n{} removed from the pizza!".format(topping))
            else:
                print("\n{} is an invalid option, please try again".format(menu_selection))


class Cart():
    """Cart is the shopping cart for the current user's order"""


    MENU_ITEMS = (
        "1: Add Pizza",
        "2: Display Pizzas",
        "3: Remove Pizza",
        "4: Place order",
        "0: Exit",
    )

    def __init__(self):
        super(Cart, self).__init__()
        self.pizzas = []

    def display_menu(self):
        while(True):
            print("\n\n")
            for menu_item in self.MENU_ITEMS:
                print(menu_item)

            menu_selection = input("\nPlease select an option from above? ")

            if menu_selection == "0":
                break
            if menu_selection == "1":
                pizza = Pizza.make_pizza()
                if pizza is not None:
                    self.pizzas.append(pizza)
                    print("\nPizza added to cart!")
            if menu_selection == "2":
                self.display_pizzas()

    def display_pizzas(self):
        print("\n\n")
        if len(self.pizzas) == 0:
            print("There are no pizzas yet")
        else:
            print("Pizzas")
            for index, pizza in enumerate(self.pizzas):
                print("{index}: Pizza {index}".format(index=index+1))
                pizza.display_toppings(heading=None, topping_format="     {topping}")

def main():
    """
    Main loop for the ordering application
    """


    cart = Cart()
    cart.display_menu()


main()