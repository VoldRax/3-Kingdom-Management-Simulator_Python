from .economy import Economy
from .army import Army
from .population import Population
from .resources import Resources
from .building import BuildingManager


class Kingdom:

    def __init__(self, name):
        self.name = name
        self.economy = Economy()
        self.population = Population()
        self.army = Army()
        self.resources = Resources()
        self.buildings = BuildingManager()
        self.turn = 0

    def next_turn(self):
        self.turn += 1

        # Buildings produce resources
        production = self.buildings.produce_resources()
        self.resources.add_resources(production)

        # Population consumes food
        self.resources.consume_food(self.population.total)

        # Economy updates
        self.economy.next_turn()

    def get_summary(self):
        return {
            "kingdom": self.name,
            "turn": self.turn,
            "population": self.population.total,
            "unemployed": self.population.available_workers,
            "jobs": self.population.all_jobs(),
            "resources": self.resources.all_resources(),
            "army": self.army.summary(),
            "buildings": self.buildings.all(),
            "economy": self.economy.summary(),
        }

    def to_dict(self):
        return {
            "name": self.name,
            "turn": self.turn,
            "economy": self.economy.summary(),
            "population": {
                "jobs": self.population.all_jobs(),
                "unemployed": self.population.available_workers,
            },
            "resources": self.resources.all_resources(),
            "army": self.army.summary(),
            "buildings": self.buildings.all(),
        }

    def from_dict(self, data):
        self.name = data["name"]
        self.turn = data["turn"]

        self.population.jobs = data["population"]["jobs"]
        self.population.available_workers = data["population"]["unemployed"]

        self.resources.resources = data["resources"]

        self.economy.gold = data["economy"]["gold"]
        self.economy.tax_rate = data["economy"]["tax_rate"]
        self.economy.trade_income = data["economy"]["trade_income"]
        self.economy.expenses = data["economy"]["expenses"]

        self.army.morale = data["army"]["morale"]
        self.army.units = data["army"]["units"]

        self.buildings = data["buildings"]