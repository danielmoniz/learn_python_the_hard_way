class GameState():
    """Defines a game_state object which stores information about the current
    state of the game."""

    # @TODO Remove description and opponent parameters
    def __init__(self, scenario, location = (0, 0), description = "", opponent = None):
        """Sets the game_state object using the current location of the player,
        the description of that location, and text describing the most recent
        event in that location."""

        self.scenario = scenario
        self.location = location 
        try:
            self.description = scenario.description
            self.opponent = scenario.opponent
            self.actions = scenario.actions
        except KeyError:
            self.description = "Nothing seems unusual about this place."
            self.opponent = None
            self.actions = ["NESW"]

    def __str__(self): 
        """The string output when simply outputting the entire GameState object."""
        return self.get_description()

    def get_description(self):
        """Return the description of the game_state object."""
        return self.description
