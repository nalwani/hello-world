from components.objective.objective import Objective


class ProcessGoal(Objective):

    def __init__(self, name):
        super().__init__(name)
        self.steps = []

    def setDeadline(self, deadline):
        super().deadline = deadline

    def addSteps(self, step):
        return self.steps.append(step)