# 🏰 Kingdom Management Simulator

A turn-based command-line strategy game written in Python where you rule a kingdom, manage resources, survive random events, and attempt to build a prosperous empire.

---

## 📖 About

Kingdom Management Simulator is a Python CLI project created to practice programming fundamentals while building a complete simulation game.

As the ruler, your objective is to grow your kingdom by making strategic decisions every turn. Every action affects your kingdom's economy, military, food supply, and population. Random events can either help your kingdom flourish or push it toward collapse.

---

## ✨ Features

* 💰 Collect Taxes
* 🌾 Buy Food
* ⚔️ Train Soldiers
* 🗺️ Expand Territory
* 📊 View Kingdom Report
* 🎲 Random Events
* 💾 Save Game
* 📂 Load Game
* 🔄 Turn-Based Gameplay
* 🏆 Win/Lose Conditions
* ✅ Resource Validation
* 🧹 Clean Modular Code Structure

---

## 🏛️ Kingdom Resources

Your kingdom is managed using the following resources:

| Resource   | Description                                        |
| ---------- | -------------------------------------------------- |
| Gold       | Used to buy food and train soldiers                |
| Food       | Required to feed the population each turn          |
| Population | Citizens available for taxes and military          |
| Army       | Determines military strength and expansion success |
| Happiness  | Represents public satisfaction                     |

---

## 🎮 Gameplay

Each turn you may choose one action:

1. Collect Taxes
2. Buy Food
3. Train Soldiers
4. Expand Territory
5. View Kingdom Report
6. End Turn
7. Save Game
8. Load Game
9. Exit

After every turn:

* Food is consumed by the population.
* The game checks victory and defeat conditions.
* Random events occur after a random number of turns.

---

## 🎲 Random Events

Random events include:

* ☠️ Plague
* 🏴 Bandit Attack
* ⛏️ Gold Mine Discovery
* 🎉 Festival
* 🌵 Drought

These events can either benefit or damage your kingdom.

---

## 🏆 Victory Conditions

Win the game by achieving:

* Population ≥ 1000
* Army ≥ 200
* Gold ≥ 10000
* Happiness ≥ 70
* Food ≥ 2500

---

## 💀 Defeat Conditions

You lose if your kingdom collapses due to extremely low resources.

---

## 📁 Project Structure

```text
Kingdom Management Simulator/
│
├── main.py             # Entry point
├── menu.py             # Main game loop
├── actions.py          # Player actions
├── events.py           # Random events
├── reports.py          # Reports and win/lose checks
├── save.py             # Save and load system
├── state.py            # Shared game state
├── validations.py      # Input and resource validation
├── utils.py            # Utility functions
├── constants.py        # Constants and menu text
├── README.md
└── main.json           # Example save file
```

---

## 🛠️ Technologies Used

* Python 3
* JSON
* Random module
* Modular programming
* Dictionaries
* Functions
* Exception handling

---

## 📚 Concepts Practiced

This project helped reinforce:

* Modular Programming
* State Management
* Dictionaries
* Functions
* Input Validation
* File Handling
* JSON Serialization
* Exception Handling
* Randomized Simulations
* Game Loops
* Resource Management

---

## 🚀 Future Improvements

Planned features include:

* Diplomacy System
* Multiple Kingdoms
* Technology Tree
* Trade System
* Difficulty Levels
* Quests
* AI Kingdoms
* Buildings
* Economy Simulation
* Weather System
* Achievement System
* Colored Terminal UI
* Sound Effects
* Database Saves

---

## ▶️ Running the Project

Clone the repository:

```bash
git clone <https://github.com/VoldRax/3-Kingdom-Management-Simulator_Python>
```

Navigate into the project:

```bash
cd "Kingdom Management Simulator"
```

Run:

```bash
python main.py
```

---

## 👨‍💻 Author

Created by **VoldRax** as part of a Python learning journey focused on building increasingly complex command-line applications.

---

## 📄 License

This project is intended for educational purposes and personal learning.