import random

def main():
    # Generate a random number between 0 and 99
    number_to_guess = random.randint(0, 99)
    
    # Start the guessing game
    print("I am thinking of a number between 0 and 99...")

    while True:
        # Ask the user for their guess
        guess = int(input("Enter a guess: "))
        
        # Check if the guess is correct, too high, or too low
        if guess < number_to_guess:
            print("Your guess is too low")
        elif guess > number_to_guess:
            print("Your guess is too high")
        else:
            print(f"Congrats! The number was: {number_to_guess}")
            break 

if __name__ == "__main__":
    main()
