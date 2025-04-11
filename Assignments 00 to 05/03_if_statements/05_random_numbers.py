import random  
def main():
    # Loop 10 times to print 10 random numbers
    for _ in range(10):
        # Generate a random integer between 1 and 100 (inclusive)
        number = random.randint(1, 100)
        # Print the number followed by a space (end=" " keeps it on the same line)
        print(number, end=" ")

# Check if this script is being run directly (not imported as a module)
if __name__ == "__main__":
    # Call the main function to execute the program
    main()

