class Scenario():
    """Stores data about a given scenario, and provides methods for getting the data."""

    def __init__(self, description = "", actions = [], opponent = None, unlockable = []):
        self.description = description
        self.actions = actions
        self.opponent = opponent
        self.unlockable = unlockable

    def __str__(self):
        """Output the scenario in text form."""
        output_string = self.description 
        output_string += "\n" + str(self.actions)
        output_string += "\n" + str(self.opponent)
        output_string += "\n" + str(self.unlockable)
        return output_string

    def get_description(self):
        return self.description

    def get_actions(self):
        return self.actions

    def get_opponent(self):
        return self.opponent

    def get_unlockable(self):
        return self.unlockable
