class GameState():
    """Defines a game_state object which stores information about the current
    state of the game."""

    def __init__(self, game_scenarios, location = (0, 0), description = "", event = None):
        """Sets the game_state object using the current location of the player,
        the description of that location, and text describing the most recent
        event in that location."""

        self.location = location 
        self.event = event 
        self.description = self.get_location_description()

    def __str__(self): 
        return self.get_description()

    def get_description(self):
        """Return the description of the game_state object."""
        return self.description

    def get_location_description(self):
        """Get the description for the current location stored in this game_state object."""
        return game_scenarios.get_game_scenario(self.location)
