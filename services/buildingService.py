from models.building import (
    Farm,
    Mine,
    Market,
    Barracks,
    Hospital,
    School,
)


class BuildingService:

    BUILDING_TYPES = {
        "farm": Farm,
        "mine": Mine,
        "market": Market,
        "barracks": Barracks,
        "hospital": Hospital,
        "school": School,
    }

    def __init__(self, kingdom):
        self.kingdom = kingdom

    def construct_building(self, building_type, name=None):
        building_class = self.BUILDING_TYPES.get(building_type.lower())

        if building_class is None:
            return False

        building = building_class(name)

        if not self.kingdom.economy.can_afford(building.cost):
            return False

        if self.kingdom.population.available_workers < building.workers_required:
            return False

        self.kingdom.economy.remove_gold(building.cost)
        self.kingdom.population.decrease(building.workers_required)

        self.kingdom.buildings.construct(building)

        return True
    
    def upgrade_building(self, building_name):
        pass

    def repair_building(self, building_name):
        pass

    def demolish_building(self, building_name):
        pass

    def collect_building_production(self):
        pass