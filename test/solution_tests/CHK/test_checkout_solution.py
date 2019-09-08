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
        self.assertEqual(checkout_solution.checkout('HHHHHHHHHHHHHHHH'), 135)

    def test_WhenMultiplesKs(self):
        self.assertEqual(checkout_solution.checkout('KKK'), 190)

    def test_WhenMultiplesPs(self):
        self.assertEqual(checkout_solution.checkout('PPPPPP'), 250)

    def test_WhenMultiplesPs(self):
        self.assertEqual(checkout_solution.checkout('QQQQ'), 110)

    def test_WhenMultiplesVs(self):
        self.assertEqual(checkout_solution.checkout('VVVVVVV'), 310)

    def test_WhenMultiplesNs(self):
        self.assertEqual(checkout_solution.checkout('NNNM'), 120)

    def test_WhenMultiplesRs(self):
        self.assertEqual(checkout_solution.checkout('RRRQ'), 150)

    def test_WhenMultiplesUs(self):
        self.assertEqual(checkout_solution.checkout('UUUU'), 120)

    def test_WhenMultiplesSs(self):
        self.assertEqual(checkout_solution.checkout('SSSZZ'), 120)

if __name__ == '__main__':
    unittest.main()