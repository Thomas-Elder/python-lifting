
from data.models.exercise import Exercise
from data.models.set import Set
from datetime import datetime

class Session:

    def __init__(self, date: datetime):
        self.date = date
        self.exercises = []
        self.competition = False

    def addExercise(self, exercise: Exercise):
        self.exercises.append(exercise)

    def getDate(self):
        return self.date

    def getExercises(self) -> list:
        return self.exercises