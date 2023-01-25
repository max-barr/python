import unittest
import score

class TestScore(unittest.TestCase):

    def test_field_goal(self):
        self.assertEqual(score.field_goal(24), 26)
        self.assertEqual(score.field_goal(2), 4)
        self.assertEqual(score.field_goal(0), 2)

    def test_free_throw(self):
        self.assertEqual(score.free_throw(1), 2)
        self.assertEqual(score.free_throw(99), 100)
        self.assertEqual(score.free_throw(5), 6)

    def test_three_pointer(self):
        self.assertEqual(score.three_pointer(1), 4)
        self.assertEqual(score.three_pointer(25), 28)
        self.assertEqual(score.three_pointer(15), 18)

# This runs our test
if __name__ == "__main__":
    unittest.main()