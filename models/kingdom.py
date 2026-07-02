from economy import Economy
from army import Army
from population import Population
from resources import Resources
from building import Buildings

class Kingdom:

    def __init__(self, name: str):
        self.name = name
        self.economy = Economy()
        self.population = Population()
        self.army = Army()
        self.resources = Resources()
        self.buildings = Buildings()
        self.turn = 0

    def nextTurn():
        pass

    def getSummary():
        pass

    def toDict():
        pass

    def fromDict():
        pass
    