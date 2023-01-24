import unittest
from player import Player

class TestPlayer(unittest.TestCase):

    def setUp(self):
        print('Setup')
        self.player_1 = Player('Joe', 'Montana', 'Quarterback', 'San Francisco 49ers', 16)
        self.player_2 = Player('Justin', 'Jefferson', 'Wide Receiver', 'Minnesota Vikings', 84)
        self.player_3 = Player('Patrick', 'Mahomes', 'Quarterback', 'Kansas City Chiefs', 15)
        self.player_4 = Player('Joe', 'Burrow', 'Quarterback', 'Cincinnati Bengals', 9)

    def tearDown(self):
        print('Teardown')
    
    def test_player_card(self):
        self.assertEqual(self.player_1.player_card, 'Joe Montana, Quarterback for the San Francisco 49ers, number 16')
        self.assertEqual(self.player_2.player_card, 'Justin Jefferson, Wide Receiver for the Minnesota Vikings, number 84')
        self.assertEqual(self.player_3.player_card, 'Patrick Mahomes, Quarterback for the Kansas City Chiefs, number 15')
        self.assertEqual(self.player_4.player_card, 'Joe Burrow, Quarterback for the Cincinnati Bengals, number 9')

if __name__ == "__main__":
    unittest.main()