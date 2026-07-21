import random

from data.events import events


class EventService:

    def __init__(self, kingdom):
        self.kingdom = kingdom
        self.events = events

    def trigger_random_event(self):
        event = random.choice(self.events)

        self.apply_event(event)

        return event

    def apply_event(self, event):
        event.effect(self.kingdom)

    def load_events(self):
        self.events = events