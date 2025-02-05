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
# To import 'tabulate', it has to be install first (Auto-install code for tabulate)
try:
    from tabulate import tabulate # If 'tabulate' is installed, this will succeed, and the script will use it.
except ImportError: # If 'tabulate' is missing, install it
    print("Installing 'tabulate' library...") # Notify the user that the 'tabulate' library is being installed.
    import subprocess
    import sys
    subprocess.check_call([sys.executable, "-m", "pip", "install", "tabulate"]) 
    from tabulate import tabulate 


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
╔╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╗
╟┼┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┼╢
╟┤    _                                               _   _                   ├╢
╟┤   / \   _ __  _____      _____ _ __    ___  _ __  | | | | __ _ _ __   __ _ ├╢
╟┤  / _ \ | '_ \/ __\ \ /\ / / _ \ '__|  / _ \| '__| | |_| |/ _` | '_ \ / _` |├╢
╟┤ / ___ \| | | \__ \\ V  V /  __/ |    | (_) | |    |  _  | (_| | | | | (_| |├╢
╟┤/_/   \_\_| |_|___/ \_/\_/ \___|_|     \___/|_|    |_| |_|\__,_|_| |_|\__, |├╢
╟┤                                                                      |___/ ├╢
╟┼┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┼╢
╚╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╝
{RESET}
"""

# Dictionary holding the questions for different categories
questions = {
    "Science": [
        ("What planet is known as the Red Planet?", "Mars"),
        ("What gas do plants breathe in that humans and animals breathe out?", "CarbonDioxide"),
        ("What is the chemical symbol for water?", "H2O"),
        ("What is the largest planet in our solar system?", "Jupiter"),
        ("What is the process by which plants make their own food called?", "Photosynthesis"),
        ("What is the chemical symbol for gold?", "Au")
    ],
    "History": [
        ("In what year did World War II end?", "1945"),
        ("In what year did Malaysia achieved independence?", "1957"),
        ("Which country occupied Malaysia during World War II?", "Japan"),

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

    def play_game(self):
        # Handles the core game loop, including asking questions, taking guesses, and handling game over conditions.
        while True: 
            category_questions = questions[self.current_category]  # Get the questions for the selected category
            random.shuffle(category_questions)  # Shuffle questions for randomness
            game_over = False  # Flag to check if the game is over

            # Loop through questions until the user runs out of questions or lives
            while self.question_index < len(category_questions):
                question, answer = category_questions[self.question_index]  # Get the current question and answer
                masked_answer = ['_' for _ in answer]  # Mask the answer for the user to guess
                guessed_letters = set()  # Set to track guessed letters

                # While the user still has lives and the answer is incomplete, keep guessing
                while self.lives > 0 and '_' in masked_answer:
                    print("\nQuestion:", question)  # Display the current question
                    print("Answer:", ' '.join(masked_answer))  # Display the partially guessed answer
                    print(f"Lives remaining: {self.lives}")  # Show the number of lives left
                    print(hangman_stages[6 - self.lives])  # Display the hangman stage based on remaining lives

                    # Prompt for a guess
                    guess = input("Guess a letter, the full answer, type 'save' to save and exit, or 'switch' to change category: ").strip()

                    # Handle special inputs: save, switch category
                    if guess.lower() == "save":
                        self.save_game_state()  # Save the current game state
                        return  # Exit to the main menu
                    if guess.lower() == "switch":
                        self.switch_category()  # Switch to a different category
                        return  # Exit to the category selection

                    # Handle guesses for a single letter
                    if len(guess) == 1:
                        if guess in guessed_letters:  # Check if the letter has already been guessed
                            print("You already guessed that letter.")
                            continue  # Skip the rest of the loop if the letter was already guessed
                        guessed_letters.add(guess)  # Add the letter to guessed letters
                        if guess.lower() in answer.lower():  # Check if the letter is in the answer
                            # Update masked_answer with the correct letter(s)
                            for i, letter in enumerate(answer):
                                if letter.lower() == guess.lower():
                                    masked_answer[i] = letter
                            print("Good guess!")
                        else:
                            self.lives -= 1  # Deduct a life for an incorrect guess
                            print("Wrong guess!")
                            
                    # Handle the case where the player guesses the full answer
                    elif guess.lower() == answer.lower():
                        masked_answer = list(answer)  # Reveal the full answer
                        print("Correct!")
                        break  # End the question
                    else:
                        self.lives -= 1  # Deduct a life for an incorrect answer
                        print("Wrong answer!")

                # Check if the player successfully guessed the answer
                if '_' not in masked_answer:
                    self.score += 10  # Award points for the correct answer
                    self.question_index += 1  # Move to the next question
                else:
                    print(f"Out of lives! The answer was '{answer}'.")  # Show the correct answer if out of lives
                    game_over = True  # Set the game over flag
                    break  # End the game loop

            if game_over:
                print("\nGame over! You ran out of lives.")
                break  # Exit the loop if game over

            # Display a message if the player completes the category
            print(f"\nCongratulations! You've completed the {self.current_category} category!")
            print(f"Your current score is {self.score}")
            
            # Offer options to continue or end the game
            while True:
                choice = input("\n1. Continue with new category\n2. End game\nChoice (1 or 2): ").strip()
                if choice == "1":
                    self.choose_category()  # Choose a new category to continue playing
                    self.question_index = 0  # Reset question index
                    break  # Continue to the next category
                elif choice == "2":
                    game_over = True  # Set game over flag
                    break  # Exit the game loop
                else:
                    print("Invalid choice. Enter 1 or 2.")  # If invalid input, prompt again
            
            if game_over:
                break  # Exit the game loop if game over

        print(f"\nGame over! Final score: {self.score}")  # Display final score
        self.save_game_state()  # Save the final game state
        self.update_leaderboard()  # Update the leaderboard
        input("Press Enter to return to main menu.")  # Wait for the user to return to the main menu

    # Function to save the current game state into a file 
    def save_game_state(self):
        save_path = os.path.join(self.save_directory, f"{self.username}_save.json") # Ensures that the folder and filename are combined correctly
        with open(save_path, 'w') as f: 
            json.dump({
                "username": self.username, 
                "score": self.score, 
                "current_category": self.current_category,
                "question_index": self.question_index, 
                "lives": self.lives
            }, f)
        print("Game saved successfully!")

        self.update_leaderboard()
        time.sleep(2)

    # Function to display all saved games to the player
    def display_saved_games(self):
        clear_screen()  # Clears the screen for a clean view
        # Get a list of files in the save directory that end with '_save.json'
        save_files = [f for f in os.listdir(self.save_directory) if f.endswith('_save.json')]
        
        if not save_files:
            print(f"{GREEN}No saved games found.{RESET}")
            input("\nPress Enter to return to main menu.")
            return []
        
        # Initialize table data and headers
        headers = ["#", "USERNAME", "CATEGORY"]
        table_data = []

        # Inserting data (_save.json files) into the table
        i = 1  # To keep track of the row number (starting from 1)
        for file in save_files:
            with open(os.path.join(self.save_directory, file), 'r') as f: # Open the save file in read mode
                data = json.load(f)
                username = data.get("username", "Unknown")
                category = data.get("current_category", "None")
                table_data.append([i, username, category])
                i += 1  # Increasing the row number by 1 

        # Print the table using tabulate
        print(f"{GREEN}")
        print(tabulate(table_data, headers=headers, tablefmt="fancy_grid"))
        print(f"{RESET}")
    
        # Get the user's choice for which save file to load
        while True:
            try:
                choice = input("\nEnter save number to load (or press enter to return to main menu): ")
                if choice == "":
                    return None
                # If the user enters 1, it becomes 0 (the first file in the list: index[0]).
                choice = int(choice) - 1
                 # Check if the choice is within the valid range of save files 
                if 0 <= choice < len(save_files):
                    return save_files[choice]
                else:
                    print("Invalid save number. Please try again.")
            except ValueError: # To prevent program from crashing if input is not a valid integer 
                print("Please enter a valid number.")
        
    # Function to load the game state from a saved file
    def load_game_state(self):
        save_file = self.display_saved_games()
        if not save_file:
            return False
        
        save_path = os.path.join(self.save_directory, save_file)
        with open(save_path, 'r') as f:  # Open the save file in read mode
            data = json.load(f) 
            # Retrieve the saved game data 
            self.username = data.get("username", "Player")
            self.score = data.get("score", 0) #  If it doesn't exist, self.score is set to 6.
            self.current_category = data.get("current_category", "") # If it doesn't exist, self.score is set to empty string
            self.question_index = data.get("question_index", 0)  # If it doesn't exist, self.score is set to 0.
            self.lives = data.get("lives", 6) # If it doesn't exist, self.lives is set to 6.

            print(f"\n Loading game for {self.username}...")
            print(f"Category: {self.current_category}")
            print(f"Score: {self.score}")
            print(f"Lives: {self.lives}")
            input("\nPress Enter to continue...")
            return True
            
    # Function of main menu        
    def main_menu(self):
        # Displays the main menu and handles user input to start a game, load a game, view the leaderboard, or quit.
        while True:
            clear_screen()  # Clears the screen for a clean view
            print(main_menu_art)  
            print("1. Start New Game")
            print("2. Load Game")
            print("3. Show Leaderboard")
            print("4. Quit")

            choice = input("Select an option: ")

            # Handle each menu option
            if choice == "1":
                self.username = input("Enter your username: ")  # Prompt for the user's username
                self.start_new_game()  # Start a new game
            elif choice == "2":
                if self.load_game_state():  # Attempt to load saved game state
                    self.play_game()  # If successful, start playing the game
            elif choice == "3":
                self.display_leaderboard()  # Show the leaderboard
                input("\nPress Enter to return to the main menu.")  # Wait for the user to press Enter
            elif choice == "4":
                print("Goodbye!")  # Display a farewell message
                break  # Exit the loop, effectively quitting the game
            else:
                print("Invalid choice. Please try again.")  # If the input is invalid, prompt again
                time.sleep(2)

    # Function to display the leaderboard with the highest scores
    def display_leaderboard(self):
        clear_screen()
        if not os.path.exists(self.leaderboard_file):
            print(f"{GREEN}No leaderboard data available.{RESET}")
            return
        # Open and read the leaderboard data from the file
        with open(self.leaderboard_file, 'r') as f:
            leaderboard = json.load(f)

        if not leaderboard:
            print("Leaderboard is empty.")
            return
        # Initialize table data and headers
        headers = ["#", "USERNAME", "SCORE"]
        table_data = []

        # Populate the table data
        for i, entry in enumerate(leaderboard, start=1):
            username = entry.get("username", "Unknown")
            score = entry.get("score", "None")
            table_data.append([i, username, score])

        # Print the table using tabulate
        print(f"{GREEN}")
        print(tabulate(table_data, headers=headers, tablefmt="fancy_grid"))
        print(f"{RESET}")

        # Function to update the leaderboard with the player's score
    def update_leaderboard(self):
          
        if not self.username:
            print("Username not set. Cannot update leaderboard.")
            return
         # Check if the leaderboard file exists
        if os.path.exists(self.leaderboard_file):
            # Open and read the existing leaderboard data from the file
            with open(self.leaderboard_file, 'r') as f:
                leaderboard = json.load(f)
        else:
            # If the file doesn't exist, initialize an empty leaderboard
            leaderboard = []

        user_found = False
        for entry in leaderboard:
             # If the username matches, update the score with the higher of the two scores
            if entry["username"] == self.username:
                entry["score"] = max(entry["score"], self.score)
                user_found = True
                break
        # If the user is not found, add a new entry for the user with their score
        if not user_found:
            leaderboard.append({"username": self.username, "score": self.score})
        # Sort the leaderboard in descending order based on the score
        leaderboard = sorted(leaderboard, key=lambda x: x["score"], reverse=True)
        # Write the updated leaderboard back to the file
        with open(self.leaderboard_file, 'w') as f:
            json.dump(leaderboard, f)
        print("Leaderboard updated successfully!")

if __name__ == "__main__":
    game = GameState()  # Create an instance of GameState
    game.main_menu()  # Call the main menu to start the game 
