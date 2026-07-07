class ArmyService:

    def __init__(self, kingdom):
        self.kingdom = kingdom

    def train_soldiers(self, unit_type, amount):
        population = self.population
        economy = self.economy
        army = self.army

        training_cost = {
            "infantry": 10,
            "archers": 15,
            "cavalry": 30,
        }

        if amount <= 0:
            return False

        if population.available_workers < amount:
            return False

        total_cost = training_cost[unit_type] * amount

        if not economy.can_afford(total_cost):
            return False

        population.decrease(amount)      # Remove unemployed civilians
        economy.remove_gold(total_cost)  # Pay training cost
        army.recruit(unit_type, amount)  # Add soldiers

        return True
    
    def feed_army(self, kingdom):
        food_needed = kingdom.army.total

        if kingdom.resources.food >= food_needed:
            kingdom.resources.consume_food(food_needed)
            return True

        # Not enough food
        kingdom.resources.food = 0
        kingdom.army.change_morale(-10)

        return False