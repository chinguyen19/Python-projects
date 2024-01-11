"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Template for the product assignment.
Name: Nguyen Huu Linh Chi
Student Id: 050358427
"""

class Product:
    """
    This class defines a simplified product for sale in a store.
    """

    def __init__(self, name, price, sale_percentage):
        self.__name = name
        self.__price = price
        self.__sale = sale_percentage

    def set_sale_percentage(self, percentage):
        self.__sale = percentage
        

    def get_price(self):
        if self.__sale != 0.0:
            price = self.__price * ((100 - self.__sale)/100)
            return price
        else:
            return self.__price

    def printout(self):
        """
        When a person's data is needed to be printed on
        screen this method will handle it.  Also good
        for debugging and testing purposes.
        """

        print("—" * 25)
        print("Name:    ", self.__name)
        print("Price:  ", self.__price)
        print("Sale: ", self.__sale)


    # TODO: Define all the methods here.  You can see what they are,
    #       what parameters they take, and what their return value is
    #       by examining the main-function carefully.
    #
    #       You also need to consider which attributes the class needs.
    #
    #       You are allowed to modify the main function, but your
    #       methods have to stay compatible with the original
    #       since the automatic tests assume that.


def main():
    ################################################################
    #                                                              #
    #  You can use the main-function to test your Product class.   #
    #  The automatic tests will not use the main you submitted.    #
    #                                                              #
    #  Voit käyttää main-funktiota Product-luokkasi testaamiseen.  #
    #  Automaattiset testit eivät käytä palauttamaasi mainia.      #
    #                                                              #
    ################################################################

    test_products = {
        "milk":   1.00,
        "sushi": 12.95,
    }

    for product_name in test_products:
        print("=" * 20)
        print(f"TESTING: {product_name}")
        print("=" * 20)

        prod = Product(product_name, test_products[product_name], 0.0)

        prod.printout()
        print(f"Normal price: {prod.get_price():.2f}")

        print("-" * 20)

        prod.set_sale_percentage(10.0)
        prod.printout()
        print(f"Sale price: {prod.get_price():.2f}")

        print("-" * 20)

        prod.set_sale_percentage(25.0)
        prod.printout()
        print(f"Sale price: {prod.get_price():.2f}")

        print("-" * 20)

    
if __name__ == "__main__":
    main()
