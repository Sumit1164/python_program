import random
def guess_number_game():
    number_to_guess = random.randint(1, 100)
    number_of_guesses = 0
    max_guesses = 10
    print("Welcome to the Guess the Number Game!")
    print("I have selected a number between 1 and 100.")
    print(f"You have {max_guesses} attempts to guess it.")
    while number_of_guesses < max_guesses:
        guess = int(input("Enter your guess: "))
        number_of_guesses += 1

        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number in {number_of_guesses} attempts.")
            break
    else:
        print(f"Sorry, you've used all {max_guesses} attempts. The number was {number_to_guess}.")
if __name__ == "__main__":
    guess_number_game()