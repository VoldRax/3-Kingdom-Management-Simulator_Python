from state import game

def numericInputValidation(prompt):
    while True:
        try:
            value = int(input(prompt))

            if value <= 0:
                print("Enter a number greater than 0.")
                continue

            return value

        except ValueError:
            print("Please enter a valid number.")

def checkResources(gold=0, food=0, population=0, army=0):

    kingdom = game["kingdom"]

    if kingdom["gold"] < gold:
        print("Not enough gold!")
        return False

    if kingdom["food"] < food:
        print("Not enough food!")
        return False

    if kingdom["population"] < population:
        print("Not enough population!")
        return False

    if kingdom["army"] < army:
        print("Not enough army!")
        return False

    return True
