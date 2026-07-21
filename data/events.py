from models.event import Event

events = [
    Event(
        "Good Harvest",
        "The farms produced extra food.",
        lambda kingdom: kingdom.resources.add_food(150)
    ),

    Event(
        "Gold Mine Found",
        "Workers discovered a rich vein of gold.",
        lambda kingdom: kingdom.economy.add_gold(300)
    ),

    Event(
        "Fire",
        "A fire destroyed supplies.",
        lambda kingdom: kingdom.resources.remove_food(100)
    ),

    Event(
        "Disease",
        "Disease spread across the kingdom.",
        lambda kingdom: kingdom.population.decrease(20)
    ),

    Event(
        "Festival",
        "Citizens celebrated together.",
        lambda kingdom: kingdom.happiness.increase(10)
    ),
]