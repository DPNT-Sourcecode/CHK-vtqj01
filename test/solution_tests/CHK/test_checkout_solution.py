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
        self.assertEqual(checkout_solution.checkout(''), 0)

    def test_WhenInvalidStringAsInput(self):
        self.assertEqual(checkout_solution.checkout('Axz'), -1)

    def test_WhenMultiplesAs(self):
        self.assertEqual(checkout_solution.checkout('AAAAA'), 200)

    def test_WhenMultiplesEs(self):
        self.assertEqual(checkout_solution.checkout('EEB'), 80)

    def test_WhenMultiplesFs(self):
        self.assertEqual(checkout_solution.checkout('FFFFFFF'), 50)

    def test_WhenMultiplesHs(self):
        self.assertEqual(checkout_solution.checkout('HHHHHH'), 50)

if __name__ == '__main__':
    unittest.main()