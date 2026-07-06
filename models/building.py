class Building:

    def __init__(self, building_type, name=None):
        self.building_type = building_type
        self.name = name if name else building_type

        self.level = 1
        self.cost = 50
        self.maintenance = 10
        self.workers_required = 12

    def upgrade(self):
        self.level += 1

    def downgrade(self):
        if self.level > 1:
            self.level -= 1

    def increase_maintenance(self, amount):
        self.maintenance += amount

    def bonus(self):
        pass

    def produce(self):
        return {}


class Farm(Building):

    def __init__(self, name=None):
        super().__init__("Farm", name)

        self.cost = 40
        self.maintenance = 5
        self.workers_required = 6

    def produce_food(self):
        return 50 * self.level

    def produce(self):
        return {
            "food": self.produce_food()
        }


class Mine(Building):

    def __init__(self, name=None):
        super().__init__("Mine", name)

        self.cost = 80
        self.maintenance = 12
        self.workers_required = 10

    def produce_iron(self):
        return 20 * self.level

    def produce_coal(self):
        return 10 * self.level

    def produce(self):
        return {
            "iron": self.produce_iron(),
            "coal": self.produce_coal()
        }


class Market(Building):

    def __init__(self, name=None):
        super().__init__("Market", name)

        self.cost = 100
        self.maintenance = 15
        self.workers_required = 8

    def generate_trade_income(self):
        return 75 * self.level

    def produce(self):
        return {
            "gold": self.generate_trade_income()
        }


class Barracks(Building):

    def __init__(self, name=None):
        super().__init__("Barracks", name)

        self.cost = 150
        self.maintenance = 20
        self.workers_required = 15

    def train_units(self):
        return 5 * self.level


class Hospital(Building):

    def __init__(self, name=None):
        super().__init__("Hospital", name)

        self.cost = 120
        self.maintenance = 18
        self.workers_required = 10

    def heal_population(self):
        return 15 * self.level


class School(Building):

    def __init__(self, name=None):
        super().__init__("School", name)

        self.cost = 110
        self.maintenance = 15
        self.workers_required = 8

    def educate_population(self):
        return 10 * self.level


class BuildingManager:

    def __init__(self):
        self.buildings = {}

    def construct(self, building):
        if building.building_type not in self.buildings:
            self.buildings[building.building_type] = []

        self.buildings[building.building_type].append(building)

    def destroy(self, building_name):
        for building_type, building_list in self.buildings.items():
            for building in building_list:
                if building.name == building_name:
                    building_list.remove(building)

                    if not building_list:
                        del self.buildings[building_type]

                    return building

        return None

    def upgrade(self, building_name):
        building = self.find(building_name)

        if building:
            building.upgrade()
            return True

        return False

    def find(self, building_name):
        for building_list in self.buildings.values():
            for building in building_list:
                if building.name == building_name:
                    return building

        return None

    def count(self, building_type):
        return len(self.buildings.get(building_type, []))

    def all(self):
        all_buildings = []

        for building_list in self.buildings.values():
            all_buildings.extend(building_list)

        return all_buildings

    def produce_resources(self):
        resources = {}

        for building in self.all():
            production = building.produce()

            for resource, amount in production.items():
                resources[resource] = resources.get(resource, 0) + amount

        return resources