import random
def rock_paper_scissors():
    options = ["rock", "paper", "scissors"]
    print("Welcome to Rock, Paper, Scissors!")
    print("Enter your choice: rock, paper, or scissors.")
    while True:
        user_choice = input("Your choice: ").lower()
        if user_choice not in options:
            print("Invalid choice. Please try again.")
            continue
        computer_choice = random.choice(options)
        print(f"Computer chose: {computer_choice}")
        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            print("You win!")
        else:
            print("You lose!")
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break
    print("Thanks for playing!")
if __name__ == "__main__":
    rock_paper_scissors()