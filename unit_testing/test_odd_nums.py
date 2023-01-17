# Import the testing framework
import unittest

# This is the unit we are running tests on 
def odd_num(num):
    if num % 2 != 0:
        return True
    else:
        return False
    
# The unit test is initialized by creating a class that inherits from unittest.TestCase
class isOddTests(unittest.TestCase):
    # Each method is its own test
    def testOne(self):
        self.assertEqual(odd_num(3), True)
    def testTwo(self):
        self.assertTrue(odd_num(55))
    def testThree(self):
        self.assertEqual(odd_num(66), False)

if __name__ == '__main__':
    # This runs our tests
    unittest.main()
