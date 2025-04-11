import random

NUM_ROUNDS = 5

def main():
    print("Welcome to the High-Low Game!")
    print('--------------------------------')

    # Initialize score
    your_score = 0

    # Milestone 4: Play multiple rounds
    for round_number in range(1, NUM_ROUNDS + 1):
        print(f"Round {round_number}")
        
        # Milestone 1: Generate random numbers for the player and the computer
        computer_num = random.randint(1, 100)
        your_num = random.randint(1, 100)
        
        print(f"Your number is {your_num}")
        
        # Milestone 2: Get user input for their guess
        choice = input("Do you think your number is higher or lower than the computer's?: ").lower()

        # Extension 1: Safeguard user input to ensure it's either 'higher' or 'lower'
        while choice not in ["higher", "lower"]:
            choice = input("Please enter either 'higher' or 'lower': ").lower()

        # Milestone 3: Check if the user's guess is correct
        if choice == "higher" and your_num > computer_num:
            print(f"You were right! The computer's number was {computer_num}")
            your_score += 1
        elif choice == "lower" and your_num < computer_num:
            print(f"You were right! The computer's number was {computer_num}")
            your_score += 1
        else:
            print(f"Aww, that's incorrect. The computer's number was {computer_num}")
        
        # Milestone 5: Print the score after each round
        print(f"Your score is now {your_score}\n")

    # Extension 2: Conditional ending messages based on performance
    print("Thanks for playing!")
    print(f"Your final score is {your_score}")

    if your_score == NUM_ROUNDS:
        print("Wow! You played perfectly!")
    elif your_score >= NUM_ROUNDS // 2:
        print("Good job, you played really well!")
    else:
        print("Better luck next time!")

if __name__ == "__main__":
    main()
