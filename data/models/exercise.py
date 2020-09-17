
from data.models.set import Set

class Exercise:

    def __init__(self, name: str):
        self.name = name
        self.sets = []

    def totalWeight(self):
        
        total = 0
        if len(self.sets):
            for s in self.sets:
                total += s.totalRepetitions * s.weight

        return total
        
    def numberOfReps(self):
        pass

    def numberOfSets(self):
        pass

    def topSet(self):
        pass