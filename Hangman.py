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