import utils

# The computer Mode
def computer_mode(player_name):
    """
    This function handles the computer mode round of the game.
    Parameter: 
        player_name: The name of the palyer playing with the computer.
    Returns:
        Player's score for the round.
    """

    max_num, total_attempts, multiplier = utils.difficulty_level()
    number = utils.computer_secret_num(max_num)

    print(f"\nHello {player_name}!")
    print(f"I am thinking of a number between 1 and {max_num}.")
    print(f"You have a maximum of {total_attempts} attempts to guess the number.")

    if number % 2 == 0:
        print("The number is an even number.")
    else:
        print("The number is an odd number.")

    attempts_used, round_score = utils.play_guessing_turn(player_name, number, max_num, total_attempts, multiplier)

    return round_score

# The 2 Player Mode
def two_player_mode(player1, player2):
    """
    This function handles the 2 player mode round of the game.

    Parameters:
        player1: The first player.
        player2: The second player.
    Round Structure:
        1. Player 1 enters the secret number.
        2. Player 2 guesses the secret number.
        3. Player 2 enters the secret number.
        4. Player 1 guesses the secret number.
        5. The round ends and their scores are compared to decide a winner.
    Returns:
        Player 1 score and player 2 score
    """
    max_num, total_attempts, multiplier = utils.difficulty_level()
    print(f"\nThe battle bigins: {player1} vs {player2}")
    print(f"The number must be between 1 and {max_num}.")
    print(f"Each player has {total_attempts} attempts.")

    # ==================================
    # PLAYER 1 SETS NUMBER
    # PLAYER 2 GUESSES
    # ==================================

    print("\n" + "=" * 40)
    print("PLAYER 1 → PLAYER 2")
    print("=" * 40)

    p1_secret = utils.get_secret_number(player1, player2, max_num)

    p2_attempts, p2_round_score = utils.play_guessing_turn(player2, p1_secret, max_num, total_attempts, multiplier)

    # ==================================
    # PLAYER 2 SETS NUMBER
    # PLAYER 1 GUESSES
    # ==================================

    print("\n" + "=" * 40)
    print("PLAYER 2 → PLAYER 1")
    print("=" * 40)

    p2_secret = utils.get_secret_number(player2, player1, max_num)

    p1_attempts, p1_round_score = utils.play_guessing_turn(player1, p2_secret, max_num, total_attempts, multiplier)

    # ==================================
    # ROUND RESULTS
    # ==================================

    print("\n" + "=" * 40)
    print("ROUND RESULTS")
    print("=" * 40)

    print(f"{player1}: {p1_round_score} points")
    print(f"{player2}: {p2_round_score} points")

    print(f"{player1} used {p1_attempts} attempt(s).")
    print(f"{player2} used {p2_attempts} attempt(s).")

    if p1_round_score > p2_round_score:
        print(f"\n{player1} wins the round")
    elif p1_round_score < p2_round_score:
        print(f"\n{player2} wins the round")
    else:
        print("\nThe round is a tie!")
    return p1_round_score, p2_round_score
# =========================
# MAIN GAME
# =========================

def main_game():
    print("WELCOME TO THE NUMBER GUESSING GAME!")

    # Select the game mode
    mode = utils.play_mode()

    if mode == "Computer Mode":
        player = utils.get_player_name()
        total_score = 0
        while True:
            round_score = computer_mode(player)

            total_score += round_score

            print(f"\nYour total score is {total_score}")

            print("\n" + "=" * 40)

            play_again = input("\nDo you want to play again? (y/n): ").strip().lower()

            if play_again not in ["y", "yes"]:
                print(f"\nYour final score is {total_score}")
                print("Thank you for playing. It is not goodbye but see you again")
                utils.update_leaderboard(player, total_score)
                break                                                            
    else:
        player1 = utils.get_player_name()
        player2 = utils.get_second_player_name(player1)

        player1_total_score = 0
        player2_total_score = 0

        round_number = 1

        while True:
            print("\n" + "=" * 40)
            print(f" Round {round_number}")
            print("=" * 40)

            p1_round_score, p2_round_score = two_player_mode(player1, player2)

            player1_total_score += p1_round_score
            player2_total_score += p2_round_score

            print("\n" + "=" * 40)
            print("TOTAL SCORES")
            print("=" * 40)

            print(f"{player1}: {player1_total_score}")
            print(f"{player2}: {player2_total_score}")

            round_number += 1

            play_again = input("Do you want to play again? (y/n): ").strip().lower()

            if play_again not in ['y', 'yes']:
                print("\n" + "=" * 40)
                print("FINAL RESULT")
                print("=" * 40)

                print(f"{player1}: {player1_total_score}")
                print(f"{player2}: {player2_total_score}")

                if player1_total_score > player2_total_score:
                    print(f"{player1} is the WINNER!!!")
                elif player1_total_score < player2_total_score:
                    print(f"{player2} is the WINNER!!!")
                else:
                    print("IT IS A TIE")
                
                print("\nThank you for playing. It is not goodbye but see you again")
                utils.update_leaderboard(player1, player1_total_score)
                utils.update_leaderboard(player2, player2_total_score)
                break
main_game()
