import unittest
from src.main import Game

class TestRockPaperScissors(unittest.TestCase):

    def setUp(self):
        self.game = Game()

    def test_valid_moves(self):
        """Test that valid moves are accepted"""
        self.assertTrue(self.game.is_valid_move('R'))
        self.assertTrue(self.game.is_valid_move('P')) 
        self.assertTrue(self.game.is_valid_move('S'))

    def test_invalid_moves(self):
        """Test that invalid moves are rejected"""
        self.assertFalse(self.game.is_valid_move('X'))
        self.assertFalse(self.game.is_valid_move(''))
        self.assertFalse(self.game.is_valid_move('RP'))

    def test_game_logic(self):
        """Test game winning logic"""
        # Rock beats Scissors
        self.assertEqual(self.game.get_winner('R', 'S'), 'Player')
        self.assertEqual(self.game.get_winner('S', 'R'), 'Computer')
        
        # Scissors beats Paper
        self.assertEqual(self.game.get_winner('S', 'P'), 'Player')
        self.assertEqual(self.game.get_winner('P', 'S'), 'Computer')
        
        # Paper beats Rock
        self.assertEqual(self.game.get_winner('P', 'R'), 'Player')
        self.assertEqual(self.game.get_winner('R', 'P'), 'Computer')

    def test_ties(self):
        """Test tie scenarios"""
        self.assertEqual(self.game.get_winner('R', 'R'), 'Tie')
        self.assertEqual(self.game.get_winner('P', 'P'), 'Tie')
        self.assertEqual(self.game.get_winner('S', 'S'), 'Tie')

    def test_score_tracking(self):
        """Test score updates correctly"""
        initial_player = self.game.player_score
        initial_computer = self.game.computer_score
        
        # Player wins
        self.game.update_score('Player')
        self.assertEqual(self.game.player_score, initial_player + 1)
        self.assertEqual(self.game.computer_score, initial_computer)
        
        # Computer wins
        self.game.update_score('Computer')
        self.assertEqual(self.game.player_score, initial_player + 1)
        self.assertEqual(self.game.computer_score, initial_computer + 1)

if __name__ == '__main__':
    unittest.main()