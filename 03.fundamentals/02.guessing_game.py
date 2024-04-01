# Guessing game
# - Have a variable with a number between 1 and 20 for the user to guess. (you can research random package if you are feeling frisky).
# - Using a loop, ask your user for a number between 1 and 20 (with exception handling in case they enter a string).
# - Check user input against the number you have stored.
# - When they get it correctly show a success message and end the program.

# BONUS
# If you are feeling extra confident:
# - Track how many times the user has guessed.
# - Limit the number of guesses and end the program after the user has guessed too many times.
# - Display how many guesses the user took to get the correct answer.

secret_number = 12
player_guess = 0
guess_num = 0

while player_guess != secret_number:
    guess_num += 1
    while player_guess < 1 or player_guess > 20:
        player_guess = input(f"Enter an integer between 1 and 20: ")

        try:
            player_guess = int(player_guess)
        except TypeError:
            print(f'{player_guess} is not an integer between 1 and 20. Try again...')
        except:
            print(f'An error occured')

    if player_guess == secret_number:
        print(
            f'You got it right in {guess_num} tries! The number was {secret_number}')
    else:
        print(f'Sorry - try again...')
        player_guess = 0
