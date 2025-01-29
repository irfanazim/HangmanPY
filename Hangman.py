# *************************************************************************
# Program: Hangman.py
# Course: CSP1114 PROBLEM SOLVING AND PROGRAM DESIGN
# Lecture / Lab Section: TC2L / TL6L
# Trimester: 2430
# Names: MEMBER_NAME_1 | MEMBER_NAME_2 | MEMBER_NAME_3 | MEMBER_NAME_4
# IDs: MEMBER_ID_1 | MEMBER_ID_2 | MEMBER_ID_3 | MEMBER_ID_3
# Emails: MEMBER_EMAIL_1 | MEMBER_EMAIL_2 | MEMBER_EMAIL_3 | MEMBER_EMAIL_3
# *************************************************************************

import json
import random
import os
import platform
import time

# ANSI color codes
GREEN = "\033[32m"
RESET = "\033[0m"
BOLD = "\033[1m"

# Clear screen function for a clean display
def clear_screen():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

# List of hangman stages (from no body to a fully drawn hangman)
hangman_stages = [
    fr"""{GREEN}
    ╔════════════════╗
    ║  +---+         ║
    ║      |         ║
    ║      |         ║
    ║      |         ║
    ║     ===        ║
    ╚════════════════╝{RESET}
    """,
    fr"""{GREEN}
    ╔════════════════╗
    ║  +---+         ║
    ║  O   |         ║
    ║      |         ║
    ║      |         ║
    ║     ===        ║
    ╚════════════════╝{RESET}
    """,
    fr"""{GREEN}
    ╔════════════════╗
    ║  +---+         ║
    ║  O   |         ║
    ║  |   |         ║
    ║      |         ║
    ║     ===        ║
    ╚════════════════╝{RESET}
    """,
    fr"""{GREEN}
    ╔════════════════╗
    ║  +---+         ║
    ║  O   |         ║
    ║ /|   |         ║
    ║      |         ║
    ║     ===        ║
    ╚════════════════╝{RESET}
    """,
    fr"""{GREEN}
    ╔════════════════╗
    ║  +---+         ║
    ║  O   |         ║
    ║ /|\  |         ║
    ║      |         ║
    ║     ===        ║
    ╚════════════════╝{RESET}
    """,
    fr"""{GREEN}
    ╔════════════════╗
    ║  +---+         ║
    ║  O   |         ║
    ║ /|\  |         ║
    ║ /    |         ║
    ║     ===        ║
    ╚════════════════╝{RESET}
    """,
    fr"""{GREEN}
    ╔════════════════╗
    ║  +---+         ║
    ║  O   |         ║
    ║ /|\  |         ║
    ║ / \  |         ║
    ║     ===        ║
    ╚════════════════╝{RESET}
    """
]

# Art for the main menu, printed at the start
main_menu_art = fr"""{GREEN}
▐▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▌
▐ _   _                                         ▌
▐| | | |                                        ▌
▐| |_| | __ _ _ __   __ _ _ __ ___   __ _ _ __  ▌
▐|  _  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ ▌
▐| | | | (_| | | | | (_| | | | | | | (_| | | | |▌
▐\_| |_/\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|▌
▐                    __/ |                      ▌
▐                   |___/                       ▌
▐▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▌
{RESET}
"""

# Dictionary holding the questions for different categories
questions = {
    "Science": [
        ("What planet is known as the Red Planet?", "Mars"),
        ("What gas do plants breathe in that humans and animals breathe out?", "CarbonDioxide"),
        ("What is the chemical symbol for water?", "H2O")
    ],
    "History": [
        ("Who was the first President of the United States?", "George Washington"),
        ("In what year did World War II end?", "1945"),
        ("The Great Fire of London occurred in which year?", "1666")
    ],
    "Geography": [
        ("What is the capital of France?", "Paris"),
        ("Which continent is the Sahara Desert located on?", "Africa"),
        ("Mount Everest is part of which mountain range?", "Himalayas")
    ]
}

# Class to handle the game state
class GameState:
    def __init__(self):
        self.score = 0  # Starting score
        self.leaderboard_file = "leaderboard.json"  # File to store the leaderboard
        self.save_directory = "saved_games"  # Directory to store saved games
        self.current_category = ""  # Current category of questions
        self.question_index = 0  # Index to track the current question
        self.username = ""  # Username of the player
        self.lives = 6  # Number of lives the player has
        
        # Create the directory for saved games if it doesn't exist
        if not os.path.exists(self.save_directory):
            os.makedirs(self.save_directory)
    
    def start_new_game(self):
        #I nitializes the game state for a new game.
        self.score = 0  # Set initial score
        self.question_index = 0  # Set initial question index
        self.lives = 6  # Set initial number of lives
        self.choose_category()  # Prompt the user to choose a category
        self.play_game()  # Start playing the game

    def choose_category(self):
        # Displays available categories for the user to choose from.
        while True:  # Loop until a valid choice is made
            print("\nChoose a category:")
            categories = list(questions.keys())  # Retrieve the available categories
            for i, category in enumerate(categories):
                print(f"{i + 1}. {category}")  # Display category choices

            try:
                choice = int(input("Enter the number of your chosen category: ")) - 1  # User selects a category
                if 0 <= choice < len(categories):  # Check for valid input
                    self.current_category = categories[choice]  # Set the chosen category
                    print(f"You chose {self.current_category}. Let's start!")  # Confirm category selection
                    break  # Exit the loop if a valid choice is made
                else:
                    print("Invalid choice. Please enter a valid number.")
            except ValueError:
                print("Invalid input. Please enter a number.")  # If input is not a valid number
    
    def switch_category(self):
        # Allows the player to switch to a different category during the game.
        while True:  # Loop until a valid choice is made
            print("\nAvailable categories:")
            categories = list(questions.keys())  # Retrieve the available categories
            for i, category in enumerate(categories):
                print(f"{i + 1}. {category}")  # Display category choices

            try:
                choice = int(input("Enter the number of your chosen category: ")) - 1  # User selects a category
                if 0 <= choice < len(categories):  # Check for valid input
                    self.current_category = categories[choice]  # Set the chosen category
                    self.question_index = 0  # Reset the question index
                    print(f"You chose {self.current_category}. Let's start!")  # Confirm category selection
                    self.play_game()  # Start the game with the new category
                    break  # Exit the loop if a valid choice is made
                else:
                    print("Invalid choice. Please enter a valid number.")
            except ValueError:
                print("Invalid input. Please enter a number.")  # If input is not a valid number