import random
from pathlib import Path
import getpass

EASY = {'max_num': 50, 'attempt': 10, 'multiplier': 100}
MEDIUM = {'max_num': 100, 'attempt': 7, 'multiplier': 150}
HARD = {'max_num': 200, 'attempt': 5, 'multiplier': 200}

# Validate the user input
def user_input(max_num):
    while True:
        try:
            guess = int(input("Enter your number: "))
            if 1 <= guess <= max_num:
                return guess
            else:
                print(f'Number out of range. Please select a number between 1 and {max_num}')
        except ValueError:
            print("This is not a valid number. Try again")

# Difficulty level selector
def difficulty_level():
    while True:
        print('\nSelect a difficulty level.')
        print('1. Easy (1 to 50, 10 attempts)')
        print('2. Medium (1 to 100, 7 attempts)')
        print('3. Hard (1 to 200, 5 attempts)')

        level = input('Choose your level (1, 2, or 3): ').strip()

        if level == '1':
            return EASY['max_num'], EASY['attempt'], EASY['multiplier']
        elif level == '2':
            return MEDIUM['max_num'], MEDIUM['attempt'], MEDIUM['multiplier']
        elif level == '3':
            return HARD['max_num'], HARD['attempt'], HARD['multiplier']

        print('Invalid Choice. Choose a valid level.(1, 2, or 3)')

# Score Calculator
def score(max_attempts, attempts_used, difficulty_multiplier):
    scores = (max_attempts - attempts_used + 1) * difficulty_multiplier
    return scores

# Play Mode Selector
def play_mode():
    while True: 
        print("\nSelect your mode of play.")
        print("[1] Computer Mode")
        print("[2] 2 Player Mode")

        mode = input('Choose your play mode (1 or 2): ').strip()

        if mode == '1':
            return "Computer Mode"
        elif mode == '2':
            return "2 Player Mode"

        print("Invalid Choice. Choose a valid player mode. (1 or 2)")

# Get the player secret number
def get_secret_number(num_setter, num_guesser, max_num):
    while True:
        print(f"\n{num_guesser} look away from the screen")

        number = getpass.getpass(f"{num_setter} enter your secret number (1 to {max_num}): ")

        try:
            number = int(number)

            if 1 <= number <= max_num:
                return number
            else:
                print(f"Number must be between 1 and {max_num}")
        except ValueError:
            print("This is not a valid number. Try again")

# The Guessing function for the 2 palyer mode
def play_guessing_turn(guesser_name, secret_number, max_num, total_attempts, multiplier):
    attempts = total_attempts
    correct_guess = False
    attempts_used = 0
    round_score = 0

    print(f"\n{guesser_name}, it is your turn to guess!")

    # the odd/even hint
    if secret_number % 2 == 0:
        print("Hint: The number is even.")
    else:
        print("Hint: The number is odd.")
        
    while attempts > 0:
    
        attempts_used = total_attempts - attempts + 1

        print(f"\nAttempt {attempts_used} out of {total_attempts}")

        guess = user_input(max_num)

        if guess == secret_number:
            print(f"\nCongratulations, {guesser_name}!\nYou guessed the correct number: {secret_number} at attempt {attempts_used}.")
        
            round_score = score(total_attempts, attempts_used, multiplier)

            print(f"You scored {round_score} points this turn.")

            correct_guess = True
            break

        attempts -= 1

        print(close_percentage(secret_number, guess))

        if attempts > 0:
            if guess < secret_number:
                print(f"{guess} is low, go higher.")
            else:
                print(f"{guess} is high, go lower.")

    if not correct_guess:
        print(f"\n{guesser_name}, you lost! You're out of attempts. The secret number was {secret_number}.")

    return attempts_used, round_score

# Computer secret number generator
def computer_secret_num(max_num):
    return random.randint(1, max_num)
        
# Check close percentage 
def close_percentage(secret_number, user_input):
    percentage = 100 - (abs(user_input - secret_number) * 100 / secret_number)
    res =  max(0, percentage)
    if res < 30 :
        return "you were very far from the secret number"
    elif res < 70 : 
        return "you were close to the secret number"
    else:
        return"you were very close to the secret number"

def get_leaderboard():
    file_path = Path("leaderboard.txt")

    if not file_path.is_file():
        return {}
    content = file_path.read_text(encoding="utf-8")
    lines = content.split('\n')
    leaderboard = {line.split(' - ')[0]: int(line.split(' - ')[1]) for line in lines if line != "" }

    return leaderboard

# Check if a player already exist in leaderboard
def player_exist(player):
    leaderboard = get_leaderboard()
    return player in leaderboard

# Get player name and check if it exists in leaderboard
def get_player_name():
    while True:
        player = input('\nEnter your name: ').strip().upper()

        if not player:
            print("Name cannot be empty.")
            continue

        if not player_exist(player):
            return player

        print(f"\n{player} already exists in the leaderboard")
        print("Are you the same person?")
        print("[1] Yes")
        print("[2] No")

        choice = input("Choose 1 or 2: ").strip()
        if choice == '1':
            return player
        elif choice == '2':
            print("Please enter a different name.")
            continue
        else:
            print("Invalid choice. Choose 1 or 2.")

#Get second player name for 2 player mode
def get_second_player_name(first_player):
    while True:
        player = get_player_name()

        if player.lower() == first_player.lower():
            print(f"{player} is already player 1.")
            print("Player 2 must have a different name.")
        else:
            return player
# update the leaderboard file 
def update_leaderboard(player, total_score):
    file_path = Path("leaderboard.txt")

    leaderboard = get_leaderboard()
     
    if player not in leaderboard:
        leaderboard[player] = total_score
    elif total_score > leaderboard[player]:
        leaderboard[player] = total_score
    sorted_lead = sorted(leaderboard.items(), key = lambda x: x[1], reverse = True)
    leaderboard_string = "\n".join([f"{key} - {value}" for key , value in sorted_lead])
    file_path.write_text(leaderboard_string + "\n", encoding="utf-8")
