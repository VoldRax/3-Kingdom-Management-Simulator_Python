# Kingdom Management Simulator

import json
import os
import random
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

kingdom = {"gold": 1000, "food": 500, "population": 100, "army": 25, "happiness": 75}


def clearConsole():
    os.system("cls")


def showBanner():
    print(banner)
    return


def displayKingdomStats():
    for asset, assetQuantity in kingdom.items():
        print(f"{asset}: {assetQuantity}")


def menu():

    turn = 0
    nextEventTurn = random.randint(3, 6)

    while True:

        checkCurrentState()
    
        if turn >= nextEventTurn:
            trigger_event()
            nextEventTurn = turn + random.randint(3, 10)
            input("\nPress Enter...")
            continue

        else:
            clearConsole()
            showBanner()
            displayKingdomStats()
            print(menuOptions)

            userChoice = input("Enter your choice:\n> ")

            match userChoice:
                case "1":
                    clearConsole()
                    collectTaxes()
                    turn += 1
                    consumeFood()
                    input("\nPress Enter...")

                case "2":
                    clearConsole()
                    buyFood()
                    turn += 1
                    consumeFood()
                    input("\nPress Enter...")

                case "3":
                    clearConsole()
                    trainSoldiers()
                    turn += 1
                    consumeFood()
                    input("\nPress Enter...")

                case "4":
                    clearConsole()
                    expandTerritory()
                    turn += 1
                    consumeFood()
                    input("\nPress Enter...")

                case "5":
                    clearConsole()
                    kingdomReport()
                    turn += 1
                    consumeFood()
                    input("\nPress Enter...")

                case "6":
                    clearConsole()
                    turn += 1
                    consumeFood()
                    input("\nPress Enter...")

                case "7":
                    clearConsole()
                    turn += 1
                    consumeFood()
                    input("\nPress Enter...")

                case "8":
                    clearConsole()
                    turn += 1
                    consumeFood()
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

    print(f"Population: {kingdom['population']}\nTax rate: {taxRate}")
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
    print(
        f"+{soldiers} army\n-{costOfFood} food\n-{goldExpense} gold\n-{soldiers} population"
    )


def expandTerritory():

    print("Expanding territory !!!")
    successRate = random.randint(1, 100)
    successRate += kingdom["army"] // 10
    if successRate > 70:
        goldIncrease = random.randint(100, 500)
        foodIncrease = random.randint(50, 250)
        populationIncrease = random.randint(10, 50)
        happinessIncrease = random.randint(10, 30)
        kingdom["gold"] += goldIncrease
        kingdom["food"] += foodIncrease
        kingdom["population"] += populationIncrease
        kingdom["happiness"] += happinessIncrease
        print("Territory Expanded !!!")
        print(
            f"+{goldIncrease} gold\n+{foodIncrease} food\n+{populationIncrease} population\n+{happinessIncrease} happiness\n"
        )
    elif successRate > 30:
        goldIncrease = random.randint(50, 200)
        foodIncrease = random.randint(25, 125)
        populationIncrease = random.randint(5, 20)
        happinessIncrease = random.randint(4, 12)
        kingdom["gold"] += goldIncrease
        kingdom["food"] += foodIncrease
        kingdom["population"] += populationIncrease
        kingdom["happiness"] += happinessIncrease
        print("Territory Expanded !!!")
        print(
            f"+{goldIncrease} gold\n+{foodIncrease} food\n+{populationIncrease} population\n+{happinessIncrease} happiness\n"
        )
    else:
        goldDecrease = random.randint(50, 200)
        armyDecrease = random.randint(5, 20)
        happinessDecrease = random.randint(3, 15)
        kingdom["gold"] -= goldDecrease
        kingdom["population"] -= armyDecrease
        kingdom["happiness"] -= happinessDecrease
        print("Territory Expanded !!!")
        print(
            f"-{goldDecrease} gold\n-{armyDecrease} army\n-{happinessDecrease} happiness\n"
        )


def kingdomReport():
    print("Kingdom Report -->\n")

    for asset, assetQuantity in kingdom.items():
        print(f"{asset}: {assetQuantity}")

    print("\nTreasury: Healthy" if kingdom["gold"] > 1000 else "\nTreasury: Unhealthy")
    print(
        "\nMilitary Strength: Stable"
        if kingdom["army"] > 75
        else "\nMilitary Strength: Unstable"
    )
    print(
        "\nFood Situation: Excellent"
        if kingdom["food"] > 500
        else "\nFood Situation: Poor"
    )

def consumeFood():
    food_consumed = kingdom["population"] // 10
    kingdom["food"] -= food_consumed
    return

def trigger_event():

    event = random.choice(["plague", "bandits", "gold_mine", "festival", "drought"])

    if event == "plague":
        clearConsole()
        showBanner()
        kingdom["population"] -= 20
        print("Event: Plague\nTreating People !!!")
        print("-20 population")
        return

    elif event == "bandits":
        clearConsole()
        showBanner()
        kingdom["gold"] -= 100
        print("Event: Bandit Attack\nResisting Bandits")
        print("-100 gold")
        return
    elif event == "gold_mine":
        clearConsole()
        showBanner()
        kingdom["gold"] += 500
        print("Event: Gold Mine discovered\nDigging mines")
        print("+gold 500")
        return
    elif event == "festival":
        clearConsole()
        showBanner()
        kingdom["happiness"] += 20
        print("Event: Festival\nPeople are happy")
        print("+20 happiness")
        return
    elif event == "drought":
        clearConsole()
        showBanner()
        kingdom["food"] -= 200
        print("Event: Drought\nProviding food to the people !!!")
        print("-200 food")
        return

def playAgain():
    playChoice = input("Wanna play again (y/n)??\n>")
    if playChoice == 'y' or playAgain == "yes":
        global kingdom
        kingdom == {"gold": 1000, "food": 500, "population": 100, "army": 25, "happiness": 75}
        return
    else:
        print("Thank You !!!")
        exit()

def checkCurrentState():
    if kingdom["population"] >= 1000 and kingdom["army"] >= 200 and kingdom["gold"] >= 10000 and kingdom["happiness"] >= 70 and kingdom["food"] >= 2500:
        print("You Won !!!")
        playAgain()
        return
        
    elif kingdom["population"] <= 10 and kingdom["army"] <= 5 and kingdom["gold"] <= 50 and kingdom["happiness"] <= 5 and kingdom["food"] <= 200:
        print("You lose !!!")
        playAgain()
        return


menu()
