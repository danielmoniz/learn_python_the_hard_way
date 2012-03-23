import unittest
import game

class TestGameFunctions(unittest.TestCase):

    def setUp(self):
        self.game = game.Game()
        pass

    def test_is_game_over(self):
        self.assertTrue(not self.game.is_game_over())

if __name__ == "__main__":
    unittest.main()
