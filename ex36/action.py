class Action():
    """Defines an action object which provides functions that allow a user to perform actions."""

    def __init__(self, action):
        self.action = action
        self.move_vector = self.determine_move_vector()

    def get_move_vector(self):
        return self.move_vector
        
    def get_action(self):
        return self.action
        
    def determine_move_vector(self):
        if self.action == "N":
            return (0, 1)
        elif self.action == "E":
            return (1, 0)
        elif self.action == "S":
            return (0, -1)
        elif self.action == "E":
            return (-1, 0)
        else:
            return (0, 0)
