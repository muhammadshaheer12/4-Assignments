import random

def main():
    # Generate a random number between 0 and 99
    secret_number = random.randint(0, 99)
    
    print("I am thinking of a number between 0 and 99...")

    while True:
        # Get the user's guess and convert it to an integer
        guess = int(input("Enter a guess: "))
        
        if guess > secret_number:
            print("Your guess is too high\n")
        elif guess < secret_number:
            print("Your guess is too low\n")
        else:
            # User guessed the correct number
            print(f"Congrats! The number was: {secret_number}")
            break

if __name__ == "__main__":
    main()
