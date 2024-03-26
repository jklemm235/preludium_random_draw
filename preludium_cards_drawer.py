import random
import argparse
import os
import platform
import sys

# Define a function to clear the terminal screen
def clear_terminal():
    """Clears the terminal screen."""
    # Check the operating system
    os_name = platform.system()
    if os_name == "Windows":
        os.system('cls')  # Clear terminal for Windows
    else:
        os.system('clear')  # Clear terminal for Unix/Linux/Mac

# Create an ArgumentParser object
parser = argparse.ArgumentParser(description='Command-line tool to get an integer')

# Add an argument for the integer value
parser.add_argument('num_players', type=int, help='Number of players')
parser.add_argument('num_cards_drawn', type=int, default=4, nargs='?',
                    help='Number of cards to draw')

# Parse the command-line arguments
args = parser.parse_args()

# Access the integer value
num_players = args.num_players
num_cards_drawn = args.num_cards_drawn

cards = dict()
with open("rawPreludium.txt", "r") as f:
    for line in f:
        card = line.split(":")
        cards[card[0]] = card[1].strip()

cardnames = list(cards.keys())
random.shuffle(cardnames)
if num_players*num_cards_drawn > len(cardnames):
    print(f"There are not enough cards: you want to draw {num_players} " +\
          f"players * {num_cards_drawn} = {num_players*num_cards_drawn} cards " +\
          f"but only {len(cardnames)} cards exist")
    exit()
idx = 0
while idx < num_players*num_cards_drawn:
    #input("Press Enter to get your cards")
    print("____________________________________________")
    print(f"Player {int(idx/num_cards_drawn + 1)} has the following cards:")
    for _ in range(num_cards_drawn):
        print(f"{cardnames[idx]}:\n\t{cards[cardnames[idx]]}")
        idx += 1
    #input("Press Enter to clear the terminal")
    #clear_terminal()
    
