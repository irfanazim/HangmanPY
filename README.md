# Answer or Hang

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Gameplay](#gameplay)
- [Leaderboard](#leaderboard)
- [Saving and Loading](#saving-and-loading)
- [Contributing](#contributing)
- [License](#license)

## Introduction
A text-based Hangman game designed for the course **CSP1114: Problem Solving and Program Design**. This game allows players to guess words or phrases from a variety of categories, with each incorrect guess bringing them closer to a "hanged" stick figure.

## Features
- **Multiple Categories:** Choose from Science, History, and Geography questions.
- **Dynamic Gameplay:** Randomly shuffled questions for each category.
- **Save and Load:** Save your game progress and load it later.
- **Leaderboard:** Track your scores and compete with others.
- **User-Friendly Interface:** Easy navigation with clear instructions.
- **Platform Compatibility:** Works on Windows, macOS, and Linux.

## Installation
To play **Hangman.py**, you need Python installed on your system. Follow these steps to set up the game:

1. **Install Python:** Ensure you have Python 3.x installed. You can download it from [python.org](https://www.python.org/).
2. **Clone the Repository:** Clone this repository to your local machine.
   ```bash
   git clone https://github.com/your-repo/hangman.git
   cd hangman
   ```
3. **Install Dependencies:** The game requires the `tabulate` library for displaying tables. You can install it using pip:
   ```bash
   pip install tabulate
   ```
4. **Run the Game:** Execute the game script.
   ```bash
   python Hangman.py
   ```

## Usage
Upon running the game, you will be presented with the main menu. Here are the available options:

- **Start New Game:** Begin a new game by selecting a category.
- **Load Game:** Load a previously saved game.
- **Show Leaderboard:** View the leaderboard with the highest scores.
- **Quit:** Exit the game.

## Gameplay
1. **Choose a Category:** Select a category (Science, History, or Geography) to start.
2. **Guess Letters or Words:** You will be presented with a question and a masked answer. Guess letters or the full answer.
3. **Lives:** You have 6 lives. Each incorrect guess reduces your lives.
4. **Winning:** Correctly guess the answer to earn points and move to the next question.

## Leaderboard
The leaderboard tracks the highest scores of all players. You can view it from the main menu. Scores are saved in a JSON file (`leaderboard.json`).

## Saving and Loading
- **Save Game:** Type `save` during gameplay to save your progress.
- **Load Game:** Select `Load Game` from the main menu to load a saved game.

## Contributing
Contributions are welcome. Feel free to open issues or submit pull requests. Here are some ways you can contribute:

- Add more categories and questions.
- Improve the user interface.
- Optimize the code for better performance.

## License
This project is licensed under the **MIT License**. See the `LICENSE` file for details.


