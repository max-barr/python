from tkinter.tix import Tree
import unittest

class Test():
    pass

class MyExcept(Exception):
    pass

class SecondEx(Exception):
    pass

def throw_ex(num):
    if num == 100:
        raise MyExcept("Not valid")
    elif num == 200:
        raise SecondEx("Not a valid number")
    else:
        return True


# Create class with camel case
class TestingAssertions(unittest.TestCase):

    def test_sample1(self):
        a = 1
        b = 1
        self.assertEqual(a,b)

    def test_sample2(self):
        t1 = Test()
        t2 = Test()
        self.assertIsInstance(t1,Test)

    def test_sample3(self):
        t1 = 10
        t2 = 10
        t3 = Test()
        self.assertIsNotNone(t1)

    def test_exception(self):
        self.assertRaises((MyExcept,SecondEx), throw_ex, 200)





# Gateway to the command line
if __name__ == "__main__":
    unittest.main()