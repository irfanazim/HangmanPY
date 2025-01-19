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
