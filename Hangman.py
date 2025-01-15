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

# ASCII Art for the Hangman Stages with green color and border
hangman_stages = [
    f"""{GREEN}
    ╔════════════════╗
    ║  +---+         ║
    ║      |         ║
    ║      |         ║
    ║      |         ║
    ║     ===        ║
    ╚════════════════╝{RESET}
    """,
    f"""{GREEN}
    ╔════════════════╗
    ║  +---+         ║
    ║  O   |         ║
    ║      |         ║
    ║      |         ║
    ║     ===        ║
    ╚════════════════╝{RESET}
    """,
    f"""{GREEN}
    ╔════════════════╗
    ║  +---+         ║
    ║  O   |         ║
    ║  |   |         ║
    ║      |         ║
    ║     ===        ║
    ╚════════════════╝{RESET}
    """,
    f"""{GREEN}
    ╔════════════════╗
    ║  +---+         ║
    ║  O   |         ║
    ║ /|   |         ║
    ║      |         ║
    ║     ===        ║
    ╚════════════════╝{RESET}
    """,
    f"""{GREEN}
    ╔════════════════╗
    ║  +---+         ║
    ║  O   |         ║
    ║ /|\  |         ║
    ║      |         ║
    ║     ===        ║
    ╚════════════════╝{RESET}
    """,
    f"""{GREEN}
    ╔════════════════╗
    ║  +---+         ║
    ║  O   |         ║
    ║ /|\  |         ║
    ║ /    |         ║
    ║     ===        ║
    ╚════════════════╝{RESET}
    """,
    f"""{GREEN}
    ╔════════════════╗
    ║  +---+         ║
    ║  O   |         ║
    ║ /|\  |         ║
    ║ / \  |         ║
    ║     ===        ║
    ╚════════════════╝{RESET}
    """
]
