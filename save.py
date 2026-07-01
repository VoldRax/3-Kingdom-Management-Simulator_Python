import json
import os

from state import game


def saveData():
    fileName = input("Enter the file name: ")
    filePath = os.path.join(os.getcwd(), f"{fileName}.json")

    with open(filePath, "w") as f:
        json.dump(game, f, indent=4)

    print(f"File saved to:\n{filePath}")


def loadData():
    try:
        filePath = input("Enter the file path: ")

        with open(filePath, "r") as f:
            loadedGame = json.load(f)

        game.clear()
        game.update(loadedGame)

        print("Game loaded successfully !!!")

    except FileNotFoundError:
        print("Invalid file path !!!")

    except json.JSONDecodeError:
        print("Invalid save file.")