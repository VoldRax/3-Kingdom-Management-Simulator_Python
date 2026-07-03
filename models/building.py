class Buildings:

    def __init__(self, buildingType, name=None):
        self.buildingType = buildingType
        self.name = name if name else buildingType

        self.level = 1
        self.cost = 50
        self.maintenance = 10
        self.workersRequired = 12

    def upgrade(self):
        self.level += 1

    def downgrade(self):
        if self.level > 1:
            self.level -= 1

    def maintenanceCost(self, amount):
        self.maintenance += amount

    def bonus(self):
        pass

    def produce(self):
        return {}

class Farm(Buildings):

    def __init__(self, name=None):
        super().__init__("Farm", name)

        self.cost = 40
        self.maintenance = 5
        self.workersRequired = 6

    def produceFood(self):
        return 50 * self.level

    def produce(self):
        return {
            "food": self.produceFood()
        }
    
class Mine(Buildings):

    def __init__(self, name=None):
        super().__init__("Mine", name)

        self.cost = 80
        self.maintenance = 12
        self.workersRequired = 10

    def produceIron(self):
        return 20 * self.level

    def produceCoal(self):
        return 10 * self.level

    def produce(self):
        return {
            "iron": self.produceIron(),
            "coal": self.produceCoal()
        }

class Market(Buildings):

    def __init__(self, name=None):
        super().__init__("Market", name)

        self.cost = 100
        self.maintenance = 15
        self.workersRequired = 8

    def generateTradeIncome(self):
        return 75 * self.level

    def produce(self):
        return {
            "gold": self.generateTradeIncome()
        }


class Barracks(Buildings):

    def __init__(self, name=None):
        super().__init__("Barracks", name)

        self.cost = 150
        self.maintenance = 20
        self.workersRequired = 15

    def trainUnits(self):
        return 5 * self.level

class Hospital(Buildings):

    def __init__(self, name=None):
        super().__init__("Hospital", name)

        self.cost = 120
        self.maintenance = 18
        self.workersRequired = 10

    def healPopulation(self):
        return 15 * self.level

class School(Buildings):

    def __init__(self, name=None):
        super().__init__("School", name)

        self.cost = 110
        self.maintenance = 15
        self.workersRequired = 8

    def educatePopulation(self):
        return 10 * self.level
class BuildingManager:

    def __init__(self):
        self.buildings = {}

    def construct(self, building):
        if building.buildingType not in self.buildings:
            self.buildings[building.buildingType] = []

        self.buildings[building.buildingType].append(building)

    def destroy(self, buildingName):
        for buildingType, buildingList in self.buildings.items():
            for building in buildingList:
                if building.name == buildingName:
                    buildingList.remove(building)

                    if not buildingList:
                        del self.buildings[buildingType]

                    return building

        return None

    def upgrade(self, buildingName):
        building = self.find(buildingName)

        if building:
            building.upgrade()
            return True

        return False

    def find(self, buildingName):
        for buildingList in self.buildings.values():
            for building in buildingList:
                if building.name == buildingName:
                    return building

        return None

    def count(self, buildingType):
        return len(self.buildings.get(buildingType, []))

    def all(self):
        allBuildings = []

        for buildingList in self.buildings.values():
            allBuildings.extend(buildingList)

        return allBuildings

    def produceResources(self):
        resources = {}

        for building in self.all():
            production = building.produce()

            for resource, amount in production.items():
                resources[resource] = resources.get(resource, 0) + amount

        return resources