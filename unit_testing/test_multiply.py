import unittest

def mult(a, b):
    return a * b

class multTests(unittest.TestCase):

    def testOne(self):
        self.assertEqual(mult(3,5), 15)
    def testTwo(self):
        self.assertNotEqual(mult(10,10), 101)
    def testThree(self):
        self.assertTrue(mult(3,3), 9)


if __name__ == '__main__':
    unittest.main()