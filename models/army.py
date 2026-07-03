class Army:
    def __init__(self):
        self.morale = 80
        self.units = {"archers": 10,
                      "infantry": 10,
                    "cavalry": 10}
        
    def recruit(self, unit, amount):
        self.units[unit] += amount
    
    def recruit(self, unit, amount):
        self.units[unit] += amount
    
    def changeMorale(self, amount):
        self.morale = amount

    def calculatePower(self):
        pass