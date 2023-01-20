import unittest

def division(x,y):
    return x / y

# The unit test is initialized by creating a class that inherits from unittest.TestCase
class divisionTests(unittest.TestCase):
    def testOne(self):
        self.assertEqual(division(4,2), 2)
    def testTwo(self):
        self.assertEqual(division(100,25), 4)
    def testThree(self):
        self.assertNotEqual(division(6,3), 3)
    def testFour(self):
        self.assertEqual(division(50,2), 25)



# This runs our tests
if __name__ == '__main__':
    unittest.main()
