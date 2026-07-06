class Army:

    def __init__(self):
        self.morale = 80

        self.units = {
            "archers": 10,
            "infantry": 10,
            "cavalry": 10
        }

    @property
    def total_units(self):
        return sum(self.units.values())

    def recruit(self, unit, amount):
        if unit not in self.units or amount <= 0:
            return False

        self.units[unit] += amount
        return True

    def remove_units(self, unit, amount):
        if unit not in self.units or amount <= 0:
            return False

        if amount > self.units[unit]:
            return False

        self.units[unit] -= amount
        return True

    def get_units(self, unit):
        return self.units.get(unit, 0)

    def all_units(self):
        return self.units

    def change_morale(self, amount):
        self.morale += amount
        self.morale = max(0, min(100, self.morale))

    def calculate_power(self):
        power = (
            self.units["archers"] * 2 +
            self.units["infantry"] * 3 +
            self.units["cavalry"] * 5
        )

        morale_bonus = power * (self.morale / 100)

        return int(morale_bonus)

    def summary(self):
        return {
            "morale": self.morale,
            "total_units": self.total_units,
            "units": self.units,
            "power": self.calculate_power()
        }