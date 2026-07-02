# 🏰 Kingdom Management Simulator
# Version 2 Development Roadmap

> **Mission:** Transform the current Kingdom Management Simulator (V1) into a realistic kingdom simulation with clean architecture and deeper gameplay.

---

# 📌 Current Version (V1)

Current Features

- Modular project structure
- Turn based gameplay
- Collect Taxes
- Buy Food
- Train Soldiers
- Expand Territory
- Random Events
- Kingdom Reports
- Save / Load using JSON
- Kingdom statistics

Current Goal:

> Make the game deeper—not bigger.

---

# 🎯 V2 Goals

Instead of adding random features, every system should interact with every other system.

Example:

Population → Produces Food

Food → Keeps Population Alive

Population → Pays Taxes

Taxes → Increase Gold

Gold → Builds Farms

Farms → Produce More Food

Everything should feel connected.

---

# 🗺️ Development Order

Complete each phase before moving to the next.

```
Phase 1
↓

Population System

↓

Phase 2
↓

Building System

↓

Phase 3
↓

Resource System

↓

Phase 4
↓

Economy

↓

Phase 5
↓

Military

↓

Phase 6
↓

Weather

↓

Phase 7
↓

Events

↓

Phase 8
↓

Reports

↓

Phase 9
↓

Balancing
```

---

# Phase 1 — Population System

## New Attributes

```python
Population

Workers

Farmers

Merchants

Soldiers

Scholars

Children

Elderly

Happiness

Health
```

---

## Features

Population grows every turn.

Birth Rate

Death Rate

Disease

Starvation

Migration

Employment

---

## Example Formula

```
Population Growth =
Births
-
Deaths
+
Migration
```

---

## Happiness

Range

```
0–100
```

Affected by

- Food
- Taxes
- War
- Festivals
- Housing
- Health

Consequences

Low Happiness

- Less productivity
- Lower tax income
- Possible rebellion

High Happiness

- Faster population growth
- Better production
- Higher tax income

---

# Phase 2 — Building System

Create a Building class.

Every building should have

```python
Name

Cost

Maintenance

Level

Workers Required

Bonuses
```

---

## Buildings

### Farm

Produces food.

---

### Mine

Produces stone and iron.

---

### Lumber Mill

Produces wood.

---

### Marketplace

Increases trade income.

---

### Barracks

Allows training soldiers.

---

### Blacksmith

Improves military strength.

---

### Hospital

Improves health.

---

### School

Produces scholars.

---

### Castle

Improves defense.

---

## Upgrade System

Every building has

```
Level 1

↓

Level 2

↓

Level 3

↓

Level 4

↓

Level 5
```

Each level

- Costs more
- Gives larger bonuses

---

# Phase 3 — Resource System

Instead of only Gold and Food

Add

```
Gold

Food

Wood

Stone

Iron

Coal

Horses
```

---

## Production

Workers gather resources.

Example

```
Wood

↓

Lumber Mill

↓

Workers

↓

Wood Produced
```

---

## Consumption

Buildings require maintenance.

Army consumes food.

Construction consumes resources.

---

# Phase 4 — Economy

Income Sources

- Taxes
- Trade
- Mining
- Markets

Expenses

- Army salaries
- Building maintenance
- Food imports
- Festivals

---

## Tax Rate

Player chooses

```
Low

Medium

High
```

Effects

Low

+ Happiness

- Gold

High

+ Gold

- Happiness

---

## Inflation (Optional)

Too much gold

↓

Prices increase.

---

# Phase 5 — Military

Replace

```
Soldiers
```

With

```
Infantry

Archers

Cavalry

Knights
```

Each unit has

```python
Attack

Defense

Training Cost

Food Consumption

Maintenance

Morale
```

---

## Army Management

Recruit

Train

Disband

Upgrade

Inspect Army

---

## Battle System

Enemy has

```
Army Size

Morale

Terrain

Weather
```

Battle Formula

```
Power =
Attack
+
Defense
+
Morale
+
Random Bonus
```

Possible Results

Victory

Defeat

Heavy Losses

Pyrrhic Victory

---

# Phase 6 — Weather

Possible Weather

```
Sunny

Rain

Storm

Snow

Drought
```

Effects

Sunny

+ Food Production

Rain

+ Crops

Storm

- Trade

Snow

- Army Movement

Drought

- Food Production

Weather changes every turn.

---

# Phase 7 — Random Events

Current events should become event objects.

Each event contains

```python
Name

Description

Probability

Effects
```

---

## Positive Events

Good Harvest

Merchant Caravan

Festival

Treasure Found

Scientific Discovery

---

## Negative Events

Bandits

Fire

Flood

Earthquake

Plague

Famine

---

## Rare Events

Dragon Attack

Meteor Strike

Ancient Ruins

Legendary Hero Arrives

---

# Phase 8 — Reports

Improve reports.

---

## Economy Report

Display

```
Income

Expenses

Net Profit

Taxes

Trade

Treasury
```

---

## Population Report

Display

```
Population

Workers

Farmers

Merchants

Soldiers

Children

Happiness

Health
```

---

## Military Report

Display

```
Army Size

Infantry

Archers

Cavalry

Knights

Morale
```

---

## Resource Report

Display

```
Gold

Food

Wood

Stone

Iron

Coal

Horses
```

---

# Phase 9 — Balancing

Adjust numbers until the game feels fair.

Questions

Can players become rich too quickly?

Can food become impossible to maintain?

Are taxes too powerful?

Does the army become overpowered?

Does population grow too quickly?

Balance before adding more features.

---

# Suggested Folder Structure

```
kingdom_simulator/

main.py

models/
    kingdom.py
    building.py
    citizen.py
    army.py
    event.py

services/
    economy.py
    population.py
    military.py
    building_service.py
    report_service.py
    event_service.py

data/
    config.json
    saves/

utils/
    logger.py
    helpers.py
    validators.py

tests/
```

---

# Optional Stretch Goals

- Technology Tree
- Diplomacy
- Multiple Kingdoms
- Trading System
- Quests
- Reputation
- Crime System
- AI Kingdoms
- Difficulty Levels
- Achievements

---

# Definition of Done (V2)

The project is considered Version 2 when it satisfies all of the following:

- Modular architecture
- Population simulation
- Building system
- Multiple resources
- Dynamic economy
- Army with different unit types
- Weather system
- Improved event system
- Detailed reports
- Save/Load support for every new feature
- Balanced gameplay
- Clean, readable code
- Type hints
- Docstrings
- Error handling
- Logging

---

# Skills Learned After V2

- Object-Oriented Programming
- Modular Architecture
- Data Modeling
- Game State Management
- Simulation Design
- JSON Persistence
- Python Packages
- Clean Code
- Software Engineering Principles

---

# Final Objective

At the end of V2, the game should no longer feel like a menu-driven resource tracker.

It should feel like a living kingdom where every decision has consequences. Population, economy, resources, military, weather, and events should influence one another to create an engaging simulation while maintaining a clean and maintainable codebase.