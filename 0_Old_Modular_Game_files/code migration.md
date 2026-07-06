# Kingdom Management Simulator - Codebase Structure Guide

See sections below.

## Recommended Structure

``` text
KingdomManagement/
├── main.py
├── game.py
├── state.py
├── actions.py
├── events.py
├── reports.py
├── save.py
├── utils.py
├── validation.py
├── constants.py
├── saves/
└── README.md
```

## File Responsibilities

### main.py

-   Starts the game.
-   Imports and calls `menu()`.

### game.py

-   Main menu loop.
-   Handles turns.
-   Calls action, event, save, and report functions.

### state.py

-   Stores the `kingdom` dictionary.
-   Later: turn, season, difficulty.

### constants.py

-   Banner
-   Menu text
-   Default kingdom values

### utils.py

-   clearConsole()
-   showBanner()
-   displayKingdomStats()

### validation.py

-   numericInputValidation()
-   resourceCheck()

### actions.py

-   collectTaxes()
-   buyFood()
-   trainSoldiers()
-   expandTerritory()
-   consumeFood()

### events.py

-   trigger_event()
-   plague()
-   bandits()
-   drought()
-   festival()
-   gold_mine()

### reports.py

-   kingdomReport()
-   checkCurrentState()

### save.py

-   saveData()
-   loadData()

## Refactoring Order

1.  constants.py
2.  state.py
3.  utils.py
4.  validation.py
5.  actions.py
6.  events.py
7.  save.py
8.  reports.py
9.  game.py
10. main.py

## Example Imports

``` python
from state import kingdom
from actions import collectTaxes
from events import trigger_event
from save import saveData, loadData
from reports import kingdomReport
```

## Future

Replace the global `kingdom` dictionary with a `Game` class to
centralize all game state.
