"""
Testing for "acme.py" and "acme_report.py" using unittest
"""

import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.weight, 10)

    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.name, "Test Product")

class AcmeProductTests(unittest.TestCase):
    """Making sure acme_report is superb!"""
    def test_default_num_products(self):
        """Test default product number being 30"""
        gen_prod = generate_products()
        self.assertEqual(len(gen_prod[0]), 30)

    def test_legal_names(self):
        """Test possible combinations"""
        ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
        NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']
        gen_prod = generate_products()[0]
        self.assertIn(generate_products()[0], [str(ADJECTIVES) + ' ' + str(NOUNS)])

if __name__ == '__main__':
    unittest.main()
