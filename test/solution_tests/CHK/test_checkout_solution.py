from lib.solutions.CHK import checkout_solution
import unittest


class TestSum(unittest.TestCase):
    def test_WithSingleOrdersForAllItems(self):
        self.assertEqual(checkout_solution.checkout('ABCD'), 115)

if __name__ == '__main__':
    unittest.main()