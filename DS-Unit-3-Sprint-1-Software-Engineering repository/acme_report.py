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
        product = adjective + space + noun
        products.append(product)

    prices = []
    for price in range(num_products):
        price = randint(5, 100)
        prices.append(price)

    weights = []
    for weight in range(num_products):
        weight = randint(5, 100)
        weights.append(weight)

    flammabilities = []
    for flammability in range(num_products):
        flammability = uniform(0.0, 2.5)
        flammabilities.append(flammability)

    return products, prices, weights, flammabilities


def inventory_report():
    """
    takes a list of products, and prints a "nice" summary
    """
    products, prices, weights, flammability = generate_products()

    print("ACME CORPORATION OFFICIAL INVENTORY REPORT")
    print("Unique product names: " + str(len(products)))

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
    mean_flammability = mean_function(flammability)

    print("Average price: " + str(mean_prices))
    print("Average weight: " + str(mean_weights))
    print("Average flammability: " + str(mean_flammability))
