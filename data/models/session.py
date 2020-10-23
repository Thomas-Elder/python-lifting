
from data.models.exercise import Exercise
from data.models.set import Set
from datetime import datetime

class Session:

    def __init__(self, date: datetime):
        self.date = date
        self.exercises = {}
        self.competition = False

    def addExercise(self, exercise: Exercise):

        if exercise.name in self.exercises:
            for s in exercise.sets:
                self.exercises[exercise.name].sets.append(s)
        else:
            self.exercises[exercise.name] = exercise

    def getDate(self):
        return self.date

    def getExercises(self) -> list:
        return self.exercises