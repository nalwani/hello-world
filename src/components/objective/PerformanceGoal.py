from components.objective.objective import Objective


class PerformanceGoal(Objective):

    def __init__(self, name):
        super().__init__(name)

    def setDeadline(self, deadline):
        super().deadline = deadline
