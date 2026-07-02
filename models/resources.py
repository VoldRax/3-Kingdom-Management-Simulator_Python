class Resources:
    def __init__(self):
        self.resources = {
            "food": 100,
            "wood": 50,
            "stone": 25,
            "iron": 10,
        }

    def increase(self, resource, amount):
        self.resources[resource] += amount

    def decrease(self, resource, amount):
        self.resources[resource] -= amount

    def has(self, resource, amount):
        if amount > self.resources[resource]:
            return False
        else:
            return True

    def consumeFood(self, amount):
        self.resources["food"] -= amount