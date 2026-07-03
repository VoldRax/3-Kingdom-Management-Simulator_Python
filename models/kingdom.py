from economy import Economy
from army import Army
from population import Population
from resources import Resources
from building import BuildingManager


class Kingdom:

    def __init__(self, name):
        self.name = name
        self.economy = Economy()
        self.population = Population()
        self.army = Army()
        self.resources = Resources()
        self.buildings = BuildingManager()
        self.turn = 0

    def nextTurn(self):
        self.turn += 1

        # Buildings produce resources
        production = self.buildings.produceResources()
        self.resources.addResources(production)

        # Population consumes food
        self.resources.consumeFood(self.population.total)

        # Economy updates
        self.economy.nextTurn()

    def getSummary(self):
        return {
            "Kingdom": self.name,
            "Turn": self.turn,
            "Population": self.population.total,
            "Unemployed": self.population.availableWorkers,
            "Jobs": self.population.allJobs(),
            "Resources": self.resources.allResources(),
            "Army": self.army.summary(),
            "Buildings": self.buildings.all(),
            "Economy": self.economy.summary()
        }

    def toDict(self):
        return {
            "name": self.name,
            "turn": self.turn,
            "economy": self.economy.summary(),
            "population": {
                "jobs": self.population.allJobs(),
                "unemployed": self.population.availableWorkers
            },
            "resources": self.resources.allResources(),
            "army": self.army.summary(),
            "buildings": self.buildings.all()
        }

    def fromDict(self, data):
        self.name = data["name"]
        self.turn = data["turn"]

        self.population.jobs = data["population"]["jobs"]
        self.population.unemployed = data["population"]["unemployed"]

        self.resources.resources = data["resources"]

        self.economy.gold = data["economy"]["gold"]
        self.economy.taxRate = data["economy"]["taxRate"]
        self.economy.tradeIncome = data["economy"]["tradeIncome"]
        self.economy.expenses = data["economy"]["expenses"]

        self.army.morale = data["army"]["morale"]
        self.army.units = data["army"]["units"]

        self.buildings = data["buildings"]