from game_scenarios import GameScenarios
from game_state import GameState
from action import Action

from string import upper

class Game():
    """The main game class. Controls game actions such as starting or ending a 
    game."""

    def __init__(self):
        """Initialize the game."""
        self.game_scenarios = GameScenarios()
        location = (0, 0)
        scenario = self.game_scenarios.get_game_scenario(location)
        self.game_state = GameState(scenario, (0, 0), "test descr")
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

    def set_game_state(self, game_state):
        self.game_state = game_state

    def get_player_input(self, game_state):
        """Return input from the player. Loop until valid input is found."""
        successful_input = False
        while not successful_input:
            scenario = game_state.scenario
            actions = scenario.actions
            print game_state
            user_input = raw_input(game_state.get_description())
# convert actions and user_input to all caps for normalization
            actions = [upper(i) for i in actions]
            user_input = upper(user_input)
            if self.is_input_acceptable(user_input, actions):
                # is this line necessary?
                successful_input = True 
                return Action(user_input)
                #self.player_act(user_input)

            #return user_input

    def player_act(self, action):
        """Perform an action requested by a player. Assumes that the given action is valid."""
        self.game_state.location
        location = self.game_state.location
        new_location = tuple([i + j for i, j in zip(location, action.move_vector)])
        new_scenario = self.game_scenarios.get_game_scenario(new_location)
        new_game_state = GameState(new_scenario, new_location)
        return new_game_state

    def is_input_acceptable(self, user_input, actions):
        """Determine whether or not user input is acceptable, ie. it belongs to one of the allowed actions."""
        print "uppercase:", actions, user_input, actions[0]
        is_standard_action = user_input in actions
# @TODO Should not be using [0]! Need a more elegant approach.
        is_move_action = user_input in actions[0] and len(user_input) == 1
        if is_standard_action or is_move_action:
            return True
        else:
            return False
