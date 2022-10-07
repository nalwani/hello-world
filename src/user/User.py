class User:

    def __index__(self, name, age):
        self.name = name
        self.age = age
        self.objectives = []

    def addObjective(self, objective):
        return self.objectives.append(objective)

    def getObjective(self, objective):
        i = self.objectives.index(objective)
        return self.objectives[i]

    def removeObjective(self, objective):
        return self.objectives.remove(objective)
