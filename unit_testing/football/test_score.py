import unittest
import score

class TestScore(unittest.TestCase):

    def test_touchdown(self):
        self.assertEqual(score.touchdown(0), 7)
        self.assertEqual(score.touchdown(20), 27)
        self.assertEqual(score.touchdown(3), 10)

    def test_two_point_conversion(self):
        self.assertEqual(score.two_point_conversion(0), 8)
        self.assertEqual(score.two_point_conversion(20), 28)
        self.assertEqual(score.two_point_conversion(3), 11)

    def test_field_goal(self):
        self.assertEqual(score.field_goal(0), 3)
        self.assertEqual(score.field_goal(20), 23)
        self.assertEqual(score.field_goal(3), 6)

    def test_safety(self):
        self.assertEqual(score.safety(0), 2)
        self.assertEqual(score.safety(14), 16)
        self.assertEqual(score.safety(28), 30)

if __name__ == "__main__":
    unittest.main()