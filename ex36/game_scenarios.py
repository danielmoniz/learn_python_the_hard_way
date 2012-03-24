from scenario import Scenario
class GameScenarios():

    def __init__(self):
        self.game_scenarios = self.set_game_scenarios()

    def set_game_scenarios(self):
        """Return the complete set of game scenarios.
        Scenarios include the following data: 
            - indexed by location, ie. 'XxY' for (x, y)
            - 'description' of location
            - 'actions' that a player can take
            - 'opponent' to defeat that will try to kill you
            - 'unlockable' actions that are allowed after defeating opponents
            """
        scenarios = {
            "default": {"description": "Nothing seems unusual about this place.", 
                "actions": ["NESW"],
                "opponent": None,
                "unlockable": []},
            "0x0": {"description": "You are in your house.", 
                "actions": ["N"],
                "opponent": None,
                "unlockable": []},
            "0x1": {"description": """You have left your house and are now in the town
                square. You can go in any direction you like, and all seem safe.""",
                "actions": ["NESW"],
                "opponent": None,
                "unlockable": []},
            "0x2": {"description": """You come across a troll lair.""",
                "actions": ["S"],
                "opponent": "troll",
                "unlockable": ["NESW"]},
        }
        return scenarios
        

    def get_game_scenario(self, location):
        x, y = location
        try:
            game_scenario = self.game_scenarios[str(x) + "x" + str(y)]
        except KeyError:
            game_scenario = self.game_scenarios["default"]
        return Scenario(**game_scenario)

    def get_default_scenario(self):
        return self.game_scenarios["default"]
