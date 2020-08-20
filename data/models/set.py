
from data.models.exercise import Exercise

class Set:

    def __init__(self, exercise: Exercise, totalRepetitions: int, successfulRepetitions: int, failedRepetitions: int, weight: int):
        self.exercise = exercise
        self.totalRepetitions = totalRepetitions
        self.successfulRepetitions = successfulRepetitions
        self.failedRepetitions = failedRepetitions
        self.weight = weight
        