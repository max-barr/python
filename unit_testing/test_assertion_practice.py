import unittest

class Test():
    pass

class Test1():
    pass

class LearnAssertions(unittest.TestCase):

    def test_sample(self):
        a = 1
        b = 1
        self.assertEqual(a,b)

    def test_sample2(self):
        a = 1
        b = 10
        self.assertNotEqual(a,b)

    def test_sample3(self):
        a = 1
        b = 1
        self.assertIs(a,b)

    def test_sample4(self):
        a = 1
        b = a
        self.assertIs(a,b)

    def test_sample5(self):
        t1 = Test()
        t2 = t1
        self.assertIs(t1,t2)
    
    def test_sample6(self):
        #These are different instances of Test()
        t1 = Test()
        t2 = Test()
        self.assertIsNot(t1,t2)

    

    


if __name__ == "__main__":
    unittest.main()