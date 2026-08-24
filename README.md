# Multi-Mode Number Guessing Game

A robust, terminal-based number guessing game written in Python. It features dynamic difficulty levels, parity hints, persistent leaderboards, and support for both single-player and head-to-head competitive modes.

## 🚀 Features
* **🤖 Computer Mode**: Play against the AI! Guess the secret number within a limited number of attempts based on your chosen difficulty level.
* **👥 2-Player Battle Mode**: Challenge a friend! Players take turns setting secret numbers for each other and compete across multiple rounds for the highest total score.
* **💡 Dynamic Hints**: The game helps you out by revealing whether the target number is odd or even before you start guessing.
* **🎯 Scoring & Multipliers**: Earn points based on how quickly you guess the number, multiplied by your difficulty setting.
* **🏆 Persistent Leaderboard**: Automatically tracks and updates player scores across gaming sessions.

## 🛠️ Built With
* **Python 3** - Core game logic, state management, and modular functions.
* Custom `utils` module - Handles helper logic like difficulty configurations, secret hiding, and file-based leaderboards.

## ⚙️ How to Run
To play the game on your local machine, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Bonita-20/Number_Guessing_Game/
   ```
2. **Navigate to the project folder:**
   ```bash
   cd Number_Guessing_Game
   ```
3. **Run the game:**
   ```bash
   python game.py
   ```
   *(Note: Ensure you keep `utils.py` in the same directory as your main script, as the program relies heavily on it to run!)*

## 🧠 Code Architecture & What I Learned
Building this project helped me master advanced beginner concepts in Python:
* **Modular Code Structure**: Separating primary game loops from execution utilities (`import utils`) to keep code highly maintainable.
* **Complex State Loops**: Implementing nested `while True` loops to handle multi-round game sessions seamlessly for both solo and multiplayer modes.
* **Data Flow**: Passing scores, variables, and player names across distinct structural functions while tracking aggregate totals.

## 📄 License
This project is open-source and available under the [MIT License](LICENSE).
