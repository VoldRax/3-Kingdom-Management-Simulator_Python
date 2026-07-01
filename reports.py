
from utils import showBanner
from state import game, createGame

def playAgain():
    playChoice = input("Wanna play again (y/n)? ").lower()

    if playChoice in ("y", "yes"):
        game.clear()
        game.update(createGame())
    else:
        print("Thank You !!!")
        exit()


def kingdomReport():
    showBanner()
    print("Kingdom Report -->\n")

    for asset, assetQuantity in game["kingdom"].items():
        print(f"{asset}: {assetQuantity}")

    print("\nTreasury: Healthy" if game["kingdom"]["gold"] > 1000 else "\nTreasury: Unhealthy")
    print(
        "\nMilitary Strength: Stable"
        if game["kingdom"]["army"] > 75
        else "\nMilitary Strength: Unstable"
    )
    print(
        "\nFood Situation: Excellent"
        if game["kingdom"]["food"] > 500
        else "\nFood Situation: Poor"
    )
    return

def checkCurrentState():
    showBanner()
    if (
        game["kingdom"]["population"] >= 1000
        and game["kingdom"]["army"] >= 200
        and game["kingdom"]["gold"] >= 10000
        and game["kingdom"]["happiness"] >= 70
        and game["kingdom"]["food"] >= 2500
    ):
        print("You Won !!!")
        playAgain()
        return

    elif (
        game["kingdom"]["food"] <= 0
        or game["kingdom"]["population"] <= 0
        or game["kingdom"]["army"] <= 0
        or game["kingdom"]["happiness"] <= 0
    ):
        print("You lose !!!")
        playAgain()
        return