
from data.models.set import Set

class Exercise:

    def __init__(self, name: str, exType: str):
        self.name = name
        self.type = exType
        self.sets = []

    def totalWeight(self):
        
        total = 0
        if len(self.sets):
            for s in self.sets:
                total += s.totalRepetitions * s.weight

        return total

    def numberOfSets(self):
        
        return len(self.sets)

    def numberOfReps(self):
        
        total = 0
        for s in self.sets:
            total += s.totalRepetitions

        return total

    def topSet(self):
        
        top = Set(0,0,0,0)
        for s in self.sets:
            if s.weight > top.weight:
                top = s

        return top

    def topSetIntensity(self, competitionLifts: dict) -> float:

        base = competitionLifts[self.type]

        return round((self.topSet().weight/base) * 100, 2)

