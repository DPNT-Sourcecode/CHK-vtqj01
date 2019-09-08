from lib.solutions.CHK import checkout_solution
import unittest


class TestSum(unittest.TestCase):
    def test_WithSingleOrdersForAllItems(self):
        self.assertEqual(checkout_solution.checkout('ABCD'), 115)

    def test_WithSingleOrdersForLimitedItems(self):
        self.assertEqual(checkout_solution.checkout('ABC'), 100)

    def test_WithMultipleOrdersForAllItems(self):
        self.assertEqual(checkout_solution.checkout('ABCDABCD'), 215)

    def test_WithMultipleOrdersForAllItemsWhenAIsWithSpecialOffer(self):
        self.assertEqual(checkout_solution.checkout('ABCDABCDA'), 245)

    def test_WhenEmptyString(self):
        self.assertEqual(checkout_solution.checkout(''), -1)

    def test_WhenInvalidStringAsInput(self):
        self.assertEqual(checkout_solution.checkout('AxB'), -1)

if __name__ == '__main__':
    unittest.main()