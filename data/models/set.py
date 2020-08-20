

class Set:

    def __init__(self):
        self.totalRepetitions = 0
        self.successfulRepetitions = 0
        self.failedRepetitions = 0
        self.weight = 0

    def addRepetitions(self, totalRepetitions: int, successfulRepetitions: int, failedRepetitions: int, weight: int):
        self.totalRepetitions = totalRepetitions
        self.successfulRepetitions = successfulRepetitions
        self.failedRepetitions = failedRepetitions
        self.weight = weight

    def getTotalRepetitions(self):
        return self.totalRepetitions
    
    def getSuccessfulRepetitions(self):
        return self.successfulRepetitions

    def getFailedRepetitions(self):
        return self.failedRepetitions

    def getWeight(self):
        return self.weight