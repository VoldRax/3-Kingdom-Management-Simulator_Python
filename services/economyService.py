class EconomyService:

    UNIT_UPKEEP = {
        "archers": 2,
        "infantry": 3,
        "cavalry": 5,
    }

    def __init__(self, kingdom):
        self.kingdom = kingdom

    def collect_taxes(self):
        population = self.kingdom.population.total
        tax_rate = self.kingdom.economy.tax_rate

        taxes = population * tax_rate

        print(f"Population: {population}")
        print(f"Tax Rate: {tax_rate}")
        print("Collecting taxes...")

        self.kingdom.economy.add_gold(taxes)

        print("Taxes Collected!")
        print(f"Gold Gained: +{taxes}")

    def calculate_trade_income(self):
        merchants = self.kingdom.population.get_workers("merchants")
        population = self.kingdom.population.total

        market_bonus = 0

        merchant_income = merchants * 2
        population_bonus = population * 0.1

        trade_income = int(
            merchant_income
            + population_bonus
            + market_bonus
        )

        self.kingdom.economy.trade_income = trade_income

        return trade_income

    def pay_maintenance(self):
        army = self.kingdom.army

        total_cost = sum(
            army.get_units(unit) * upkeep
            for unit, upkeep in self.UNIT_UPKEEP.items()
        )

        if self.kingdom.economy.remove_gold(total_cost):
            return total_cost

        return None
    
    