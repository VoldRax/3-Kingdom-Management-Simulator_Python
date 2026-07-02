class Population:
    def __init__(self):
        self.total = self.jobs["farmers"] + self.jobs["workers"] + self.jobs["merchants"] + self.jobs["scholars"] + self.jobs["soldiers"]
        self.jobs = {
                        "farmers": 50,
                        "workers": 20,
                        "merchants": 10,
                        "scholars": 5,
                        "soldiers": 30
                        }
        self.health = 80
        self.happiness = 50

    def increase(self, amount):
        self.total += amount

    def decrease(self, amount):
        self.total -= amount

    def assignWorkers(self, job, amount):
        pass