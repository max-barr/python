import unittest

# reverseList - Write a function that reverses the values in the list (without creating a temporary array).

def reverseList(list):
    for i in range(int(len(list)/2)):
        list[i], list[len(list)-i-1] = list[len(list)-i-1], list[i]
    return list

class reverseListTests(unittest.TestCase):
    def testOne(self):
        self.assertEqual(reverseList([1,3,5]), [5,3,1])
    def testTwo(self):
        self.assertEqual(reverseList([2,4,6]), [6,4,2])
    def testThree(self):
        self.assertEqual(reverseList([22,45,1,666]), [666,1,45,22])
    def testFour(self):
        self.assertEqual(reverseList([1,2,3,4,5,6,7]), [7,6,5,4,3,2,1])

# ------------------------------------






if __name__ == '__main__':
    # This runs our tests
    unittest.main()