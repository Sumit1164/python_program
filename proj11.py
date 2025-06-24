import random
def roll_dice():
    return random.randint(1, 6)
def dice_play():
    print("Welcome to the Dice Game!")
    print("Roll the dice and try to guess the number.")
    while True:
        guess = input("Enter your guess (1-6) or 'quit' to end the game: ")
        if guess.lower() == "quit":
            print("Thanks for playing!")
            break
        try:
            guess = int(guess)
            if guess < 1 or guess > 6:
                print("Invalid guess. Please enter a number between 1 and 6.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 6 or 'quit'.")
            continue
        dice_roll = roll_dice()
        print(f"The dice rolled: {dice_roll}")
        if guess == dice_roll:
            print("Congratulations! You guessed correctly.")
        else:
            print("Sorry, you guessed incorrectly.")
if __name__ == "__main__":
    dice_play()