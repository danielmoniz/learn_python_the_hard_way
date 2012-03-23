from game_scenarios import GameScenarios
import game_state as GameState
class Game():
    """The main game class. Controls game actions such as starting or ending a 
    game."""

    # game_over = False
    # game_state = None

    def __init__(self):
        """Initialize the game."""
        self.game_scenarios = GameScenarios()
        self.game_state = GameState.GameState(self.game_scenarios, (0, 0), "test descr", "no event")
        self.game_over = False

    def start_game(self):
        """Start the actual game."""
        pass

    def end_game(self, message):
        """End the game with a message."""
        self.game_over = True
        print message
        exit(0)

    def win_game(self):
        """Called when a player wins the game. Also ends the game."""
        self.end_game("You have won!")

    def lose_game(self):
        """Ends the game for a player with a losing message."""
        self.end_game("You have lost!")

    def is_game_over(self):
        """Return true if the game is over, false if otherwise."""
        return self.game_over

    def get_game_state(self):
        """Return the state of the current game. Eg. determine location, then 
        the string to go along with location, and return all information in a 
        GameState object."""
        return self.game_state

    def get_player_input(self, game_state):
        """Return input from the player. Loop until valid input is found."""
        while True:
            """print game_state.location
            print game_state.event
            print game_state.description"""
            user_input = raw_input(game_state)
            self.win_game()
            return user_input
