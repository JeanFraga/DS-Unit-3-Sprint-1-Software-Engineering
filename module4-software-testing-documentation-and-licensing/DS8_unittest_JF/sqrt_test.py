"""This is our testing file for square root functions"""

import unittest
from sqrt import lazy_sqrt, builtin_sqrt, newton_sqrt

#Our class for square root functions
class SqrtTests(unittest.TestCase):
    """These are our tests for square root funcs"""
    def test_sqrt9(self):
        sqrt_9 = lazy_sqrt(9)
        self.assertEqual(sqrt_9, 3)

    def test_sqrt2(self):
        self.assertAlmostEqual(newton_sqrt(2), 1.414213562)

class OtherTests(unittest.TestCase):
    def test_thing(self):
        pass

if __name__ == '__main__':
    unittest.main()