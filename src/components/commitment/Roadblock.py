class Roadblock:
    def __init__(self):
        self.matter = ""
        self.strategies = []

    def define(self, matter):
        self.matter = matter
        return self.matter

    def addStrategy(self, strategy):
        return self.strategies.append(strategy)