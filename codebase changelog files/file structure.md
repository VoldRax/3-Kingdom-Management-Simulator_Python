# Kingdom Management Simulator - V1 Software Design Document

> This is Part 1 of a living design document.

## Goals
- Learn clean OOP
- Avoid global state
- Modular architecture

## Folder Structure

```
kingdom_simulator/
│
├── main.py
├── game.py
├── models/
│   ├── kingdom.py
│   ├── economy.py
│   ├── population.py
│   ├── army.py
│   ├── resources.py
│   └── building.py
├── services/
│   ├── economy_service.py
│   ├── army_service.py
│   ├── event_service.py
│   ├── save_service.py
│   └── report_service.py
├── ui/
│   └── menu.py
├── data/
│   └── saves/
└── tests/
```

## Class Responsibilities

### Kingdom
Owns:
- Economy
- Population
- Army
- Resources
- Buildings

Methods:
- next_turn()
- summary()

### Economy
Data:
- gold
- tax_rate
- trade_income
- expenses

Methods:
- add_gold()
- spend_gold()
- can_afford()

### Population
Data:
- total
- happiness
- workers
- soldiers

Methods:
- grow()
- decrease()
- change_happiness()

### Army
Data:
- infantry
- archers
- morale

Methods:
- recruit()
- dismiss()
- power()

### Resources
Data:
- food
- wood
- stone
- iron

Methods:
- add()
- remove()
- has()

## Services

EconomyService
- collect_taxes(kingdom)
- calculate_income(kingdom)

ArmyService
- recruit(kingdom,...)

SaveService
- save(kingdom)
- load()

ReportService
- kingdom_report()

## Main Flow

main.py
→ create Kingdom
→ show menu
→ call services
→ end turn
→ save

---
More chapters will be appended in future versions.
