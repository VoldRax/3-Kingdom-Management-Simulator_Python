
import random
from utils import prepareScreen, showBanner, clearConsole
from state import game

def trigger_event():

    event = random.choice(["plague", "bandits", "gold_mine", "festival", "drought"])

    if event == "plague":
        prepareScreen()
        game["kingdom"]["population"] -= 20
        print("Event: Plague\nTreating People !!!")
        print("-20 population")
        return

    elif event == "bandits":
        prepareScreen()
        game["kingdom"]["gold"] -= 100
        print("Event: Bandit Attack\nResisting Bandits")
        print("-100 gold")
        return
    elif event == "gold_mine":
        prepareScreen()
        game["kingdom"]["gold"] += 500
        print("Event: Gold Mine discovered\nDigging mines")
        print("+gold 500")
        return
    elif event == "festival":
        prepareScreen()
        game["kingdom"]["happiness"] += 20
        print("Event: Festival\nPeople are happy")
        print("+20 happiness")
        return
    elif event == "drought":
        prepareScreen()
        game["kingdom"]["food"] -= 200
        print("Event: Drought\nProviding food to the people !!!")
        print("-200 food")
        return
