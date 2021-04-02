import random

# Purpose: Just for fun
# Author: @mcg-cyber
# Licence: MIT

print("Welcome to Number Guessing Game!")


def main():
    print("Remember you have three guesses to guess the right number!")
    guess_count = 0
    guess = random.randint(1, 15)
    guess_limit = 3
    while True:
        try:
            number_to_guess = int(input("Enter your guessing number between 1-10: "))
            guess_count += 1
            if guess_limit == guess_count:
                print("Out of guess. Fuck off!")
                break
            if number_to_guess == guess:
                print(f"You guessed right, number was {number_to_guess}")
                break
            if number_to_guess < guess:
                print("Higher number is required")
            if number_to_guess > guess:
                print("Lower number is required")
            else:
                # print(f"Guess was {guess}, maybe next time!")
                pass

        except ValueError as error:
            print(f"Asshole! Enter integer not a string! {error}")


if __name__ == '__main__':
    main()
