class Resources:

    def __init__(self):
        self.resources = {
            "food": 100,
            "wood": 50,
            "stone": 25,
            "iron": 10
        }

    def increase(self, resource, amount):
        if resource not in self.resources or amount <= 0:
            return False

        self.resources[resource] += amount
        return True

    def decrease(self, resource, amount):
        if resource not in self.resources or amount <= 0:
            return False

        if amount > self.resources[resource]:
            return False

        self.resources[resource] -= amount
        return True

    def has(self, resource, amount):
        if resource not in self.resources:
            return False

        return self.resources[resource] >= amount

    def consumeFood(self, amount):
        return self.decrease("food", amount)

    def get(self, resource):
        return self.resources.get(resource, 0)

    def allResources(self):
        return self.resources

    def canAfford(self, costs):
        for resource, amount in costs.items():
            if not self.has(resource, amount):
                return False

        return True

    def pay(self, costs):
        if not self.canAfford(costs):
            return False

        for resource, amount in costs.items():
            self.decrease(resource, amount)

        return True

    def addResources(self, resources):
        for resource, amount in resources.items():
            self.increase(resource, amount)