
from data.models.set import Set

class Exercise:

    def __init__(self, name: str):
        self.name = name
        self.sets = []

    def addSet(self, set: Set):
        self.sets.append()

    def getSets(self):
        return self.sets