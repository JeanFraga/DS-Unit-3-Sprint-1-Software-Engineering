"""
This file is to detail the products serviced by ACME
"""

import random


class Product:
    def __init__(self, name, price=10, weight=20,
                 flammability=0.5, identifier=random.randint(1000000, 9999999)):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = identifier

    def stealability(self):
        """
        calculates the price divided by the weight, and then returns a message:
        if the ratio is less than 0.5 return "Not so stealable...", if it is
        greater or equal to 0.5 but less than 1.0 return "Kinda stealable.",
        and otherwise return "Very stealable!"
        """
        steal_ratio = self.price/self.weight
        if steal_ratio < 0.5:
            return print("Not so stealable...")
        elif 0.5 <= steal_ratio < 1.0:
            return print("Kinda stealable.")
        else:
            return print("Very stealable!")

    def explode(self):
        """
        calculates the flammability times the weight, and then returns a
        message: if the product is less than 10 return "...fizzle.", if it is
        greater or equal to 10 but less than 50 return "...boom!", and
        otherwise return "...BABOOM!!"
        """
        flam_times_weight = self.flammability*self.weight
        if flam_times_weight < 10:
            return print("...fizzle.")
        elif 10 <= flam_times_weight < 50:
            return print("...boom!")
        else:
            return print("...BABOOM!!")


class BoxingGlove(Product):
    def __init__(self, name, price=10, weight=10,
                 flammability=0.5, identifier=random.randint(1000000, 9999999)):
        super().__init__(name, price, weight, flammability, identifier)

    def explode(self):
        """
        prints "...it's a glove." in this subclass
        """
        print("...it's a glove.")

    def punch(self):
        """
        returns "That tickles." if the weight is below 5, "Hey that hurt!" if
        the weight is greater or equal to 5 but less than 15, and "OUCH!"
        otherwise
        """
        glove_weight = self.weight
        if glove_weight < 5:
            return print("That tickles.")
        elif 5 <= glove_weight < 15:
            return print("Hey that hurt!")
        else:
            return print("OUCH!")
