
import random
from state import game
from validations import numericInputValidation, checkResources

def collectTaxes():
    taxRate = random.randint(2, 5)
    estimatedTax = game["kingdom"]["population"] * taxRate

    print(f"Population: {game["kingdom"]['population']}\nTax rate: {taxRate}")
    print(f"Tax to be collected: {estimatedTax}")

    print("Collecting taxes !!!")

    actualTax = estimatedTax - random.randint(1, 12)
    game["kingdom"]["gold"] += actualTax

    happinessDecrease = random.randint(1, 8)
    game["kingdom"]["happiness"] -= happinessDecrease


    print("Tax Collected !!!")
    print(f"Tax Collected: {actualTax}")
    print(f"+{actualTax} gold\n-{happinessDecrease} happiness")


def buyFood():

    amount = numericInputValidation(
        "Enter the amount of food you want to buy: "
    )

    costOfFood = amount * 2

    if not checkResources(gold=costOfFood):
        return

    print("Buying food !!!")

    game["kingdom"]["gold"] -= costOfFood
    game["kingdom"]["food"] += amount

    print("Food bought !!!")
    print(f"+{amount} food")
    print(f"-{costOfFood} gold")

def trainSoldiers():


    soldiers = numericInputValidation(
        "Enter the number of people to train: "
    )

    foodExpense = soldiers * 2
    goldExpense = soldiers * 10

    if not checkResources(
        gold=goldExpense,
        food=foodExpense,
        population=soldiers,
    ):
        return

    print("Training soldiers...")

    game["kingdom"]["gold"] -= goldExpense
    game["kingdom"]["food"] -= foodExpense
    game["kingdom"]["population"] -= soldiers
    game["kingdom"]["army"] += soldiers

    print("Training complete!")
    print(f"+{soldiers} army")
    print(f"-{foodExpense} food")
    print(f"-{goldExpense} gold")
    print(f"-{soldiers} population")

def expandTerritory():

    armyRequired = 20

    if not checkResources(army=armyRequired):
        return
    print("Expanding territory !!!")
    successRate = random.randint(1, 100)
    successRate += game["kingdom"]["army"] // 10
    if successRate > 70:
        goldIncrease = random.randint(100, 500)
        foodIncrease = random.randint(50, 250)
        populationIncrease = random.randint(10, 50)
        happinessIncrease = random.randint(10, 30)
        game["kingdom"]["gold"] += goldIncrease
        game["kingdom"]["food"] += foodIncrease
        game["kingdom"]["population"] += populationIncrease
        game["kingdom"]["happiness"] += happinessIncrease
        print("Territory Expanded !!!")
        print(
            f"+{goldIncrease} gold\n+{foodIncrease} food\n+{populationIncrease} population\n+{happinessIncrease} happiness\n"
        )
        return
    elif successRate > 30:
        goldIncrease = random.randint(50, 200)
        foodIncrease = random.randint(25, 125)
        populationIncrease = random.randint(5, 20)
        happinessIncrease = random.randint(4, 12)
        game["kingdom"]["gold"] += goldIncrease
        game["kingdom"]["food"] += foodIncrease
        game["kingdom"]["population"] += populationIncrease
        game["kingdom"]["happiness"] += happinessIncrease
        print("A small village added !!!")
        print(
            f"+{goldIncrease} gold\n+{foodIncrease} food\n+{populationIncrease} population\n+{happinessIncrease} happiness\n"
        )
        return
    else:
        goldDecrease = random.randint(50, 200)
        armyDecrease = random.randint(5, 20)
        happinessDecrease = random.randint(3, 15)
        game["kingdom"]["gold"] -= goldDecrease
        game["kingdom"]["army"] -= armyDecrease
        game["kingdom"]["happiness"] -= happinessDecrease
        print("Expansion Failed !!!")
        print(
            f"-{goldDecrease} gold\n-{armyDecrease} army\n-{happinessDecrease} happiness\n"
        )
        checkResources()
        return

def consumeFood():
    food_consumed = game["kingdom"]["population"] // 10
    game["kingdom"]["food"] -= food_consumed
    return