import unittest

# import the Fraction type from the fractions module in the standard library
from fractions import Fraction

# Imports sum() from the my_sum package
from my_sum import sum

# Defines a new test case class which inherits unittest.TestCase
class TestSum(unittest.TestCase):

    # Define test method to test that it can sum a list of integers
    def test_list_int(self):
        # Declare variable data with list of numbers 1,2,3
        data = [1,2,3]
        # Assign the result of my_sum.sum(data) to a result variable
        result = sum(data)
        # Assert that the value of result == 6 with the assertEqual method of the unittest.TestCase class
        self.assertEqual(result, 6, "Should be 6")

    # Test that it can sum a list of fractions
    def test_list_fraction(self):
        data = [Fraction(1,4), Fraction(1,4), Fraction(2,5)]
        result = sum(data)
        self.assertEqual(result, 1)


if __name__ == "__main__":
    unittest.main()


