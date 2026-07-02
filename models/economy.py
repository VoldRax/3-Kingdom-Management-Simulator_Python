class Economy:
    def __init__(self):
        self.gold = 1000
        self.taxRate = 3
        self.tradeIncome = 18
        self.expenses = 200

    def addGold(self, amount):
        self.gold += amount
        

    def removeGold(self, amount):
        self.gold += amount
        

    def canAfford(self, amount):
        if amount > self.gold:
            return False
        else:
            return True
    
    def changeTaxRate(self, newTaxRate):
        self.taxRate += newTaxRate
    
    def calculateTotalIncome():
        pass

    def calculateTotalExpenses():
        pass