import random

from state import game
from events import trigger_event
from reports import checkCurrentState, kingdomReport
from utils import prepareScreen, displayKingdomStats 
from constants import menuOptions
from actions import (
    collectTaxes,
    buyFood,
    trainSoldiers,
    expandTerritory,
    consumeFood
)
from save import saveData, loadData

def endTurn():
    consumeFood()
    game["turn"] += 1

def consumeFood():
    foodConsumed = game["kingdom"]["population"] // 10
    game["kingdom"]["food"] -= foodConsumed

def mainMenu():

    nextEventTurn = random.randint(3, 6)

    try:
        while True:

            checkCurrentState()

            if game["turn"] >= nextEventTurn:
                trigger_event()
                endTurn()
                nextEventTurn = game["turn"] + random.randint(3, 10)

                input("\nPress Enter...")
                continue

            prepareScreen()
            displayKingdomStats()
            print(menuOptions)

            userChoice = input("Enter your choice:\n> ")

            match userChoice:

                case "1":
                    prepareScreen()
                    collectTaxes()
                    endTurn()
                    input("\nPress Enter...")

                case "2":
                    prepareScreen()
                    buyFood()
                    endTurn()
                    input("\nPress Enter...")

                case "3":
                    prepareScreen()
                    trainSoldiers()
                    endTurn()
                    input("\nPress Enter...")

                case "4":
                    prepareScreen()
                    expandTerritory()
                    endTurn()
                    input("\nPress Enter...")

                case "5":
                    prepareScreen()
                    kingdomReport()
                    input("\nPress Enter...")

                case "6":
                    prepareScreen()
                    print("Turn ended !!!")
                    endTurn()
                    input("\nPress Enter...")

                case "7":
                    prepareScreen()
                    saveData()
                    input("\nPress Enter...")

                case "8":
                    prepareScreen()
                    loadData()
                    input("\nPress Enter...")

                case "9":
                    print("Thank You!")
                    break

                case _:
                    prepareScreen()
                    print("Invalid choice!")
                    input("\nPress Enter...")

    except KeyboardInterrupt:
        print("\n\nGame interrupted.")

        choice = input("Save before exiting? (y/n): ").lower()

        if choice in ("y", "yes"):
            saveData()

        print("Goodbye!")