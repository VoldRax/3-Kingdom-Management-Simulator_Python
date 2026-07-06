class Economy:

    def __init__(self):
        self.gold = 1000
        self.tax_rate = 3
        self.trade_income = 18
        self.expenses = 200

    # Helper Methods (never directly used)

    def add_gold(self, amount):
        if amount <= 0:
            return False

        self.gold += amount
        return True

    def remove_gold(self, amount):
        if amount <= 0:
            return False

        if amount > self.gold:
            return False

        self.gold -= amount
        return True
    
    # Methods which should be used

    def can_afford(self, amount):
        return self.gold >= amount

    def pay(self, amount):
        return self.remove_gold(amount)

    def earn(self, amount):
        return self.add_gold(amount)

    def change_tax_rate(self, new_tax_rate):
        if new_tax_rate < 0:
            return False

        self.tax_rate = new_tax_rate
        return True

    def calculate_total_income(self):
        tax_income = self.tax_rate * 10
        return tax_income + self.trade_income

    def calculate_total_expenses(self):
        return self.expenses

    def net_income(self):
        return (
            self.calculate_total_income()
            - self.calculate_total_expenses()
        )

    def next_turn(self):
        self.gold += self.net_income()

    def summary(self):
        return {
            "gold": self.gold,
            "tax_rate": self.tax_rate,
            "trade_income": self.trade_income,
            "expenses": self.expenses,
            "net_income": self.net_income(),
        }