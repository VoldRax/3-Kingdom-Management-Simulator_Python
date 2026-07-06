import os
from constants import banner
from state import game

def clearConsole():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def showBanner():
    print(banner)
    return

def prepareScreen():
    clearConsole()
    showBanner()


def displayKingdomStats():
    for asset, assetQuantity in game["kingdom"].items():
        print(f"{asset}: {assetQuantity}")