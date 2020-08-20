
import pandas
from data.models.exercise import Exercise
from data.models.set import Set

class Session:

    def __init__(self, date: pandas.datetime):
        self.date = date
        self.exercises = []

    def addExercise(self, exercise: Exercise):
        self.exercises.append(exercise)

    def getDate(self):
        return self.date

    def getExercises(self) -> list:
        return self.exercises