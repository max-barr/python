import unittest
import math

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

# isPalindrome - Write a function that checks whether the given word is a palindrome (a word that spells the same backward).

def isPalindrome(str):
    # Run loop from 0 to len/2
    for i in range(int(len(str)/2)):
        if str[i] != str[len(str)-i-1]:
            return False
    return True

class isPalindromeTests(unittest.TestCase):
    def testOne(self):
        self.assertTrue(isPalindrome("racecar"))
    def testTwo(self):
        self.assertFalse(isPalindrome("smitty"))
    def testThree(self):
        self.assertTrue(isPalindrome("wonderednow"))

# --------------------------------------

# coins - Write a function that determines how many quarters, dimes, nickels, and pennies to give to a customer for a change where you minimize the number of coins you give out.

def coins(num):
    list = []
    quarters = math.floor(num/25)
    list.append(quarters)
    new_num = num % 25
    dimes = math.floor(new_num/10)
    list.append(dimes)
    new_num = new_num % 10
    nickels = math.floor(new_num/5)
    list.append(nickels)
    new_num = new_num % 5
    # Pennies 
    list.append(new_num)
    return list

class coinsTests(unittest.TestCase):
    def testOne(self):
        self.assertEqual(coins(87), [3,1,0,2])
    def testTwo(self):
        self.assertEqual(coins(23), [0,2,0,3])
    def testThree(self):
        self.assertEqual(coins(98), [3,2,0,3])
    def testFour(self):
        self.assertEqual(coins(16), [0,1,1,1])
    def testFive(self):
        self.assertEqual(coins(125), [5,0,0,0])


if __name__ == '__main__':
    # This runs our tests
    unittest.main()