import unittest
from Player import Player

class TestPlayer(unittest.TestCase):

    def setUp(self):
        print("Running Setup")
        self.player_1 = Player('Damian', 'Lillard', 'Point Guard', 'Portland Trail Blazers', 0)
        self.player_2 = Player('LeBron', 'James', 'Forward', 'Los Angeles Lakers', 6)
        self.player_3 = Player('Joel', 'Embiid', 'Center', 'Philadelphia 76ers', 21)

    def test_player_card(self):
        self.assertEqual(self.player_1.player_card, 'Damian Lillard, number 0, Point Guard for the Portland Trail Blazers')
        self.assertEqual(self.player_2.player_card, 'LeBron James, number 6, Forward for the Los Angeles Lakers')
        self.assertEqual(self.player_3.player_card, 'Joel Embiid, number 21, Center for the Philadelphia 76ers')

    def test_tee_him_up(self):
        self.assertEqual(self.player_1.tee_him_up(), "Damian Lillard has been assessed a technical foul. The other team will shoot one free throw.")
        self.assertNotEqual(self.player_1.tee_him_up(), "Damannn Lillard has been assessed a technical foul. The other team will shoot one free throw.")
        
    def tearDown(self):
        print("Running Teardown")

if __name__ == "__main__":
    unittest.main()