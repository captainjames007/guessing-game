import random

# Name: James
# Date: 11/5/2024

def start_game():
    play_again = 'y'  # Initial value to start the loop
    while play_again == 'y':
        # Generate a random number between 1 and 100
        secret_number = random.randint(1, 100)
        attempts = 0
        user_guess = None

        print("Welcome to the Guessing Game!")

        while user_guess != secret_number:
            user_guess = int(input("Guess a number between 1 and 100: "))
            attempts += 1

            if user_guess < secret_number:
                print("Your guess is too low! Have some faith!")
            elif user_guess > secret_number:
                print("Your guess is too high, simmer down now!")
            else:
                print(f"Correct! You've guessed the number in {attempts} attempts.")

        play_again = input("Would you like to guess another number (Y/N)? ").strip().lower()

    print("Thanks for playing!")

# Start the game
start_game()
