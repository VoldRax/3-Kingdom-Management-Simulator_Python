def createGame():
    return {
        "turn": 0,
        "next_event_turn": 5,
        "kingdom": {
            "gold": 1000,
            "food": 500,
            "population": 100,
            "army": 25,
            "happiness": 75,
        },
    }

game = createGame()