from components.objective import objective


class Outcome(objective):

    def __init__(self, phrase):
        super().__init__(phrase)

    def setDeadline(self, deadline):
        super().deadline = deadline
