class PopulationService:

    def __init__(self, kingdom):
        self.kingdom = kingdom

    def calculate_births(self):
        population = self.kingdom.population.total

        rate = 0.02

        modifier = 1.0

        if self.kingdom.population.happiness >= 80:
            modifier += 0.20

        if self.kingdom.population.health >= 80:
            modifier += 0.10

        if self.kingdom.resources.food >= population:
            modifier += 0.10

        births = int(population * rate * modifier)

        return births
    
    def calculate_deaths(self):
        population = self.kingdom.population.total
        health = self.kingdom.population.health
        happiness = self.kingdom.population.happiness
        food = self.kingdom.resources.food

        rate = 0.01
        modifier = 1.0

        # Health
        if health >= 80:
            modifier -= 0.2
        elif health <= 40:
            modifier += 0.5

        # Food
        if food < population:
            modifier += 0.5

        # Happiness
        if happiness <= 30:
            modifier += 0.2

        return max(0, int(population * rate * modifier))

    def grow_population(self, kingdom):
        births = self.calculate_births(kingdom)
        deaths = self.calculate_deaths(kingdom)

        kingdom.population.increase(births)
        kingdom.population.decrease(deaths)

        return {
            "births": births,
            "deaths": deaths,
            "net": births - deaths,
        }
    
    def update_happiness(self):
        if self.kingdom.resources.food < self.kingdom.population.total:
            self.kingdom.population.change_happiness(-10)
        else:
            self.kingdom.population.change_happiness(+2)

        if self.kingdom.economy.tax_rate > 0.20:
            self.kingdom.population.change_happiness(-5)

        if self.kingdom.population.health > 80:
            self.kingdom.population.change_happiness(+3)

    def starvation_check(self):
        population = self.kingdom.population.total
        food = self.kingdom.resources.food

        # Enough food
        if food >= population:
            self.kingdom.resources.consume_food(population)
            return

        # Food shortage
        shortage = population - food

        # Consume all remaining food
        self.kingdom.resources.food = 0

        # People become unhealthy and unhappy
        self.kingdom.population.change_health(-10)
        self.kingdom.population.change_happiness(-15)

        # Some people die from starvation
        deaths = max(1, shortage // 2)
        self.kingdom.population.decrease(deaths)