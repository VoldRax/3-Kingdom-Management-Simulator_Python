class Army:

    def __init__(self):
        self.morale = 80

        self.units = {
            "archers": 10,
            "infantry": 10,
            "cavalry": 10
        }

    @property
    def totalUnits(self):
        return sum(self.units.values())

    def recruit(self, unit, amount):
        if unit not in self.units or amount <= 0:
            return False

        self.units[unit] += amount
        return True

    def removeUnits(self, unit, amount):
        if unit not in self.units or amount <= 0:
            return False

        if amount > self.units[unit]:
            return False

        self.units[unit] -= amount
        return True

    def getUnits(self, unit):
        return self.units.get(unit, 0)

    def allUnits(self):
        return self.units

    def changeMorale(self, amount):
        self.morale += amount

        if self.morale > 100:
            self.morale = 100
        elif self.morale < 0:
            self.morale = 0

    def calculatePower(self):
        power = (
            self.units["archers"] * 2 +
            self.units["infantry"] * 3 +
            self.units["cavalry"] * 5
        )

        moraleBonus = power * (self.morale / 100)

        return int(moraleBonus)

    def summary(self):
        return {
            "morale": self.morale,
            "totalUnits": self.totalUnits,
            "units": self.units,
            "power": self.calculatePower()
        }