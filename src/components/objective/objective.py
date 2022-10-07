class Objective:

    def __init__(self, name):
        self.name = name
        self.deadline = ""
        self.metrics = []

    def __str__(self):
        return f"Objective: {self.name} "

    def addMetric(self, metric):
        return self.metrics.append(metric)

    def removeMetric(self, metric):
        return self.metrics.remove(metric)

    def addDeadline(self, deadline):
        self.deadline = deadline
        return self.deadline
