import unittest

class MyExcept(Exception):
    pass

class SecondEx(Exception):
    pass

def throw_ex(var):
    if var == 100:
        raise MyExcept("Not a valid number")
    elif var == 200:
        raise SecondEx("Not a valid...")
    else:
        return True

class LearnUnitTesting(unittest.TestCase):

    def test_sample(self):
        self.assertEqual(throw_ex(10), True)

    def test_sample2(self):
        # First param is exception, 2nd is function (not calling the function), param the function will take is 3rd argument
        self.assertRaises((MyExcept,SecondEx), throw_ex, 200)


if __name__ == "__main__":
    unittest.main()