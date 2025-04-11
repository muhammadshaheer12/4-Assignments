import random

def roll_dice():
    # Simulate rolling two dice
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    return die1, die2

def main():
    # Roll the dice
    die1, die2 = roll_dice()
    
    # Calculate the total of the dice
    total = die1 + die2
    
    # Print the results of the rolls and the total
    print(f"Roll 1: {die1}")
    print(f"Roll 2: {die2}")
    print(f"Total: {total}")

if __name__ == "__main__":
    main()
