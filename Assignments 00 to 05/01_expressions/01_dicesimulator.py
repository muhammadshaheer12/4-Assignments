import random

def roll_dice():
    # Local variables inside the function
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    return die1, die2

def main():
    # This loop runs the dice roll three times
    for i in range(1, 4):
        die1, die2 = roll_dice()
        print(f"Roll {i}: Die 1 = {die1}, Die 2 = {die2}")

# Run the main function
if __name__ == "__main__":
    main()
