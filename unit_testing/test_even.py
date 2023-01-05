# Import the testing framework
import unittest

# This is the unit we are running the tests on
def isEven(num):
    if num % 2 == 0:
        return True
    else:
        return False

# The unit test is initialized by creating a class that inherits from unittest.TestCase
class isEvenTests(unittest.TestCase):
    # Each method in this class is a test to be run
    def testOne(self):
        self.assertEqual(isEven(2), True)
        # Another way to write this
        self.assertTrue(isEven(2))
    def testTwo(self):
        self.assertEqual(isEven(3), False)
        # Another way to write this
        self.assertFalse(isEven(3))
    # any task you want to run before the methods above, you put in the setUp method
    def setUp(self):
        # Add the setUp tasks
        print("Running setUp")
    # any task you want to run after the tests are executed, put in the tearDown method
    def tearDown(self):
        # Add tearDown tasks
        print("Running tearDown tasks")

if __name__ == '__main__':
    # This runs our tests
    unittest.main()

