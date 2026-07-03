class Economy:

    def __init__(self):
        self.gold = 1000
        self.taxRate = 3
        self.tradeIncome = 18
        self.expenses = 200

    def addGold(self, amount):
        if amount <= 0:
            return False

        self.gold += amount
        return True

    def removeGold(self, amount):
        if amount <= 0:
            return False

        if amount > self.gold:
            return False

        self.gold -= amount
        return True

    def canAfford(self, amount):
        return self.gold >= amount

    def pay(self, amount):
        return self.removeGold(amount)

    def earn(self, amount):
        return self.addGold(amount)

    def changeTaxRate(self, newTaxRate):
        if newTaxRate < 0:
            return False

        self.taxRate = newTaxRate
        return True

    def calculateTotalIncome(self):
        taxIncome = self.taxRate * 10

        return taxIncome + self.tradeIncome

    def calculateTotalExpenses(self):
        return self.expenses

    def netIncome(self):
        return self.calculateTotalIncome() - self.calculateTotalExpenses()

    def nextTurn(self):
        self.gold += self.netIncome()

    def summary(self):
        return {
            "gold": self.gold,
            "taxRate": self.taxRate,
            "tradeIncome": self.tradeIncome,
            "expenses": self.expenses,
            "netIncome": self.netIncome()
        }