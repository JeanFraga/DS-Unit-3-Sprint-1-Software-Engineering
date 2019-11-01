"""
Prints a summary of the products
"""

from random import randint, sample, uniform
from acme import Product

ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products(num_products=30):
    """
    generate a given number of products (default 30), randomly, and return them
    as a list
    """
    products = []
    for product in range(num_products):
        adjective = sample(ADJECTIVES, 1)[0]
        noun = sample(NOUNS, 1)[0]
        space = " "
        product_name = adjective + space + noun
        price = randint(5, 100)
        weight = randint(5, 100)
        flammability = uniform(0.0, 2.5)
        product = Product(product_name, price, weight, flammability)
        products.append(product)

    return products


def inventory_report():
    """
    takes a list of products, and prints a "nice" summary
    """
    products = generate_products()

    print("ACME CORPORATION OFFICIAL INVENTORY REPORT")
    print("Unique product names: " + str(len(products)))

    prices = []
    weights = []
    flammabilities = []

    for product in range(len(products)):
        prices.append(products[product].price)
        weights.append(products[product].weight)
        flammabilities.append(products[product].flammability)

    def mean_function(category):
        """
        a simple mean function to calculate for each category.
        """
        for i in category:
            sum_i = 0 + i
        category_mean = sum_i/len(category)
        return category_mean

    mean_prices = mean_function(prices)
    mean_weights = mean_function(weights)
    mean_flammability = mean_function(flammabilities)

    print("Average price: " + str(mean_prices))
    print("Average weight: " + str(mean_weights))
    print("Average flammability: " + str(mean_flammability))
