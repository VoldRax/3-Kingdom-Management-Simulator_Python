# Kingdom Management Simulator

from cmath import cos
import os
import random
import json
import time

banner = """==================================
        KINGDOM MANAGEMENT
==================================\n"""

menuOptions = """\n==================================\n
1. Collect Taxes
2. Buy Food
3. Train Soldiers
4. Expand Territory
5. View Kingdom Report
6. End Turn
7. Save Game
8. Load Game
9. Exit

==================================\n"""

kingdom = {
    "gold": 1000,
    "food": 500,
    "population": 100,
    "army": 25,
    "happiness": 75
}

def clearConsole():
    os.system("cls")

def showBanner():
    print(banner)
    return

def displayKingdomStats():
    for asset, assetQuantity in kingdom.items():
        print(f"{asset}: {assetQuantity}")
    
def menu():
    while True:
        clearConsole()
        showBanner()
        displayKingdomStats()
        print(menuOptions)

        userChoice = input("Enter your choice:\n> ")

        match userChoice:
            case "1":
                clearConsole()
                collectTaxes()
                input("\nPress Enter...")

            case "2":
                clearConsole()
                buyFood()
                input("\nPress Enter...")

            case "3":
                clearConsole()
                trainSoldiers()
                input("\nPress Enter...")

            case "4":
                clearConsole()
                
                input("\nPress Enter...")

            case "5":
                clearConsole()
                
                input("\nPress Enter...")

            case "6":
                clearConsole()
                
                input("\nPress Enter...")

            case "7":
                clearConsole()
                input("\nPress Enter...")

            case "8":
                clearConsole()
                input("\nPress Enter...")

            case "9":
                print("Thank You!")
                break

            case _:
                clearConsole()
                print("Invalid choice!")
                input("\nPress Enter...")

def collectTaxes():
    taxRate = random.randint(2, 5)
    estimatedTax = kingdom["population"] * taxRate
    
    print(f"Population: {kingdom["population"]}\nTax rate: {taxRate}")
    print(f"Tax to be collected: {estimatedTax}")
    
    print("Collecting taxes !!!")

    actualTax = estimatedTax - random.randint(1, 12)
    kingdom["gold"] += actualTax
    
    happinessDecrease = random.randint(1, 8)
    kingdom["happiness"] -= happinessDecrease
    
    print("Tax Collected !!!")
    print(f"Tax Collected: {actualTax}")
    print(f"+{actualTax} gold\n-{happinessDecrease} happiness")
    
def buyFood():
    amount = int(input("Enter the amount of food you want to buy: "))
    costOfFood = amount * 2
    print("Buying food !!!")
    kingdom["gold"] -= costOfFood
    kingdom["food"] += amount
    print("Food bought !!!")
    print(f"+{amount} food\n-{costOfFood} gold")

def trainSoldiers():
    soldiers = int(input("Enter the number of the people you want to train: "))
    costOfFood = soldiers * 2
    goldExpense = soldiers * 10
    print("Training People !!!")
    kingdom["gold"] -= goldExpense
    kingdom["food"] -= costOfFood
    kingdom["population"] -= soldiers
    kingdom["army"] += soldiers
    print("Food bought !!!")
    print(f"+{soldiers} army\n-{costOfFood} food\n-{goldExpense} gold\n-{soldiers} population")

def expandTerritory():
    print("Expanding territory !!!")
    
menu()