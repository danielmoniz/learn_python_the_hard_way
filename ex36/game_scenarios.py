class GameScenarios():

    def __init__(self):
        self.game_scenarios = self.set_game_scenarios()

    def set_game_scenarios(self):
        """Return the complete set of game scenarios.
        Scenarios include the following data: 
            - indexed by location, ie. 'XxY' for (x, y)
            - 'description' of location
            - 'options' that a player can take
            - 'opponent' to defeat that will try to kill you
            - 'unlockable' actions that are allowed after defeating opponents
            """
        scenarios = {
            "0x0": {"description": "You are in your house.", 
                "options": ["N"]},
            "0x1": {"""description": "You have left your house and are now in the town
                square. You can go in any direction you like, and all seem safe."""},
                "options": ["NESW"]},
        }
        return scenarios
        

    def get_game_scenario(self, location):
        x, y = location
        return self.game_scenarios[str(x) + "x" + str(y)]["description"]
