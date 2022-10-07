class Commitment:
    def __init__(self):
        self.strategy = " "
        self.roadblocks = []

    def selectStrategy(self, strategy):
        if strategy == "pay":
            return "you choose to pay"
        if strategy == "accountability patner":
            return "you choose accountability partner"
        if strategy == "sharing":
            return "you choose charing"

        return "this strategy doesn't exist"

    def addRoadblock(self, roadblock):
        return self.roadblocks.append(roadblock)
