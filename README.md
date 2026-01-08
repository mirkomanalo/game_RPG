# Python RPG Battle Simulator

A text-based, turn-based RPG game written in Python. 
The project implements a "Survival Mode" where the hero fights an endless stream of 
procedurally generated monsters, managing resources (HP and Potions) to survive as long as possible.

## Learning Objectives
This project was built to practice core **Object-Oriented Programming (OOP)** concepts:
* **Classes & Objects**: Modeling entities like Heroes and Monsters.
* **Inheritance**: Creating a modular `Character` base class extended by `Hero` and `Monster`.
* **Polymorphism**: Overriding the `attack()` method to implement different behaviors (e.g., Critical Hits for monsters).
* **Type Hints**: Using Python's static typing features for robust code.
* **Game Logic**: Implementing nested loops for the game state and battle mechanics.

## Features
* **Survival System**: Infinite monster generation with randomized stats.
* **Loot Mechanism**: Monsters have a chance to drop potions upon death.
* **Turn-Based Combat**: Strategic choices between attacking and healing.
* **Input Validation**: robust handling of user commands.

## How to Run
Requirement: Python 3

1. Clone the repository:
   ```bash
   git clone https://github.com/mirkomanalo/game_RPG.git
   
