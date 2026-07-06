class Population:

    def __init__(self):
        self.jobs = {
            "farmers": 50,
            "workers": 20,
            "merchants": 10,
            "scholars": 5,
            "soldiers": 30,
        }

        self.unemployed = 20

    @property
    def total(self):
        return sum(self.jobs.values()) + self.unemployed

    @property
    def available_workers(self):
        return self.unemployed

    def increase(self, amount):
        if amount <= 0:
            return False

        self.unemployed += amount
        return True

    def decrease(self, amount):
        if amount <= 0:
            return False

        if amount > self.unemployed:
            return False

        self.unemployed -= amount
        return True

    def assign_workers(self, job, amount):
        if amount <= 0:
            return False

        if job not in self.jobs:
            return False

        if amount > self.unemployed:
            return False

        self.unemployed -= amount
        self.jobs[job] += amount

        return True

    def remove_workers(self, job, amount):
        if amount <= 0:
            return False

        if job not in self.jobs:
            return False

        if amount > self.jobs[job]:
            return False

        self.jobs[job] -= amount
        self.unemployed += amount

        return True

    def get_workers(self, job):
        return self.jobs.get(job, 0)

    def all_jobs(self):
        return self.jobs